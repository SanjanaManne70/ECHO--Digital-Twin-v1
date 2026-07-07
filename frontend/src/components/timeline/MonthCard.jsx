export default function MonthCard({

    month,

    activeDays,

    expanded,

    onClick,

    children,

}) {

    return (

        <div>

            <div

                onClick={onClick}

                className="cursor-pointer bg-white rounded-2xl shadow-lg p-5
                border-l-8 border-indigo-500 hover:shadow-xl transition"

            >

                <div className="flex justify-between">

                    <div>

                        <h3 className="text-2xl font-bold">

                            🌞 {month}

                        </h3>

                        <p className="text-gray-500 mt-2">

                            {activeDays} Recorded Days

                        </p>

                    </div>

                    <div className="text-2xl">

                        {expanded ? "−" : "+"}

                    </div>

                </div>

            </div>

            {

                expanded && (

                    <div className="ml-8 mt-5 space-y-4">

                        {children}

                    </div>

                )

            }

        </div>

    );

}