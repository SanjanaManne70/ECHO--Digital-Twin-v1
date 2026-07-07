import { NavLink } from "react-router-dom";

function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-slate-900 text-white p-6">
      <h1 className="text-2xl font-bold text-blue-400">
        ECHO
      </h1>

      <nav className="mt-10 flex flex-col gap-4">

        <NavLink
          to="/dashboard"
          className={({ isActive }) =>
            `p-2 rounded ${
              isActive
                ? "bg-blue-500 text-white"
                : "hover:bg-slate-700"
            }`
          }
        >
          🏠 Dashboard
        </NavLink>

        <NavLink
          to="/current"
          className={({ isActive }) =>
            `p-2 rounded ${
              isActive
                ? "bg-blue-500 text-white"
                : "hover:bg-slate-700"
            }`
          }
        >
          👤 Current You
        </NavLink>

        <NavLink
          to="/goals"
          className={({ isActive }) =>
            `p-2 rounded ${
              isActive
                ? "bg-blue-500 text-white"
                : "hover:bg-slate-700"
            }`
          }
        >
          🎯 Goals
        </NavLink>

        <NavLink
          to="/timeline"
          className={({ isActive }) =>
            `p-2 rounded ${
              isActive
                ? "bg-blue-500 text-white"
                : "hover:bg-slate-700"
            }`
          }
        >
          📅 Timeline
        </NavLink>

        <NavLink
          to="/memory"
          className={({ isActive }) =>
            `p-2 rounded ${
              isActive
                ? "bg-blue-500 text-white"
                : "hover:bg-slate-700"
            }`
          }
        >
          🧠 Memory
        </NavLink>

        <NavLink
          to="/simulation"
          className={({ isActive }) =>
            `p-2 rounded ${
              isActive
                ? "bg-blue-500 text-white"
                : "hover:bg-slate-700"
            }`
          }
        >
          🤖 Simulation
        </NavLink>

      </nav>
    </aside>
  );
}

export default Sidebar;