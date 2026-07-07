import { useEffect, useState } from "react";
import api from "../api/api";

export default function usePlanner() {

    const [pending, setPending] = useState([]);

    const [completed, setCompleted] = useState([]);

    async function refresh() {

        const [

            pendingRes,

            completedRes,

        ] = await Promise.all([

            api.get("/planner/"),

            api.get("/planner/completed"),

        ]);

        setPending(pendingRes.data);

        setCompleted(completedRes.data);

    }

    async function addTask(title) {

        await api.post("/planner/", {

            title,

        });

        refresh();

    }

    async function completeTask(task) {

    await api.put(

        `/planner/${task.id}`

    );

    await refresh();

}

    async function clearCompleted() {

        await api.delete(

            "/planner/completed"

        );

        refresh();

    }

    useEffect(() => {

        refresh();

    }, []);

    return {

        pending,

        completed,

        addTask,

        completeTask,

        clearCompleted,

    };

}