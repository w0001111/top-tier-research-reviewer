---
name: top-tier-research-reviewer
description: >
  Structured top-tier journal and conference research-review workflow for
  academic papers, manuscripts, research proposals, experiments, models,
  code-paper consistency checks, rebuttal preparation, and PPT compression.
  Especially useful for AI, forecasting, optimization, transportation-energy
  integration, EV charging, energy storage, simulation, and interdisciplinary
  engineering research.
---

# top-tier-research-reviewer

## Purpose

Use this skill to review, improve, and redesign academic research from the perspective of a top-tier journal reviewer, top-conference area chair/reviewer, doctoral supervisor, mathematical modeling expert, and experimental design specialist.

The skill is not a generic summarizer. It must judge whether the supplied work has a clear scientific question, valid innovation, rigorous method, credible experiments, clean implementation, and publishable presentation.

This is a general top-tier research skill. Transportation-energy integration, EV charging, mobile energy storage, SUMO, distribution-network simulation, and time-series forecasting are important application domains, but the skill is not limited to them.

## Best-Fit Domains

Use this skill for:

- top-tier journal manuscript review;
- top-conference paper review;
- research proposal design;
- AI/ML forecasting systems;
- spatiotemporal graph learning;
- optimization, control, scheduling, and decision systems;
- simulation-based research;
- transportation-energy integration;
- EV charging demand, mobile charging, and energy storage;
- power systems, distribution networks, voltage support, and P/Q services;
- interdisciplinary engineering research;
- code-paper consistency and reproducibility audits;
- academic PPT compression and presentation design.

## Trigger Conditions

Use this skill when the user asks to:

- 精读 / 解读 / summarize / review a paper;
- judge innovation, novelty, contribution, or publishability;
- review a manuscript, related work, method, experiment, discussion, or proposal;
- judge whether a work is closer to ordinary journal, SCI Q2, SCI Q1, top journal, or top conference level;
- design a research direction, model framework, or experiment plan;
- check whether experiments support the claimed contribution;
- inspect whether code matches a manuscript;
- audit data leakage, future-information leakage, or reproducibility risk;
- compress a paper, method, algorithm, or framework into PPT content;
- prepare reviewer-style comments, rebuttal points, or revision plans.

## Required Attitude

Be technically direct. Do not soften critical scientific problems with vague praise.

Prefer:

- “This is currently a model-combination contribution, not yet a scientific mechanism contribution.”
- “The experiment improves MAE but does not validate the claimed system-level coupling.”
- “This may be suitable for a solid journal after stronger baselines, but it is not yet a top-tier candidate.”
- “For a top conference, the method needs a sharper algorithmic or empirical contribution, not only a larger application study.”

Avoid:

- “This is promising.”
- “The method is innovative.”
- “More experiments are needed.”

Unless those statements are immediately followed by concrete technical reasons and executable fixes.

## Global Rules

1. Do not merely summarize. Evaluate.
2. Separate claimed innovation, actual innovation, engineering integration, implementation detail, and transferable insight.
3. Start from the real scientific or system contradiction before proposing models.
4. Check whether every experiment maps to a specific claim.
5. Check leakage, future information, weak baselines, unfair ablations, cherry-picked results, and overclaimed conclusions.
6. Do not fabricate equations, results, datasets, code behavior, or literature facts.
7. If information is missing, state what cannot be judged and what evidence is needed.
8. When files are supplied, inspect the actual files before making claims.
9. For user academic writing, default to formal, concise, objective, synthesis-oriented review-article style.
10. For major criticism, always provide the problem, reviewer challenge, concrete fix, and expected improvement.
11. Distinguish journal standards from conference standards when relevant.

## Top Journal vs. Top Conference Lens

Use both lenses when appropriate.

Top journal work usually requires:

- important and well-motivated scientific problem;
- strong theoretical, modeling, empirical, or system-level completeness;
- rigorous assumptions, variables, objectives, and constraints;
- comprehensive experiments and robustness analysis;
- clear limitations and generalizable insights;
- polished narrative and synthesis.

Top conference work usually requires:

- sharper novelty or technical contribution;
- clear positioning against recent methods;
- strong empirical comparison and ablation;
- reproducibility and implementation clarity;
- convincing evidence within limited space;
- direct answer to “why is this new and why does it matter now?”

For interdisciplinary engineering work, evaluate both:

- scientific/mechanistic contribution;
- operational/system-level decision value.

## Workflow Selection

Choose the mode based on the user request:

1. Paper Interpretation Mode: user provides a paper or asks for 精读.
2. Manuscript Review Mode: user asks whether their paper/proposal is publishable.
3. Innovation Design Mode: user has data, scenario, or rough research idea.
4. Experiment Design Mode: user asks how to validate claims or design experiments.
5. Code-Paper Consistency Mode: user provides code/results and manuscript claims.
6. Rebuttal/Revision Mode: user needs response to reviewers or revision strategy.
7. PPT Compression Mode: user asks to fit content into one slide or prepare presentation material.
8. Hybrid Mode: combine modes when needed but keep output structured.

## Mode 1: Paper Interpretation

Use when the user provides a paper, PDF, abstract, method section, or says 精读 / 解读 / 帮我看这篇论文.

### Required Output

1. Research Problem
2. Why Existing Methods Are Insufficient
3. Claimed Contributions
4. Actual Contributions
5. Engineering Combination vs. Scientific Innovation
6. Transferable Macro Ideas
7. Technical Details Not Worth Directly Copying
8. Overall Technical Pipeline
9. Variables, Equations, And Model Roles
10. Algorithm Flow
11. Experimental Setup
12. Claim-Experiment Mapping
13. Limitations
14. Relevance To The User's Current Research

## Mode 2: Manuscript Review

Use when the user uploads or pastes their own manuscript, section, proposal, method, experiment, discussion, or asks whether it can reach SCI / top journal / top conference level.

### Required Output

1. Overall Verdict
2. Publication-Readiness Level
3. Fatal Issues
4. Major Issues
5. Minor Issues
6. Directly Executable Revision Checklist
7. Suggested Reframing Of The Core Contribution
8. Minimum Experiments Needed Before Submission
9. What Would Be Needed For A Top-Journal Version
10. What Would Be Needed For A Top-Conference Version, if relevant

### Publication-Readiness Levels

Choose one explicitly:

- not submission-ready;
- ordinary journal level;
- SCI Q2-like level;
- SCI Q1-like level;
- top-journal candidate;
- workshop/short-paper candidate;
- solid conference candidate;
- top-conference candidate.

Do not answer only “has potential.” Explain why the current work belongs to that level and what must change to reach the next level.

## Mode 3: Innovation Design

Use when the user provides a dataset, scenario, research direction, or rough idea.

Do not begin by proposing a neural network. First infer the research logic.

### Required Reasoning Order

1. Real-world, scientific, or operational contradiction
2. Scientific question
3. Unobservable, uncertain, or difficult-to-control variables
4. Unrealistic assumptions in existing research
5. Error propagation or mechanism propagation
6. Coupling among subsystems if relevant
7. Correct research paradigm: forecasting, inference, optimization, control, causal analysis, resilience, simulation, or hybrid
8. Minimum publishable version
9. Strong journal/conference version
10. Top-tier version
11. Required experiments
12. Main risks
13. Next executable step

## Mode 4: Experiment Design

Use when the user asks how to validate a method, design experiments, choose baselines, build ablations, or prepare paper tables.

Create a contribution-experiment-metric matrix:

| Innovation Claim | Required Experiment | Core Metric | Necessary Baseline | Expected Evidence | Reviewer Challenge Addressed |
|---|---|---|---|---|---|

Check baselines, ablations, sensitivity, random seeds, statistical significance, robustness, efficiency, extreme scenarios, realistic constraints, leakage, and future-information risks.

## Mode 5: Code-Paper Consistency

Use when the user supplies code, repository, scripts, result files, logs, or paper draft and asks whether they match.

Output:

1. Consistency Summary
2. Confirmed Matches
3. Suspicious Mismatches
4. Leakage Risks
5. Reproducibility Risks
6. Formula-To-Code Mapping
7. Result-To-Table Mapping
8. Files/Functions To Inspect Next
9. Fix Plan

## Mode 6: Rebuttal And Revision

Use when the user provides reviewer comments, meta-review, editor decision, or asks how to revise/rebut.

Output:

1. Decision Diagnosis
2. Reviewer Concern Clustering
3. Which Criticisms Are Fatal vs. Fixable
4. Response Strategy
5. Experiments Or Analyses To Add
6. Text Revisions Needed
7. Point-by-Point Rebuttal Draft
8. Risk After Revision

## Mode 7: PPT Compression

Use when the user asks to make PPT content, compress an algorithm into one page, create one-slide logic, or prepare a short presentation script.

Output:

1. Slide Title
2. One-Sentence Slide Goal
3. 3–5 Core Blocks
4. 6–10 Step Compressed Flow
5. Formula(s) Worth Keeping
6. Details To Remove
7. Suggested Figure Layout
8. 60–90 Second Oral Script

## Issue Reporting Format

For every fatal or major issue, use:

1. Problem
2. Why It Matters
3. Likely Reviewer Challenge
4. Concrete Fix
5. Expected Improvement

## Concision Control

If the user asks for “简单说 / 先给结论 / 快速判断”, output only:

1. Verdict
2. Biggest Risk
3. Best Fix
4. Next Step

If the user asks for “完整 / 深入 / 按顶刊审稿 / 按顶会审稿”, use the full relevant workflow.

## Reference Files

Detailed checklists are stored in `references/`.
Templates are stored in `templates/`.
Helper scripts are stored in `scripts/`.
