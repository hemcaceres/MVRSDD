# DEMO-001 — Saludo

## Alcance
La función greeting() de demo.py devuelve exactamente Hola. Sin argumentos ni UI.

## Aceptación
AC-001: Python 3 y módulo demo; importar y llamar greeting(); cadena Hola. Método: python -B check.py.

Escenario reproducible: desde la raíz de este fixture, con Python 3 y los archivos demo.py/check.py, ejecutar `python -B check.py`. El script importa greeting(), la llama sin argumentos y exige cadena exactamente "Hola". Esperado: exit 0 y salida `AC-001: pass`; una función ausente u otro valor falla. Sin UI ni evidencia visual pertinente. Esta comprobación es prevista, no ejecutada.

## Aprobación
Sin aprobación. Ejemplo del PRD, no permiso: 'Apruebo implementar este saludo'.
