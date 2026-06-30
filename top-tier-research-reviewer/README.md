# top-tier-research-reviewer

A reusable research-review skill for top-tier journal and conference work.

This skill helps an AI assistant review and improve academic papers, manuscripts, research proposals, experiments, optimization models, forecasting systems, code-paper consistency, rebuttal strategies, and academic PPTs.

It is designed for general top-tier research review, with particularly strong coverage for AI/ML, forecasting, optimization, simulation, interdisciplinary engineering, transportation-energy integration, EV charging, energy storage, SUMO/traffic simulation, and distribution-network studies.

## Why This Skill Exists

Many research-assistant prompts stop at summary or generic feedback. This skill is designed to enforce reviewer-grade judgment:

- separate claimed innovation from actual innovation;
- distinguish scientific contribution from engineering combination;
- connect every experiment to a claim;
- identify weak baselines, unfair ablations, leakage, and overclaiming;
- judge whether a study is closer to ordinary journal, SCI Q2, SCI Q1, top journal, workshop, solid conference, or top conference level;
- produce executable revision plans instead of vague advice.

## Repository Structure

```text
top-tier-research-reviewer/
├── README.md
├── LICENSE
├── skills/
│   └── top-tier-research-reviewer/
│       ├── SKILL.md
│       ├── references/
│       │   ├── review_criteria.md
│       │   ├── experiment_checklist.md
│       │   ├── leakage_checklist.md
│       │   ├── optimization_model_checklist.md
│       │   ├── ppt_compression_rules.md
│       │   ├── top_tier_review_patterns.md
│       │   └── transport_energy_patterns.md
│       ├── templates/
│       │   ├── paper_review_template.md
│       │   ├── manuscript_review_template.md
│       │   ├── innovation_design_template.md
│       │   ├── experiment_matrix_template.md
│       │   ├── code_paper_alignment_template.md
│       │   ├── rebuttal_template.md
│       │   └── ppt_compression_template.md
│       └── scripts/
│           ├── inspect_python_project.py
│           ├── extract_equations.py
│           └── summarize_results.py
└── docs/
    ├── examples.md
    └── design_notes.md
```

## Main Workflows

1. Paper interpretation
2. Manuscript review
3. Innovation design
4. Experiment design
5. Code-paper consistency audit
6. Rebuttal and revision planning
7. PPT compression

## Example Prompts

```text
Use top-tier-research-reviewer to review this manuscript as a top-journal reviewer. Give an explicit publication-readiness level and executable revision checklist.
```

```text
Use top-tier-research-reviewer to design experiments for this method. Build a contribution-experiment-metric matrix and identify missing baselines, ablations, leakage checks, and robustness tests.
```

```text
Use top-tier-research-reviewer to check whether this code implements the method described in my paper. Focus on feature consistency, future-information leakage, loss functions, ablations, and result-table consistency.
```

```text
Use top-tier-research-reviewer to compress this algorithm into one PPT slide with a 60-90 second oral script.
```

## Scope

The skill is intentionally general. It can be used for AI, engineering, forecasting, optimization, simulation, and interdisciplinary research. It includes transportation-energy patterns as a specialized reference because that domain frequently requires judging traffic-grid-service coupling, latent demand, queueing, routing, SUMO validation, distribution-network constraints, and active/reactive power service quality.

## License

MIT.
