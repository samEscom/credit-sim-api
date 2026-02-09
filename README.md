# Credit Simulation API

API desarrollada en FastAPI para la simulación de créditos utilizando el Sistema Francés, con procesamiento asíncrono de auditoría y persistencia de datos.

## 🚀 Requerimientos del Proyecto

El sistema cumple con los siguientes requerimientos fundamentales:
1.  **Cálculo (Sistema Francés)**: Generación de tabla de amortización con cuota fija mensual.
2.  **Persistencia**: Almacenamiento de cada simulación en base de datos mediante SQLAlchemy ORM.
3.  **Auditoría de Riesgo Asíncrona**:
    -   Notificación a un servicio de scoring externo.
    -   Simulación de retardo aleatorio (1-3s) y tasa de fallo (10%).
    -   **Respuesta Inmediata**: El usuario recibe el resultado en < 200ms mientras la auditoría corre en segundo plano.
4.  **Endpoints Extra**:
    -   `GET /credit/simulate/history`: Listado histórico de simulaciones (ordenado por fecha).
    -   `GET /credit/simulate/{id}`: Consulta de una simulación específica por su ID.

## 🏗️ Arquitectura

La aplicación sigue principios de **Clean Architecture** (Arquitectura Hexagonal):

```text
app/
├── api/                # Capa de entrada (Controllers, Routes, Schemas, Mappers)
├── application/        # Casos de uso y reglas de aplicación (Use Cases, Ports)
├── domain/             # Corazón del negocio (Entities, Domain Services)
├── infrastructure/     # Implementaciones externas (Persistence, Clients)
└── config/             # Configuración global
```

## 🛠️ Ejecución Local

Para correr el proyecto localmente, asegúrate de tener instalado `uv` y `docker`.

### Instalación de dependencias
```bash
make install-local
```

### Configuración inicial (Variables de entorno)
```bash
make setup
```

### Ejecutar Servidor (con Base de Datos)
Este comando levanta la base de datos en Docker y corre el servidor FastAPI con hot-reload:
```bash
make run-local
```

### Otros comandos útiles
```bash
make lint-fix   # Ejecuta ruff para formatear y corregir el código
make lint       # Verifica errores de estilo
```

---
Desarrollado con ❤️ para simulaciones de crédito precisas y rápidas.
