import Icon from "./Icon";

export default function EmptyState({ icon = "spark", title, description, action, className = "" }) {
  return (
    <div className={`flex flex-col items-center px-6 py-14 text-center ${className}`}>
      <div className="mb-5 grid h-14 w-14 place-items-center rounded-2xl border border-[var(--line)] bg-white/[0.03] text-signal-cyan">
        <Icon name={icon} size={26} />
      </div>
      <h3 className="font-display text-lg font-semibold text-white">{title}</h3>
      {description && <p className="mt-2 max-w-md text-sm leading-relaxed text-slate-400">{description}</p>}
      {action && <div className="mt-6">{action}</div>}
    </div>
  );
}
