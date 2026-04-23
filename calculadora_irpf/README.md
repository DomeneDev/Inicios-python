# ⚖️ Calculadora de IRPF Pro

Este proyecto es un motor de cálculo fiscal modular diseñado para procesar retenciones salariales basadas en tramos progresivos. Se centra en la iteración compleja sobre colecciones y el cálculo de métricas financieras.

## 🚀 Características

- **Cálculo Progresivo**: Implementación de lógica de tramos donde cada euro tributa según su intervalo correspondiente.
- **Informe Detallado**: Generación de balances que incluyen sueldo neto, bruto y el tipo impositivo real (efectivo).
- **Configuración Flexible**: Estructura de datos preparada para actualizar los tramos impositivos según la normativa vigente.

## 📂 Estructura del Proyecto

```plaintext
calculadora_irpf/
├── main.py              # Interfaz de usuario y desglose de resultados.
├── irpf_logic.py        # Motor de cálculo (lógica progresiva).
└── README.md            # Documentación del proyecto.
```
🛠️ Instalación y Uso
Asegúrate de tener instalado Python 3.10 o superior.

Ejecuta el programa principal:
```plintext
Bash
python main.py
```
🛡️ Roadmap de Aprendizaje
[x] Sprint 1: Lógica core de tramos y listas de tuplas .

[x] Sprint 2: Manejo de excepciones para entradas de sueldo negativas o no numéricas (Estado actual).

[ ] Sprint 3: Refactorización Arquitectónica (Utils).

[ ] Sprint 4: Persistencia de cálculos en CSV para histórico de nóminas.

[ ] Sprint 5: Refactorización a Programación Orientada a Objetos (POO).

