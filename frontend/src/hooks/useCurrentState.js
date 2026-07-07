import { useEffect, useState } from "react";
import api from "../api/api";

export default function useCurrentState() {

  const [state, setState] = useState(null);

  async function loadState() {

    const token = localStorage.getItem("token");
    console.log("Fetching current state...");
    const res = await api.get(
      "/current-state/",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    console.log("Received:", res.data);

    setState(res.data);

  }

  useEffect(() => {
    loadState();
  }, []);

  return {
    state,
    refresh: loadState,
  };

}