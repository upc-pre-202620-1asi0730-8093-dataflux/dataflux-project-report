# RentBuild
<div align="center">

  <img src="assets/md-images-front/upc-logo.png" width="150px" />

  <p>Universidad Peruana de Ciencias Aplicadas</p>
  <p>Facultad de Ingeniería</p>
  <p>Carrera de Ingeniería de Software</p>

  <p>Ciclo académico 2026-20</p><br>

  <p><b>1ASI0730</b></p>
  <p><b>Aplicaciones Web</b></p>
  <p>NRC</p>
  <p><b>8093</b></p>
  <p><b>Informe de Trabajo Final</b></p>
  <p>Docente</p>
  <p><b>Bautista Ubillús, Efraín Ricardo</b></p>
  <p>Startup</p>
  <p><b>DataFlux</b></p><br>
  <p>Producto</p>
  <p><b>RentBuild</b></p>

</div>

<div align="center">
  <h3>Integrantes</h3>

  <table>
    <thead>
      <tr>
        <th>Código</th>
        <th>Apellidos y Nombres</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>U20211B198</td>
        <td>Cisneros Salas, Luis Angel</td>
      </tr>
      <tr>
        <td>U202410211</td>
        <td>Manosalva Tovar, Miroslav Oscar</td>
      </tr>
      <tr>
        <td>U202111529</td>
        <td>Montalvo Vásquez, Bruno Rodrigo</td>
      </tr>
      <tr>
        <td>U20211F962</td>
        <td>Vargas Manchinelli, Deiby Juan</td>
      </tr>
      <tr>
        <td>U2023228489</td>
        <td>Viza Quispe, Marlon Packard</td>
      </tr>
    </tbody>
  </table>
  <br>

  <p><b>Septiembre, 2026</b></p>

</div>

<div style="page-break-after: always;"></div>

## Registro de Versiones del Informe

| Versión | Fecha |  Autor   |                                                  Descripción de modificación                                                   |
| :-----: |:-----:|:--------:| :----------------------------------------------------------------------------------------------------------------------------: |
|   AV1   |       |  Todos   | Se agregó la primera versión del informe, incluyendo carátula, registro de versiones, perfiles del equipo, análisis inicial del problema, artefactos de UX, arquitectura preliminar y evidencias del Sprint 1. |

<div style="page-break-after: always;"></div>


## Project Report Collaboration Insights

A continuación, se presenta el repositorio utilizado para la elaboración colaborativa del informe del proyecto RentBuild.

#### Link del repositorio del Reporte:

- https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-project-report.git

### Entrega AV1:

#### Participación por integrante:

##### Commits en el Project Report:

<div style="page-break-after: always;"></div>

# Contenido

## Índice

- [Registro de Versiones del Informe](#registro-de-versiones-del-informe)
- [Project Report Collaboration Insights](#project-report-collaboration-insights)
- [Contenido](#contenido)
- [Student Outcome](#student-outcome)
- [Capítulo I: Introducción](#capítulo-i-introducción)
    - [1.1. Startup Profile](#11-startup-profile)
        - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
        - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
    - [1.2. Solution Profile](#12-solution-profile)
        - [1.2.1. Antecedentes y problemática](#121-antecedentes-y-problemática)
        - [1.2.2. Lean UX Process](#122-lean-ux-process)
            - [1.2.2.1. Lean UX Problem Statements](#1221-lean-ux-problem-statements)
            - [1.2.2.2. Lean UX Assumptions](#1222-lean-ux-assumptions)
            - [1.2.2.3. Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
            - [1.2.2.4. Lean UX Canvas](#1224-lean-ux-canvas)
    - [1.3. Segmentos objetivo](#13-segmentos-objetivo)
- [Capítulo II: Requirements Elicitation & Analysis](#capítulo-ii-requirements-elicitation--analysis)
    - [2.1. Competidores](#21-competidores)
        - [2.1.1. Análisis competitivo](#211-análisis-competitivo)
        - [2.1.2. Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
    - [2.2. Entrevistas](#22-entrevistas)
        - [2.2.1. Diseño de entrevistas](#221-diseño-de-entrevistas)
        - [2.2.2. Registro de entrevistas](#222-registro-de-entrevistas)
        - [2.2.3. Análisis de entrevistas](#223-análisis-de-entrevistas)
    - [2.3. Needfinding](#23-needfinding)
        - [2.3.1. User Personas](#231-user-personas)
        - [2.3.2. User Task Matrix](#232-user-task-matrix)
        - [2.3.3. User Journey Mapping](#233-user-journey-mapping)
        - [2.3.4. Empathy Mapping](#234-empathy-mapping)
    - [2.4. Big Picture Event Storming](#24-big-picture-event-storming)
    - [2.5. Ubiquitous Language](#25-ubiquitous-language)
- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
    - [3.1. User Stories](#31-user-stories)
    - [3.2. Impact Mapping](#32-impact-mapping)
    - [3.3. Product Backlog](#33-product-backlog)
- [Capítulo IV: Product Design](#capítulo-iv-product-design)
    - [4.1. Style Guidelines](#41-style-guidelines)
        - [4.1.1. General Style Guidelines](#411-general-style-guidelines)
        - [4.1.2. Web Style Guidelines](#412-web-style-guidelines)
    - [4.2. Information Architecture](#42-information-architecture)
        - [4.2.1. Organization Systems](#421-organization-systems)
        - [4.2.2. Labeling Systems](#422-labeling-systems)
        - [4.2.3. SEO Tags and Meta Tags](#423-seo-tags-and-meta-tags)
        - [4.2.4. Searching Systems](#424-searching-systems)
        - [4.2.5. Navigation Systems](#425-navigation-systems)
    - [4.3. Landing Page UI Design](#43-landing-page-ui-design)
        - [4.3.1. Landing Page Wireframe](#431-landing-page-wireframe)
        - [4.3.2. Landing Page Mock-up](#432-landing-page-mock-up)
    - [4.4. Web Applications UX/UI Design](#44-web-applications-uxui-design)
        - [4.4.1. Web Applications Wireframes](#441-web-applications-wireframes)
        - [4.4.2. Web Applications Wireflow Diagrams](#442-web-applications-wireflow-diagrams)
        - [4.4.3. Web Applications Mock-ups](#443-web-applications-mock-ups)
        - [4.4.4. Web Applications User Flow Diagrams](#444-web-applications-user-flow-diagrams)
    - [4.5. Web Applications Prototyping](#45-web-applications-prototyping)
    - [4.6. Domain-Driven Software Architecture](#46-domain-driven-software-architecture)
        - [4.6.1. Design-Level Event Storming](#461-design-level-event-storming)
        - [4.6.2. Software Architecture Context Diagram](#462-software-architecture-context-diagram)
        - [4.6.3. Software Architecture Container Diagrams](#463-software-architecture-container-diagrams)
        - [4.6.4. Software Architecture Components Diagrams](#464-software-architecture-components-diagrams)
    - [4.7. Software Object-Oriented Design](#47-software-object-oriented-design)
        - [4.7.1. Class Diagrams](#471-class-diagrams)
    - [4.8. Database Design](#48-database-design)
        - [4.8.1. Database Diagrams](#481-database-diagrams)
- [Capítulo V: Product Implementation, Validation & Deployment](#capítulo-v-product-implementation-validation--deployment)
    - [5.1. Software Configuration Management](#51-software-configuration-management)
        - [5.1.1. Software Development Environment Configuration](#511-software-development-environment-configuration)
        - [5.1.2. Source Code Management](#512-source-code-management)
        - [5.1.3. Source Code Style Guide & Conventions](#513-source-code-style-guide--conventions)
        - [5.1.4. Software Deployment Configuration](#514-software-deployment-configuration)
    - [5.2. Landing Page, Services & Applications Implementation](#52-landing-page-services--applications-implementation)
        - [5.2.1. Sprint 1](#521-sprint-1)
            - [5.2.1.1. Sprint Planning 1](#5211-sprint-planning-1)
            - [5.2.1.2. Aspect Leaders and Collaborators](#5212-aspect-leaders-and-collaborators)
            - [5.2.1.3. Sprint Backlog 1](#5213-sprint-backlog-1)
            - [5.2.1.4. Development Evidence for Sprint Review](#5214-development-evidence-for-sprint-review)
            - [5.2.1.5. Execution Evidence for Sprint Review](#5215-execution-evidence-for-sprint-review)
            - [5.2.1.6. Services Documentation Evidence for Sprint Review](#5216-services-documentation-evidence-for-sprint-review)
            - [5.2.1.7. Software Deployment Evidence for Sprint Review](#5217-software-deployment-evidence-for-sprint-review)
            - [5.2.1.8. Team Collaboration Insights during Sprint](#5218-team-collaboration-insights-during-sprint)
- [Conclusiones](#conclusiones)
    - [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
- [Video About-The-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)

<div style="page-break-after: always;"></div>

## Student Outcome

El curso contribuye al cumplimiento del Student Outcome ABET:  
**ABET - EAC - Student Outcome 5**

**Criterio:** *La capacidad de funcionar efectivamente en un equipo cuyos miembros
juntos proporcionan liderazgo, crean un entorno de colaboración e inclusivo,
establecen objetivos, planifican tareas y cumplen objetivos.*

En el siguiente cuadro se describe las acciones realizadas y enunciados de conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro del ABET - EAC - Student Outcome 5.

| Criterio específico                                                                                 | Acciones realizadas                                                                                                                                                                                            | Conclusiones |
|:----------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| **Trabaja en equipo para proporcionar liderazgo en forma conjunta.**                                | **Cisneros Salas, Luis Angel**<br>**AV1:**<br><br>**Manosalva Tovar, Miroslav Oscar**<br>**AV1:**<br><br>**Montalvo Vásquez, Bruno Rodrigo**<br>**AV1:**<br><br>**Vargas Manchinelli, Deiby Juan**<br>**AV1:**<br><br>**Viza Quispe, Marlon Packard**<br>**AV1:** | **AV1:**     |
| **Crea un entorno colaborativo e inclusivo, establece metas, planifica tareas y cumple objetivos.** | **Cisneros Salas, Luis Angel**<br>**AV1:**<br><br>**Manosalva Tovar, Miroslav Oscar**<br>**AV1:**<br><br>**Montalvo Vásquez, Bruno Rodrigo**<br>**AV1:**<br><br>**Vargas Manchinelli, Deiby Juan**<br>**AV1:**<br><br>**Viza Quispe, Marlon Packard**<br>**AV1:** | **AV1:**     |

<div style="page-break-after: always;"></div>

# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup

### 1.1.2. Perfiles de integrantes del equipo

|   Código   | Nombre completo del integrante  | Descripción de la carrera                                          |                                  Fotografía                                  | Conocimientos y habilidades                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:----------:|:--------------------------------| :----------------------------------------------------------------- |:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| U20211B198 | Cisneros Salas, Luis            | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |     <img src="assets/md-images-members/luis-angel.jpeg" width="150px" />     | Soy estudiante de Ingeniería de Software interesado en crear soluciones digitales que simplifiquen procesos y resuelvan problemas reales. Actualmente fortalezco mis conocimientos en C#, y cuento con experiencia en C++, Java, JavaScript, HTML y CSS. Me interesa especialmente el desarrollo frontend, las bases de datos y las aplicaciones web. Soy una persona organizada, responsable, de rápido aprendizaje y con facilidad para trabajar en equipo. Busco esta oportunidad para adquirir experiencia y seguir creciendo profesionalmente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| U202410211 | Manosalva Tovar, Miroslav       | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas | <img src="assets/md-images-members/miroslav-manosalva.jpeg" width="150px" /> | Soy Miroslav Manosalva Tovar, estudiante de Ingeniería de Software. Tengo conocimientos en el área de programación y experiencia en la elaboración de interfaces de usuario (UI), que puedo aportar al desarrollo de RentBuild. Mi experiencia trabajando con interfaces me permite contribuir a la presentación de la información y a la organización visual de las funcionalidades de la plataforma. Me considero una persona responsable y persistente: procuro cumplir con las actividades que asumo y mantener el esfuerzo cuando encuentro dificultades. En este proyecto, busco aplicar mis conocimientos de programación y diseño de interfaces, seguir fortaleciendo mi formación y contribuir al desarrollo de una solución útil para sus usuarios.                                                                                                                                                                                                                                                                 |
| U202111529 | Montalvo Vasquez, Bruno Rodrigo | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |   <img src="assets/md-images-members/bruno-montalvo.png" width="150px" />    | Soy Bruno Rodrigo Montalvo Vasquez, estudiante de la carrera de Ingeniería de Software. Me encuentro interesado y motivado por aprender nuevos temas relacionados con mi carrera. Asimismo, estoy abierto a trabajar con profesionales de mi área académica para mejorar mis conocimientos, adquirir experiencia y fortalecer mis habilidades de trabajo en equipo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| U20211F962 | Vargas Manchinelli, Deiby Juan  | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |    <img src="assets/md-images-members/deiby-vargas.jpeg" width="150px" />    | Estudio Ingeniería de Software y me apasiona usar la tecnología para convertir problemas en soluciones prácticas. Actualmente estoy aprendiendo y fortaleciendo mis conocimientos en C#, además de tener experiencia con C++, Java, JavaScript, HTML y CSS. Me interesa el frontend, las bases de datos y el desarrollo web. Soy organizado, aprendo rápido y disfruto trabajar en equipo. Mi objetivo es ganar experiencia, aprender y seguir creciendo en el mundo del software.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| U202322849 | Viza Quispe, Marlon Packard     | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |     <img src="assets/md-images-members/marlon-viza.jpg" width="150px" />     | Soy estudiante de Ingeniería de Software con interés en el desarrollo web, frontend y bases de datos. Tengo experiencia con C++, Java, JavaScript, HTML y CSS, y actualmente estoy fortaleciendo mis conocimientos en C#. Me motiva crear soluciones útiles y eficientes, aprender constantemente y enfrentar nuevos desafíos. Me considero una persona organizada, creativa y con buena capacidad para trabajar en equipo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## 1.2. Solution Profile

### 1.2.1. Antecedentes y problemática

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

#### 1.2.2.2. Lean UX Assumptions

#### 1.2.2.3. Lean UX Hypothesis Statements

#### 1.2.2.4. Lean UX Canvas

## 1.3. Segmentos objetivo

# Capítulo II: Requirements Elicitation & Analysis

## 2.1. Competidores

### 2.1.1. Análisis competitivo

<table style="text-align: center; width: 100%;">
  <tr>
    <th colspan="6">Competitive Analysis Landscape</th>
  </tr>

  <tr>
    <td colspan="2"><strong>¿Por qué llevar a cabo este análisis?</strong></td>
    <td colspan="4">
      Identificar oportunidades de diferenciación frente a soluciones existentes de alquiler de equipos y determinar cómo RentBuild puede ofrecer una solución más simple y especializada para PYMES del sector construcción.
    </td>
  </tr>

  <tr>
      <td colspan="2"><strong>Logotipos</strong></td>
      <td><img src="assets/md-images-chapter2/RentBuild-logo.png" alt="RentBuild" height="50"></td>
      <td><img src="assets/md-images-chapter2/RentBuild-Competidor_Booqable.png" alt="Booqable" height="50"></td>
      <td><img src="assets/md-images-chapter2/RentBuild-Competidor_Rentman.png" alt="Rentman" height="50"></td>
      <td><img src="assets/md-images-chapter2/RentBuild-Competidor_Odoo%20Rental.png" alt="Odoo Rental" height="50"></td>
  </tr>

  <tr>
    <td rowspan="2"><strong>Perfil</strong></td>
    <td><strong>Overview</strong></td>
    <td>RentBuild</td>
    <td>Booqable</td>
    <td>Rentman</td>
    <td>Odoo Rental</td>
  </tr>

  <tr>
    <td><strong>Ventaja Competitiva</strong></td>
    <td>Gestión del ciclo completo de la maquinaria, desde reserva y alquiler hasta devolución, inspección, mantenimiento y nueva disponibilidad.</td>
    <td>Facilidad para gestionar reservas, inventario y pedidos de alquiler desde una misma plataforma.</td>
    <td>Gestión avanzada de inventario, almacenes, disponibilidad, mantenimiento y trazabilidad de equipos.</td>
    <td>Integración con otros módulos como inventario, ventas, facturación y mantenimiento.</td>
  </tr>

  <tr>
    <td rowspan="2"><strong>Perfil de Marketing</strong></td>
    <td><strong>Mercado Objetivo</strong></td>
    <td>Pequeñas y medianas empresas de alquiler de maquinaria para construcción y pequeñas empresas constructoras.</td>
    <td>Empresas de alquiler de diferentes tamaños y sectores.</td>
    <td>Empresas de alquiler, eventos y organizaciones que administran grandes cantidades de equipos.</td>
    <td>Empresas de distintos sectores que necesitan integrar alquileres con otros procesos administrativos.</td>
  </tr>

  <tr>
    <td><strong>Estrategias de Marketing</strong></td>
    <td>Marketing B2B, publicidad digital dirigida al sector construcción, demostraciones, prueba inicial y contacto directo con empresas de alquiler.</td>
    <td>Promoción de digitalización del negocio de alquiler, reservas online y facilidad de administración.</td>
    <td>Promoción basada en eficiencia operativa, control de equipos y reducción de errores mediante automatización.</td>
    <td>Promoción mediante el ecosistema integrado de aplicaciones empresariales de Odoo.</td>
  </tr>

  <tr>
    <td rowspan="3"><strong>Perfil de Producto</strong></td>
    <td><strong>Productos y Servicios</strong></td>
    <td>Inventario, disponibilidad, reservas, contratos, pagos, entregas, devoluciones, incidencias, inspecciones y mantenimiento.</td>
    <td>Inventario, reservas, pedidos, contratos, facturación, pagos, recogidas y devoluciones.</td>
    <td>Inventario, planificación, almacenes, proyectos, códigos QR, reparaciones, mantenimiento y facturación.</td>
    <td>Reservas, alquileres, cotizaciones, facturación, recogidas y devoluciones, con integración a otros módulos.</td>
  </tr>

  <tr>
    <td><strong>Precios y Costos</strong></td>
    <td>Modelo SaaS con planes de suscripción escalables según las necesidades de las PYMES.</td>
    <td>Suscripción mensual o anual mediante diferentes planes.</td>
    <td>Suscripción según usuarios, módulos y funcionalidades utilizadas.</td>
    <td>Suscripción mediante planes y aplicaciones del ecosistema Odoo.</td>
  </tr>

  <tr>
    <td><strong>Canales de Distribución (Web y/o Móvil)</strong></td>
    <td>Plataforma web responsive accesible desde computadora, tablet o smartphone.</td>
    <td>Plataforma web y herramientas móviles para determinadas operaciones.</td>
    <td>Plataforma web y aplicación móvil.</td>
    <td>Plataforma web y aplicación móvil.</td>
  </tr>

  <tr>
    <td rowspan="4"><strong>Análisis SWOT</strong></td>
    <td><strong>Fortalezas</strong></td>
    <td>
      • Gestión integral del ciclo de alquiler.<br>
      • Control de disponibilidad y estado de equipos.<br>
      • Integración de alquiler y mantenimiento.<br>
      • Plataforma centralizada.
    </td>
    <td>
      • Gestión de inventario en tiempo real.<br>
      • Reservas y pagos online.<br>
      • Plataforma especializada en alquiler.<br>
      • Automatización de procesos.
    </td>
    <td>
      • Gestión avanzada de inventario.<br>
      • Seguimiento mediante QR.<br>
      • Control de múltiples almacenes.<br>
      • Gestión de reparaciones.
    </td>
    <td>
      • Amplio ecosistema ERP.<br>
      • Integración entre diferentes módulos.<br>
      • Alta capacidad de personalización.<br>
      • Gestión de alquiler y facturación.
    </td>
  </tr>

  <tr>
    <td><strong>Debilidades</strong></td>
    <td>
      • Marca nueva.<br>
      • Poco reconocimiento en el mercado.<br>
      • Menor cantidad de integraciones iniciales.<br>
      • Funcionalidades aún en crecimiento.
    </td>
    <td>
      • Solución general para diferentes tipos de alquiler.<br>
      • Algunas funciones dependen del plan contratado.<br>
      • Menor especialización en maquinaria.<br>
      • Dependencia de servicios en línea.
    </td>
    <td>
      • Mayor complejidad de uso.<br>
      • Curva de aprendizaje más alta.<br>
      • Funciones avanzadas pueden resultar innecesarias.<br>
      • Dependencia de módulos adicionales.
    </td>
    <td>
      • Configuración más compleja.<br>
      • Curva de aprendizaje elevada.<br>
      • Gran cantidad de módulos.<br>
      • Menor especialización en alquiler de maquinaria.
    </td>
  </tr>

  <tr>
    <td><strong>Oportunidades</strong></td>
    <td>
      • Incorporar nuevas automatizaciones.<br>
      • Integrar nuevas funcionalidades de mantenimiento.<br>
      • Ampliar integraciones con otros sistemas.<br>
      • Expandir la gestión hacia nuevos tipos de equipos.
    </td>
    <td>
      • Incorporar nuevas tecnologías de automatización.<br>
      • Expandir funcionalidades de gestión de activos.<br>
      • Mejorar integraciones externas.<br>
      • Ampliar servicios digitales de alquiler.
    </td>
    <td>
      • Fortalecer automatización del mantenimiento.<br>
      • Mejorar análisis de datos de equipos.<br>
      • Incorporar nuevas integraciones.<br>
      • Expandir funcionalidades de trazabilidad.
    </td>
    <td>
      • Ampliar su ecosistema de aplicaciones.<br>
      • Incorporar nuevas automatizaciones.<br>
      • Mejorar la integración entre módulos.<br>
      • Expandir funciones relacionadas con alquiler.
    </td>
  </tr>

  <tr>
    <td><strong>Amenazas</strong></td>
    <td>
      • Competidores internacionales consolidados.<br>
      • Aparición de nuevas plataformas especializadas.<br>
      • Evolución rápida de tecnologías de gestión.<br>
      • Competidores con mayor cantidad de integraciones.
    </td>
    <td>
      • Nuevas plataformas especializadas.<br>
      • Competidores con precios más bajos.<br>
      • Mayor competencia SaaS.<br>
      • Soluciones con mayor especialización.
    </td>
    <td>
      • Plataformas más simples.<br>
      • Nuevos competidores especializados.<br>
      • Alternativas con menores costos.<br>
      • Evolución tecnológica del sector.
    </td>
    <td>
      • Plataformas SaaS especializadas.<br>
      • Soluciones con implementación más rápida.<br>
      • Competidores con menor complejidad.<br>
      • Herramientas específicas para alquiler de equipos.
    </td>
  </tr>
</table>

### 2.1.2. Estrategias y tácticas frente a competidores

A partir del análisis competitivo, DataFlux aplicará estrategias para afrontar las fortalezas de sus competidores, aprovechar sus debilidades y responder a las oportunidades y amenazas del mercado.

#### Estrategia ofensiva: aprovechar la menor especialización de Booqable

Booqable posee una plataforma consolidada de alquiler, pero su enfoque es general para distintos tipos de equipos. RentBuild aprovechará esta menor especialización.

- **Gestión especializada:** integrar alquiler, devolución, incidencias y mantenimiento de maquinaria.
- **Control del equipo:** mantener actualizado el estado y disponibilidad de cada maquinaria.

#### Estrategia defensiva: responder a la gestión avanzada de Rentman

Rentman destaca por su gestión avanzada de inventario y equipos. RentBuild responderá con una plataforma más simple y enfocada.

- **Interfaz sencilla:** facilitar las operaciones principales con menos pasos.
- **Dashboard operativo:** visualizar rápidamente disponibilidad, alquileres y mantenimientos.

#### Estrategia competitiva: aprovechar la complejidad de Odoo Rental

Odoo Rental cuenta con un amplio ecosistema de módulos, pero su configuración puede resultar más compleja.

- **Enfoque específico:** concentrar las funciones necesarias para la gestión de alquiler de maquinaria.
- **Implementación simple:** reducir la dependencia de módulos y configuraciones adicionales.

#### Estrategia adaptativa: aprovechar oportunidades tecnológicas

RentBuild buscará fortalecer sus capacidades conforme evolucionen las necesidades del mercado.

- **Automatización:** incorporar alertas y seguimiento automático de equipos.
- **Integraciones:** añadir progresivamente servicios complementarios a la plataforma.

#### Estrategia defensiva frente a amenazas del mercado

La presencia de competidores consolidados y nuevas plataformas especializadas representa una amenaza para RentBuild.

- **Diferenciación:** reforzar la gestión integral del ciclo de alquiler como ventaja principal.
- **Mejora continua:** incorporar nuevas funcionalidades para mantener la competitividad de la plataforma.

## 2.2. Entrevistas

### 2.2.1. Diseño de entrevistas

**Segmento 1: Pequeñas y medianas empresas de alquiler de maquinaria**

**Objetivo:** Conocer cómo gestionan actualmente sus máquinas y alquileres, qué problemas enfrentan y qué tan útil podría resultarles una solución como RentBuild.

**Contexto**

1. ¿A qué se dedica actualmente su empresa y qué tipo de maquinaria suelen alquilar?

2. ¿Quién se encarga normalmente de gestionar los alquileres y las máquinas?

**Situación actual**

3. Cuando un cliente quiere alquilar una máquina, ¿cómo realizan normalmente todo el proceso?

4. ¿Cómo saben qué máquinas están disponibles, alquiladas o fuera de servicio?

5. ¿Qué herramientas utilizan actualmente para llevar el control de sus máquinas y alquileres?

**Problemas**

6. ¿Cuál es la principal dificultad que tienen al gestionar sus alquileres?

7. ¿Alguna vez han tenido problemas porque una máquina fue reservada para más de un cliente o no estaba disponible cuando debía estarlo?

8. ¿Qué ocurre cuando una máquina es devuelta con algún daño o presenta una falla?

9. ¿Cómo controlan actualmente los mantenimientos y cuándo una máquina puede volver a alquilarse?

10. ¿Qué parte del proceso de alquiler les toma más tiempo o les genera más problemas?

**Opinión sobre RentBuild**

> *"Estamos desarrollando RentBuild, una plataforma pensada para pequeñas y medianas empresas de alquiler de maquinaria. La idea es permitir gestionar las máquinas y alquileres desde un solo lugar, desde la reserva hasta la devolución y mantenimiento, de una manera sencilla."*

11. ¿Qué le parece esta idea? ¿Cree que podría ser útil para su empresa? ¿Por qué?

12. Si pudiera mejorar una sola parte de la gestión de sus alquileres, ¿cuál sería?


**Segmento 2: Pequeñas empresas constructoras**

**Objetivo:** Conocer cómo buscan y alquilan maquinaria actualmente, qué dificultades encuentran y qué tan útil podría resultarles RentBuild.

**Contexto**

1. ¿A qué tipo de proyectos de construcción o remodelación se dedica su empresa?

2. ¿Con qué frecuencia necesitan alquilar maquinaria o equipos?

**Situación actual**

3. Cuando necesitan una máquina para un proyecto, ¿cómo buscan actualmente dónde alquilarla?

4. ¿Cómo averiguan si una máquina está disponible para las fechas que necesitan?

5. ¿Qué información necesitan conocer antes de decidir alquilar una máquina?

**Problemas**

6. ¿Cuál es la principal dificultad que encuentran cuando necesitan conseguir maquinaria?

7. ¿Alguna vez han necesitado una máquina y no pudieron conseguirla cuando la necesitaban? ¿Qué ocurrió?

8. ¿Han tenido problemas con la entrega, el uso o la devolución de una máquina alquilada?

9. ¿Qué parte del proceso de conseguir y alquilar maquinaria les toma más tiempo?

10. ¿Qué cambiarían de la forma en que actualmente buscan o alquilan maquinaria?

**Opinión sobre RentBuild**

> *"Estamos desarrollando RentBuild, una plataforma pensada para facilitar el alquiler de maquinaria. La idea es que las empresas puedan buscar equipos, consultar información y disponibilidad y gestionar sus alquileres desde un solo lugar, de una manera sencilla."*

11. ¿Qué le parece esta idea? ¿Cree que podría ser útil para su empresa? ¿Por qué?

12. Si pudiera encontrar toda la información de una máquina en un solo lugar, ¿qué información sería indispensable para usted?

### 2.2.2. Registro de entrevistas

### Entrevista 1 — Pedro González

| Campo | Detalle |
|-------|---------|
| Nombres y apellidos | Pedro González |
| Edad | 27 años |
| Distrito | Villa El Salvador |
| Segmento objetivo | Primer segmento objetivo: Pequeñas y medianas empresas de alquiler de maquinaria |
| Fecha de entrevista | 18 setiembre 2026 |
| Duración | 02:48 |
| Timing en el video | 00:00 - 02:48 |
| URL del video | [Ver video](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202111529_upc_edu_pe/IQBFiR1QwYfTSL96qzfO9KaTATUN322TsrAuqI6OxMv3ymk?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=FaBBc3)|

<p align="center">
  <img src="assets/md-images-chapter2/Cap2entrevista1.png" width="700">
</p>

**Resumen:**  
Pedro González se desempeña como contratista en el rubro de alquiler de maquinaria pesada (tractores, camiones y mezcladoras). Su gestión la realiza de forma manual y mediante correos electrónicos. Mantiene el control de la disponibilidad y el estado de sus equipos a través de documentación física y papeles, lo que dificulta el seguimiento constante y puede ocasionar el traspapeleo de registros importantes. Confirmó haber tenido inconvenientes debido a la falta de trazabilidad en las reservas. Cuando una maquinaria es devuelta con fallas o daños, aplican penalidades previamente pactadas. Para el control de salidas y mantenimientos, realizan una inspección previa con fotografías y escaneo preventivo antes de liberar la máquina. Identifica que la etapa más crítica y propensa a problemas es el registro de retorno de los equipos por mal uso o daños no reportados. Mostró gran interés en la propuesta de RentBuild, destacando que una solución web centralizada agilizaría considerablemente sus procesos y reduciría la dependencia de documentos físicos, siendo el módulo de registro de entrada y salida de equipos la función que más valoraría.

### Entrevista 2 — Carlos Rodríguez

| Campo | Detalle |
|-------|---------|
| Nombres y apellidos | Carlos Rodríguez |
| Edad | 51 años |
| Distrito | San Juan de Miraflores |
| Segmento objetivo | Primer segmento objetivo: Pequeñas y medianas empresas de alquiler de maquinaria |
| Fecha de entrevista | 18 setiembre 2026 |
| Duración | 04:34 |
| Timing en el video | 02:49 - 07:23 |
| URL del video | [Ver video](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202111529_upc_edu_pe/IQBFiR1QwYfTSL96qzfO9KaTATUN322TsrAuqI6OxMv3ymk?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=FaBBc3)|

<p align="center">
  <img src="assets/md-images-chapter2/Cap2entrevista2.png" width="700">
</p>

**Resumen:**  
Carlos Rodríguez es técnico mecánico y también se dedica al alquiler de camiones de carga. Gestiona los alquileres y el control de las unidades de manera directa e informal junto a su esposa, utilizando únicamente un cuaderno de apuntes para registrar las fechas de retorno, mantenimiento y disponibilidad. Esta falta de un sistema centralizado les ha ocasionado problemas frecuentes como duplicidad de reservas, vehículos parados por falta de fluidez en la demanda y complicaciones cuando una unidad presenta fallas técnicas en ruta. Respecto a la propuesta del aplicativo, mostró una valoración positiva destacando que permitiría automatizar el proceso, evitar errores en los apuntes manuales y optimizar significativamente los tiempos de gestión de su negocio.

### Entrevista 3 — Carmen Losada Paredes

| Campo | Detalle |
|-------|---------|
| Nombres y apellidos | Carmen Losada Paredes |
| Edad | 51 años |
| Distrito | San Juan de Lurigancho |
| Segmento objetivo | Primer segmento objetivo: Pequeñas y medianas empresas de alquiler de maquinaria |
| Fecha de entrevista | 18 setiembre 2026 |
| Duración | 03:13 |
| Timing en el video | 07:24 - 10:38 |
| URL del video | [Ver video](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202111529_upc_edu_pe/IQBFiR1QwYfTSL96qzfO9KaTATUN322TsrAuqI6OxMv3ymk?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=FaBBc3)|

<p align="center">
  <img src="assets/md-images-chapter2/Cap2entrevista3.png" width="700">
</p>

**Resumen:**  
Carmen Losada Paredes administra una pequeña empresa dedicada al alquiler de camiones concreteros (mixers). Gestiona el negocio de manera directa a través de redes sociales para la captación de clientes y utiliza una base de datos en Excel como única herramienta para controlar la disponibilidad de las unidades y los mantenimientos. La falta de una herramienta centralizada y automatizada le ha generado problemas de duplicidad de reservas, alquilando la misma máquina a dos clientes distintos en una misma fecha. Además, considera que el trámite administrativo actual es bastante pesado y tedioso. Respecto a la propuesta del aplicativo, mostró una recepción positiva, destacando que le permitiría agilizar los procesos de tramitación, evitar errores en las reservas y lograr una mayor rotación en el alquiler de sus equipos.

### Entrevista 4 — Yovani Meléndez Zuleta

| Campo | Detalle |
|-------|---------|
| Nombres y apellidos | Yovani Meléndez Zuleta |
| Edad | 49 años |
| Distrito | San Juan de Lurigancho |
| Segmento objetivo | Segundo segmento objetivo: Pequeñas empresas constructoras |
| Fecha de entrevista | 18 setiembre 2026 |
| Duración | 04:22 |
| Timing en el video | 10:39 - 14:59 |
| URL del video | [Ver video](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202111529_upc_edu_pe/IQBFiR1QwYfTSL96qzfO9KaTATUN322TsrAuqI6OxMv3ymk?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=FaBBc3)|

<p align="center">
  <img src="assets/md-images-chapter2/Cap2entrevista4.png" width="700">
</p>

**Resumen:**  
Yovani Meléndez Zuleta es administrador de maquinaria en una empresa dedicada a la ejecución de obras públicas y privadas, principalmente enfocado en áreas verdes, parques y pistas. Requiere alquilar maquinaria con alta frecuencia y actualmente recurre a anuncios en internet, avisos publicitarios y coordinación directa telefónica para ubicar proveedores. Su principal problema radica en la pérdida de tiempo durante la búsqueda y la falta de disponibilidad oportuna de equipos en buen estado técnico. Destaca la recepción positiva hacia la propuesta de la plataforma, manifestando que centralizar la disponibilidad e información en un solo lugar les permitirá optimizar tiempos de gestión y agilizar la contratación de las máquinas para sus obras.

### Entrevista 5 — Sonia Gutiérrez

| Campo | Detalle |
|-------|---------|
| Nombres y apellidos | Sonia Gutiérrez |
| Edad | 41 años |
| Distrito | San Juan de Miraflores |
| Segmento objetivo | Segundo segmento objetivo: Pequeñas empresas constructoras |
| Fecha de entrevista | 18 setiembre 2026 |
| Duración | 03:33 |
| Timing en el video | 14:59 - 18:32 |
| URL del video | [Ver video](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202111529_upc_edu_pe/IQBFiR1QwYfTSL96qzfO9KaTATUN322TsrAuqI6OxMv3ymk?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=FaBBc3)|

<p align="center">
  <img src="assets/md-images-chapter2/Cap2entrevista5.png" width="700">
</p>

**Resumen:**  
Sonia Gutiérrez trabaja en una empresa inmobiliaria ubicada en San Juan de Miraflores y requieren alquilar maquinaria o equipos de construcción aproximadamente cada 15 días. Actualmente, cuando necesitan equipos para sus proyectos u obras inmobiliarias, buscan proveedores navegando por internet y se comunican directamente con ellos para consultar precios y disponibilidad. Mencionó que han enfrentado problemas como la cancelación o falta de disponibilidad a última hora por parte de proveedores que ya habían confirmado el alquiler. Además, señala que el proceso actual de buscar y comparar proveedores uno por uno les consume bastante tiempo. Mostró una recepción muy positiva hacia la propuesta de la plataforma centralizada, destacando que les facilitaría encontrar en un solo lugar la oferta disponible, la capacidad/carga técnica de las máquinas y los precios, agilizando considerablemente su gestión.

### Entrevista 6 — Ana Rivera Quispe

| Campo | Detalle |
|-------|---------|
| Nombres y apellidos | Ana Rivera Quispe |
| Edad | 36 años |
| Distrito | Los Olivos |
| Segmento objetivo | Segundo segmento objetivo: Pequeñas empresas constructoras |
| Fecha de entrevista | 18 setiembre 2026 |
| Duración | 02:50 |
| Timing en el video | 18:33 - 21:22 |
| URL del video | [Ver video](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202111529_upc_edu_pe/IQBFiR1QwYfTSL96qzfO9KaTATUN322TsrAuqI6OxMv3ymk?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=FaBBc3)|

<p align="center">
  <img src="assets/md-images-chapter2/Cap2entrevista6.png" width="700">
</p>

**Resumen:**  
Ana Rivera Quispe se dedica a la administración de pequeñas empresas dedicadas a la construcción de pequeños edificios, departamentos y casas. Requieren alquilar maquinaria con mucha frecuencia debido a la demanda de sus obras. Actualmente, buscan proveedores principalmente mediante redes sociales por ser un canal más rápido y confirman la disponibilidad conversando directamente con la persona encargada. La principal condición que evalúan antes de alquilar es que las máquinas se encuentren en buenas condiciones de operatividad. Señala que el mayor obstáculo y la parte que les toma más tiempo en todo el proceso es lograr comunicarse y conversar directamente con la persona indicada o el propietario de la máquina. Valora de forma positiva la propuesta del aplicativo centralizado, destacando que les permitiría encontrar los equipos adecuados de manera mucho más rápida.

### 2.2.3. Análisis de entrevistas

## 2.3. Needfinding

### 2.3.1. User Personas

El user persona se construyó a partir de patrones encontrados en las entrevistas.

**Segmento objetivo 1: Pequeñas y medianas empresas de alquiler de maquinaria**
![User Persona 1](./assets/md-images-chapter2/user-persona-armando-casas.png)

**Segmento Objetivo 2: Pequeñas empresas constructoras**
![User Persona 2](./assets/md-images-chapter2/user-persona-andrea-torres.png)

### 2.3.2. User Task Matrix

En esta sección se presenta el User Task Matrix, que concentra las tareas que realizan Marisol Vega Torres (Segmento 1 — Empresas de Alquiler) y Jorge Ramírez Delgado (Segmento 2 — Empresas Constructoras) para cumplir sus objetivos, independientemente de la existencia de una solución de software. Se considera para cada tarea su frecuencia (qué tan seguido la realiza) y su importancia (qué tan crítica es para su rol), en una escala de Baja / Media / Alta.

| Tarea | Marisol Vega Torres — Frecuencia | Marisol Vega Torres — Importancia | Jorge Ramírez Delgado — Frecuencia | Jorge Ramírez Delgado — Importancia |
| :--- | :---: | :---: | :---: | :---: |
| Verificar disponibilidad de equipo | Alta | Alta | Alta | Alta |
| Registrar/actualizar inventario de equipos | Alta | Alta | — | — |
| Gestionar reservaciones de clientes | Alta | Alta | — | — |
| Buscar y comparar proveedores de alquiler | — | — | Alta | Alta |
| Coordinar entrega y recojo de equipo | Alta | Alta | Media | Alta |
| Revisar condiciones y costos de alquiler | Media | Alta | Alta | Alta |
| Elaborar y firmar contratos de alquiler | Media | Alta | Media | Media |
| Dar seguimiento a fechas de devolución | Alta | Alta | Alta | Alta |
| Registrar incidentes o daños del equipo | Media | Alta | Media | Media |
| Programar mantenimiento preventivo | Media | Alta | — | — |
| Comunicarse con proveedores/clientes vía teléfono o WhatsApp | Alta | Media | Alta | Alta |
| Reportar avance de gastos/costos de alquiler a su empresa | Media | Media | Media | Alta |

Del análisis del cuadro se observa que las tareas con mayor frecuencia e importancia para ambos segmentos son verificar disponibilidad de equipo y dar seguimiento a fechas de devolución, lo que confirma que la visibilidad en tiempo real del estado del inventario es una necesidad crítica compartida. Marisol dedica más tiempo a tareas internas de gestión (inventario, mantenimiento, contratos), mientras que Jorge se enfoca en tareas de búsqueda y coordinación externa (comparar proveedores, coordinar entregas). Ambos coinciden en la alta dependencia de canales informales como el teléfono y WhatsApp para comunicarse, lo que representa una oportunidad clara para una solución digital centralizada.

Las principales diferencias se encuentran en las tareas asociadas a la responsabilidad de cada segmento. Armando realiza actividades relacionadas con la administración del inventario, el registro de maquinaria, las devoluciones y el mantenimiento, debido a que la empresa de alquiler es responsable de gestionar los equipos. En cambio, Andrea se enfoca en localizar maquinaria adecuada, consultar sus condiciones y realizar solicitudes de alquiler según las necesidades de sus proyectos. Por esta razón, determinadas tareas se identifican como N/A para alguno de los User Personas, ya que no forman parte de sus responsabilidades dentro de la plataforma.


### 2.3.3. User Journey Mapping

El User Journey Mapping permite representar de manera integral la experiencia de los principales usuarios de RentBuild a lo largo del proceso de alquiler de maquinaria y equipos para pequeñas construcciones. El recorrido end-to-end que se pretende ilustrar comprende las distintas etapas que atraviesan la Persona Alquiler y la Persona Constructora, desde la identificación de una necesidad y la búsqueda o gestión de un equipo, hasta la reservación, formalización del alquiler, entrega, utilización y posterior devolución de la maquinaria. A través de este recorrido se busca identificar las acciones, necesidades, expectativas y principales dificultades que experimentan ambos segmentos, con el propósito de reconocer oportunidades de mejora que puedan ser abordadas mediante las funcionalidades propuestas en RentBuild.

**1. User Journey Map - Pequeñas y medianas empresas de alquiler de maquinaria**

![User Journey Map](./assets/md-images-chapter2/user-journey-map1.png)

**2. User Journey Map para el segundo segmento**

![User Journey Map](./assets/md-images-chapter2/user-journey-map2.png)

### 2.3.4. Empathy Mapping

El Empathy Mapping permite profundizar en la comprensión de los principales segmentos de usuarios de RentBuild mediante la identificación de sus pensamientos, sentimientos, comportamientos, necesidades y dificultades. Para la elaboración de este artefacto se tomó como referencia la información definida previamente en las User Personas, analizando lo que cada usuario piensa y siente, dice y hace, observa y escucha dentro de su contexto. Asimismo, se identificaron sus principales frustraciones y los beneficios que esperan obtener durante el proceso de alquiler y gestión de maquinaria. Este análisis permite representar de forma estructurada la perspectiva de la Persona Alquiler y la Persona Constructora, facilitando la identificación de necesidades y oportunidades que pueden ser atendidas mediante la solución propuesta.

**1. Empathy Map - Pequeñas y medianas empresas de alquiler de maquinaria**

![Empathy Map](./assets/md-images-chapter2/empathy-map1.png)

**2. Empathy Map - Pequeñas empresas constructoras**

![Empathy Map](./assets/md-images-chapter2/empathy-map2.png)

## 2.4. Big Picture Event Storming

El Big Picture Event Storming permitió identificar y representar los principales eventos del dominio de RentBuild, mostrando de manera general el flujo del negocio desde el registro de la maquinaria hasta su devolución, inspección y mantenimiento.

La siguiente imagen presenta el resultado del Big Picture Event Storming realizado para el proyecto:

![Big Picture Event Storming de RentBuild](assets/md-images-chapter2/big-picture-event-storming.png)

## 2.5. Ubiquitous Language

En esta sección se presenta el glosario de términos y conceptos utilizados en el dominio del negocio de RentBuild, con el objetivo de establecer un lenguaje común, sin ambigüedades, entre todos los miembros del equipo y stakeholders del proyecto. Mantener un Ubiquitous Language actualizado permite que la comunicación entre las áreas de negocio y desarrollo sea clara y consistente a lo largo de todo el ciclo de vida del producto. Eric Evans, en su libro *Domain-Driven Design: Tackling Complexity in the Heart of Software*, establece que el Ubiquitous Language debe modelarse dentro de un Bounded Context, donde los términos y conceptos del dominio del negocio son identificados y no deben presentar ambigüedad.

| Término | Definición |
| :--- | :--- |
| Equipo | Maquinaria o herramienta perteneciente al inventario de una empresa de alquiler, disponible para ser rentada por un periodo determinado (ej. andamios, mezcladoras, plataformas elevadoras, generadores). |
| Empresa de Alquiler | Empresa propietaria del equipo, responsable de administrar su inventario, disponibilidad, reservaciones y mantenimiento dentro de la plataforma. |
| Empresa Constructora | Empresa que busca y solicita el alquiler de equipos para el desarrollo de sus proyectos de construcción. |
| Inventario | Conjunto de equipos registrados por una empresa de alquiler, junto con sus características, estado y ubicación. |
| Disponibilidad | Estado que indica si un equipo puede ser reservado o alquilado en una fecha determinada, sin superposición con otra reservación o alquiler activo. |
| Reservación | Solicitud realizada por una empresa constructora para apartar un equipo durante un periodo específico, antes de confirmarse como un alquiler formal. |
| Contrato de Alquiler | Documento que formaliza las condiciones del alquiler de un equipo, incluyendo tarifas, plazos, responsabilidades y condiciones de devolución. |
| Entrega | Proceso mediante el cual el equipo alquilado es trasladado o puesto a disposición de la empresa constructora en el lugar acordado. |
| Devolución | Proceso mediante el cual el equipo alquilado es devuelto a la empresa de alquiler al finalizar el periodo de alquiler. |
| Mantenimiento | Conjunto de actividades de inspección, reparación o servicio preventivo realizadas sobre un equipo para garantizar su correcto funcionamiento y disponibilidad. |
| Incidencia | Registro de un daño, falla o problema detectado en un equipo, ya sea durante su uso, entrega o devolución. |
| Estado del Equipo | Condición actual de un equipo dentro del inventario: disponible, alquilado o en mantenimiento. |
| Período de Alquiler | Rango de fechas durante el cual un equipo se encuentra reservado o alquilado por una empresa constructora. |
| Tarifa | Costo asociado al alquiler de un equipo, generalmente calculado por día, semana o periodo acordado. |
| Operador de Alquiler | Colaborador de una empresa de alquiler responsable de gestionar las reservaciones, contratos, entregas, devoluciones e incidencias del equipo. |
| Jefe de Obra | Responsable dentro de una empresa constructora encargado de identificar, solicitar y coordinar el alquiler de equipo necesario para su proyecto. |
| Perfil de Proveedor | Información pública de una empresa de alquiler visible para las empresas constructoras, incluyendo su historial de cumplimiento y equipo disponible. |

# Capítulo III: Requirements Specification

## 3.1. User Stories

<table>
<tr>
<th>Epic / Story ID</th>
<th>Título</th>
<th>Descripción</th>
<th>Criterios de Aceptación</th>
<th>Relacionado con</th>
</tr>

<tr>
<td>EP01</td>
<td>Gestión de usuarios y acceso</td>
<td>Epic orientado al registro, autenticación y gestión básica de las cuentas de los usuarios de RentBuild.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US01</td>
<td>Registro de usuario</td>
<td>Como usuario, quiero registrarme en RentBuild para acceder a las funcionalidades de la plataforma.</td>
<td>
Given que el usuario accede al formulario de registro<br>
When ingresa sus datos correctamente<br>
Then el sistema crea su cuenta<br>
And muestra un mensaje de confirmación
</td>
<td>EP01</td>
</tr>

<tr>
<td>US02</td>
<td>Inicio de sesión</td>
<td>Como usuario registrado, quiero iniciar sesión para acceder a las funcionalidades correspondientes a mi cuenta.</td>
<td>
Given que el usuario posee una cuenta registrada<br>
When ingresa credenciales válidas<br>
Then el sistema permite el acceso a la plataforma
</td>
<td>EP01</td>
</tr>

<tr>
<td>US03</td>
<td>Gestionar perfil</td>
<td>Como usuario, quiero consultar y actualizar mis datos personales y de contacto para mantener mi información actualizada.</td>
<td>
Given que el usuario ha iniciado sesión<br>
When modifica sus datos de perfil<br>
Then el sistema guarda la información actualizada<br>
And muestra los nuevos datos
</td>
<td>EP01</td>
</tr>

<tr>
<td>US04</td>
<td>Recuperar contraseña</td>
<td>Como usuario, quiero recuperar mi contraseña para volver a acceder a mi cuenta.</td>
<td>
Given que el usuario solicita recuperación<br>
When ingresa su correo<br>
Then el sistema envía instrucciones de recuperación
</td>
<td>EP01</td>
</tr>

<tr>
<td>US05</td>
<td>Cerrar sesión</td>
<td>Como usuario, quiero cerrar sesión para proteger mi cuenta.</td>
<td>
Given que el usuario está autenticado<br>
When selecciona cerrar sesión<br>
Then el sistema finaliza su sesión
</td>
<td>EP01</td>
</tr>

<tr>
<td>EP02</td>
<td>Gestión de maquinaria</td>
<td>Epic orientado al registro, organización y consulta del inventario de maquinaria disponible para alquiler.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US06</td>
<td>Registrar maquinaria</td>
<td>Como empresa de alquiler, quiero registrar mis máquinas y equipos para mantener organizado mi inventario.</td>
<td>
Given que el usuario tiene permisos para gestionar maquinaria<br>
When registra los datos de un equipo<br>
Then el sistema almacena la maquinaria en el inventario<br>
And muestra el equipo registrado
</td>
<td>EP02</td>
</tr>

<tr>
<td>US07</td>
<td>Consultar maquinaria</td>
<td>Como empresa de alquiler, quiero consultar las máquinas registradas para conocer la información de mis equipos.</td>
<td>
Given que existen equipos registrados<br>
When el usuario consulta el inventario<br>
Then el sistema muestra la lista de maquinaria<br>
And muestra información relevante de cada equipo
</td>
<td>EP02</td>
</tr>

<tr>
<td>US08</td>
<td>Actualizar información de maquinaria</td>
<td>Como empresa de alquiler, quiero actualizar la información de mis equipos para mantener el inventario actualizado.</td>
<td>
Given que existe una maquinaria registrada<br>
When el usuario modifica sus datos<br>
Then el sistema guarda la información actualizada
</td>
<td>EP02</td>
</tr>

<tr>
<td>US09</td>
<td>Consultar disponibilidad de maquinaria</td>
<td>Como empresa de alquiler, quiero conocer la disponibilidad de cada equipo para evitar conflictos al gestionar nuevos alquileres.</td>
<td>
Given que existen equipos registrados<br>
When el usuario consulta su disponibilidad<br>
Then el sistema muestra si cada equipo está disponible, reservado o alquilado
</td>
<td>EP02</td>
</tr>

<tr>
<td>US10</td>
<td>Consultar estado de maquinaria</td>
<td>Como empresa de alquiler, quiero conocer el estado de mis equipos para evitar alquilar maquinaria que no se encuentra en condiciones de uso.</td>
<td>
Given que existe una maquinaria registrada<br>
When el usuario consulta su información<br>
Then el sistema muestra su estado actual<br>
And permite identificar si está disponible para alquiler
</td>
<td>EP02</td>
</tr>

<tr>
<td>EP03</td>
<td>Búsqueda y solicitud de alquiler</td>
<td>Epic orientado a permitir que las pequeñas empresas constructoras encuentren maquinaria y gestionen solicitudes de alquiler.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US11</td>
<td>Buscar maquinaria</td>
<td>Como empresa constructora, quiero buscar maquinaria según mis necesidades para encontrar equipos adecuados para mi proyecto.</td>
<td>
Given que el usuario accede al catálogo de maquinaria<br>
When busca o filtra equipos<br>
Then el sistema muestra las maquinarias que coinciden con sus necesidades
</td>
<td>EP03</td>
</tr>

<tr>
<td>US12</td>
<td>Consultar información de maquinaria</td>
<td>Como empresa constructora, quiero consultar las características de una maquinaria para determinar si es adecuada para mi proyecto.</td>
<td>
Given que el usuario visualiza una maquinaria<br>
When selecciona el equipo<br>
Then el sistema muestra sus características, estado y condiciones de alquiler
</td>
<td>EP03</td>
</tr>

<tr>
<td>US13</td>
<td>Consultar disponibilidad para un periodo</td>
<td>Como empresa constructora, quiero consultar la disponibilidad de una maquinaria para un periodo determinado antes de solicitar el alquiler.</td>
<td>
Given que el usuario selecciona una maquinaria y un periodo<br>
When consulta su disponibilidad<br>
Then el sistema indica si el equipo puede ser alquilado durante dicho periodo
</td>
<td>EP03</td>
</tr>

<tr>
<td>US14</td>
<td>Solicitar alquiler de maquinaria</td>
<td>Como empresa constructora, quiero solicitar el alquiler de una maquinaria para utilizarla en mi proyecto.</td>
<td>
Given que la maquinaria está disponible<br>
When el usuario registra una solicitud de alquiler<br>
Then el sistema registra la solicitud<br>
And muestra su estado
</td>
<td>EP03</td>
</tr>

<tr>
<td>EP04</td>
<td>Planes y suscripciones</td>
<td>Epic orientado a la gestión de planes.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US15</td>
<td>Visualizar planes disponibles</td>
<td>Como usuario, quiero ver los planes para elegir uno.</td>
<td>
Given que el usuario accede a la sección de planes<br>
When visualiza opciones<br>
Then el sistema muestra los planes con sus características y precios
</td>
<td>EP04</td>
</tr>

<tr>
<td>US16</td>
<td>Suscribirse a un plan</td>
<td>Como usuario, quiero suscribirme a un plan para acceder a funciones premium.</td>
<td>
Given que el usuario selecciona un plan<br>
When confirma la suscripción<br>
Then el sistema registra el plan
</td>
<td>EP04</td>
</tr>

<tr>
<td>US17</td>
<td>Cambiar de plan</td>
<td>Como usuario, quiero cambiar de plan según mis necesidades.</td>
<td>
Given que el usuario tiene un plan activo<br>
When selecciona otro<br>
Then el sistema actualiza la suscripción
</td>
<td>EP04</td>
</tr>

<tr>
<td>EP05</td>
<td>Gestión de reservas y alquileres</td>
<td>Epic orientado a la administración de reservas y al seguimiento del ciclo de alquiler de los equipos.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US18</td>
<td>Gestionar solicitudes de alquiler</td>
<td>Como empresa de alquiler, quiero revisar las solicitudes recibidas para decidir cuáles atender y mantener control sobre mis alquileres.</td>
<td>
Given que existen solicitudes de alquiler<br>
When el usuario consulta las solicitudes<br>
Then el sistema muestra la información de cada solicitud<br>
And permite identificar su estado
</td>
<td>EP05</td>
</tr>

<tr>
<td>US19</td>
<td>Confirmar o rechazar una solicitud</td>
<td>Como empresa de alquiler, quiero aceptar o rechazar solicitudes de alquiler para controlar la disponibilidad de mis equipos.</td>
<td>
Given que existe una solicitud pendiente<br>
When el usuario selecciona aceptar o rechazar<br>
Then el sistema actualiza el estado de la solicitud<br>
And muestra el nuevo estado
</td>
<td>EP05</td>
</tr>

<tr>
<td>US20</td>
<td>Consultar alquileres activos</td>
<td>Como empresa de alquiler, quiero consultar mis alquileres activos para conocer qué equipos están actualmente alquilados.</td>
<td>
Given que existen alquileres activos<br>
When el usuario consulta sus alquileres<br>
Then el sistema muestra los equipos alquilados<br>
And muestra información del periodo correspondiente
</td>
<td>EP05</td>
</tr>

<tr>
<td>US21</td>
<td>Consultar estado de una solicitud de alquiler</td>
<td>Como empresa constructora, quiero consultar el estado de mi solicitud para saber si mi alquiler fue aceptado, rechazado o aún está pendiente.</td>
<td>
Given que el usuario ha realizado una solicitud<br>
When consulta sus solicitudes<br>
Then el sistema muestra el estado actualizado de cada una
</td>
<td>EP05</td>
</tr>

<tr>
<td>US22</td>
<td>Gestionar entregas y devoluciones</td>
<td>Como empresa de alquiler, quiero registrar las entregas y devoluciones de maquinaria para mantener trazabilidad sobre los equipos alquilados.</td>
<td>
Given que existe un alquiler confirmado<br>
When se registra la entrega o devolución<br>
Then el sistema actualiza el estado del alquiler<br>
And registra la operación realizada
</td>
<td>EP05</td>
</tr>

<tr>
<td>EP06</td>
<td>Gestión de mantenimiento e incidencias</td>
<td>Epic orientado al seguimiento del estado operativo de la maquinaria y a la gestión de mantenimientos e incidencias.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US23</td>
<td>Registrar mantenimiento</td>
<td>Como empresa de alquiler, quiero registrar mantenimientos realizados a una maquinaria para mantener un historial de su estado operativo.</td>
<td>
Given que existe una maquinaria registrada<br>
When el usuario registra un mantenimiento<br>
Then el sistema almacena la información<br>
And la relaciona con el equipo correspondiente
</td>
<td>EP06</td>
</tr>

<tr>
<td>US24</td>
<td>Programar mantenimiento</td>
<td>Como empresa de alquiler, quiero programar mantenimientos para evitar que los equipos sean utilizados cuando requieren atención.</td>
<td>
Given que una maquinaria requiere mantenimiento<br>
When el usuario registra una fecha de mantenimiento<br>
Then el sistema guarda la programación<br>
And permite consultar el mantenimiento pendiente
</td>
<td>EP06</td>
</tr>

<tr>
<td>US25</td>
<td>Registrar incidencia de maquinaria</td>
<td>Como empresa de alquiler, quiero registrar incidencias de mis equipos para llevar un control de problemas y reparaciones.</td>
<td>
Given que una maquinaria presenta una incidencia<br>
When el usuario registra el problema<br>
Then el sistema almacena la incidencia<br>
And la relaciona con la maquinaria correspondiente
</td>
<td>EP06</td>
</tr>

<tr>
<td>US26</td>
<td>Consultar historial de maquinaria</td>
<td>Como empresa de alquiler, quiero consultar el historial de una maquinaria para conocer sus alquileres, incidencias y mantenimientos.</td>
<td>
Given que existe una maquinaria registrada<br>
When el usuario consulta su historial<br>
Then el sistema muestra las operaciones asociadas al equipo
</td>
<td>EP06</td>
</tr>

<tr>
<td>EP07</td>
<td>Información y contratación del servicio</td>
<td>Epic orientado a brindar información sobre RentBuild y facilitar el contacto de potenciales clientes con la plataforma.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US27</td>
<td>Consultar información de RentBuild</td>
<td>Como visitante, quiero conocer las funcionalidades y beneficios de RentBuild para determinar si la solución se adapta a las necesidades de mi empresa.</td>
<td>
Given que el visitante accede al Landing Page<br>
When revisa la información del producto<br>
Then el sistema muestra sus principales funcionalidades y beneficios
</td>
<td>EP07</td>
</tr>

<tr>
<td>US28</td>
<td>Solicitar demostración</td>
<td>Como potencial cliente, quiero solicitar una demostración de RentBuild para conocer cómo funciona antes de utilizar el servicio.</td>
<td>
Given que el visitante desea conocer la plataforma<br>
When completa y envía el formulario de demostración<br>
Then el sistema registra la solicitud<br>
And muestra un mensaje de confirmación
</td>
<td>EP07</td>
</tr>

<tr>
<td>US29</td>
<td>Contactar con RentBuild</td>
<td>Como potencial cliente, quiero contactar con el equipo de RentBuild para realizar consultas sobre el servicio.</td>
<td>
Given que el visitante accede a la sección de contacto<br>
When completa y envía sus datos y consulta<br>
Then el sistema registra la solicitud de contacto
</td>
<td>EP07</td>
</tr>

<tr>
<td>EP08</td>
<td>Landing Page de RentBuild</td>
<td>Epic orientado a presentar la propuesta de valor de RentBuild y facilitar la navegación de los potenciales clientes hacia las funcionalidades y acciones principales de la plataforma.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US30</td>
<td>Visualizar propuesta de valor</td>
<td>Como visitante, quiero identificar la propuesta de valor de RentBuild para comprender cómo puede ayudar a mi empresa a gestionar el alquiler de maquinaria.</td>
<td>
Given que el visitante accede al Landing Page<br>
When visualiza la sección principal<br>
Then el sistema muestra la propuesta de valor de RentBuild<br>
And presenta sus principales beneficios para la gestión de alquileres
</td>
<td>EP08</td>
</tr>

<tr>
<td>US31</td>
<td>Explorar funcionalidades principales</td>
<td>Como potencial cliente, quiero conocer las principales funcionalidades de RentBuild para identificar cuáles pueden ayudarme a gestionar mis operaciones de alquiler de maquinaria.</td>
<td>
Given que el visitante se encuentra en el Landing Page<br>
When revisa la sección de funcionalidades<br>
Then el sistema muestra las principales funcionalidades de RentBuild<br>
And presenta una descripción breve de cada funcionalidad
</td>
<td>EP08</td>
</tr>

<tr>
<td>US32</td>
<td>Identificar la solución para mi empresa</td>
<td>Como visitante, quiero identificar cómo RentBuild puede ayudar según mi tipo de empresa para conocer las funcionalidades relevantes para mis necesidades.</td>
<td>
Given que el visitante accede a la sección orientada a clientes<br>
When selecciona o visualiza su tipo de empresa<br>
Then el sistema presenta los beneficios relevantes para empresas de alquiler o empresas constructoras
</td>
<td>EP08</td>
</tr>

<tr>
<td>US33</td>
<td>Acceder a la Web Application</td>
<td>Como visitante, quiero acceder a la Web Application desde el Landing Page para utilizar las funcionalidades de RentBuild.</td>
<td>
Given que el visitante se encuentra en el Landing Page<br>
When selecciona el CTA para acceder a la plataforma<br>
Then el sistema redirige al visitante hacia la Web Application
</td>
<td>EP08</td>
</tr>

<tr>
<td>US34</td>
<td>Consultar el Landing Page en diferentes dispositivos</td>
<td>Como visitante, quiero visualizar correctamente el Landing Page desde diferentes dispositivos para conocer RentBuild sin importar el dispositivo que utilice.</td>
<td>
Given que el visitante accede al Landing Page desde un dispositivo<br>
When navega por sus diferentes secciones<br>
Then el sistema adapta correctamente el contenido a la resolución de pantalla<br>
And permite utilizar las funcionalidades de navegación sin pérdida de información
</td>
<td>EP08</td>
</tr>

<tr>
<td>US35</td>
<td>Cambiar el idioma del Landing Page</td>
<td>Como visitante, quiero cambiar el idioma del Landing Page para consultar la información de RentBuild en el idioma de mi preferencia.</td>
<td>
Given que el visitante accede al Landing Page<br>
When selecciona un idioma disponible<br>
Then el sistema muestra el contenido del Landing Page en el idioma seleccionado<br>
And mantiene la estructura y funcionalidad de la página
</td>
<td>EP08</td>
</tr>

</table>

## 3.2. Impact Mapping

![Impact Mapping](./assets/md-images-chapter3/impact-mapping.png)

## 3.3. Product Backlog

El Product Backlog de RentBuild contiene las historias de usuario identificadas para el desarrollo de la solución. Estas se presentan en orden correlativo según su identificador, desde US01 hasta US35.

| # Orden | User Story ID | Título | Descripción | Story Points |
| :---: | :---: | :--- | :--- | :---: |
| 1 | US01 | Registro de usuario | Como usuario, quiero registrarme en RentBuild para poder acceder a las funcionalidades de la plataforma. | 5 |
| 2 | US02 | Inicio de sesión | Como usuario, quiero iniciar sesión para acceder de forma segura a mi cuenta. | 3 |
| 3 | US03 | Gestionar perfil | Como usuario, quiero gestionar mi perfil para mantener actualizada mi información. | 3 |
| 4 | US04 | Cerrar sesión | Como usuario, quiero cerrar sesión para proteger el acceso a mi cuenta. | 1 |
| 5 | US05 | Recuperar contraseña | Como usuario, quiero recuperar mi contraseña para volver a acceder a mi cuenta en caso de olvidarla. | 3 |
| 6 | US06 | Registrar maquinaria | Como empresa de alquiler, quiero registrar maquinaria para mantener mi inventario disponible en RentBuild. | 5 |
| 7 | US07 | Consultar maquinaria | Como empresa de alquiler, quiero consultar mi maquinaria para conocer los equipos registrados. | 3 |
| 8 | US08 | Actualizar información de maquinaria | Como empresa de alquiler, quiero actualizar la información de mi maquinaria para mantener sus datos actualizados. | 3 |
| 9 | US09 | Consultar disponibilidad de maquinaria | Como empresa de alquiler, quiero consultar la disponibilidad de mi maquinaria para conocer qué equipos están disponibles. | 5 |
| 10 | US10 | Consultar estado de maquinaria | Como empresa de alquiler, quiero consultar el estado de mi maquinaria para conocer su condición actual. | 3 |
| 11 | US11 | Buscar maquinaria | Como empresa constructora, quiero buscar maquinaria para encontrar equipos que se ajusten a mis necesidades. | 5 |
| 12 | US12 | Consultar información de maquinaria | Como empresa constructora, quiero consultar la información de una maquinaria para conocer sus características antes de solicitar un alquiler. | 3 |
| 13 | US13 | Consultar disponibilidad para un periodo | Como empresa constructora, quiero consultar la disponibilidad de una maquinaria para un periodo determinado para saber si puedo alquilarla. | 5 |
| 14 | US14 | Solicitar alquiler de maquinaria | Como empresa constructora, quiero solicitar el alquiler de una maquinaria para utilizarla en mi proyecto. | 5 |
| 15 | US15 | Consultar planes | Como usuario, quiero consultar los planes disponibles para conocer las opciones que ofrece RentBuild. | 3 |
| 16 | US16 | Seleccionar plan | Como usuario, quiero seleccionar un plan para elegir la opción que se adapte a mis necesidades. | 3 |
| 17 | US17 | Gestionar suscripción | Como usuario, quiero gestionar mi suscripción para administrar el plan seleccionado. | 5 |
| 18 | US18 | Gestionar solicitudes de alquiler | Como empresa de alquiler, quiero gestionar las solicitudes de alquiler para administrar las solicitudes recibidas. | 5 |
| 19 | US19 | Confirmar o rechazar una solicitud | Como empresa de alquiler, quiero confirmar o rechazar una solicitud para determinar si el alquiler puede realizarse. | 3 |
| 20 | US20 | Consultar alquileres activos | Como empresa de alquiler, quiero consultar los alquileres activos para conocer las operaciones que se encuentran en curso. | 3 |
| 21 | US21 | Consultar estado de una solicitud de alquiler | Como empresa constructora, quiero consultar el estado de mi solicitud de alquiler para conocer su situación actual. | 3 |
| 22 | US22 | Gestionar entregas y devoluciones | Como empresa de alquiler, quiero gestionar las entregas y devoluciones para controlar el movimiento de la maquinaria. | 5 |
| 23 | US23 | Registrar mantenimiento | Como empresa de alquiler, quiero registrar mantenimientos para mantener un historial de las intervenciones realizadas a cada maquinaria. | 5 |
| 24 | US24 | Programar mantenimiento | Como empresa de alquiler, quiero programar mantenimientos para organizar las próximas intervenciones de la maquinaria. | 3 |
| 25 | US25 | Registrar incidencia de maquinaria | Como empresa de alquiler, quiero registrar incidencias para mantener un registro de los problemas ocurridos con la maquinaria. | 3 |
| 26 | US26 | Consultar historial de maquinaria | Como empresa de alquiler, quiero consultar el historial de una maquinaria para conocer sus mantenimientos e incidencias anteriores. | 5 |
| 27 | US27 | Consultar información de RentBuild | Como visitante, quiero consultar información de RentBuild para conocer la solución y su propuesta de valor. | 2 |
| 28 | US28 | Solicitar demostración | Como visitante, quiero solicitar una demostración para conocer cómo funciona RentBuild. | 2 |
| 29 | US29 | Contactar con RentBuild | Como visitante, quiero contactar con RentBuild para realizar consultas sobre la solución. | 2 |
| 30 | US30 | Visualizar propuesta de valor | Como visitante, quiero visualizar la propuesta de valor de RentBuild para comprender cómo puede ayudar a mi empresa. | 2 |
| 31 | US31 | Explorar funcionalidades principales | Como visitante, quiero explorar las funcionalidades principales para conocer qué puedo realizar con RentBuild. | 3 |
| 32 | US32 | Identificar la solución para mi empresa | Como visitante, quiero identificar si RentBuild se adapta a mi tipo de empresa para determinar si la solución responde a mis necesidades. | 3 |
| 33 | US33 | Acceder a la Web Application | Como visitante, quiero acceder a la Web Application desde la Landing Page para utilizar las funcionalidades de RentBuild. | 2 |
| 34 | US34 | Utilizar la plataforma desde dispositivos de diferentes tamaños | Como usuario, quiero utilizar RentBuild desde diferentes tamaños de pantalla para acceder a la plataforma de manera adecuada. | 5 |
| 35 | US35 | Utilizar la plataforma en diferentes idiomas | Como usuario, quiero utilizar RentBuild en diferentes idiomas para comprender y utilizar la plataforma. | 5 |

<div style="page-break-before: always;"></div>

# Capítulo IV: Product Design

## 4.1. Style Guidelines

Las **Style Guidelines** de RentBuild establecen las decisiones visuales y de interacción que deben mantenerse de forma consistente en la Landing Page y en la Web Application. Estas pautas funcionan como referencia común para el equipo al momento de diseñar e implementar interfaces, assets y componentes, evitando variaciones innecesarias entre productos y dispositivos.

La propuesta toma como base la identidad ya implementada en la Landing Page de RentBuild y la extiende a la Web Application. Además, se adoptan principios de **Material Design** para la jerarquía, los estados, el feedback visual y la consistencia de los componentes. En la futura implementación de la Web Application, estos criterios se alinean con el uso de **Angular Material**.

### 4.1.1. General Style Guidelines

#### Tone of Voice

El tono de comunicación de RentBuild se define como **serio, formal, respetuoso y sereno**. La plataforma se dirige principalmente a empresas que necesitan controlar operaciones de alquiler y a pequeñas empresas constructoras que requieren maquinaria para sus proyectos, por lo que la comunicación debe transmitir control, claridad y confianza.

- **Serio:** se priorizan mensajes útiles y orientados a la operación del negocio.
- **Formal:** se emplean expresiones claras y profesionales, evitando lenguaje ambiguo o excesivamente coloquial.
- **Respetuoso:** los mensajes de ayuda, error y validación orientan al usuario sin atribuirle culpa.
- **Sereno:** incluso en estados de mantenimiento, retraso o incidencia, la interfaz informa la situación y la acción disponible sin recurrir a mensajes alarmistas.

#### Branding

El isotipo de RentBuild se construye a partir de una representación simplificada y abstracta de una maquinaria de construcción, principalmente inspirada en la estructura de una excavadora. Esta elección busca establecer una relación visual inmediata con el sector en el que se especializa la plataforma: el alquiler de maquinaria y equipos para construcción. Asimismo, la forma del isotipo integra de manera sutil la inicial “R” de RentBuild, reforzando la identidad propia de la marca. 

#### Typography

La identidad tipográfica de **RentBuild** se basa principalmente en la familia **Inter**, utilizada como tipografía general de la Landing Page debido a su alta legibilidad en interfaces digitales y su adecuada adaptación a elementos como textos descriptivos, tarjetas, formularios, botones y componentes de navegación. Adicionalmente, la implementación incorpora **Rubik** como tipografía de apoyo para determinados elementos de mayor carácter visual o editorial, mientras que **Poppins** se utiliza en elementos específicos de la interfaz, como el selector de idioma. Esta combinación permite mantener una jerarquía visual clara y una presentación consistente en las distintas secciones de la Landing Page.

Se establece la siguiente jerarquía tipográfica como referencia:

| Nivel              | Referencia de uso                                                                  | Familia tipográfica | Peso sugerido |
| ------------------ | ---------------------------------------------------------------------------------- | ------------------- | ------------: |
| H1 / Hero          | Mensaje principal de la Landing Page y textos de mayor impacto visual              | Inter / Rubik       |       700–800 |
| H2 / Section Title | Títulos principales de secciones como Features, Benefits, About, Pricing y Contact | Inter               |           700 |
| H3 / Card Title    | Títulos de funcionalidades, beneficios, planes y elementos destacados              | Inter               |       600–700 |
| Body               | Descripciones, contenido informativo, formularios y textos generales               | Inter               |           400 |
| Caption / Helper   | Textos secundarios, estados, etiquetas, metadatos y mensajes de apoyo              | Inter               |       400–500 |
| Button Label       | Call to Action (CTA), botones de navegación y acciones de la interfaz              | Inter               |           600 |
| Language Selector  | Opciones y controles relacionados con la selección de idioma                       | Poppins             |       500–600 |


#### Colors

La paleta de colores de **RentBuild** se basa en los tokens definidos en `css/variables.css` de la Landing Page. La identidad visual combina un **naranja cálido** como color principal para llamadas a la acción y elementos destacados, junto con tonos **azul oscuro** para títulos, navegación y elementos asociados a la marca. Asimismo, se emplean colores neutros para fondos, textos secundarios, bordes y superficies, permitiendo mantener un adecuado nivel de contraste y una jerarquía visual consistente.

| Token             | Hex       | Aplicación                                                                                                       |
| ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| Primary           | `#F59E0B` | Color principal de la interfaz, utilizado en CTA, elementos destacados y acentos visuales                        |
| Primary Dark      | `#B86D00` | Variante oscura del color principal, utilizada en estados interactivos como hover y elementos de mayor contraste |
| Navy / Brand Blue | `#1E3A5F` | Branding, títulos, navegación y elementos principales de identidad visual                                        |
| Text / Ink        | `#1E293B` | Texto principal, encabezados y contenido que requiere alto contraste                                             |
| Blue              | `#2563EB` | Enlaces, estados de enfoque y acciones secundarias                                                               |
| Mint              | `#54BD95` | Indicadores positivos, estados de disponibilidad y elementos complementarios                                     |
| Background        | `#F8FAFC` | Fondo general de la Landing Page y secciones de contenido                                                        |
| Surface           | `#FFFFFF` | Cards, formularios, paneles y superficies elevadas                                                               |
| Text Muted        | `#737984` | Descripciones, textos secundarios, metadatos y contenido auxiliar                                                |
| Footer            | `#64748B` | Texto secundario y contenido complementario del footer                                                           |
| Border            | `#E2E8F0` | Bordes, divisores, contornos de inputs y separación entre componentes                                            |

En la Web Application se utilizan además colores semánticos para estados de operación: verde para disponibilidad o éxito, azul para estados confirmados, naranja para mantenimiento o atención requerida y rojo para error o acciones críticas.

#### Spacing

El sistema de espaciado de **RentBuild** utiliza una escala consistente definida mediante variables CSS. Los valores principales son `4 px`, `8 px`, `16 px`, `24 px`, `48 px` y `80 px`, empleados para controlar márgenes, paddings y separación entre los distintos elementos y secciones de la Landing Page. Esta progresión permite mantener una distribución visual uniforme y establecer una jerarquía clara entre contenidos relacionados.

Para los bordes redondeados se establecen como valores principales `8 px`, `16 px` y `24 px`, correspondientes a los tokens `--radius-sm`, `--radius-md` y `--radius-lg`. Adicionalmente, algunos componentes utilizan radios específicos como `10 px`, `20 px`, `30 px` o `999 px`, este último empleado principalmente en elementos con forma de pill, badges y controles completamente redondeados.

El contenido principal de la Landing Page se encuentra limitado mediante un contenedor con un ancho máximo de **1180 px** (`--container-max`). Este contenedor adapta automáticamente su ancho en pantallas más pequeñas mediante márgenes laterales responsivos, mientras que las distintas secciones utilizan espacios verticales amplios para mantener una adecuada separación visual.

Las cards, formularios y paneles emplean sombras suaves, utilizando como referencia el token `--shadow-card`, definido como `0 3px 8px rgb(12 36 66 / 8%)`. Estas sombras permiten diferenciar las superficies y generar profundidad sin producir una apariencia visual excesivamente cargada.

<p align="center">
  <img src="assets/md-images-chapter4/GeneralStyleGuidelinesPreview.png"
       alt="General Style Guidelines de RentBuild"
       width="100%">
</p>


### 4.1.2. Web Style Guidelines

Las **Web Style Guidelines** trasladan la identidad visual de **RentBuild** a interfaces web responsive, manteniendo coherencia entre la **Landing Page** y la **Web Application**. La Landing Page utiliza una navegación horizontal y una organización principalmente secuencial del contenido, mientras que la Web Application se estructura mediante una sidebar persistente, módulos funcionales, cards, formularios, filtros, tablas y listas operativas.

La guía busca mantener consistencia en el uso de colores, tipografías, espaciado, jerarquías visuales, componentes interactivos y estados de interfaz, permitiendo que ambas experiencias formen parte de un mismo sistema visual.

#### Material Design and Components

El lenguaje visual de **RentBuild** toma principios de **Material Design** como referencia para la jerarquía, separación de superficies, consistencia de acciones, feedback visual y estados de interacción. Estos principios se adaptan a la identidad propia de RentBuild mediante sus tokens de color, tipografía, espaciado, bordes y radios.

Para la **Web Application**, los componentes se diseñan con una estructura compatible con patrones de interfaces basadas en componentes, pudiendo posteriormente implementarse con tecnologías como **Angular Material** sin perder la identidad visual definida para RentBuild.

Los componentes principales son:

| Componente | Criterio de diseño |
|---|---|
| Primary CTA | Acción principal de alta visibilidad; utiliza principalmente el color `Primary` (`#F59E0B`) y texto de alto contraste |
| Secondary Button | Acción complementaria presentada mediante borde, fondo blanco o superficie neutra |
| Input / Select / Textarea | Label visible, borde consistente, espaciado uniforme y estados diferenciados de focus, error y disabled |
| Search Bar | Búsqueda directa por nombre o categoría, complementada con filtros cuando corresponde |
| Status Badge | Etiqueta breve acompañada de color para representar disponibilidad, alquiler, mantenimiento, aprobación, rechazo u otros estados |
| Data Card | Agrupa información relevante en superficies blancas con bordes suaves y jerarquía clara |
| Catalog Card | Presenta maquinaria mediante categoría, nombre, estado, disponibilidad, tarifa y acceso a detalle |
| Data Table | Organiza información operativa como inventario, solicitudes, alquileres, mantenimiento e historial |
| Form Card | Contenedor utilizado para procesos como registro de maquinaria o mantenimiento |
| Sidebar | Navegación principal persistente de la Web Application, con estado activo diferenciado mediante fondo claro y color naranja |
| Header | Navegación principal de la Landing Page, con acceso a las principales secciones del contenido |
| Filter Control | Selectores y controles utilizados para reducir resultados por categoría, estado, maquinaria u otros criterios |
| User Profile Block | Área que muestra información básica del usuario y acceso a la acción de cerrar sesión |

#### Responsive Web Design

La Landing Page de **RentBuild** aplica un diseño responsivo que adapta progresivamente la distribución, navegación, tipografía y tamaño de los componentes según el ancho disponible. La implementación utiliza principalmente los breakpoints de `1120 px`, `1023 px`, `767 px` y `480 px`.

- **Desktop Web Browser:** se mantiene la distribución completa de las secciones, con navegación horizontal, composiciones de varias columnas y un ancho máximo de contenido controlado mediante el contenedor principal.
- **Tablet / Small Laptop:** a partir de `1023 px`, la navegación horizontal se transforma en un menú desplegable mediante un botón tipo hamburguesa. También se reducen espacios, tamaños tipográficos y separación entre cards para aprovechar mejor el área disponible.
- **Mobile Web Browser:** a partir de `767 px`, las principales secciones pasan progresivamente a una distribución de una columna. Elementos como Hero, About, Contact y Pricing reorganizan su contenido verticalmente, mientras que las cards y recursos visuales ajustan su ancho al espacio disponible. Por debajo de `480 px` se realizan ajustes adicionales en navegación, cards, footer y elementos visuales para pantallas pequeñas.

#### Interaction States

Los elementos interactivos de **RentBuild**, como botones, enlaces, controles del menú, selector de idioma, acordeones y campos de formulario, deben ofrecer una respuesta visual clara ante la interacción del usuario. Se consideran los estados **default, hover, focus, disabled, success y error**, aplicándolos según corresponda al tipo de componente.

La Landing Page actual incorpora cambios visuales en estado `hover` para botones y enlaces, además de un estado de foco accesible mediante `:focus-visible`. Este último utiliza un `outline` de `3 px` en el color Navy de la marca y un `outline-offset` de `5 px`, permitiendo identificar claramente el elemento seleccionado mediante navegación por teclado.

Los formularios también contemplan retroalimentación para estados de **success** y **error**, comunicando al usuario el resultado de acciones como el envío de información.

#### Internationalization and Accessibility

**RentBuild** contempla **English (`en`)** como idioma predeterminado y **Spanish (`es`)** como idioma alternativo. La implementación actual utiliza archivos de traducción independientes (`en.json` y `es.json`) y un selector `EN / ES` que permite cambiar el idioma de la interfaz. La preferencia seleccionada se conserva mediante `localStorage` utilizando la clave `rentbuild-language`.

En materia de accesibilidad, RentBuild incorpora estructura semántica, textos alternativos para recursos visuales, navegación mediante teclado, enlace de salto al contenido principal y atributos ARIA como `aria-label`, `aria-expanded`, `aria-controls`, `aria-current` y `aria-live` cuando corresponde. Asimismo, se proporciona un foco visual claramente identificable y se respeta la preferencia del usuario `prefers-reduced-motion`, desactivando animaciones y transiciones cuando el sistema solicita una reducción de movimiento.

## 4.2. Information Architecture

Para el desarrollo de **RentBuild**, la Arquitectura de la Información se plantea considerando las necesidades de los usuarios, la naturaleza de las tareas que realizan y la estructura del contenido disponible tanto en la **Landing Page** como en la **Web Application**. Esta organización permite presentar la información de manera clara, facilitar el acceso a las funcionalidades principales y reducir la complejidad durante la navegación e interacción con la plataforma.

### 4.2.1. Organization Systems

En la **Landing Page**, la información se organiza principalmente de manera **jerárquica y secuencial**. El visitante inicia su recorrido con la propuesta de valor presentada en el **Hero** y continúa progresivamente por las secciones que explican el funcionamiento, las características y los beneficios de RentBuild. Posteriormente, puede conocer con mayor detalle el producto, revisar información sobre la solución, consultar los planes disponibles y finalmente acceder a las opciones de contacto.

El recorrido principal de la Landing Page sigue aproximadamente la siguiente secuencia:

**Home / Hero → How It Works → Features → Benefits → Product Showcase → About RentBuild → Pricing → Contact**

Esta estructura permite acompañar al visitante desde el descubrimiento inicial de RentBuild hasta la evaluación de sus funcionalidades y planes, finalizando con una posible acción de contacto o conversión.

En la **Web Application**, la información se organiza principalmente **por tópicos y tareas**, utilizando una barra lateral persistente que permite acceder directamente a las principales funcionalidades del sistema. 

- **Perfil:** permite visualizar la información correspondiente a la cuenta del usuario.
- **Inventario:** presenta la maquinaria registrada junto con información como categoría, estado y unidades disponibles.
- **Registrar maquinaria:** permite incorporar nuevos equipos al inventario mediante un formulario.
- **Solicitudes:** permite consultar las solicitudes de alquiler realizadas y su respectivo estado.
- **Alquileres activos:** muestra los alquileres que se encuentran actualmente en curso, incluyendo información sobre periodo, tarifa y costo estimado.
- **Mantenimiento:** permite registrar mantenimientos o incidencias relacionadas con la maquinaria y consultar su historial.
- **Historial:** centraliza los eventos relacionados con cada equipo, como solicitudes, aprobaciones, rechazos, incidencias y mantenimientos.
- **Catálogo:** permite explorar la maquinaria disponible mediante cards, búsqueda y filtros por categoría y estado.

Además de la organización por tópicos, RentBuild incorpora una organización **secuencial** asociada al ciclo operativo de la maquinaria. Las diferentes funcionalidades se relacionan siguiendo un flujo general como el siguiente:

**registro o consulta de maquinaria → solicitud de alquiler → aprobación o rechazo → alquiler activo → mantenimiento o incidencia → historial → actualización de disponibilidad**

Esta combinación entre organización temática y secuencial permite que el usuario pueda acceder directamente a una funcionalidad específica desde la navegación principal y, al mismo tiempo, comprender la relación existente entre las distintas etapas del ciclo de alquiler y gestión de maquinaria.

### 4.2.2. Labeling Systems

El sistema de etiquetado de **RentBuild** utiliza términos breves, descriptivos y relacionados directamente con las tareas del dominio de alquiler y gestión de maquinaria. Las etiquetas buscan mantener consistencia entre la **Landing Page** y la **Web Application**, evitando términos ambiguos y facilitando que el usuario pueda anticipar el contenido o acción asociada a cada elemento.

La plataforma contempla internacionalización mediante **English (`en`)** y **Spanish (`es`)**, manteniendo equivalencias para los principales elementos de navegación, contenido y estados de la interfaz.

| Contexto | Etiqueta principal | Asociación esperada |
|---|---|---|
| Landing Page | `Home` | Propuesta de valor principal de RentBuild |
| Landing Page | `How it works` | Explicación general del funcionamiento y ciclo operativo |
| Landing Page | `Features` | Funcionalidades principales para la gestión de maquinaria |
| Landing Page | `Benefits` | Beneficios obtenidos mediante el uso de RentBuild |
| Landing Page | `Product Demo` | Presentación visual del funcionamiento del producto |
| Landing Page | `About` | Información sobre RentBuild y su propósito |
| Landing Page | `Plans` | Planes Basic, Pro y Premium |
| Landing Page | `Contact us` | Comunicación y contacto con el equipo de RentBuild |
| Web Application | `Profile / Perfil` | Información de la cuenta del usuario |
| Web Application | `Inventory / Inventario` | Maquinaria registrada, categoría, estado y unidades |
| Web Application | `Register machinery / Registrar maquinaria` | Registro de nuevos equipos |
| Web Application | `Requests / Solicitudes` | Solicitudes de alquiler y su estado |
| Web Application | `Active rentals / Alquileres activos` | Alquileres actualmente vigentes |
| Web Application | `Maintenance / Mantenimiento` | Registro y consulta de mantenimientos e incidencias |
| Web Application | `History / Historial` | Eventos y actividades asociados a la maquinaria |
| Web Application | `Catalog / Catálogo` | Exploración y consulta de la maquinaria disponible |

Los estados también utilizan etiquetas breves acompañadas por indicadores visuales. Para la maquinaria se utilizan estados como `Available / Disponible`, `Rented / Alquilado`, `Reserved / Reservado` y `Maintenance / Mantenimiento`. Para las solicitudes se emplean `Pending / Pendiente`, `Approved / Aprobada` y `Rejected / Rechazada`, mientras que los alquileres activos pueden mostrar estados como `In progress / En curso`.

El color funciona como apoyo visual para reconocer rápidamente estos estados, pero el significado no depende exclusivamente de él, ya que cada badge mantiene una etiqueta textual.

### 4.2.3. SEO Tags and Meta Tags

Los **SEO Tags y Meta Tags** permiten identificar y describir correctamente la Landing Page de RentBuild para navegadores, motores de búsqueda y dispositivos. 

| Producto | Tag | Valor |
|---|---|---|
| Landing Page | `title` | `RentBuild — Equipment rental, under control` |
| Landing Page | `description` | `RentBuild connects equipment, reservations, rentals, deliveries, returns, and maintenance in one platform. Built by DataFlux.` |
| Landing Page | `keywords` | `equipment rental, construction machinery, machinery management, rental management software, equipment availability, maintenance management, RentBuild` |
| Landing Page | `author` | `DataFlux` |
| Landing Page | `theme-color` | `#1E3A5F` |
| Landing Page | `charset` | `UTF-8` |
| Landing Page | `viewport` | `width=device-width, initial-scale=1.0` |
| Landing Page | `lang` | `en`, actualizado dinámicamente a `es` cuando corresponde |
| Web Application | `title` | `RentBuild | Equipment rental workspace` |
| Web Application | `description` | `Manage machinery inventory, rental requests, active rentals, maintenance and equipment history with RentBuild.` |
| Web Application | `keywords` | `equipment inventory, machinery rental, rental requests, active rentals, maintenance, equipment history, machinery catalog, RentBuild` |
| Web Application | `author` | `DataFlux` |

### 4.2.4. Searching Systems

El sistema de búsqueda de **RentBuild** se concentra en las áreas de la Web Application donde el volumen de maquinaria o registros puede dificultar la localización directa de información. En la Landing Page no se requiere un motor de búsqueda interno, debido a que el contenido se encuentra organizado en secciones accesibles mediante navegación y enlaces contextuales.

En la Web Application se combinan mecanismos de **búsqueda directa**, **filtrado** y **exploración visual**.

| Área | Búsqueda / filtros | Presentación de resultados |
|---|---|---|
| Landing Page | Navegación mediante secciones y enlaces internos | Desplazamiento hacia la sección correspondiente |
| Catálogo | Búsqueda por nombre o categoría | Cards de maquinaria |
| Catálogo | Filtro por categoría | Cards que coinciden con la categoría seleccionada |
| Catálogo | Filtro por estado | Cards según disponibilidad o estado de la maquinaria |
| Historial | Filtro por maquinaria | Tabla con eventos, fechas y detalles asociados |
| Inventario | Consulta directa de maquinaria registrada | Tabla con equipo, categoría, estado y unidades |
| Solicitudes | Consulta de solicitudes registradas | Tabla con maquinaria, fechas de alquiler y estado |
| Alquileres activos | Consulta de alquileres actualmente vigentes | Tabla con maquinaria, periodo, tarifa, costo y estado |
| Mantenimiento | Selección de maquinaria y tipo de registro | Formulario e historial de mantenimientos e incidencias |

El **Catálogo de maquinaria** constituye el principal sistema de búsqueda exploratoria. El usuario dispone de una barra con el placeholder `Search by name or category… / Buscar por nombre o categoría…`, acompañada por filtros de categoría y estado. Los resultados se presentan mediante cards que muestran información esencial como categoría, nombre del equipo, estado, disponibilidad, tarifa y acceso a detalles.

Por otra parte, el módulo **Historial** permite filtrar los eventos según una maquinaria determinada, facilitando la consulta de solicitudes, mantenimientos, incidencias y otros acontecimientos relacionados con un equipo.

El criterio general consiste en utilizar **búsqueda directa** cuando el usuario conoce el nombre o categoría de la maquinaria y **filtros** cuando necesita reducir progresivamente el conjunto de resultados.

### 4.2.5. Navigation Systems

**RentBuild** emplea diferentes niveles de navegación para permitir que el usuario acceda a las principales funcionalidades sin perder el contexto dentro de la plataforma.

| Tipo de navegación | Aplicación en RentBuild |
|---|---|
| Global | Header de la Landing Page y sidebar persistente de la Web Application |
| Local | Contenido y controles propios de módulos como Inventario, Mantenimiento, Historial y Catálogo |
| Contextual | Acciones como `View details / Ver detalle`, registro de maquinaria y consulta de información específica |
| Utility | Selector `EN / ES`, información del usuario y `Log out / Cerrar sesión` |
| Quick actions | `Register machinery / Registrar maquinaria`, `Save record / Guardar registro` y `View details / Ver detalle` |
| Responsive | Menú desplegable en la Landing Page y adaptación de la navegación para pantallas de menor tamaño |

En la **Landing Page**, la navegación global permite acceder a las principales áreas informativas de RentBuild. El logo funciona como acceso a `Home`, mientras que la navegación dirige al usuario hacia secciones como `How it works`, `Features`, `Plans`, `Our Team` y `Contact us`. Otras secciones, como Benefits, Product Demo y About, forman parte del recorrido secuencial del contenido.

## 4.3. Landing Page UI Design

El diseño de la Landing Page de RentBuild busca comunicar de manera clara la propuesta de valor de la plataforma y presentar sus principales funcionalidades relacionadas con la gestión de equipos y operaciones de alquiler.

### 4.3.1. Landing Page Wireframe

### Nav y Hero

La sección inicial del wireframe presenta el logotipo de RentBuild, el menú de navegación y el mensaje principal de la plataforma. El contenido se divide en dos áreas: a la izquierda se muestra la propuesta de valor y los botones de acción, mientras que a la derecha se reserva espacio para elementos visuales relacionados con la gestión de equipos.

![Landing_Page_UI_Design-Nav_y_Hero.png](assets/md-images-chapter4/Landing_Page_UI_Design-Nav_y_Hero.png)

### Operational Management

Esta sección muestra las principales actividades que pueden gestionarse dentro de RentBuild. Se presentan bloques relacionados con la disponibilidad de equipos, las reservas y el mantenimiento. La distribución permite mostrar de forma sencilla cómo la plataforma centraliza diferentes procesos relacionados con el alquiler de maquinaria.

![Landing_Page_UI_Design-Operational_Management.png](assets/md-images-chapter4/Landing_Page_UI_Design-Operational_Management.png)

### Key Features

La sección de funciones principales está dividida entre un espacio para video y cuatro bloques informativos. Estos representan la gestión y disponibilidad de equipos, reservas y alquileres, mantenimiento e incidencias, y reportes operativos. La estructura permite presentar las funciones principales de RentBuild de manera clara y ordenada.

![Landing_Page_UI_Design-Key_Features.png](assets/md-images-chapter4/Landing_Page_UI_Design-Key_Features.png)

### RentBuild Platform Overview

Esta sección explica con mayor detalle la finalidad de RentBuild y su funcionamiento general. Se combina un bloque de información con un espacio destinado a un video demostrativo. El contenido destaca la gestión de equipos, el seguimiento del ciclo de alquiler y el control del mantenimiento.

![Landing_Page_UI_Design-RentBuild_Platform_Overview.png](assets/md-images-chapter4/Landing_Page_UI_Design-RentBuild_Platform_Overview.png)

### Benefits

La sección de beneficios presenta las principales ventajas que obtiene el usuario al utilizar RentBuild. Entre ellas se encuentran un mejor control de la disponibilidad de maquinaria, organización de reservas, seguimiento de alquileres y gestión del mantenimiento. La información se presenta de manera sencilla y acompañada de elementos visuales.

![Landing_Page_UI_Design-Benefits.png](assets/md-images-chapter4/Landing_Page_UI_Design-Benefits.png)

### Pricing

La sección de precios presenta tres alternativas de suscripción: Basic, Pro y Premium. Cada plan muestra diferentes características y niveles de acceso a las funciones de RentBuild. También se incluye un selector entre modalidad mensual y anual.

![Landing_Page_UI_Design-Pricing.png](assets/md-images-chapter4/Landing_Page_UI_Design-Pricing.png)

### Our Team

La sección Our Team presenta a los integrantes responsables del desarrollo del proyecto. Cada miembro aparece dentro de una tarjeta que contiene su fotografía, nombre, carrera o función y una breve descripción. La distribución se organiza en dos filas para mantener una presentación ordenada.

![Landing_Page_UI_Design-Our_Team.png](assets/md-images-chapter4/Landing_Page_UI_Design-Our_Team.png)

### Footer

El Footer representa la última sección de la Landing Page y concentra los enlaces secundarios de navegación. Incluye accesos relacionados con el producto, soporte, información de la empresa, contacto, términos y políticas de privacidad.

![Landing_Page_UI_Design-Benefits.png](assets/md-images-chapter4/Landing_Page_UI_Design-Benefits.png)

### 4.3.2. Landing Page Mock-up

El mock-up de la Landing Page de **RentBuild** representa la versión visual de alta fidelidad del diseño definido previamente en el wireframe. En esta etapa se incorporan la paleta de colores, tipografía, imágenes, tarjetas, sombras, botones y elementos gráficos que conforman la identidad visual final de la plataforma.

### Nav y Hero

El mock-up del Hero aplica la identidad visual definitiva de RentBuild mediante colores, tipografía, botones y elementos gráficos. El mensaje principal ocupa una posición destacada y se acompaña de llamadas a la acción como registro y demostración. A la derecha se muestran elementos relacionados con equipos y disponibilidad.

![Landing_Page_ Mock_up-Nav_y_Hero.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Nav_y_Hero.png)

### Operational Management

En la versión de alta fidelidad, esta sección utiliza iconos, colores y una organización visual uniforme para representar disponibilidad, reservas y mantenimiento. Cada función se presenta mediante títulos y textos breves que permiten una lectura rápida. El uso de fondos claros y espacios amplios evita la saturación de información.

![Landing_Page_ Mock_up-Operational_Management.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Operational_Management.png)

### Key Features

La sección presenta un reproductor de video acompañado de cuatro tarjetas que representan las funciones principales de RentBuild. Las tarjetas utilizan bordes redondeados, sombras suaves y títulos claramente diferenciados. Se muestran funciones de gestión de equipos, alquileres, mantenimiento y reportes.

![Landing_Page_ Mock_up-Kep_Features.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Kep_Features.png)

### RentBuild Platform Overview

El mock-up combina un bloque descriptivo con un video de mayor tamaño para explicar cómo funciona RentBuild. Los textos destacan la gestión de equipos, el seguimiento del ciclo de alquiler y el mantenimiento de maquinaria. La organización en dos columnas permite distribuir correctamente la información.

![Landing_Page_ Mock_up-RentBuild_Platform_Overview.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-RentBuild_Platform_Overview.png)

### Benefits

La sección de beneficios utiliza textos breves y elementos gráficos para destacar las ventajas principales de RentBuild. Se muestran aspectos relacionados con el control de maquinaria, reservas, devoluciones y mantenimiento. La jerarquía entre títulos y descripciones permite identificar rápidamente cada beneficio.

![Landing_Page_ Mock_up-Benefits.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Benefits.png)

### Pricing

El mock-up presenta tres tarjetas correspondientes a los planes Basic, Pro y Premium. El plan Premium se destaca visualmente mediante el uso del color naranja, mientras que los demás mantienen tonos más claros. Cada tarjeta muestra sus principales funcionalidades y un botón de acción.

![Landing_Page_ Mock_up-Pricing.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Pricing.png)

### Our Team

La sección utiliza tarjetas con fotografías circulares de cada integrante, acompañadas de su nombre, rol y una breve descripción. Los elementos se organizan en filas y mantienen espacios suficientes para mejorar la lectura. Los colores y estilos de las tarjetas siguen la identidad visual de RentBuild.

![Landing_Page_ Mock_up-Our_Team.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Our_Team.png)

### Footer

El Footer del mock-up utiliza un fondo oscuro para diferenciar claramente el final de la página. Los enlaces están distribuidos en columnas relacionadas con producto, soporte, empresa y otros recursos. Los textos claros generan un buen contraste con el fondo.

![Landing_Page_ Mock_up-Footer.png](assets/md-images-chapter4/Landing_Page_%20Mock_up-Footer.png)

## 4.4. Web Applications UX/UI Design

### 4.4.1. Web Applications Wireframes

### 4.4.2. Web Applications Wireflow Diagrams

### 4.4.3. Web Applications Mock-ups

### 4.4.4. Web Applications User Flow Diagrams

## 4.5. Web Applications Prototyping

## 4.6. Domain-Driven Software Architecture

### 4.6.1. Design-Level Event Storming

El Design-Level Event Storming permitió profundizar en los procesos identificados durante el Big Picture Event Storming, detallando los eventos, comandos, actores y reglas principales involucrados en el dominio de RentBuild. Este análisis facilita la identificación de los límites y responsabilidades de los diferentes componentes del sistema.

![Design-Level Event Storming](assets/md-images-chapter4/design-level-event-storming.png)

### 4.6.2. Software Architecture Context Diagram

El Software Architecture Context Diagram presenta a **RentBuild** como un único sistema de software y muestra su interacción con los principales usuarios y servicios externos. En este nivel del C4 Model no se representan todavía los componentes internos, containers, bounded contexts ni tecnologías de implementación, ya que el objetivo es delimitar el alcance funcional de la solución y reconocer las dependencias externas con las que se comunica.

Los principales actores que interactúan con RentBuild son:

- **Rental Operator:** representa al usuario perteneciente a una empresa de alquiler de maquinaria. Utiliza RentBuild para administrar equipos, solicitudes de alquiler, reservas, entregas, devoluciones, incidencias y actividades de mantenimiento.
- **Construction Manager:** representa al usuario perteneciente a una empresa constructora. Utiliza la plataforma para buscar maquinaria, revisar disponibilidad, realizar solicitudes de alquiler y efectuar el seguimiento de sus reservas y alquileres activos.
- **System Administrator:** representa al responsable de administrar el acceso a la plataforma, supervisar su operación y atender casos excepcionales que requieran intervención administrativa.

RentBuild también mantiene comunicación con servicios externos necesarios para determinadas capacidades del producto:

- **Google Maps Platform:** proporciona servicios de geolocalización y mapas utilizados para apoyar la localización de maquinaria y la coordinación de entregas y devoluciones.
- **Stripe:** procesa los pagos asociados a los planes de suscripción de RentBuild.
- **SendGrid:** proporciona servicios de correo transaccional para comunicaciones relacionadas con cuentas, reservas, alquileres, suscripciones y otras notificaciones del sistema.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/context/rentbuild-c4-context-diagram.png"
       alt="RentBuild Software Architecture Context Diagram"
       width="90%">
</p>

### 4.6.3. Software Architecture Container Diagrams

The Software Architecture Container Diagram presents the main containers that compose the RentBuild platform and the technologies used to implement them.

RentBuild is composed of a public **Landing Page**, a **Single Page Application**, a **RESTful API**, and a **MySQL Database**. The Landing Page provides public information about the platform, while the Single Page Application allows authenticated users to interact with the main business capabilities. The RESTful API exposes the application services and manages access to persistent data.

Additionally, the RESTful API communicates with external services such as **Google Maps Platform** for geolocation capabilities, **Stripe** for subscription payment processing, and **SendGrid** for transactional email delivery.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/container/rentbuild-c4-system2-container-diagram.png"
       alt="RentBuild Software Architecture Container Diagram"
       width="90%">
</p>

### 4.6.4. Software Architecture Components Diagrams

Se presenta un diagrama de componentes por cada container con lógica propia: la Web Application y la RentBuild API. El Landing Page y la Base de Datos no se descomponen, ya que el primero es contenido estático y la segunda es un almacén sin componentes internos.

#### Web Application

![Component Diagram — Web Application](./assets/md-images-chapter4/software-architecture-component-diagram-web-application.png)

La Web Application se organiza en una capa transversal y un módulo por bounded context. La capa transversal la forman el **App Router**, que define las rutas y las protege según el rol; el **Auth Store**, que mantiene el estado global de sesión; y el **HTTP Client**, que centraliza la URL base de la API, las cabeceras de autenticación y el manejo de errores. Cada bounded context aporta un par de componentes: sus **Views** (componentes Vue de la interfaz) y su **Service** (la lógica de acceso a la API para ese contexto). Así, un cambio en los recursos de alquileres afecta solo a `Rental Service` y `Rental Views`, sin tocar el resto de la aplicación. La única dependencia cruzada es la de `Rental Views` sobre `Inventory Service`, necesaria para consultar la disponibilidad del equipo antes de enviar una solicitud.

#### RentBuild API

![Component Diagram — RentBuild API](./assets/md-images-chapter4/software-architecture-component-diagram-api.png)

La API tiene un controller de ASP.NET Core por bounded context: `/api/v1/users` y `/api/v1/auth` (IAM), `/api/v1/company-profiles` (Profiles), `/api/v1/equipment`, `/api/v1/categories` y `/api/v1/availability` (Inventory), `/api/v1/rental-requests`, `/api/v1/contracts`, `/api/v1/deliveries` y `/api/v1/returns` (Rentals), y `/api/v1/maintenance-records` e `/api/v1/incidents` (Maintenance). Todos los controllers persisten a través del componente **Persistence** (DbContext y repositorios de Entity Framework Core), y el **Notification Client** concentra el envío de correos transaccionales. Las dos dependencias entre contextos reflejan reglas del negocio: **Rentals actualiza el estado del equipo en Inventory** al aceptar una solicitud, registrar una entrega o una devolución (reserva → alquilado → disponible), y **Maintenance marca el equipo en mantenimiento o disponible** al programar o completar un trabajo. Estas son las transiciones que hoy las empresas pierden al gestionar con hojas de cálculo, y aquí quedan bajo control de la API.

---

## 4.7. Software Object-Oriented Design

El diseño orientado a objetos detalla la implementación de cada bounded context identificado en la arquitectura. Cada diagrama sigue la misma estructura: entidades del dominio con sus atributos y comportamiento, value objects para conceptos sin identidad propia (periodos, tarifas, direcciones), enumeraciones para los estados del Ubiquitous Language, un repositorio por agregado y un servicio de aplicación que orquesta los casos de uso de las User Stories. Los nombres están en inglés según la convención de nomenclatura del proyecto y los tipos corresponden a C#, el lenguaje de los Web Services; las etiquetas de las relaciones van en español para facilitar la lectura.

### 4.7.1. Class Diagrams

#### IAM

![Class Diagram — IAM](./assets/md-images-chapter4/class-diagram-iam.png)

`User` es la entidad central, con `role` (empresa de alquiler o constructora) y `status`. `Credentials` es un value object que encapsula la validación de correo y contraseña, y `Session` representa el token vigente. `AuthenticationService` orquesta registro, inicio y cierre de sesión (US01, US02) a través de `UserRepository`.

#### Profiles

![Class Diagram — Profiles](./assets/md-images-chapter4/class-diagram-profiles.png)

`CompanyProfile` guarda los datos de la empresa (US03) y compone un value object `Address` con coordenadas, que alimenta la integración con Google Maps. `ProviderProfile` extiende el perfil de una empresa de alquiler con su reputación pública — alquileres completados y tasa de cumplimiento —, que corresponde al término "Perfil de Proveedor" del Ubiquitous Language.

#### Inventory

![Class Diagram — Inventory](./assets/md-images-chapter4/class-diagram-inventory.png)

`Equipment` es el agregado principal: pertenece a una `EquipmentCategory`, compone una `RentalRate` (tarifa diaria y semanal) y mantiene su `EquipmentStatus` (disponible, alquilado, en mantenimiento). Los `AvailabilityBlock` con su `DateRange` permiten responder `isAvailableFor(period)` sin superposiciones, que es la regla que evita las dobles reservas descritas en la problemática. `InventoryService` cubre el registro, la actualización, la búsqueda para constructoras y el cambio de estado (US04–US11).

#### Rentals

![Class Diagram — Rentals](./assets/md-images-chapter4/class-diagram-rentals.png)

`RentalRequest` modela la reservación: nace en estado `PENDING` y, al aceptarse, genera un `RentalContract` (US12–US16). El contrato compone un `RentalPeriod` y registra una `Delivery` y un `EquipmentReturn` (US17). `EquipmentReturn.requiresMaintenance()` es el punto donde una devolución con daño dispara el flujo del contexto Maintenance. `RentalService` orquesta el ciclo completo mediante los dos repositorios.

#### Maintenance

![Class Diagram — Maintenance](./assets/md-images-chapter4/class-diagram-maintenance.png)

`MaintenanceRecord` distingue mantenimientos preventivos y correctivos con su ciclo de estados (US18, US19). `Incident` registra daños o fallas con su severidad y puede originar un `MaintenanceRecord` (US20). `EquipmentHistory` es un modelo de lectura que agrega alquileres, incidencias y mantenimientos de un equipo para responder US21 sin acoplar el contexto a Rentals: solo consume un `RentalSummary` con los datos mínimos.

---

## 4.8. Database Design

El modelo de datos traduce las entidades de cada bounded context a tablas relacionales, conservando la separación por contexto: cada grupo de tablas pertenece a un único contexto y las referencias entre contextos se resuelven por identificador (`equipment_id`, `company_profile_id`, `contract_id`), nunca por tablas compartidas. Los value objects se aplanan en columnas de la entidad que los contiene (`Address` dentro de `company_profiles`, `RentalRate` dentro de `equipment`, `RentalPeriod` como `start_date`/`end_date`). Los estados se almacenan como cadenas cortas que corresponden a las enumeraciones del diseño de clases. El DBMS es MySQL, gestionado desde la API mediante Entity Framework Core y sus migraciones. Las columnas marcadas con asterisco son obligatorias.

### 4.8.1. Database Diagrams

![Database Diagram](./assets/md-images-chapter4/database-diagram.png)

Relaciones principales:

- `users` 1—0..1 `company_profiles`: cada usuario tiene a lo sumo un perfil de empresa; `company_profiles` 1—0..1 `provider_profiles`: solo las empresas de alquiler tienen perfil público de proveedor.
- `company_profiles` 1—N `equipment`: una empresa de alquiler posee muchos equipos; `equipment_categories` 1—N `equipment`.
- `equipment` 1—N `availability_blocks`: bloqueos de disponibilidad por periodo.
- `rental_requests` referencia al equipo, a la constructora y al proveedor; `rental_requests` 1—0..1 `rental_contracts`: una solicitud aceptada genera exactamente un contrato.
- `rental_contracts` 1—0..1 `deliveries` y 1—0..1 `equipment_returns`: un contrato tiene una entrega y una devolución.
- `equipment` 1—N `maintenance_records` y 1—N `incidents`; `incidents` 0..1—0..1 `maintenance_records`: una incidencia puede originar un mantenimiento correctivo; `incidents` puede referenciar el contrato durante el cual ocurrió.

Restricciones destacadas: `users.email`, `company_profiles.ruc` y `equipment.serial_number` son únicos; `rental_contracts.request_id`, `deliveries.contract_id` y `equipment_returns.contract_id` son únicos para garantizar la relación uno a uno.

---

# Capítulo V: Product Implementation, Validation & Deployment

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

**Project Management**

Para la administración del proyecto RentBuild se recurrió al uso de herramientas de comunicación, planificación y control de versiones. Se creó una organización en GitHub para centralizar la gestión del código fuente y su versionado. En cuanto a la planificación y asignación de tareas del equipo, se utilizó Trello mediante tableros personalizados para cada Sprint. Para la comunicación interna y coordinación de reuniones, se utilizó WhatsApp.

- Organización del trabajo: GitHub
- Planificación y asignación de tareas: Trello
- Comunicación: WhatsApp

Enlaces:

- GitHub: https://github.com/
- Trello: https://trello.com/
- WhatsApp: https://www.whatsapp.com/

**Requirement Management**

Para esta fase, el equipo utilizó Trello como herramienta visual para gestionar y priorizar los requisitos y tareas del proyecto mediante tableros organizados por Sprint. Se utilizó UXPressia para desarrollar los User Personas, Empathy Maps, Journey Maps e Impact Maps correspondientes a los dos segmentos objetivo de RentBuild: empresas de alquiler de maquinaria y pequeñas empresas constructoras.

Enlaces:

- Trello: https://trello.com/
- UXPressia: https://uxpressia.com/

**Product UX/UI Design**

En el diseño de la experiencia e interfaz de usuario, el equipo utilizó Figma para la creación de Wireframes, Mock-ups y Prototipos interactivos del Landing Page y de la Web Application, lo que permitió validar la propuesta visual y de interacción antes de la implementación.

Enlaces:

- Figma: https://www.figma.com/

**Software Development**

Para el desarrollo de la primera versión del Landing Page de RentBuild se utilizaron los lenguajes HTML, CSS y JavaScript en Visual Studio Code.

Enlaces:

- Visual Studio Code: https://code.visualstudio.com/

**Software Documentation**

Para el control de versiones y la colaboración en el desarrollo del informe, se utilizó GitHub siguiendo la estrategia de trabajo GitFlow, mediante el uso de ramas específicas para cada funcionalidad o corrección, lo que facilitó el trabajo colaborativo del equipo. Todo el contenido del proyecto fue centralizado en un repositorio dentro de una organización creada en GitHub. Para la documentación técnica se optó por archivos en formato Markdown, debido a su simplicidad, legibilidad y compatibilidad con GitHub.

Enlaces:

- GitHub: https://github.com/upc-pre-202620-1asi0730-8093-dataflux/dataflux-project-report

**Software Deployment**

Para el despliegue de la primera versión del Landing Page de RentBuild se utilizó Vercel.

Enlaces:

- Vercel: https://dataflux-landing-page.vercel.app/

### 5.1.2. Source Code Management

Para el control de versiones del código fuente de RentBuild, el equipo utiliza Git como sistema de versionado, gestionado a través de GitHub como plataforma de alojamiento. Se ha creado una organización pública en GitHub que centraliza los repositorios correspondientes a cada producto de la solución. Para esta primera entrega (AV1), el repositorio activo corresponde al Landing Page; los repositorios de Web Services (RESTful API) y Frontend Web Applications se incorporarán en las siguientes entregas conforme avance el desarrollo del proyecto.

**Repositorio del proyecto (AV1):**

| Producto | Repositorio |
| :--- | :--- |
| Informe del Proyecto | upc-pre-202620-1asi0730-8093-dataflux/dataflux-landing-page |
| Landing Page | https://dataflux-landing-page.vercel.app/ |

**Workflow de control de versiones: GitFlow**

El equipo aplica GitFlow como estrategia de ramificación, complementando la rama principal (`main`) y la rama de desarrollo (`develop`) con ramas específicas según el tipo de trabajo:

- **Feature branches**: se crean a partir de `develop` para el desarrollo de nuevas funcionalidades. Convención de nombres: `feature/nombre-de-la-funcionalidad` (ej. `feature/landing-hero-section`, `feature/landing-footer`).
- **Release branches**: se crean a partir de `develop` cuando el conjunto de features está listo para una nueva versión. Convención de nombres: `release/vX.Y.Z` (ej. `release/v1.0.0`).
- **Hotfix branches**: se crean a partir de `main` para corregir errores críticos detectados en producción. Convención de nombres: `hotfix/nombre-del-fix` (ej. `hotfix/fix-broken-navbar-link`).

**Semantic Versioning**

Las versiones (Releases) del Landing Page se nombran siguiendo Semantic Versioning 2.0.0, bajo el formato `MAJOR.MINOR.PATCH`:

- **MAJOR**: cambios incompatibles con versiones anteriores.
- **MINOR**: nuevas funcionalidades compatibles con versiones anteriores.
- **PATCH**: correcciones de errores compatibles con versiones anteriores.

Ejemplo: la primera versión desplegada del Landing Page se etiqueta como `v1.0.0`.

**Conventional Commits**

Todos los mensajes de commit siguen la convención de Conventional Commits, con el formato `tipo: descripción breve`, utilizando prefijos como:

- `feat`: para nuevas funcionalidades (ej. `feat: add landing page hero section`)
- `fix`: para corrección de errores (ej. `fix: correct broken footer link`)
- `docs`: para cambios en documentación (ej. `docs: update README with setup instructions`)
- `style`: para cambios de formato que no afectan la lógica
- `refactor`: para reestructuración de código sin cambiar su comportamiento

Esta convención permite mantener un historial de cambios claro y trazable para todo el equipo, incluso en esta etapa inicial del proyecto.

### 5.1.3. Source Code Style Guide & Conventions

El equipo adoptará nomenclatura en inglés para todas las variables, funciones, clases y archivos del proyecto, con el objetivo de mantener flexibilidad, escalabilidad y coherencia en el desarrollo de RentBuild.

**HTML / CSS**

Se sigue el Google HTML/CSS Style Guide. Las clases CSS estarán en `kebab-case`. Se utilizarán etiquetas semánticas e identificadores claros y descriptivos para accesibilidad y mantenimiento. Se usaron diferentes etiquetas para conformar la estructura del Landing Page del producto:

- `header`: Define todo el contenido introductorio de la página, incluyendo el logo de RentBuild y el menú de navegación principal.
- `nav`: Define la sección de la página dedicada a la navegación.
- `main`: Define el contenido principal de la página, agrupando las secciones informativas del Landing Page.
- `section`: Delimita cada bloque temático de la página.
- `div`: Permite la separación de diferentes objetos dentro de la página, lo que nos permitió aplicar hojas de estilo específicas para cada parte de los componentes visuales.
- `img`: Permite la inserción de imágenes en la página web. Todas las imágenes incluyen el atributo `alt` como parte de las prácticas de Accessibility (a11y).
- `ul` / `li`: La etiqueta `ul` define una lista desordenada, usada principalmente para el menú de navegación y la lista de beneficios de la plataforma; `li` define cada elemento dentro de dichas listas.
- `a`: Se usó para definir hipervínculos que trasladan a los usuarios entre las diferentes secciones de la página, así como los Call-to-Action que redirigen al registro/login en la Web Application.
- `p`: Define los párrafos de texto, separándolos del resto del contenido.
- `button`: Declara un botón interactivo que permite al usuario realizar una acción específica.
- `footer`: Define el contenido final de la página, incluyendo enlaces a Términos y Condiciones, Privacy Policy y datos de contacto.
- `h1` - `h4`: Definen los diferentes títulos y subtítulos de la página, siendo `h1` el mayor nivel y `h4` el más bajo.

**JavaScript**

Se sigue el Google JavaScript Style Guide y las MDN JavaScript guidelines. Se utiliza `camelCase` para variables y funciones, `const` y `let` en lugar de `var`, y punto y coma obligatorio al final de cada sentencia. Los nombres de archivo siguen `kebab-case`.

### 5.1.4. Software Deployment Configuration

Para el despliegue del Landing Page de RentBuild se utilizó Vercel, importando el repositorio `dataflux-landing-page` de la organización de GitHub del equipo desde la rama `main`. La configuración del proyecto utiliza el preset de aplicación Vite y el directorio raíz `./`.

![Vercel - Importación del proyecto](./assets/md-images-chapter5/vercel-import-project.png)

Una vez importado el proyecto, Vercel genera el Production Deployment, el cual queda en estado *Ready* y accesible públicamente en el dominio `dataflux-landing-page.vercel.app`. El despliegue toma como fuente la rama `main`, por lo que cada actualización de esta rama se refleja en producción.

![Vercel - Production Deployment](./assets/md-images-chapter5/vercel-production-deployment.png)

## 5.2. Landing Page, Services & Applications Implementation

### 5.2.1. Sprint 1

#### 5.2.1.1. Sprint Planning 1

| | |
| :--- | :--- |
| **Sprint #** | Sprint 1 |
| **Sprint Planning Background** | |
| Date | 2026-09-17 |
| Time | 10:00 PM |
| Location | Vía Discord |
| Prepared By | Luis Angel Cisneros Salas |
| Attendees | Cisneros Salas, Luis Angel<br>Viza Quispe, Marlon Packard<br>Manosalva Tovar, Miroslav Oscar<br>Montalvo Vásquez, Bruno Rodrigo<br>Vargas Manchinelli, Deiby Juan |
| Sprint 1 Review Summary | Durante el Sprint 1, el equipo completó exitosamente el desarrollo de la primera versión del Landing Page de RentBuild utilizando HTML, CSS y JavaScript, tomando como base los Wireframes y Mock-ups diseñados previamente en Figma. Asimismo, se avanzó con las pantallas iniciales de la Web Application correspondientes a la gestión de usuarios (Registro, Login, Perfil), gestión de maquinaria (Inventario, Registro, Detalle, Estado/Disponibilidad), solicitudes de alquiler (Bandeja de solicitudes, Mis solicitudes, Alquileres activos), mantenimiento e incidencias (Registro, Historial), y el Catálogo/búsqueda de maquinaria. El Landing Page se desplegó en un entorno de producción mediante Vercel, permitiendo su acceso público, y todas las tareas planificadas en el Sprint Backlog fueron completadas dentro del tiempo estimado. |
| Sprint 1 Retrospective Summary | En esta sección tuvimos varios aciertos, ya que la división de tareas entre diseño (Figma), desarrollo del Landing Page (HTML/CSS/JS) y desarrollo de las pantallas de la Web Application permitió avanzar en paralelo sin bloqueos. Sin embargo, nos quedamos con dos pendientes específicos: la definición temprana de la herramienta de despliegue y la integración de la lógica de negocio en algunas pantallas de la Web Application, lo cual puso a prueba nuestra capacidad de resolución de problemas sobre la marcha. |
| **Sprint Goal & User Stories** | |
| Sprint 1 Goal | Desarrollar e implementar la primera versión funcional del Landing Page de RentBuild, incluyendo su estructura y diseño visual basado en los prototipos definidos en Figma, así como las pantallas iniciales de la Web Application correspondientes a la gestión de usuarios, maquinaria, solicitudes de alquiler, mantenimiento/incidencias y catálogo de búsqueda, asegurando su despliegue en un entorno de producción accesible públicamente. |
| Sprint 1 Velocity | 59 |
| Sum of Story Points | 59 story points |

#### 5.2.1.2. Aspect Leaders and Collaborators

En esta sección se presenta el Leadership-and-Collaboration Matrix (LACX) elaborado por el equipo para el Sprint 1, el cual identifica al líder y a los colaboradores responsables de cada aspecto dentro del alcance definido para este sprint.

| Team Member (Last, First) | GitHub Username | Diseño visual y maquetación (Landing Page) | Desarrollo Web Application | Despliegue (Vercel) |
| :--- | :--- | :---: | :---: | :---: |
| Cisneros Salas, Luis Angel | LuisCS03 | C | L | C |
| Viza Quispe, Marlon Packard | V8Z5 | L | C | C |
| Manosalva Tovar, Miroslav Oscar | Miroa123 | C | C | L |
| Montalvo Vásquez, Bruno Rodrigo | TartaroZ | C | C | C |
| Vargas Manchinelli, Deiby Juan | poluxbinPe | C | C | C |

#### 5.2.1.3. Sprint Backlog 1

El propósito central de este Sprint fue construir la primera versión del Landing Page de RentBuild y avanzar en paralelo con las pantallas iniciales de la Web Application, cubriendo la gestión de usuarios, maquinaria, solicitudes de alquiler y mantenimiento/incidencias. El trabajo se organizó a partir de las User Stories asociadas a los Epics comprendidos en este Sprint (EP01, EP02, EP03, EP04, EP05 y EP06). Como herramienta de seguimiento y control de tareas, el equipo optó por Trello.

![Sprint 1 - Tablero de Trello](./assets/md-images-chapter5/sprint-1-trello-board.png)

**Trello:** https://trello.com/invite/b/6aacc6b9cc0413f772436a35/ATTI72782e0013e72d3ec63864ccbd335c7099570315/dataflux

| User Story ID | User Story Title | Work-Item ID | Work-Item Title | Description | Assigned To | Status (To do / In Process / To Review / Done) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US-01 | Registro | UT-01 | Crear estructura HTML | Maquetar el formulario de registro de usuario | Luis Cisneros | Done |
| US-01 | Registro | UT-02 | Añadir estilos CSS | Aplicar estilos según el diseño de Figma | Luis Cisneros | Done |
| US-01 | Registro | UT-03 | Añadir validaciones JS | Validar campos y mostrar mensaje de confirmación | Luis Cisneros | Done |
| US-02 | Login | UT-04 | Crear estructura HTML | Maquetar formulario de inicio de sesión | Marlon Viza | Done |
| US-02 | Login | UT-05 | Añadir estilos CSS | Aplicar estilos según diseño aprobado | Marlon Viza | Done |
| US-02 | Login | UT-06 | Añadir lógica JS | Validar credenciales y manejo de errores | Marlon Viza | Done |
| US-03 | Perfil de usuario | UT-07 | Crear estructura HTML | Maquetar sección de datos personales | Deiby Vargas | To Do |
| US-03 | Perfil de usuario | UT-08 | Añadir estilos CSS | Aplicar estilos según diseño | Deiby Vargas | To Do |
| US-04 | Registrar nueva maquinaria | UT-09 | Crear formulario de registro | Maquetar campos del equipo (nombre, tipo, estado) | Miroslav Manosalva | Done |
| US-04 | Registrar nueva maquinaria | UT-10 | Añadir validaciones JS | Validar datos ingresados del equipo | Miroslav Manosalva | Done |
| US-05 | Inventario de maquinaria | UT-11 | Crear vista de lista | Maquetar tabla/lista de maquinaria registrada | Bruno Montalvo | Done |
| US-05 | Inventario de maquinaria | UT-12 | Añadir estilos CSS | Aplicar estilos responsivos a la lista | Bruno Montalvo | Done |
| US-07/08 | Detalle + estado/disponibilidad | UT-13 | Crear vista de detalle | Maquetar sección con info, estado y disponibilidad | Luis Cisneros | In Progress |
| US-07/08 | Detalle + estado/disponibilidad | UT-14 | Añadir lógica JS | Mostrar estado dinámico (disponible/reservado/alquilado) | Luis Cisneros | In Progress |
| US-09 | Catálogo/búsqueda | UT-15 | Crear buscador | Maquetar barra de búsqueda y filtros | Marlon Viza | Done |
| US-09 | Catálogo/búsqueda | UT-16 | Añadir lógica JS | Filtrar resultados según criterios | Marlon Viza | Done |
| US-13/14 | Bandeja de solicitudes | UT-17 | Añadir acciones JS | Maquetar lista de solicitudes recibidas | Miroslav Manosalva | In Progress |
| US-15 | Alquileres activos | UT-18 | Crear vista de alquileres | Maquetar lista de equipos alquilados vigentes | Miroslav Manosalva | In Progress |
| US-16 | Mis solicitudes | UT-19 | Crear vista de solo lectura | Maquetar estado de solicitudes del cliente | Bruno Montalvo | To Do |
| US-18/20 | Registrar mantenimiento/incidencia | UT-20 | Crear formulario | Maquetar registro de mantenimiento e incidencias | Deiby Vargas | To Do |
| US-18/20 | Registrar mantenimiento/incidencia | UT-21 | Añadir validaciones JS | Validar tipo y fecha del registro | Luis Cisneros | In Progress |
| US-21 | Historial de maquinaria | UT-22 | Crear vista de historial | Maquetar historial de alquileres/incidencias/mantenimientos | Luis Cisneros | In Progress |
| US-21 | Historial de maquinaria | UT-23 | Añadir estilos CSS | Aplicar estilos a la línea de tiempo del historial | Marlon Viza | Done |

#### 5.2.1.4. Development Evidence for Sprint Review

En este primer Sprint, el equipo desarrolló tanto la primera versión del Landing Page como las pantallas iniciales de la Web Application, distribuyendo las tareas según lo definido en el Sprint Backlog. Cada integrante contribuyó con distintas funcionalidades a lo largo del sprint. A continuación, se presenta la tabla con los commits realizados durante este periodo.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on (Date) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RentBuild/Landing-Page | feature/app-features | a4682cd | feat(team): add profile photos for Bruno, Deiby and Miroslav | add profile photos for Bruno, Deiby and Miroslav | 18/09/2026 |
| RentBuild/Landing-Page | feature/app-features | bd3e866 | feat(catalog): add machinery search and filter screen | add machinery search and filter screen | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 8649b7c | feat(inventory): add machinery history screen | add machinery history screen | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | c220f22 | feat(maintenance): add register maintenance and incident form | add register maintenance and incident form | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 18b2785 | feat(rentals): add active rentals screen | add active rentals screen | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | a0b3479 | feat(requests): add my rental requests screen for construction companies | add my rental requests screen for construction companies | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | eb60cf5 | feat(inventory): add machinery detail screen with status and availability | add machinery detail screen with status and availability | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 0a4dc7d | feat(inventory): add register new machinery form | add register new machinery form | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | fe84942 | feat(inventory): display machinery list with status and availability | display machinery list with status and availability | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 4c44274 | feat(profile): add user profile screen | add user profile screen | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 8c6ff60 | feat(dashboard): implement user home screen | implement user home screen | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 17e01c2 | feat(auth): implement user registration form | implement user registration form | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | 8a81a87 | feat(auth): add login modal for RentBuild | add login modal for RentBuild | 16/09/2026 |
| RentBuild/Landing-Page | feature/app-features | dcb16bb | feat(team): add profile photo for Luis Angel Cisneros Salas | add profile photo for Luis Angel Cisneros Salas | 16/09/2026 |

#### 5.2.1.5. Execution Evidence for Sprint Review

Como equipo, lo que logramos en este primer Sprint fue la exitosa implementación de nuestra Landing Page y su posterior despliegue gracias a la herramienta GitHub Pages. A continuación, presentaremos lo logrado a través de imágenes mostrando las principales vistas.

**Landing Page**

Sección principal (Hero):

![Landing Page - Hero](./assets/md-images-chapter5/execution-evidence/landing-01-hero.png)

Sección "Todo el ciclo de alquiler, conectado":

![Landing Page - Ciclo de alquiler](./assets/md-images-chapter5/execution-evidence/landing-02-rental-cycle.png)

Sección "Funciones para gestionar mejor tus equipos":

![Landing Page - Funciones](./assets/md-images-chapter5/execution-evidence/landing-03-features.png)

Sección "Mayor control sobre cada alquiler":

![Landing Page - Mayor control](./assets/md-images-chapter5/execution-evidence/landing-04-control.png)

Sección "Funciones RentBuild":

![Landing Page - Funciones RentBuild](./assets/md-images-chapter5/execution-evidence/landing-05-features-video.png)

Sección "Nuestro equipo":

![Landing Page - Nuestro equipo](./assets/md-images-chapter5/execution-evidence/landing-06-team.png)

Sección "RentBuild: Simplificando el alquiler y la gestión de equipos":

![Landing Page - Sobre RentBuild](./assets/md-images-chapter5/execution-evidence/landing-07-about.png)

Sección "Planes que crecen con tu negocio":

![Landing Page - Planes](./assets/md-images-chapter5/execution-evidence/landing-08-plans.png)

Sección "Contáctanos":

![Landing Page - Contáctanos](./assets/md-images-chapter5/execution-evidence/landing-09-contact.png)

**Web Application**

Inicio de sesión:

![Web Application - Login](./assets/md-images-chapter5/execution-evidence/app-01-login.png)

Registro de cuenta:

![Web Application - Registro](./assets/md-images-chapter5/execution-evidence/app-02-register.png)

Perfil de usuario:

![Web Application - Perfil](./assets/md-images-chapter5/execution-evidence/app-03-profile.png)

Inventario de maquinaria:

![Web Application - Inventario](./assets/md-images-chapter5/execution-evidence/app-04-inventory.png)

Registro de nueva maquinaria:

![Web Application - Registrar maquinaria](./assets/md-images-chapter5/execution-evidence/app-05-register-machinery.png)

Mis solicitudes de alquiler:

![Web Application - Mis solicitudes](./assets/md-images-chapter5/execution-evidence/app-06-my-requests.png)

Alquileres activos:

![Web Application - Alquileres activos](./assets/md-images-chapter5/execution-evidence/app-07-active-rentals.png)

Registro de mantenimiento o incidencia:

![Web Application - Mantenimiento e incidencias](./assets/md-images-chapter5/execution-evidence/app-08-maintenance.png)

Historial de maquinaria:

![Web Application - Historial](./assets/md-images-chapter5/execution-evidence/app-09-history.png)

Catálogo de maquinaria:

![Web Application - Catálogo](./assets/md-images-chapter5/execution-evidence/app-10-catalog.png)

#### 5.2.1.6. Services Documentation Evidence for Sprint Review

Dado que el alcance del Sprint 1 se centró en el desarrollo de la primera versión del Landing Page, no se contempló en este sprint la implementación de Web Services. Por consiguiente, no se cuenta aún con endpoints documentados. La documentación de servicios mediante OpenAPI Specification se incorporará a partir de los sprints correspondientes al desarrollo del RESTful API.

#### 5.2.1.7. Software Deployment Evidence for Sprint Review

En esta sección se resumen las actividades realizadas por el equipo en relación con el despliegue de MaquiGest durante el Sprint 1. Estas actividades incluyeron la creación de cuentas en el proveedor de hosting vercel, la configuración de los recursos necesarios y el despliegue de la primera versión del Landing Page. A continuación, se presentan capturas de pantalla que evidencian los pasos realizados durante este proceso.

**1.** Ingresando a la cuenta le damos click a *Add New* para añadir un proyecto.

![Paso 1 - Add New](./assets/md-images-chapter5/deployment-evidence/step-1-add-new.png)

**2.** Le damos click en *Project* para generar un proyecto.

![Paso 2 - Project](./assets/md-images-chapter5/deployment-evidence/step-2-project.png)

**3.** Le damos click en el proyecto que deseamos importar.

![Paso 3 - Import Git Repository](./assets/md-images-chapter5/deployment-evidence/step-3-import-repository.png)

**4.** Nos aparecerá el siguiente recuadro para poder hacer el deploy.

![Paso 4 - Deploy](./assets/md-images-chapter5/deployment-evidence/step-4-deploy.png)

**5.** Finalmente ya tenemos nuestra Landing Page desplegada.

![Paso 5 - Proyecto creado en Vercel](./assets/md-images-chapter5/deployment-evidence/step-5a-project-created.png)

![Paso 5 - Production Deployment](./assets/md-images-chapter5/deployment-evidence/step-5b-production-deployment.png)

![Paso 5 - Landing Page desplegada](./assets/md-images-chapter5/deployment-evidence/step-5c-landing-page-live.png)

#### 5.2.1.8. Team Collaboration Insights during Sprint

En esta sección se explica cómo se desarrollaron las actividades de implementación del Landing Page durante el Sprint 1, evidenciando la participación colaborativa de todos los integrantes del equipo. A continuación, se presentan capturas de los analíticos de colaboración y commits en GitHub correspondientes al repositorio del proyecto, en los que se refleja el aporte individual de cada miembro del equipo.

# Conclusiones

## Conclusiones y recomendaciones

**Problema y segmentos.** El análisis del sector (Clements, 2025, indica que el 67 % de las empresas de alquiler opera con sistemas parcialmente integrados que requieren transferencia manual de información) y el User Task Matrix apuntan en la misma dirección. En ambos segmentos, las tareas de mayor frecuencia e importancia son verificar la disponibilidad de los equipos y dar seguimiento a las fechas de devolución. Ambos dependen además del teléfono y de WhatsApp. Esto respalda el Problem Statement y la necesidad de una solución digital centralizada.

1. **Diferenciación.** El análisis competitivo frente a Booqable, Rentman y Odoo Rental mostró un espacio para una plataforma más especializada y simple. RentBuild se enfoca en maquinaria para construcción y en el ciclo completo (reserva, alquiler, entrega, devolución, inspección y mantenimiento), sin la complejidad de plataformas de mayor escala.
2. **Producto del Sprint 1.** El equipo alcanzó el Sprint Goal. Se desarrolló la primera versión del Landing Page con HTML, CSS y JavaScript, a partir de los wireframes y mock-ups de Figma, y se desplegó en Vercel con acceso público. También se implementaron las pantallas iniciales de la Web Application: usuarios (registro, login y perfil), inventario de maquinaria, catálogo y búsqueda, solicitudes de alquiler y mantenimiento e incidencias. Las 23 tareas planificadas del Sprint Backlog se completaron dentro del sprint, con los 59 story points comprometidos, lo que cumple el alcance planificado para esta entrega.
3. **Trabajo en equipo y liderazgo compartido.** El equipo estableció una meta común mediante el Sprint Goal y planificó las tareas con responsables por aspecto en la matriz LACX, donde el liderazgo se repartió entre los integrantes (diseño y maquetación, desarrollo de la Web Application y despliegue). Esta división permitió avanzar en paralelo sin bloqueos. Las ramas de GitFlow, los Conventional Commits y el tablero de Trello dieron trazabilidad al trabajo y permiten que cualquier integrante continúe las tareas de otro.
4. **Mejora continua.** En la retrospectiva el equipo identificó una oportunidad de mejora: la herramienta de despliegue debió definirse antes. La integración de la lógica de negocio en algunas pantallas fue el mayor reto del sprint y se resolvió sobre la marcha. Estos aprendizajes, junto con la retroalimentación del docente, se incorporarán en las siguientes versiones de los artefactos.

**Recomendaciones**

1. Para TB1, desplegar la primera versión de la Web Application e iniciar el RESTful API con ASP.NET Core y su documentación en OpenAPI, como pide el enunciado.
2. Organizar el RESTful API por los Bounded Contexts del Design-Level EventStorming y aplicar los principios de RESTful en las URLs y los verbos HTTP.
3. Incluir pruebas unitarias y de integración o aceptación en el repositorio de Web Services.
4. Priorizar en el Sprint 2 las funcionalidades que aún no existen: reservas con verificación de conflictos de disponibilidad, contratos y pagos, y suscripciones con los tres niveles de plan definidos en los assumptions.
5. Implementar alertas de fechas de devolución y un dashboard operativo con disponibilidad, alquileres activos y mantenimientos. Son las tareas de mayor frecuencia e importancia del User Task Matrix.
6. Usar como servicio externo de terceros un canal de notificaciones (WhatsApp o correo electrónico), ya que ambos segmentos dependen de esos medios. Así se cumple el requisito del enunciado con una integración que aporta valor real.
7. Aplicar inglés como idioma por defecto en la interfaz y la documentación, con soporte para es_419 y atributos ARIA. Publicar además los términos y condiciones y la protección de privacidad en el footer del Landing Page y de la Web Application.
8. Verificar que los call-to-action de cada segmento en el Landing Page redirijan a la vista correspondiente de la Web Application, con un estilo visual consistente entre ambos.

# Video About-The-Team

# Bibliografía

Brandolini, A. (2013). *Introducing EventStorming*. Leanpub.

Clements, K. (2025, January 25). *The 2025 state of rental technology report*. Quipli. https://www.quipli.com/resources/2025-state-of-rental-report/

Cohn, M. (2004). *User stories applied: For agile software development*. Addison-Wesley.

Cohn, M. (2005). *Agile estimating and planning*. Prentice Hall.

Cooper, A., Reimann, R., Cronin, D., & Noessel, C. (2014). *About face: The essentials of interaction design* (4th ed.). Wiley.

Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley.

Garrett, J. J. (2011). *The elements of user experience: User-centered design for the web and beyond* (2nd ed.). New Riders.

Gothelf, J., & Seiden, J. (2016). *Lean UX: Designing great products with agile teams* (2nd ed.). O'Reilly Media.

Gray, D., Brown, S., & Macanufo, J. (2010). *Gamestorming: A playbook for innovators, rulebreakers, and changemakers*. O'Reilly Media.

Newman, S. (2021). *Building microservices: Designing fine-grained systems* (2nd ed.). O'Reilly Media.

Ries, E. (2011). *The lean startup: How today's entrepreneurs use continuous innovation to create radically successful businesses*. Crown Business.

Schwaber, K., & Sutherland, J. (2020). *The Scrum guide: The definitive guide to Scrum*. Scrum.org. https://scrumguides.org/

# Anexos

**Web Applications Mock-ups:** https://www.figma.com/design/OIBiedVSqvMmmqYcjx14Ec/Sin-t%C3%ADtulo?node-id=0-1&t=qrleaHn5r7IHGSxf-1

**Lean UX Canvas:** https://www.figma.com/board/OcVqiqyfAERGRZHmmTNKMI/Sin-t%C3%ADtulo?node-id=0-1&t=bgNbwgpxLyQB1bi2-1

**Trello:** https://trello.com/invite/b/6aacc6b9cc0413f772436a35/ATTI72782e0013e72d3ec63864ccbd335c7099570315/dataflux

**Miro:** https://miro.com/welcomeonboard/bXFFSkpkdTBCYnBvUTdtSEJJT242NnpTQ0pTTTA4dWdleTJ2QTN0YmZRcUsrRmR4RjZ2ODBvb0JsdzJMZXVlbjljK1RPWFBpNjBPWHFZSWhhNkQwQ1hNczRUelBUWlJSenZCcml6aERpZG1RTFZ5WDZZUk42cjZPVXQ2RVUyR1ZBS2NFMDFkcUNFSnM0d3FEN050ekl3PT0hdjE=?share_link_id=904943457433

**Web Applications WireFlow:** https://www.figma.com/board/x7IvCSgobEyo1SbH3PRnqg/Rent-Build-WireFlow?t=TBFB1usHt4A4XCnH-1

**Segmento Objetivo 1:** https://app.creately.com/d/QwlCIfA0o0k/edit

**Segmento Objetivo 2:** https://app.creately.com/d/DyKHPyVwNtd/edit

**Class Diagrams:** PlantUML://www.plantuml.com/plantuml/png/XLBThjCm3BxFKqIz0g4ZmHkSewsWNI0X9Xx0IxrYaTZ5SIOnnBj3fgvhrOrpqzhnz_D5yNCsK2ifklo3U025v4E4d5_Cb0x5S1U4ztH6_zwvoyItFmiDudyxxzzHLxyiwQ1Ogm26lIX1RJ0RT58h0wKZR0d6YM9FsHJqpTlQ3kKGAO2sl063ABsCvogzGWBz36p8b0ZPwkpFDSjNpAWd22Gy3tJ4y1rsJ85aQZyIBqC5uIDf0fqBliH_jukeAxMMJR67gT_YIMAfnajLggvLSt7F6tfkjX4s1PCjthCDmXrL2kR9zHCoAjJ3cyeNw6NEIy8cbm9DEfcuDqQR1iKCzsqLpi9x2GHnnTW8PzCIJ1HUvNpB1PGUB8hA1RbEqdne_DEJRnBmh-QwQ-wU_n8vsmGtEZz6U3SA_mSnRqPO_Kr1tLJDfkiNTGzkLb_DFIDt9SM_

**Database Diagrams:** PlantUML://www.plantuml.com/plantuml/png/fPH1hjiW48Rtd09bMSaNgA8egswwwGsiAKoSKO5n0KVAYz_T7maESMpBIlGs5lppo_FzUCm-HF2niqQ4V-HQy62b8OVntA9a7uyi1Bf8yImt-B-ZbiD6Gf33Mbw4b3yaQVbJaejok_tpUxTBMbMbXsFxrsCgXUZ9DKbH4B5XJp0MCJ5e7Yk9YGvGQu9irQZ8WhbwRUinG0qc0HZqzQZrhslhpmTlCg8_WI9scAcVb7Ns0weZrEGecQy42Roe1t95cjCFPpCZUy0hTidSgSWU5cnTwC0JhqMxnnzobUrBeT15ZmrCKsayiUbItBLmuoDS0rISca3aKBxK3NGkhmCdlwRykGf40MxGeOTdu5VceeLccEBRQft09c9-6a6BaJNFSDvZ64PXSZmpTPtDmmUxEh0YC8LdiSjuudBqvT8t-msJcplapVjtXEV9osU7qlTLnPTo1udbB8DjyjEBWhLSlhzqkJhUPa_VZ_y-KTQbEX_vgOalUH357ftkhFa2

**Figma:** https://www.figma.com/design/OIBiedVSqvMmmqYcjx14Ec/Sin-t%C3%ADtulo?node-id=0-1&t=DNCxdsFf6vB1SXbX-1
