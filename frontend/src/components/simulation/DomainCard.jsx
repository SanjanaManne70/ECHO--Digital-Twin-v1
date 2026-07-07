export default function DomainCard({ domain }) {

    const icon = {

        Health: "❤️",

        Learning: "🧠",

        Mood: "😊",

        Energy: "⚡",

        Sleep: "😴",

    }[domain.name] || "📊";

    const trend = {

        up: "📈 Improving",

        down: "📉 Declining",

        stable: "➡ Stable",

    }[domain.trend];

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition">

            <h3 className="text-2xl font-bold mb-5">

                {icon} {domain.name}

            </h3>

            <div className="space-y-5">

                <div>

                    <p className="text-gray-500">

                        Current

                    </p>

                    <p className="font-semibold text-lg">

                        {domain.current}

                    </p>

                </div>

                <div className="text-center text-3xl">

                    ↓

                </div>

                <div>

                    <p className="text-gray-500">

                        Future

                    </p>

                    <p className="font-semibold text-lg text-indigo-600">

                        {domain.future}

                    </p>

                </div>

                <div className="mt-5 bg-indigo-50 rounded-lg p-3 text-center font-semibold text-indigo-700">

                    {trend}

                </div>

            </div>

        </div>

    );

}