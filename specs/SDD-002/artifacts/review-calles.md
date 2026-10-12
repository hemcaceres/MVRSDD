# SDD-001 — Revisión independiente de incorporación en Calles Posadas

2026-10-08 — Rol Verifier, agente Codex `/root/sdd_review`; implementador `/root`. No implementé esta incorporación. Esta revisión aplica P-06 y delimita la actualización del harness autorizada, sin revalidar ni modificar features de producto. El informe se preparó en el workspace del template para que el Leader lo conserve como evidencia del destino; no escribí en Calles Posadas ni instalé/ejecuté herramientas nativas.

## Comprobaciones realizadas personalmente

Leí AGENTS, guía/roles del harness, README/contexto/decisiones, catálogo y contrato/tareas/evidencia de SDD-001; inspeccioné el antecedente PRD en cuanto al alcance del producto y sin convertir sus propuestas en permisos. Contrasté la canónica/adaptador/metadatos y las fuentes compartidas con el template revisado. No hay nueva capacidad de producto, nueva arquitectura ni autorización de publicación en este tramo.

Ejecuté comprobaciones Python stdlib de sólo lectura sobre el destino, con resultados exit 0:

- Recalculé SHA256 de los **128 archivos** del manifiesto del producto: cada hash vigente coincide con product-before.json y product-after.json; los dos manifiestos son iguales. Esta constatación cubre fuentes, datos, docs, pruebas, contratos/evidencia FEAT y archivos enumerados, no credenciales ni cachés excluidos de la línea de base.
- Recalculé los hashes de los **nueve archivos compartidos**: contenido vigente del destino igual al template y a source-hashes.json, sin dependencia de otra carpeta para utilizar el harness.
- Comparé AGENTS íntegro con su snapshot anterior tras retirar únicamente la entrada añadida: igualdad; el bloque Next.js también es idéntico. No se descartaron sus instrucciones ni se alteró su configuración.
- Comprobé que README conserva todo el texto anterior de producto como prefijo, y que las nueve filas FEAT del catálogo son idénticas a las anteriores. No se reaprueban ni reabren sus contratos/estados.
- Reconstruí por comparación los diffs de las **12 rutas** migradas antes del aviso posterior de fixtures: coinciden exactamente con migration-diff.patch, considerando por separado la corrección final documentada de la tabla. El patch inicial conserva la historia y no se confunde con el resultado vigente; el aviso posterior de README se revisó por separado a continuación.
- Comprobé referencias locales de **11 Markdown pertinentes** (entradas, guía/roles/prompts, README, catálogo y documentos SDD-001): sin enlaces locales rotos. No es una auditoría de todos los enlaces históricos del producto, de las plantillas relativas al destino de copia, de snapshots before ni de sitios web/anchors.

## Salidas leídas y aceptación

Inspeccioné technical-results.json, unit-tests.txt, snapshots before, product-before/after.json, source-hashes.json, migration-diff.patch, propuesta y catalog-table-fix.patch. La suite del Developer muestra dos tests OK, exit 0, con el comando stdlib documentado. **No repetí esa suite en el destino** porque genera temporales allí. Los scripts son byte a byte los mismos que comprobé personalmente en el template durante la confirmación de ERR-007; este informe distingue esa prueba anterior del output de esta incorporación. No ejecuté build, ETL, pruebas del producto ni interacción con la UI.

| Criterio | Dictamen del tramo |
|---|---|
| AC-001 | Respaldado por igualdad de las fuentes, diff y entradas mínimas; canónica resuelve fuentes del proyecto y metadatos/adaptador no duplican el router. No acredita discovery nativo. |
| AC-002 | Respaldado por hashes vigentes, snapshots, reglas Next.js/AGENTS, prefijo README y filas FEAT preservados. |
| AC-003 | Respaldado por salida real de dos tests y scripts compartidos revisados: aislamiento, copia VERSION y preservación ante sobrescritura. Pruebas técnicas del preparador, no conducta del agente ni aceptación de producto. |
| AC-004 | Pendiente de prueba real del usuario con Gemini en Antigravity IDE; Claude diferido por falta de suscripción. No se declara pass ni prueba visual; el diferimiento no bloquea incorporar/actualizar el harness. |

## Hallazgos y límites

**ERR-001 del destino confirmado resuelto:** el fallo original era una línea vacía que separaba SDD-001 de la tabla Markdown. Inspeccioné el patch de corrección y confirmé personalmente la fila contigua a FEAT-009 en el catálogo vigente, con las nueve filas FEAT preservadas. No detecté un defecto de implementación ni de preservación que impida entregar esta actualización.

Límite de futuras evaluaciones funcionales: el preparador copia AGENTS del producto, incluido el bloque generado Next.js que pide leer una guía en node_modules antes de escribir código. Los fixtures sintéticos de Python no incluyen node_modules. La orientación y preparación documental no requieren escribir código; los dos tests técnicos tampoco ejercen decisiones del agente. Para los casos bug/approved/resume, un agente podría detenerse ante esa guía ausente; **no se ejercieron esos casos funcionales en Calles** ni se atribuye un resultado que demuestre resolver ese conflicto. Antes de usarlos para medir conducta, precisar el alcance de las reglas de Next.js respecto del saludo Python o suministrar la referencia pertinente; mantener el workspace y permisos del fixture aislados. Es un límite de ese método de evaluación, sin afectar la actualización solicitada ni la prueba nativa de orientación pendiente.

Confirmación posterior de documentación: inspeccioné el aviso añadido al final del README vigente y el bloque de evidencia «Límite de los fixtures locales». Ambos explicitan conservación del bloque Next.js, ausencia de node_modules en los fixtures y registro del límite sin pass cuando una implementación requiera guías ausentes; distinguen la orientación inicial del saludo sintético. El aviso no elimina reglas ni promete evaluación funcional realizada. Esta aclaración es consistente con el límite señalado, sin cambiar el preparador ni reabrir contrato.

También contrasté los cambios acordados de README y SDD-002 en el template: distinguen Antigravity IDE de Gemini CLI, dejan las validaciones graduales a cargo del usuario, conservan el diferimiento de Claude y mantienen AC-006 sin pass. El catálogo del template ya indica el harness incorporado y no conserva una siguiente acción de incorporación obsoleta. No reinterpretan las pruebas anteriores ni agregan una exigencia de suscripción para actualizar SDD.

## Dictamen

**Favorable a entregar la incorporación técnica vigente**, con AC-001…AC-003 respaldados y ERR-001 cerrado. AC-004/PEND-SDD-001-001 sigue pendiente del usuario; PEND-SDD-001-002 mantiene Claude diferido conforme al acuerdo. No hay motivo para detener actualizaciones SDD por esos pendientes. No avalo declarar Verificada la conducta nativa ni concedo permiso de commit, push, PR o despliegue. Estado/siguiente acción se actualizan únicamente en el catálogo; el Leader incorpora este dictamen y los límites a la evidencia existente.
