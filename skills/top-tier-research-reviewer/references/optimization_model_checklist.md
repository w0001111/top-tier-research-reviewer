# Optimization Model Checklist

## Model Definition

- Sets and indices are defined.
- Parameters and decision variables are separated.
- Units are consistent.
- Objective terms have interpretable weights or prices.
- Constraints are physically, operationally, or algorithmically justified.
- Boundary conditions are specified.
- Feasibility conditions are explicit.

## General Optimization Checks

Check nonlinearities, binary-continuous products, big-M constants, convex relaxations, infeasible cases, optimality gap, and scalability.

## System Optimization Checks

Check resource capacity, temporal dynamics, routing or assignment, queueing/service limits, uncertainty, robustness, unmet demand penalty, fairness/service quality, safety/physical constraints, economic objective, and operational feasibility.

## EV Charging And Mobile Energy Systems

Check battery capacity, charging/discharging power limits, reactive capability, apparent power coupling, SoC dynamics, travel time, service time, queueing, depot recharge, station assignment, route continuity, vehicle availability, voltage constraints, and active/reactive service priority.
