class HybridImpactEngine:

    def calculate(
        self,
        analysis,
    ):

        impact = {}

        SEVERITY_WEIGHTS = {

            "low":1,

            "medium":3,

            "high":5,

        }
        base = SEVERITY_WEIGHTS.get(
            analysis.severity,
            1,
        )

        sign = 1

        if analysis.sentiment == "negative":
            sign = -1

        for domain in analysis.affected_domains:

            impact[domain] = sign * base

        return impact