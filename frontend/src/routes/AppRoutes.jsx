
import { Routes, Route, Outlet } from "react-router-dom";

import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Dashboard from "../pages/dashboard/Dashboard";
import CurrentYou from "../pages/current/CurrentYou";
import ProtectedRoute from "../components/ProtectedRoute";
import Timeline from "../pages/timeline/Timeline";
import Memory from "../pages/memory/Memory";
import Goals from "../pages/goals/Goals";
import Simulation from "../pages/simulation/Simulation";
import ExecutionHistory from "../pages/execution-history/ExecutionHistory.jsx";
import Sidebar from "../components/layout/Sidebar";

function ProtectedLayout() {
  return (
    <ProtectedRoute>
      <Sidebar />
      <main className="min-h-screen">
        <Outlet />
      </main>
    </ProtectedRoute>
  );
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      <Route element={<ProtectedLayout />}>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/current" element={<CurrentYou />} />
        <Route path="/goals" element={<Goals />} />
        <Route path="/timeline" element={<Timeline />} />
        <Route path="/memory" element={<Memory />} />
        <Route path="/simulation" element={<Simulation />} />
        <Route path="/execution-history" element={<ExecutionHistory />} />
      </Route>
    </Routes>
  );
}

export default AppRoutes;
