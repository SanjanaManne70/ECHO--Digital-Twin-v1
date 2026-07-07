import json

from app.models import current_state


class DailyChapterPrompt:

    def build(
        self,
        memories,
        insights,
        goals,
        current_state,
    ):

        memories_json = json.dumps(
            memories,
            indent=2,
            default=str,
        )

        insights_json = json.dumps(
            insights,
            indent=2,
            default=str,
        )

        goals_json = json.dumps(
            goals,
            indent=2,
            default=str,
        )

        state_json = json.dumps(
            current_state,
            indent=2,
            default=str,
        )

        return f"""
You are ECHO.

You are the user's Living Digital Twin.

Your job is NOT to repeat today's memories.

Instead, understand everything that happened today and write ONE meaningful chapter describing the day.

Today's Memories:

{memories_json}

Today's Insights:

{insights_json}

Current Goals:

{goals_json}

Current Digital Twin State:

{state_json}

Instructions

- Read all memories carefully.
- Understand the overall day.
- Do NOT list memories.
- Write as if you are narrating today's chapter.
- Be encouraging but realistic.
- Never exaggerate.
- Keep the summary under 120 words.
- Growth points should be short.
- Highlight only the most important achievement.
- Tomorrow's suggestion should be practical.

Return ONLY JSON.

{{
    "title":"🔥 Breakthrough Day",

    "mood":"😊",

    "summary":"Today you demonstrated remarkable persistence while working toward your goals. Your learning remained consistent and your confidence continued to improve.",

    "growth":[
        "Learning improved",
        "Confidence increased",
        "Consistency strengthened"
    ],

    "highlight":"Solved a difficult Dynamic Programming problem after multiple attempts.",

    "tomorrow":"Continue practicing while getting enough rest."
}}

IMPORTANT

- Return ONLY valid JSON.
- No markdown.
- No explanation.
- No ```json blocks.
"""