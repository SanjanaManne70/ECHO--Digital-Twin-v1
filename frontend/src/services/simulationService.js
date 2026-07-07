import api from "../api/api";

export async function simulate(scenario) {

    const token = localStorage.getItem("token");

    const response = await api.post(

        "/simulation/",

        {
            scenario,
        },

        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }

    );

    return response.data;
}