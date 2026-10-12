# Resultados de evaluación SDD-002

Snapshots de entradas y resultados sintéticos del 2026-10-08, no contratos ni permisos del template o de un producto. Las aprobaciones simuladas sólo correspondían a los workspaces aislados durante la evaluación. No tratar estos snapshots como fuentes vigentes de instrucciones.

[cases.json](cases.json) conserva solicitudes, rutas y alcance original. [source-hashes.json](source-hashes.json) identifica las instrucciones/preparador evaluados, disponibles en el repo. Se conservan los archivos de producto resultantes por caso, sin repetir las copias del workflow en cada snapshot. Los hashes completos antes/después viven en [eval-entry.md](../eval-entry.md); [eval-execution.md](../eval-execution.md) conserva reproducciones y comandos de aceptación.

Estos son resultados finales, no condiciones iniciales para repetir. Reconstruir los casos con `.harness/tests/prepare_sdd_cases.py` desde una copia nueva o usando otro `--output`, y ejecutar sus solicitudes con el evaluador/herramienta correspondiente. El preparador necesita sólo Python 3. La skill canónica y prompts del repo suministran las fuentes de evaluación; los snapshots no constituyen proyectos nuevos con skills activas.

Los informes enlazan estos archivos conservados en lugar de depender de las carpetas ignoradas del autor. La actualización de enlaces no cambia las respuestas ni resultados observados de los evaluadores.

El caso suplementario [external-execution/case.json](external-execution/case.json) conserva la observación de lectura efectiva de P-02 desde el proyecto con skill instalada fuera de él; [informe](../eval-external-execution.md). Su target inicial equivale al fixture unapproved del preparador; se suministró la copia externa de la skill indicada y un archivo de prompts ajeno/distinto junto a su instalación. Se conservan ambos archivos de prompts y resultados de target, con hashes completos en el informe.

ERR-007 añadió README/roles y VERSION como contexto de las referencias del prompt preservado; no son nuevas ejecuciones del evaluador. El preparador vigente incluye VERSION en futuras copias. El hash histórico de `.harness/tests/prepare_sdd_cases.py` en source-hashes.json corresponde al [preparador anterior conservado](prepare_sdd_cases.before-version.py), no a esa corrección posterior. Este archivo histórico sólo identifica las entradas originales; usar el preparador vigente desde la raíz para repetir pruebas.
