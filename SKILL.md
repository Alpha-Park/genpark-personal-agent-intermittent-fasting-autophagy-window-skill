---
name: genpark-personal-agent-intermittent-fasting-autophagy-window-skill
version: "1.0.0"
description: "Zero-dependency hepatic glycogen depletion tracker, beta-hydroxybutyrate (BHB) kinetics estimator, cellular autophagy activation scorer, and circadian eating window optimizer."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Intermittent Fasting Autophagy Window Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to govern nutritional timing, model metabolic fasting states (glycogenolysis to ketogenesis), track cellular autophagy progression, and enforce circadian-safe kitchen closure.

## Agent In-Context Capabilities

- **Liver Glycogen Depletion Kinetics**: Accounts for baseline meal carbohydrate mass and exercise expenditure to model remaining glycogen.
- **Autophagy Activation Index**: Tracks AMPK/mTOR reciprocal signaling and estimates percent macroautophagy induction over time.
- **Circadian Eating Windows**: Computes precise feeding windows ensuring at least 3.5 hours of digestive clearance before bedtime.

## Tools Summary

1. `calculate_autophagy_metabolic_phase`: Computes current metabolic phase, glycogen grams remaining, serum BHB, and autophagy percentage.
2. `optimize_eating_window`: Calculates optimal feeding start and end times based on individual sleep/wake schedule.
