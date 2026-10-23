const FILLS = {
  cyan: "from-signal-blue to-signal-cyan",
  mint: "from-emerald-400 to-signal-cyan",
  violet: "from-signal-blue to-signal-violet",
};

export default function ProgressBar({ value = 0, tone = "cyan", label, className = "" }) {
  const pct = Math.max(0, Math.min(100, Number(value) || 0));
  return (
    <div
      role="progressbar"
      aria-valuemin={0}
      aria-valuemax={100}
      aria-valuenow={Math.round(pct)}
      aria-label={label}
      className={`h-2 w-full overflow-hidden rounded-full bg-white/[0.07] ${className}`}
    >
      <div
        className={`fill-grow h-full rounded-full bg-gradient-to-r ${FILLS[tone]}`}
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}
