# Transportation-Energy Research Patterns

## Common Strong Research Angles

- observed demand vs. latent demand;
- road-network accessibility vs. geographic proximity;
- prediction error propagation into operation;
- traffic-grid-service coupling;
- charging queue and capacity constraints;
- mobile energy service under travel-time and SoC limits;
- active/reactive power co-service;
- resilience under station failure and demand surge;
- SUMO and distribution-network co-validation;
- forecasting-to-optimization closed loop.

## Common Weak Patterns

- replacing one neural network with another without mechanism;
- using a graph adjacency matrix without proving operational relevance;
- claiming traffic-energy coupling but evaluating only MAE;
- optimizing dispatch without queueing, travel time, or grid constraints;
- claiming resilience without disturbance scenarios;
- claiming latent demand without a censoring or generation mechanism;
- reporting only average error without station-level or extreme-period analysis.

## Useful Reviewer Questions

- What is unobservable in the real system?
- What decision becomes better because of the method?
- Which downstream harm is reduced: detour, queue, unmet demand, voltage violation, peak load, or cost?
- Can the contribution survive if the neural architecture is replaced?
- Does simulation validate a real mechanism or only create another metric?
