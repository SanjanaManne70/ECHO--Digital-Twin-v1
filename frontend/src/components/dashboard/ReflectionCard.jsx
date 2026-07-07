import { useState } from "react";

export default function ReflectionCard({

    reflection,

}) {

    const [expanded, setExpanded] = useState(false);

    if (!reflection) {

        return (

            <div className="bg-white rounded-2xl shadow-lg p-6 mt-8">

                <h2 className="text-2xl font-bold mb-5">

                    🧠 Today's Reflection

                </h2>

                <p className="text-gray-400">

                    No reflection available.

                </p>

            </div>

        );

    }

    const LIMIT = 250;

    const shouldTrim = reflection.length > LIMIT;

    const displayText = expanded
        ? reflection
        : reflection.slice(0, LIMIT);

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 mt-8">

            <h2 className="text-2xl font-bold mb-5">

                🧠 Today's Reflection

            </h2>

            <p className="leading-8 text-gray-700">

                {displayText}

                {shouldTrim && !expanded && "..."}

                {shouldTrim && (

                    <button

                        onClick={() => setExpanded(!expanded)}

                        className="ml-2 text-indigo-600 hover:text-indigo-800 font-semibold"

                    >

                        {expanded ? "Read Less" : "Read More"}

                    </button>

                )}

            </p>

        </div>

    );

}