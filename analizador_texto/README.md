Analizador de Métricas de Texto
Este es un proyecto modular en Python diseñado para procesar cadenas de texto y extraer métricas estadísticas de contenido. El proyecto está enfocado en aplicar buenas prácticas de desarrollo, tipado estático y modularización de código.

🚀 Características

Limpieza de Datos: Normalización de texto (minúsculas y eliminación de puntuación).

Frecuencia de Palabras: Generación de diccionarios con el conteo de cada término.

Estadísticas Avanzadas: \* Conteo total de palabras.

Identificación de la palabra más larga.

Cálculo de la longitud promedio de las palabras.

📂 Estructura del Proyecto

La arquitectura del código sigue el principio de separación de responsabilidades:
```plaintext

analizador_texto/
├── main.py # Interfaz de usuario y orquestación del programa.
├── procesador.py # Núcleo lógico (motor de procesamiento).
└── README.md # Documentación del proyecto.
```

🛠️ Instalación y Uso

Clona este repositorio o descarga los archivos.

Asegúrate de tener instalado Python 3.9 o superior.

Ejecuta el programa principal:

Bash

python main.py

📝 Ejemplo de Salida

Python es genial, python es potente. Python, Python; es el mejor lenguaje.
```plaintext

+------------------------------------+

| Resultados del análisis del texto  |

+------------------------------------+

 - Total de palabras del texto: 12.
 - Palabra más larga: lenguaje.
 - Media de longitud de las palabras: 4.83.
- Cantidad de palabras:
    - python: 4 veces.
    - es: 3 veces.
    - genial: 1 vez
    - potente: 1 vez
    - el: 1 vez
    - mejor: 1 vez
    - lenguaje: 1 vez

```
🛡️ Roadmap de Aprendizaje

Este proyecto evolucionará conforme avance mi formación en Python:

[x] Sprint 1: Lógica core y modularización .

[x] Sprint 2: Implementación de manejo de excepciones (try-except).

[x] Sprint 3: Refactorización Arquitectónica (Utils).

[x] Sprint 4: Persistencia de datos en archivos .json (Estado actual).

[ ] Sprint 5: Refactorización a Programación Orientada a Objetos (POO).
