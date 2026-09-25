"""Identify localization text without altering engine identifiers or source notes."""

from pathlib import Path
import re

IDENTITY_FIELDS = frozenset({'id', 'key', 'index', 'level', 'model'})


def metadata_reason(filepath: str, field: str, source: str) -> str:
    name = Path(filepath).name.removeprefix('KR_')
    if 'notinclude' in name:
        return 'Unreleased placeholder not included in release.'
    if field in IDENTITY_FIELDS:
        return 'Engine identity; must retain the source value.'
    if name.startswith('BattleSpeechBubbleDlg') and field == 'desc':
        return 'Trigger annotation; the player-facing speech is stored in dlg.'
    if source.lstrip().startswith(('//', 'SE //')):
        return 'Explicit source comment or sound cue.'
    if name.startswith('Items') and field == 'desc' and re.search(r'name\s*만\s*번역', source):
        return 'Source explicitly instructs translators to translate name only.'
    return ''
