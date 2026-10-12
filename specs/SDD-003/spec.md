# SDD-003 — Ciclo de implementación y revisión con contraejemplos

## Origen y alcance

El usuario pidió comparar el [video de Xavier Mitjana](https://www.youtube.com/watch?v=sc6PJpFyrvY) con los prompts del harness. Tras revisar su transcripción automática completa y los prompts vigentes, se propusieron dos bloques concretos para P-03 y P-06. El usuario respondió «Perfecto, hace las modificaciones» el 2026-10-12.

Integrar en `.harness/prompts.md` el ciclo de planificar, implementar, ejercer aceptación, inspeccionar y corregir; autonomía para decisiones menores dentro del contrato; comprobación del flujo completo y límites de mocks; y registro de la causa cuando no se pueda avanzar. P-06 explicita búsqueda de contraejemplos y hallazgos fundamentados, distinguiendo defectos de preferencias o mejoras fuera del alcance.

Excluir cambios en otros prompts, skills, plantillas o producto, nuevas herramientas, rondas obligatorias, exigencia de perfección, ampliación de alcance y publicación. Mantener las aprobaciones, evidencia, revisión independiente y condiciones de cierre existentes. No hay decisión nueva de arquitectura.

## Aceptación y comprobación prevista

- AC-001: con P-03 vigente como condición inicial, integrar el bloque aprobado y leer el resultado completo. Debe indicar autonomía acotada, ciclo de aceptación/corrección, repetición sólo ante diferencias o riesgos concretos, flujo completo, límites de simulaciones y causa de falta de avance. Método: contraste textual del diff y lectura semántica independiente, registrados en evidence.md.
- AC-002: con P-06 vigente como condición inicial, integrar la búsqueda de contraejemplos. Debe fundamentar hallazgos con criterios o impactos, distinguir preferencias y mejoras fuera del alcance y conservar la independencia del revisor. Método: contraste textual del diff y revisión independiente del bloque completo.
- AC-003: tras la edición, comparar `.harness/prompts.md` contra su versión inicial. Sólo P-03 y P-06 pueden cambiar; se conservan nueve prompts, referencias y límites de aprobación/publicación/cierre. Método: comparación por bloques con Git, `git diff --check` sobre el archivo y revisión de enlaces/documentos del tramo. No se cambia ni se reinterpreta SDD-002 o sus comprobaciones históricas.

El objeto de aceptación es el texto de los prompts; estas comprobaciones no demuestran mejoras de rendimiento de agentes ni ejecución funcional/nativa del nuevo ciclo. No hay interfaz ni código de producto que ejercer.

## Aprobación

2026-10-12 — decisor: usuario de esta conversación. Referencia: «Perfecto, hace las modificaciones», inmediatamente después de la respuesta que presentó los dos bloques completos y recomendó el ajuste acotado a P-03 y P-06. Autoriza integrar y comprobar ese cambio concreto; este documento conserva el acuerdo, sin atribuir una aprobación separada del archivo ni permisos de publicación.

[Tareas](tasks.md) · [Evidencia](evidence.md) · [Catálogo](../index.md).
