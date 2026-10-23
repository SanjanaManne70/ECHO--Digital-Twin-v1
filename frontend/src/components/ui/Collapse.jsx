/** Animated expand/collapse. Collapsed content is inert (not focusable, hidden from AT). */
export default function Collapse({ open, children, className = "" }) {
  return (
    <div className={`echo-collapse ${className}`} data-open={open ? "true" : "false"} inert={!open}>
      <div className="echo-collapse-inner">{children}</div>
    </div>
  );
}
