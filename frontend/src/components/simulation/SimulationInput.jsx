import { useEffect, useState } from "react";

export default function SimulationInput({ onSimulate, loading = false }) {
  const [scenario, setScenario] = useState("");
  const maxLength = 600;

  useEffect(() => {
    function applyPrompt(event) {
      setScenario(event.detail || "");
    }
    window.addEventListener("echo-future-prompt", applyPrompt);
    return () => window.removeEventListener("echo-future-prompt", applyPrompt);
  }, []);

  function handleSubmit(event) {
    event.preventDefault();
    if (!scenario.trim() || loading) return;
    onSimulate(scenario.trim());
  }

  return (
    <form className="future-input-panel" onSubmit={handleSubmit}>
      <div className="future-input-topline">
        <span className="future-input-number">01</span>
        <div>
          <h3>Design your scenario</h3>
          <p>Describe one decision, habit, or change you want to explore.</p>
        </div>
        <span className="future-input-tag">YOUR INPUT</span>
      </div>
      <label className="future-sr-only" htmlFor="future-scenario">Describe your future scenario</label>
      <textarea
        id="future-scenario"
        rows={4}
        maxLength={maxLength}
        value={scenario}
        onChange={(event) => setScenario(event.target.value)}
        placeholder="What if I dedicate one hour every morning to learning, exercise, and focused work?"
        disabled={loading}
      />
      <div className="future-input-footer">
        <span className="future-input-hint"><span>↳</span> Be specific about the habit and timeframe for a more useful outlook.</span>
        <span className="future-character-count">{scenario.length} / {maxLength}</span>
      </div>
      <div className="future-submit-row">
        <span className="future-privacy-note"><span>◈</span> Scenario analyzed by your ECHO engine</span>
        <button className="future-submit-button" type="submit" disabled={!scenario.trim() || loading}>
          <span>{loading ? "Simulating…" : "Explore this future"}</span>
          <span className="future-submit-arrow">{loading ? "◌" : "↗"}</span>
        </button>
      </div>
    </form>
  );
}
