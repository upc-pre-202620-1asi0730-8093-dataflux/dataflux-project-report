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

|   Código   | Nombre completo del integrante  | Descripción de la carrera                                          |                               Fotografía                                | Conocimientos y habilidades                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:----------:|:--------------------------------| :----------------------------------------------------------------- |:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| U20211B198 | Cisneros Salas, Luis            | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |     <img src="assets/md-images-members/luis-angel.jpeg" width="150px" />     | Soy estudiante de Ingeniería de Software interesado en crear soluciones digitales que simplifiquen procesos y resuelvan problemas reales. Actualmente fortalezco mis conocimientos en C#, y cuento con experiencia en C++, Java, JavaScript, HTML y CSS. Me interesa especialmente el desarrollo frontend, las bases de datos y las aplicaciones web. Soy una persona organizada, responsable, de rápido aprendizaje y con facilidad para trabajar en equipo. Busco esta oportunidad para adquirir experiencia y seguir creciendo profesionalmente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| U202410211 | Manosalva Tovar, Miroslav       | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas | <img src="assets/md-images-members/miroslav-manosalva.jpeg" width="150px" /> | Soy Miroslav Manosalva Tovar, estudiante de Ingeniería de Software. Tengo conocimientos en el área de programación y experiencia en la elaboración de interfaces de usuario (UI), que puedo aportar al desarrollo de RentBuild. Mi experiencia trabajando con interfaces me permite contribuir a la presentación de la información y a la organización visual de las funcionalidades de la plataforma. Me considero una persona responsable y persistente: procuro cumplir con las actividades que asumo y mantener el esfuerzo cuando encuentro dificultades. En este proyecto, busco aplicar mis conocimientos de programación y diseño de interfaces, seguir fortaleciendo mi formación y contribuir al desarrollo de una solución útil para sus usuarios.                                                                                                                                                                                                                                                                 |
| U202111529 | Montalvo Vasquez, Bruno Rodrigo | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |   <img src="assets/md-images-members/bruno-montalvo.png" width="150px" />    | Soy Bruno Rodrigo Montalvo Vasquez, estudiante de la carrera de Ingeniería de Software. Me encuentro interesado y motivado por aprender nuevos temas relacionados con mi carrera. Asimismo, estoy abierto a trabajar con profesionales de mi área académica para mejorar mis conocimientos, adquirir experiencia y fortalecer mis habilidades de trabajo en equipo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| U20211F962 | Vargas Manchinelli, Deiby Juan  | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |    <img src="assets/md-images-members/deiby-vargas.jpeg" width="150px" />    | Estudio Ingeniería de Software y me apasiona usar la tecnología para convertir problemas en soluciones prácticas. Actualmente estoy aprendiendo y fortaleciendo mis conocimientos en C#, además de tener experiencia con C++, Java, JavaScript, HTML y CSS. Me interesa el frontend, las bases de datos y el desarrollo web. Soy organizado, aprendo rápido y disfruto trabajar en equipo. Mi objetivo es ganar experiencia, aprender y seguir creciendo en el mundo del software.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| U202322849 | Viza Quispe, Marlon Packard     | Ingeniería de Software - Universidad Peruana de Ciencias Aplicadas |    <img src="assets/md-images-members/marlon-viza.jpeg" width="150px" />     | Soy estudiante de Ingeniería de Software con interés en el desarrollo web, frontend y bases de datos. Tengo experiencia con C++, Java, JavaScript, HTML y CSS, y actualmente estoy fortaleciendo mis conocimientos en C#. Me motiva crear soluciones útiles y eficientes, aprender constantemente y enfrentar nuevos desafíos. Me considero una persona organizada, creativa y con buena capacidad para trabajar en equipo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

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

### 2.1.2. Estrategias y tácticas frente a competidores

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

### 2.2.3. Análisis de entrevistas

## 2.3. Needfinding

### 2.3.1. User Personas

El user persona se construyó a partir de patrones encontrados en las entrevistas

**Segmento objetivo 1: Pequeñas y medianas empresas de alquiler de maquinaria**
![User Persona 1](./assets/md-images-chapter2/user-persona-armando-casas.png)

**Segmento Objetivo 2: Pequeñas empresas constructoras**
![User Persona 2](./assets/md-images-chapter2/user-persona-andrea-torres.png)

### 2.3.2. User Task Matrix

| TASK | Armando Casas (Empresa de alquiler) Frecuencia | Armando Casas (Empresa de alquiler) Importancia | Andrea Torres (Empresa constructora) Frecuencia | Andrea Torres (Empresa constructora) Importancia |
| :---- | :---: | :---: | :---: | :---: |
| **Consultar el inventario de maquinaria** | **Often** | **High** | **Sometimes** | **Medium** |
| **Consultar la disponibilidad de una maquinaria** | **Often** | **High** | **Often** | **High** |
| **Registrar o actualizar información de maquinaria** | **Often** | **High** | **Rarely** | **Low** |
| **Gestionar reservas y solicitudes de alquiler** | **Often** | **High** | **Often** | **High** |
| **Coordinar la entrega de maquinaria** | **Often** | **High** | **Often** | **High** |
| **Registrar la devolución de maquinaria** | **Often** | **High** | **Sometimes** | **Medium** |
| **Verificar el estado de la maquinaria después de un alquiler** | **Often** | **High** | **Sometimes** | **Medium** |
| **Registrar incidentes o daños en una maquinaria** | **Sometimes** | **High** | **Sometimes** | **High** |
| **Consultar el historial de mantenimiento de una maquinaria** | **Often** | **High** | **Rarely** | **Medium** |
| **Programar o registrar mantenimientos** | **Sometimes** | **High** | **Rarely** | **Low** |
| **Buscar maquinaria según las necesidades de un proyecto** | **Rarely** | **Low** | **Often** | **High** |
| **Consultar características y condiciones de una maquinaria** | **Sometimes** | **Medium** | **Often** | **High** |
| **Realizar seguimiento del estado de una solicitud o alquiler** | **Often** | **High** | **Often** | **High** |

### 2.3.3. User Journey Mapping

![User Journey Map](./assets/md-images-chapter2/user-journey-map1.png)

**2. User Journey Map para el segundo segmento**

![User Journey Map](./assets/md-images-chapter2/user-journey-map2.png)

### 2.3.4. Empathy Mapping

**1. Empathy Map para el primer segmento**

![Empathy Map](./assets/md-images-chapter2/empathy-map1.png)

**2. Empathy Map para el segundo segmento**

![Empathy Map](./assets/md-images-chapter2/empathy-map2.png)

## 2.4. Big Picture Event Storming

## 2.5. Ubiquitous Language

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
<td>EP02</td>
<td>Gestión de maquinaria</td>
<td>Epic orientado al registro, organización y consulta del inventario de maquinaria disponible para alquiler.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US04</td>
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
<td>US05</td>
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
<td>US06</td>
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
<td>US07</td>
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
<td>US08</td>
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
<td>US09</td>
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
<td>US10</td>
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
<td>US11</td>
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
<td>US12</td>
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
<td>Gestión de reservas y alquileres</td>
<td>Epic orientado a la administración de reservas y al seguimiento del ciclo de alquiler de los equipos.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US13</td>
<td>Gestionar solicitudes de alquiler</td>
<td>Como empresa de alquiler, quiero revisar las solicitudes recibidas para decidir cuáles atender y mantener control sobre mis alquileres.</td>
<td>
Given que existen solicitudes de alquiler<br>
When el usuario consulta las solicitudes<br>
Then el sistema muestra la información de cada solicitud<br>
And permite identificar su estado
</td>
<td>EP04</td>
</tr>

<tr>
<td>US14</td>
<td>Confirmar o rechazar una solicitud</td>
<td>Como empresa de alquiler, quiero aceptar o rechazar solicitudes de alquiler para controlar la disponibilidad de mis equipos.</td>
<td>
Given que existe una solicitud pendiente<br>
When el usuario selecciona aceptar o rechazar<br>
Then el sistema actualiza el estado de la solicitud<br>
And muestra el nuevo estado
</td>
<td>EP04</td>
</tr>

<tr>
<td>US15</td>
<td>Consultar alquileres activos</td>
<td>Como empresa de alquiler, quiero consultar mis alquileres activos para conocer qué equipos están actualmente alquilados.</td>
<td>
Given que existen alquileres activos<br>
When el usuario consulta sus alquileres<br>
Then el sistema muestra los equipos alquilados<br>
And muestra información del periodo correspondiente
</td>
<td>EP04</td>
</tr>

<tr>
<td>US16</td>
<td>Consultar estado de una solicitud de alquiler</td>
<td>Como empresa constructora, quiero consultar el estado de mi solicitud para saber si mi alquiler fue aceptado, rechazado o aún está pendiente.</td>
<td>
Given que el usuario ha realizado una solicitud<br>
When consulta sus solicitudes<br>
Then el sistema muestra el estado actualizado de cada una
</td>
<td>EP04</td>
</tr>

<tr>
<td>US17</td>
<td>Gestionar entregas y devoluciones</td>
<td>Como empresa de alquiler, quiero registrar las entregas y devoluciones de maquinaria para mantener trazabilidad sobre los equipos alquilados.</td>
<td>
Given que existe un alquiler confirmado<br>
When se registra la entrega o devolución<br>
Then el sistema actualiza el estado del alquiler<br>
And registra la operación realizada
</td>
<td>EP04</td>
</tr>

<tr>
<td>EP05</td>
<td>Gestión de mantenimiento e incidencias</td>
<td>Epic orientado al seguimiento del estado operativo de la maquinaria y a la gestión de mantenimientos e incidencias.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US18</td>
<td>Registrar mantenimiento</td>
<td>Como empresa de alquiler, quiero registrar mantenimientos realizados a una maquinaria para mantener un historial de su estado operativo.</td>
<td>
Given que existe una maquinaria registrada<br>
When el usuario registra un mantenimiento<br>
Then el sistema almacena la información<br>
And la relaciona con el equipo correspondiente
</td>
<td>EP05</td>
</tr>

<tr>
<td>US19</td>
<td>Programar mantenimiento</td>
<td>Como empresa de alquiler, quiero programar mantenimientos para evitar que los equipos sean utilizados cuando requieren atención.</td>
<td>
Given que una maquinaria requiere mantenimiento<br>
When el usuario registra una fecha de mantenimiento<br>
Then el sistema guarda la programación<br>
And permite consultar el mantenimiento pendiente
</td>
<td>EP05</td>
</tr>

<tr>
<td>US20</td>
<td>Registrar incidencia de maquinaria</td>
<td>Como empresa de alquiler, quiero registrar incidencias de mis equipos para llevar un control de problemas y reparaciones.</td>
<td>
Given que una maquinaria presenta una incidencia<br>
When el usuario registra el problema<br>
Then el sistema almacena la incidencia<br>
And la relaciona con la maquinaria correspondiente
</td>
<td>EP05</td>
</tr>

<tr>
<td>US21</td>
<td>Consultar historial de maquinaria</td>
<td>Como empresa de alquiler, quiero consultar el historial de una maquinaria para conocer sus alquileres, incidencias y mantenimientos.</td>
<td>
Given que existe una maquinaria registrada<br>
When el usuario consulta su historial<br>
Then el sistema muestra las operaciones asociadas al equipo
</td>
<td>EP05</td>
</tr>

<tr>
<td>EP06</td>
<td>Información y contratación del servicio</td>
<td>Epic orientado a brindar información sobre RentBuild y facilitar el contacto de potenciales clientes con la plataforma.</td>
<td>-</td>
<td>-</td>
</tr>

<tr>
<td>US22</td>
<td>Consultar información de RentBuild</td>
<td>Como visitante, quiero conocer las funcionalidades y beneficios de RentBuild para determinar si la solución se adapta a las necesidades de mi empresa.</td>
<td>
Given que el visitante accede al Landing Page<br>
When revisa la información del producto<br>
Then el sistema muestra sus principales funcionalidades y beneficios
</td>
<td>EP06</td>
</tr>

<tr>
<td>US23</td>
<td>Solicitar demostración</td>
<td>Como potencial cliente, quiero solicitar una demostración de RentBuild para conocer cómo funciona antes de utilizar el servicio.</td>
<td>
Given que el visitante desea conocer la plataforma<br>
When completa y envía el formulario de demostración<br>
Then el sistema registra la solicitud<br>
And muestra un mensaje de confirmación
</td>
<td>EP06</td>
</tr>

<tr>
<td>US24</td>
<td>Contactar con RentBuild</td>
<td>Como potencial cliente, quiero contactar con el equipo de RentBuild para realizar consultas sobre el servicio.</td>
<td>
Given que el visitante accede a la sección de contacto<br>
When completa y envía sus datos y consulta<br>
Then el sistema registra la solicitud de contacto
</td>
<td>EP06</td>
</tr>

</table>

## 3.2. Impact Mapping

![Impact Mapping](./assets/md-images-chapter3/impact-mapping.png)

## 3.3. Product Backlog

# Capítulo IV: Product Design

## 4.1. Style Guidelines

### 4.1.1. General Style Guidelines

### 4.1.2. Web Style Guidelines

## 4.2. Information Architecture

### 4.2.1. Organization Systems

### 4.2.2. Labeling Systems

### 4.2.3. SEO Tags and Meta Tags

### 4.2.4. Searching Systems

### 4.2.5. Navigation Systems

## 4.3. Landing Page UI Design

### 4.3.1. Landing Page Wireframe

### 4.3.2. Landing Page Mock-up

## 4.4. Web Applications UX/UI Design

### 4.4.1. Web Applications Wireframes

### 4.4.2. Web Applications Wireflow Diagrams

### 4.4.3. Web Applications Mock-ups

### 4.4.4. Web Applications User Flow Diagrams

## 4.5. Web Applications Prototyping

## 4.6. Domain-Driven Software Architecture

### 4.6.1. Design-Level Event Storming

### 4.6.2. Software Architecture Context Diagram

### 4.6.3. Software Architecture Container Diagrams

### 4.6.4. Software Architecture Components Diagrams

Los diagramas de componentes de arquitectura de software presentan una vista detallada de la organización interna de los principales contenedores frontend y backend que conforman RentBuild.

A nivel de frontend, la Single Page Application desarrollada con Angular se organiza alrededor de los bounded contexts definidos para la solución: IAM, Profiles, Inventory, Rentals, Maintenance y Subscriptions. Adicionalmente, Shared Frontend concentra componentes, modelos y capacidades técnicas transversales reutilizables por los diferentes contextos de la aplicación. Una vista general de componentes muestra cómo estos elementos se integran dentro de la aplicación frontend, mientras que los diagramas individuales permiten observar su organización interna mediante las capas Presentation, Application, Domain e Infrastructure, según corresponda.

Además, para cada bounded context del frontend se presenta una vista detallada basada en las capas DDD Presentation, Application, Domain e Infrastructure. Estas vistas permiten identificar los componentes internos, sus responsabilidades, tecnologías y relaciones. Complementariamente, se mantiene una vista específica de la Presentation Layer, donde se muestran con mayor detalle los componentes Angular responsables de las páginas, formularios, vistas y elementos de interfaz correspondientes.

A nivel de backend, la RESTful API desarrollada con Java y Spring Boot mantiene la misma organización basada en bounded contexts. Una vista general presenta los contextos contenidos dentro de la aplicación backend, mientras que los diagramas individuales descomponen cada bounded context en las capas Interfaces, Application, Domain e Infrastructure siguiendo principios de Domain-Driven Design.

A continuación, se presentan las diferentes vistas de componentes que conforman la arquitectura de RentBuild.

#### Frontend General Components Diagram

El Frontend General Components Diagram presenta la organización general de la Single Page Application de RentBuild. El frontend está implementado con Angular y se estructura alrededor de los bounded contexts definidos para el dominio del negocio.

Los mecanismos de layout y routing de la aplicación permiten coordinar la navegación hacia IAM, Profiles, Inventory, Rentals, Maintenance y Subscriptions. Asimismo, Shared Frontend proporciona capacidades reutilizables de interfaz y servicios transversales, mientras que la infraestructura del frontend permite la comunicación con la RentBuild Backend API.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-general-component-diagram.png"
       alt="RentBuild Frontend General Components Diagram"
       width="95%">
</p>

#### IAM Frontend Components Diagram

El bounded context IAM del frontend es responsable de las funcionalidades relacionadas con autenticación, registro, recuperación de contraseña, gestión de sesión y acceso a la cuenta.

La Presentation Layer administra las vistas y las interacciones relacionadas con la autenticación. La Application Layer coordina los flujos de autenticación y el estado de sesión. La Domain Layer contiene los modelos y reglas del frontend asociados con autenticación, mientras que la Infrastructure Layer proporciona la comunicación con los servicios de autenticación del backend y mecanismos técnicos como la persistencia de sesión.

IAM también proporciona información de la cuenta autenticada a otros contextos del frontend y utiliza las capacidades compartidas proporcionadas por Shared Frontend.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-iam-component-diagram.png"
       alt="RentBuild IAM Frontend Components Diagram"
       width="90%">
</p>


#### IAM Frontend Detailed Component Diagram

El IAM Frontend Detailed Component Diagram presenta una vista más completa de la organización interna del bounded context IAM, integrando las capas Presentation, Application, Domain e Infrastructure y mostrando las relaciones existentes entre sus componentes.

La Presentation Layer está conformada por `LoginComponent`, `RegisterComponent` y `RecoverPasswordComponent`, responsables de las principales interacciones relacionadas con autenticación, registro y recuperación de contraseña.

La Application Layer coordina los casos de uso y el estado asociado con los procesos de autenticación y gestión de sesión. La Domain Layer concentra los modelos y reglas vinculados con credenciales, sesión y conceptos propios del contexto IAM. Por su parte, la Infrastructure Layer permite consumir los servicios REST expuestos por la RentBuild Backend API y transformar los recursos recibidos en modelos utilizados por el frontend.

Este nivel de detalle permite observar cómo los componentes de presentación delegan las operaciones a la capa de aplicación, cómo esta coordina el acceso a infraestructura y dominio, y cómo la infraestructura establece la comunicación con los servicios backend.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/IAM-Frontend-Detailed.png"
       alt="RentBuild IAM Frontend Detailed Component Diagram"
       width="95%">
</p>

#### Profiles Frontend Components Diagram

El bounded context Profiles del frontend administra la información relacionada con los perfiles de usuarios, empresas y proveedores.

La Presentation Layer contiene las vistas y formularios asociados con los perfiles. La Application Layer coordina las consultas y operaciones de actualización, mientras que la Domain Layer contiene los modelos y reglas correspondientes. La Infrastructure Layer se encarga de la comunicación con los endpoints de Profiles disponibles en el backend.

Este bounded context también utiliza la información de la cuenta autenticada proporcionada por IAM y las capacidades comunes proporcionadas por Shared Frontend.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-profiles-component-diagram.png"
       alt="RentBuild Profiles Frontend Components Diagram"
       width="90%">
</p>

#### Profiles Frontend Detailed Component Diagram

El Profiles Frontend Detailed Component Diagram presenta una vista más completa de la organización interna del bounded context Profiles, integrando las capas Presentation, Application, Domain e Infrastructure y mostrando las relaciones entre sus componentes.

La Presentation Layer está conformada por `ProfileComponent`, `EditProfileComponent` y `CompanyProfileComponent`, responsables de visualizar y actualizar la información correspondiente a los perfiles de usuarios y empresas.

La Application Layer coordina las consultas, actualizaciones y el estado relacionado con la gestión de perfiles. La Domain Layer concentra los modelos y reglas asociados con usuarios, empresas y perfiles. Por su parte, la Infrastructure Layer permite consumir los servicios REST expuestos por la RentBuild Backend API y transformar los recursos recibidos en modelos utilizados por el frontend.

Este nivel de detalle permite observar cómo los componentes de presentación delegan las operaciones a la capa de aplicación, cómo esta coordina el acceso al dominio y a la infraestructura, y cómo la infraestructura establece la comunicación con los servicios backend relacionados con Profiles.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/Profiles-Frontend-Detailed.png"
       alt="RentBuild Profiles Frontend Detailed Component Diagram"
       width="95%">
</p>

#### Inventory Frontend Components Diagram

El bounded context Inventory del frontend administra el catálogo de maquinaria, los detalles de los equipos, sus categorías, tarifas, estado operativo y disponibilidad.

Su Application Layer coordina los flujos relacionados con la gestión y consulta del inventario, comunicándose con las capas Domain e Infrastructure. Inventory también proporciona información sobre maquinaria y disponibilidad requerida por Rentals y coordina con Maintenance los cambios relacionados con el estado de los equipos.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-inventory-component-diagram.png"
       alt="RentBuild Inventory Frontend Components Diagram"
       width="90%">
</p>

#### Inventory Frontend Detailed Component Diagram

El Inventory Frontend Detailed Component Diagram presenta una vista más completa de la organización interna del bounded context Inventory, integrando las capas Presentation, Application, Domain e Infrastructure y mostrando las relaciones entre sus componentes.

La Presentation Layer está conformada por `EquipmentListComponent`, `EquipmentDetailComponent`, `EquipmentFormComponent`, `EquipmentSearchComponent`, `EquipmentFilterComponent` y `AvailabilityBadgeComponent`. Estos componentes soportan las principales interacciones relacionadas con consulta, detalle, registro, edición, búsqueda, filtrado y visualización de disponibilidad de maquinaria.

La Application Layer coordina los casos de uso y el estado asociado con la gestión del inventario. La Domain Layer concentra los modelos y reglas relacionados con equipos, categorías, tarifas, disponibilidad y estado operativo. Por su parte, la Infrastructure Layer permite consumir los servicios REST expuestos por la RentBuild Backend API y transformar los recursos recibidos en modelos utilizados por el frontend.

Este nivel de detalle permite observar cómo los componentes de presentación delegan las operaciones a la capa de aplicación, cómo esta coordina el acceso al dominio y a la infraestructura, y cómo la infraestructura establece la comunicación con los servicios backend correspondientes al contexto Inventory.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/Inventory-Frontend-Detailed.png"
       alt="RentBuild Inventory Frontend Detailed Component Diagram"
       width="95%">
</p>

#### Rentals Frontend Components Diagram

El bounded context Rentals del frontend soporta la interacción correspondiente al ciclo de alquiler, incluyendo solicitudes de alquiler, reservas, entregas, alquileres activos y devoluciones.

Este contexto utiliza la información de los equipos y su disponibilidad proporcionada por Inventory, así como la información de empresas y participantes administrada por Profiles. Su Infrastructure Layer se encarga de la comunicación con los endpoints de Rentals expuestos por el backend.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-rentals-component-diagram.png"
       alt="RentBuild Rentals Frontend Components Diagram"
       width="90%">
</p>

#### Rentals Frontend Detailed Component Diagram

El Rentals Frontend Detailed Component Diagram presenta una vista más completa de la organización interna del bounded context Rentals, integrando las capas Presentation, Application, Domain e Infrastructure y mostrando las relaciones entre sus componentes.

La Presentation Layer está conformada por `RentalRequestsComponent`, `RentalRequestDetailComponent`, `ReservationsComponent`, `ActiveRentalsComponent`, `DeliveryFormComponent` y `ReturnFormComponent`. Estos componentes soportan las principales interacciones relacionadas con solicitudes de alquiler, consulta de detalles, reservas, alquileres activos, entregas y devoluciones de maquinaria.

La Application Layer coordina los casos de uso y el estado asociados con el ciclo de alquiler. La Domain Layer concentra los modelos y reglas relacionados con solicitudes de alquiler, reservas, contratos de alquiler, entregas y devoluciones. Por su parte, la Infrastructure Layer permite consumir los servicios REST expuestos por la RentBuild Backend API y transformar los recursos recibidos en modelos utilizados por el frontend.

Este nivel de detalle permite observar cómo los componentes de presentación delegan las operaciones a la capa de aplicación, cómo esta coordina el acceso al dominio y a la infraestructura, y cómo la infraestructura establece la comunicación con los servicios backend correspondientes al contexto Rentals.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/Rentals-Frontend-Detailed.png"
       alt="RentBuild Rentals Frontend Detailed Component Diagram"
       width="95%">
</p>

#### Maintenance Frontend Components Diagram

El bounded context Maintenance del frontend administra las programaciones de mantenimiento, inspecciones, incidencias, registros de mantenimiento e historial de mantenimiento de la maquinaria.

Este contexto colabora con Inventory para reflejar cambios en el estado y disponibilidad de los equipos, y con Rentals cuando una incidencia o actividad de mantenimiento afecta a una maquinaria asociada con un alquiler activo.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-maintenance-component-diagram.png"
       alt="RentBuild Maintenance Frontend Components Diagram"
       width="90%">
</p>

#### Maintenance Frontend Detailed Component Diagram

El Maintenance Frontend Detailed Component Diagram presenta una vista más completa de la organización interna del bounded context Maintenance, integrando las capas Presentation, Application, Domain e Infrastructure y mostrando las relaciones entre sus componentes.

La Presentation Layer está conformada por `MaintenanceListComponent`, `MaintenanceDetailComponent`, `IncidentFormComponent` e `InspectionComponent`. Estos componentes soportan las principales interacciones relacionadas con la consulta de mantenimientos, visualización de detalles, registro de incidencias y gestión de inspecciones de maquinaria.

La Application Layer coordina los casos de uso y el estado asociados con las operaciones de mantenimiento. La Domain Layer concentra los modelos y reglas relacionados con mantenimientos, inspecciones, incidencias, estados de mantenimiento e historial de los equipos. Por su parte, la Infrastructure Layer permite consumir los servicios REST expuestos por la RentBuild Backend API y transformar los recursos recibidos en modelos utilizados por el frontend.

Este nivel de detalle permite observar cómo los componentes de presentación delegan las operaciones a la capa de aplicación, cómo esta coordina el acceso al dominio y a la infraestructura, y cómo la infraestructura establece la comunicación con los servicios backend correspondientes al contexto Maintenance.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/Maintenance-Frontend-Detailed.png"
       alt="RentBuild Maintenance Frontend Detailed Component Diagram"
       width="95%">
</p>

#### Subscriptions Frontend Components Diagram

El bounded context Subscriptions del frontend administra los planes disponibles, la suscripción actual, el estado de la suscripción y los flujos relacionados con la gestión o cambio de plan.

Este contexto utiliza IAM para identificar la cuenta autenticada y Profiles para obtener la información de la empresa asociada con la suscripción. Su Infrastructure Layer se comunica con los servicios correspondientes de Subscriptions disponibles en el backend.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-subscriptions-component-diagram.png"
       alt="RentBuild Subscriptions Frontend Components Diagram"
       width="90%">
</p>

#### Subscriptions Frontend Detailed Component Diagram

El Subscriptions Frontend Detailed Component Diagram presenta una vista más completa de la organización interna del bounded context Subscriptions, integrando las capas Presentation, Application, Domain e Infrastructure y mostrando las relaciones entre sus componentes.

La Presentation Layer está conformada por `PlansComponent`, `CurrentSubscriptionComponent` y `ChangePlanComponent`. Estos componentes soportan las principales interacciones relacionadas con la consulta de planes disponibles, visualización de la suscripción actual y modificación del plan contratado.

La Application Layer coordina los casos de uso y el estado asociados con la gestión de suscripciones. La Domain Layer concentra los modelos y reglas relacionados con suscripciones, planes, períodos de facturación y estados de suscripción. Por su parte, la Infrastructure Layer permite consumir los servicios REST expuestos por la RentBuild Backend API y transformar los recursos recibidos en modelos utilizados por el frontend.

Este nivel de detalle permite observar cómo los componentes de presentación delegan las operaciones a la capa de aplicación, cómo esta coordina el acceso al dominio y a la infraestructura, y cómo la infraestructura establece la comunicación con los servicios backend correspondientes al contexto Subscriptions.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/Subscriptions-Frontend-Detailed.png"
       alt="RentBuild Subscriptions Frontend Detailed Component Diagram"
       width="95%">
</p>

#### Shared Frontend Components Diagram

El Shared Frontend concentra capacidades transversales y reutilizables utilizadas por los diferentes bounded contexts de la Single Page Application de RentBuild.

La Presentation Layer contiene componentes comunes de interfaz como `LayoutComponent`, `NavigationComponent`, `LanguageSwitcherComponent` y `FooterComponent`. Estos elementos proporcionan la estructura visual compartida, la navegación principal, el cambio de idioma y contenido reutilizable entre las diferentes vistas de la aplicación.

La Domain Layer contiene value objects reutilizables que no pertenecen exclusivamente a un bounded context, como `Money` y `DateRange`, permitiendo representar valores comunes mediante objetos autovalidados.

Por su parte, la Infrastructure Layer proporciona mecanismos técnicos compartidos. `ApiClient` centraliza capacidades comunes para la comunicación HTTP con la RentBuild REST API, `AuthInterceptor` incorpora la información de autenticación requerida en las solicitudes salientes y `LocalStorageService` proporciona acceso reutilizable al almacenamiento local del navegador.

De esta manera, Shared Frontend evita duplicar capacidades técnicas y visuales comunes dentro de los bounded contexts y mantiene dichas responsabilidades separadas de los conceptos específicos del dominio.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-frontend-shared-component-diagram.png"
       alt="RentBuild Shared Frontend Components Diagram"
       width="90%">
</p>

#### Backend General Components Diagram

El Backend General Components Diagram presenta la organización general de la RentBuild API Application implementada con Java y Spring Boot.

El contenedor backend está organizado alrededor de seis bounded contexts de negocio: IAM, Profiles, Inventory, Rentals, Maintenance y Subscriptions. Adicionalmente, un componente Shared proporciona capacidades técnicas y transversales reutilizables por los diferentes contextos del backend.

La Single Page Application desarrollada con Angular aparece fuera del límite del backend debido a que actúa como cliente de los servicios REST expuestos por la aplicación. De igual manera, la base de datos MySQL se representa fuera del límite de componentes del backend como el contenedor encargado de la persistencia de la información.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-general-component-diagram.png"
       alt="RentBuild Backend General Components Diagram"
       width="95%">
</p>

#### IAM Backend Component Diagram

El bounded context IAM del backend administra la autenticación, autorización, credenciales, usuarios, roles y control de acceso.

La Interfaces Layer expone los endpoints REST relacionados con autenticación, registro y administración de cuentas. La Application Layer coordina los casos de uso correspondientes y delega las decisiones de negocio a la Domain Layer. Por su parte, la Infrastructure Layer proporciona los mecanismos de persistencia y adaptadores técnicos necesarios.

Las capacidades relacionadas con seguridad son proporcionadas mediante mecanismos como Spring Security, codificación de contraseñas y autenticación basada en tokens. Además, este contexto puede comunicarse con el servicio externo de correo transaccional para soportar operaciones como recuperación de contraseña y notificaciones relacionadas con la cuenta.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-iam-component-diagram.png"
       alt="RentBuild IAM Backend Component Diagram"
       width="90%">
</p>

#### Profiles Backend Component Diagram

El bounded context Profiles del backend administra la información correspondiente a usuarios, empresas, proveedores y clientes.

La Interfaces Layer expone los endpoints REST relacionados con perfiles. La Application Layer coordina operaciones de registro, actualización de perfiles, gestión de información empresarial y consultas.

La Domain Layer contiene los conceptos y reglas de negocio relacionados con los perfiles, mientras que la Infrastructure Layer proporciona las implementaciones de repositorios y mecanismos de persistencia. Profiles también colabora con IAM para identificar la cuenta autenticada asociada con cada perfil.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-profiles-component-diagram.png"
       alt="RentBuild Profiles Backend Component Diagram"
       width="90%">
</p>

#### Inventory Backend Component Diagram

El bounded context Inventory del backend administra la maquinaria, categorías, tarifas, estado operativo y disponibilidad.

La Interfaces Layer expone los endpoints REST correspondientes a la gestión del inventario. La Application Layer coordina el registro y actualización de maquinaria, consultas de disponibilidad, gestión de tarifas y demás operaciones relacionadas con el inventario.

La Domain Layer contiene los conceptos y reglas de negocio asociados con los equipos, mientras que la Infrastructure Layer proporciona las implementaciones de persistencia mediante Spring Data JPA.

Rentals utiliza Inventory para validar la disponibilidad de la maquinaria, mientras que Maintenance interactúa con este contexto cuando las actividades de mantenimiento modifican el estado operativo o la disponibilidad de los equipos.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-inventory-component-diagram.png"
       alt="RentBuild Inventory Backend Component Diagram"
       width="90%">
</p>

#### Rentals Backend Component Diagram

El bounded context Rentals del backend administra el ciclo completo de alquiler, incluyendo solicitudes, reservas, contratos, entregas, alquileres activos y devoluciones.

La Interfaces Layer expone las operaciones REST requeridas por el frontend. La Application Layer coordina los diferentes flujos del alquiler, mientras que la Domain Layer contiene los agregados, entidades, value objects y reglas de negocio correspondientes.

La Infrastructure Layer proporciona las implementaciones necesarias para la persistencia. Rentals colabora con Inventory para verificar la disponibilidad de la maquinaria y con Profiles para obtener la información de las empresas y participantes involucrados en las operaciones de alquiler.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-rentals-component-diagram.png"
       alt="RentBuild Rentals Backend Component Diagram"
       width="90%">
</p>

#### Maintenance Backend Component Diagram

El bounded context Maintenance del backend administra las programaciones de mantenimiento, inspecciones, incidencias, registros de mantenimiento e historial de mantenimiento de la maquinaria.

La Interfaces Layer expone los endpoints REST relacionados con estas operaciones. La Application Layer coordina los casos de uso asociados con programación de mantenimiento, inspecciones, registro de incidencias y actualización de mantenimientos.

La Domain Layer contiene los conceptos y reglas de negocio relacionados con el mantenimiento, mientras que la Infrastructure Layer proporciona las implementaciones de repositorios y mecanismos de persistencia.

Maintenance colabora con Inventory para actualizar el estado y disponibilidad de la maquinaria y con Rentals cuando una actividad de mantenimiento o incidencia afecta a un equipo asociado con un alquiler activo.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-maintenance-component-diagram.png"
       alt="RentBuild Maintenance Backend Component Diagram"
       width="90%">
</p>

#### Subscriptions Backend Component Diagram

El bounded context Subscriptions del backend administra los planes de suscripción, suscripciones activas, cambios de plan, estado de facturación y operaciones relacionadas con pagos.

La Interfaces Layer expone los endpoints REST necesarios para la gestión de suscripciones. La Application Layer coordina la selección de planes, activación de suscripciones, cambios de plan, estado de facturación y operaciones relacionadas con pagos.

La Domain Layer contiene los conceptos y reglas de negocio correspondientes a las suscripciones, mientras que la Infrastructure Layer proporciona los mecanismos de persistencia necesarios.

Este bounded context utiliza IAM para identificar la cuenta autenticada y Profiles para asociar la suscripción con la información de la empresa. Asimismo, un Payment Connector integra el contexto con Stripe para realizar el procesamiento de los pagos correspondientes a las suscripciones.

<p align="center">
  <img src="./assets/md-images-chapter4/c4/components/rentbuild-backend-subscriptions-component-diagram.png"
       alt="rentbuild Subscriptions Backend Component Diagram"
       width="90%">
</p>

## 4.7. Software Object-Oriented Design

### 4.7.1. Class Diagrams

## 4.8. Database Design

### 4.8.1. Database Diagrams

# Capítulo V: Product Implementation, Validation & Deployment

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

### 5.1.2. Source Code Management

### 5.1.3. Source Code Style Guide & Conventions

### 5.1.4. Software Deployment Configuration

## 5.2. Landing Page, Services & Applications Implementation

### 5.2.1. Sprint 1

#### 5.2.1.1. Sprint Planning 1

#### 5.2.1.2. Aspect Leaders and Collaborators

#### 5.2.1.3. Sprint Backlog 1

#### 5.2.1.4. Development Evidence for Sprint Review

#### 5.2.1.5. Execution Evidence for Sprint Review

#### 5.2.1.6. Services Documentation Evidence for Sprint Review

#### 5.2.1.7. Software Deployment Evidence for Sprint Review

#### 5.2.1.8. Team Collaboration Insights during Sprint

# Conclusiones

## Conclusiones y recomendaciones

# Bibliografía

# Anexos