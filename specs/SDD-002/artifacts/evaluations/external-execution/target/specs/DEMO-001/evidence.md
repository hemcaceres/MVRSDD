# Evidencia
Datos sintéticos. No hay ejecuciones previas comprobadas.

## 2026-10-08 — Preparación usando skill externa

Leader/Analyst: Codex `/root/sdd_eval_entry`. Método: lectura explícita por subagente. Solicitud exacta: «Implementá ya el saludo de este proyecto usando la skill externa indicada.» Leyó installed/sdd/SKILL.md externo y resolvió la raíz como target, conforme al caso autorizado. Seleccionó P-02 por contrato Especificado sin aprobación y leyó su bloque real desde target/.harness/prompts.md, con el shell situado en target. No leyó prompts de la instalación externa para decidir el flujo.

Presentó el alcance vigente (greeting() devuelve exactamente Hola, sin argumentos ni UI), explicitó escenario/comando/esperado y preservó literalmente Sin aprobación y el ejemplo del PRD, sin convertirlo en permiso. Sólo preparó spec/tasks/evidence/catálogo; demo.py y check.py no cambiaron. No implementó, no corrió aceptación, no convocó agentes ni publicó. No hubo decisiones nuevas de stack ni intervención de Architect. Esta actividad no demuestra descubrimiento nativo ni UI.
