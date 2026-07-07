import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api/api";
import { useAuth } from "../../context/AuthContext";
export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleLogin(e) {
    e.preventDefault();

    try {
      const formData = new URLSearchParams();

      formData.append("username", email);
      formData.append("password", password);

      const res = await api.post(
        "/auth/login",
        formData,
        {
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded",
          },
        }
      );

      login(res.data.access_token);

      navigate("/dashboard");

    } catch (err) {
      console.error(err);
      alert("Invalid email or password");
    }
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-slate-100">
      <form
        onSubmit={handleLogin}
        className="bg-white shadow-xl rounded-xl p-8 w-96"
      >
        <h1 className="text-3xl font-bold text-center mb-6">
          ECHO Login
        </h1>

        <input
          className="border w-full p-3 rounded mb-4"
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="border w-full p-3 rounded mb-6"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
  className="bg-blue-600 hover:bg-blue-700 text-white w-full p-3 rounded"
>
  Login
</button>

<div className="mt-6 text-center">
  <p className="text-gray-600">
    Don't have an account?{" "}
    <button
      type="button"
      onClick={() => navigate("/register")}
      className="text-blue-600 font-semibold hover:underline"
    >
      Register here
    </button>
  </p>
</div>
      </form>
    </div>
  );
}