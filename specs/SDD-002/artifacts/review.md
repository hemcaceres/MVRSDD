# SDD-002 — Revisión independiente

2026-10-08 — Verifier: Codex `/root/sdd_review`. Implementador: `/root`. No implementé la skill, adaptadores, preparador ni documentación; mis únicas escrituras de entrega son este informe. Apliqué P-06 mediante lectura de la entrada canónica y las fuentes del harness en el orden requerido. No alteré MVR, configuración, autenticación o modelo ni realicé publicación.

## Alcance y comprobaciones personales

Contrasté el contrato autorizado por «Hacelo» con el diff de AGENTS.md, README.md y catálogo, y leí los archivos nuevos completos: skill canónica, adaptador Claude, openai.yaml, preparador, tests y validador. Comprobé las referencias P-01…P-09 y los límites de aprobación, propuestas, permisos de fixtures, revisión independiente y publicación. CLAUDE.md/GEMINI.md y prompts se conservan como fuentes comunes, sin duplicar su flujo en adaptadores. Los hashes vigentes de canónica/adaptador coinciden con los de la evaluación independiente.

Ejecuté personalmente desde la raíz:

```text
python -B -X utf8 .harness/tests/test_sdd_cases.py
exit 0; Ran 2 tests; OK

PYTHONPATH=.harness-test-sdd-deps (variable PowerShell)
python -B -X utf8 specs/SDD-002/artifacts/validate_structure.py
exit 0; UTF-8, frontmatter/metadatos compatibles, P-01…P-09 existentes

git diff --check
exit 0; sin salida
```

Los tests crean evaluaciones temporales dentro del workspace y verifican aislamiento y preservación ante sobrescritura. Son pruebas del preparador, no certificación de decisiones del agente. No reinstalé PyYAML; usé la dependencia aislada disponible.

También ejecuté `python -B check.py`, con cwd en cada fixture final bug, approved y resume: tres exits 0, tres salidas `AC-001: pass`. Esta repetición confirma el retorno exacto del saludo resultante. No reproduje personalmente el fallo previo del bug ni tomé decisiones del router en esas ejecuciones: su reproducción y selección P-05/P-03/P-08 pertenecen al evaluador de ejecución.

## Artefactos inspeccionados y suficiencia

Leí completos [eval-entry.md](eval-entry.md), [eval-execution.md](eval-execution.md), [technical-results.json](technical-results.json) y los tres logs nativos. Inspeccioné además los contratos y efectos finales de new-capability/unapproved y documentos/resultados de los saludos. La lectura explícita de los evaluadores fue ejercida por agentes distintos del autor; no se presenta como activación nativa ni como ocho sesiones independientes.

| AC | Conclusión de esta revisión |
|---|---|
| AC-001 | Respaldado: estructura consistente, un router canónico, metadatos sin proceso y adaptador ejercido por lectura explícita. |
| AC-002 | Respaldado en catálogo vacío/activo y consulta ajena; respuestas y snapshots conservan hashes sin escrituras ni implementación. |
| AC-003 | Respaldado en los escenarios solicitados: propuesta/sin aprobación y bug/aprobada/continuidad. Se conserva el error, los contratos y la revisión/publicación separadas; los saludos no se declaran Verificada. |
| AC-004 | Respaldado para orientación con skill externa, límites de ausencia/ambigüedad y aplicación real de P-02 desde el proyecto objetivo con skill externa en el caso suplementario. |
| AC-005 | Respaldado por preparador reproducible Python stdlib, manifest relativo y pruebas personales de aislamiento/preservación; snapshots y entradas finales conservados en el repo tras resolver REV-SDD-002-001. |
| AC-006 | Parcial, sin aceptación nativa completa. Claude muestra discovery de sdd pero falla por login; Codex falla por permisos/modelo configurado; Gemini no disponible. Ninguno demuestra orientación nativa exitosa. |

Los logs concuerdan con ERR-004/005 y PEND-SDD-002-001: no prueban un defecto de skill ni una corrección operativa. Los fallos técnicos ERR-001…003 tienen comprobaciones posteriores registradas, compatibles con mis tests vigentes. P-01/P-06/P-07/P-09 se contrastaron como instrucciones; no se afirma evaluación funcional completa de esas rutas. No hubo UI, capturas o inspección visual de esta versión; no se reutilizó evidencia visual histórica de MVR.

2026-10-08 — Ronda suplementaria de AC-004: inspeccioné completo [eval-external-execution.md](eval-external-execution.md) y su [entrada conservada](evaluations/external-execution/case.json). El evaluador leyó y aplicó P-02 desde target/.harness/prompts.md con la skill externa; el prompt vecino de installed tiene hash distinto. Preparó sólo contrato/tareas/evidencia/catálogo ante falta de aprobación, sin implementar, instalar o publicar. Esto cierra el límite anterior de comprobar la raíz externa únicamente en orientación. No es ejecución nativa ni ejecución personal mía del router. Comparé byte a byte sus 12 archivos preservados contra los originales ejercidos: sin diferencias, exit 0. Los hashes vigentes de canónica/adaptador continúan coincidentes; `git diff --check` volvió a pasar sin salida. No cambió implementación, por lo que no repetí pruebas ajenas a esta ampliación de evidencia.

## Hallazgo de entrega

REV-SDD-002-001 — Evidencia funcional en carpetas ignoradas. Origen: esta revisión. Ubicación: enlaces de eval-execution.md a `../../../.harness-test-sdd-final/…` y manifest temporal citado por ambos evaluadores. Reproducción: `.gitignore` excluye `.harness-test-*/`; una nueva copia del repo pierde esos resultados/contratos finales. Esperado: entrada, cambios y resultados inspeccionables desde el repo, sin depender de la computadora del autor. Impacto: insuficiencia de evidencia portable, no defecto del router. Corrección esperada: conservar manifest/snapshots finales pertinentes bajo artifacts y actualizar los enlaces; no convertirlos en fuentes de instrucciones activas. Comprobación: archivos disponibles, referencias relativas resolubles y snapshots coincidentes con los fixtures ejercidos. Pendiente de confirmación del Developer.

2026-10-08 — Confirmación independiente del arreglo REV-SDD-002-001: Developer conservó entradas y resultados en [evaluations/NOTICE.md](evaluations/NOTICE.md), actualizó enlaces de eval-execution y añadió nota de preservación a eval-entry. Ejecuté una comparación byte a byte de los 90 archivos preservados frente a sus originales ejercidos; no hubo diferencias. Comprobé referencias de eval-execution/NOTICE y hashes de las fuentes canónicas: todas disponibles/coincidentes, exit 0. El NOTICE distingue snapshots finales, condiciones iniciales regenerables y permisos simulados. **Hallazgo resuelto** para los once casos originales; no cambia sus resultados ni acredita activación nativa.

## Dictamen fechado

No detecté defectos de implementación ni ampliación silenciosa del permiso. Dictamen favorable del resultado común vigente y de su evidencia portable: REV-SDD-002-001 resuelto; AC-001…AC-005 respaldados por las comprobaciones descritas, incluido el caso suplementario de raíz externa. AC-006 conserva aceptación nativa incompleta conforme a PEND-SDD-002-001. Por ese pendiente **no avalo marcar SDD-002 Verificada**. Esta revisión tampoco concede autorización humana de publicación. Estado y siguiente acción vigentes se mantienen únicamente en el catálogo.

## 2026-10-08 — Confirmación posterior de ERR-007

Esta ronda renueva el dictamen anterior tras el arreglo del preparador y sus referencias; no reinterpreta las evaluaciones históricas. Contrasté el [preparador anterior conservado](evaluations/prepare_sdd_cases.before-version.py) con el vigente: el único cambio del script es añadir VERSION a los archivos copiados por `project()`. Su SHA256 anterior coincide con el valor histórico de source-hashes.json. La assertion nueva del test comprueba la existencia/contenido del archivo VERSION referenciado por `.harness/README.md`.

Ejecuté personalmente de nuevo `python -B -X utf8 .harness/tests/test_sdd_cases.py`: exit 0, dos tests OK. Comprobé que README/roles añadidos al snapshot externo son byte a byte los originales del fixture, y que VERSION es el del template; VERSION no se atribuye al snapshot inicial de la evaluación, donde faltaba. La skill/adaptador conservan sus hashes evaluados. `git diff --check`: exit 0, sin salida.

Una primera auditoría amplia de referencias sobre 109 Markdown (incluidos ocultos) salió 1 por las tres plantillas base `.harness/templates/{spec,tasks,evidence}.md`: sus enlaces `../index.md` son relativos al destino de copia, una condición preexistente fuera de este arreglo. Repetí con ese dominio explícito excluido: 106 Markdown, ninguna referencia local rota, exit 0. Esto incluye las fuentes suplementarias conservadas; no prueba enlaces web, anchors ni comportamiento de UI. No repetí decisiones del router ni pruebas nativas porque ese flujo no cambió.

**ERR-007 confirmado resuelto**: las fuentes suplementarias tienen sus referencias disponibles y las nuevas evaluaciones conservan VERSION. Dictamen vigente favorable para AC-001…AC-005, sin hallazgos de implementación/preservación pendientes de esta revisión. AC-006 permanece parcial y sigue impidiendo marcar SDD-002 Verificada. No hay autorización de publicación.
