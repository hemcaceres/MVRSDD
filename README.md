# Harness SDD liviano

Versión **1.0.0 — 2026-10-08**. Identificador en [VERSION](VERSION) e historial en [CHANGELOG.md](CHANGELOG.md).

Template en español para transformar un PRD en incrementos de producto, comprobarlos y dejar constancia suficiente para que otra persona continúe desde el repositorio. Conserva roles, discovery, catálogo de specs, tareas y evidencia. Cada feature nueva entra como propuesta; su cierre exige aceptación observable, evidencia visual cuando aplica y otro agente como revisor. No requiere instalar un runtime ni ejecutar transiciones del harness.

Esta es la distribución principal. El harness anterior y los experimentos se conservan en las ramas históricas; no se incluyen como instrucciones activas del template. No migra automáticamente proyectos que usen el harness anterior.

## Usarlo en un producto nuevo

1. Usá este repositorio como template, una copia de main o el paquete de una versión publicada en una carpeta nueva. No copies el `.git` de otro proyecto.
2. Guardá el PRD recibido en `docs/prd.md`, o enlazá su ubicación desde `docs/project.md`. Conservá su procedencia y distinguí sus hipótesis de decisiones aprobadas.
3. Abrí la carpeta con tu agente y dale la consigna de abajo. El agente completa contexto, decisiones y catálogo; sólo prepara los tres documentos de la próxima feature cuando haya alcance suficiente.
4. Acordá el MVP, resolvé las decisiones necesarias y aprobá la spec concreta antes de implementar. No hay una feature de producto preaprobada en esta plantilla; el catálogo distingue el trabajo del propio harness.

> Leé AGENTS.md y actuá como Leader. Partí del PRD y hacé discovery para proponer el MVP, sus exclusiones y un catálogo de incrementos de producto. Preguntá sólo lo que afecte al próximo alcance. Prepará la próxima spec y sus tareas, y presentá el contrato para aprobación antes de modificar código de producto. Dejá comandos reales de ejecución y prueba, evidencia de lo comprobado y continuidad desde los archivos.

Para features posteriores, registrá primero Propuesta y aplicá el mismo discovery y aprobación del contrato. Prepará cómo observar cada criterio antes del código. Antes de cerrar, convocá otro agente como Verifier y entregá enlaces a las comprobaciones y capturas reales. Los errores reportados y corregidos quedan en evidencia, con reproducción y comprobación posterior.

Los [prompts por etapa](.harness/prompts.md) ofrecen consignas copiables para discovery desde el PRD, próxima feature, implementación aprobada, ideas nuevas, errores, revisión y continuidad. Podés usarlos directamente o adaptarlos a comandos, instrucciones o skills de tu herramienta; consultalos según la etapa.

### Una entrada SDD para distintas herramientas

La [skill canónica sdd](.agents/skills/sdd/SKILL.md) elige la etapa desde tu pedido y el catálogo, y lee sólo el prompt pertinente del proyecto. No contiene datos de MVR ni un PRD predefinido. Los contratos y permisos pertenecen al proyecto actual, aunque la skill esté instalada en otro lugar. Sin harness o con varios proyectos posibles, pide la ubicación antes de escribir.

| Herramienta | Entrada | Uso |
|---|---|---|
| Codex | `.agents/skills/sdd/`, con metadatos `agents/openai.yaml` | Mencionar `$sdd` y agregar el pedido. |
| Gemini CLI | La misma `.agents/skills/sdd/` | Comprobar con `/skills list`; pedir que use `sdd` con tu necesidad. La activación puede requerir consentimiento de Gemini. |
| Gemini en Antigravity IDE | La misma `.agents/skills/sdd/` | Abrir la raíz del proyecto, iniciar una conversación y pedir que use `sdd`. Revisar skills en Customizations del panel del agente. |
| Claude Code | [Adaptador mínimo](.claude/skills/sdd/SKILL.md) en `.claude/skills/sdd/` | Invocar `/sdd` y agregar el pedido. El adaptador lee el flujo común. |
| Otra herramienta con lectura de archivos | [AGENTS.md](AGENTS.md) y entrada canónica | Pedir explícitamente que lea y aplique la skill. |

La estructura y ubicación siguen la documentación de [OpenAI](https://learn.chatgpt.com/docs/build-skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/) y [Claude Code](https://code.claude.com/docs/en/skills), sobre el estándar [Agent Skills](https://agentskills.io/specification). La compatibilidad declarada por esos productos no sustituye una prueba de esta integración; los resultados observados viven en [SDD-002](specs/SDD-002/evidence.md). La selección por intención depende del agente.

Antigravity IDE comparte la ubicación de workspace según [su documentación oficial](https://antigravity.google/docs/skills?app=antigravity-ide); su prueba es distinta de Gemini CLI. Las validaciones nativas se registrarán durante el uso de cada herramienta por el usuario. Claude queda diferido hasta disponer de suscripción; esos pendientes no frenan la incorporación o actualización del harness y no se presentan como comprobados.

Invocar sólo `sdd` muestra estado y próxima acción recomendada, sin escribir. Con un pedido, por ejemplo «Quiero agregar favoritos», prepara propuesta/contrato antes del código; «Retomá lo pendiente» reconstruye el próximo paso autorizado. Estos ejemplos no agregan capacidades ni permisos al producto. También podés usar: `Leé .agents/skills/sdd/SKILL.md y aplicala a [mi pedido]`. Esa lectura explícita permite usar el flujo, pero no demuestra descubrimiento nativo.

Abrí la raíz del proyecto en tu herramienta. Si no aparece la skill, refrescá sus skills o reiniciá la sesión según su documentación. Conservá `CLAUDE.md` y `GEMINI.md` como entradas a AGENTS.md; no copies el workflow en esos archivos. Al integrar en un producto existente, incorporá también `.agents/skills/sdd/` y, para Claude Code, `.claude/skills/sdd/` mediante diff. Este template no instala ni actualiza skills globales automáticamente.

### Repetir comprobaciones de la entrada

La skill sólo necesita un agente con acceso a los archivos del proyecto. Para preparar evaluaciones comunes se requiere Python 3, sin paquetes externos. Desde la raíz:

```text
python -B -X utf8 .harness/tests/prepare_sdd_cases.py
python -B -X utf8 .harness/tests/test_sdd_cases.py
```

El preparador genera `.harness-test-sdd/cases.json`, solicitudes y proyectos sintéticos; rechaza sobrescribir una evaluación existente. Para repetir, usá una copia nueva o elegí otro directorio con `--output .harness-test-sdd-otra`. El test comprueba aislamiento y preservación del preparador, no decisiones del agente. Los contratos simulados sólo autorizan sus fixtures.

La [comprobación estructural de SDD-002](specs/SDD-002/artifacts/validate_structure.py) requiere PyYAML sólo para validar YAML, no para usar la skill. Su [evidencia](specs/SDD-002/evidence.md) incluye instalación aislada, comandos y resultados reproducibles.

Abrí cada caso como workspace aislado con la herramienta evaluada y ejecutá su solicitud, conservando entrada, respuesta, cambios, comandos y resultados. Para el caso de skill externa, usá el archivo `external-skill/sdd/SKILL.md` indicado por cases.json y el proyecto del caso; para ausencia/ambigüedad, no elijas otro objetivo silenciosamente. Se recomienda un evaluador distinto del autor. Guardá informes en la evidencia de la feature con herramienta y método; los snapshots evaluados no son nuevas fuentes de instrucciones.

Comprobá aparte descubrimiento y activación nativos de cada herramienta disponible: `$sdd` en Codex, `/skills list` y activación en Gemini CLI, `/sdd` en Claude Code. Ante UI, guardá capturas reales del selector y respuesta con estado/viewport; una interacción requiere secuencia y observaciones. Si falta una herramienta o prueba, registrala sin comprobar. No uses los artefactos históricos de otro proyecto para acreditar esta versión.

## Usarlo en un producto existente

Revisá sus instrucciones y acuerdos primero. Integrá por diff `AGENTS.md`, `.harness/`, contexto y catálogo. Conservá el código, la documentación, las decisiones y las pruebas existentes; no sobrescribas `README.md`, `docs/` o `specs/` completos. Incorporá por feature la estructura útil sin invalidar aprobaciones ni borrar evidencia histórica. No hace falta reespecificar todo el producto para realizar un cambio acotado.

## Dónde leer y escribir

- [Contexto del producto](docs/project.md): problema, alcance acordado, restricciones, arquitectura, datos y comandos reales.
- [Decisiones](docs/decisions.md): alternativas, resolución y autoridad cuando corresponda.
- [Catálogo](specs/index.md): única fuente del estado actual, trabajo activo, bloqueo y siguiente acción.
- `specs/<id>/spec.md`: contrato aprobado; `tasks.md`: trabajo y comprobación por tarea; `evidence.md`: ejecuciones e historial.
- [Guía reusable](.harness/README.md), [roles](.harness/roles.md) y [plantillas](.harness/templates/spec.md).

## Entrega y continuación

Al desarrollar el producto, adaptá este README para que abra con su propósito y enlace instrucciones concretas para iniciarlo, probarlo y consultar el catálogo. Los comandos y prerrequisitos reales viven en `docs/project.md`; acá se enlazan, sin mantener una segunda copia que pueda quedar obsoleta.

Una persona nueva debe poder entender el alcance, encontrar el estado actual, ejecutar el producto y repetir las comprobaciones relevantes sin acceder a la conversación ni a carpetas de otra computadora. Guardá pruebas y salidas necesarias en el repositorio del producto con rutas relativas, o documentá cómo obtenerlas. Un reporte guardado demuestra una ejecución anterior; no reemplaza el código de la prueba.

En UI, las capturas/secuencias o grabaciones se guardan bajo `specs/<id>/artifacts/` y se enlazan desde evidence.md con criterio, escenario, viewport y resultado. Verifier inspecciona esa evidencia; un build o una imagen aislada no demuestra una interacción. Si falta aceptación o revisión independiente, la feature permanece sin cerrar.

El catálogo separa producto verificado de publicación autorizada. En la evidencia, cada ejecución o revisión indica fecha, autor, alcance, resultado y límites. Las notas de etapas anteriores se identifican como históricas. El contexto y el contrato no repiten tareas pendientes ni estados de implementación.

## Alcance y límites

La comparación local y el piloto en un producto respaldan esta estructura y mostraron mejoras en evidencia y revisión después de ajustar las instrucciones. Son experiencias acotadas: no demuestran ahorro de tokens ni garantizan que cualquier agente cumpla el proceso. Los tests verdes deben contrastarse con el comportamiento y, si aplica, con las fuentes de datos. Lo no comprobado queda visible y no se declara verificado.

No incluye validador genérico, budgets, digests, recibos de aprobaciones ni instalador. Las comprobaciones son las del producto y se amplían ante un riesgo o hueco concreto. Commit, push, PR y despliegue requieren autorización correspondiente.
