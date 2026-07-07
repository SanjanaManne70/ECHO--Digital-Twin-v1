import api from "../api/api";

export async function getLatestAnalysis() {

    const token = localStorage.getItem("token");

    const response = await api.get(
        "/memory/latest-analysis",
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );

    return response.data;
}