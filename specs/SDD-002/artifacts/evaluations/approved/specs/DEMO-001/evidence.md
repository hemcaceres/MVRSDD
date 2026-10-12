# Evidencia
Datos sintéticos. No hay ejecuciones previas comprobadas.

## 2026-10-08 — Implementación autorizada, ruta P-03

Roles Leader/Developer; responsable: Codex subagente `sdd_eval_execution`, método lectura explícita de la skill local. Pedido exacto: «Implementá el saludo que ya aprobamos.»

Se identificó DEMO-001 desde catálogo y contrato, con aprobación simulada limitada al saludo de este fixture. Antes del código se leyó AC-001: Python 3 y módulo demo; importar y llamar greeting() sin argumentos; esperado cadena exacta `Hola`; método `python -B check.py`. demo.py tenía sólo el comentario de implementación pendiente; check.py era preexistente. Se agregó exclusivamente greeting() con retorno `Hola`, conservando el marcador y la prueba. No se abrió otra feature, no hubo decisiones nuevas ni nueva aprobación del mismo contrato.

Autocontrol Developer: `python -B check.py` desde raíz del fixture, exit 0, salida `AC-001: pass`; la función devolvió la cadena exacta `Hola`. Se cierra T-001 por comportamiento ejercido; no se limita a importación/build. No hay UI ni otros AC o datos representativos necesarios para función sin entradas.

Rol Leader, mismo responsable: T-002 no se cierra. La asignación prohíbe convocar más agentes; se requiere revisión de otro agente del saludo vigente. El autocontrol no equivale a Verifier. No se publicó ni se modificó el contrato.
