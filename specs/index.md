# Catálogo de specs

Registrar cada feature nueva como Propuesta (proposed), incluso después del MVP; después hacer discovery, definir resultado/aceptación/tareas y obtener aprobación del contrato concreto antes del código. Usar IDs estables, prioridades y dependencias. Las features lejanas pueden ser entradas sin carpeta o spec detallada; no crear archivos vacíos para completar el catálogo.

| ID | Resultado esperado | Prioridad | Dependencias | Spec | Estado actual |
|---|---|---|---|---|---|
| SDD-002 | Reutilizar una sola skill SDD entre herramientas, con entradas mínimas y pruebas comunes. | Alta | Harness existente | [Contrato](SDD-002/spec.md) · [Tareas](SDD-002/tasks.md) · [Evidencia](SDD-002/evidence.md) | En verificación |
| SDD-003 | Explicitar el ciclo de implementación y la búsqueda de contraejemplos en la revisión. | Media | Prompts vigentes del harness | [Contrato](SDD-003/spec.md) · [Tareas](SDD-003/tasks.md) · [Evidencia](SDD-003/evidence.md) | Verificada |

Usar estados legibles y consistentes: Propuesta (proposed), Discovery, Especificada, Aprobada, En implementación, En verificación, Verificada o Bloqueada. Explicar un bloqueo con causa concreta. Verificada exige tareas comprobadas, todos los AC satisfechos con evidencia pertinente, artefactos visuales si aplica y revisión favorable de un agente distinto del implementador sobre el resultado vigente; no significa publicada. Tests/build exitosos no bastan. Una condición sin comprobar o la falta de revisor impiden declarar aceptación completa.

## Trabajo activo y siguiente acción

SDD-003: tramo documental cerrado el 2026-10-12 por Codex `/root` (Leader), con AC-001…003 y tareas comprobados y [dictamen independiente favorable](SDD-003/review.md). Los bloques aprobados están integrados en P-03/P-06; no hay siguiente acción pendiente de este tramo. Esta aceptación evalúa texto, no eficacia de agentes ni compatibilidad nativa. SDD-002 conserva su pendiente de validación nativa indicado abajo.

Trabajo activo: SDD-002. Responsable: Codex `/root` (Leader). Entrada portable implementada; AC-001…005 respaldados por evaluación independiente y [dictamen favorable del resultado común vigente](SDD-002/artifacts/review.md). ERR-006/REV-SDD-002-001 y ERR-007 resueltos con comprobación y confirmación del revisor. No hay hallazgos pendientes de implementación o preservación.

**Siguiente acción:** el usuario comprobará progresivamente PEND-SDD-002-001/AC-006 durante el uso, comenzando por Gemini en Antigravity IDE con el harness ya incorporado en Calles Posadas. Claude queda diferido hasta contar con suscripción. Estos pendientes no bloquean incorporar ni actualizar SDD. No se declara Verificada la compatibilidad nativa ni se equipara Antigravity IDE con Gemini CLI. Registrar resultados reales y confirmación independiente cuando existan; si se comprueba UI, conservar capturas/secuencia con viewport. Esta entrada corresponde al harness; no hay producto ni MVP configurado.

## Publicación

2026-10-12 — usuario de esta conversación: «Hace el commit, publica en remoto y actualia el harness en C:\DEV\calles-posadas». Autoriza commit y push del harness vigente (entrada portable SDD-002 y prompts SDD-003, con sus documentos y evidencia) a `origin/main` del template, y actualización local del harness en Calles Posadas. El resultado de publicación se identifica mediante la historia Git y su correspondencia con `origin/main`. No incluye PR, despliegue ni publicación de cambios de producto en Calles Posadas. La publicación no convierte el pendiente nativo de SDD-002 en comprobado.

Este archivo es la única fuente del estado global vigente. El detalle de tareas vive en cada tasks.md; la historia de comprobaciones en evidence.md. Al cambiar el estado, revisar que contexto, contrato y encabezados no repitan un pendiente obsoleto.
