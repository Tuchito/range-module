# Feature 2: Range Module Class — Design

## Estrategia
`RangeModule` actúa como una fachada pública que delega todas las operaciones de intervalos a `IntervalManager`. La separación de responsabilidades es clara:
- `IntervalManager`: lógica de manipulación de intervalos (privado).
- `RangeModule`: interfaz pública según el problema LeetCode 715.

## Estructura

```
RangeModule
├── __init__()          → Crea una instancia de IntervalManager
├── addRange(left, right)   → Delega a _add_interval
├── removeRange(left, right) → Delega a _remove_interval
└── queryRange(left, right)  → Delega a _query_interval
```

## Dependencias
- `src/interval_manager.py` — `IntervalManager` (Feature 1, ya implementada).

## Complejidad
| Operación | Complejidad | Notas |
|-----------|-------------|-------|
| `addRange` | O(n) | Por fusión de intervalos en IntervalManager |
| `removeRange` | O(n) | Por división de intervalos en IntervalManager |
| `queryRange` | O(log n) | Búsqueda binaria con `bisect` en IntervalManager |

## Decisiones de diseño
- `RangeModule` no agrega lógica adicional; solo expone la interfaz.
- Se mantiene la encapsulación: `_intervals` y los métodos `_*` de `IntervalManager` permanecen privados.
- Los métodos públicos de `RangeModule` tienen los nombres exactos del problema (`addRange`, `removeRange`, `queryRange`), no los nombres internos (`_add_interval`, etc.).
