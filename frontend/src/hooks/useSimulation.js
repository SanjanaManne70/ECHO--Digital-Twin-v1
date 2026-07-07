import { useState } from "react";

import { simulate } from "../services/simulationService";

export default function useSimulation() {

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState(null);

    async function runSimulation(scenario) {

        setLoading(true);

        try {

            const data = await simulate(scenario);

            setResult(data);

        }

        finally {

            setLoading(false);

        }

    }

    return {

        loading,

        result,

        runSimulation,

    };

}