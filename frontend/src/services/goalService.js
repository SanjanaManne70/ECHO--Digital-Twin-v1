import api from "../api/api";

function authHeaders() {
    const token = localStorage.getItem("token");

    return {
        Authorization: `Bearer ${token}`,
    };
}

export async function getGoals() {

    const res = await api.get(
        "/goal/",
        {
            headers: authHeaders(),
        }
    );

    return res.data;
}
export async function deleteGoal(id) {

    const token = localStorage.getItem("token");

    await api.delete(

        `/goal/${id}`,

        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }

    );

}