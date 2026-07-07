import { useState } from "react";

export default function TaskItem({

    task,

    onToggle,

}) {

    const [checked, setChecked] = useState(false);

    function handleToggle() {

        setChecked(true);

setTimeout(async () => {

    await onToggle(task);

}, 300);
    }

    return (

        <div className="flex items-center gap-3 py-3 border-b">

            <input

            type="checkbox"

            checked={checked || task.completed}

            disabled={task.completed}

            onChange={handleToggle}

            className="w-5 h-5 accent-green-600 cursor-pointer disabled:cursor-default"

        />

            <span

                className={`flex-1 text-lg ${

                    task.completed

                        ? "line-through text-gray-400"

                        : "text-gray-800"

                }`}

            >

                {task.title}

            </span>

        </div>

    );

}