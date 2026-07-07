import { Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Dashboard from "../pages/dashboard/Dashboard";
import CurrentYou from "../pages/current/CurrentYou";
import ProtectedRoute from "../components/ProtectedRoute";
import Timeline from "../pages/timeline/Timeline";
import Memory from "../pages/memory/Memory";
import Goals from "../pages/goals/Goals";
import Simulation from "../pages/simulation/Simulation";
function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />
      <Route
        path="/current"
        element={
          <ProtectedRoute>
            <CurrentYou />
          </ProtectedRoute>
        }
      />
      <Route
        path="/timeline"
        element={<Timeline />}
      />
      <Route
        path="/memory"
        element={<Memory />}
      />
      <Route
        path="/simulation"

        element={<Simulation />}

    />
      <Route
        path="/goals"
        element={<Goals />}
      />
    </Routes>
    
    
  );
}

export default AppRoutes;
