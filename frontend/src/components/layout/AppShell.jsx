import { useState } from "react";
import { Outlet, useLocation } from "react-router-dom";
import Sidebar from "./Sidebar";
import EchoLogo from "../brand/EchoLogo";
import Icon from "../ui/Icon";

/**
 * Single authenticated shell: sidebar (drawer on mobile), top bar on small
 * screens, and a keyed content area so each route gets one calm entrance.
 * Sidebar is mounted exactly once here.
 */
export default function AppShell() {
  const [navState, setNavState] = useState({ open: false, path: null });
  const location = useLocation();

  // Drawer is "open" only for the route it was opened on, so navigating closes it
  // without an effect.
  const navOpen = navState.open && navState.path === location.pathname;
  const setNavOpen = (open) => setNavState({ open, path: location.pathname });

  return (
    <div className="echo-backdrop min-h-dvh">
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[70] focus:rounded-lg focus:bg-ink-800 focus:px-4 focus:py-2 focus:text-white"
      >
        Skip to content
      </a>

      <Sidebar open={navOpen} onClose={() => setNavOpen(false)} />

      <div className="md:pl-64">
        <div className="sticky top-0 z-30 flex h-14 items-center justify-between border-b border-[var(--line)] bg-ink-950/85 px-4 backdrop-blur-xl md:hidden">
          <button
            type="button"
            onClick={() => setNavOpen(true)}
            aria-label="Open navigation"
            aria-expanded={navOpen}
            aria-controls="primary-navigation"
            className="-ml-2 grid h-10 w-10 place-items-center rounded-lg text-slate-300 hover:bg-white/5"
          >
            <Icon name="menu" size={22} />
          </button>
          <EchoLogo size="sm" />
          <span className="w-8" aria-hidden="true" />
        </div>

        <main id="main" tabIndex={-1} className="min-h-dvh outline-none md:min-h-screen">
          <div key={location.pathname} className="page-enter">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  );
}
