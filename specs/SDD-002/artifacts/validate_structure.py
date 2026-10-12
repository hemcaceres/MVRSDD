"""Technical structure only; behavior and native activation require separate evidence.

Python 3 with PyYAML. Run from repository root; see evidence.md for preparation.
"""

import json
import re
from pathlib import Path

import yaml


root = Path(__file__).resolve().parents[3]
skill = root / ".agents/skills/sdd/SKILL.md"
adapter = root / ".claude/skills/sdd/SKILL.md"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == "sdd", path
    assert isinstance(metadata["description"], str) and metadata["description"], path
    return metadata, text


common, content = frontmatter(skill)
entry, wrapper = frontmatter(adapter)
assert common == entry, "Discovery metadata drift between canonical skill and adapter"
metadata = yaml.safe_load((skill.parent / "agents/openai.yaml").read_text(encoding="utf-8"))
assert 25 <= len(metadata["interface"]["short_description"]) <= 64
assert "$sdd" in metadata["interface"]["default_prompt"]
assert metadata.get("policy", {}).get("allow_implicit_invocation", True) is True
prompts = root / ".harness/prompts.md"
assert prompts.is_file()
referenced = set(re.findall(r"P-\d{2}", content))
available = set(re.findall(r"^## (P-\d{2})", prompts.read_text(encoding="utf-8"), re.MULTILINE))
assert referenced <= available, referenced - available
assert (root / ".agents/skills/sdd/SKILL.md").is_file()
print(json.dumps({
    "encoding": "UTF-8",
    "canonical_skill": skill.relative_to(root).as_posix(),
    "claude_adapter": adapter.relative_to(root).as_posix(),
    "discovery_metadata_consistent": True,
    "display_name": metadata["interface"]["display_name"],
    "implicit_invocation_allowed": True,
    "referenced_prompt_ids": sorted(referenced),
    "scope": "technical structure; not behavioral or native acceptance",
}, ensure_ascii=False, indent=2))
