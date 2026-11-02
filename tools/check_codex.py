"""Check required Codex metadata; never import project modules or execute skills."""

import re
import sys
import tomllib
from pathlib import Path

import yaml


root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
errors = []
agents = sorted((root / ".codex" / "agents").glob("*.toml"))
skills = sorted((root / ".agents" / "skills").glob("*/SKILL.md"))
if not agents:
    errors.append("missing .codex/agents/*.toml")
if not skills:
    errors.append("missing .agents/skills/*/SKILL.md")
names = set()
for path in agents:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        for key in ("name", "description", "developer_instructions"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                errors.append(f"{path}: missing or empty {key}")
        name = data.get("name")
        if isinstance(name, str):
            if name in names:
                errors.append(f"{path}: duplicate agent name {name}")
            names.add(name)
        for key in ("sandbox_mode", "approval_policy", "model_provider", "mcp_servers"):
            if key in data:
                errors.append(f"{path}: {key} does not override parent agent permissions/settings")
    except (OSError, ValueError) as error:
        errors.append(f"{path}: {error}")
for path in skills:
    try:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n(.+)", text, flags=re.DOTALL)
        if not match:
            errors.append(f"{path}: missing YAML frontmatter or skill body")
            continue
        data = yaml.safe_load(match.group(1))
        if not isinstance(data, dict):
            errors.append(f"{path}: frontmatter must be a mapping")
            continue
        for key in ("name", "description"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                errors.append(f"{path}: missing or empty {key}")
        name = data.get("name", "")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{path}: invalid skill name")
        elif name != path.parent.name or len(name) > 64:
            errors.append(f"{path}: skill name must match its folder and be at most 64 characters")
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{path}: {error}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Codex metadata valid: {len(agents)} agent(s), {len(skills)} skill(s).")
