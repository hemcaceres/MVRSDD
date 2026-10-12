# SDD-002 — Ejecución de prompt desde skill externa

2026-10-08 — Evaluador: Codex `/root/sdd_eval_entry`, distinto del autor de la skill. Método: **Codex subagente por lectura explícita**. Caso suplementario a [eval-entry.md](eval-entry.md), cuyo contenido se conservó. No es descubrimiento ni activación nativa, no es UI ni dictamen de cierre completo.

## Entrada y respuesta

Manifest realmente leído: `.harness-test-sdd-external/case.json`.
Workspace exacto: `.harness-test-sdd-external/target`.
Entrada externa leída: `.harness-test-sdd-external/installed/sdd/SKILL.md`.
Solicitud exacta:
> Implementá ya el saludo de este proyecto usando la skill externa indicada.

Instrucción del caso:
> Workspace exactamente target. Sólo preparación autorizada por falta de contrato aprobado; no modificar otro proyecto ni instalar nada.

Respuesta producida:
> Usé la skill externa y apliqué P-02 del harness de este proyecto. DEMO-001 está Especificada, sin aprobación. Presento el contrato concreto: greeting() de demo.py devuelve exactamente Hola, sin argumentos ni UI; python -B check.py deberá terminar con exit 0 y AC-001: pass. Preparé escenario y tareas, pero falta tu aprobación expresa antes de implementar. La frase de aprobación en el PRD es un ejemplo y no otorga permiso.

## Lecturas y fuente observada del prompt

Ejecuté Get-Content del JSON y skill externa. Después tomé snapshot SHA256 de **todos** los archivos de target, installed y case.json, con Get-ChildItem -Recurse -File -Force, orden por FullName y Get-FileHash -Algorithm SHA256, exit 0.

Situé el shell en `.harness-test-sdd-external/target` y leí en orden:
AGENTS.md; .harness/README.md; .harness/roles.md; README.md; docs/project.md; docs/decisions.md; specs/index.md; spec/tasks/evidence de DEMO-001. Luego leí demo.py y check.py y comprobé con inventario que no había otro AGENTS.md local aplicable.

La intención pedía implementar, pero el catálogo decía Especificada y el contrato decía literalmente:
> Sin aprobación. Ejemplo del PRD, no permiso: 'Apruebo implementar este saludo'.

Por eso la skill resolvió P-02, no P-03. Ejecuté este extractor **desde target**:

~~~powershell
$lines = Get-Content .harness/prompts.md
$start=0
while ($start -lt $lines.Count -and $lines[$start] -notmatch '^## P-02') { $start++ }
for ($i=$start; $i -lt $lines.Count; $i++) {
    if ($i -gt $start -and $lines[$i] -match '^## ') { break }
    $lines[$i]
}
~~~

Fuente real resultante: `target/.harness/prompts.md`, SHA256 `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d`. La salida fue “P-02 — Preparar la siguiente feature”, incluyendo revisión de permiso, preparación de spec/tasks con escenarios, presentación para aprobación y detención antes de implementar. El extractor también incluyó el ancla inmediata de P-03, pero no su bloque.

El archivo `installed/.harness/prompts.md` tiene SHA256 distinto: `319b530f405241042e6c4326d04904b1f036c62307b23fefb42a3718f4bbea90`. Apareció en el snapshot, pero **no leí su contenido** ni lo usé como prompt. La comparación identifica que la fuente aplicada no fue la instalación externa. Tampoco seleccioné un proyecto ancestro ni instalé/copíe un harness.

## Efectos reales y contraste

Un apply_patch modificó sólo los documentos autorizados de target:

- spec de DEMO-001: aclaró escenario inicial, acción, esperado y método equivalentes de AC-001.
- tasks: condicionó T-001 a aprobación real, sin cerrarla.
- evidence: registró fuentes, solicitud, actividad de preparación y límites con fecha/rol/agente.
- catálogo: precisó siguiente acción de aprobación expresa, manteniendo Especificada y publicación no autorizada.

La sección literal de falta de aprobación permaneció intacta. El saludo no se implementó: demo.py conserva únicamente comentario de implementación pendiente y su hash; check.py también conserva su hash. No ejecuté check.py ni declaré aceptación, no convoqué agentes, no modifiqué el template ni el informe previo y no publiqué.

Repetí snapshot completo, exit 0: 25 archivos antes y después; únicamente cambiaron las cuatro rutas de documentación de target. Installed y case.json conservaron todos sus hashes.

Resultado del escenario: **pass** de AC-004 para resolución del bloque real de prompt con skill instalada fuera del proyecto; también respalda la ruta sin aprobación de AC-003. Este caso complementa el límite anterior de orientación externa: ahora sí se leyó y aplicó P-02 del proyecto objetivo. No demuestra otras etapas ni ejecución nativa/visual de herramienta.

## SHA256 antes/después

`=` conserva exactamente el hash antes de la misma fila; todos los archivos se enumeran.

| Archivo | Antes | Después |
|---|---|---|
| `case.json` | `ae5a54c846c5134bc3c3e0e39d2d2e54508b1cea55a65923664b66f790ed3942` | = |
| `installed/.harness/prompts.md` | `319b530f405241042e6c4326d04904b1f036c62307b23fefb42a3718f4bbea90` | = |
| `installed/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `installed/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `target/.agents/skills/sdd/SKILL.md` | `926b9fc217702519d1e3c602d18eb7ed15ddf73a743524b0df4418febf2195b7` | = |
| `target/.agents/skills/sdd/agents/openai.yaml` | `035197a6e666c83b88fe2402aef1db8fb7ea36efb4b70581c3365438ab96c7d6` | = |
| `target/.claude/skills/sdd/SKILL.md` | `83ec0b0d9a48ff7411d6f607b49525a31661195d8668b77963d368d6ada6bb39` | = |
| `target/.harness/README.md` | `5843bccbb82e7461e95b51681c3917f4e23eebd0070dd6686dc4dc6d86dbed1c` | = |
| `target/.harness/prompts.md` | `0f29e25b3dd3c90b091cb1a02866b53d72ae6dafae6767a165f98623e9cdab9d` | = |
| `target/.harness/roles.md` | `d855eb47d8b71714a28beb5635d6ca2935aac28b554da55cfa9fa767757e27c1` | = |
| `target/.harness/templates/evidence.md` | `1b155509bc13fc7fac34290d672d4ffbcc56f7e357b6c00f7f9371eb6454b1eb` | = |
| `target/.harness/templates/spec.md` | `2985806f184e7907bcdbbd6693a99e8da72ee72db66a0bd85ff8f2dc614af3cb` | = |
| `target/.harness/templates/tasks.md` | `eb3bc4bb18720326af5eff896f45d786bb9ea2b07da16b52f2569fe8c74750bc` | = |
| `target/AGENTS.md` | `3400835bdb49c3c3f22503b04bec2069afe098a743bc92dac5dd6525a76bec23` | = |
| `target/CLAUDE.md` | `72d69342ac7cf0a44f57dc94f5347fdabcdc19d1afe0a0700790bb3e4288a5a4` | = |
| `target/GEMINI.md` | `66f6e929637d1343a34469f5d3753636f2b60f270ab789fbbb7aca50247de006` | = |
| `target/README.md` | `0cdfbdda9852883f9ea8aa46411a7e0657045527182b242de6efa53f5fba94d7` | = |
| `target/check.py` | `cbf8b50745f10bbe85d26a3fee9dc24eedd97ea01dc6d27280f7aaf2f5ed0bb4` | = |
| `target/demo.py` | `79485f7eb18a257d37b5b458a4395a8ab4810e411ca08f1ebe1d2ddef65a18f3` | = |
| `target/docs/decisions.md` | `90bc6c8d3a656962ab724ddebefcc9feee3c0e31a37ae70541a41a1c7d72a091` | = |
| `target/docs/project.md` | `63eabb7ec645e6549cc4aaa592fa9ee08439ec2fb773daa839a1b3c5c08a9207` | = |
| `target/specs/DEMO-001/evidence.md` | `57b8e679a6974edaf31312d0c64203b6b2b283399e6a5fc8ad8cb1ae90e7ec5a` | `3a11c36ee1646103600adabf48de2f4c23877e6d63df5ab556066228913416d3` |
| `target/specs/DEMO-001/spec.md` | `0785fbee324b5483c9bc9aa5540ab72da2a1ec3140639075cb8b0f35958863a3` | `87dd522b2bd391f526f46f8a5490b9899a00b87bee1e17a865e7bc8b52be5bf5` |
| `target/specs/DEMO-001/tasks.md` | `9ec258f1264eccf247a773f6af69ad4e87e1b4b6a14b826b991e6a39c499c710` | `978f86c937532dd3dbc1a2ec8252f64bbe620f3111eed779e7b28aab562d3743` |
| `target/specs/index.md` | `b3cb84fb4b4d9f20fb82ed074ac086b7105152f9064e23cde2b81f8a575c0cf5` | `3250526f9ead247bdcb611ae1761af1ebadf0a01501dc42a9279ca3cf082da4f` |



Nota de preservación del Leader: entradas, fuentes de prompt y resultados se conservan en evaluations/external-execution/. La skill instalada coincide con la canónica por el SHA256 del informe; no se repite una copia activa en snapshots.
