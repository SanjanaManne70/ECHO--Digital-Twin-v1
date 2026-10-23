import DashboardLayout from "../../components/layout/DashboardLayout";

import HealthCard from "../../components/current/HealthCard";
import LearningCard from "../../components/current/LearningCard";
import CareerCard from "../../components/current/CareerCard";
import MoodCard from "../../components/current/MoodCard";
import InsightCard from "../../components/current/InsightCard";
import PlannerWidget from "../../components/current/PlannerWidget";
import useCurrentState from "../../hooks/useCurrentState";
import useLatestAnalysis from "../../hooks/useLatestAnalysis";
import "../../styles/echo-pages.css";
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
                <div className="echo-upgrade echo-current"><h2 className="text-2xl p-10">Loading your digital twin...</h2></div>
            </DashboardLayout>
        );
    }

    return (
        <DashboardLayout>
          <div className="echo-upgrade echo-current">
            <header className="echo-page-header">
              <div><p className="echo-eyebrow">YOUR DIGITAL TWIN · LIVE SNAPSHOT</p><h1>Current You</h1><p>A living snapshot of the patterns shaping you right now.</p></div>
              <span className="echo-live-pill"><i /> Twin context loaded</span>
            </header>
            <div className="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-3 echo-card-grid">

                <HealthCard value={state.Sleep} />

                <LearningCard value={state.Learning} />

                <CareerCard />

                <MoodCard value={state.Mood} />

                <PlannerWidget />

        

             

                <InsightCard analysis={analysis} />

            </div>
          </div>
        </DashboardLayout>
    );
}

export default CurrentYou;