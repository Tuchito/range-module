# Feature 3: Optimización y Tests — Tasks

## Tareas

### Tests
- [x] Crear directorio `src/tests/`.
- [x] Crear `src/tests/__init__.py`.
- [x] Crear `src/tests/test_range_module.py`.
- [x] Implementar tests de `addRange`:
  - [x] Agregar intervalo a lista vacía.
  - [x] Agregar intervalo que fusiona dos existentes.
  - [x] Agregar intervalo adyacente (sin gaps).
  - [x] Agregar intervalo ya completamente cubierto.
- [x] Implementar tests de `removeRange`:
  - [x] Eliminar porción de un intervalo (dividir en dos).
  - [x] Eliminar intervalo completo.
  - [x] Eliminar unión de varios intervalos.
  - [x] Eliminar de intervalo no existente.
- [x] Implementar tests de `queryRange`:
  - [x] Consulta cubierta completamente.
  - [x] Consulta no cubierta.
  - [x] Consulta parcialmente cubierta.
  - [x] Consulta con `left == right` (debe ser `True`).
  - [x] Consulta en lista vacía (debe ser `False`).
- [x] Implementar test del ejemplo LeetCode 715.
- [x] Implementar tests edge cases:
  - [x] Múltiples add/remove secuenciales.
  - [x] Intervalos contiguos sin superposición.

### Optimización
- [x] `_query_interval` ya usa `bisect_right` → O(log n), sin cambios necesarios.

### Verificación
- [x] Ejecutar `pytest src/tests/ -v` → 21 tests pasan.
- [x] Verificar que la solución pase el ejemplo de LeetCode 715.
