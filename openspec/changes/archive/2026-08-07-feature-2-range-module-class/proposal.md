# Feature 2: Range Module Class — Proposal

## Why
El problema Range Module (LeetCode 715) requiere una clase pública con métodos `addRange`, `removeRange` y `queryRange`. La Feature 1 implementó la lógica interna de intervalos en `IntervalManager` con métodos privados (`_add_interval`, `_remove_interval`, `_query_interval`). Esta feature expone esa lógica a través de una interfaz pública que cumple con la especificación del problema.

## What Changes
- Se crea `src/range_module.py` con la clase `RangeModule`.
- `RangeModule` encapsula una instancia de `IntervalManager`.
- Se implementan los métodos públicos:
  - `addRange(left: int, right: int) -> None`
  - `removeRange(left: int, right: int) -> None`
  - `queryRange(left: int, right: int) -> bool`
- Cada método delega la operación correspondiente al `IntervalManager`.

### Criterios de aceptación
- La clase `RangeModule` tiene los tres métodos públicos con la firma correcta.
- `addRange` agrega y fusiona intervalos correctamente.
- `removeRange` elimina o divide intervalos correctamente.
- `queryRange` devuelve `True` solo si todo el intervalo está cubierto.
- La clase se puede instanciar sin parámetros.
- Se cumplen las restricciones del problema (n ≤ 10^4, valores entre 0 y 10^9).

### Fuera de alcance
- Optimizaciones adicionales (Feature 3).
- Pruebas unitarias (Feature 3).
