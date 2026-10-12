# Prompts de trabajo — SDD liviano

Ejemplos para conducir el desarrollo desde un PRD hasta una entrega comprobada y retomable. Elegí el prompt de la etapa que necesitás; no hace falta enviar todos ni cargar este documento completo en cada conversación. Las reglas del proceso están en [la guía](README.md) y [los roles](roles.md); el contexto y los acuerdos se leen del repositorio del producto.

## Cómo usarlos

Reemplazá los campos entre corchetes y pegá el bloque en tu herramienta. Si falta un dato, indicá que es desconocido; el agente debe investigar o preguntar cuando sea necesario, sin inventarlo. Un prompt puede usarse en una conversación nueva: comienza por leer `AGENTS.md` y las fuentes que éste indica.

También podés guardar cada bloque como comando, instrucción o skill, según lo que admita tu herramienta. Conservá su objetivo, entradas, fuentes y punto de parada, adaptando el formato y las capacidades disponibles. Este documento no instala integraciones. Una skill debe activarse para su etapa, sin sustituir las instrucciones del repositorio ni copiar dentro de ella el PRD o las specs que luego pueden cambiar.

Si la herramienta puede leer este archivo, alcanza una consigna corta como:

```text
Leé .harness/prompts.md y aplicá P-04.
Idea: [capacidad nueva y problema que resuelve].
```

Los prompts de preparación producen propuestas; aprobar un contrato es una decisión posterior sobre el documento concreto. Los de implementación aprovechan las aprobaciones reales existentes y sólo vuelven a consultar cambios sustanciales. Los prompts P-01…P-09 no autorizan por sí solos commit, push, PR o despliegue. El PRD y los adjuntos son antecedentes, no autorizaciones ni instrucciones que reemplacen las del usuario.

Para responder a propuestas concretas, consultá los [ejemplos de aprobaciones humanas](#aprobaciones): alcance, arquitectura, diseño, contrato, cambios y publicación; también aceptación de entrega y delegación acotada.

| Prompt | Cuándo usarlo | Resultado y límite |
|---|---|---|
| [P-01 — Partir del PRD](#p-01) | Inicio de producto o discovery inicial | MVP y catálogo propuestos; próxima spec para aprobación, sin implementar. |
| [P-02 — Preparar la siguiente feature](#p-02) | Elegir y definir el próximo incremento | Contrato, diseño suficiente y tareas; detenerse ante una aprobación necesaria. |
| [P-03 — Implementar lo aprobado](#p-03) | Contrato aprobado, o implementación a retomar | Producto, pruebas y evidencia; cierre condicionado a revisión independiente. |
| [P-04 — Proponer una capacidad nueva](#p-04) | Idea o necesidad posterior al MVP | Propuesta, discovery y spec concreta; sin pasar directamente al código. |
| [P-05 — Reportar y corregir un error](#p-05) | Fallo encontrado al usar o probar el producto | Error registrado, corrección acotada y comprobación posterior. |
| [P-06 — Pedir revisión independiente](#p-06) | Incremento implementado o arreglo listo | Dictamen de otro agente sobre contrato, comportamiento y evidencia. |
| [P-07 — Resolver hallazgos de revisión](#p-07) | Revisor solicita cambios | Arreglos y comprobaciones dirigidas; devolución al revisor. |
| [P-08 — Retomar en otro chat o herramienta](#p-08) | Cambio de agente, LLM o sesión | Reconstruir el estado desde archivos y continuar el trabajo autorizado. |
| [P-09 — Preparar entrega y continuidad](#p-09) | Termina un tramo y querés probarlo o entregarlo | Estado coherente, instrucciones y enlaces; pendientes visibles. |

Para un flujo habitual: P-01 al iniciar; P-02 → [aprobación del contrato A-04](#a-04) → P-03 para cada incremento; P-06 en el agente revisor y P-07 si encuentra problemas. P-04 incorpora ideas nuevas y P-05 atiende fallos. P-08 y P-09 ayudan a continuar fuera de la conversación original.

<a id="p-01"></a>
## P-01 — Investigar desde el PRD

```text
Leé AGENTS.md y las fuentes que indica. Actuá como Leader y Analyst;
ejercé Architect cuando haya decisiones de diseño o tecnología necesarias.
PRD o antecedentes: [ruta o documento].
Restricciones adicionales del usuario: [restricciones, o ninguna adicional].

Investigá el problema, los usuarios, el resultado buscado y lo que ya existe
en el repositorio. Distinguí necesidades, hipótesis, sugerencias y acuerdos.
Preguntá sólo lo que pueda cambiar el próximo alcance o una decisión importante;
avanzá con lo que no dependa de esas respuestas.
Si hace falta investigación externa, usá las herramientas disponibles,
citá fuentes y separá lo encontrado de tus inferencias. No afirmes haber
investigado algo que no pudiste consultar.

Proponé el MVP mínimo útil, exclusiones y un catálogo de incrementos con
prioridades y dependencias. Registrá cada feature nueva como Propuesta.
Explicá las opciones relevantes de arquitectura, datos y diseño de interfaz;
registrá y consultá las decisiones importantes, sin elegirlas silenciosamente.
Detallá sólo la próxima feature: comportamiento, aceptación observable,
diseño suficiente, tareas y cómo comprobar cada criterio, incluidos errores
y evidencia visual cuando corresponda.

Dejá contexto y decisiones en sus archivos canónicos. Presentá el contrato
concreto para aprobación y señalá las decisiones abiertas. No implementes
código de producto ni prepares carpetas vacías para todo el roadmap.
```

<a id="p-02"></a>
## P-02 — Preparar la siguiente feature

```text
Leé AGENTS.md y sus fuentes. Actuá como Leader y Analyst.
Feature solicitada: [ID, o siguiente según el catálogo].

Revisá estado actual, prioridades, dependencias y trabajo en curso. Si hay
una feature incompleta o cambios de otro agente, identificá cómo afectan
la selección; no cambies silenciosamente su asignación ni los sobrescribas.
Si el contrato de la feature elegida ya está aprobado y sigue vigente,
informá que está lista para P-03; no repitas discovery ni pidas reaprobación.

Para una feature sin contrato aprobado, registrá primero Propuesta si es nueva
y hacé discovery del incremento. Acordá alcance y exclusiones, resolvé los
huecos que afecten aceptación y ejercé Architect sólo donde haya una decisión
necesaria. Incluí diseño de interfaz cuando corresponda, para poder revisarlo
antes del código. Consultá las decisiones importantes pendientes.

Prepará spec.md y tasks.md con IDs estables y escenarios por AC: condición
inicial, acción, resultado esperado, método y artefacto pertinente. Reutilizá
acuerdos existentes y detallá sólo lo necesario para implementar este tramo.
Actualizá el catálogo y presentá la spec concreta, sus exclusiones y preguntas
pendientes. Detenete antes de implementar si falta aprobación del contrato.
```

<a id="p-03"></a>
## P-03 — Implementar o continuar una feature aprobada

```text
Leé AGENTS.md y sus fuentes, incluido el contrato, tareas y evidencia de
[ID de feature]. Actuá como Leader y Developer para este incremento.

Confirmá la aprobación real del contrato vigente. Si falta, prepará la
propuesta y detenete antes del código; este pedido no aprueba una spec
desconocida. Si ya existe, usala sin solicitar otra vez el mismo permiso.
Inspeccioná cambios preexistentes y lo completado antes de continuar.

Trabajá de forma autónoma dentro del contrato aprobado, resolviendo las
decisiones menores de implementación sin pedir confirmación por cada paso.
Implementá las tareas pendientes dentro del alcance. Por cada resultado,
seguí el ciclo: planificá el cambio, implementá, ejercé el escenario de
aceptación, inspeccioná el resultado y corregí las diferencias observadas.
Repetí las comprobaciones afectadas hasta satisfacer los criterios; no
repitas rondas sin un fallo o riesgo concreto.

Comprobá cada resultado antes de cerrar la tarea y registrá actividad,
comando o pasos, datos, esperado, observado y límites en evidence.md.
Probá el comportamiento
solicitado con casos representativos y errores relevantes, además de las
comprobaciones técnicas necesarias. No rebajes criterios para hacer pasar
una prueba ni confundas compilación con aceptación.

Comprobá el flujo completo aprobado: que controles, mensajes, datos y
recursos cumplan su función. No presentes contenido de relleno, acciones
sin implementar ni simulaciones como capacidades terminadas. Conservá
los mocks o datos de prueba previstos, identificando sus límites.

Ejercé la interfaz real cuando aplique: conservá capturas y, para interacciones,
secuencia o grabación con observaciones/assertions en artifacts/, enlazadas
por AC y viewport. Si no podés comprobar algo, dejalo pendiente con motivo.
Registrá errores y arreglos sin borrar el historial. Consultá cambios
sustanciales de alcance antes de implementarlos.

Si el ciclo deja de avanzar, identificá la causa y registrá qué falta
para resolverla. No rebajes criterios ni amplíes el alcance para cerrar.

Solicitá otro agente como Verifier y entregale contrato, diff, pruebas,
artefactos y errores conocidos; podés usar P-06. Corregí sus hallazgos y pedí
confirmación de lo cambiado. Si no hay otro agente disponible, informá la
limitación y dejá la revisión pendiente. Sólo marcá Verificada cuando todos
los AC, tareas y revisión independiente del resultado vigente lo permitan.
Entregá enlaces a evidencia y capturas y el siguiente paso. No comiences
automáticamente otra feature ni publiques los cambios.
```

<a id="p-04"></a>
## P-04 — Agregar una capacidad nueva

```text
Leé AGENTS.md y sus fuentes. Actuá como Leader y Analyst.
Necesidad nueva: [qué problema quiero resolver y para quién].
Ejemplo de uso o resultado esperado: [ejemplo, si lo tengo].
Restricciones o preferencias: [detalle, si aplica].

Revisá si el catálogo o un contrato existente ya cubren esta necesidad.
Si es un fallo del comportamiento aprobado, tratá el reporte como P-05.
Si es una capacidad nueva o un cambio sustancial, registrá Propuesta con
ID estable, origen, dependencias y relación con el trabajo actual.
No implementes la idea directamente aunque parezca sencilla.

Hacé discovery, delimitá alcance/exclusiones y proponé alternativas sólo
donde sean útiles. Señalá impacto en arquitectura, datos, seguridad e interfaz;
registrá y consultá decisiones importantes. Prepará spec y tareas cuando
haya información suficiente, con aceptación observable y comprobaciones
funcionales/visuales pertinentes. Evitá expandir otras features en curso.

Presentá el contrato concreto para aprobación, indicando qué se agregaría,
qué queda fuera y qué falta decidir. Detenete antes del código de producto.
```

<a id="p-05"></a>
## P-05 — Reportar un error encontrado en mis pruebas

```text
Leé AGENTS.md y sus fuentes. Actuá como Leader y Developer.
Encontré este error: [síntoma].
Pasos para reproducir: [pasos, o todavía no los tengo].
Esperaba: [resultado esperado].
Ocurrió: [resultado observado].
Entorno, datos y captura: [detalle/ruta, si los tengo; sin datos sensibles].
Feature relacionada: [ID, o identificarla desde el repositorio].

Registrá el reporte con ID ERR estable en la evidencia de la feature:
origen usuario, reproducción conocida, esperado y observado. Distinguí
lo reportado de lo que pudiste reproducir personalmente; conservá ambos.
Si faltan datos indispensables, pedilos y continuá la investigación posible.

Contrastá el error con el contrato aprobado. Si lo incumple, reproducilo
de forma controlada y corregilo dentro de ese alcance; no hace falta nueva
feature ni discovery completo. Si la expectativa agrega una capacidad o
cambia sustancialmente el acuerdo, presentá Propuesta y pedí aprobación
del contrato modificado antes de implementar ese cambio.

Si corregís una feature Verificada, reabrí sólo esa entrada para implementación
o verificación y añadí tareas del arreglo sin borrar contrato, IDs ni historia.
Preservá datos y trabajo concurrente. Comprobá el caso original y regresiones
pertinentes; cuando aporte, dejá una prueba que detecte el fallo original.
Para interfaz, guardá evidencia real de la reproducción cuando sea posible
y del resultado corregido, con pasos, estado y viewport.

Registrá causa encontrada, corrección, comprobación posterior y pendientes.
Obtené revisión independiente de lo cambiado antes de recuperar Verificada;
no atribuyas al revisor conclusiones que no emitió. Entregá enlaces a error,
pruebas y capturas, sin publicar cambios ni inventar verificaciones históricas.
```

<a id="p-06"></a>
## P-06 — Revisar de forma independiente

Enviar este prompt a **otro agente que no haya implementado el cambio**, o al revisor independiente designado por el usuario. Cambiar la etiqueta de rol del implementador no lo convierte en un revisor independiente.

```text
Leé AGENTS.md y sus fuentes. Actuá como Verifier de [ID de feature].
Implementador: [agente responsable].
Cambios a revisar: [base y diff, o archivos/cambios delimitados].
Errores o hallazgos conocidos: [IDs y referencias, si existen].

Confirmá que no implementaste estos cambios. Si no tenés independencia,
informalo y no emitas un dictamen como revisión independiente.
Contrastá contrato aprobado, diff, tareas y evidencia. Evaluá si las pruebas
demuestran los resultados solicitados, también errores, límites y riesgos
relevantes. Buscá contraejemplos que puedan invalidar la aceptación: casos
límite, entradas inválidas, estados vacíos y secuencias relevantes según
el contrato y el riesgo. Contrastá las afirmaciones del implementador con
el comportamiento y la evidencia. Fundamentá cada hallazgo con un criterio
o impacto concreto; distinguí defectos de preferencias y mejoras fuera
del alcance.

Ejecutá comprobaciones pertinentes en un entorno controlado;
no modifiques datos reales ni repitas toda la suite sin razón.
Si la aceptación depende de datos externos, contrastá su respaldo y procedencia,
no sólo su presencia o el dominio del enlace, y dejá explícito lo no comprobado.

Para UI, comprobá interacciones relevantes e inspeccioná las capturas o
grabaciones reales: estado, datos, viewport y relación con el AC. Una imagen
existente o el resumen del implementador no demuestran por sí solos aceptación.
Revisá que otra persona pueda ejecutar producto y comprobaciones desde el repo.

Registrá en evidence.md fecha, responsable, alcance revisado, hallazgos con
IDs y ubicación, impacto, reproducción y comprobación esperada. Diferenciá
qué ejecutaste personalmente, qué artefactos inspeccionaste, qué salidas sólo
leíste y qué no pudiste comprobar. No arregles código de producto como parte
de esta revisión: devolvé los hallazgos al Developer.

Emití un dictamen del resultado vigente. No avales cierre con AC pendientes
ni fallos que invaliden aceptación, integridad o seguridad. En una segunda
ronda, confirmá los arreglos y lo que puedan afectar; la revisión anterior
no cubre automáticamente cambios posteriores. No concedas aprobaciones humanas
ni autorización de publicación.
```

<a id="p-07"></a>
## P-07 — Corregir hallazgos de revisión

```text
Leé AGENTS.md y el contrato, tareas, evidencia y revisión de [ID de feature].
Actuá como Leader y Developer. Hallazgos a resolver: [IDs o referencia].

Reproducí y corregí los hallazgos dentro del contrato aprobado. Si alguno
requiere un cambio sustancial del acuerdo, presentalo para decisión antes
de implementar esa parte; no reabras aprobación por una corrección equivalente.
Conservá los hallazgos y fallos originales y registrá cambios y comprobaciones
que resuelven cada uno. Añadí o ajustá pruebas sólo donde exista un hueco
concreto y repetí las comprobaciones afectadas por el arreglo.

Actualizá tareas después de verificar sus resultados. Renová la evidencia
visual de estados o interacciones que hayan cambiado, cuando corresponda.
Devolvé al Verifier independiente el diff del arreglo, comprobaciones y
artefactos para confirmar resolución y dictamen vigente. Tu autocontrol
no sustituye esa confirmación. Mantené pendientes y siguiente acción en el
catálogo hasta que el cierre sea válido; entregá enlaces, sin publicar cambios.
```

<a id="p-08"></a>
## P-08 — Retomar trabajo en otro chat o herramienta

```text
Leé AGENTS.md y sus fuentes. Actuá como Leader para retomar [ID de feature
o trabajo activo del catálogo]. No supongas acceso a la conversación anterior.

Reconstruí desde archivos el problema, acuerdos, contrato y aprobaciones
reales, estado actual, tareas, evidencia, errores y revisión vigente.
Inspeccioná cambios sin guardar y asignaciones concurrentes antes de tocar
archivos. Diferenciá lo comprobado de lo declarado y lo pendiente.

Resumí el punto de partida y continuá el siguiente paso autorizado de esa
feature, sin repetir trabajo válido ni pedir nuevamente permisos registrados.
Si falta una aprobación necesaria, identificá el contrato o decisión concreta
y detené sólo la parte que dependa de ella. Si falta evidencia, verificá
lo pertinente sin inventar resultados anteriores.

Actualizá los archivos existentes para dejar continuidad: catálogo para
estado/siguiente acción, tareas para trabajo y evidencia para historia.
No crees otro reporte de traspaso por rutina. Respetá límites de tu herramienta:
si no podés comprobar UI o convocar revisión independiente, dejalo visible
y pendiente. No cambies de feature ni publiques sin autorización.
```

<a id="p-09"></a>
## P-09 — Preparar entrega para probar y continuar

```text
Leé AGENTS.md y sus fuentes. Actuá como Leader para preparar la entrega
de [ID de feature o tramo delimitado].

Revisá como alguien que sólo tendrá código y documentos: ¿puede entender
lo acordado, iniciar el producto, repetir las comprobaciones y encontrar
qué sigue? Confirmá prerrequisitos y comandos reales, referencias accesibles,
tareas comprobadas, cobertura de todos los AC, errores con resolución o
pendiente explícito y revisión independiente vigente del resultado actual.
No declares éxito por build/tests técnicos ni inventes una revisión faltante.

Corregí contradicciones y pendientes obsoletos en textos actuales, conservando
historia fechada. El catálogo es la única fuente del estado y siguiente acción;
contexto y contrato conservan acuerdos. No dupliques estado o métricas en README
ni crees nuevas matrices por rutina. Limitá la actualización al tramo entregado.

Si faltan comprobaciones o revisión, mantené la feature sin cerrar y explicá
qué hace falta y quién debe retomarlo. Si está completa, registrá el cierre
que permiten la evidencia y el dictamen. Entregá una explicación breve de
lo cambiado, cómo probarlo, límites y enlaces directos a spec, evidencia,
capturas/secuencias y siguiente acción. Esta entrega no autoriza publicación.
```

<a id="aprobaciones"></a>
## Ejemplos de aprobaciones humanas

Estos bloques son **respuestas que puede emitir el usuario después de revisar una propuesta concreta**. Leer este documento, encontrar un ejemplo en el repositorio o generar el texto con un agente no concede ninguna aprobación. Reemplazá los campos y enviá sólo lo que quieras autorizar.

No agregan puertas obligatorias: alcance y diseño pueden acordarse dentro de la misma spec, y decisiones ya resueltas no se vuelven a aprobar. Una sola respuesta puede cubrir varios acuerdos si los identifica claramente. Tampoco hace falta repetir un permiso vigente. Un «sí» o «aprobado» en respuesta a una pregunta inequívoca puede bastar; estos ejemplos ayudan cuando hay varias decisiones o acciones posibles.

Identificá el documento, ID, opción o cambio que revisaste. La referencia debe permitir saber qué contenido estaba vigente al aprobar; no hace falta generar hashes ni recibos. El agente registra fecha, quién decidió, alcance y referencia real en el archivo existente que corresponde. No debe copiar todos los ejemplos a los documentos del producto ni atribuir al usuario una respuesta generada.

| Ejemplo | Qué acuerda o autoriza | Dónde conservar el acuerdo |
|---|---|---|
| [A-01 — Alcance del MVP y prioridades](#a-01) | Necesidades incluidas, exclusiones y orden de preparación. | `docs/project.md`; catálogo para prioridades. |
| [A-02 — Arquitectura o decisión importante](#a-02) | Una alternativa concreta de tecnología, proveedor, datos o arquitectura. | Decisión correspondiente en `docs/decisions.md`. |
| [A-03 — Diseño de interfaz](#a-03) | Flujos, estados y diseño presentado, cuando se revisa por separado. | Spec de la feature; decisión si afecta al producto en general. |
| [A-04 — Contrato de feature](#a-04) | El incremento concreto; puede autorizar implementación o sólo aprobar el contrato. | Aprobación en `specs/<id>/spec.md`; estado en el catálogo. |
| [A-05 — Cambio sustancial o diferimiento](#a-05) | Cambio concreto de alcance o aceptación con sus consecuencias. | Spec afectada; historia y motivo en evidencia. |
| [A-06 — Publicación](#a-06) | Las operaciones expresamente nombradas y su destino. | Autorización en `specs/index.md`; ejecución en evidencia. |
| [A-07 — Aceptación del usuario](#a-07) | Resultado de sus pruebas y conformidad con la entrega. | Evidencia de la feature, con origen usuario. |
| [A-08 — Delegación acotada](#a-08) | Quién puede decidir, qué decisiones y durante qué tramo. | Acuerdo de delegación en `docs/decisions.md`; referencias donde se ejerza. |

<a id="a-01"></a>
### A-01 — Acordar el MVP y el orden de trabajo

```text
Apruebo el alcance del MVP presentado en [documento y referencia revisada]:
incluye [resultados] y deja fuera [exclusiones].
El orden de preparación será [IDs o prioridades].
Registrá este acuerdo y prepará el contrato de [próxima feature] para revisión.
La implementación de cada feature queda sujeta a su contrato concreto aprobado.
```

Acordar el roadmap permite preparar incrementos; una lista de ideas no preaprueba sus contratos futuros.

<a id="a-02"></a>
### A-02 — Aprobar arquitectura o una decisión importante

```text
Apruebo [ID de decisión] presentada en [documento y referencia revisada],
opción [nombre]: [decisión concreta].
Acepto los impactos descritos sobre [operación, costes, datos u otros aplicables],
con estas condiciones: [condiciones, o ninguna adicional].
Registrá la decisión con referencia a esta respuesta y continuá la preparación
de las features que dependan de ella. La implementación sigue el contrato
aprobado de cada feature.
```

Usalo cuando se presentó una decisión importante nueva. Elegir tecnología no autoriza automáticamente contratar servicios, introducir credenciales, modificar datos reales ni ejecutar una migración; esas acciones deben estar comprendidas en una autorización concreta.

<a id="a-03"></a>
### A-03 — Aprobar diseño o experiencia de uso

```text
Apruebo el diseño de [feature/flujo] presentado en [spec, prototipo o capturas
y referencia revisada]: [opción elegida y estados incluidos].
Conservá estos acuerdos en la spec y prepará cualquier criterio pendiente
para completar su contrato. La implementación seguirá la aprobación de ese
contrato; esta respuesta acuerda el diseño presentado.
```

Este ejemplo sirve si querés revisar diseño antes de cerrar la spec. Si ya forma parte del contrato aprobado, no se exige otra aprobación de interfaz. Aprobar un mockup tampoco demuestra que la interfaz implementada funcione: eso se comprueba después, con evidencia real.

<a id="a-04"></a>
### A-04 — Aprobar una feature y autorizar su implementación

```text
Apruebo el contrato de [ID de feature] que acabamos de revisar en
specs/[ID]/spec.md [referencia del contenido revisado], con su alcance,
exclusiones, diseño, criterios de aceptación y tareas asociadas.
Autorizo implementarlo y comprobarlo según ese acuerdo. Continuá con P-03
para esta feature, conservando evidencia y revisión independiente antes del cierre.
```

Si querés aprobar el contrato pero implementar más adelante:

```text
Apruebo el contrato de [ID] en [spec y referencia revisada].
Dejalo Aprobado; todavía no empieces la implementación. La voy a solicitar
en otro momento o con otro agente.
```

Si la propuesta necesita ajustes y todavía no la aprobás:

```text
Antes de aprobar [ID], ajustá [cambios concretos] y presentame el contrato
actualizado. Todavía no implementes.
```

No se interpreta una solicitud de revisión como aprobación. Si autorizás directamente un cambio concreto ya definido, el agente conserva ese alcance y referencia; no debe pedir otra vez el mismo permiso por actualizar el documento.

<a id="a-05"></a>
### A-05 — Aprobar un cambio de alcance o diferir algo

```text
Apruebo el cambio presentado para [ID de feature] en [referencia]:
agregar/cambiar/retirar [detalle concreto], con el comportamiento esperado
[resultado] y los criterios/tareas afectados [IDs].
Acepto sus impactos y exclusiones descritos: [detalle].
Actualizá el contrato conservando la referencia al acuerdo anterior y
continuá la implementación y comprobación dentro de este alcance modificado.
```

Para retirar explícitamente un criterio del incremento y dejarlo para otro:

```text
Apruebo diferir [criterio/capacidad e ID] de [feature], según la propuesta
[referencia y motivo], y mantener [alcance restante].
Registrá el destino [feature futura o pendiente concreto] y el límite de
esta entrega. Verificá el contrato restante; el criterio diferido no se
registra como probado ni satisfecho.
```

No se usa para ocultar un fallo manteniendo la aceptación original. Una corrección que recupera el comportamiento ya aprobado sigue P-05/P-07 sin esta aprobación adicional. Si una condición deja decisiones esenciales abiertas, el agente resuelve y consulta esas partes antes de implementarlas; puede avanzar con lo ya autorizado que no dependa de ellas.

<a id="a-06"></a>
### A-06 — Autorizar publicación por operación y destino

Elegí las operaciones que querés autorizar. Pueden combinarse en una sola respuesta explícita; autorizar commit no incluye automáticamente push, PR, merge o despliegue. La autorización no equivale a ejecución: el agente registra después lo que efectivamente hizo y su resultado.

**Commit local:**

```text
Autorizo guardar en un commit local los cambios revisados de [feature/tramo]
en la rama [rama]. Incluí sólo ese alcance, preservando cambios ajenos.
```

**Commit y push:**

```text
Autorizo commit y push de los cambios revisados de [feature/tramo]
en la rama [rama], al remoto [remoto].
```

**Abrir una PR:**

```text
Autorizo abrir una PR [borrador o lista para revisión] desde [rama de origen
ya publicada] hacia [rama de destino], con los cambios revisados de [tramo].
```

**Merge de una PR concreta:**

```text
Autorizo hacer merge de [URL/ID de PR] hacia [rama de destino], con el método
[método acordado], si las comprobaciones y revisiones requeridas están vigentes
y corresponden a los cambios que revisamos [referencia].
```

**Despliegue:**

```text
Autorizo desplegar [versión/commit revisado] en [entorno y destino].
Alcance operativo autorizado: [acciones concretas y cambios de datos si aplican].
Condiciones acordadas: [condiciones verificables, o ninguna adicional].
Registrá las comprobaciones realizadas y el resultado del despliegue.
```

Antes de solicitar esta autorización, el agente debe tener el cambio concreto listo para revisar e identificar destino e impactos pertinentes. Si hay condiciones, comprueba que se cumplan; no las declara satisfechas por inferencia. Si sólo falta publicación, conserva el estado técnico real de la feature y ese pendiente por separado.

<a id="a-07"></a>
### A-07 — Dar conformidad después de probar el producto

```text
Probé [feature/versión] en [entorno] con estos casos: [pasos o IDs].
Observé [resultados] y acepto la entrega para [uso/alcance].
Pendientes o límites que conozco: [detalle, o ninguno observado].
Registrá esta devolución como prueba/conformidad del usuario, diferenciándola
de las comprobaciones del agente y del dictamen independiente.
```

Es una devolución útil y opcional, no una nueva puerta obligatoria. No transforma criterios sin comprobar en pass ni reemplaza la revisión independiente. Si tus pruebas detectan un fallo, usá P-05; aceptar otros resultados no borra ese reporte.

<a id="a-08"></a>
### A-08 — Delegar decisiones de forma acotada

```text
Delego en [agente/persona] las decisiones de [categoría concreta] durante
[feature, experimento o tramo], dentro de [límites y criterios].
Consultame [decisiones reservadas]. Registrá las decisiones como tomadas
por el delegado bajo esta autorización, con sus motivos y alcance.
```

La delegación no es una aprobación general de contratos futuros ni publicación. Si querés delegar también la aprobación de specs, indicá expresamente cuáles y con qué límites. Se registra al decisor real; nunca se atribuyen al usuario respuestas que tomó el agente delegado. Si quien desarrolla también decide dentro de una delegación, la revisión independiente sigue correspondiendo a otro agente.
