import DashboardLayout from "../../components/layout/DashboardLayout";

import HealthCard from "../../components/current/HealthCard";
import LearningCard from "../../components/current/LearningCard";
import CareerCard from "../../components/current/CareerCard";
import MoodCard from "../../components/current/MoodCard";
import InsightCard from "../../components/current/InsightCard";
import PlannerWidget from "../../components/current/PlannerWidget";
import useCurrentState from "../../hooks/useCurrentState";
import useLatestAnalysis from "../../hooks/useLatestAnalysis";
function CurrentYou() {

    const {
        state,
        refresh: refreshState,
    } = useCurrentState();

    const {
        analysis,
        refresh: refreshAnalysis,
    } = useLatestAnalysis();

    if (!state) {
        return (
            <DashboardLayout>
                <h2 className="text-2xl p-10">Loading...</h2>
            </DashboardLayout>
        );
    }

    return (
        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-8">
                Current You
            </h1>

            <div className="grid grid-cols-2 gap-6">

                <HealthCard value={state.Sleep} />

                <LearningCard value={state.Learning} />

                <CareerCard />

                <MoodCard value={state.Mood} />

                <PlannerWidget />

        

             

                <InsightCard analysis={analysis} />

            </div>

        </DashboardLayout>
    );
}

export default CurrentYou;