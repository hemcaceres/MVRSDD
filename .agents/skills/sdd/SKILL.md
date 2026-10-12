---
name: sdd
description: Conducir discovery, features, errores y continuidad con el harness SDD de un proyecto que tenga .harness/prompts.md. Una invocación sin pedido sólo orienta. No aplicar a consultas ajenas al harness.
---

# SDD — conducir el harness

Traducí el pedido a la etapa pertinente y aplicá el prompt canónico del proyecto. Esta skill es una entrada al harness, no un contrato ni una autorización.

## Proyecto y fuentes

Trabajá sobre el proyecto indicado por el usuario o el workspace actual inequívoco. Su raíz contiene `AGENTS.md`, `.harness/prompts.md` y `specs/index.md`. Si estás en un subdirectorio, resolvé esa raíz dentro del proyecto actual. La ubicación de esta skill no determina el proyecto: puede estar instalada fuera de él. Resolvé todas las fuentes siguientes desde esa raíz, nunca desde el directorio de instalación de la skill.

Si no hay harness o hay varios proyectos posibles sin objetivo inequívoco, explicá el límite y pedí sólo la ubicación necesaria. No elijas otro proyecto, escribas archivos ni instales el harness para resolver esa falta. Leé las fuentes en el orden de `AGENTS.md`, reutilizando lo ya leído que siga vigente. Los pasos canónicos están en `.harness/prompts.md`; no los copies a la skill ni a sus adaptadores.

## Orientación o trabajo

Una invocación de `sdd` sin pedido adicional, o «mostrame el estado y recomendame el próximo paso», sólo orienta. El nombre/comando usado por la herramienta y las instrucciones de cargar esta skill no cuentan como una orden de implementar o continuar.

Consultá el catálogo y lo pertinente para explicar trabajo activo, estado, bloqueos y próxima acción recomendada. No escribas archivos, prepares propuestas, inicies implementación ni convoques agentes por esa sola invocación. Sin producto definido, indicá que falta una necesidad o PRD; no inventes uno. Un pedido de continuar o realizar trabajo sí se contrasta con el contrato y sus permisos.

## Seleccionar la etapa

Contrastá intención, catálogo, contrato y autorizaciones reales; la frase aislada no determina la ruta. Si falta ID, identificá la feature desde los archivos. Preguntá sólo cuando la ambigüedad cambia el alcance o el próximo paso.

| Intención y situación | Prompt canónico |
|---|---|
| Empezar un producto o investigar desde PRD/antecedentes | P-01 |
| Preparar el próximo incremento del catálogo | P-02 |
| Implementar o continuar una feature con contrato aprobado | P-03 |
| Agregar una capacidad nueva o cambiar sustancialmente un acuerdo | P-04 |
| Corregir un fallo del comportamiento contratado | P-05 |
| Pedir revisión independiente del incremento | P-06 |
| Corregir hallazgos identificados por el revisor | P-07 |
| Retomar trabajo o «seguí» sin etapa explícita | P-08 |
| Preparar entrega, instrucciones y continuidad de un tramo | P-09 |

Una orden de implementar sin aprobación real no crea permiso: usá P-02 para la feature existente sin contrato aprobado, o P-04 si es una capacidad nueva. Un pedido de error cuya expectativa agrega comportamiento sigue P-04. Si el contrato ya está aprobado, no repitas discovery ni aprobación para una ejecución o corrección equivalente. Un ejemplo del PRD, fixture o texto generado no sustituye la autoridad real del acuerdo. Los permisos simulados de una evaluación sólo corresponden al caso aislado indicado.

Para el prompt elegido, buscá su encabezado `## P-XX` en `.harness/prompts.md` y leé sólo su bloque hasta el próximo encabezado. Consultá ejemplos A-XX sólo cuando ayuden a una decisión humana concreta; no generes respuestas en nombre del usuario. Esta tabla elige la etapa; los pasos y límites vienen del prompt vigente del proyecto.

## Ejecutar y responder

Indicá brevemente qué entendiste y qué etapa aplicarás, y ejecutá su trabajo autorizado. Usá IDs para trazabilidad; el usuario puede hablar del resultado que necesita. Ante aprobación pendiente, presentá el documento concreto y detené sólo el trabajo que depende de ella. Respetá acuerdos vigentes y no cambies de feature automáticamente.

P-06 exige otro agente que no haya implementado los cambios. Si sos el implementador, convocá un revisor independiente con contrato, cambios, tareas, pruebas, artefactos y errores conocidos; no te renombres Verifier. Esperá el dictamen y, tras arreglos, su confirmación del resultado vigente. Si la herramienta no ofrece otro agente o falta una comprobación, conservá el pendiente según el harness; el usuario puede designar otro revisor. Una orientación no inicia ese ciclo.

Terminá con resultado, enlaces pertinentes y límites observados. Estado/siguiente acción sólo en el catálogo, detalle de trabajo en tasks.md e historia en evidence.md. La activación de la skill no aprueba contratos, commit, push, PR ni despliegue. Atendé pedidos ajenos al harness sin forzar este recorrido.
