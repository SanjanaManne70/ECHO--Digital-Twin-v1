
import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const links = [
  { to: "/dashboard", label: "🏠 Dashboard" },
  { to: "/current", label: "👤 Current You" },
  { to: "/goals", label: "🎯 Goals" },
  { to: "/timeline", label: "🗓️ Timeline" },
  { to: "/memory", label: "🧠 Memory" },
  { to: "/simulation", label: "🤖 Simulation" },
  { to: "/execution-history", label: "📊 Execution History" },
];

function Sidebar() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate("/login", { replace: true });
  }

  return (
    <aside className="fixed left-0 top-0 z-50 flex h-screen w-64 flex-col overflow-y-auto bg-slate-900 p-6 text-white">
      {/* Brand */}
      <h1 className="text-2xl font-bold text-blue-400">
        ECHO
      </h1>

      {/* Navigation */}
      <nav className="mt-10 flex flex-col gap-4">
        {links.map(({ to, label }) => (
          <NavLink
            key={to}
            to={to}
            end
            className={({ isActive }) =>
              `rounded-lg p-3 transition-colors ${
                isActive
                  ? "bg-blue-500 text-white"
                  : "text-white hover:bg-slate-700"
              }`
            }
          >
            {label}
          </NavLink>
        ))}
      </nav>

      {/* Logout pinned to the bottom */}
      <div className="mt-auto border-t border-slate-700 pt-5">
        <button
          type="button"
          onClick={handleLogout}
          className="flex w-full items-center gap-3 rounded-lg px-3 py-3 text-left text-red-300 transition-colors hover:bg-red-500/10 hover:text-red-200 focus:outline-none focus:ring-2 focus:ring-red-400"
        >
          <span aria-hidden="true">↪</span>
          <span>Logout</span>
        </button>
      </div>
    </aside>
  );
}

export default Sidebar;
