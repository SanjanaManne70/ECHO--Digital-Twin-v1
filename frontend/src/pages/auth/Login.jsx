import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../../api/api";
import { useAuth } from "../../context/AuthContext";
import AuthShell from "../../components/auth/AuthShell";
import Input, { Field } from "../../components/ui/Input";
import PasswordInput from "../../components/auth/PasswordInput";

function MailIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" className="h-5 w-5" stroke="currentColor" strokeWidth="1.7">
      <rect x="3.5" y="5" width="17" height="14" rx="2.5" />
      <path d="m4.5 7 7.5 6 7.5-6" />
    </svg>
  );
}

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleLogin(e) {
    e.preventDefault();
    if (loading) return;

    setError("");
    setLoading(true);

    try {
      const formData = new URLSearchParams();
      formData.append("username", email.trim());
      formData.append("password", password);

      const res = await api.post("/auth/login", formData, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });

      login(res.data.access_token);
      navigate("/dashboard", { replace: true });
    } catch (err) {
      console.error("Login failed", err);
      setError(
        err?.response?.status === 401
          ? "That email and password don't match. Please try again."
          : err?.response?.data?.detail || "We couldn't sign you in. Check your connection and try again."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <AuthShell
      heading="Welcome back"
      subheading="Step back into your evolving digital twin."
    >
      <form onSubmit={handleLogin} className="space-y-5" noValidate>
        <Field label="Email address" className="auth-field">
          {({ id, ...aria }) => (
            <div className="relative">
              <span className="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-slate-400">
                <MailIcon />
              </span>
              <Input
                id={id}
                {...aria}
                type="email"
                name="email"
                autoComplete="email"
                inputMode="email"
                placeholder="you@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="auth-input pl-12"
              />
            </div>
          )}
        </Field>

        <Field label="Password" className="auth-field">
          {({ id, ...aria }) => (
            <PasswordInput
              id={id}
              {...aria}
              name="password"
              autoComplete="current-password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="auth-input pl-4 pr-16"
            />
          )}
        </Field>

        {error && (
          <div role="alert" className="auth-error">
            <span aria-hidden="true" className="mt-0.5">ⓘ</span>
            <p>{error}</p>
          </div>
        )}

        <button type="submit" disabled={loading || !email.trim() || !password} className="auth-submit">
          <span>{loading ? "Signing in…" : "Sign in"}</span>
          {loading ? (
            <span aria-hidden="true" className="auth-spinner" />
          ) : (
            <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" className="h-5 w-5 transition-transform duration-200 group-hover:translate-x-1" stroke="currentColor" strokeWidth="1.8">
              <path d="M4.5 12h14m-6-6 6 6-6 6" />
            </svg>
          )}
        </button>

        <p className="pt-1 text-center text-sm text-slate-400">
          Don&apos;t have an account?{" "}
          <Link to="/register" className="auth-link">Create account</Link>
        </p>
      </form>

      <div className="mt-7 flex items-center justify-center gap-2 text-[11px] tracking-wide text-slate-500">
        <span className="h-1.5 w-1.5 rounded-full bg-emerald-400 shadow-[0_0_10px_rgba(52,211,153,.8)]" />
        Your personal space, ready when you are
      </div>
    </AuthShell>
  );
}
