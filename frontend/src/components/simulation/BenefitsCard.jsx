export default function BenefitsCard({ benefits }) {

    if (!benefits.length) return null;

    return (

        <div className="bg-green-50 border border-green-200 rounded-2xl p-6">

            <h2 className="text-2xl font-bold text-green-700 mb-5">

                ✅ Benefits

            </h2>

            <div className="space-y-3">

                {

                    benefits.map((b, i) => (

                        <div

                            key={i}

                            className="bg-white rounded-lg p-3 shadow-sm"

                        >

                            ✔ {b}

                        </div>

                    ))

                }

            </div>

        </div>

    );

}