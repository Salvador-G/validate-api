# 📘 Alcance del Proyecto: Validate

## Descripción General
**Validate** es una plataforma modular de verificación de identidad digital que centraliza distintos métodos de autenticación y validación de usuarios.  
Su propósito es ofrecer un sistema escalable y seguro que permita realizar comprobaciones biométricas, KYC, validaciones documentales y otras verificaciones relacionadas con la identidad de una persona.

La solución está orientada a empresas o plataformas que requieren validar la identidad de sus clientes de manera automatizada, segura y conforme a las normativas de protección de datos.

---

## Objetivos del Proyecto

- Desarrollar una plataforma web que integre diferentes procesos de verificación de identidad.
- Implementar un flujo central de validación con soporte para módulos internos y externos.
- Garantizar la integridad y seguridad de los datos sensibles.
- Facilitar la integración con APIs gubernamentales o privadas (RENIEC, SUNAT, etc.).
- Ofrecer una interfaz moderna, intuitiva y modular para los usuarios y administradores.

---

## Alcance Funcional

### Módulos principales del sistema

1. **Autenticación / Registro**
   - Permitir registro de nuevos usuarios.
   - Inicio de sesión mediante credenciales seguras (JWT o sesión).
   - Recuperación de contraseña y validación por correo o SMS.

2. **Verificación de identidad**
   - Módulo central de validación de usuario.
   - Enrutamiento hacia los submódulos internos.

3. **Módulos internos**
   - **360 Identity Check:** validación combinada (biometría, KYC, antecedentes).
   - **KYC:** validación documental (DNI, pasaporte, comprobantes).
   - **Background Check:** revisión de antecedentes y validaciones externas.
   - **Face Match:** comparación facial entre imagen registrada y nueva captura.
   - **Security Questions:** validación mediante preguntas de seguridad.
   - **Tests Psicológicos:** cuestionarios básicos para detección de patrones.

4. **Notificaciones**
   - Sistema de envío de alertas, mensajes o correos automáticos.
   - Configuración de plantillas personalizadas.

5. **Pagos**
   - Gestión de créditos, fichas o planes de validación.
   - Integración con pasarelas de pago (Stripe, PayPal u otras).

6. **Analítica**
   - Panel de métricas y reportes (volumen de validaciones, tasas de éxito, etc.).
   - Visualización en dashboard administrativo.

---

## Alcance Técnico

### Arquitectura
- **Tipo:** Monolito modular escalable (con posibilidad de evolución a microservicios).
- **Frontend:** Angular.
- **Backend:** Por definir (Django REST Framework / FastAPI / Flask).
- **Base de datos:** PostgreSQL o MongoDB (según stack final).
- **Comunicación:** REST API.
- **Infraestructura:** Contenedores Docker con Nginx como proxy inverso.
- **Autenticación:** JWT + Refresh tokens.
- **Pruebas:** Unitarias, de integración y de rendimiento.
- **Despliegue:** Docker Compose + CI/CD.

---

## Alcance No Funcional

- Cumplimiento de buenas prácticas de seguridad (CORS, CSRF, HTTPS, sanitización de datos).
- Cumplimiento con políticas de protección de datos (GDPR / Ley de Habeas Data).
- Escalabilidad modular del sistema.
- Documentación completa en formato Markdown y Swagger.
- Soporte para entornos de staging y producción.

---

## Entregables Principales

| Etapa | Entregable | Descripción | Formato |
|-------|-------------|-------------|----------|
| Etapa 1 | Documento de análisis técnico | Requerimientos funcionales y técnicos | `.md` / `.pdf` |
| Etapa 2 | Documento de arquitectura | Definición del tipo de arquitectura, componentes y stack | `.md` / `.drawio` |
| Etapa 3 | Modelo de datos | Esquema de base de datos y relaciones | `.sql` / `.png` |
| Etapa 4 | Especificación de módulos | Detalle de cada módulo y flujo interno | `.md` |
| Etapa 5 | API funcional | Endpoints implementados y documentados | `.json` / `.yaml` |
| Etapa 6 | Frontend Angular | Aplicación funcional con vistas y flujos de usuario | Código fuente |
| Etapa 7 | Informe de pruebas | Resultados de QA, errores y ajustes | `.md` / `.pdf` |
| Etapa 8 | Documentación de despliegue | Guía para instalación y configuración | `.md` |
| Etapa 9 | Informe de mantenimiento | Cambios, versiones y mejoras | `.md` |

---

## Exclusiones (Fuera de Alcance)

- Desarrollo de aplicaciones móviles (por ahora solo web).
- Implementaciones de IA avanzada (reconocimiento facial propio, se integrará con APIs externas).
- Integraciones con sistemas propietarios no documentados.
- Procesamiento de pagos reales durante fase de desarrollo (solo sandbox o mockups).

---

## Supuestos

- Las APIs externas estarán disponibles y documentadas.
- El entorno de desarrollo será configurado en contenedores Docker.
- Se cuenta con acceso a repositorio Git centralizado.
- Se utilizarán datos de prueba durante el desarrollo inicial.

---

## Riesgos Iniciales

| Riesgo | Descripción | Mitigación |
|--------|-------------|------------|
| Dependencia de APIs externas | Las integraciones con RENIEC, SUNAT u otras pueden fallar o requerir permisos | Mock APIs y uso de entornos sandbox |
| Falta de definición del backend | Aún no se ha elegido framework final | Realizar pruebas rápidas entre DRF y FastAPI |
| Complejidad modular | La cantidad de submódulos puede generar sobrecarga | Implementar de forma incremental por prioridades |
| Seguridad de datos | Manejo de información sensible | Cifrado, anonimización y auditoría de accesos |

---

## Conclusión

El proyecto **Validate** se plantea como una plataforma robusta y escalable para la verificación de identidad digital.  
El enfoque modular permitirá incorporar progresivamente nuevas fuentes de validación y servicios, garantizando una base técnica sólida y segura desde el inicio.

