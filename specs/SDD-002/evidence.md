# SDD-002 — Evidencia

## 2026-10-08 — Propuesta, discovery y autorización

Leader/Analyst: Codex `/root`. Registró SDD-002 como Propuesta antes de crear implementación. Leyó instrucciones, contexto y catálogo; el árbol Git estaba limpio (`git status --short`, exit 0, sin salida). Revisó el antecedente SDD-001 de MVR y la skill `skill-creator`. Concretó en [spec.md](spec.md) los cuatro ajustes autorizados por «Hacelo» y métodos de aceptación antes de código. No hubo decisión nueva de stack ni intervención de Architect.

La revisión previa ejecutó en MVR su validador estructural con exit 0, y consultó documentación oficial de [OpenAI](https://learn.chatgpt.com/docs/build-skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/), [Claude Code](https://code.claude.com/docs/en/skills) y [Agent Skills](https://agentskills.io/specification). Es antecedente técnico, no prueba funcional de esta versión. MVR conserva sus archivos; no se importan sus permisos simulados ni su cierre histórico al template.

Estado y siguiente acción en [catálogo](../index.md).

## 2026-10-08 — Implementación y autocontrol técnico

Developer: Codex `/root`. Incorporó skill neutral, adaptador de lectura Claude, metadatos OpenAI, entrada común en AGENTS.md y documentación de uso/pruebas. La raíz se resuelve desde el proyecto actual/indicado, sin referencia `../../../` desde la instalación. Conservó los prompts y las entradas CLAUDE.md/GEMINI.md sin copiar el workflow. No modificó MVR ni sus acuerdos/evidencia.

Creó el [preparador](../../.harness/tests/prepare_sdd_cases.py) con once casos y [dos tests técnicos](../../.harness/tests/test_sdd_cases.py) sobre aislamiento y rechazo de sobrescritura. `python -B -X utf8 .harness/tests/prepare_sdd_cases.py` generó once casos con exit 0. Tras completar metadatos, `python -B -X utf8 .harness/tests/prepare_sdd_cases.py --output .harness-test-sdd-final` generó los casos vigentes con exit 0. Repetir este último comando devolvió exit 1 esperado: «Evaluation already exists; preserve it and choose a new output directory.» No se sobrescribió la evaluación. Los tests posteriores al arreglo del directorio temporal devolvieron exit 0, dos tests OK. Esto comprueba el preparador, no aceptación funcional del agente.

El generador de skill-creator creó agents/openai.yaml con `--name sdd`, Python UTF-8 y los tres valores de interfaz del archivo. Dos `quick_validate.py` sobre skill canónica/adaptador devolvieron exit 0 («Skill is valid!»). El [validador local](artifacts/validate_structure.py) confirmó UTF-8, frontmatter, metadatos compatibles, selección implícita y existencia de P-01…P-09 con exit 0. [Salidas reales](artifacts/technical-results.json). AC-001 sólo tiene autocontrol técnico aquí; conducta/adaptador/raíz se contrastan en evaluación independiente.

Para repetir la comprobación local desde la raíz con Python 3 (PowerShell):

```powershell
python -B -m pip install --target .harness-test-sdd-deps PyYAML==6.0.3 --disable-pip-version-check
$env:PYTHONPATH = (Resolve-Path .harness-test-sdd-deps).Path
python -B -X utf8 specs/SDD-002/artifacts/validate_structure.py
python -B -X utf8 .harness/tests/test_sdd_cases.py
```

PyYAML sólo es dependencia del validador; se obtuvo de caché en la carpeta ignorada, instalación exit 0. La skill y el preparador no lo requieren. Los validadores externos de skill-creator son una comprobación adicional del entorno del autor; la validación local queda en el repo para repetir sin depender de su ruta personal. Los evaluadores independientes reciben cada solicitud y fixture, con autorización limitada a su workspace.

## ERR-001 — Dependencia del validador ausente

2026-10-08, origen autocontrol `/root`, comprobación técnica AC-001. Esperado: generador/validadores ejecutables. Observado: Python del host y runtime empaquetado no incluían `yaml`, `ModuleNotFoundError`, exit 1. No se presentó como validación exitosa. Corrección del entorno de prueba: PyYAML 6.0.3 en `.harness-test-sdd-deps`; ambos quick_validate y validador local devolvieron exit 0. Cierra esta falta de dependencia sin agregar runtime a la skill.

## ERR-002 — Temporal fuera del workspace

2026-10-08, origen tests del preparador `/root`, AC-005. Esperado: crear/copiar casos aislados y conservar evaluación existente. Observado: ambos tests fallaron al crear subdirectorios del temporal Windows con WinError 5 y errores de limpieza; el sandbox no permitía esos accesos. Corrección: temporales de los tests bajo `.harness-test-sdd-unit` dentro del repo, ignorados. Reejecución: dos tests OK, exit 0; cierra ese fallo del entorno. No se eliminan temporales ajenos ni se atribuye ese fallo a la conducta de la skill.

## ERR-003 — Metadatos en carpeta protegida

2026-10-08, origen generador `/root`, AC-001. Tras evitar importación YAML con `--name sdd`, el generador falló con WinError 5 al crear `.agents/skills/sdd/agents`; apply_patch también rechazó crear sus directorios. El sandbox trata `.agents` como carpeta protegida. Se ejecutó el mismo generador mediante escalación revisada automáticamente, limitada a los metadatos autorizados; exit 0, «Created agents/openai.yaml». Validación UTF-8/YAML posterior exit 0. Cierra la creación faltante; no modifica permisos permanentes ni configuración de usuario.

## 2026-10-08 — Intentos nativos y límites de AC-006

Developer `/root`, autocontrol por CLI, sin UI ni capturas. Inventario mediante Get-Command encontró Python 3, Codex CLI y Claude Code, sin Gemini CLI. Las versiones/comandos se inspeccionaron mediante --help; no se instaló una herramienta ni se alteró autenticación/modelo.

- Codex: en el caso orientation-active, `codex -a never exec --sandbox read-only --ephemeral --skip-git-repo-check --json '$sdd'`, exit 1. [Salida inicial](artifacts/native-codex.jsonl). Falló al inicializar el runtime por permisos sobre el estado local, antes de respuesta.
- El mismo comando con escalación revisada automáticamente pudo iniciar el runtime, pero devolvió exit 1 porque el modelo configurado `gpt-6.1-sol` fue rechazado por el servicio para esta cuenta ChatGPT. [Salida del reintento](artifacts/native-codex-retry.jsonl). No se cambió el modelo ni se obtuvo orientación nativa.
- Claude: en orientation-empty, `claude -p '/sdd' --no-session-persistence --permission-mode dontAsk --tools 'Read,Glob,Grep,Skill' --allowedTools 'Read,Glob,Grep,Skill' --strict-mcp-config --output-format stream-json --verbose`, exit 1. [Salida](artifacts/native-claude.jsonl). El evento init incluye sdd en slash_commands/skills: discovery observado. También muestra dos entradas sdd al evaluar el fixture dentro de un repo que tiene su propio adaptador; no prueba dos definiciones de flujo. La respuesta es «Not logged in · Please run /login», sin llamada al modelo ni ejecución del flujo. No se hizo login ni se declara activación comprobada.
- Gemini: no disponible; discovery/activación sin comprobar.

Estos fallos quedan como ERR-004 (Codex, modelo/entorno de ejecución) y ERR-005 (Claude, autenticación faltante). Esperado en ambos: orientación con estado sin cambios. Observado: errores anteriores, sin respuesta funcional. No hay corrección comprobada ni defecto de skill demostrado. Pendiente PEND-SDD-002-001: completar AC-006 en entornos operativos de Codex, Claude y Gemini; si se usa UI, guardar secuencia/capturas reales con viewport. El cierre nativo histórico de MVR no se reaplica a esta versión. Estado y siguiente acción sólo en catálogo.

## 2026-10-08 — Evaluación funcional independiente

Leader `/root`: asignó escenarios aislados a `/root/sdd_eval_entry` y `/root/sdd_eval_execution`, distintos del autor de la skill; limitó permisos a fixtures/informes y prohibió publicación. Cada evaluador aplicó la entrada y solicitudes con herramientas reales. El Leader leyó sus salidas; no atribuye como personales sus ejecuciones.

[Evaluación de entrada](artifacts/eval-entry.md): ocho casos en un mismo subagente, por lectura explícita, con respuestas, fuentes y hashes por archivo. Orientación vacía/activa (esta última mediante adaptador Claude), consulta ajena, proyecto con skill externa, falta de harness y ambigüedad no cambiaron archivos. Capacidad nueva registró FAVORITES-001 como Propuesta y preparó borrador; sin aprobación preparó contrato existente sin tocar demo.py/check.py ni retirar «Sin aprobación». No se presenta como ocho sesiones nativas ni como Claude ejecutado.

[Evaluación de ejecución](artifacts/eval-execution.md): tres casos. Bug se reprodujo con `python -B check.py`, exit 1, AssertionError 'Hola mundo'; se registró ERR-001 del fixture y comprobó corrección con exit 0. Aprobada y continuidad implementaron el saludo dentro de su permiso simulado, cada una con exit 0. Las tres devuelven exactamente Hola. Sus catálogos conservan revisión pendiente, sin autocertificar Verificada. Se ejerció aceptación del saludo y routing/permiso por lectura explícita; sin UI.

[Manifest y snapshots finales](artifacts/evaluations/NOTICE.md) conservan entradas y resultados bajo artifacts, sin copiar el workflow once veces. [Huellas de las fuentes evaluadas](artifacts/evaluations/source-hashes.json). Los resultados finales no son condiciones iniciales ni permisos del template: para repetir se usa el preparador. Estas comprobaciones respaldan AC-001…AC-005 en los escenarios descritos; no convierten AC-006 en cumplido. Las rutas P-01/P-06/P-07/P-09 restantes se inspeccionaron, sin afirmar cobertura exhaustiva de formulaciones o ejecución completa de todos esos ciclos.

## ERR-006 — Evidencia enlazada a carpetas ignoradas

2026-10-08, origen Verifier `/root/sdd_review`, hallazgo REV-SDD-002-001, AC-005. Esperado: otra copia del repo conserva entradas y resultados funcionales. Observado: el informe de ejecución enlazaba `.harness-test-sdd-final`, ignorada por Git; una copia nueva perdía esos artefactos. Corrección del Leader `/root`: conservar once snapshots/manifest/huellas bajo `artifacts/evaluations`, ajustar enlaces del informe y añadir nota de preservación sin cambiar resultados. La [revisión](artifacts/review.md) conserva el hallazgo original. El Verifier comparó 90 archivos byte a byte contra fixtures ejercidos, sin diferencias, y confirmó referencias/huellas coincidentes; la confirmación definitiva se conserva en su dictamen actualizado. El autocontrol de enlaces locales devolvió exit 0, sin referencias rotas. Este arreglo no modifica la skill ni atribuye nuevas ejecuciones a los evaluadores.

## 2026-10-08 — Comprobación suplementaria de fuentes externas

Leader `/root` preparó con la misma función `project` un fixture adicional sin aprobación y una copia externa de la skill, con un archivo de prompts distinto junto a su instalación. Evaluador `/root/sdd_eval_entry` ejerció el pedido literal y escribió [su informe](artifacts/eval-external-execution.md), por lectura explícita en Codex. Leyó/aplicó P-02 desde `target/.harness/prompts.md`, no desde `installed/.harness/prompts.md`; sus hashes son distintos y se conservan [ambas fuentes](artifacts/evaluations/external-execution/target/.harness/prompts.md) y [el archivo vecino ajeno](artifacts/evaluations/external-execution/installed/.harness/prompts.md). Preparó sólo cuatro documentos de target, conservando falta de aprobación, código, instalación y manifest. No ejecutó check.py ni afirmó aceptación del saludo.

Esta comprobación cierra el límite del caso externo inicial que sólo orientaba: AC-004 tiene observación de lectura real de un bloque canónico del proyecto con skill instalada fuera de él. [Entrada](artifacts/evaluations/external-execution/case.json) y snapshots finales están preservados; el informe registra hashes antes/después. La canónica no cambió. No cierra AC-006 ni demuestra otras etapas con instalación externa.

## 2026-10-08 — Revisión independiente y entrega del tramo

Verifier `/root/sdd_review`, distinto del implementador, emitió [dictamen vigente](artifacts/review.md). Contrastó contrato/diff/archivos nuevos, canónica/adaptador/metadatos/preparador y documentación. Ejecutó personalmente dos tests técnicos (OK), validador local (exit 0), git diff --check (exit 0) y los tres check.py resultantes (exit 0). Leyó los informes de los evaluadores y logs nativos sin atribuirse reproducción/routing ni una activación exitosa. No hubo inspección visual de esta versión.

El revisor confirmó cierre de REV-SDD-002-001/ERR-006: 90 archivos de los once snapshots comparados byte a byte, referencias resolubles y huellas de fuentes coincidentes; además comparó doce archivos del suplemento externo, sin diferencias. La conclusión suplementaria actualiza el límite anterior de AC-004, con lectura real de P-02 desde target. Conservó en su informe el hallazgo y dictamen previos como históricos.

Dictamen favorable a AC-001…AC-005 en los escenarios ejercidos, sin hallazgos pendientes de implementación/preservación. AC-006 continúa parcial: no hay activación nativa exitosa en los tres entornos ni evidencia UI. El Leader `/root` leyó el dictamen y cerró T-001/T-002/T-003/T-005 por sus comprobaciones reales, mantuvo T-004 parcial y SDD-002 En verificación, con siguiente acción en catálogo. Este cierre del tramo no significa feature Verificada, publicación ni prueba nativa del workflow.

Entrega: [skill canónica](../../.agents/skills/sdd/SKILL.md), [adaptador Claude](../../.claude/skills/sdd/SKILL.md), [uso y comandos](../../README.md), [resultados conservados](artifacts/evaluations/NOTICE.md) y [revisión](artifacts/review.md). MVR conserva su integración e historia, sin modificaciones en este tramo. No se realizó commit, push, PR ni despliegue.

## ERR-007 — Referencias del prompt suplementario preservado

2026-10-08, origen autocontrol final `/root`, AC-005. El control de los 93 Markdown encontró dos enlaces locales rotos desde el snapshot `external-execution/target/.harness/prompts.md`: README.md y roles.md no se habían copiado. Al conservarlos, el control de 95 Markdown señaló que faltaba ../VERSION, también ausente en los fixtures originales. Esperado: fuentes preservadas con referencias consultables. Corrección: conservar README/roles originales y VERSION del harness, y añadir VERSION al preparador para nuevas evaluaciones. Una assertion de regresión comprueba ese archivo referenciado. Se conserva [preparador anterior](artifacts/evaluations/prepare_sdd_cases.before-version.py) para identificar los inputs históricos de los informes/huellas; los snapshots originales no se reinterpretan como otra ejecución. No cambia router, permisos ni resultados. Se solicita confirmación del revisor y se repiten tests del preparador/control de referencias pertinentes.

2026-10-08 — Comprobación posterior del Developer `/root`: dos tests OK (exit 0), control de 95 Markdown sin referencias locales rotas (exit 0) y git diff --check sin salida (exit 0). Verifier `/root/sdd_review` confirmó ERR-007 resuelto en [dictamen actualizado](artifacts/review.md): repitió personalmente dos tests, contrastó el cambio único VERSION en preparador/histórico, los archivos de soporte y hashes de router/adaptador. Su control de 106 Markdown incluyó archivos ocultos y excluyó las tres plantillas base cuyas referencias apuntan al destino de copia; sin roturas nuevas, exit 0. Estas comprobaciones cierran ERR-007 y confirman el resultado común vigente tras ese arreglo, sin alterar el pendiente nativo AC-006. El Leader actualizó catálogo conservando En verificación.

## 2026-10-08 — Validación progresiva acordada y actualización de Calles Posadas

Leader `/root`: registra el pedido real del usuario de actualizar el harness de Calles Posadas para Gemini en Antigravity, realizar validaciones durante el uso y dejar Claude pendiente por falta de suscripción sin frenar actualizaciones. Se conserva AC-006 y sus fallos previos; no se declara pass ni se requiere reintentar CLIs o contratar una suscripción para integrar la actualización. Antigravity IDE se documenta como entorno distinto de Gemini CLI. Su [documentación oficial](https://antigravity.google/docs/skills?app=antigravity-ide), leída el 2026-10-08, admite .agents/skills en el workspace y revisión de skills en Customizations. Esta consulta prueba el contrato de descubrimiento documentado, no la activación real en el equipo del usuario. Estado/siguiente acción en catálogo; la integración concreta se documenta en el repo destino.

## 2026-10-08 — Incorporación concreta en Calles Posadas

Developer/Leader /root aplicó la distribución y la entrada común al proyecto solicitado, con contrato local SDD-001, sin copiar acuerdos/artefactos de producto ni alterar FEAT-001…009. Dos pruebas técnicas del preparador pasaron; 128 archivos de producto conservaron hashes y las reglas de Next.js permanecieron íntegras. Las fuentes compartidas coinciden con este template. La evidencia y snapshots de esa aplicación viven en el propio proyecto.

Verifier /root/sdd_review revisó independientemente el resultado local y los cambios documentales de este template: [dictamen preservado](artifacts/review-calles.md). Favorable al tramo técnico; pruebas nativas sin ejercer. Se documentó el límite de los fixtures locales que copian reglas Next.js sin node_modules, sin atribuir implementación de casos a Gemini. El Leader conservó AC-006 parcial y actualizó siguiente acción al uso/prueba humana en Antigravity; Claude diferido por el acuerdo del usuario, sin bloquear actualizaciones. Esta incorporación cierra el pedido de actualización del destino; no cierra el pendiente nativo ni autoriza publicación.
