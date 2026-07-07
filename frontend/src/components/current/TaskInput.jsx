import { useState } from "react";

export default function TaskInput({

    onSave,

}) {

    const [title, setTitle] = useState("");

    function save() {

        if (!title.trim()) return;

        onSave(title);

        setTitle("");

    }

    return (

        <div className="mt-4">

            <input

                className="border rounded-lg w-full p-3"

                placeholder="Enter a task..."

                value={title}

                onChange={(e) => setTitle(e.target.value)}

            />

            <button

                onClick={save}

                className="mt-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg px-6 py-2"

            >

                Save

            </button>

        </div>

    );

}