export default function AlertCard({ state, trend }) {

    const alerts=[];

    if(state.Energy<60)

        alerts.push("⚡ Energy is below ideal.");

    if(trend.learning_change<0)

        alerts.push("📚 Learning has declined recently.");

    if(state.Mood>90)

        alerts.push("😊 Mood is excellent.");

    if(alerts.length===0)

        alerts.push("Everything looks stable.");

    return(

        <div className="bg-white rounded-2xl shadow-lg p-6 mt-8">

            <h2 className="text-2xl font-bold mb-5">

                ⚠ AI Alerts

            </h2>

            {

                alerts.map(

(a,i)=>

<p key={i} className="py-2">

{a}

</p>

)

            }

        </div>

    );

}