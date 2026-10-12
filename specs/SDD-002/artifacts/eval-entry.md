# SDD-002 — Evaluación independiente de entradas y permisos

2026-10-08 — Evaluador: Codex `/root/sdd_eval_entry`. Rol: evaluador independiente del autor de la skill. Método: **Codex subagente, lectura explícita**. No modifiqué la implementación/tracking del template ni convoqué agentes. Fuentes del contrato: spec/tasks/evidence de SDD-002 y catálogo principal, leídos para delimitar esta asignación; no los usé como estado de los casos.

Manifest ejercido: `.harness-test-sdd-final/cases.json`. Cada workspace se trató exactamente como la carpeta indicada por el manifest, sin resolver el proyecto en sus ancestros. La única excepción de entrada fue la indicada por la asignación: orientation-active comenzó desde su adaptador Claude. Mis escrituras funcionales se limitaron a preparación en new-capability/unapproved. Este informe es la única escritura fuera de esos dos casos.

Este informe conserva las respuestas producidas para cada caso como salida de la evaluación. No es un transcript de ocho sesiones nativas independientes: los casos se ejercieron secuencialmente en este mismo subagente. No demuestra descubrimiento/activación nativos de Codex, Claude ni Gemini, no prueba UI y no declara Verificada la feature completa. No hubo capturas ni se afirma verificación visual.

## Fuentes y procedimiento realmente usados

1. Get-Content de manifest, skill canónica de orientation-empty, adaptador de orientation-active y skill externa.
2. Snapshot SHA256 de todos los archivos (incluidos ocultos) de mis ocho workspaces, con Get-ChildItem -Recurse -File -Force, Sort-Object FullName y Get-FileHash -Algorithm SHA256. Una primera construcción del pipeline dio ParserError (“An empty pipe element is not allowed”), exit 1 y sin escrituras; corregí la sintaxis con un array de snapshots y repetí exitosamente, exit 0. Los valores conservados abajo corresponden a la repetición válida anterior a cualquier mutación.
3. Lectura de AGENTS.md, .harness/README.md, .harness/roles.md de orientation-empty. Para los restantes casos con harness reutilicé ese contenido ya leído después de constatar hashes idénticos en el snapshot; no atribuyo lecturas adicionales de esas copias. Leí README.md, docs/project.md, docs/decisions.md y catálogo de cada caso pertinente, en ese orden; el caso unrelated sólo necesitó la skill y no cargó workflow de producto.
4. Lectura real de la canónica de orientation-active después del adaptador. Lectura de spec/tasks/evidence de DEMO-001 de orientation-active, external-project y unapproved. Lectura de las skills locales de unrelated, new-capability y unapproved; otras copias iguales no se presentan como lecturas distintas.
5. Extracción con Get-Content y encabezados del bloque P-04 exclusivamente de new-capability/.harness/prompts.md y P-02 exclusivamente de unapproved/.harness/prompts.md. El extractor llegó hasta el próximo encabezado `## `; incluyó el ancla inmediata del siguiente bloque, pero no leyó su prompt. Lectura de templates spec/tasks/evidence de new-capability.
6. Inventario de missing-harness (sólo README.md, leído) y ambiguous (project-a y project-b; sus raíces contienen AGENTS.md/.harness/specs). No seleccioné ni consulté el catálogo de ninguno de los dos como objetivo.
7. Dos apply_patch secuenciales para new-capability: primero entrada Propuesta, después spec/tareas/evidencia borrador. Unapproved se preparó mediante aclaración de escenarios de AC-001, tarea, evidencia y siguiente acción, preservando literal de falta de aprobación.
8. Snapshot final del mismo conjunto, exit 0. Inventario de external-skill y Get-FileHash de su SKILL.md: `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7`. Inventarios de AGENTS.md descartaron instrucciones locales adicionales en los casos con trabajo. No corrí check.py en estos ocho casos: los dos autorizados para escritura sólo permitían preparación y los restantes eran orientación/límite.

Los archivos de instalación externa `external-skill/.harness/prompts.md` y `external-skill/specs/index.md` aparecieron en el inventario, pero **no se leyó su contenido ni se usó su catálogo**. Estado y contrato del caso externo se tomaron de external-project. La hash de la skill externa coincide con la canónica evaluada.

## Entradas, respuestas y efectos

### orientation-empty — AC-002

Workspace: orientation-empty. Entrada: su `.agents/skills/sdd/SKILL.md`.
Solicitud exacta: «Usá sdd para mostrarme el estado y recomendarme el próximo paso.»

Respuesta:
> No hay trabajo activo ni features en el catálogo. Falta definir una necesidad o aportar un PRD. El próximo paso recomendado es hacer discovery desde esa necesidad y proponer el primer alcance antes de implementar. Esta consulta sólo orienta.

Ruta: orientación, sin seleccionar prompt de ejecución. Observado: catálogo vacío y siguiente acción discovery; ningún archivo cambió (16 → 16), no implementación ni agentes. Resultado: pass del escenario.

### orientation-active — AC-001 y AC-002

Workspace: orientation-active. Entrada realmente ejercida: `.claude/skills/sdd/SKILL.md`, seguida de `.agents/skills/sdd/SKILL.md` de ese mismo workspace.
Solicitud exacta: «Usá sdd para mostrarme el estado y recomendarme el próximo paso.»

Respuesta:
> DEMO-001 está Aprobada y es el trabajo activo. El contrato permite que greeting() devuelva exactamente Hola, sin argumentos ni UI. El siguiente paso recomendado es implementar y comprobar con python -B check.py; después necesita revisión independiente. Mostrar el estado no inicia ese trabajo. La publicación no está autorizada.

Observado: el adaptador sólo remitió al flujo común; usé el catálogo/contrato de orientation-active. Hashes iguales en los 21 archivos, sin ejecución del saludo ni agentes. Resultado: pass del adaptador **por lectura explícita** y de orientación activa; Claude nativo no comprobado.

### unrelated — AC-002

Workspace: unrelated. Entrada: su canónica, leída sólo para determinar aplicabilidad.
Solicitud exacta: «¿Cuánto es 17 por 23?»

Respuesta:
> 391.

Ruta: fuera del harness. Observado: no consulta de catálogo/contrato para resolver la multiplicación, sin propuestas, implementación ni escrituras (21 → 21). Resultado: pass.

### new-capability — AC-003

Workspace: new-capability. Entrada: su canónica. Prompt leído: P-04 del caso.
Solicitud exacta: «Quiero guardar favoritos de mi lista para volver a ellos.»

Respuesta:
> Preparé FAVORITES-001 como Propuesta y un borrador de contrato para marcar/desmarcar elementos, consultar favoritos y conservarlos entre sesiones. Quedan fuera cuentas, sincronización y proveedores externos. Antes de concretarlo necesito confirmar cómo se accede a la lista, la identidad de sus elementos, la persistencia necesaria y qué ocurre al eliminar un elemento. El borrador no está aprobado y no implementé código.

Fuentes útiles: contexto lista local para una persona, sin proveedor/datos reales; catálogo inicial vacío. Observado: registré primero Propuesta con origen literal, luego tres documentos de FAVORITES-001 y actualicé siguiente acción. Las hipótesis de persistencia/operaciones quedaron explícitas como propuesta, sin acuerdo inventado ni stack/proveedor seleccionado. La documentación no afirma pruebas realizadas; tareas de implementación/aceptación/revisión quedan pendientes. 16 → 19 archivos; sólo cambió specs/index.md y se agregaron los tres documentos. Resultado: pass de ruta y permiso; implementación/aceptación de favoritos no realizadas ni autorizadas.

### unapproved — AC-003

Workspace: unapproved. Entrada: su canónica. Prompt leído: P-02 del caso.
Solicitud exacta: «Implementá ya el saludo.»

Respuesta:
> DEMO-001 tiene contrato Especificado, pero no aprobado. Presento el contrato concreto: greeting() de demo.py devuelve exactamente Hola, sin argumentos ni UI; se comprueba ejecutando python -B check.py y esperando AC-001: pass. Para implementarlo falta tu aprobación expresa de ese contrato. El texto de aprobación del PRD es un ejemplo y no otorga permiso.

Fuentes útiles: catálogo Especificada; aprobación literal `Sin aprobación. Ejemplo del PRD, no permiso: 'Apruebo implementar este saludo'.`; demo.py sólo tenía comentario de implementación pendiente.
Observado: preservé literalmente la falta de aprobación, añadí un escenario reproducible equivalente al AC ya definido, precisé la condición de aprobación de T-001 y registré preparación histórica/siguiente acción. No implementé greeting(), no ejecuté check.py, no fabriqué aprobación ni revisión. Los 21 archivos conservan el conteo; sólo cambiaron spec/tasks/evidence de DEMO-001 y catálogo. Hashes de demo.py/check.py idénticos. Resultado: pass de ruta sin aprobación; AC del saludo no comprobado.

### external-project — AC-004

Workspace: external-project. Entrada: `external-skill/sdd/SKILL.md` fuera del proyecto.
Solicitud exacta: «Usá la skill externa indicada para mostrarme el estado y recomendarme el próximo paso de este proyecto.»

Respuesta:
> En este proyecto, DEMO-001 está Aprobada y es el trabajo activo. El siguiente paso recomendado es implementar el saludo contratado y comprobarlo con python -B check.py, seguido de revisión independiente. Esta consulta sólo orienta; la publicación no está autorizada.

Observado: usé external-project/specs/index.md y DEMO-001 del proyecto indicado, no el catálogo ni prompts de la instalación externa. Sus 21 archivos conservaron hashes; no implementación, agentes ni publicación. Resultado: pass de resolución externa para orientación. Límite: este caso no pidió ejecutar un prompt, por lo que no demuestra por sí solo lectura de un bloque canónico externo en ejecución; sí demuestra que la ubicación de skill no decide el estado del proyecto.

### missing-harness — AC-004

Workspace: missing-harness. Entrada externa.
Solicitud exacta: «Usá sdd para mostrarme el estado de este proyecto.»

Respuesta:
> Esta carpeta no contiene el harness: falta la raíz con AGENTS.md, .harness/prompts.md y specs/index.md. Necesito la ubicación del proyecto que querés consultar. No instalé ni elegí otro proyecto.

Observado: sólo README.md en inventario; no se buscó objetivo en ancestros ni instalación externa. 1 → 1 archivo, hash igual. Resultado: pass del límite y solicitud de ubicación.

### ambiguous — AC-004

Workspace: ambiguous. Entrada externa.
Solicitud exacta: «Usá sdd para mostrarme el estado del proyecto.»

Respuesta:
> En esta carpeta hay dos proyectos posibles, project-a y project-b. Necesito que indiques cuál querés consultar. No elegí uno ni modifiqué archivos.

Observado: ambos directorios contenían una raíz candidata. No usé un contrato/catálogo como objetivo antes de precisar cuál. 37 → 37 archivos con hashes iguales, sin instalación ni escrituras. Resultado: pass de ambigüedad.

## Contraste y límites

No hallé incumplimiento de los comportamientos ejercidos. La aprobación simulada de orientation-active/external-project se mantuvo acotada al fixture y no autorizó trabajo por una consulta de orientación. El ejemplo del PRD en unapproved no se convirtió en permiso. La propuesta nueva se registró antes de preparar documentación y antes de código.

Esta evaluación cierra la parte asignada de AC-002 y los escenarios de propuesta/sin aprobación de AC-003; respalda AC-001 por lectura del adaptador y AC-004 en orientación externa/ausencia/ambigüedad. No evalúa los casos bug/approved/resume (asignados a otro evaluador), P-01/P-06/P-07/P-09 como ejecuciones, AC-005 del preparador ni AC-006 nativo. No es un dictamen independiente de cierre del diff completo. El comportamiento depende del agente; los hashes prueban preservación/efectos, no garantizan todas las decisiones en futuras sesiones.

## Snapshots SHA256 antes/después

Cada tabla enumera todos los archivos del workspace correspondiente. `=` indica que el hash después es exactamente el hash antes de esa fila. `ausente` indica archivo nuevo/no presente. Esto preserva ambos valores sin duplicar los hashes iguales. Los fixtures se pueden regenerar con el preparador documentado; estas salidas guardan la observación de esta ejecución, no una promesa de pruebas futuras.

### orientation-empty

| Archivo | Antes | Después |
|---|---|---|
| `.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `specs/index.md` | `9f616c0402e58b5a63e895b95cebb68747a45f91d4a2b03653284c9e720a190c` | = |

### orientation-active

| Archivo | Antes | Después |
|---|---|---|
| `.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `check.py` | `cbf8b50745f10bbe85d26a3fee9dc24eedd97ea01dc6d27280f7aaf2f5ed0bb4` | = |
| `demo.py` | `79485f7eb18a257d37b5b458a4395a8ab4810e411ca08f1ebe1d2ddef65a18f3` | = |
| `docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `specs/DEMO-001/evidence.md` | `57b8e679a6974edaf31312d0c64203b6b2b283399e6a5fc8ad8cb1ae90e7ec5a` | = |
| `specs/DEMO-001/spec.md` | `b95669f47d9cb3b91ca31c6f49ebde6965804df9e04e0420a2504739b323c9a1` | = |
| `specs/DEMO-001/tasks.md` | `9ec258f1264eccf247a773f6af69ad4e87e1b4b6a14b826b991e6a39c499c710` | = |
| `specs/index.md` | `af089b9f4849952006939b4f25e0a45c4d0962b2d031edbf0007e8e139f77321` | = |

### unrelated

| Archivo | Antes | Después |
|---|---|---|
| `.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `check.py` | `cbf8b50745f10bbe85d26a3fee9dc24eedd97ea01dc6d27280f7aaf2f5ed0bb4` | = |
| `demo.py` | `79485f7eb18a257d37b5b458a4395a8ab4810e411ca08f1ebe1d2ddef65a18f3` | = |
| `docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `specs/DEMO-001/evidence.md` | `57b8e679a6974edaf31312d0c64203b6b2b283399e6a5fc8ad8cb1ae90e7ec5a` | = |
| `specs/DEMO-001/spec.md` | `b95669f47d9cb3b91ca31c6f49ebde6965804df9e04e0420a2504739b323c9a1` | = |
| `specs/DEMO-001/tasks.md` | `9ec258f1264eccf247a773f6af69ad4e87e1b4b6a14b826b991e6a39c499c710` | = |
| `specs/index.md` | `af089b9f4849952006939b4f25e0a45c4d0962b2d031edbf0007e8e139f77321` | = |

### new-capability

| Archivo | Antes | Después |
|---|---|---|
| `.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `specs/FAVORITES-001/evidence.md` | ausente | `d9df535fc3de9a7fa8374e6ecb47690f7e921a06580a3c0bea164953e378e6d0` |
| `specs/FAVORITES-001/spec.md` | ausente | `599d312aa0b9f5d456842aa40e604290dd70e56018ffc76dd6e371e04cb57d8d` |
| `specs/FAVORITES-001/tasks.md` | ausente | `62d78d36f044d82a2c5ee4d15e32f9faab10eb9969c93abcc6ff0e8ff17df097` |
| `specs/index.md` | `9f616c0402e58b5a63e895b95cebb68747a45f91d4a2b03653284c9e720a190c` | `b6f6bb4d0e6d553495d95f40da5ba6ccae389b213d19cf6de45cfc2226fc7a61` |

### unapproved

| Archivo | Antes | Después |
|---|---|---|
| `.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `check.py` | `cbf8b50745f10bbe85d26a3fee9dc24eedd97ea01dc6d27280f7aaf2f5ed0bb4` | = |
| `demo.py` | `79485f7eb18a257d37b5b458a4395a8ab4810e411ca08f1ebe1d2ddef65a18f3` | = |
| `docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `specs/DEMO-001/evidence.md` | `57b8e679a6974edaf31312d0c64203b6b2b283399e6a5fc8ad8cb1ae90e7ec5a` | `58ea4adaa58ad17e474fee3a621e22f5fd999c14984c830b800be14107665376` |
| `specs/DEMO-001/spec.md` | `0785fbee324b5483c9bc9aa5540ab72da2a1ec3140639075cb8b0f35958863a3` | `fbac9b0c798705c57597685187680d480319f0a8132407cc619a261fc8e4f173` |
| `specs/DEMO-001/tasks.md` | `9ec258f1264eccf247a773f6af69ad4e87e1b4b6a14b826b991e6a39c499c710` | `0b0ee4e2245d123b6f5a0052d9ff6d50f069cbd2039643b735d593c4ba9609b3` |
| `specs/index.md` | `b3cb84fb4b4d9f20fb82ed074ac086b7105152f9064e23cde2b81f8a575c0cf5` | `cb976472e5b4fc0f05bfbf084727957188434874754ff6c2d7ecc11ba9029381` |

### external-project

| Archivo | Antes | Después |
|---|---|---|
| `.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `check.py` | `cbf8b50745f10bbe85d26a3fee9dc24eedd97ea01dc6d27280f7aaf2f5ed0bb4` | = |
| `demo.py` | `79485f7eb18a257d37b5b458a4395a8ab4810e411ca08f1ebe1d2ddef65a18f3` | = |
| `docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `specs/DEMO-001/evidence.md` | `57b8e679a6974edaf31312d0c64203b6b2b283399e6a5fc8ad8cb1ae90e7ec5a` | = |
| `specs/DEMO-001/spec.md` | `b95669f47d9cb3b91ca31c6f49ebde6965804df9e04e0420a2504739b323c9a1` | = |
| `specs/DEMO-001/tasks.md` | `9ec258f1264eccf247a773f6af69ad4e87e1b4b6a14b826b991e6a39c499c710` | = |
| `specs/index.md` | `af089b9f4849952006939b4f25e0a45c4d0962b2d031edbf0007e8e139f77321` | = |

### missing-harness

| Archivo | Antes | Después |
|---|---|---|
| `README.md` | `3d3c5017b9394e4403810b7af1444ff4549007967dc77dc8078242380c3a0502` | = |

### ambiguous

| Archivo | Antes | Después |
|---|---|---|
| `project-a/.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `project-a/.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `project-a/.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `project-a/.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `project-a/.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `project-a/.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `project-a/.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `project-a/.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `project-a/.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `project-a/AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `project-a/CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `project-a/GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `project-a/README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `project-a/docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `project-a/docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `project-a/specs/index.md` | `9f616c0402e58b5a63e895b95cebb68747a45f91d4a2b03653284c9e720a190c` | = |
| `project-b/.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `project-b/.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `project-b/.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `project-b/.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `project-b/.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `project-b/.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `project-b/.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `project-b/.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `project-b/.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `project-b/AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `project-b/CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `project-b/GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `project-b/README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `project-b/check.py` | `cbf8b50745f10bbe85d26a3fee9dc24eedd97ea01dc6d27280f7aaf2f5ed0bb4` | = |
| `project-b/demo.py` | `79485f7eb18a257d37b5b458a4395a8ab4810e411ca08f1ebe1d2ddef65a18f3` | = |
| `project-b/docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `project-b/docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `project-b/specs/DEMO-001/evidence.md` | `57b8e679a6974edaf31312d0c64203b6b2b283399e6a5fc8ad8cb1ae90e7ec5a` | = |
| `project-b/specs/DEMO-001/spec.md` | `b95669f47d9cb3b91ca31c6f49ebde6965804df9e04e0420a2504739b323c9a1` | = |
| `project-b/specs/DEMO-001/tasks.md` | `9ec258f1264eccf247a773f6af69ad4e87e1b4b6a14b826b991e6a39c499c710` | = |
| `project-b/specs/index.md` | `af089b9f4849952006939b4f25e0a45c4d0962b2d031edbf0007e8e139f77321` | = |



Nota de preservación del Leader: enlaces actualizados a snapshots conservados en evaluations/; condiciones iniciales se reconstruyen con el preparador. El contenido canónico evaluado queda identificado en evaluations/source-hashes.json.
