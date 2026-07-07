import { useState } from "react";

import usePlanner from "../../hooks/usePlanner";

import TaskItem from "./TaskItem";

import TaskInput from "./TaskInput";

export default function PlannerWidget() {

    const {

    pending,

    completed,

    addTask,

    completeTask,

    clearCompleted,

} = usePlanner();

    const [

        adding,

        setAdding,

    ] = useState(false);

    const [

        showCompleted,

        setShowCompleted,

    ] = useState(false);

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <div className="flex justify-between items-center mb-6">

    <h2 className="text-2xl font-bold">

        📝 Today's Planner

    </h2>

    {

        !adding && (

            <button

                onClick={() => setAdding(true)}

                className="text-indigo-600 hover:text-indigo-700 font-semibold"

            >

                + Add Task

            </button>

        )

    }

</div>

            {

                pending.length === 0 && !adding && (

                    <div className="mt-8 text-center">

                        <p className="text-gray-500">

                            No plans for today.

                        </p>

                        <p className="text-gray-400 mt-2">


                        </p>

                    </div>

                )

            }

            {

                pending.map(task => (

                    <TaskItem

                        key={task.id}

                        task={task}

                        onToggle={completeTask}

                    />

                ))

            }

            {

                adding

                &&

                <TaskInput

                    onSave={(title)=>{

                        addTask(title);

                        setAdding(false);

                    }}

                />

            }

           
            

            <div className="flex justify-between items-center">

                <button

                    onClick={() => setShowCompleted(

                        !showCompleted

                    )}

                    className="font-semibold"

                >

                    {

                        showCompleted

                            ? "▼ Completed Tasks"

                            : "▶ Completed Tasks"

                    }

                </button>

                {

                    showCompleted &&
    completed.length > 0 && (

                        <button

                            onClick={clearCompleted}

                            className="text-red-500 hover:text-red-700 text-xl"

                            title="Delete completed tasks"

                        >

                            🗑️

                        </button>

                    )

                }

            </div>
            <div className="mt-4">

    {

        showCompleted && (

            completed.length === 0 ? (

                <p className="text-gray-400">

                    No completed tasks yet.

                </p>

            ) : (

                completed.map(task => (

                    <TaskItem

                        key={task.id}

                        task={task}

                        onToggle={() => {}}

                    />

                ))

            )

        )

    }

</div>

        </div>

    );

}