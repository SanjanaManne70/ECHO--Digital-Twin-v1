export default function YearCard({

    year,

    activeDays,

    expanded,

    onClick,

    children,

}) {

    return (

        <div className="mb-8">

            <div

                onClick={onClick}

                className="cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-600
                text-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition"

            >

                <div className="flex justify-between items-center">

                    <div>

                        <h2 className="text-3xl font-bold">

                            📚 {year}

                        </h2>

                        <p className="opacity-90 mt-2">

                            {activeDays} Active Days

                        </p>

                    </div>

                    <div className="text-3xl">

                        {expanded ? "−" : "+"}

                    </div>

                </div>

            </div>

            {

                expanded && (

                    <div className="mt-6 ml-6 space-y-5">

                        {children}

                    </div>

                )

            }

        </div>

    );

}