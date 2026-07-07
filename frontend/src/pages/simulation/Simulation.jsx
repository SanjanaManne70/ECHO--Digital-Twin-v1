import { useState } from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";
import SimulationInput from "../../components/simulation/SimulationInput";
import SimulationResult from "../../components/simulation/SimulationResult";

import api from "../../api/api";

export default function Simulation() {

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState(null);

    async function runSimulation(scenario) {

        if (!scenario.trim()) return;

        try {

            setLoading(true);

            setResult(null);

            const token = localStorage.getItem("token");

            const response = await api.post(

                "/simulation/",

                {
                    scenario,
                },

                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }

            );

            setResult(response.data);

        }

        catch (err) {

            console.log(err);

            alert("Simulation failed.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <DashboardLayout>

            <div className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-2xl p-8 mb-10">

                <h1 className="text-4xl font-bold">

                    🔮 Future You

                </h1>

                <p className="mt-2 opacity-90">

                    Explore how today's decisions may shape your future over the next 30 days.

                </p>

            </div>

            <SimulationInput

                onSimulate={runSimulation}

            />

            {

                loading && (

                    <div className="mt-10 bg-white rounded-xl shadow-lg p-10 text-center">

                        <div className="animate-spin rounded-full h-12 w-12 border-4 border-gray-200 border-t-indigo-600 mx-auto"></div>

                        <h2 className="text-2xl font-bold mt-6">

                            🤖 ECHO is simulating your future...

                        </h2>

                        <p className="text-gray-500 mt-3">

                            Analyzing your Digital Twin, habits, goals, and predicting your next 30 days.

                        </p>

                    </div>

                )

            }

            {

                !loading && result && (

                    <SimulationResult

                        result={result}

                    />

                )
                

            }
            {
    !loading && !result && (

        <div className="mt-12 bg-white rounded-2xl shadow-lg p-12 text-center">

            <div className="text-6xl mb-6">

                🔮

            </div>

            <h2 className="text-3xl font-bold">

                Your Future Awaits

            </h2>

            <p className="text-gray-500 mt-4">

                Enter a habit or lifestyle change above and let ECHO predict how your next 30 days could unfold.

            </p>

        </div>

    )
}

        </DashboardLayout>

    );

}