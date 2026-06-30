# Experiment Checklist

## Contribution-Experiment-Metric Matrix

| Innovation Claim | Required Experiment | Core Metric | Necessary Baseline | Expected Evidence | Reviewer Challenge Addressed |
|---|---|---|---|---|---|

## Baseline Checklist

- naive baseline;
- historical average or persistence baseline;
- statistical model;
- classical ML model;
- deep learning baseline;
- graph/spatiotemporal baseline if relevant;
- strong recent or representative SOTA;
- rule-based operational baseline if relevant;
- optimization baseline if relevant;
- oracle or upper-bound benchmark if appropriate.

## Ablation Checklist

Each ablation should disable one claimed contribution.

## Robustness Checklist

Test noisy inputs, missing data, distribution shift, demand surge, component failure, parameter variation, prediction error levels, capacity or constraint changes, extreme events, and out-of-domain scenarios where applicable.

## Statistical Reliability

Use multiple random seeds, mean and standard deviation, confidence intervals when suitable, paired comparison for forecasting, significance testing where suitable, and transparent selection of reported runs.

## Efficiency

Report training time, inference time, optimization runtime, scalability, and memory use where relevant.
