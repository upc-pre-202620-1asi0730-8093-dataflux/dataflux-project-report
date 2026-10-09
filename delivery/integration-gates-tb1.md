# Integración y cierre verificable de TB1

Estado comprobado el 8 de octubre de 2026. Los PR abiertos y pruebas locales no equivalen a una release publicada. Los commits de los compañeros se conservan; no se vuelve a subir el ZIP completo como contribución de Deiby.

## Orden de revisión

1. Revisar [Subscriptions #12](https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-webapp/pull/12) y [ajustes comunes #13](https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-webapp/pull/13). Ambos se dirigen a develop y solicitan revisión a V8Z5. El coordinador decide cuándo integrarlos.
2. Al combinar ambos, resolver `src/app/App.vue`: conservar `AppFooter`, `standalonePage`, salto al contenido, `main-content` y la navegación de Subscriptions exclusiva de `rental_company`. El parche [integration-app-navigation.patch](integration-app-navigation.patch) muestra la adaptación sobre el PR común, sin importar el módulo de negocio de forma directa. La combinación local pasó **77/77 tests** y build de **353 módulos**; no se publicó ni se mergeó esta combinación.
3. Inventory ya aparece en develop `119a9ee77080` con 22 archivos. Bruno debe completar o revisar `application/inventory.module.js`, `presentation/inventory-routes.js`, los endpoints de environment, datos de demo, claves de idioma y navegación. La composición descubre precisamente esos patrones; el build actual puede pasar porque sus vistas aún no se importan.
4. Revisar [Shared #10](https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-webapp/pull/10) y [Maintenance #11](https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-webapp/pull/11) con Miroslav. Dashboard utiliza Inventory/Rentals/Subscriptions sin verificar que existan. Maintenance no aporta su módulo/rutas, endpoints, traducciones ni colecciones del mock. Resolver la composición y evitar renderizar stores ausentes antes de afirmar que están integrados.
5. Confirmar el responsable de Rentals y publicar su aporte en su rama/PR. Sus rutas y puertos son necesarios para solicitudes, decisiones, entregas y devoluciones; no aparecen en la base remota comprobada. No atribuir a la versión publicada las pruebas del ZIP agregado local.

## Correcciones de operaciones para revisar

- **Devolución y mantenimiento:** `incident-reactivation-policy.js` no debe exigir que haya existido una incidencia artificial para reactivar el equipo. Debe exigir que no quede una incidencia bloqueante abierta, junto con las condiciones de mantenimiento/inspección. [integration-maintenance-reactivation.patch](integration-maintenance-reactivation.patch) conserva esa corrección local y sus nueve regresiones. `git apply --check` pasó contra el head `e04b8734` de PR11; las pruebas locales usan la composición del checkout agregado, aún ausente del PR. Miroslav revisa/aplica sobre su contexto, completa esa composición y verifica el recorrido integrado.
- **Alquileres y fallos HTTP:** la aprobación y entrega pueden dejar reserva huérfana, estados parciales o duplicados cuando el segundo write falla. La corrección local y sus regresiones se entregan para revisión en [integration-rentals-retries.md](integration-rentals-retries.md). Debe aplicarse sobre el aporte real de Rentals, con Inventory, antes de demostrar el recorrido. La compensación de una Fake API no promete transacciones ni idempotencia de producción.
- **Formato compartido:** Shared fija fechas/importes a `es-PE`; conciliar sus consumidores con el locale canónico al probar la demo EN/ES. Subscriptions incluye su propio formato probado.

## Publicación y evidencia

Revisar [landing #1](https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-website/pull/1), conservar su build SHA y configurar `VITE_FRONTEND_URL` con la dirección pública comprobada del frontend. La URL se incorpora al build; recompilar después de configurarla. La base `/dataflux-website/` corresponde a Pages; para raíz, `/`.

El compañero de despliegue publica la versión integrada. Probar desde otro navegador la recarga de rutas SPA, ambas cuentas ficticias, solicitudes/decisiones, entrega/devolución/mantenimiento y suscripción vencida. La API base debe ser accesible públicamente, sin depender del localhost del visitante. Guardar URLs, SHA, capturas y video que realmente correspondan a esa versión.

El Team Leader completa responsabilidades y cumplimiento reales en [performance-tb1.md](performance-tb1.md). El equipo aplica las correcciones del [guion de keynote](keynote-corrections-tb1.md), exporta PPTX/PDF y DOCX/PDF, graba la exposición con los cinco integrantes y verifica el acceso del docente. Estos documentos preparados no reemplazan sus exports ni el video. No se ha realizado merge, release, publicación de hosting ni entrega en Aula Virtual durante esta preparación.
