function Task({ task }) {

    return (

        <div className="flex items-center gap-3 py-2">

            <input

                type="checkbox"

                checked={task.completed}

                readOnly

            />

            <span>

                {task.title}

            </span>

        </div>

    );

}

export default function PlannerCard({

    tasks,

}) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 mt-8">

            <h2 className="text-2xl font-bold mb-5">

                📅 Today's Planner

            </h2>

            {

                tasks.length === 0

                ?

                <p>No pending tasks.</p>

                :

                tasks.map(

                    task => (

                        <Task

                            key={task.id}

                            task={task}

                        />

                    )

                )

            }

        </div>

    );

}