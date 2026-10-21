from app.agents.planner_agent import PlannerAgent
from app.agents.planner_models import Goal


goal = Goal(
    title="Crack Google",
    description="I want to sleep better, exercise daily and prepare DSA for interviews.",
    duration_days=180,
)

planner = PlannerAgent()

strategy, actions = planner.plan(goal)

print("\n========== STRATEGY ==========")
print(strategy)

print("\n========== HABITS ==========")
for habit in strategy.habits:
    print(habit)

print("\n========== ACTIONS ==========")
for action in actions:
    print(action)