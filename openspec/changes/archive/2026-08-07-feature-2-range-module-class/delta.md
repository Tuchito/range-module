# Delta: Range Module Class

## Cambios realizados

### Especificaciones añadidas

#### range-module
- **Descripción**: Implementación de la clase `RangeModule` con interfaz pública (`addRange`, `removeRange`, `queryRange`).
- **Archivo creado**: `specs/range-module/spec.md` (se creará al archivar).
- **Responsabilidad**: Proveer una clase `RangeModule` que utiliza `IntervalManager` para manejar intervalos.

### Implementación
- **Archivo creado**: `src/range_module.py`
- **Métodos**:
  - `addRange(left, right)`: Agrega un intervalo.
  - `removeRange(left, right)`: Elimina un intervalo.
  - `queryRange(left, right)`: Consulta si un intervalo está cubierto.
- **Complejidad**: O(n) en el peor caso para add/remove, O(n) para query.

### Dependencias
- `src/interval_manager.py` (Feature 1).
- `typing` para type hints.

### Pruebas
- Casos cubiertos: agregar intervalos, eliminar intervalos, consultar intervalos.
- Casos edge: intervalos adyacentes, superpuestos, vacíos.