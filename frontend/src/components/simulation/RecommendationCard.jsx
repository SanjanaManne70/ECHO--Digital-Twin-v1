export default function RecommendationCard({ recommendations }) {

    if (!recommendations.length) return null;

    return (

        <div className="bg-indigo-50 border border-indigo-200 rounded-2xl p-6">

            <h2 className="text-2xl font-bold text-indigo-700 mb-5">

                💡 ECHO Recommends

            </h2>

            <div className="space-y-3">

                {

                    recommendations.map((r, i) => (

                        <div

                            key={i}

                            className="bg-white rounded-lg p-3 shadow-sm"

                        >

                            ✓ {r}

                        </div>

                    ))

                }

            </div>

        </div>

    );

}