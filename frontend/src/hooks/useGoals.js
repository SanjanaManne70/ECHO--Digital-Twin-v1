import { useEffect, useState } from "react";
import { getGoals } from "../services/goalService";

export default function useGoals() {

    const [goals, setGoals] = useState([]);

    const [loading, setLoading] = useState(true);

    async function refresh() {

        try {

            const data = await getGoals();

            setGoals(data);

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        refresh();

    }, []);

    return {

        goals,

        loading,

        refresh,

    };

}