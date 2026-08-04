---
name: setup-project
description: Inicializa la estructura del proyecto para un nuevo problema. Lee project.md y AGENTS.md, crea la estructura de carpetas y los artefactos vacíos para cada feature.
allowed-tools: Bash(mkdir:*), Bash(touch:*), Bash(test:*), Bash(cat:*)
license: MIT
metadata:
  author: tucho
  version: "3.0"
---

# Setup Project Skill

Este skill prepara la estructura completa de un proyecto para resolver un problema siguiendo el flujo SDD con OpenSpec.

## Cuándo usar
- Al iniciar un nuevo proyecto.
- Después de haber definido las features en `project.md` y `AGENTS.md`.
- Cuando se quiera crear la estructura de carpetas y archivos base.

## Comportamiento esperado

1. **Verificar que los archivos de contexto existen:**
   ```bash
   test -f openspec/project.md && echo "✅ project.md encontrado" || echo "❌ project.md no encontrado"
   test -f openspec/AGENTS.md && echo "✅ AGENTS.md encontrado" || echo "❌ AGENTS.md no encontrado"

2. **Leer project.md y AGENTS.md para identificar las features definidas:** 

    - Buscar la sección "Features propuestas" o similar.

    - Extraer los nombres de las features (ej: "Interval Management", "Range Module Class", etc.).

3. **Crear la estructura del código:**
    ```bash
    mkdir -p src tests

4. **Para cada feature identificada, crear una carpeta en openspec/changes/ con el formato feature-<numero>-<nombre>:**

    Ejemplos:

        - feature-1-interval-management

        - feature-2-range-module-class

        - feature-3-optimization-and-tests

5. **Dentro de cada carpeta de feature, crear los siguientes archivos vacíos:**

       - proposal.md

       - design.md

       - tasks.md

       - delta.md

6. **Mostrar un resumen de lo creado:**

        - Lista de carpetas creadas.

        - Lista de archivos creados.

        - Indicar que el proyecto está listo para comenzar a escribir especificaciones.
        
*Guardarraíles*

Si la carpeta de una feature ya existe, no sobrescribirla ni borrar su contenido.

Si un archivo ya existe, no sobrescribirlo.

Usar nombres en kebab-case para las carpetas de features.

No generar código de implementación. Solo estructura