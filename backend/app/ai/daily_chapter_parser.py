import json


class DailyChapterParser:

    def parse(self, raw_response):

        data = json.loads(raw_response)

        return {

            "title": data.get("title", "📖 Another Chapter"),

            "mood": data.get("mood", "🙂"),

            "summary": data.get(

                "summary",

                "Another meaningful day added to your journey."

            ),

            "growth": data.get(

                "growth",

                []

            ),

            "highlight": data.get(

                "highlight",

                ""

            ),

            "tomorrow": data.get(

                "tomorrow",

                ""

            ),

        }