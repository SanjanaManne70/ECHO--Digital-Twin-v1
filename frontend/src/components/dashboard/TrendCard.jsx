export default function TrendCard({ trend }) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-5">

                📈 Weekly Trend

            </h2>

            <TrendRow
                title="Mood"
                value={trend.mood_change}
            />

            <TrendRow
                title="Learning"
                value={trend.learning_change}
            />

            <TrendRow
                title="Energy"
                value={trend.energy_change}
            />

            <TrendRow
                title="Sleep"
                value={trend.sleep_change}
            />

        </div>

    );

}

function TrendRow({ title, value }) {

    return (

        <div className="flex justify-between py-3 border-b">

            <span>{title}</span>

            <span
                className={
                    value >= 0
                        ? "text-green-600 font-bold"
                        : "text-red-600 font-bold"
                }
            >
                {value >= 0 ? "▲" : "▼"} {Math.abs(value)}
            </span>

        </div>

    );

}