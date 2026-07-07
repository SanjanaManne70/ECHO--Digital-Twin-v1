export default function GoalCard({ goal, onDelete }) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">

            <div className="flex justify-between">

                <h2 className="text-2xl font-bold">

                    🎯 {goal.title}

                </h2>

                <button

                    onClick={() => onDelete(goal.id)}

                    className="text-red-500 hover:text-red-700 text-xl"

                >

                    🗑

                </button>

            </div>

            <p className="mt-4 text-gray-600 leading-7">

                {goal.description}

            </p>

            <div className="mt-8">

                <div className="flex justify-between">

                    <span className="font-semibold">

                        Progress

                    </span>

                    <span>

                        {goal.progress}%

                    </span>

                </div>

                <div className="bg-gray-200 h-3 rounded-full mt-3">

                    <div

                        className="bg-gradient-to-r from-green-500 to-emerald-600 h-3 rounded-full"

                        style={{

                            width: `${goal.progress}%`

                        }}

                    />

                </div>

            </div>

            <div className="mt-8 flex justify-between">

                <span>

                    {

                        goal.completed

                        ? "✅ Completed"

                        : "🚀 In Progress"

                    }

                </span>

                <span className="text-gray-500">

                    AI Tracking

                </span>

            </div>

        </div>

    );

}