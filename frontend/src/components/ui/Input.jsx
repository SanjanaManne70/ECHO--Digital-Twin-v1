import { useId } from "react";

const BASE =
  "w-full rounded-xl border border-[var(--line)] bg-ink-950/60 px-4 text-[15px] text-slate-100 " +
  "placeholder:text-slate-500 transition duration-200 " +
  "hover:border-[var(--line-strong)] focus:border-signal-cyan/70 focus:bg-ink-950/90 " +
  "focus:outline-none focus:ring-4 focus:ring-signal-cyan/15 aria-[invalid=true]:border-rose-400/60";

/** Label + control + hint/error wrapper. Pass render-prop children to get id/aria props. */
export function Field({ label, hint, error, className = "", children }) {
  const id = useId();
  const describedBy = error ? `${id}-err` : hint ? `${id}-hint` : undefined;
  const control = typeof children === "function"
    ? children({ id, "aria-describedby": describedBy, "aria-invalid": error ? true : undefined })
    : children;

  return (
    <div className={className}>
      {label && (
        <label htmlFor={id} className="mb-2 block text-sm font-medium text-slate-300">
          {label}
        </label>
      )}
      {control}
      {error ? (
        <p id={`${id}-err`} className="mt-2 text-sm text-rose-300">{error}</p>
      ) : hint ? (
        <p id={`${id}-hint`} className="mt-2 text-sm text-slate-400">{hint}</p>
      ) : null}
    </div>
  );
}

export default function Input({ className = "", ...rest }) {
  return <input className={`${BASE} h-12 ${className}`} {...rest} />;
}

export function Textarea({ className = "", rows = 4, ...rest }) {
  return <textarea rows={rows} className={`${BASE} min-h-[7rem] resize-y py-3 leading-relaxed ${className}`} {...rest} />;
}
