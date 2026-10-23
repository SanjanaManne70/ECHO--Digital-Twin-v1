/** ECHO wordmark. The final O carries the signature glow used on the login screen. */
export default function EchoLogo({ size = "md", glow = true, className = "" }) {
  const sizes = { sm: "text-xl", md: "text-2xl", lg: "text-5xl sm:text-6xl" };
  return (
    <span
      className={`font-display font-semibold tracking-[0.22em] text-white ${sizes[size]} ${className}`}
      aria-label="ECHO"
    >
      <span aria-hidden="true">ECH</span>
      <span
        aria-hidden="true"
        className={glow ? "animate-echo-glow-o text-signal-cyan" : "text-signal-cyan"}
      >
        O
      </span>
    </span>
  );
}
