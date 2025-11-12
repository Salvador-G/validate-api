## 🧩 Tabla: auth.users

Representa a los usuarios del sistema. Contiene la información principal de autenticación, como correo, contraseña y roles.

### Campos
| Campo | Tipo | Restricciones | Descripción |
|--------|------|----------------|--------------|
| id | uuid | PK | Identificador único del usuario. |
| email | varchar(255) | unique, not null | Correo electrónico del usuario, usado para login. |
| password_hash | varchar(255) | not null | Hash de la contraseña del usuario. |
| first_name | varchar(255) |  | Nombre del usuario. |
| last_name | varchar(255) |  | Apellido del usuario. |
| role | varchar(50) | default: 'client' | Rol o tipo de usuario dentro del sistema. |
| is_active | boolean | default: true | Indica si el usuario está activo o bloqueado. |
| is_verified | boolean | default: false | Indica si el correo del usuario ha sido verificado. |
| created_at | timestamp | default: now() | Fecha de creación del registro. |
| updated_at | timestamp |  | Fecha de la última actualización del usuario. |

### Propósito
Esta tabla es el núcleo del sistema de autenticación.  
Define las credenciales básicas, estado y roles de cada usuario en la plataforma.

## 🔐 Tabla: auth.sessions

Registra las sesiones activas de los usuarios, incluyendo los tokens de acceso, el dispositivo y otros datos del entorno desde donde se inició la sesión.

### Campos
| Campo | Tipo | Restricciones | Descripción |
|--------|------|----------------|--------------|
| id | uuid | PK | Identificador único de la sesión. |
| user_id | uuid | not null, ref: > auth.users.id | Relación con el usuario que inició la sesión. |
| token | varchar(512) | not null | Token JWT o de sesión asignado al usuario. |
| refresh_token | varchar(512) |  | Token de refresco para renovar la sesión. |
| ip_address | varchar(45) |  | Dirección IP desde donde se realizó el login. |
| user_agent | varchar(255) |  | Información del navegador o dispositivo usado. |
| expires_at | timestamp |  | Fecha y hora de expiración del token. |
| revoked | boolean | default: false | Indica si la sesión fue revocada manualmente. |
| created_at | timestamp | default: now() | Fecha de creación del registro de sesión. |

### Propósito
Permite gestionar el ciclo de vida de las sesiones de los usuarios, controlar el acceso activo, auditar inicios de sesión y revocar accesos comprometidos.

## 🔑 Tabla: auth.password_resets

Gestiona las solicitudes de restablecimiento de contraseña de los usuarios.  
Cada registro representa un token temporal enviado al usuario para recuperar el acceso a su cuenta.

### Campos
| Campo | Tipo | Restricciones | Descripción |
|--------|------|----------------|--------------|
| id | uuid | PK | Identificador único del registro de restablecimiento. |
| user_id | uuid | not null, ref: > auth.users.id | Usuario al que pertenece la solicitud. |
| token | varchar(512) | not null | Token temporal generado para el restablecimiento de contraseña. |
| expires_at | timestamp | not null | Fecha y hora de expiración del token. |
| used | boolean | default: false | Indica si el token ya fue utilizado. |
| created_at | timestamp | default: now() | Fecha de creación del registro. |

### Propósito
Permite al sistema manejar el flujo seguro de recuperación de contraseñas,  
asegurando que cada solicitud tenga un tiempo de validez y se marque como usada una vez completada.

## 🧭 Tabla: auth.two_factor_auth

Almacena la configuración de autenticación en dos pasos (2FA) para los usuarios del sistema.  
Permite habilitar o deshabilitar la verificación adicional mediante un código o clave secreta.

### Campos
| Campo | Tipo | Restricciones | Descripción |
|--------|------|----------------|--------------|
| id | uuid | PK | Identificador único del registro de autenticación 2FA. |
| user_id | uuid | not null, ref: > auth.users.id | Relación con el usuario propietario de la configuración. |
| secret_key | varchar(64) |  | Clave secreta generada para el método de verificación (por ejemplo, TOTP). |
| is_enabled | boolean | default: false | Indica si la autenticación en dos pasos está activa para el usuario. |
| created_at | timestamp | default: now() | Fecha en que se creó la configuración de 2FA. |

### Propósito
Permite aumentar la seguridad de las cuentas de usuario mediante la implementación  
de un segundo factor de autenticación, generalmente una app como Google Authenticator o Authy.

## 📜 Tabla: auth.audit_logs

Registra eventos y acciones relevantes realizadas por los usuarios o el sistema en el módulo de autenticación.  
Sirve para mantener un historial detallado de actividad, útil para auditoría y seguridad.

### Campos
| Campo | Tipo | Restricciones | Descripción |
|--------|------|----------------|--------------|
| id | uuid | PK | Identificador único del registro de auditoría. |
| user_id | uuid | ref: > auth.users.id | Usuario que realizó la acción (puede ser nulo si fue una acción del sistema). |
| action | varchar(255) | not null | Descripción de la acción o evento registrado. |
| ip_address | varchar(45) |  | Dirección IP desde donde se realizó la acción. |
| timestamp | timestamp | default: now() | Momento exacto en que ocurrió el evento. |
| metadata | jsonb |  | Datos adicionales en formato JSON (por ejemplo: navegador, endpoint, resultado, etc.). |

### Propósito
Proporciona trazabilidad completa sobre las operaciones del sistema de autenticación,  
facilitando la detección de accesos sospechosos, auditorías de seguridad y análisis de incidentes.

## 🔗 Relaciones del esquema: auth

El esquema `auth` está diseñado con una estructura relacional centrada en la tabla `auth.users`, que actúa como el núcleo de todas las operaciones de autenticación, sesión y seguridad.

### Descripción general de relaciones

| Relación | Tipo | Descripción |
|-----------|------|--------------|
| `auth.sessions.user_id → auth.users.id` | 1:N | Un usuario puede tener múltiples sesiones activas o históricas. |
| `auth.password_resets.user_id → auth.users.id` | 1:N | Un usuario puede generar múltiples solicitudes de restablecimiento de contraseña. |
| `auth.two_factor_auth.user_id → auth.users.id` | 1:1 | Cada usuario tiene una configuración única de autenticación en dos pasos. |
| `auth.audit_logs.user_id → auth.users.id` | 1:N | Cada usuario puede tener múltiples registros de auditoría asociados a sus acciones. |

### Diagrama conceptual (texto)

```text
auth.users (1)
├───< auth.sessions (N)
├───< auth.password_resets (N)
├───1── auth.two_factor_auth (1)
└───< auth.audit_logs (N)
```

### Interpretación

- **`auth.users`** es la tabla principal: almacena la información base de cada usuario.  
- **`auth.sessions`** gestiona las sesiones activas, tokens y dispositivos.  
- **`auth.password_resets`** se usa para recuperación de contraseñas seguras.  
- **`auth.two_factor_auth`** habilita una capa adicional de seguridad.  
- **`auth.audit_logs`** registra todas las acciones y eventos para trazabilidad.

Esta estructura modular permite mantener una **autenticación segura, auditable y escalable**, preparada para integrarse con otros esquemas (como `core`) o servicios externos.
