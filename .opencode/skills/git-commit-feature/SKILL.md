---
name: git-commit-feature
description: Inicializa el repositorio local, crea una rama para la feature y realiza un commit convencional de los cambios. Pregunta el nombre, tipo y mensaje, y ejecuta git add y commit.
allowed-tools: Bash(git:*), Bash(echo:*), Bash(test:*), Bash(mkdir:*)
license: MIT
metadata:
  author: tucho
  version: "3.0"
---

# Git Commit Feature Skill (con inicialización de repo y rama)

Este skill automatiza:
1. La inicialización del repositorio local (si no existe).
2. La creación de una rama para la feature.
3. El commit local siguiendo el estándar Conventional Commits.

## Cuándo usar
- Al iniciar un nuevo proyecto (para crear el repo y la primera rama).
- Antes de empezar a implementar una feature (para crear la rama).
- Después de implementar una feature (para committear).

## Comportamiento esperado

1. **Verificar si existe un repositorio Git:**
   ```bash
   test -d .git && echo "✅ Repositorio Git existente" || echo "❌ No hay repositorio Git"

   - Sino existe, inicializarlo:
   ``bash 
   git init 
   echo "Repositorio Git inicializado"

2. **Verificar el estado del repositorio:**

    ```bash
    git status --porcelain
    - Si no hay cambios, mostrar: "⚠️ No hay cambios para commitar." y detenerse.

3. **Preguntar al usuario el nombre de la feature:**

    - Usar AskUserQuestion para obtener el nombre (ej: interval-management).

    - Generar el nombre de la rama: feature/<nombre>.

4. **Crear y cambiar a la nueva rama:**

    ```bash
    git checkout -b feature/<nombre>

    - Si la rama ya existe, preguntar si desea cambiarse a ella o crear una nueva.

5. **Mostrar un resumen de los cambios:**

    bash
    git status


6. **Preguntar al usuario el tipo de commit:**

    - Usar AskUserQuestion con las siguientes opciones:

    - feat: Nueva funcionalidad

    - fix: Corrección de error

    - docs: Documentación

    - style: Estilo (formato, espacios, etc.)

    - refactor: Refactorización de código

    - test: Pruebas

    - chore: Mantenimiento (configuración, dependencias, etc.)

7. **Preguntar el mensaje del commit:**

    - Usar AskUserQuestion para obtener una breve descripción de la feature.

    Ejemplo: "add proposal, design, tasks for interval management"

8. **Ejecutar los comandos:**

    ```bash
    git add .
    git commit -m "<tipo>(feature-<nombre>): <mensaje>"

9. **Mostrar el resultado del commit:**

   - Rama actual.

   - Hash del commit.

   - Resumen de cambios.

*Guardarraíles*
    - Verificar que hay cambios para commitar antes de ejecutar.

    - Si no hay cambios, mostrar mensaje y detener.

    - Si la rama ya existe, preguntar antes de sobrescribir.

    - No ejecutar git push (esto se hará en un skill separado o manualmente).

