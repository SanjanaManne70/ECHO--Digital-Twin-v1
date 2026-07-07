import { useState } from "react";
import { createMemory } from "../../services/memoryService";

export default function MemoryModal({ onSaved }) {

    const [open, setOpen] = useState(false);

    const [title, setTitle] = useState("");

    const [description, setDescription] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleSubmit(e) {

        e.preventDefault();

        if (!title.trim() || !description.trim()) {

            alert("Please fill all fields.");

            return;

        }

        setLoading(true);

        try {

            await createMemory({

                title,

                description,

            });

            if (onSaved) {

                await onSaved();

            }

            setTitle("");

            setDescription("");

            setOpen(false);

        }

        catch (err) {

            console.error(err);

            alert("Failed to save memory.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <>

            <button

                onClick={() => setOpen(true)}

                className="bg-white text-indigo-700 font-semibold px-6 py-3 rounded-xl hover:bg-gray-100 transition"

            >

                + New Memory

            </button>

            {

                open && (

                    <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">

                        <div className="bg-white rounded-2xl shadow-2xl p-8 w-[450px]">

                            <h2 className="text-2xl font-bold mb-6">

                                Add Memory

                            </h2>

                            <input

                                className="border rounded-lg p-3 w-full mb-4 text-gray-900 placeholder-gray-400 bg-white"

                                placeholder="Title"

                                value={title}

                                onChange={(e) => setTitle(e.target.value)}

                            />

                            <textarea

                                rows={5}

                                className="border rounded-lg p-3 w-full mb-6 text-gray-900 placeholder-gray-400 bg-white"

                                placeholder="Describe what happened..."

                                value={description}

                                onChange={(e) => setDescription(e.target.value)}

                            />

                            <div className="flex justify-end gap-3">

                                <button

                                    onClick={() => setOpen(false)}

                                    className="px-5 py-2 rounded-lg bg-gray-200"

                                >

                                    Cancel

                                </button>

                                <button

                                    onClick={handleSubmit}

                                    disabled={loading}

                                    className="px-5 py-2 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700"

                                >

                                    {

                                        loading

                                            ? "Saving..."

                                            : "Save Memory"

                                    }

                                </button>

                            </div>

                        </div>

                    </div>

                )

            }

        </>

    );

}