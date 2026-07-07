import { useState } from "react";

export default function DayCard({ day }) {

    const [expanded, setExpanded] = useState(false);

    return (

        <div className="bg-white rounded-2xl shadow-lg overflow-hidden transition-all">

            {/* Header */}

            <div

                onClick={() => setExpanded(!expanded)}

                className="cursor-pointer p-6 hover:bg-gray-50 transition"

            >

                <div className="flex justify-between items-start">

                    <div>

                        <p className="text-sm text-gray-500">

                            {new Date(day.date).toLocaleDateString(undefined, {
                                weekday: "long",
                                month: "long",
                                day: "numeric",
                            })}

                        </p>

                        <h2 className="text-2xl font-bold mt-2">

                            {day.title}

                        </h2>

                        <p className="text-gray-600 mt-3 leading-7">

                            {day.summary}

                        </p>

                    </div>

                    <div className="text-5xl">

                        {day.mood}

                    </div>

                </div>

            </div>

            {

                expanded && (

                    <div className="border-t bg-gray-50 p-6 space-y-8">

                        {/* Growth */}

                        {

                            day.growth.length > 0 && (

                                <div>

                                    <h3 className="text-xl font-bold mb-4">

                                        🌱 Growth

                                    </h3>

                                    <ul className="space-y-2">

                                        {

                                            day.growth.map((item, index) => (

                                                <li

                                                    key={index}

                                                    className="text-gray-700"

                                                >

                                                    • {item}

                                                </li>

                                            ))

                                        }

                                    </ul>

                                </div>

                            )

                        }

                        {/* Highlight */}

                        {

                            day.highlight && (

                                <div>

                                    <h3 className="text-xl font-bold mb-3">

                                        🏆 Biggest Win

                                    </h3>

                                    <p className="text-gray-700 leading-7">

                                        {day.highlight}

                                    </p>

                                </div>

                            )

                        }

                        {/* Tomorrow */}

                        {

                            day.tomorrow && (

                                <div>

                                    <h3 className="text-xl font-bold mb-3">

                                        ➡ Tomorrow's Focus

                                    </h3>

                                    <p className="text-gray-700 leading-7">

                                        {day.tomorrow}

                                    </p>

                                </div>

                            )

                        }

                    </div>

                )

            }

        </div>

    );

}