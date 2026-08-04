---
name: git-commit-feature
description: Inicializa el repositorio local, crea una rama para la feature y realiza un commit convencional de los cambios.
---

Ejecuta el skill `git-commit-feature` para inicializar el repositorio (si no existe), crear una rama y hacer commit de una feature.

**Uso:** `/git-commit-feature`

**Comportamiento:**
1. Verifica si existe un repositorio Git. Si no, lo inicializa (`git init`).
2. Muestra el estado del repositorio.
3. Pregunta el nombre de la feature (ej: `interval-management`).
4. Crea y cambia a la rama `feature/<nombre>`.
5. Muestra los cambios pendientes.
6. Pregunta el tipo de commit (`feat`, `fix`, `docs`, `chore`, etc.).
7. Pregunta el mensaje del commit.
8. Ejecuta `git add .` y `git commit`.
9. Muestra el resultado del commit.

**Nota:** Este comando no hace push. El push se hará manualmente o con otro skill.
