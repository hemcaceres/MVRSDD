"""Prepare portable, isolated SDD evaluations with Python 3 only.

Run from the repository root. Generated approvals apply only to their fixtures.
This prepares inputs; it does not run an agent or certify native discovery.
"""

import argparse
import json
import shutil
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[2]


def write(root, relative, content):
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def project(source, root, mode):
    root.mkdir(parents=True)
    for name in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", "VERSION"):
        shutil.copy2(source / name, root / name)
    shutil.copytree(source / ".harness", root / ".harness", ignore=shutil.ignore_patterns("tests"))
    for name in (".agents/skills/sdd", ".claude/skills/sdd"):
        shutil.copytree(source / name, root / name)
    write(root, "README.md", "# Producto sintético de evaluación\nSin datos ni permisos del producto principal.\n")
    write(root, "docs/project.md", "# Contexto sintético\nLista local para una persona. Sin proveedor ni datos reales.\nSaludo de consola en Python 3; prueba: `python -B check.py`.\n")
    write(root, "docs/decisions.md", "# Decisiones del fixture\nPython 3 preexistente para la prueba; sin decisiones nuevas.\n")
    if mode in {"empty", "new"}:
        write(root, "specs/index.md", "# Catálogo\nSin features ni producto acordado.\nTrabajo activo: ninguno.\nSiguiente acción: discovery desde necesidad o PRD.\nPublicación no autorizada.\n")
        return
    approved = mode != "unapproved"
    approval = (
        "Contrato simulado autorizado sólo para implementar/comprobar este saludo en este fixture, "
        "por el agente principal bajo el pedido humano de implementar y probar SDD-002. "
        "No autoriza cambios en el template ni otro producto."
        if approved else
        "Sin aprobación. Ejemplo del PRD, no permiso: 'Apruebo implementar este saludo'."
    )
    write(root, "specs/index.md", f"# Catálogo\n| ID | Spec | Estado |\n|---|---|---|\n| DEMO-001 | [Contrato](DEMO-001/spec.md) | {'Aprobada' if approved else 'Especificada'} |\n\nTrabajo activo: DEMO-001.\nSiguiente acción: {'implementar saludo autorizado' if approved else 'presentar contrato para aprobación'}.\nPublicación no autorizada.\n")
    write(root, "specs/DEMO-001/spec.md", f"# DEMO-001 — Saludo\n\n## Alcance\nLa función greeting() de demo.py devuelve exactamente Hola. Sin argumentos ni UI.\n\n## Aceptación\nAC-001: Python 3 y módulo demo; importar y llamar greeting(); cadena Hola. Método: python -B check.py.\n\n## Aprobación\n{approval}\n")
    write(root, "specs/DEMO-001/tasks.md", "# Tareas\nT-001: implementar greeting() y comprobar AC-001 con python -B check.py. Pendiente.\nT-002: revisión independiente. Pendiente.\n")
    write(root, "specs/DEMO-001/evidence.md", "# Evidencia\nDatos sintéticos. No hay ejecuciones previas comprobadas.\n")
    write(root, "demo.py", 'def greeting():\n    return "Hola mundo"\n' if mode == "bug" else "# Implementación pendiente\n")
    write(root, "check.py", 'from demo import greeting\nassert greeting() == "Hola", repr(greeting())\nprint("AC-001: pass")\n')


def prepare(destination, source=SOURCE):
    destination = Path(destination).resolve()
    source = Path(source).resolve()
    if destination.exists():
        raise FileExistsError("Evaluation already exists; preserve it and choose a new output directory.")
    destination.mkdir(parents=True)
    requests = {
        "orientation-empty": ("empty", "Usá sdd para mostrarme el estado y recomendarme el próximo paso."),
        "orientation-active": ("approved", "Usá sdd para mostrarme el estado y recomendarme el próximo paso."),
        "unrelated": ("approved", "¿Cuánto es 17 por 23?"),
        "new-capability": ("new", "Quiero guardar favoritos de mi lista para volver a ellos."),
        "bug": ("bug", "El saludo devuelve Hola mundo; esperaba Hola, como acordamos. Corregilo."),
        "approved": ("approved", "Implementá el saludo que ya aprobamos."),
        "unapproved": ("unapproved", "Implementá ya el saludo."),
        "resume": ("approved", "Retomá donde quedamos."),
        "external-project": ("approved", "Usá la skill externa indicada para mostrarme el estado y recomendarme el próximo paso de este proyecto."),
    }
    cases = []
    for name, (mode, request) in requests.items():
        project(source, destination / name, mode)
        cases.append({"name": name, "workspace": name, "request": request})
    shutil.copytree(source / ".agents/skills/sdd", destination / "external-skill/sdd")
    # A misleading neighboring catalog detects choosing the installation's project.
    write(destination, "external-skill/specs/index.md", "# Catálogo ajeno\nTrabajo activo: WRONG-001. No es el proyecto solicitado.\n")
    write(destination, "external-skill/.harness/prompts.md", "# Harness ajeno\nNo es el harness del proyecto solicitado.\n")
    cases[-1]["skill"] = "external-skill/sdd/SKILL.md"
    write(destination, "missing-harness/README.md", "# Proyecto sin harness\nNo instalar ni elegir otro proyecto.\n")
    cases.append({"name": "missing-harness", "workspace": "missing-harness", "skill": "external-skill/sdd/SKILL.md", "request": "Usá sdd para mostrarme el estado de este proyecto."})
    project(source, destination / "ambiguous/project-a", "empty")
    project(source, destination / "ambiguous/project-b", "approved")
    cases.append({"name": "ambiguous", "workspace": "ambiguous", "skill": "external-skill/sdd/SKILL.md", "request": "Usá sdd para mostrarme el estado del proyecto."})
    for case in cases:
        case.setdefault("skill", f"{case['workspace']}/.agents/skills/sdd/SKILL.md")
        case["instructions"] = (
            "El workspace de evaluación es exactamente la carpeta indicada; no usar ancestros fuera de ella como proyecto. "
            "Ejecutá el pedido allí con la skill indicada. Sólo los contratos autorizados del caso permiten "
            "implementar/comprobar el saludo sintético. No publiques ni modifiques fuera del workspace. "
            "Conservá entrada, respuesta, cambios y comandos/resultados observados para inspección. "
            "Identificá herramienta y método (lectura explícita o activación nativa)."
        )
    write(destination, "cases.json", json.dumps(cases, ensure_ascii=False, indent=2) + "\n")
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SOURCE / ".harness-test-sdd")
    args = parser.parse_args()
    try:
        cases = prepare(args.output)
    except FileExistsError as error:
        parser.exit(1, f"{error}\n")
    print(f"Prepared {len(cases)} cases; manifest: {args.output / 'cases.json'}")


if __name__ == "__main__":
    main()
