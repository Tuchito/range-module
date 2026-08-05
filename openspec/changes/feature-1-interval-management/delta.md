# Delta: Interval Management

## Cambios realizados

### Especificaciones añadidas

#### interval-management
- **Descripción**: Implementación de la lógica de manejo de intervalos semiabiertos `[left, right)`.
- **Archivo creado**: `specs/interval-management/spec.md` (se creará al archivar).
- **Responsabilidad**: Proveer una clase `IntervalManager` con métodos internos para agregar, eliminar y consultar intervalos.

### Implementación
- **Archivo creado**: `src/interval_manager.py`
- **Métodos**:
  - `_add_interval(left, right)`: Agrega un intervalo y fusiona si es necesario.
  - `_remove_interval(left, right)`: Elimina un intervalo y divide si es necesario.
  - `_query_interval(left, right)`: Verifica si todo el intervalo está cubierto.
- **Complejidad**: O(n) en el peor caso para add/remove, O(log n) para query con `bisect`.

### Dependencias
- `bisect` (biblioteca estándar de Python).
- `typing` para type hints.

### Pruebas
- Casos cubiertos: agregar intervalos, eliminar intervalos, consultar intervalos.
- Casos edge: intervalos adyacentes, superpuestos, vacíos.