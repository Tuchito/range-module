@openspec/project.md
@openspec/AGENTS.md
@openspec/changes/feature-2-range-module-class/proposal.md
@openspec/changes/feature-2-range-module-class/design.md
@openspec/changes/feature-2-range-module-class/tasks.md
@openspec/changes/feature-2-range-module-class/delta.md

Implementa el código de la Feature 2: Range Module Class.

**Instrucciones:**

1. Crea el archivo `src/range_module.py`.

2. La clase `RangeModule` debe:
   - Tener un constructor `__init__()` que inicialice una instancia de `IntervalManager`.
   - Implementar los métodos públicos:
     - `addRange(left: int, right: int) -> None`
     - `removeRange(left: int, right: int) -> None`
     - `queryRange(left: int, right: int) -> bool`

3. Cada método debe delegar en el `IntervalManager` correspondiente:
   - `addRange` → `_interval_manager._add_interval(left, right)`
   - `removeRange` → `_interval_manager._remove_interval(left, right)`
   - `queryRange` → `_interval_manager._query_interval(left, right)`

4. Incluye type hints y docstrings en todos los métodos.

5. No modifiques `src/interval_manager.py` (ya existe de la Feature 1).

**Restricciones:**
- Usa la instancia de `IntervalManager` como atributo privado (`_interval_manager`).
- No agregues lógica adicional en `RangeModule` (solo delegación).
- Sigue el estilo de codificación de Python (PEP 8).
- No generes tests.