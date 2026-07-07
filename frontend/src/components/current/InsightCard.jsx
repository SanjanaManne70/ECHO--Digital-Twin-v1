
export default function InsightCard({ analysis }) {

    if (!analysis) {
        return (
            <div className="bg-white rounded-xl shadow-lg p-6">
                Loading AI Insight...
            </div>
        );
    }
    const emotionEmoji = {
        happy: "😊",
        frustration: "😣",
        anger: "😠",
        sadness: "😔",
        disappointment: "😞",
        fear: "😨",
        neutral: "😐",
    };

    const sentimentColor = {
        positive: "text-green-600",
        negative: "text-red-600",
        neutral: "text-yellow-600",
    };

    return (

        <div className="bg-white rounded-xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-5">
                🧠 AI Insight
            </h2>

            <div className="space-y-4">

                <div>

                    <p className="text-sm text-gray-500">
                        Emotion
                    </p>

                    <p className="text-xl font-semibold">

                        {emotionEmoji[
                            analysis.emotion.toLowerCase()
                        ] || "🙂"}{" "}

                        {analysis.emotion}

                    </p>

                </div>

                <div>

                    <p className="text-sm text-gray-500">
                        Sentiment
                    </p>

                    <p
                        className={`font-semibold ${
                            sentimentColor[
                                analysis.sentiment.toLowerCase()
                            ] || "text-gray-600"
                        }`}
                    >
                        {analysis.sentiment}
                    </p>

                </div>

                <div>

                    <p className="text-sm text-gray-500">
                        Severity
                    </p>

                    <p className="font-semibold">

                        {analysis.severity}

                    </p>

                </div>

                <div className="border-t pt-4">

                    <p className="text-sm text-gray-500 mb-2">
                        AI Reasoning
                    </p>

                    <p className="leading-7 text-gray-700">

                        {analysis.reason}

                    </p>

                </div>

            </div>

        </div>

    );

}