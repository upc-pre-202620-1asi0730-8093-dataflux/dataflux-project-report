import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { execFileSync, spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { marked } = require('marked');
const [output, python = 'python'] = process.argv.slice(2);
if (!output) throw new Error('Usage: node tools/export-report.mjs <output.pdf> [python executable]');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = marked.parse(fs.readFileSync(path.join(root, 'README.md'), 'utf8'));
let sourceBase = '';
try {
  const remote = execFileSync('git', ['remote', 'get-url', 'origin'], { cwd: root, encoding: 'utf8' }).trim();
  const commit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: root, encoding: 'utf8' }).trim();
  const match = remote.match(/^(?:https:\/\/github\.com\/|git@github\.com:)([\w.-]+\/[\w.-]+?)(?:\.git)?$/);
  if (match && /^[a-f0-9]{40,64}$/.test(commit)) sourceBase = `https://github.com/${match[1]}/blob/${commit}/`;
} catch { /* A source archive can still export without repository links. */ }
const result = spawnSync(python, [path.join(root, 'tools/render_report.py'), root, path.resolve(output), sourceBase], {
  input: html, encoding: 'utf8', maxBuffer: 4 * 1024 * 1024,
});
process.stdout.write(result.stdout || '');
process.stderr.write(result.stderr || '');
if (result.error) throw result.error;
process.exitCode = result.status ?? 1;
