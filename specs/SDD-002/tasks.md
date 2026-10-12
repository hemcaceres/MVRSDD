# SDD-002 — Tareas

| ID | Resultado | Aceptación | Comprobación y evidencia | Estado |
|---|---|---|---|---|
| T-001 | Skill neutral, metadatos OpenAI, adaptador Claude y regla común. | AC-001, AC-004 | [Validación técnica](artifacts/technical-results.json), [adaptador ejercido](artifacts/eval-entry.md) y [bloque real desde proyecto con skill externa](artifacts/eval-external-execution.md). | Comprobada |
| T-002 | Casos comunes aislados e instrucciones reproducibles. | AC-005 | [Preparación/tests/rechazo](evidence.md#2026-10-08--implementación-y-autocontrol-técnico); [snapshots preservados](artifacts/evaluations/NOTICE.md). | Comprobada |
| T-003 | Conducta ejercida por evaluadores independientes. | AC-002, AC-003, AC-004 | [Entradas y hashes](artifacts/eval-entry.md), [ejecución](artifacts/eval-execution.md), [fuentes externas](artifacts/eval-external-execution.md), con alcance/límites declarados. | Comprobada |
| T-004 | Descubrimiento/activación nativa por herramienta. | AC-006 | [Intentos reales y PEND-SDD-002-001](evidence.md#2026-10-08--intentos-nativos-y-límites-de-ac-006). Acuerdo posterior: usuario valida durante uso, comenzando Gemini en Antigravity IDE; Claude diferido por falta de suscripción, sin bloquear actualizaciones. No se declara pass. | Parcial; pruebas nativas a cargo del usuario, Claude diferido |
| T-005 | Revisión independiente del cambio vigente. | AC-001…AC-006 | [Dictamen vigente de /root/sdd_review](artifacts/review.md): favorable a AC-001…005, hallazgo de preservación cerrado; AC-006 parcial impide Verificada. | Comprobada |

Contrato: [spec](spec.md). Historia: [evidencia](evidence.md). Estado global: [catálogo](../index.md).
