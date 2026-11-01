# -*- coding: utf-8 -*-
"""
Personal Agent Intermittent Fasting Autophagy Window Client
Zero-dependency hepatic glycogen depletion tracker, beta-hydroxybutyrate (BHB) kinetics
estimator, cellular autophagy activation scorer, and circadian eating window optimizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentIntermittentFastingAutophagy:
    """
    Quantifies metabolic transition phases of fasting, tracking liver glycogen depletion,
    ketone body synthesis, AMPK/mTOR reciprocal signaling, and cellular autophagy activation.
    """

    def calculate_autophagy_metabolic_phase(
        self,
        fasting_duration_hours: float,
        prior_meal_carb_grams: float = 60.0,
        exercise_met_hours: float = 1.0
    ) -> Dict[str, Any]:
        """
        Models metabolic phase transitions from postprandial to peak autophagy.
        Autophagy increases as liver glycogen drops below 20g and AMPK phosphorylates ULK1.
        """
        dur = max(0.0, min(168.0, float(fasting_duration_hours)))
        carbs = max(0.0, min(400.0, float(prior_meal_carb_grams)))
        ex_met = max(0.0, min(25.0, float(exercise_met_hours)))

        # Initial glycogen storage (typically 90-130g in adult liver)
        initial_glycogen_g = min(130.0, 85.0 + (carbs * 0.25))

        # Glycogen depletion kinetics (~5.2g/hour at rest + 12g per active MET-hour)
        depleted_glycogen_g = (dur * 5.2) + (ex_met * 12.0)
        remaining_glycogen_g = round(max(0.0, initial_glycogen_g - depleted_glycogen_g), 1)

        # Serum Beta-Hydroxybutyrate (BHB) concentration (mmol/L)
        if remaining_glycogen_g > 35.0:
            bhb_mmol_l = round(0.1 + (dur * 0.01), 2)
        else:
            hours_post_glycogen = dur - ((initial_glycogen_g - 35.0) / 5.2)
            bhb_mmol_l = round(min(5.5, 0.35 + (max(0.0, hours_post_glycogen) * 0.12)), 2)

        # Autophagy Activation Index (0 - 100%)
        if dur < 8.0:
            autophagy_pct = round((dur / 8.0) * 10.0, 1)
            phase = "Phase 1: Postprandial Digestion & Insulin Surge"
            desc = "Nutrient absorption dominant. mTOR active, cellular repair suppressed."
        elif dur < 14.0:
            autophagy_pct = round(10.0 + ((dur - 8.0) / 6.0) * 25.0, 1)
            phase = "Phase 2: Postabsorptive Hepatic Glycogenolysis"
            desc = "Blood glucose maintained by liver glycogen reserves. Insulin declines to basal."
        elif dur < 22.0:
            autophagy_pct = round(35.0 + ((dur - 14.0) / 8.0) * 35.0, 1)
            phase = "Phase 3: Gluconeogenic & Ketogenic Shift"
            desc = "AMPK active, mTOR downregulated. Adipose lipolysis accelerating. Autophagic proteolysis initiates in hepatic and endothelial tissue."
        elif dur < 36.0:
            autophagy_pct = round(70.0 + ((dur - 22.0) / 14.0) * 20.0, 1)
            phase = "Phase 4: Robust Macroautophagy & Mitophagy"
            desc = "Systemic cellular cleanup. Damaged mitochondria, misfolded protein aggregates, and intracellular pathogens degraded."
        else:
            autophagy_pct = round(min(100.0, 90.0 + ((dur - 36.0) / 24.0) * 10.0), 1)
            phase = "Phase 5: Peak Deep Autophagy & Stem Cell Renewal"
            desc = "Maximum autophagic turnover. Hematopoietic stem cell rejuvenation signaling."

        return {
            "fasting_hours_elapsed": dur,
            "estimated_hepatic_glycogen_remaining_g": remaining_glycogen_g,
            "estimated_serum_bhb_ketones_mmol_l": bhb_mmol_l,
            "autophagy_activation_index": f"{autophagy_pct}%",
            "current_metabolic_phase": phase,
            "biochemical_status": desc,
            "metabolic_fuel": "Fatty Acids & Ketones" if remaining_glycogen_g < 20.0 else "Glucose & Glycogen"
        }

    def optimize_eating_window(
        self,
        target_fast_hours: float = 16.0,
        bedtime_hour: float = 23.0,
        wake_hour: float = 7.0
    ) -> Dict[str, Any]:
        """
        Calculates optimal start and end times for the daily feeding window, enforcing
        early time-restricted feeding (eTRF) to preserve melatonin onset and sleep architecture.
        """
        fast_dur = max(12.0, min(24.0, float(target_fast_hours)))
        feed_dur = 24.0 - fast_dur
        bed = max(18.0, min(28.0, float(bedtime_hour))) % 24.0
        wake = max(4.0, min(12.0, float(wake_hour)))

        # Rule: Dinner must end at least 3.5 hours before bedtime to protect nocturnal core temperature drop
        window_end_hour = (bed - 3.5) % 24.0
        window_start_hour = (window_end_hour - feed_dur) % 24.0

        def format_time(h_float: float) -> str:
            hh = int(h_float) % 24
            mm = int((h_float - int(h_float)) * 60)
            return f"{hh:02d}:{mm:02d}"

        return {
            "fasting_protocol": f"{int(fast_dur)}:{int(feed_dur)} Time-Restricted Feeding",
            "target_fast_duration_hours": fast_dur,
            "feeding_window_duration_hours": feed_dur,
            "optimal_feeding_start_time": format_time(window_start_hour),
            "optimal_feeding_end_time (Kitchen Close)": format_time(window_end_hour),
            "pre_bedtime_digestive_buffer_hours": 3.5,
            "circadian_optimization_note": "Ending intake 3.5h before bed prevents insulin-mediated suppression of nocturnal growth hormone and melatonin."
        }
