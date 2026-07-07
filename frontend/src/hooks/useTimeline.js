import { useEffect, useState } from "react";
import { getTimeline } from "../services/timelineService";

export default function useTimeline() {

    const [timeline, setTimeline] = useState([]);

    const [loading, setLoading] = useState(true);

    async function refresh() {

        try {

            const data = await getTimeline();
            console.log("Timeline API Response:", data);

            setTimeline(data);

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        refresh();

    }, []);

    return {

        timeline,

        loading,

        refresh,

    };

}