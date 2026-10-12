# SDD-002 — Entrada SDD portable

## Origen y necesidad

El usuario pidió revisar la integración SDD-001 del proyecto MVR y evaluar una entrada genérica. La respuesta propuso cuatro ajustes concretos: entrada neutral en AGENTS.md, contenido canónico compartido con adaptador mínimo para Claude, resolución del harness desde el proyecto y separación de pruebas comunes/nativas. El mensaje posterior «Hacelo» autoriza esos cambios en el template.

## Alcance y exclusiones

Incorporar `.agents/skills/sdd/SKILL.md` con el flujo reusable derivado de MVR, sin datos, contratos, aprobaciones ni artefactos de ese producto. Conservar `.harness/prompts.md` como fuente de los pasos. Agregar `agents/openai.yaml` para OpenAI y una entrada mínima `.claude/skills/sdd/SKILL.md` que lea el contenido canónico. Codex y Gemini comparten `.agents/skills`; otras herramientas pueden usar lectura explícita. Neutralizar AGENTS.md y documentar uso, requisitos y comprobaciones en README.md.

La skill resuelve las fuentes en la raíz del proyecto sobre el que trabaja, aunque su propio archivo esté instalado en otro lugar. No debe buscar el harness junto a su instalación ni elegir silenciosamente entre proyectos. Preparar casos aislados reutilizables y documentar las comprobaciones nativas por herramienta. No agregar runtime, MCP, instalador global, proveedor ni publicación. No modificar MVR ni borrar su integración/evidencia histórica: es el antecedente del piloto, no una dependencia de ejecución del template. No prometer compatibilidad nativa sin ejercerla.

## Comportamiento y aceptación

- AC-001: con un proyecto que contiene AGENTS.md, `.harness/prompts.md` y `specs/index.md`, un pedido pertinente carga una sola definición del flujo; el adaptador Claude remite a ella y los metadatos OpenAI no definen el proceso. Los prompts permanecen canónicos.
  - Comprobación: validar frontmatter/metadatos/referencias y comparar el diff; un evaluador independiente ejerce lectura por la entrada Claude. No equivale a descubrimiento nativo.
- AC-002: ante una invocación de sdd sin pedido, con catálogo vacío o activo, mostrar estado/próxima acción sin escrituras, implementación ni agentes. Una consulta ajena al harness no activa el recorrido.
  - Comprobación: evaluador independiente en fixtures, entrada/salida y hashes antes/después; caso ajeno explícito. Guardar resultados en artifacts/.
- AC-003: ante capacidad nueva, fallo contratado, implementación aprobada/sin aprobación y continuidad, distinguir alcance y permiso desde archivos y pedido; ejecutar sólo el trabajo autorizado y mantener revisión independiente/publicación separadas.
  - Comprobación: casos aislados con solicitudes naturales, observar cambios reales, conservar fallos y repetir `python check.py` cuando corresponda. Inspeccionar rutas restantes y declarar límites de cobertura.
- AC-004: con la skill instalada fuera del proyecto, leer el harness del proyecto indicado; sin harness o ante dos proyectos posibles sin objetivo definido, explicar el límite y solicitar la ubicación sin escribir ni instalar.
  - Comprobación: evaluador recibe skill externa y fixture con fuentes diferentes; observar qué fuentes usa y hashes. Ejercer ausencia y ambigüedad por separado.
- AC-005: una persona puede preparar casos desde una copia del repo con Python 3, sin rutas personales ni dependencias de MVR; repetir sobre una evaluación existente rechaza sobrescritura y conserva sus archivos. Casos y solicitudes son comunes; resultados se identifican por herramienta/método.
  - Comprobación: ejecutar preparador en directorio aislado, inspeccionar entradas, comprobar rechazo y preservación; documentar comandos realmente ejecutados.
- AC-006: las entradas nativas descubren/activan sdd en Codex, Gemini CLI y Claude Code, conservando orientación. La documentación distingue lectura explícita, validación estructural y funcionamiento nativo.
  - Comprobación: en cada herramienta disponible, comprobar descubrimiento y una activación real; conservar salida y método. Si se usa UI, capturas reales del selector y respuesta con viewport/estado en artifacts/. Lo que no se pueda ejecutar queda sin comprobar, sin reutilizar el cierre de MVR como prueba de esta versión.
  - Acuerdo de ejecución 2026-10-08: el usuario realizará las validaciones nativas a medida que use cada herramienta, empezando por Gemini en Antigravity IDE en Calles Posadas. Antigravity IDE y Gemini CLI son entornos diferentes. Claude queda diferido por falta de suscripción. Estas comprobaciones no bloquean incorporar/actualizar el harness; AC-006 no se registra como satisfecho por el diferimiento.

## Diseño y dependencias

Una skill de instrucciones con frontmatter estándar `name`/`description`; metadatos e invocaciones específicos quedan fuera del flujo común. Claude usa un adaptador de lectura, sin copia del router; Gemini/Codex comparten carpeta. Son ajustes dentro de la propuesta autorizada, sin decisión nueva de stack ni intervención de Architect. Las capacidades de acceso a archivos, interfaz y revisión dependen de la herramienta; se informa su ausencia conforme al harness.

## Aprobación del contrato

2026-10-08 — decisor: usuario de esta conversación. Referencia: mensaje «Hacelo», inmediatamente posterior a la revisión que enumeró los cuatro ajustes y recomendó llevar la integración a `dev-harness-template`. Autoriza implementar y comprobar ese cambio concreto. Esta spec conserva esa autorización; no se atribuye una aprobación separada del archivo, compatibilidad ya ejecutada ni permiso de commit, push, PR, despliegue o borrado de MVR.

Estado/siguiente acción en [catálogo](../index.md), detalle en [tareas](tasks.md), historia en [evidencia](evidence.md).

Acuerdo adicional 2026-10-08 — usuario: «Yo voy a hacer las validaciones a medida que vaya usando cada herramienta» y «Claude por ahora no se va a probar porque no tengo suscripcion». Autoriza actualizar el harness en Calles Posadas y diferir prueba nativa de Claude sin frenar actualizaciones SDD. No convierte pruebas pendientes en pass. La incorporación en ese proyecto se registra en su propio catálogo/contrato.
