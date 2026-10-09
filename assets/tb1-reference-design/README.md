# Reference product design

Recovered PlantUML sources preserve the team's product design and adapt its stack. See [COMPARISON.md](COMPARISON.md) for decisions and [reference-validation.json](reference-validation.json) for source traceability.

Render with PlantUML 1.2026.8 (standard C4 library included):

```sh
java -jar plantuml-1.2026.8.jar -charset UTF-8 -tsvg "assets/tb1-reference-design/*.puml"
java -jar plantuml-1.2026.8.jar -charset UTF-8 -tpng "assets/tb1-reference-design/*.puml"
```

C#/ASP.NET Core/EF Core/MySQL and external providers are proposed product design. TB1 uses Vue/JavaScript and a Node/json-server demo. The separately labelled JavaScript snapshot does not replace the backend design.
