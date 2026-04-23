# 🏠 HomeBudget Pro: Gestión de Gastos Configurable

**HomeBudget Pro** es una herramienta de control financiero personal diseñada bajo la filosofía de la _Navaja de Ockham_: simplicidad en la interfaz y robustez en la lógica. Permite monitorizar el flujo de caja doméstico, clasificar gastos por categorías dinámicas y analizar la salud financiera en tiempo real.

---

## 🚀 Características Principales

- **Categorización Dinámica**: Sin categorías fijas; el sistema se adapta a tu estilo de vida.
- **Gestión de Flujo de Caja**: Registro de tipos de movimientos Ingresos y Gastos.
- **Motor de Búsqueda**: Filtrado inteligente por categorías para detectar fugas de capital.
- **Control de Identidad**: Sistema de IDs únicos e irrepetibles para asegurar la integridad de los registros.

## 📂 Estructura del Proyecto

```plaintext
home_budget/
├── main.py              # Orquestador del programa y menú de usuario.
├── budget_logic.py      # Motor de cálculo y gestión de movimientos.
├── utils.py             # Funciones de apoyo a lógica y a main
└── README.md            # Documentación del sistema.
```
🛠️ Instalación y Uso
Requisitos: Tener instalado Python 3.10 o superior.

```plaintext
Ejecución:
Bash
python main.py
```
🛡️ Roadmap de Desarrollo (Sprints)

🟢 Sprint 1: Lógica Core (Estado Actual)
[x] Implementación de estructura de datos basada en listas de diccionarios.

[x] Desarrollo de funciones CRUD (Crear, Leer, Eliminar) de movimientos.

[x] Motor de balance neto y filtrado por categorías.

🟡 Sprint 2: Robustez y Validación
[x] Manejo de excepciones (try-except) para entradas de dinero no numéricas.

[x] Validación de campos vacíos en conceptos y categorías.

🔵 Sprint 3: Refactorización Arquitectónica (Utils)
[x] Aplicación de la Navaja de Ockham: Simplificación del main.py.

[x] Creación de utils.py para desacoplar la lógica de formateo de moneda y menús.

🟠 Sprint 4: Persistencia de Datos
[ ] Implementación de guardado automático en formato CSV para histórico anual.

[ ] Carga de datos al iniciar la aplicación.

🔴 Sprint 5: Paradigma de Objetos (POO)
[ ] Reingeniería total mediante clases: Movement, Account y Report.

[ ] Encapsulamiento de la lógica financiera en métodos de clase.
```
