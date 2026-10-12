# DEMO-001 — Saludo

## Alcance
La función greeting() de demo.py devuelve exactamente Hola. Sin argumentos ni UI.

## Aceptación
AC-001: Python 3 y módulo demo; importar y llamar greeting(); cadena Hola. Método: python -B check.py.

Escenario de AC-001: desde la raíz de este fixture y con Python 3, ejecutar `python -B check.py`; el script importa greeting(), la llama sin argumentos y compara exactamente con "Hola". Esperado: exit 0 y salida `AC-001: pass`. La cadena `Hola mundo`, ausencia de función u otro valor falla. No hay UI ni artefacto visual pertinente. El archivo check.py ya existe; no se ejecutó aceptación antes de aprobación.

## Aprobación
Sin aprobación. Ejemplo del PRD, no permiso: 'Apruebo implementar este saludo'.
