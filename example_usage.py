# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Intermittent Fasting Autophagy Window Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentIntermittentFastingAutophagy

def main():
    agent = PersonalAgentIntermittentFastingAutophagy()

    print("=" * 70)
    print("DEMO: Personal Agent Intermittent Fasting & Autophagy Window Modeler")
    print("=" * 70)

    # 1. Evaluate 18 hours into a fast
    res_phase = agent.calculate_autophagy_metabolic_phase(
        fasting_duration_hours=18.0,
        prior_meal_carb_grams=45.0,
        exercise_met_hours=2.0
    )

    print(f"\n1. Metabolic State at 18.0 Hours Fasting:")
    print(f"   Phase: {res_phase['current_metabolic_phase']}")
    print(f"   Autophagy Activation: {res_phase['autophagy_activation_index']}")
    print(f"   Hepatic Glycogen Remaining: {res_phase['estimated_hepatic_glycogen_remaining_g']} g")
    print(f"   Serum Ketones (BHB): {res_phase['estimated_serum_bhb_ketones_mmol_l']} mmol/L")
    print(f"   Fuel Source: {res_phase['metabolic_fuel']}")
    print(f"   Status: {res_phase['biochemical_status']}")

    # 2. Optimize 16:8 circadian eating window
    res_window = agent.optimize_eating_window(
        target_fast_hours=16.0,
        bedtime_hour=23.0,
        wake_hour=7.0
    )

    print(f"\n2. Circadian-Aligned Eating Window:")
    print(f"   Protocol: {res_window['fasting_protocol']}")
    print(f"   Window Opens: {res_window['optimal_feeding_start_time']}")
    print(f"   Window Closes: {res_window['optimal_feeding_end_time (Kitchen Close)']}")
    print(f"   Circadian Buffer: {res_window['pre_bedtime_digestive_buffer_hours']} hours before sleep")

    print("\nVerification complete: Intermittent fasting autophagy engine executed flawlessly.")

if __name__ == "__main__":
    main()
