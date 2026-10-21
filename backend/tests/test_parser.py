from app.ai.response_parser import ResponseParser

parser = ResponseParser()

response = """
{
  "sentiment":"negative",
  "emotion":["disappointment"],
  "confidence":1.0,
  "severity":"high",
  "affected_domains":[
      "Mood",
      "Confidence"
  ],
  "reason":"Interview failure."
}
"""

analysis = parser.parse(response)

print(analysis)
print(analysis.sentiment)
print(analysis.emotion)
print(analysis.severity)
print(analysis.affected_domains)
print(analysis.reason)