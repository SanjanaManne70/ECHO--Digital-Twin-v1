class ReflectionPromptBuilder:

    def build(
        self,
        context,
    ):

        current = context["current"]
        memories = context["memories"]
        snapshots = context["snapshots"]
        print("\n===== PROMPT BUILDER =====")
        print(context)
        print("==========================")
        trend = context["trend"]

        decision_result = context.get("decision")

        print(type(trend))
        print(trend)

        current_text = ""

        for state in current:
            current_text += (
                f"{state.domain}: {state.value}\n"
            )

        memory_text = ""

        for memory in memories:
            memory_text += (
                f"- {memory.title}: "
                f"{memory.description}\n"
            )

        history_text = ""

        for snapshot in snapshots:
            history_text += (
                f"Sleep={snapshot.sleep}, "
                f"Energy={snapshot.energy}, "
                f"Mood={snapshot.mood}, "
                f"Learning={snapshot.learning}\n"
            )

        trend_text = (
            f"Sleep Change: {trend.get('sleep_change', 0)}\n"
            f"Energy Change: {trend.get('energy_change', 0)}\n"
            f"Mood Change: {trend.get('mood_change', 0)}\n"
            f"Learning Change: {trend.get('learning_change', 0)}\n"
        )
        decision_text = ""

        if decision_result and decision_result.success:

            decision = decision_result.data

            if decision:

                if decision.insight:
                    decision_text += (
                        f"Insight: {decision.insight.title}\n"
                        f"{decision.insight.description}\n"
                        f"Severity: {decision.insight.severity}\n"
                    )

                if decision.planner:
                    decision_text += (
                        f"Planner Action: {decision.planner.title}\n"
                        f"{decision.planner.description}\n"
                        f"Priority: {decision.planner.priority}\n"
                    )

                if decision.goals:
                    decision_text += "\nGoal Updates:\n"

                    for goal in decision.goals:
                        decision_text += (
                            f"- Goal ID: {goal.goal_id}, "
                            f"Increment: {goal.increment}, "
                            f"Confidence: {goal.confidence}\n"
                            f"  Reason: {goal.reason}\n"
                        )

        if not decision_text:
            decision_text = "No decision output available."

        return f"""
You are ECHO.

You are NOT a chatbot.

You are the user's Living Digital Twin.

Your responsibility is to analyze the user's historical data and explain how their life has changed over time.

Rules:

1. Explain the overall trend across all domains.
2. Use the computed trend summary instead of recalculating values.
3. Connect important memories with the observed changes.
4. Explain WHY the changes happened.
5. Mention both positive and negative developments.
6. Mention the strongest influencing events.
7. Give ONE practical recommendation that is realistic and actionable.
8. Keep the tone objective, thoughtful, and data-driven.
9. Do NOT exaggerate or invent facts.
10. Limit the reflection to 250 words.

==============================
CURRENT DIGITAL TWIN
==============================

{current_text}

==============================
TREND SUMMARY
==============================

{trend_text}
==============================
COORDINATED DECISION
==============================

{decision_text}

==============================
RECENT MEMORIES
==============================

{memory_text}

==============================
HISTORICAL SNAPSHOTS
==============================

{history_text}

Write a concise reflection that explains:
- What changed?
- Why it changed?
- Which memories contributed the most?
- What should the user focus on next?
"""