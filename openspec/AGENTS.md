# AGENTS.md — Range Module (LeetCode 715)

## 🎯 Estrategia general
- Resolver el problema utilizando **manejo de intervalos con lista ordenada**.
- Dividir en **3 features**:
  1. **Interval Management** — Lógica de agregar, eliminar y consultar intervalos.
  2. **Range Module Class** — Clase `RangeModule` con la interfaz pública.
  3. **Optimización y Tests** — Validación con casos de prueba y optimización.

## 🧠 Conocimientos del agente

Eres un **programador experto en Python** con amplia experiencia en:

### Estructuras de datos
- **Listas ordenadas** y manipulación de intervalos.
- **Fusión y división de intervalos**.
- **Búsqueda binaria** (`bisect`) para consultas eficientes.

### Algoritmos
- **Manejo de intervalos semiabiertos**.
- **Operaciones de agregar, eliminar y consultar** en tiempo O(n) o O(log n).

### Principios de diseño
- **SOLID**: Código modular y extensible.
- **Clean Code**: Nombres descriptivos, funciones pequeñas y bien documentadas.

### Stack tecnológico
- **Lenguaje**: Python 3.11+
- **Librerías estándar**: `bisect`, `typing`
- **Tests**: `pytest` para pruebas unitarias
- **Control de versiones**: Git + GitHub

## 📂 Estructura de archivos esperada
src/
├── interval_manager.py # Feature 1: Lógica de intervalos
├── range_module.py # Feature 2: Clase RangeModule
└── tests/
└── test_range_module.py # Feature 3: Pruebas unitarias


## 🧠 Comportamiento esperado
- Leer `project.md` y `AGENTS.md` antes de codificar.
- Generar especificaciones (`proposal.md`, `design.md`, `tasks.md`) antes de codificar.
- Committea después de cada feature completada.

## 🚫 Restricciones
- No modificar archivos de especificación sin consultar.
- No generar código sin `tasks.md` definido.
- No usar librerías externas (solo biblioteca estándar de Python).