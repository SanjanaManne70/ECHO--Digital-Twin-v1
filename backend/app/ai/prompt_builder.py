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
        # ---------------------------------
        # Format Current Digital Twin State
        # ---------------------------------

        state_data = []

        for item in state or []:
            state_data.append({
                "domain": item.domain,
                "value": round(item.value, 2),
            })

        # ---------------------------------
        # Format Latest Memory Analysis
        # ---------------------------------

        analysis_data = None

        if analysis:
            analysis_data = {
                "sentiment": analysis.sentiment,
                "emotion": analysis.emotion,
                "confidence": analysis.confidence,
                "severity": analysis.severity,
                "affected_domains": analysis.affected_domains,
                "reason": analysis.reason,
            }

        # ---------------------------------
        # Format Recent Memories
        # ---------------------------------

        memory_data = []

        for memory in memories or []:
            memory_data.append({
                "title": memory.title,
                "description": memory.description,
                "created_at": (
                    memory.created_at.isoformat()
                    if memory.created_at
                    else None
                ),
            })

        # ---------------------------------
        # Format Goals
        # ---------------------------------

        goal_data = []

        for goal in goals or []:
            goal_data.append({
                "id": goal.id,
                "title": goal.title,
                "category": goal.category,
                "target_value": goal.target_value,
                "target_unit": goal.target_unit,
                "current_value": goal.current_value,
                "progress": goal.progress,
                "description": goal.description,
                "completed": goal.completed,
            })

        # ---------------------------------
        # Convert to readable JSON
        # ---------------------------------

        analysis_json = json.dumps(
            analysis_data,
            indent=2,
        )

        state_json = json.dumps(
            state_data,
            indent=2,
        )

        trend_json = json.dumps(
            trend or {},
            indent=2,
        )

        memory_json = json.dumps(
            memory_data,
            indent=2,
        )

        goal_json = json.dumps(
            goal_data,
            indent=2,
        )

        # ---------------------------------
        # Decision Prompt
        # ---------------------------------

        return f"""
    You are ECHO.

    You are an AI Living Digital Twin.

    Your job is to think like the user's future self.

    You must reason using the complete structured context below.

    ==============================
    LATEST MEMORY ANALYSIS
    ==============================

    {analysis_json}


    ==============================
    CURRENT DIGITAL TWIN STATE
    ==============================

    {state_json}


    ==============================
    RECENT TREND
    ==============================

    {trend_json}


    ==============================
    RECENT MEMORIES
    ==============================

    {memory_json}


    ==============================
    CURRENT GOALS
    ==============================

    {goal_json}


    ==============================
    DECISION RULES
    ==============================

    1. You may create a goal update ONLY for a goal that appears in Current Goals.

    2. The "goal_id" MUST exactly match the "id" of one of the listed goals.

    3. NEVER invent, guess, or use 0 as a goal_id.

    4. If none of the current goals are relevant to this memory, return:
    "goal_updates": []

    5. Do not update completed goals.

    6. Base your decision on the latest memory, current digital twin state,
    recent trend, recent memories, and current goals.

    7. Generate an insight only when the context supports a useful observation.

    8. Generate a planner task only when an actionable next step is appropriate.

    9. Keep the planner task focused on ONE actionable step.

    10. Think about the user's current state and recent pattern,
        not just the latest memory in isolation.

    11. Think ONLY once.

    ==============================
    OUTPUT FORMAT
    ==============================

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

        "goal_updates": [
            {{
                "goal_id": 0,
                "increment": 0,
                "confidence": 0,
                "reason": ""
            }}
        ]
    }}

    Rules:

    - If no planner is needed, return an empty planner.
    - If no goal matches, return "goal_updates": [].
    - Every goal_id must come from the Current Goals list.
    - Do not update completed goals.
    - Return ONLY JSON.
    """