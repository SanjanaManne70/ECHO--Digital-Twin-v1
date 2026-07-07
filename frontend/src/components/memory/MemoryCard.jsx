export default function MemoryCard({ memory }) {

    return (

        <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition">

            <p className="text-xs text-gray-500">

                {new Date(memory.created_at).toLocaleString()}

            </p>

            <h2 className="text-xl font-bold mt-3">

                {memory.title}

            </h2>

            <p className="mt-3 text-gray-600">

                {memory.description}

            </p>

        </div>

    );

}