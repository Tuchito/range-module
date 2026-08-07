# Feature 1: Interval Management — Artefactos

---

## 📄 proposal.md

### Objetivo
Definir la lógica fundamental para manejar intervalos semiabiertos `[left, right)` en una lista ordenada. Esta feature proporciona los métodos internos necesarios para agregar, eliminar y consultar intervalos, que serán utilizados por la clase `RangeModule` en la Feature 2.

### Alcance
- Implementar una estructura de datos que mantenga una lista de intervalos activos.
- Proveer operaciones internas para:
  - Agregar un intervalo (fusionando con intervalos adyacentes o superpuestos).
  - Eliminar un intervalo (dividiendo intervalos existentes si es necesario).
  - Consultar si un intervalo está completamente cubierto por los intervalos activos.

### Criterios de aceptación
- La lista de intervalos está siempre ordenada por `left`.
- No hay intervalos superpuestos en la lista (se fusionan al agregar).
- Los intervalos se dividen correctamente al eliminar.
- La consulta devuelve `True` solo si todo el intervalo está cubierto.
- Uso de `bisect` para búsqueda eficiente.

### Fuera de alcance
- La clase `RangeModule` con la interfaz pública (Feature 2).
- Pruebas unitarias (Feature 3).
- Optimización avanzada (O(log n) para consultas).

