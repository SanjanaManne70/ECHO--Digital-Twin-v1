import { useState } from "react";

/** Truncates long text with an accessible Read more / Read less toggle. */
export default function ExpandableText({ text = "", limit = 220, className = "" }) {
  const [expanded, setExpanded] = useState(false);
  const shouldTrim = text.length > limit;
  const shown = expanded || !shouldTrim ? text : text.slice(0, limit).trimEnd() + "…";

  return (
    <p className={`whitespace-pre-line leading-8 text-slate-300 ${className}`}>
      {shown}
      {shouldTrim && (
        <button
          type="button"
          aria-expanded={expanded}
          onClick={() => setExpanded((v) => !v)}
          className="ml-2 font-semibold text-signal-cyan transition hover:text-white"
        >
          {expanded ? "Read less" : "Read more"}
        </button>
      )}
    </p>
  );
}
