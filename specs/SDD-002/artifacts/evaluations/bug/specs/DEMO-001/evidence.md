# Evidencia
Datos sintéticos. No hay ejecuciones previas comprobadas.

## 2026-10-08 — ERR-001: saludo distinto del contrato

Rol Leader/Developer; responsable: Codex subagente `sdd_eval_execution`, mediante lectura explícita de la skill local. Pedido exacto: «El saludo devuelve Hola mundo; esperaba Hola, como acordamos. Corregilo.» Ruta P-05.

Origen: usuario del caso sintético. Reportado: `Hola mundo`; esperado: `Hola`. Reproducción personal desde la raíz del fixture: `python -B check.py`, exit 1, `AssertionError: 'Hola mundo'`. El contrato AC-001 exige exactamente `Hola`; no agrega alcance ni requiere discovery.

Causa: literal incorrecto en `demo.py`. Corrección: retornar `Hola`; se conserva `check.py`, que detectó el fallo original. Comprobación posterior se registra a continuación. No hubo UI, nuevas decisiones ni verificación histórica.

Autocontrol posterior de Developer: Python 3 disponible, módulo demo sin argumentos; `python -B check.py`, exit 0, salida `AC-001: pass`. La llamada devolvió exactamente `Hola`, cerrando reproducción y corrección T-003/ERR-001 y T-001. Esta prueba ejerce el único comportamiento contratado; no es una comprobación visual ni un build.

Rol Leader, mismo responsable: no se declara revisión independiente del saludo. La asignación de evaluación prohíbe convocar más agentes; T-002 requiere un revisor diferente y queda pendiente. El autocontrol no equivale a Verifier. No se publicó ni se modificó el contrato.
