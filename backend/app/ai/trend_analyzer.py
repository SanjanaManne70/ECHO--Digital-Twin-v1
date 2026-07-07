class TrendAnalyzer:

    def analyze(
        self,
        snapshots,
    ):

        if len(snapshots) < 2:

            return {

                "summary": "Not enough history.",

            }

        oldest = snapshots[-1]

        latest = snapshots[0]

        return {

            "sleep_change":
                round(
                    latest.sleep - oldest.sleep,
                    2,
                ),

            "energy_change":
                round(
                    latest.energy - oldest.energy,
                    2,
                ),

            "mood_change":
                round(
                    latest.mood - oldest.mood,
                    2,
                ),

            "learning_change":
                round(
                    latest.learning - oldest.learning,
                    2,
                ),

        }