# Contributing to Edhate AL SkillHub

## Contribution workflow

1. Pull the latest `main` with a clean working tree.
2. Create a branch, for example `git switch -c feat/api-integration-guidance`.
3. Update an existing skill or add one folder under `skills/` using `templates/SKILL.md`.
4. Review the instructions and try a realistic request in a disposable project or branch.
5. Commit your changes, push your branch, and open a pull request against `main`.

Contributors without write access can use a fork when repository policy allows it.

## Skill format

- Use a descriptive lowercase folder name with hyphens, such as `edhate-bc-api-integration`.
- Include `SKILL.md` with YAML frontmatter containing `name` and `description`.
- Match `name` to the folder name and keep it under 64 characters.
- Explain the capability and when the assistant should use it in `description`.
- Keep instructions focused on decisions that improve the work.
- Add `references/`, `scripts/`, or `assets/` only when needed, and link supporting files from the skill.
- Use portable relative links. Do not depend on a contributor's local filesystem paths.
- Keep project-specific object ranges, prefixes, endpoints, and customer rules in the project unless they are approved shared standards.
- Never include credentials, access tokens, private customer payloads, or production exports.
- Clearly distinguish proposed conventions from approved company standards.

## Review and validation

Check that the frontmatter is valid, linked resources exist, and scaffold placeholders have been replaced. Try at least one representative request and explain the observed result in the pull request. For changed executable helpers, run them with safe test inputs and document results.

When the Codex skill-creator validator is available, run its `scripts/quick_validate.py` against the changed skill folder. Structural validation does not replace a behavior check.

Review whether the skill preserves the user's task scope, avoids invented API details, adapts to the target Business Central version, and respects deployment authorization. Live deployment or customer data changes are not part of routine skill testing.

A maintainer should review changes before merging. Repository administrators must configure GitHub branch protection separately to enforce this process.

## Automated checks

Install `requirements-dev.txt` in a virtual environment, then run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. CI runs the same checks. The validator checks skill naming, required YAML fields, nonempty instructions, portable local Markdown links, and unsupported symlinks. It does not validate remote URLs, compile AL, or prove that an assistant follows the skill correctly.

Add the skill to the README catalog. Keep substantial guidance in linked references and document new executable dependencies. Preserve source attribution and applicable licenses when importing third-party material. Git history tracks contributors; personal profiles and per-skill changelogs are optional.

You may improve another contributor's skill through a reviewed pull request. An advance proposal is useful for large changes but is not required for routine fixes. Do not copy upstream mandatory questionnaires or approval stages unless the Edhate workflow actually requires them.
