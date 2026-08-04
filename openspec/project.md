# Range Module — LeetCode 715

## 📖 Descripción del problema

Diseña una estructura de datos que pueda rastrear rangos de números representados como intervalos semiabiertos `[left, right)`. Un intervalo semiabierto incluye todos los números reales `x` donde `left <= x < right`.

La estructura debe soportar tres operaciones:

1. **`addRange(left, right)`** — Agrega el intervalo `[left, right)`, fusionándolo con intervalos existentes si se superponen o son adyacentes.
2. **`removeRange(left, right)`** — Elimina el intervalo `[left, right)` de los rangos rastreados, dividiendo intervalos si es necesario.
3. **`queryRange(left, right)`** — Devuelve `True` si **todo** el intervalo `[left, right)` está completamente rastreado, y `False` en caso contrario.

## 🧠 Estrategia general

Mantendremos una **lista de intervalos activos** ordenada por el extremo izquierdo. Cada operación modificará esta lista:

| Operación | Acción |
|-----------|--------|
| **`addRange`** | Insertar el nuevo intervalo y fusionar con los que se superpongan o sean adyacentes. |
| **`removeRange`** | Eliminar partes de intervalos existentes que se superpongan con `[left, right)`, dividiendo si es necesario. |
| **`queryRange`** | Verificar que el intervalo `[left, right)` esté completamente cubierto por uno o más intervalos activos. |

## 📂 Features propuestas

| Feature | Nombre | Responsabilidad |
|---------|--------|-----------------|
| **001** | Interval Management | Implementar la lógica de agregar, eliminar y consultar intervalos. |
| **002** | Range Module Class | Crear la clase `RangeModule` con la interfaz pública (`addRange`, `removeRange`, `queryRange`). |
| **003** | Optimización y Tests | Validar con casos de prueba y optimizar si es necesario. |

## 📊 Complejidad esperada

| Operación | Complejidad |
|-----------|-------------|
| `addRange` | O(n) en el peor caso (por fusión de intervalos) |
| `removeRange` | O(n) en el peor caso (por división de intervalos) |
| `queryRange` | O(log n) con búsqueda binaria (o O(n) en el peor caso) |

**Nota:** Con `n ≤ 10^4`, O(n) por operación es aceptable.

## 🔗 Relación con ejercicios anteriores

Este problema es similar a:
- **"Falling Squares"** (gestión de intervalos con alturas).
- **"The Skyline Problem"** (manejo de intervalos y fusiones).
- **"Count of Range Sum"** (consultas de rangos).

## 🚀 Siguiente paso

Feature 1: **Interval Management** — Implementar la lógica de manipulación de intervalos.
Feature 2: **Range Module Clase**  - Exponga la interfaz pública para el usuario.
Feature 3: **Optimización y test** - Validar la solución con casos de prueba y optimizar el rendimiento.