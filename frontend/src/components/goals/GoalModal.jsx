import { useState } from "react";
import api from "../../api/api";

export default function GoalModal({ onSaved }) {

    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    async function handleSubmit(e) {

        e.preventDefault();

        try {

            const token = localStorage.getItem("token");

            await api.post(

                "/goal/",

                {

                    title,

                    description,

                },

                {

                    headers: {

                        Authorization: `Bearer ${token}`,

                    },

                }

            );

            setTitle("");

            setDescription("");

            onSaved();

        }

        catch (err) {

            console.log(err);

            alert("Failed to create Goal.");

        }

    }

    return (

        <div className="bg-white rounded-xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-6">

                ➕ Add Goal

            </h2>

            <input

                className="border w-full p-3 rounded mb-4"

                placeholder="Goal Title"

                value={title}

                onChange={(e)=>setTitle(e.target.value)}

            />

            <textarea

                className="border w-full p-3 rounded mb-4"

                placeholder="Goal Description"

                value={description}

                onChange={(e)=>setDescription(e.target.value)}

            />

            <button

                onClick={handleSubmit}

                className="bg-green-600 hover:bg-green-700 text-white w-full rounded p-3"

            >

                Save Goal

            </button>

        </div>

    );

}