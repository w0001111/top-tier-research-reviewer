# Leakage Checklist

## Time-Series Leakage

- Are train, validation, and test splits chronological?
- Are future labels used in feature construction?
- Are rolling features computed using only past values?
- Are missing values filled using future observations?
- Are normalization statistics fitted only on training data?
- Is validation data repeatedly used to tune the final model without reporting?

## Feature Leakage

Check whether features include future or unavailable information: future demand/labels, future system state, future price, future weather observation instead of forecast, future traffic state, realized outcomes, post-event state, or labels embedded in aggregate features.

## Online Adaptation Leakage

- Does online learning update using true labels before prediction time?
- Is adaptation evaluated with realistic label delay?
- Are hyperparameters selected from the test period?

## Spatial / Graph Leakage

- Are test nodes included in training normalization in a way that violates the target setting?
- Are graph edges computed using information unavailable in deployment?
- Does transductive evaluation match the claimed deployment scenario?

## Result Leakage

- Were test results used to choose architecture?
- Are failed runs omitted without reporting selection rules?
- Are seeds cherry-picked?
- Are post-hoc experiments presented as pre-designed validation?
