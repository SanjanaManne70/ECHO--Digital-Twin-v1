function Summary({ title, value }) {

    return (

        <div className="flex justify-between py-2 border-b">

            <span>{title}</span>

            <span className="font-bold">

                {Number(value).toFixed(1)}

            </span>

        </div>

    );

}

export default function TwinSummaryCard({ state }) {

    if (!state) return null;

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-6">

                ❤️ Twin Summary

            </h2>

            {

                Object.entries(state).map(

                    ([key, value]) => (

                        <Summary

                            key={key}

                            title={key}

                            value={value}

                        />

                    )

                )

            }

        </div>

    );

}