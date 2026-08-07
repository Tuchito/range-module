## 📄 tasks.md

### Tareas del agente

- [ ] Crear `src/interval_manager.py`.
- [ ] Implementar `_add_interval(left, right)`:
  - Buscar posición de inserción con `bisect`.
  - Fusionar intervalos superpuestos o adyacentes.
- [ ] Implementar `_remove_interval(left, right)`:
  - Buscar intervalos que se superpongan.
  - Recortar o dividir según sea necesario.
- [ ] Implementar `_query_interval(left, right)`:
  - Verificar que todo el intervalo esté cubierto.
- [ ] Usar `bisect` para búsqueda eficiente.
- [ ] Incluir type hints y docstrings.
- [ ] Asegurar que los intervalos están siempre ordenados y sin superposiciones.

---