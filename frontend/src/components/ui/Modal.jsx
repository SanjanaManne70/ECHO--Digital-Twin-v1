import { useEffect, useId, useRef } from "react";
import { createPortal } from "react-dom";
import Icon from "./Icon";

const FOCUSABLE =
  'a[href],button:not([disabled]),textarea:not([disabled]),input:not([disabled]),select:not([disabled]),[tabindex]:not([tabindex="-1"])';

/** Accessible dialog: Escape/backdrop close, focus trap, focus restore, scroll lock. */
export default function Modal({ title, description, onClose, children, footer, size = "md" }) {
  const titleId = useId();
  const panelRef = useRef(null);
  const onCloseRef = useRef(onClose);

  useEffect(() => {
    onCloseRef.current = onClose;
  }, [onClose]);

  useEffect(() => {
    const previouslyFocused = document.activeElement;
    const panel = panelRef.current;
    const overflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";

    // Focus the first form control, falling back to the first focusable element.
    const first = panel?.querySelector("input,textarea,select") ?? panel?.querySelector(FOCUSABLE);
    first?.focus();

    function onKey(e) {
      if (e.key === "Escape") {
        onCloseRef.current?.();
        return;
      }
      if (e.key !== "Tab" || !panel) return;
      const items = [...panel.querySelectorAll(FOCUSABLE)];
      if (items.length === 0) return;
      const firstEl = items[0];
      const lastEl = items[items.length - 1];
      if (e.shiftKey && document.activeElement === firstEl) {
        e.preventDefault();
        lastEl.focus();
      } else if (!e.shiftKey && document.activeElement === lastEl) {
        e.preventDefault();
        firstEl.focus();
      }
    }

    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = overflow;
      previouslyFocused?.focus?.();
    };
  }, []);

  const width = size === "lg" ? "max-w-2xl" : "max-w-lg";

  return createPortal(
    <div
      className="fixed inset-0 z-[60] flex items-end justify-center bg-ink-950/70 p-0 backdrop-blur-sm animate-echo-fade sm:items-center sm:p-6"
      onMouseDown={(e) => {
        if (e.target === e.currentTarget) onClose?.();
      }}
    >
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        className={`glass flex max-h-[92vh] w-full ${width} animate-echo-pop flex-col rounded-t-2xl sm:rounded-2xl`}
      >
        <header className="flex items-start justify-between gap-4 border-b border-[var(--line)] px-6 py-5">
          <div>
            <h2 id={titleId} className="font-display text-lg font-semibold text-white">{title}</h2>
            {description && <p className="mt-1 text-sm text-slate-400">{description}</p>}
          </div>
          <button
            type="button"
            onClick={onClose}
            aria-label="Close dialog"
            className="-mr-2 grid h-9 w-9 place-items-center rounded-lg text-slate-400 transition hover:bg-white/5 hover:text-white"
          >
            <Icon name="close" size={18} />
          </button>
        </header>
        <div className="flex-1 overflow-y-auto px-6 py-5">{children}</div>
        {footer && <footer className="flex flex-wrap justify-end gap-3 border-t border-[var(--line)] px-6 py-4">{footer}</footer>}
      </div>
    </div>,
    document.body
  );
}
