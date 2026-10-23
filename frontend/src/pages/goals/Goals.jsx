import DashboardLayout from "../../components/layout/DashboardLayout";
import GoalCard from "../../components/goals/GoalCard";
import GoalModal from "../../components/goals/GoalModal";
import useGoals from "../../hooks/useGoals";
import { deleteGoal } from "../../services/goalService";
import "../../styles/echo-pages.css";

export default function Goals() {
  const { goals, loading, refresh } = useGoals();

  async function handleDelete(id) {
    await deleteGoal(id);
    refresh();
  }

  if (loading) {
    return (
      <DashboardLayout>
        <div className="echo-upgrade echo-goals">
          <p className="echo-eyebrow">PERSONAL ROADMAP</p>
          <h1 className="echo-page-title">Loading your goals...</h1>
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="echo-upgrade echo-goals">
        <header className="echo-page-header echo-hero-panel">
          <div>
            <p className="echo-eyebrow">INTENTIONS INTO ACTION</p>
            <h1>🎯 Goals</h1>
            <p>Your AI-powered roadmap, one meaningful step at a time.</p>
          </div>
          <span className="echo-orb-icon" aria-hidden="true">✦</span>
        </header>

        <div className="echo-goals-workspace">
          <section className="echo-goals-list-panel" aria-labelledby="goals-list-title">
            <div className="echo-goals-section-heading">
              <div>
                <p className="echo-eyebrow">YOUR ROADMAP</p>
                <h2 id="goals-list-title">{goals.length ? "Goals in progress" : "Your next chapter starts here"}</h2>
              </div>
              <span className="echo-goals-count">{goals.length} {goals.length === 1 ? "goal" : "goals"}</span>
            </div>

            {goals.length === 0 ? (
              <div className="echo-empty-state echo-goals-empty">
                <span className="echo-goals-empty-icon" aria-hidden="true">🎯</span>
                <h3>No goals yet</h3>
                <p>Create your first goal using the form. It will appear here so you can track its progress.</p>
              </div>
            ) : (
              <div className="echo-goals-cards">
                {goals.map((goal) => (
                  <GoalCard key={goal.id} goal={goal} onDelete={handleDelete} />
                ))}
              </div>
            )}
          </section>

          <aside className="echo-goals-create-panel">
            <div className="echo-goals-create-intro">
              <span className="echo-goals-create-icon" aria-hidden="true">＋</span>
              <div>
                <p className="echo-eyebrow">MAKE IT REAL</p>
                <h2>Add a goal</h2>
                <p>Turn an intention into a clear next step.</p>
              </div>
            </div>
            <GoalModal onSaved={refresh} />
          </aside>
        </div>
      </div>
    </DashboardLayout>
  );
}
