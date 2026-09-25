"""Load exact localized keyword names from the target resource directory."""

import json
from pathlib import Path


def keyword_directory(target: Path, workspace: Path) -> Path:
    """Use the workspace root for its descendants, otherwise the target directory."""
    resolved = target.resolve()
    root = workspace.resolve()
    if resolved.is_relative_to(root):
        return root
    return resolved.parent if resolved.is_file() else resolved


def load_keyword_names(directory: Path) -> frozenset[str]:
    """Validate dictionary resources and collect names without normalization."""
    if not directory.is_dir():
        raise NotADirectoryError(f"Keyword resource directory does not exist: {directory}")
    paths = sorted(set(directory.glob("BattleKeywords*.json")) | set(directory.glob("Bufs*.json")))
    names: set[str] = set()
    for path in paths:
        data: object = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict) or not isinstance(data.get("dataList"), list):
            raise ValueError(f"Keyword resource requires a dataList array: {path}")
        for position, entry in enumerate(data["dataList"]):
            if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
                raise ValueError(f"Keyword resource requires a string name: {path}, dataList[{position}]")
            names.add(entry["name"])
    return frozenset(names)
