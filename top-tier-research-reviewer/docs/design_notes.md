# Design Notes

## Design Philosophy

This skill follows a main-skill architecture:

- `SKILL.md` defines the role, trigger conditions, workflows, output standards, and completion discipline.
- `references/` stores detailed review checklists and domain-specific patterns.
- `templates/` stores reusable output structures.
- `scripts/` contains lightweight helper tools for inspecting local research projects.

The skill intentionally keeps one main entry point instead of splitting every workflow into a separate skill. This is useful when the user's research workflow requires moving across paper interpretation, novelty audit, experiment design, implementation audit, rebuttal, and presentation compression in one continuous session.

## Why Top-Tier Instead Of Transport-Energy Only

The initial scope focused on transportation-energy research. The scope was expanded because the same review logic applies across top-tier journal and conference research:

- clear problem framing;
- valid novelty;
- rigorous modeling;
- strong baselines;
- claim-experiment alignment;
- leakage-free implementation;
- concise presentation.

Transportation-energy remains a specialized reference domain rather than the title scope.

## What This Skill Should Not Do

- It should not merely summarize papers.
- It should not praise work without concrete evidence.
- It should not fabricate equations, results, datasets, code behavior, or literature claims.
- It should not propose a neural network before identifying the scientific or system contradiction.
- It should not confuse model complexity with contribution strength.
