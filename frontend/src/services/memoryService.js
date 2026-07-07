import api from "../api/api";

function authHeaders() {
    const token = localStorage.getItem("token");

    return {
        Authorization: `Bearer ${token}`,
    };
}

export async function createMemory(memory) {

    console.log("Sending", memory);

    const res = await api.post(
        "/memory/",
        memory,
        {
            headers: authHeaders(),
        }
    );

    console.log("Response", res);

    return res.data;
}

export async function getMemories() {

    const res = await api.get(
        "/memory/",
        {
            headers: authHeaders(),
        }
    );

    return res.data;
}