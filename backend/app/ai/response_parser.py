import json

from app.ai.analysis_result import AnalysisResult
from app.ai.goal_match_result import (
    GoalMatchResult,
    GoalUpdate,
)
from app.ai.decision_result import (
    DecisionResult,
    PlannerDecision,
    InsightDecision,
    GoalDecision,
)
from app.ai.simulation_result import (
    OverallPrediction,
    SimulationResult,
    DomainPrediction,
    GoalPrediction,
)
class ResponseParser:

    def parse(self, response: str) -> AnalysisResult:

        data = json.loads(response)

        # Normalize emotion
        emotion = data.get("emotion", "neutral")

        if isinstance(emotion, list):
            emotion = emotion[0] if emotion else "neutral"

        emotion = emotion.lower()

        # Normalize sentiment
        sentiment = data.get(
            "sentiment",
            "neutral",
        ).lower()

        # Normalize severity
        severity = data.get(
            "severity",
            "medium",
        ).lower()

        # Keep only valid severity values
        severity_map = {
            "low": "low",
            "medium": "medium",
            "moderate": "medium",
            "high": "high",
        }

        severity = severity_map.get(
            severity,
            "medium",
        )

        return AnalysisResult(
            sentiment=sentiment,
            emotion=emotion,
            confidence=float(
                data.get(
                    "confidence",
                    0.5,
                )
            ),
            severity=severity,
            affected_domains=data.get(
                "affected_domains",
                [],
            ),
            reason=data.get(
                "reason",
                "",
            ),
        )
    
    def parse_goal_matching(
        self,
        raw_response,
    ):

        try:

            data = json.loads(raw_response)

        except Exception:

            return GoalMatchResult()

        result = GoalMatchResult()

        for update in data.get("updates", []):

            result.updates.append(

                GoalUpdate(

                    goal_id=update.get("goal_id"),

                    increment=float(update.get("increment", 0)),

                    confidence=float(update.get("confidence", 0)),

                    reason=update.get("reason", ""),

                )

            )

        return result

    def parse_decision(
        self,
        raw_response,
    ):

        data = json.loads(raw_response)

        result = DecisionResult()

        insight = data.get("insight")

        if insight:

            result.insight = InsightDecision(

                title=insight.get("title", ""),

                description=insight.get("description", ""),

                severity=insight.get("severity", "medium"),

            )

        planner = data.get("planner")

        if planner:

            result.planner = PlannerDecision(

                title=planner.get("title", ""),

                description=planner.get("description", ""),

                priority=planner.get("priority", "Medium"),

            )

        for g in data.get("goal_updates", []):

            result.goals.append(

                GoalDecision(

                    goal_id=g["goal_id"],

                    increment=g["increment"],

                    confidence=g["confidence"],

                    reason=g["reason"],

                )

            )

        return result
    
    def parse_simulation(
        self,
        raw_response,
    ):

        try:

            data = json.loads(raw_response)

        except Exception as e:

            print(raw_response)

            return SimulationResult()

        result = SimulationResult()

        overall = data.get("overall")

        if overall:

            result.overall = OverallPrediction(

                status=overall.get("status", ""),

                confidence=float(overall.get("confidence", 0)),

                summary=overall.get("summary", ""),

            )

        for d in data.get("domains", []):

            result.domains.append(

                DomainPrediction(

                    name=d.get("name", ""),

                    current=d.get("current", ""),

                    future=d.get("future", ""),

                    trend=d.get("trend", ""),

                )

            )

        for g in data.get("goals", []):

            result.goals.append(

                GoalPrediction(

                    title=g.get("title", ""),

                    current_progress=float(
                        g.get("current_progress", 0)
                    ),

                    future_progress=float(
                        g.get("future_progress", 0)
                    ),

                    completion=g.get(
                        "completion",
                        "",
                    ),

                )

            )

        result.benefits = data.get(
            "benefits",
            [],
        )

        result.risks = data.get(
            "risks",
            [],
        )

        result.recommendations = data.get(
            "recommendations",
            [],
        )

        return result