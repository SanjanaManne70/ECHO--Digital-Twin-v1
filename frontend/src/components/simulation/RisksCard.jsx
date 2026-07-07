export default function RisksCard({ risks }) {

    if (!risks.length) return null;

    return (

        <div className="bg-red-50 border border-red-200 rounded-2xl p-6">

            <h2 className="text-2xl font-bold text-red-700 mb-5">

                ⚠ Possible Risks

            </h2>

            <div className="space-y-3">

                {

                    risks.map((r, i) => (

                        <div

                            key={i}

                            className="bg-white rounded-lg p-3 shadow-sm"

                        >

                            ⚠ {r}

                        </div>

                    ))

                }

            </div>

        </div>

    );

}