import { useState } from "react";

export default function NewMemoryModal({ onClose, onSave }) {

    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [mood, setMood] = useState("😊");

    function handleSave() {

        if (!content.trim()) return;

        onSave({

    title: title.trim() || "Untitled",

    description: content.trim(),

});

        onClose();
    }

    return (

        <div
            className="fixed inset-0 z-50 flex items-center justify-center bg-[#2B2A4C]/40 backdrop-blur-md p-4"
            onClick={onClose}
        >

            <div
                onClick={(e) => e.stopPropagation()}
                className="
                    paper-grain
                    relative
                    bg-[#FBF7F0]
                    rounded-3xl
                    shadow-2xl
                    border
                    border-[#2B2A4C]/10
                    w-[650px]
                    h-[80vh]
                    flex
                    flex-col
                    overflow-hidden
                "
            >

                {/* Close */}

                <button
                    onClick={onClose}
                    className="absolute top-5 right-6 text-3xl text-[#2B2A4C]/40 hover:text-[#2B2A4C]"
                >
                    ×
                </button>

                {/* Header */}

                <div className="px-8 pt-8">

                    <p className="font-hand text-lg text-[#C1548A]">

                        {new Date().toLocaleDateString(undefined, {
                            weekday: "long",
                            month: "long",
                            day: "numeric",
                            year: "numeric",
                        })}

                    </p>

                    <input
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="Give this memory a title..."
                        className="
                            w-full
                            mt-2
                            bg-transparent
                            outline-none
                            text-4xl
                            font-semibold
                            text-[#2B2A4C]
                            placeholder:text-[#2B2A4C]/30
                        "
                    />

                </div>

                {/* Mood */}

                <div className="flex gap-3 px-8 mt-5">

                    {["😊", "😍", "🎉", "😴", "😢", "😤"].map((emoji) => (

                        <button
                            key={emoji}
                            onClick={() => setMood(emoji)}
                            className={`
                                w-11
                                h-11
                                rounded-full
                                text-2xl
                                transition-all
                                ${
                                    mood === emoji
                                        ? "bg-[#2B2A4C]/10 scale-110"
                                        : "opacity-50 hover:opacity-100 hover:scale-105"
                                }
                            `}
                        >
                            {emoji}
                        </button>

                    ))}

                </div>

                {/* Diary */}

                <div className="flex-1 px-8 mt-6">

                    <textarea
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        placeholder="Dear Diary..."
                        className="
                            w-full
                            h-full
                            resize-none
                            bg-transparent
                            outline-none
                            text-lg
                            leading-9
                            text-[#2B2A4C]/90
                            placeholder:text-[#2B2A4C]/30
                        "
                        style={{
                            backgroundImage:
                                "repeating-linear-gradient(to bottom, transparent 0px, transparent 35px, rgba(43,42,76,0.10) 36px)",
                        }}
                    />

                </div>

                {/* Footer */}

                <div className="flex justify-end gap-3 px-8 py-5 border-t border-[#2B2A4C]/10">

                    <button
                        onClick={onClose}
                        className="px-5 py-2 rounded-full text-[#2B2A4C]/60 hover:text-[#2B2A4C]"
                    >
                        Cancel
                    </button>

                    <button
                        onClick={handleSave}
                        className="
                            px-6
                            py-2
                            rounded-full
                            bg-[#2B2A4C]
                            text-white
                            hover:bg-[#3d3c66]
                            transition-all
                        "
                    >
                        Save Memory
                    </button>

                </div>

            </div>

        </div>

    );

}