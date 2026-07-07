import { useState } from "react";

export default function InsightDashboardCard({

    insight,

}) {

    const [expanded, setExpanded] = useState(false);

    if (!insight) {

        return (

            <div className="bg-white rounded-2xl shadow-lg p-6">

                <h2 className="text-2xl font-bold mb-5">

                    💡 Biggest Insight

                </h2>

                <p className="text-gray-400">

                    No insights available.

                </p>

            </div>

        );

    }

    const LIMIT = 180;

    const text = insight.description || "";

    const shouldTrim = text.length > LIMIT;

    const displayText = expanded
        ? text
        : text.slice(0, LIMIT);

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 h-full">

            <h2 className="text-2xl font-bold mb-5">

                💡 Biggest Insight

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