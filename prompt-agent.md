@openspec/project.md
@openspec/AGENTS.md
@openspec/changes/feature-3-optimization-and-tests/proposal.md
@openspec/changes/feature-3-optimization-and-tests/design.md
@openspec/changes/feature-3-optimization-and-tests/tasks.md


Implementa el código de la Feature 3: Optimización y Tests.

**Instrucciones:**

1. Crea el archivo `tests/test_range_module.py` con pruebas unitarias para `RangeModule`.

2. Las pruebas deben cubrir:
   - `addRange`: intervalos simples, superpuestos, adyacentes.
   - `removeRange`: eliminación parcial, total, sin superposición.
   - `queryRange`: consultas exactas, parciales, fuera de rango.
   - Casos edge: intervalos vacíos, `left >= right`.

3. Usa `pytest` para las pruebas (asume que está instalado).

4. Optimiza `queryRange` en `IntervalManager` si es necesario:
   - Asegura que use `bisect` para búsqueda eficiente.
   - Si ya está optimizado, no lo modifiques.

5. Incluye type hints y docstrings en los tests.

**Restricciones:**
- No modifiques `src/interval_manager.py` o `src/range_module.py` a menos que sea estrictamente necesario.
- Los tests deben ser independientes y no depender del orden de ejecución.