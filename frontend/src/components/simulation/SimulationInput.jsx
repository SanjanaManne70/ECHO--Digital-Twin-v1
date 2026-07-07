import { useState } from "react";

export default function SimulationInput({ onSimulate }) {

    const [scenario, setScenario] = useState("");

    function handleClick() {

        if (!scenario.trim()) return;

        onSimulate(scenario);

    }

    return (

        <div className="bg-white rounded-2xl shadow-lg p-8">

            <h2 className="text-2xl font-bold mb-2">

                Imagine Your Future

            </h2>

            <p className="text-gray-500 mb-6">

                Describe a habit, lifestyle change, or decision you'd like ECHO to simulate.

            </p>

            <textarea

                rows={5}

                value={scenario}

                onChange={(e) => setScenario(e.target.value)}

                className="w-full border border-gray-300 rounded-xl p-4 focus:ring-2 focus:ring-indigo-500 focus:outline-none"

                placeholder="Example: What happens if I solve 5 Dynamic Programming problems every day for one month?"

            />

            <button

                onClick={handleClick}

                className="mt-6 bg-indigo-600 hover:bg-indigo-700 transition text-white px-8 py-3 rounded-xl font-semibold"

            >

                🔮 Simulate Future

            </button>

        </div>

    );

}