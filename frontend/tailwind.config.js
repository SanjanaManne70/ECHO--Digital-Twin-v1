/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Original tokens preserved
        primary: "#2563EB",
        secondary: "#0F172A",
        accent: "#38BDF8",
        background: "#F8FAFC",
        // ECHO V2 midnight scale
        ink: {
          950: "#04060d",
          900: "#070b16",
          850: "#0a1020",
          800: "#0d1526",
          700: "#141e35",
          600: "#1c2946",
        },
        signal: {
          cyan: "#22d3ee",
          blue: "#3b82f6",
          violet: "#8b5cf6",
          mint: "#34d399",
          amber: "#fbbf24",
          rose: "#fb7185",
        },
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["Sora", "Inter", "ui-sans-serif", "system-ui", "sans-serif"],
      },
      boxShadow: {
        glow: "0 0 0 1px rgba(34,211,238,.25), 0 0 32px -6px rgba(34,211,238,.35)",
        "glow-violet": "0 0 0 1px rgba(139,92,246,.3), 0 0 32px -6px rgba(139,92,246,.35)",
        panel: "0 1px 0 0 rgba(255,255,255,.04) inset, 0 18px 40px -24px rgba(0,0,0,.7)",
      },
      keyframes: {
        "echo-rise": {
          from: { opacity: "0", transform: "translateY(10px)" },
          to: { opacity: "1", transform: "translateY(0)" },
        },
        "echo-fade": {
          from: { opacity: "0" },
          to: { opacity: "1" },
        },
        "echo-pop": {
          from: { opacity: "0", transform: "scale(.96) translateY(8px)" },
          to: { opacity: "1", transform: "scale(1) translateY(0)" },
        },
        "echo-sweep": {
          "0%": { transform: "translateY(-120%)" },
          "100%": { transform: "translateY(220%)" },
        },
        "echo-breathe": {
          "0%,100%": { opacity: ".72", transform: "scale(1)" },
          "50%": { opacity: "1", transform: "scale(1.015)" },
        },
        "echo-gradient": {
          "0%,100%": { backgroundPosition: "0% 50%" },
          "50%": { backgroundPosition: "100% 50%" },
        },
        "echo-light-up": {
          "0%,100%": { opacity: ".35", textShadow: "none" },
          "50%": { opacity: "1", textShadow: "0 0 14px rgba(34,211,238,.8)" },
        },
        "echo-glow-o": {
          "0%,100%": { textShadow: "0 0 10px rgba(34,211,238,.55), 0 0 26px rgba(59,130,246,.35)" },
          "50%": { textShadow: "0 0 18px rgba(34,211,238,.95), 0 0 44px rgba(139,92,246,.6)" },
        },
        "echo-shimmer": {
          from: { backgroundPosition: "200% 0" },
          to: { backgroundPosition: "-200% 0" },
        },
      },
      animation: {
        "echo-rise": "echo-rise .5s cubic-bezier(.22,1,.36,1) both",
        "echo-fade": "echo-fade .4s ease both",
        "echo-pop": "echo-pop .28s cubic-bezier(.22,1,.36,1) both",
        "echo-sweep": "echo-sweep 7s linear infinite",
        "echo-breathe": "echo-breathe 6s ease-in-out infinite",
        "echo-gradient": "echo-gradient 8s ease infinite",
        "echo-light-up": "echo-light-up 6s ease-in-out infinite",
        "echo-glow-o": "echo-glow-o 4.5s ease-in-out infinite",
        "echo-shimmer": "echo-shimmer 2.2s linear infinite",
      },
    },
  },
  plugins: [],
}
