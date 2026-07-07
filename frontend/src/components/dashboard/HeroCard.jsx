export default function HeroCard({ state, user }) {

    return (

        <div className="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 text-white rounded-2xl shadow-xl p-8 mb-8">

            <h1 className="text-4xl font-bold">

                👋 Welcome {user?.full_name || "Explorer" } ..!

            </h1>

            <p className="mt-2 opacity-90">

                Your Digital Twin has been updated.

            </p>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-8">

                <Stat
                    title="😊 Mood"
                    value={state.Mood}
                />

                <Stat
                    title="📚 Learning"
                    value={state.Learning}
                />

                <Stat
                    title="⚡ Energy"
                    value={state.Energy}
                />

                <Stat
                    title="😴 Sleep"
                    value={state.Sleep}
                />

            </div>

        </div>

    );

}

function Stat({ title, value }) {

    return (

        <div className="bg-white/10 backdrop-blur rounded-xl p-4">

            <p className="opacity-80">

                {title}

            </p>

            <p className="text-3xl font-bold mt-2">

                {value == null ? "--" : Number(value).toFixed(1)}

            </p>

        </div>

    );

}