# 🧭 Roadmap General del Proyecto: Validate

Este roadmap define las fases principales para el desarrollo de la plataforma **Validate**, orientada a la verificación de identidad, análisis de perfiles y validación de antecedentes de colaboradores o postulantes.  

---

## ETAPA 1 – ANÁLISIS Y ALCANCE

**Objetivo:**  
Definir el alcance funcional y técnico del sistema, identificando los módulos principales y las dependencias entre ellos.

**Entregables:**
- Documento de alcance funcional con descripción de módulos:
  1. Autenticación / Registro  
  2. Verificación de identidad  
  3. Módulos internos:
     - 360 Identity Check  
     - KYC  
     - Background Check  
     - Face Match  
     - Security Questions  
     - Tests Psicológicos  
  4. Notificaciones  
  5. Pagos  
  6. Analítica  
- Mapa de flujo de usuario (desde registro hasta validación completa).  
- Identificación de APIs externas necesarias (RENIEC, SUNAT, SOAT, etc.).  
- Documento de requerimientos no funcionales (rendimiento, seguridad, escalabilidad).

---

## ETAPA 2 – DISEÑO TÉCNICO Y ARQUITECTURA

**Objetivo:**  
Definir la arquitectura base, los límites entre módulos y la estructura de datos inicial.

**Entregables:**
- Definición de arquitectura **monolito modular con enfoque hexagonal**.  
- Diagrama de módulos y dependencias internas.  
- Diagrama entidad-relación inicial (usuarios, validaciones, resultados, auditoría).  
- Documentación de decisiones tecnológicas (stack, frameworks, librerías).  
- Diseño base de flujos: autenticación, verificación de identidad y procesos de validación.  
- Definición de contratos de API (Swagger o OpenAPI).

---

## ETAPA 3 – CONFIGURACIÓN DEL ENTORNO

**Objetivo:**  
Establecer un entorno de desarrollo reproducible y colaborativo.

**Entregables:**
- Repositorios creados:
  - `/backend` → FastAPI, flask o Django REST Framework  
  - `/frontend` → Angular  
- Configuración de **Docker Compose** (backend, base de datos, Redis, Nginx, frontend).  
- Variables de entorno (`.env.example`) y scripts de instalación local.  
- Pipeline básico CI/CD (GitHub Actions o GitLab CI).  
- Documentación técnica del entorno (`/docs/setup.md`).

---

## ETAPA 4 – BACKEND CORE

**Objetivo:**  
Construir la base del backend y la API central del sistema.

**Entregables:**
- Estructura modular del proyecto:
```plaintext
backend/
├── core/
├── modules/
│ ├── auth/
│ ├── identity/
│ ├── kyc/
│ ├── notifications/
│ ├── payments/
│ └── analytics/
```
- Autenticación JWT (Access + Refresh Tokens).  
- Registro y verificación de usuarios.  
- API base para verificación de identidad.  
- Endpoint de estado del proceso de validación.  
- Documentación de API (Swagger).  
- Tests unitarios base.


---

## ETAPA 5 – FRONTEND CORE

**Objetivo:**  
Desarrollar la interfaz de usuario principal, conectando con la API y representando los procesos de validación.

**Entregables:**
- Estructura modular (Angular).  
- Flujo completo de autenticación (login, registro, recuperación).  
- Componentes principales:
- 360 Identity Check (resumen general del estado de validación).  
- KYC (formulario dinámico con datos personales y documentos).  
- Background Check (historial y resultados).  
- Face Match (captura e integración biométrica).  
- Security Questions (preguntas de seguridad).  
- Test Psicológicos (evaluación básica).  
- Sistema visual de notificaciones (alertas y banners).  
- Conexión con APIs del backend mediante Axios/Fetch.  
- CRUD visual básico para Auth, KYC y Notificaciones.

---

## ETAPA 6 – INTEGRACIONES Y SEGURIDAD

**Objetivo:**  
Integrar APIs externas y reforzar seguridad y validaciones de datos.

**Entregables:**
- Integración con APIs:
- RENIEC / SUNAT / SOAT / SUTRAN / MTC.  
- API biométrica (Face Match / OCR).  
- Pasarela de pagos (ej. Culqi, MercadoPago).  
- Validación extendida de identidad y datos KYC.  
- Roles y permisos (RBAC).  
- Logs de auditoría y monitoreo.  
- Sistema de notificaciones internas (correo, SMS, WebSocket).  

---

## ETAPA 7 – INFRAESTRUCTURA Y DEPLOY

**Objetivo:**  
Preparar la infraestructura de producción y automatizar el despliegue.

**Entregables:**
- Dockerización completa (frontend, backend, DB, Redis, Nginx).  
- Configuración HTTPS + Nginx reverse proxy.  
- Deploy en VPS o servicio cloud (DigitalOcean, AWS, etc.).  
- Backups automáticos, logging y monitoreo básico.  
- Documentación de despliegue (`/docs/deploy.md`).

---

## ETAPA 8 – OPTIMIZACIÓN Y ESCALABILIDAD

**Objetivo:**  
Optimizar rendimiento y preparar módulos para posible separación futura.

**Entregables:**
- Pruebas de carga y estrés (locust / k6).  
- Optimización de queries y endpoints críticos.  
- Implementación de caché con Redis.  
- Identificación de módulos desacoplables (Notificaciones, Face Match, Pagos).  
- Plan de transición hacia arquitectura de microservicios.  

---

## ETAPA 9 – CIERRE Y DOCUMENTACIÓN FINAL

**Objetivo:**  
Consolidar la documentación técnica y funcional del proyecto.

**Entregables:**
- Documentación final del sistema:
- Arquitectura y decisiones técnicas.  
- Estructura de módulos.  
- Endpoints documentados (Swagger + ejemplos).  
- Flujos CI/CD y despliegue.  
- Manual de contribución (`/docs/contributing.md`).  
- Informe técnico de retrospectiva (aprendizajes, mejoras y próximos pasos).

---

## ESTRUCTURA DE DOCUMENTACIÓN SUGERIDA
```plaintext
/docs
├── fases/
│ ├── ETAPA_1_ANALISIS.md
│ ├── ETAPA_2_ARQUITECTURA.md
│ ├── ETAPA_3_ENTORNO.md
│ ├── ETAPA_4_BACKEND.md
│ ├── ETAPA_5_FRONTEND.md
│ ├── ...
├── setup.md
├── deploy.md
└── contributing.md
```