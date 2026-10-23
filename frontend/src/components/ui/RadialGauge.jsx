import { useId } from "react";

/** Circular 0-100 gauge. Renders "—" when value is missing; never invents a number. */
export default function RadialGauge({ value, label, tone = "cyan", size = 132 }) {
  const id = useId().replace(/[^a-zA-Z0-9_-]/g, "");
  const has = value != null && Number.isFinite(Number(value));
  const pct = has ? Math.max(0, Math.min(100, Number(value))) : 0;
  const r = 52;
  const c = 2 * Math.PI * r;

  const stops = {
    cyan: ["#3b82f6", "#22d3ee"],
    violet: ["#3b82f6", "#a78bfa"],
    mint: ["#22d3ee", "#34d399"],
    amber: ["#a78bfa", "#fbbf24"],
  }[tone];

  return (
    <div
      role="img"
      aria-label={has ? `${label}: ${Number(value).toFixed(1)} out of 100` : `${label}: no data`}
      className="relative grid place-items-center"
      style={{ width: size, height: size }}
    >
      <svg viewBox="0 0 120 120" width={size} height={size} className="-rotate-90">
        <defs>
          <linearGradient id={id} x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor={stops[0]} />
            <stop offset="100%" stopColor={stops[1]} />
          </linearGradient>
        </defs>
        <circle cx="60" cy="60" r={r} fill="none" stroke="rgba(148,163,184,.12)" strokeWidth="9" />
        <circle
          cx="60"
          cy="60"
          r={r}
          fill="none"
          stroke={`url(#${id})`}
          strokeWidth="9"
          strokeLinecap="round"
          strokeDasharray={c}
          strokeDashoffset={c * (1 - pct / 100)}
          style={{ transition: "stroke-dashoffset 1s cubic-bezier(.22,1,.36,1)" }}
        />
      </svg>
      <div className="absolute inset-0 grid place-items-center text-center">
        <div>
          <p className="font-display text-2xl font-semibold text-white">{has ? Number(value).toFixed(1) : "—"}</p>
        </div>
      </div>
    </div>
  );
}
