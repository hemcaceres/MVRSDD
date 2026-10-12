# Evaluación de ejecución — bug, approved y resume

Fecha: 2026-10-08, contexto de usuario America/Buenos_Aires. Responsable: Codex subagente `sdd_eval_execution`, distinto del implementador de la skill SDD-002. Método: **lectura explícita** de `SKILL.md` local y aplicación de los prompts del proyecto aislado. No se comprobó descubrimiento o activación nativa, Claude/Gemini, interfaz ni capturas. Esta evaluación no constituye por sí sola la revisión completa de SDD-002.

Entradas exactas y límites: [cases.json](evaluations/cases.json). Sólo se ejercieron los tres casos asignados. Se leyeron skill, AGENTS, `.harness/README.md`, roles, contexto, decisiones, catálogo, contrato, tareas y evidencia de cada fixture, y el bloque pertinente de prompts. Se inspeccionaron demo.py y check.py antes de implementar. Los contratos son permisos simulados limitados al saludo bajo la instrucción humana de probar la integración; no autorizan producto principal, publicación ni cambios en otros workspaces. No se modificó skill, contrato, check.py o tracking del template.

Entorno ejecutado: PowerShell, Python 3.13.5 (`python --version`, exit 0). Cada comando de aceptación se ejecutó con cwd en la carpeta del caso, usando `python -B check.py`, sin bytecode. El contrato común exige greeting() de demo.py sin argumentos, retornando exactamente la cadena `Hola`; check.py importa, llama y compara el resultado. Es aceptación del comportamiento único, no sólo comprobación de importación o build. No hay UI ni entradas múltiples que requieran casos adicionales.

## bug

Solicitud: **«El saludo devuelve Hola mundo; esperaba Hola, como acordamos. Corregilo.»**

Se seleccionó **P-05**: incumplimiento del contrato aprobado DEMO-001, sin capacidad nueva. Catálogo inicial Aprobada, T-001 y T-002 pendientes; no existían ejecuciones históricas acreditadas. demo.py contenía `return "Hola mundo"`.

Reproducción personal previa:

```text
python -B check.py
exit 1
AssertionError: 'Hola mundo'
```

Esperado del contrato: `Hola`. Observado antes: `Hola mundo`, coincidente con el reporte; registrado como ERR-001 sin borrar el fallo. Corrección: cambiar sólo el literal de demo.py a `Hola`. Se conservó la prueba que detectó el error. Comprobación posterior:

```text
python -B check.py
exit 0
AC-001: pass
```

T-001/T-003 se cerraron por la comprobación observada. T-002 sigue pendiente y catálogo En verificación. Respuesta del caso: «Corregí ERR-001 dentro de DEMO-001. El caso original fallaba con Hola mundo y ahora devuelve exactamente Hola; check.py pasó. Falta revisión independiente del saludo; no se publicó.»

Archivos inspeccionables: [demo.py](evaluations/bug/demo.py), [prueba conservada](evaluations/bug/check.py), [contrato](evaluations/bug/specs/DEMO-001/spec.md), [evidencia ERR-001](evaluations/bug/specs/DEMO-001/evidence.md), [tareas](evaluations/bug/specs/DEMO-001/tasks.md), [catálogo](evaluations/bug/specs/index.md).

## approved

Solicitud: **«Implementá el saludo que ya aprobamos.»**

Se seleccionó **P-03** tras contrastar catálogo y contrato DEMO-001. Aprobación simulada disponible y limitada al fixture; no se pidió reaprobar ni se creó otra feature. demo.py sólo contenía comentario de implementación pendiente; se conservó ese comentario y se agregó greeting() con retorno `Hola`.

```text
python -B check.py
exit 0
AC-001: pass
```

Esperado: cadena exacta `Hola`; observado: comparación de check.py satisfecha. T-001 comprobada, T-002 pendiente, catálogo En verificación. Respuesta del caso: «Implementé el saludo aprobado DEMO-001; greeting() devuelve Hola y check.py pasó. Falta revisión independiente del incremento; no se publicó.»

Archivos inspeccionables: [demo.py](evaluations/approved/demo.py), [prueba conservada](evaluations/approved/check.py), [contrato](evaluations/approved/specs/DEMO-001/spec.md), [evidencia](evaluations/approved/specs/DEMO-001/evidence.md), [tareas](evaluations/approved/specs/DEMO-001/tasks.md), [catálogo](evaluations/approved/specs/index.md).

## resume

Solicitud: **«Retomá donde quedamos.»**

Se seleccionó **P-08** y se reconstruyó desde archivos: DEMO-001 Aprobada, siguiente acción implementar saludo autorizado, T-001/T-002 pendientes, evidencia sin ejecuciones previas y demo.py con sólo marcador. No se asumió conversación anterior, otra asignación ni revisión favorable. Listado local confirmó ausencia de repositorio Git propio; no se utilizó el ancestro como proyecto. Se leyó P-03 para continuar ese paso autorizado, sin repetir discovery/aprobación, preservando comentario y check.py.

```text
python -B check.py
exit 0
AC-001: pass
```

Esperado: cadena exacta `Hola`; observado: comparación satisfecha. T-001 comprobada, T-002 pendiente y catálogo En verificación. Respuesta del caso: «Retomé DEMO-001 desde el catálogo: estaba aprobada y pendiente de implementación. Implementé el saludo y check.py pasó. Falta revisión independiente; no se empezó otra feature ni se publicó.»

Archivos inspeccionables: [demo.py](evaluations/resume/demo.py), [prueba conservada](evaluations/resume/check.py), [contrato](evaluations/resume/specs/DEMO-001/spec.md), [evidencia](evaluations/resume/specs/DEMO-001/evidence.md), [tareas](evaluations/resume/specs/DEMO-001/tasks.md), [catálogo](evaluations/resume/specs/index.md).

## Dictamen de los casos y límites

Los tres casos ejercieron correctamente la ruta y el comportamiento autorizado mediante lectura explícita. Se mantuvieron IDs y contrato, no se inventaron aprobaciones ni revisiones, se preservó el fallo reproducido del bug y se actualizó continuidad en los documentos existentes. No surgió un hallazgo bloqueante en estas tres rutas.

En los saludos soy Developer: sus comprobaciones son **autocontrol**, aunque sea evaluador independiente de la skill. La asignación prohíbe convocar más agentes; por eso no declaré ninguno de los saludos Verificada y quedó explícita revisión pendiente en cada catálogo/evidencia. No se comprobó el ciclo real de convocatoria/confirmación de otro revisor del saludo.

Durante lectura del caso bug hubo dos diagnósticos de búsqueda: `rg --files specs src` salió 1 porque `src` no existe; `Get-Content greeting.py` indicó archivo inexistente (la lectura compuesta salió 0). Se corrigió la inspección leyendo demo.py, nombre definido por el contrato; no fueron fallos de aceptación ni se ocultaron. Los demás bloques de lectura mostrados salieron 0. El fallo de aceptación original de bug salió 1 y los tres comandos posteriores de aceptación salieron 0.

Este informe conserva las salidas observadas y enlaza los archivos finales; no adjunta screenshots ficticias ni declara prueba visual. Las carpetas aisladas son temporales; el Leader debe conservar los resultados necesarios en artifacts antes de retirarlas para que estos enlaces sigan disponibles.


Nota de preservación del Leader: enlaces actualizados a snapshots conservados en evaluations/; condiciones iniciales se reconstruyen con el preparador. El contenido canónico evaluado queda identificado en evaluations/source-hashes.json.
