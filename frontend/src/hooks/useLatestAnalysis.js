import { useEffect, useState } from "react";
import { getLatestAnalysis } from "../services/analysisService";

export default function useLatestAnalysis() {

    const [analysis, setAnalysis] = useState(null);

    async function refresh() {

        const data = await getLatestAnalysis();

        setAnalysis(data);

    }

    useEffect(() => {

        refresh();

    }, []);

    return {
        analysis,
        refresh,
    };
}