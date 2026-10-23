import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import SimulationInput from "../../components/simulation/SimulationInput";
import SimulationResult from "../../components/simulation/SimulationResult";
import api from "../../api/api";
import "../../styles/echo-pages.css";

function FutureIllustration() {
  return (
    <div className="future-illustration" aria-hidden="true">
      <div className="future-nebula future-nebula-one" />
      <div className="future-nebula future-nebula-two" />
      <div className="future-starfield" />
      <div className="future-orbit future-orbit-one" />
      <div className="future-orbit future-orbit-two" />
      <div className="future-orbit future-orbit-three" />
      <div className="future-planet">
        <div className="future-planet-glow" />
        <div className="future-planet-land" />
        <div className="future-planet-ring" />
      </div>
      <div className="future-moon"><span /></div>
      <div className="future-satellite"><i /><b /></div>
      <div className="future-signal future-signal-one" />
      <div className="future-signal future-signal-two" />
      <div className="future-art-label future-label-top">POSSIBLE TIMELINE <span>↗</span></div>
      <div className="future-art-label future-label-bottom"><span className="future-live-dot" /> FUTURE STATE // 030</div>
    </div>
  );
}

const examples = [
  { icon: "⚡", label: "Daily coding", prompt: "What might happen if I solve 5 DSA problems every day for the next 30 days?" },
  { icon: "🧠", label: "Focused learning", prompt: "What might happen if I study a new technical topic for 90 focused minutes every day for 30 days?" },
  { icon: "🌱", label: "Healthier routine", prompt: "What might happen if I follow a consistent sleep schedule, take short walks, and stay hydrated for 30 days?" },
];

export default function Simulation() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function runSimulation(scenario) {
    if (!scenario.trim() || loading) return;
    try {
      setLoading(true);
      setResult(null);
      const token = localStorage.getItem("token");
      const response = await api.post(
        "/simulation/",
        { scenario },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setResult(response.data);
    } catch (err) {
      console.error("ECHO simulation failed:", err);
      alert("Simulation failed. Please check that the backend is running and try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <DashboardLayout>
      <main className="echo-upgrade echo-simulation future-lab">
        <section className="future-hero">
          <div className="future-hero-copy">
            <div className="future-kicker"><span className="future-kicker-line" /> ECHO INTELLIGENCE / 01</div>
            <div className="future-status"><span className="future-live-dot" /> 30-DAY SCENARIO ENGINE</div>
            <h1>Meet the <span>you</span><br />that comes next.</h1>
            <p className="future-hero-description">
              Every choice creates a different trajectory. Explore a possible future shaped by the habits you build today.
            </p>
            <div className="future-hero-meta">
              <span><b>30</b> DAY OUTLOOK</span>
              <i />
              <span><b>AI</b> POWERED SIMULATION</span>
            </div>
          </div>
          <FutureIllustration />
          <div className="future-hero-index">01 <span>/</span> FUTURE LAB</div>
        </section>

        <section className="future-workspace">
          <div className="future-section-heading">
            <div>
              <p className="future-section-kicker">DEFINE YOUR NEXT CHAPTER</p>
              <h2>What if you tried…</h2>
              <p>Choose a starting point or describe your own scenario.</p>
            </div>
            <div className="future-step"><span>STEP</span><b>01</b><i /> <span>02 · SIMULATE</span></div>
          </div>

          <div className="future-prompt-grid">
            {examples.map((example) => (
              <button
                type="button"
                className="future-prompt-card"
                key={example.label}
                onClick={() => window.dispatchEvent(new CustomEvent("echo-future-prompt", { detail: example.prompt }))}
                disabled={loading}
              >
                <span className="future-prompt-icon">{example.icon}</span>
                <span className="future-prompt-label">{example.label}</span>
                <span className="future-prompt-arrow">↗</span>
              </button>
            ))}
          </div>

          <SimulationInput onSimulate={runSimulation} loading={loading} />

          {loading && (
            <section className="future-processing" aria-live="polite">
              <div className="future-processing-art">
                <div className="future-processing-orbit"><span /></div>
                <div className="future-processing-core">E</div>
              </div>
              <div>
                <p className="future-section-kicker">COMPUTING POSSIBLE OUTCOMES</p>
                <h2>Mapping your next 30 days<span className="future-ellipsis">…</span></h2>
                <p>ECHO is evaluating your scenario and preparing a possible outlook from your Digital Twin context.</p>
                <div className="future-progress-track"><span /></div>
              </div>
              <span className="future-processing-code">ENGINE / ACTIVE</span>
            </section>
          )}

          {!loading && result && <SimulationResult result={result} />}

          {!loading && !result && (
            <section className="future-empty">
              <div className="future-empty-art">
                <div className="future-empty-orbit future-empty-orbit-a" />
                <div className="future-empty-orbit future-empty-orbit-b" />
                <div className="future-empty-star">✦</div>
              </div>
              <div className="future-empty-copy">
                <p className="future-section-kicker">YOUR NEXT TIMELINE IS UNWRITTEN</p>
                <h2>A possibility is waiting.</h2>
                <p>Run your first simulation to explore potential benefits, risks, life-domain changes and recommendations for the road ahead.</p>
              </div>
              <div className="future-empty-index">FUTURE / 000</div>
            </section>
          )}
        </section>
        <footer className="future-footnote"><span>✳</span> Simulations are AI-generated possibilities, not guarantees or professional advice.</footer>
      </main>
    </DashboardLayout>
  );
}
