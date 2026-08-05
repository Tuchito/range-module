### Decisión de diseño
Se utilizará una **lista de intervalos ordenada** para mantener los rangos activos. La lista se mantiene siempre sin superposiciones y ordenada por `left`.

### Estructura de datos
- **Lista de intervalos**: `List[Tuple[int, int]]` donde cada tupla es `(left, right)`.
- **Invariancia**: La lista está ordenada por `left` y no contiene intervalos superpuestos.

### Operaciones principales

| Operación | Estrategia |
|-----------|------------|
| **Agregar intervalo** | Insertar el nuevo intervalo y fusionar con los adyacentes o superpuestos. |
| **Eliminar intervalo** | Recortar o dividir intervalos existentes que se superpongan con `[left, right)`. |
| **Consultar intervalo** | Verificar que `[left, right)` esté completamente cubierto por uno o más intervalos. |

### Complejidad esperada
- **Agregar**: O(n) en el peor caso (por fusión).
- **Eliminar**: O(n) en el peor caso (por división).
- **Consultar**: O(log n) con `bisect` para encontrar el intervalo inicial.