---
name: setup-project
description: Inicializa la estructura del proyecto para un nuevo problema. Lee project.md y AGENTS.md y crea las carpetas de features con artefactos vacíos.
---

Ejecuta el skill `setup-project` para crear la estructura de carpetas y archivos base del proyecto.

**Uso:** `/setup-project`

**Comportamiento:**
1. Lee `openspec/project.md` y `openspec/AGENTS.md` para identificar las features definidas.
2. Crea las carpetas `src/` y `tests/`.
3. Crea las carpetas de features en `openspec/changes/` con el formato `feature-<numero>-<nombre>`.
4. Dentro de cada carpeta de feature, crea `proposal.md`, `design.md`, `tasks.md` y `delta.md` vacíos.
5. Muestra un resumen de lo creado.

**Nota:** Este comando no genera código de implementación. Solo prepara la estructura del proyecto.
