# Correcciones y guion para la exposición TB1

Presentación compartida: [DataFlux keynote TB1](https://canva.link/297wev0diny954j), 30 páginas. Se conserva el material del equipo. La copia compartida debe actualizarse antes de exportar PowerPoint/PDF y grabar; este archivo prepara texto y recorrido, no acredita esas exportaciones ni el video.

## Correcciones concretas

| Página o tema | Cambio que debe quedar en la presentación |
| --- | --- |
| 2, integrantes | Sustituir la quinta ficha de plantilla por la fotografía, nombre y carrera reales del integrante correspondiente. Contrastar los cinco nombres con la carátula del informe; no cambiar el orden sin acuerdo del equipo. |
| 3, cierre del problema | Usar la meta, plazo y medición de abajo. Presentarla como hipótesis del piloto, no como resultados alcanzados. |
| 4, propuesta | Usar **DataFlux** para el equipo y **RentBuild** para el producto. Retirar **MaquiGest** como nombre vigente. |
| Lean UX | Las siete hipótesis corresponden a las siete feature assumptions. Mostrar business outcome, usuarios, beneficio y feature; referenciar H01–H07 del informe. |
| Backlog | Conservar US01–US35 y TS01–TS09. Priorizar inventario/alquiler/disponibilidad y explicar autenticación como dependencia previa a publicar recursos privados. |
| Arquitectura | Frontend Vue/PrimeVue; API ASP.NET Core/EF Core/C# propuesta para AV2; Fake API identificada como simulación de TB1. Usar los suplementos actuales del informe y retirar etiquetas Angular/Spring/Java contradictorias. |
| Evidencia del sprint | Mostrar commits, PRs y capturas reales. Distinguir rama probada, PR pendiente, versión integrada y versión publicada. No presentar una URL localhost como despliegue público. |
| Colaboración | Usar los gráficos y cortes definidos en `collaboration-counts.json`; explicar que cuentan historia del informe y no califican a los integrantes. |

## Texto para el cierre medible de la página 3

Buscamos centralizar el inventario, la disponibilidad y las solicitudes de alquiler de empresas proveedoras y constructoras. Contrastaremos la propuesta durante los primeros seis meses de un piloto: al menos 20 empresas de alquiler con uso recurrente, 10 constructoras que completen búsqueda y solicitud, 50 equipos registrados y 30 reservas o alquileres, con menos de cinco conflictos de disponibilidad o duplicidades.

La recurrencia exige actividad en dos semanas distintas. Contaremos empresas y operaciones únicas, excluyendo cuentas y repeticiones de demostración. Estas son metas propuestas: aún faltan la fecha e instrumentos del piloto y no se afirma adopción lograda en TB1.

## Sustentación inicial de 12 minutos

| Tiempo | Tema | Evidencia que debe mostrar quien expone |
| --- | --- | --- |
| 00:00–01:00 | Equipo, problema y solución | Cinco integrantes; segmentos proveedor/constructora y cierre medible. |
| 01:00–03:40 | Mejoras respecto a AV1 | Problem Statement e hipótesis; TS y backlog; C4/EventStorming/Money/flujos corregidos. |
| 03:40–09:00 | Demostración | Versión integrada: registro/acceso por segmento, inventario, solicitudes y recorridos operativos que realmente funcionen, selección/cambio/renovación de plan y términos. Identificar los límites de la Fake API. |
| 09:00–12:00 | Trabajo del equipo y cierre | Cada integrante explica su responsabilidad, diff, pruebas y PR; versión publicada y pendientes reales. |

La distribución dedica menos del 10% a la introducción, menos del 30% a mejoras, más del 40% a demo y más del 20% a colaboración. El equipo asigna los turnos personales y practica; cada integrante debe poder explicar su propio aporte.

## Recorrido preparado para Subscriptions

1. Entrar con una cuenta ficticia de empresa de alquiler y abrir Plan y suscripción.
2. Comparar Esencial, Profesional y Crecimiento; cambiar idioma y señalar precio mensual en PEN.
3. Elegir un plan, mostrar confirmación, cancelar y volver a confirmar. La escritura se realiza en la Fake API; no hay cobro.
4. Cambiar un plan vigente y comprobar que conserva el periodo.
5. En una base de prueba, usar una suscripción vencida, recargar y contratar el mismo plan. Comprobar que comienza un nuevo mes válido.
6. Señalar que autoRenew es una preferencia guardada, sin renovación ni cobro programados. La cuenta constructora no muestra esta sección.

## Archivos y grabación

- Exportar `upc-pre-202620-1asi0730-8093-dataflux-keynote-tb1.pptx` y el PDF correspondiente, después de revisar las 30 páginas.
- Grabar a los cinco integrantes ante cámara con presentación y demostración, sin superar 30 minutos para el video.
- Preparar `upc-pre-202620-1asi0730-8093-dataflux-expo-tb1.mp4` y el enlace privado de Microsoft Stream accesible al docente; reproducir ambos.
- Conservar el comprobante de la carga en la actividad de TB1.
