# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Intermittent Fasting Autophagy Window Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentIntermittentFastingAutophagy

mcp = FastMCP("PersonalAgentIntermittentFastingAutophagy")
client = PersonalAgentIntermittentFastingAutophagy()

@mcp.tool()
def calculate_autophagy_metabolic_phase(
    fasting_duration_hours: float,
    prior_meal_carb_grams: float = 60.0,
    exercise_met_hours: float = 1.0
) -> str:
    """Calculates metabolic phase, hepatic glycogen depletion, ketones, and autophagy index during fasting."""
    import json
    return json.dumps(client.calculate_autophagy_metabolic_phase(
        fasting_duration_hours, prior_meal_carb_grams, exercise_met_hours
    ), indent=2)

@mcp.tool()
def optimize_eating_window(
    target_fast_hours: float = 16.0,
    bedtime_hour: float = 23.0,
    wake_hour: float = 7.0
) -> str:
    """Calculates optimal start and end times for daily feeding window aligned with circadian biology."""
    import json
    return json.dumps(client.optimize_eating_window(
        target_fast_hours, bedtime_hour, wake_hour
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
