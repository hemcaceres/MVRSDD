---
name: sdd
description: Conducir discovery, features, errores y continuidad con el harness SDD de un proyecto que tenga .harness/prompts.md. Una invocación sin pedido sólo orienta. No aplicar a consultas ajenas al harness.
---

# Entrada SDD para Claude Code

Leé `.agents/skills/sdd/SKILL.md` desde la raíz del proyecto actual y aplicá esa definición canónica al pedido del usuario. Este adaptador sólo carga la skill: invocar `/sdd` sin pedido adicional conserva su orientación sin escrituras. No resuelvas esa referencia desde la instalación del adaptador; si falta el proyecto o la entrada canónica, informá el límite y pedí su ubicación, sin instalar ni copiar el flujo.
