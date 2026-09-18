"""Validate installable skills. Requires PyYAML; see requirements-dev.txt."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    errors = []
    folders = sorted((root / 'skills').iterdir())
    count = 0
    for folder in folders:
        if not folder.is_dir():
            continue
        count += 1
        path = folder / 'SKILL.md'
        try:
            content = path.read_text(encoding='utf-8')
            match = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.S)
            if not match:
                raise ValueError('missing YAML frontmatter or body')
            metadata = yaml.safe_load(match[1])
            if not isinstance(metadata, dict):
                raise ValueError('frontmatter must be a mapping')
            name = metadata.get('name', '')
            if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or name != folder.name:
                raise ValueError('name must match folder and use lowercase letters, digits and hyphens (maximum 64 characters)')
            description = metadata.get('description')
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                raise ValueError('description must contain 1–1024 characters')
            if not match[2].strip():
                raise ValueError('empty skill instructions')
            for item in folder.rglob('*'):
                if item.is_symlink():
                    raise ValueError(f'symlinks are not supported: {item.name}')
            for document in folder.rglob('*.md'):
                text = document.read_text(encoding='utf-8')
                text = re.sub(r'```.*?```', '', text, flags=re.S)
                for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                    url = urlsplit(link.strip('<>'))
                    if url.scheme or url.netloc or not url.path:
                        continue
                    target = (document.parent / unquote(url.path)).resolve()
                    if not target.is_relative_to(folder.resolve()) or not target.exists():
                        raise ValueError(f'broken or nonportable link in {document.name}: {link}')
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f'{folder.name}: {error}')
    if not count:
        errors.append('No skills found')
    return errors


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    print('\n'.join(errors) if errors else 'All skills passed structural and local-link validation.')
    sys.exit(bool(errors))
