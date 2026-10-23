import { useEffect, useRef, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import ReflectionCard from "../../components/dashboard/ReflectionCard";
import InsightDashboardCard from "../../components/dashboard/InsightDashboardCard";
import useDashboard from "../../hooks/useDashboard";
import twinPortrait from "../../assets/login-twin.jpg";

const metrics = [
  { key: "Mood", icon: "☻", tone: "mood" },
  { key: "Learning", icon: "▥", tone: "learning" },
  { key: "Energy", icon: "ϟ", tone: "energy" },
  { key: "Sleep", icon: "☾", tone: "sleep" },
];

function portraitStorageKey(user) {
  const identity = user?.id ?? user?.user_id ?? user?.email ?? user?.full_name ?? "default";
  return `echo-twin-portrait:${String(identity).toLowerCase()}`;
}

function resizePortrait(file) {
  return new Promise((resolve, reject) => {
    const image = new Image();
    const objectUrl = URL.createObjectURL(file);
    image.onload = () => {
      const maxDimension = 1200;
      const scale = Math.min(1, maxDimension / Math.max(image.naturalWidth, image.naturalHeight));
      const canvas = document.createElement("canvas");
      canvas.width = Math.max(1, Math.round(image.naturalWidth * scale));
      canvas.height = Math.max(1, Math.round(image.naturalHeight * scale));
      const context = canvas.getContext("2d");
      if (!context) {
        URL.revokeObjectURL(objectUrl);
        reject(new Error("Your browser could not process this image."));
        return;
      }
      context.drawImage(image, 0, 0, canvas.width, canvas.height);
      URL.revokeObjectURL(objectUrl);
      resolve(canvas.toDataURL("image/jpeg", 0.86));
    };
    image.onerror = () => {
      URL.revokeObjectURL(objectUrl);
      reject(new Error("That image could not be opened. Please choose another file."));
    };
    image.src = objectUrl;
  });
}

export default function Dashboard() {
  const { loading, state, reflection, insight, user } = useDashboard();
  const fileInputRef = useRef(null);
  const [customPortrait, setCustomPortrait] = useState("");
  const [portraitError, setPortraitError] = useState("");
  const [pendingPortrait, setPendingPortrait] = useState("");
  const [isEditingPortrait, setIsEditingPortrait] = useState(false);

  const storageKey = portraitStorageKey(user);

  useEffect(() => {
    setCustomPortrait(localStorage.getItem(storageKey) || "");
  }, [storageKey]);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="echo-dashboard-loading">
          <span className="echo-loading-orb" />
          <p>Waking up your digital twin…</p>
        </div>
      </DashboardLayout>
    );
  }

  const safeState = state || {};
  const displayName = user?.full_name?.trim()?.split(" ")[0] || "Explorer";

  async function handlePortraitSelected(event) {
    const file = event.target.files?.[0];
    event.target.value = "";
    if (!file) return;

    setPortraitError("");
    if (!file.type.startsWith("image/")) {
      setPortraitError("Choose an image file (JPG, PNG, or WEBP).");
      return;
    }
    if (file.size > 12 * 1024 * 1024) {
      setPortraitError("Choose an image smaller than 12 MB.");
      return;
    }

    try {
      const resized = await resizePortrait(file);
      setPendingPortrait(resized);
      setIsEditingPortrait(true);
    } catch (error) {
      setPortraitError(error.message || "Could not process that image.");
    }
  }

  function applyPortrait() {
    try {
      localStorage.setItem(storageKey, pendingPortrait);
      setCustomPortrait(pendingPortrait);
      setPendingPortrait("");
      setIsEditingPortrait(false);
      setPortraitError("");
    } catch {
      setPortraitError("Your browser could not save this image. Try a smaller image.");
    }
  }

  function cancelPortraitEdit() {
    setPendingPortrait("");
    setIsEditingPortrait(false);
    setPortraitError("");
  }

  function resetPortrait() {
    localStorage.removeItem(storageKey);
    setCustomPortrait("");
    setPendingPortrait("");
    setIsEditingPortrait(false);
    setPortraitError("");
  }

  return (
    <DashboardLayout>
      <div className="echo-dashboard">
        <header className="echo-dashboard-greeting">
          <div>
            <p className="echo-hello">HELLOOO,</p>
            <h1>{displayName} <span aria-hidden="true">👋</span></h1>
            <p className="echo-greeting-subtitle">Your Digital Twin has been updated.</p>
          </div>
          <div className="echo-live-indicator"><span /> DIGITAL TWIN ACTIVE</div>
        </header>

        <section className="echo-twin-stage" aria-label="Your digital twin and current metrics">
          <div className="echo-nebula" aria-hidden="true" />
          <div className="echo-orbit echo-orbit-one" aria-hidden="true" />
          <div className="echo-orbit echo-orbit-two" aria-hidden="true" />
          <div className="echo-orbit echo-orbit-three" aria-hidden="true" />
          <div className="echo-portrait-glow" aria-hidden="true" />
          <div className={`echo-portrait${customPortrait ? " echo-portrait-custom" : ""}`}>
            <img
              src={customPortrait || twinPortrait}
              alt={customPortrait ? "Your chosen digital-twin portrait" : "Holographic female digital twin"}
              className={customPortrait ? "echo-custom-portrait-image" : ""}
            />
          </div>

          <div className="echo-portrait-actions">
            <button type="button" onClick={() => fileInputRef.current?.click()}>
              {customPortrait ? "Change portrait" : "Use your own portrait"}
            </button>
            {customPortrait && (
              <button type="button" className="echo-portrait-reset" onClick={resetPortrait}>
                Reset
              </button>
            )}
            <input
              ref={fileInputRef}
              className="echo-portrait-file-input"
              type="file"
              accept="image/png,image/jpeg,image/webp,image/avif"
              onChange={handlePortraitSelected}
              aria-label="Choose your digital twin portrait"
            />
          </div>

          <div className="echo-twin-plinth" aria-label="Digital you">
            <span className="echo-plinth-title">DIGITAL YOU</span>
          </div>

          {metrics.map(({ key, icon, tone }) => (
            <div key={key} className={`echo-metric echo-metric-${tone}`}>
              <span className="echo-metric-ring" aria-hidden="true" />
              <span className="echo-metric-icon" aria-hidden="true">{icon}</span>
              <span className="echo-metric-name">{key}</span>
              <strong>{safeState[key] == null ? "--" : Number(safeState[key]).toFixed(1)}</strong>
            </div>
          ))}

          <span className="echo-star echo-star-a" aria-hidden="true" />
          <span className="echo-star echo-star-b" aria-hidden="true" />
          <span className="echo-star echo-star-c" aria-hidden="true" />
          <span className="echo-star echo-star-d" aria-hidden="true" />
        </section>

        {portraitError && <p className="echo-portrait-error" role="alert">{portraitError}</p>}

        {isEditingPortrait && (
          <div className="echo-portrait-modal-backdrop" role="presentation">
            <section className="echo-portrait-modal" role="dialog" aria-modal="true" aria-labelledby="echo-portrait-modal-title">
              <h2 id="echo-portrait-modal-title">Preview your Digital Twin</h2>
              <p>For the best fit, choose a clear, straight-facing portrait with your face centered.</p>
              <div className="echo-portrait-preview">
                <img src={pendingPortrait} alt="Preview of the portrait you selected" />
              </div>
              <div className="echo-portrait-modal-actions">
                <button type="button" className="echo-portrait-cancel" onClick={cancelPortraitEdit}>Cancel</button>
                <button type="button" className="echo-portrait-apply" onClick={applyPortrait}>Use this portrait</button>
              </div>
            </section>
          </div>
        )}

        <section className="echo-dashboard-cards" aria-label="Your latest reflection and insight">
          <div className="echo-dashboard-card echo-reflection-wrap">
            <ReflectionCard reflection={reflection?.reflection} />
          </div>
          <div className="echo-dashboard-card echo-insight-wrap">
            <InsightDashboardCard insight={insight} />
          </div>
        </section>
      </div>
    </DashboardLayout>
  );
}
