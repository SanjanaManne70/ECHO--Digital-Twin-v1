from collections import defaultdict
from datetime import datetime

from app.services.daily_chapter_service import DailyChapterService


class TimelineBuilder:

    def __init__(self):

        self.chapter_service = DailyChapterService()

    def build(self, timeline):

        grouped = defaultdict(list)

        # Group events by date
        for event in timeline:

            created_at = event["created_at"]

            if isinstance(created_at, datetime):
                day = created_at.date()
            else:
                day = created_at

            grouped[day].append(event)

        daily_timeline = []

        # Build one chapter for each day
        for day, events in grouped.items():

            memories = []
            insights = []
            goals = []
            current_state = {}

            for event in events:

                if event["type"] == "memory":

                    memories.append(event)

                elif event["type"] == "insight":

                    insights.append(event)

                elif event["type"] == "planner":

                    goals.append(event)

                elif event["type"] == "snapshot":

                    current_state = {
                        "learning": event.get("learning"),
                        "mood": event.get("mood"),
                        "energy": event.get("energy"),
                        "sleep": event.get("sleep"),
                    }

            chapter = self.chapter_service.build(

                memories=memories,

                insights=insights,

                goals=goals,

                current_state=current_state,

            )

            daily_timeline.append({

                "date": day,

                "title": chapter["title"],

                "mood": chapter["mood"],

                "summary": chapter["summary"],

                "growth": chapter["growth"],

                "highlight": chapter["highlight"],

                "tomorrow": chapter["tomorrow"],

                # Temporary.
                # We'll remove this after updating DayCard.
                "events": events,

            })

        daily_timeline.sort(

            key=lambda x: x["date"],

            reverse=True,

        )

        return daily_timeline