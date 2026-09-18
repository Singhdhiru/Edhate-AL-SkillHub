# Edhate AL SkillHub

A shared collection of AI skills for Microsoft Dynamics 365 Business Central AL development, maintained by the Edhate team.

Skills provide reusable instructions for an AI coding assistant. Each skill is an independent folder containing a `SKILL.md` file and, where useful, supporting references, scripts, or templates.

## Available skills

| Skill | Purpose |
| --- | --- |
| [edhate-bc-api-integration](skills/edhate-bc-api-integration/SKILL.md) | Guide inbound and outbound Business Central API integration work. |

The initial integration skill provides general guidance. Add approved Edhate engineering standards through reviewed contributions; no customer-specific conventions are assumed.

## Repository layout

```text
skills/                         Reusable, installable skills
  edhate-bc-api-integration/
    SKILL.md
templates/                     Starting points for new contributions
.github/                        Pull request template
CONTRIBUTING.md                 Contribution and review process
```

## Get the collection

Clone the shared repository:

```bash
git clone https://github.com/Singhdhiru/Edhate-AL-SkillHub.git
cd Edhate-AL-SkillHub
```

Download approved updates with `git pull --ff-only` when your working tree is clean. Commit your contributions on a separate branch before updating.

## Install and use

Cloning this repository alone does not install its skills. Copy the individual skill folders from `skills/` into the skill directory supported by your AI coding assistant. Consult that assistant's documentation for discovery and reload requirements.

For Codex, an example personal installation is to copy `skills/edhate-bc-api-integration` into `~/.codex/skills/`. Check for an existing folder before copying so local changes are preserved. After pulling repository updates, refresh your installed copy too.

Example request after installation:

> Use $edhate-bc-api-integration to implement this Business Central integration using the project's conventions and the supplied API documentation.

Supply the project requirements and API contract. Keep credentials outside prompts and skill files.

## Contribute

Team members can improve an existing skill or add a new folder under `skills/`. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [skill template](templates/SKILL.md).

## Publishing and ownership

Repository: https://github.com/Singhdhiru/Edhate-AL-SkillHub

This collection is intended for public sharing. Maintainers should invite contributors and configure protection for `main` to require pull request review.

Add a CODEOWNERS file once the actual maintainer usernames or team are known. Choose a license before inviting external reuse; this starter does not grant an open-source license.
