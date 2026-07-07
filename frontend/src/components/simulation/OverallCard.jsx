export default function OverallCard({ overall }) {

    if (!overall) return null;

    const color = {

        "Excellent Trajectory": "bg-green-100 text-green-700",

        "Good Trajectory": "bg-blue-100 text-blue-700",

        "Moderate Risk": "bg-yellow-100 text-yellow-700",

        "High Risk": "bg-red-100 text-red-700",

    };

    return (

        <div className="bg-gradient-to-r from-indigo-600 via-purple-600 to-blue-600 rounded-2xl shadow-xl p-8 text-white">

            <div className="flex justify-between items-center">

                <div>

                    <h1 className="text-4xl font-bold">

                        🔮 Future You

                    </h1>

                    <p className="mt-3 text-lg opacity-90">

                        {overall.summary}

                    </p>

                </div>

                <div className={`px-4 py-2 rounded-full font-semibold ${color[overall.status] || "bg-white text-black"}`}>

                    {overall.status}

                </div>

            </div>

            <div className="mt-8">

                <div className="flex justify-between mb-2">

                    <span>Prediction Confidence</span>

                    <span>{overall.confidence}%</span>

                </div>

                <div className="w-full bg-white/30 rounded-full h-4">

                    <div

                        className="bg-white h-4 rounded-full transition-all duration-1000"

                        style={{

                            width: `${overall.confidence}%`

                        }}

                    />

                </div>

            </div>

        </div>

    );

}