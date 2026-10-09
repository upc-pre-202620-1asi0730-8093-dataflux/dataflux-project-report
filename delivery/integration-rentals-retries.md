# Alquileres: recuperación de escrituras parciales en TB1

Corrección local lista para revisión del responsable de Rentals, 8 de octubre de 2026. No se ha publicado, mergeado ni desplegado este parche. Se probó en `work/frontend-integration`, rama `feature/tb1-frontend-integration`, sobre `9a720ae`. Ese agregado incorporó los módulos del ZIP `maquigest-webapp-1.0.0` en `e76afec`, conserva IAM/Profiles versionados y contiene la corrección de mantenimiento `aba0c12`. No equivale al aporte remoto de un integrante ni a una versión integrada en GitHub.

El archivo [integration-rentals-retries.patch](integration-rentals-retries.patch) contiene **12 archivos**: ocho modificados y cuatro nuevos. SHA-256: `794360ea33766289d51cc28aa1e7c42aed5340751ed1ddc18976c31601469d84`. No incluye cambios de Subscriptions, IAM, Profiles, Maintenance, Shared, vistas, traducciones, servidor, configuración, dependencias ni fixtures originales.

## Problema y resultado

| Severidad | Reproducción comprobada antes del cambio | Comportamiento corregido |
| --- | --- | --- |
| P1 | La reserva de disponibilidad se escribe; el POST de Rental responde 503. Queda el bloqueo sin alquiler y la aprobación se bloquea a sí misma al reintentar. | La reserva se correlaciona con `rentalRequestId`; un fallo confirmado libera exclusivamente esa reserva. Si la compensación falla, el siguiente intento reconoce la misma reserva. |
| P1 | Se crea Rental, pero falla la actualización de la solicitud. Quedan Rental y bloqueo con solicitud pendiente. | Se elimina exclusivamente el Rental confirmado de esa aprobación y después se libera la reserva. Si eliminarlo falla, se conserva el bloqueo y se advierte recuperación incompleta; el reintento reutiliza el Rental existente. |
| P1 | Se crea Delivery/Return, se cambia Rental y falla el PATCH final de Equipment. Estado parcial y registros duplicados al reintentar. | Equipment se actualiza primero, luego Rental y finalmente el registro. Un fallo confirmado compensa en orden inverso. Delivery y Return se reconocen por `rentalId`, sin otro POST si ya existe el registro equivalente. |
| P1 | El servidor escribe, pero la respuesta de éxito se sustituye por 503. Repetir sin comprobar duplica efectos. | Una lectura posterior verifica si quedó la escritura esperada. Si esa lectura falla, se informa resultado desconocido y se detiene la compensación; el reintento usa la correlación persistida y el estado fresco. |

Los guards de la store serializan confirmaciones simultáneas en la misma instancia. La recuperación relee solicitud, Rental, Equipment, disponibilidad e incidencias mediante APIs/ACL reales. Una reserva ajena, cambios de participantes/período/correlación, un estado incompatible o registros duplicados/conflictivos no se adivinan ni se sobrescriben como recuperación automática.

## Archivos y contrato mínimo

- `rentals/application/rental-operations.js`: orquestación con dependencias explícitas; compensaciones secuenciales. La primera compensación fallida detiene las restantes para no liberar equipo mientras podría seguir existiendo un Rental.
- `rentals/application/rentals.store.js`: usa esa orquestación, conserva `rentalRequestId` en las transiciones y evita doble confirmación pendiente.
- `rentals/infrastructure/rentals-api.js` y `rental-write-recovery.js`: creación reconocible por solicitud/alquiler, verificación tras respuesta fallida, recuperación de estado y eliminación limitada al Rental confirmado esperado. Se utilizan GET/POST/PUT/PATCH/DELETE ordinarios del mock.
- `rentals/infrastructure/inventory-equipment-operation-acl-adapter.js` y `equipment-operation.port.js`: recibos de reserva/estado, liberación exclusiva por identidad y período, restauración con lectura fresca y restricciones de incidencias.
- `rentals/domain/model/rental.entity.js` y `rental-assembler.js`: `rentalRequestId` opcional, entero positivo cuando existe. Los Rentals antiguos sin ese campo siguen deserializándose.
- `inventory/domain/model/availability-block.entity.js` y `infrastructure/equipment-assembler.js`: preservan el identificador opcional al leer y guardar Equipment. Es necesario para que una edición ordinaria de Inventory no borre la correlación de Rentals.
- `rentals/application/rentals.store.test.js` y `tests/rental-api-harness.js`: 34 regresiones con recursos ficticios en memoria. Solo se sustituye el transporte HTTP; entidades, APIs, ensambladores, store y ACLs de Rentals son los reales. IAM se configura como dependencia real del ACL, sin usar composición global ni cuentas reales.

Todas las rutas de esta lista parten de `src/app/`. El identificador añadido requiere preservar campos adicionales en los bloques de disponibilidad y recursos Rental. No añade un endpoint ni establece una restricción única en servidor.

## Aplicación y validación por el equipo

1. Integrar o revisar primero el aporte real de Rentals y su composición/rutas/puertos, junto con Inventory y las dependencias compartidas que necesita el módulo. El parche corrige operaciones; **no incorpora un contexto ausente ni su navegación**. Inventory remoto apareció en develop `119a9ee77080` durante esta preparación; revisar diferencias antes de aplicar y conservar los commits de Bruno.
2. En una rama local revisable del responsable del módulo, ejecutar `git apply --check <ruta>/integration-rentals-retries.patch`. Si hay conflicto, trasladar las modificaciones por responsabilidad; no reemplazar el módulo de un compañero con el ZIP ni aplicar a ciegas todo el agregado.
3. Tras revisión, aplicar con `git apply <ruta>/integration-rentals-retries.patch`. Se comprobó que el parche aplica sobre `9a720ae` mediante `git apply --cached --check` con un índice temporal. En el agregado corregido también pasó `git apply --reverse --check`. No se modificó el índice habitual ni se deshicieron cambios.
4. Ejecutar la regresión propia: `npm test -- src/app/rentals/application/rentals.store.test.js`.
5. Comprobar compatibilidad en una composición equivalente: `npm test -- src/app/rentals/application/rentals.store.test.js src/app/iam/application/iam.store.test.js src/app/profiles/application/profiles.store.test.js src/app/maintenance/application/incident.store.test.js`, después `npm run build` y `git diff --check`.
6. Una vez combinado el aporte verdadero, comprobar los recorridos en la UI de esa versión con cuentas ficticias y registrar su SHA. Estas pruebas locales no certifican automáticamente una release remota ni el cumplimiento visual/i18n.

## Evidencia local

- `evidence/tb1-rental-recovery-before.log`: antes del fix, el conjunto inicial de 16 casos produjo **13 fallos y 3 aciertos**. Reprodujo reservas huérfanas, Rental activo/equipo disponible y registros repetidos. Las posteriores regresiones ampliaron el conjunto a 34; no se atribuye el resultado de 16 al conjunto ampliado.
- `evidence/tb1-rental-recovery-compatibility.log`: resultado final **61/61** en cuatro archivos: 34 de Rentals, 18 existentes de IAM/Profiles y 9 de Maintenance.
- `evidence/tb1-rental-recovery-build.log`: build Vite correcto, **405 módulos**; `git diff --check` correcto.
- `evidence/tb1-rental-recovery-patch-check.log`: parche aplicable a la base agregada, comprobado con índice temporal aislado.
- `evidence/frontend-workflow-probe.mjs`: probe previo de stores/API/adaptadores que motivó los casos. No se escribieron servicios externos ni datos originales.

El agregado conserva un test antiguo no versionado de Subscriptions cuyo código corregido pertenece al PR separado #12. Por instrucción del coordinador no se alteró, incluyó ni eliminó ese test. Las 61 pruebas se ejecutaron con rutas explícitas; **no se afirma que el `npm test` general de este agregado desactualizado pase**. El equipo debe validar la suite general al combinar los módulos reales.

## Límites que deben aparecer en la demo

Es recuperación de una Fake API académica, sin transacción entre recursos, restricción única, ETag, bloqueo servidor, journal durable ni autorización real demostrada por estas pruebas. La verificación presupone lecturas inmediatas y consistentes del mock. El guard de la store evita duplicaciones de esa instancia; no garantiza exclusión entre pestañas, usuarios o procesos concurrentes.

Un cierre de pestaña, logout/cancelación mediante `takeUntil(sessionEnded)`, caída del proceso o pérdida de red durante la compensación puede dejar efectos parciales. El código avisa cuando observa una compensación fallida o no puede verificar una escritura, pero no detecta ni revierte automáticamente un proceso ya cerrado. Los reintentos de entrega/devolución probados conservan la selección original en la sesión; tras recargar, un Rental ya avanzado puede dejar de mostrar la acción anterior y requerir inspección manual del mock. La aprobación puede reconocer sus efectos por solicitud mientras esa solicitud siga disponible.

Los registros anteriores sin correlación, los datos duplicados/conflictivos y los cambios de otro actor requieren revisión; no se inventa su propietario. Reintentar un Delivery/Return con fecha o notas distintas no produce otro registro: se informa conflicto. El mensaje de recuperación incompleta pide inspección, no promete que todos los recursos hayan quedado sin cambios. Una implementación de producción deberá resolver autoridad, concurrencia, atomicidad e idempotencia en el backend correspondiente.
