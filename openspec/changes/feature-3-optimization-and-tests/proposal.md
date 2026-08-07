# Feature 3: Optimización y Tests — Proposal

## Why
Las Features 1 y 2 implementaron la lógica de intervalos (`IntervalManager`) y la clase pública (`RangeModule`). Falta validar que la solución sea correcta mediante pruebas unitarias y asegurar que pase los casos de LeetCode 715. También es necesario optimizar `_add_interval` y `_remove_interval`, que actualmente son O(n) por recorrido completo de la lista.

## What Changes
- Se crea `src/tests/test_range_module.py` con pruebas unitarias usando `pytest`.
- Se cubren casos base, edge cases y el ejemplo de LeetCode.
- Se optimiza `_add_interval` y `_remove_interval` usando `bisect` para encontrar rangos relevantes en O(log n) en lugar de recorrer toda la lista.
- Se mantiene la corrección de la solución tras la optimización.

### Criterios de aceptación
- Todos los tests pasan correctamente.
- Cobertura de al menos los siguientes escenarios:
  - Agregar intervalos que se fusionan.
  - Eliminar intervalos que dividen.
  - Consultar intervalos cubiertos y no cubiertos.
  - Casos vacíos, adyacentes y superpuestos.
  - Ejemplo completo de LeetCode 715.
- `_add_interval` y `_remove_interval` usan `bisect` para acotar el rango de recorrido.
- La solución sigue pasando todos los tests después de la optimización.

### Fuera de alcance
- Optimización a O(log n) con Segment Tree o Balanced BST (requiere reestructura mayor).
- Tests de rendimiento / benchmarking.
