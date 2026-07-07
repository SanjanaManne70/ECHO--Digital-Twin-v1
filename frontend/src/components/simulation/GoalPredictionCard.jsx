export default function GoalPredictionCard({ goal }) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">

            <h2 className="text-2xl font-bold mb-6">

                🎯 {goal.title}

            </h2>

            <p className="text-gray-500">

                Current Progress

            </p>

            <div className="w-full bg-gray-200 rounded-full h-4 mt-2">

                <div

                    className="bg-indigo-600 h-4 rounded-full transition-all duration-1000"

                    style={{

                        width: `${goal.current_progress}%`

                    }}

                />

            </div>

            <p className="mt-2 font-semibold">

                {goal.current_progress}%

            </p>

            <div className="text-center text-3xl my-6">

                ↓

            </div>

            <p className="text-gray-500">

                Future Progress

            </p>

            <div className="w-full bg-gray-200 rounded-full h-4 mt-2">

                <div

                    className="bg-green-600 h-4 rounded-full transition-all duration-1000"

                    style={{

                        width: `${goal.future_progress}%`

                    }}

                />

            </div>

            <p className="mt-2 font-semibold">

                {goal.future_progress}%

            </p>

            <div className="mt-6 bg-green-100 rounded-xl p-3">

                <p className="text-green-700 font-semibold">

                    📅 {goal.completion}

                </p>

            </div>

        </div>

    );

}