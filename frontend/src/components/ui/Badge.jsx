const TONES = {
  neutral: "bg-slate-400/10 text-slate-300 border-slate-400/20",
  success: "bg-emerald-400/10 text-emerald-300 border-emerald-400/25",
  danger: "bg-rose-400/10 text-rose-300 border-rose-400/25",
  info: "bg-sky-400/10 text-sky-300 border-sky-400/25",
  violet: "bg-violet-400/10 text-violet-300 border-violet-400/25",
  warn: "bg-amber-400/10 text-amber-300 border-amber-400/25",
};

export default function Badge({ tone = "neutral", dot = true, className = "", children }) {
  return (
    <span className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-xs font-medium ${TONES[tone]} ${className}`}>
      {dot && <span className="h-1.5 w-1.5 rounded-full bg-current" aria-hidden="true" />}
      {children}
    </span>
  );
}
