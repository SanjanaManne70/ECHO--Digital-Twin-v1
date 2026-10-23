import { useState } from "react";
import Input from "../ui/Input";

export default function PasswordInput({ className = "", ...props }) {
  const [visible, setVisible] = useState(false);
  return (
    <div className="relative">
      <Input {...props} type={visible ? "text" : "password"} className={`pr-16 ${className}`} />
      <button
        type="button"
        onClick={() => setVisible((v) => !v)}
        aria-pressed={visible}
        aria-label={visible ? "Hide password" : "Show password"}
        className="absolute right-2 top-1/2 -translate-y-1/2 rounded-lg px-2.5 py-1.5 text-xs font-medium text-slate-400 transition hover:bg-white/5 hover:text-white"
      >
        {visible ? "Hide" : "Show"}
      </button>
    </div>
  );
}
