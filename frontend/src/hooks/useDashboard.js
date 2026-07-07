import { useEffect, useState } from "react";
import api from "../api/api";

export default function useDashboard() {

    const [loading, setLoading] = useState(true);

    const [dashboard, setDashboard] = useState({
        state: null,
        reflection: null,
        insight: null,
        planner: [],
        trend: null,
        user:null,
    });

    async function refreshDashboard() {

        setLoading(true);

        const [
            state,
            reflection,
            insight,
            planner,
            trend,
            user,
        ] = await Promise.all([
            api.get("/current-state/"),
            api.get("/reflection/"),
            api.get("/insight/"),
            api.get("/planner/"),
            api.get("/trend/"),
            api.get("/users/me"),
        ]);

        setDashboard({
            state: state.data,
            reflection: reflection.data,
            insight: insight.data,
            planner: planner.data,
            trend: trend.data,
            user: user.data,
        });
        console.log(user.data);

        setLoading(false);
    }

    useEffect(() => {
        refreshDashboard();
    }, []);

    return {
        loading,
        refreshDashboard,
        ...dashboard,
    };
}