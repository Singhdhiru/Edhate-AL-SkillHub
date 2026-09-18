"""Copy selected skills to an explicit destination without overwriting folders."""
import argparse
import shutil
from pathlib import Path


def install(source, destination, names, dry_run=False):
    source = source.resolve()
    destination = destination.expanduser().resolve()
    names = list(dict.fromkeys(names))
    if not names:
        raise ValueError('No skills selected')
    for name in names:
        folder = source / name
        if Path(name).name != name or not (folder / 'SKILL.md').is_file():
            raise ValueError(f'Unknown skill: {name}')
        if folder.is_symlink() or any(p.is_symlink() for p in folder.rglob('*')):
            raise ValueError(f'Symlinks are not supported: {name}')
        if destination == source or destination.is_relative_to(folder.resolve()):
            raise ValueError('Destination must be outside the source skill')
        target = destination / name
        if target.exists() or target.is_symlink():
            raise ValueError(f'Already exists: {target}. Back up and move the installed folder before reinstalling.')
    for name in names:
        print(f'{"Would install" if dry_run else "Installing"}: {name} -> {destination / name}')
        if not dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source / name, destination / name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, required=True, help='Your assistant’s skill directory')
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--skill', action='append', help='Skill folder name; repeat to select several')
    selection.add_argument('--all', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'skills'
    names = sorted(p.name for p in source.iterdir() if p.is_dir()) if args.all else args.skill
    try:
        install(source, args.destination, names, args.dry_run)
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')
