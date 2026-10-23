import Icon from "./Icon";

const TONES = {
  error: { box: "border-rose-400/30 bg-rose-500/10 text-rose-100", icon: "alert", role: "alert" },
  warn: { box: "border-amber-400/30 bg-amber-500/10 text-amber-100", icon: "alert", role: "status" },
  success: { box: "border-emerald-400/30 bg-emerald-500/10 text-emerald-100", icon: "check", role: "status" },
  info: { box: "border-sky-400/30 bg-sky-500/10 text-sky-100", icon: "info", role: "status" },
};

export default function Alert({ tone = "info", title, children, className = "" }) {
  const t = TONES[tone];
  return (
    <div role={t.role} className={`flex gap-3 rounded-xl border p-4 text-sm animate-echo-fade ${t.box} ${className}`}>
      <Icon name={t.icon} size={18} className="mt-0.5 shrink-0" />
      <div className="min-w-0">
        {title && <p className="font-semibold">{title}</p>}
        {children && <div className={title ? "mt-1 opacity-90" : ""}>{children}</div>}
      </div>
    </div>
  );
}
