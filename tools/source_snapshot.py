"""Resolve the explicitly pinned Korean snapshot without a stale-client fallback."""
import hashlib
import json
from pathlib import Path


def resolve_source_directory(requested: str | None, project_root: Path) -> str:
    """Require an explicit source or the repository's versioned snapshot manifest."""
    if requested is not None:
        source = Path(requested)
        if not source.is_dir():
            raise FileNotFoundError(f'Korean source directory does not exist: {source}')
        return str(source)
    config_path = project_root / 'references/source-snapshot.json'
    with config_path.open(encoding='utf-8') as stream:
        config = json.load(stream)
    required = ('version', 'source_dir', 'sha256_manifest', 'manifest_sha256')
    if not isinstance(config, dict) or any(not isinstance(config.get(key), str) or not config[key] for key in required):
        raise ValueError(f'Source snapshot configuration requires nonempty string fields {required}: {config_path}')
    source = (project_root / config['source_dir']).resolve()
    manifest = (project_root / config['sha256_manifest']).resolve()
    if not source.is_relative_to(project_root) or not manifest.is_relative_to(project_root):
        raise ValueError(f'Pinned source paths must stay within the project: {config_path}')
    if not source.is_dir() or not manifest.is_file():
        raise FileNotFoundError(
            f'Pinned Korean snapshot {config["version"]} is unavailable: source={source}, '
            f'manifest={manifest}. Restore the matching snapshot or pass --source-dir explicitly; '
            'the installed Steam export is not used as a fallback.'
        )
    actual = hashlib.sha256(manifest.read_bytes()).hexdigest()
    if actual != config['manifest_sha256']:
        raise ValueError(f'Source manifest hash mismatch: {manifest}; expected={config["manifest_sha256"]}, actual={actual}')
    return str(source)
