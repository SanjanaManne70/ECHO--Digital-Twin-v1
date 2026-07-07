import json

class PromptBuilder:

    def build_memory_prompt(
        self,
        title: str,
        description: str,
    ) -> str:

        return f"""
You are ECHO's Memory Analysis Engine.

ECHO is an AI-powered Living Digital Twin.

Your job is to analyze the user's memory and understand its DIRECT impact.

IMPORTANT RULES:

1. Identify ONLY the PRIMARY (direct) affected life domain.
2. DO NOT infer secondary or indirect effects.
3. DO NOT propagate impacts across domains.
4. The ALSG (Adaptive Life State Graph) will calculate indirect effects.
5. Choose affected_domains ONLY from this list:
   - Sleep
   - Energy
   - Mood
   - Learning
6. Return ONLY valid JSON.
7. Do NOT include explanations outside the JSON.

-------------------------
EXAMPLES
-------------------------

Example 1

Memory:
"I slept only 3 hours yesterday."

Correct:

{{
    "sentiment":"negative",
    "emotion":"fatigue",
    "confidence":0.95,
    "severity":"high",
    "affected_domains":["Sleep"],
    "reason":"The event directly affects sleep."
}}

-------------------------

Example 2

Memory:
"I failed my coding interview."

Correct:

{{
    "sentiment":"negative",
    "emotion":"disappointment",
    "confidence":0.95,
    "severity":"high",
    "affected_domains":["Learning"],
    "reason":"The event directly impacts learning and skill development."
}}

-------------------------

Example 3

Memory:
"I felt very lonely today."

Correct:

{{
    "sentiment":"negative",
    "emotion":"sadness",
    "confidence":0.95,
    "severity":"medium",
    "affected_domains":["Mood"],
    "reason":"The event directly affects the user's mood."
}}

-------------------------

Example 4

Memory:
"I exercised for an hour and feel energetic."

Correct:

{{
    "sentiment":"positive",
    "emotion":"motivated",
    "confidence":0.95,
    "severity":"low",
    "affected_domains":["Energy"],
    "reason":"The event directly increases the user's energy."
}}

-------------------------

Now analyze this memory.

Title:
{title}

Description:
{description}

Return ONLY valid JSON in exactly this format:

{{
    "sentiment":"",
    "emotion":"",
    "confidence":0.0,
    "severity":"",
    "affected_domains":[],
    "reason":""
}}
"""
    def build_goal_matching_prompt(
        self,
        title: str,
        description: str,
        goals: list,
    ):

        goal_json = json.dumps(goals, indent=2)

        return f"""
You are ECHO's Goal Intelligence Engine.

Memory Title:
{title}

Memory Description:
{description}

User Goals:

{goal_json}

Determine whether this memory contributes toward any goal.

Return ONLY valid JSON.

Example:

{{
  "updates": [
    {{
      "goal_id": 1,
      "increment": 4,
      "confidence": 0.95,
      "reason": "Solved four Dynamic Programming problems."
    }}
  ]
}}

If no goals match:

{{"updates":[]}}

Return ONLY JSON.
"""
    def build_decision_prompt(
        self,
        analysis,
        goals,
        trend,
        memories,
        state,
    ):

        return f"""
    You are ECHO.

    You are an AI Living Digital Twin.

    Your job is to think like the user's future self.

    You have access to:

    Latest Memory Analysis:
    {analysis}

    Current State:
    {state}

    Recent Trend:
    {trend}

    Recent Memories:
    {memories}

    Current Goals:
    {goals}

    Think ONLY once.

    Return ONLY valid JSON.

    {{
        "insight": {{
            "title": "",
            "description": "",
            "severity": ""
        }},

        "planner": {{
            "title": "",
            "description": "",
            "priority": ""
        }},

        "goal_updates":[
            {{
                "goal_id":0,
                "increment":0,
                "confidence":0,
                "reason":""
            }}
        ]
    }}

    Rules:

    - If no planner needed, return an empty planner.
    - If no goal matches, return goal_updates as [].
    - Return ONLY JSON.
    """