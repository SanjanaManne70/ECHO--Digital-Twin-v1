import api from "../api/api";

export async function getTimeline() {

    const res = await api.get("/timeline/");

    return res.data;

}