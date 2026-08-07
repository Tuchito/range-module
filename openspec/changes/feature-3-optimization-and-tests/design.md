# Feature 3: Optimización y Tests — Design

## Estrategia de Tests

### Framework
- `pytest` como framework de pruebas.
- Archivo: `src/tests/test_range_module.py`.

### Estructura de tests

| Grupo | Descripción |
|-------|-------------|
| `test_add_range` | Agregar intervalos, fusionar superpuestos, fusionar adyacentes |
| `test_remove_range` | Eliminar porción, dividir intervalo, eliminar completo |
| `test_query_range` | Consultas cubiertas, no cubiertas, parcialmente cubiertas |
| `test_empty_state` | Consultas en estado vacío |
| `test_leetcode_example` | Caso completo del problema LeetCode 715 |
| `test_edge_cases` | Intervalos idénticos, contiguos,sin intersección |

### Casos edge a cubrir
- `addRange` con intervalo que fusiona múltiples existentes.
- `removeRange` que divide un intervalo en dos.
- `removeRange` que elimina la unión de varios intervalos.
- `queryRange` con `[left, right)` donde `left == right` (debe retornar `True`).
- `queryRange` en lista vacía (debe retornar `False`).
- `addRange` de un intervalo ya completamente cubierto.
- `removeRange` de un intervalo no existente.

## Estrategia de Optimización

### Problema actual
- `_add_interval`: recorre toda la lista → O(n).
- `_remove_interval`: recorre toda la lista → O(n).

### Solución
Usar `bisect_left` y `bisect_right` para encontrar los índices relevantes:

**`_add_interval` optimizado:**
1. Encontrar con `bisect_left` el primer intervalo cuyo `right >= left`.
2. Encontrar con `bisect_right` el último intervalo cuyo `left <= right`.
3. Fusionar solo los intervalos en ese rango [start_idx, end_idx].

**`_remove_interval` optimizado:**
1. Encontrar con `bisect_left` el primer intervalo que se superpone.
2. Recorrer solo los intervalos que se superponen con `[left, right)`.
3. Dividir o recortar según sea necesario.

### Complejidad después de optimización
| Operación | Antes | Después |
|-----------|-------|---------|
| `_add_interval` | O(n) | O(k) donde k = intervalos fusionados |
| `_remove_interval` | O(n) | O(k) donde k = intervalos afectados |
| `_query_interval` | O(log n) | O(log n) (sin cambios) |

## Dependencias
- `pytest` (instalar con `pip install pytest`).
- `src/interval_manager.py` y `src/range_module.py` (Features 1 y 2).
