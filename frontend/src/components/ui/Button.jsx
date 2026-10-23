import Icon from "./Icon";

const VARIANTS = {
  primary:
    "text-white bg-[length:200%_200%] bg-gradient-to-r from-signal-blue via-signal-cyan to-signal-blue " +
    "animate-echo-gradient shadow-[0_8px_24px_-10px_rgba(34,211,238,.55)] hover:shadow-[0_10px_30px_-8px_rgba(34,211,238,.7)]",
  secondary:
    "text-slate-100 glass hover:border-[var(--line-strong)] hover:bg-white/5",
  ghost: "text-slate-300 hover:text-white hover:bg-white/5",
  danger:
    "text-rose-200 bg-rose-500/10 border border-rose-400/30 hover:bg-rose-500/20",
};

const SIZES = {
  sm: "h-9 px-3.5 text-sm gap-1.5",
  md: "h-11 px-5 text-sm gap-2",
  lg: "h-12 px-6 text-base gap-2",
};

export default function Button({
  variant = "primary",
  size = "md",
  loading = false,
  icon,
  className = "",
  children,
  type = "button",
  disabled,
  ...rest
}) {
  return (
    <button
      type={type}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      className={`inline-flex items-center justify-center rounded-xl font-semibold transition duration-200
        active:scale-[.98] disabled:cursor-not-allowed disabled:opacity-55 disabled:active:scale-100
        ${VARIANTS[variant]} ${SIZES[size]} ${className}`}
      {...rest}
    >
      {loading ? (
        <span className="h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white" aria-hidden="true" />
      ) : (
        icon && <Icon name={icon} size={18} />
      )}
      {children}
    </button>
  );
}
