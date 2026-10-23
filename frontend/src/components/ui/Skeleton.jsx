export function Skeleton({ className = "" }) {
  return <div className={`skeleton ${className}`} aria-hidden="true" />;
}

export function Spinner({ size = 40, className = "" }) {
  return (
    <span
      className={`inline-block animate-spin rounded-full border-2 border-white/10 border-t-signal-cyan ${className}`}
      style={{ width: size, height: size }}
      aria-hidden="true"
    />
  );
}

/** Generic page-level loading placeholder. `label` is announced to screen readers. */
export default function PageLoading({ label = "Loading…", rows = 3 }) {
  return (
    <div role="status" aria-live="polite" className="space-y-4">
      <span className="sr-only">{label}</span>
      <Skeleton className="h-10 w-64" />
      <Skeleton className="h-5 w-96 max-w-full" />
      <div className="grid gap-4 pt-4 sm:grid-cols-2 xl:grid-cols-3">
        {Array.from({ length: rows }).map((_, i) => (
          <Skeleton key={i} className="h-36" />
        ))}
      </div>
    </div>
  );
}
