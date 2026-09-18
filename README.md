# Edhate AL SkillHub

Shared AI skills for Microsoft Dynamics 365 Business Central AL development. Developers can install skills into their projects, pull updates, and contribute improvements through pull requests.

## Skill catalog

| Skill | Use it for |
| --- | --- |
| [edhate-bc-api-integration](skills/edhate-bc-api-integration/SKILL.md) | Inbound APIs, outbound HTTP calls, authentication decisions, synchronization, and failure recovery |
| [edhate-bc-mcp-server](skills/edhate-bc-mcp-server/SKILL.md) | Build and test MCP servers exposing Business Central operations to AI assistants |

This collection currently contains two independently maintained skills. Its guidance adapts to the consuming project; company-specific standards must be documented before they are treated as requirements.

## Get started

Requires Python 3.10 or later for the installer and validation tools, plus Git to clone and update.

```bash
git clone https://github.com/Singhdhiru/Edhate-AL-SkillHub.git
cd Edhate-AL-SkillHub
python3 scripts/install.py --destination /path/to/your/assistant/skills --all --dry-run
python3 scripts/install.py --destination /path/to/your/assistant/skills --all
```

Replace the destination with the skill directory supported by your assistant. On Windows, use `python` if `python3` is unavailable. For a Codex personal installation, you can supply `--destination ~/.codex/skills`. Verify discovery and reload requirements for your assistant. No editor extension is required by this installer.

Install just one skill using `--skill edhate-bc-api-integration` instead of `--all`. The installer copies the entire skill package, including references. It refuses existing destination folders and symlinks and supports a preview with `--dry-run`.

After installation, try:

> Use the edhate-bc-api-integration skill to implement this integration using the supplied API contract and this project's AL conventions.

## Update an installation

1. Commit any contributions on a separate branch and update a clean checkout with `git pull --ff-only`.
2. Compare the repository skill with your installed copy.
3. Back up and move the old installed folder outside your assistant's skill directory.
4. Run the installer again and follow your assistant's reload process.

Updates are deliberate: pulling this repository does not refresh previously copied skills. Existing installations are never overwritten by the installer.

## Contribute and validate

See [CONTRIBUTING.md](CONTRIBUTING.md) and [templates/SKILL.md](templates/SKILL.md). Team members and external contributors can propose changes through pull requests.

```bash
python3 -m venv .venv
# macOS/Linux:
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

On Windows, use `.venv\Scripts\python.exe` in place of `.venv/bin/python`.

GitHub Actions runs structural validation and tool tests on pushes and pull requests. These checks do not prove AL correctness or assistant behavior. Include a realistic skill evaluation in contributions.

## Layout

```text
skills/          Installable skill packages and focused references
scripts/         Installer and structural validator
tests/           Installer and validator behavior tests
templates/       Starter for new skills
.github/         Automated checks and pull request template
```

## Maintenance and attribution

The maintainer should configure branch protection to require review and successful checks. The workflow file alone does not enforce merge restrictions.

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for the installed collection that informed this design. Edhate's original contributions do not yet have an open-source license; choose one before promising unrestricted reuse. Never submit customer secrets or private exports.
