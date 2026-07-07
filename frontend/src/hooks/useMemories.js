import { useEffect, useState } from "react";

import {

    getMemories,

    createMemory,

} from "../services/memoryService";

export default function useMemories() {

    const [memories, setMemories] = useState([]);

    const [loading, setLoading] = useState(true);

    async function refresh() {

        try {

            const data = await getMemories();

            setMemories(data);

        }

        finally {

            setLoading(false);

        }

    }

    async function addMemory(memory) {

    console.log("1. addMemory called");

    try {

        const result = await createMemory(memory);

        console.log("2. POST finished", result);

        await refresh();

        console.log("3. Refresh finished");

    } catch (err) {

        console.error("ADD MEMORY ERROR", err);

        throw err;

    }

}

    useEffect(() => {

        refresh();

    }, []);

    return {

        memories,

        loading,

        refresh,

        addMemory,

    };

}