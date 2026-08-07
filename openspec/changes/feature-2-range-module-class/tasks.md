# Feature 2: Range Module Class — Tasks

## Tareas

- [x] Crear `src/range_module.py`.
- [x] Importar `IntervalManager` desde `src.interval_manager`.
- [x] Implementar la clase `RangeModule`:
  - [x] `__init__(self)`: inicializar `self._interval_manager = IntervalManager()`.
  - [x] `addRange(self, left: int, right: int) -> None`: delegar a `self._interval_manager._add_interval(left, right)`.
  - [x] `removeRange(self, left: int, right: int) -> None`: delegar a `self._interval_manager._remove_interval(left, right)`.
  - [x] `queryRange(self, left: int, right: int) -> bool`: delegar a `self._interval_manager._query_interval(left, right)`.
- [x] Incluir type hints en todos los métodos.
- [x] Incluir docstrings con descripción y Args/Returns.
- [x] Verificar que la interfaz coincide con LeetCode 715.
