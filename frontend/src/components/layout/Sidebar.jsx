import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const links = [
  { to: "/dashboard", label: "Dashboard", icon: "⌂" },
  { to: "/current", label: "Current You", icon: "♟" },
  { to: "/goals", label: "Goals", icon: "◎" },
  { to: "/timeline", label: "Timeline", icon: "▦" },
  { to: "/memory", label: "Memory", icon: "❋" },
  { to: "/simulation", label: "Simulation", icon: "▣" },
  { to: "/execution-history", label: "Execution History", icon: "▥" },
];

function Sidebar() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate("/login", { replace: true });
  }

  return (
    <aside className="echo-sidebar fixed left-0 top-0 z-50 flex h-screen w-64 flex-col overflow-y-auto p-4 text-white">
      <div className="echo-sidebar-brand">
        <div className="echo-sidebar-wordmark">ECH<span>O</span></div>
        <p>YOUR DIGITAL TWIN</p>
      </div>

      <nav id="primary-navigation" className="echo-sidebar-nav mt-8 flex flex-col gap-2">
        {links.map(({ to, label, icon }) => (
          <NavLink
            key={to}
            to={to}
            end
            className={({ isActive }) =>
              `echo-sidebar-link ${isActive ? "is-active" : ""}`
            }
          >
            <span className="echo-sidebar-icon" aria-hidden="true">{icon}</span>
            <span>{label}</span>
          </NavLink>
        ))}
      </nav>

      <div className="echo-sidebar-logout mt-auto border-t pt-4">
        <button type="button" onClick={handleLogout} className="echo-logout-button">
          <span aria-hidden="true">↪</span><span>Logout</span>
        </button>
      </div>
    </aside>
  );
}

export default Sidebar;
