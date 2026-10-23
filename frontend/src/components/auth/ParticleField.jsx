import { useEffect, useRef } from "react";
import useReducedMotion from "../../hooks/useReducedMotion";

/** Bright animated particles and connecting trails for the auth backdrop. */
export default function ParticleField({ className = "" }) {
  const canvasRef = useRef(null);
  const reduced = useReducedMotion();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return undefined;

    const ctx = canvas.getContext("2d");
    if (!ctx) return undefined;

    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const LINK_DISTANCE = 175;
    let width = 0;
    let height = 0;
    let rafId = 0;
    let lastFrame = 0;
    let particles = [];

    function buildParticles() {
      const rect = canvas.getBoundingClientRect();
      width = rect.width;
      height = rect.height;
      canvas.width = Math.max(1, Math.round(width * dpr));
      canvas.height = Math.max(1, Math.round(height * dpr));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const count = Math.min(260, Math.max(100, Math.round((width * height) / 5500)));
      particles = Array.from({ length: count }, () => ({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.65,
        vy: (Math.random() - 0.5) * 0.65,
        radius: Math.random() * 2 + 0.7,
        rgb: Math.random() < 0.7 ? "35,190,255" : "155,75,255",
        phase: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.055 + 0.025,
        glow: Math.random() * 12 + 6,
      }));
    }

    function render(animate, delta = 1) {
      ctx.clearRect(0, 0, width, height);

      for (const particle of particles) {
        if (animate) {
          particle.x += particle.vx * delta;
          particle.y += particle.vy * delta;
          particle.phase += particle.pulseSpeed * delta;

          if (particle.x < -15) particle.x = width + 15;
          if (particle.x > width + 15) particle.x = -15;
          if (particle.y < -15) particle.y = height + 15;
          if (particle.y > height + 15) particle.y = -15;
        }

        const pulse = (Math.sin(particle.phase) + 1) / 2;
        const alpha = 0.45 + pulse * 0.55;
        const radius = particle.radius * (0.85 + pulse * 0.65);

        ctx.save();
        ctx.shadowBlur = particle.glow + pulse * 14;
        ctx.shadowColor = `rgb(${particle.rgb})`;
        ctx.fillStyle = `rgba(${particle.rgb},${alpha})`;
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, radius, 0, Math.PI * 2);
        ctx.fill();

        if (pulse > 0.72) {
          ctx.shadowBlur = 15;
          ctx.fillStyle = "rgba(255,255,255,0.95)";
          ctx.beginPath();
          ctx.arc(particle.x, particle.y, radius * 0.48, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();
      }

      ctx.lineWidth = 0.8;
      for (let i = 0; i < particles.length; i += 1) {
        for (let j = i + 1; j < particles.length; j += 1) {
          const first = particles[i];
          const second = particles[j];
          const dx = first.x - second.x;
          const dy = first.y - second.y;
          const distance = Math.sqrt(dx * dx + dy * dy);

          if (distance < LINK_DISTANCE) {
            const alpha = (1 - distance / LINK_DISTANCE) * 0.42;
            ctx.strokeStyle = `rgba(65,155,255,${alpha})`;
            ctx.beginPath();
            ctx.moveTo(first.x, first.y);
            ctx.lineTo(second.x, second.y);
            ctx.stroke();
          }
        }
      }
    }

    function animationFrame(time) {
      if (document.hidden) {
        rafId = 0;
        return;
      }

      const delta = lastFrame ? Math.min((time - lastFrame) / 16.67, 2) : 1;
      lastFrame = time;
      render(true, delta);
      rafId = window.requestAnimationFrame(animationFrame);
    }

    function startAnimation() {
      window.cancelAnimationFrame(rafId);
      rafId = 0;
      lastFrame = 0;

      if (reduced) {
        render(false);
      } else if (!document.hidden) {
        rafId = window.requestAnimationFrame(animationFrame);
      }
    }

    buildParticles();
    startAnimation();

    function handleResize() {
      buildParticles();
      startAnimation();
    }

    window.addEventListener("resize", handleResize);
    document.addEventListener("visibilitychange", startAnimation);

    return () => {
      window.cancelAnimationFrame(rafId);
      window.removeEventListener("resize", handleResize);
      document.removeEventListener("visibilitychange", startAnimation);
    };
  }, [reduced]);

  return (
    <canvas
      ref={canvasRef}
      aria-hidden="true"
      className={`pointer-events-none absolute inset-0 h-full w-full ${className}`}
    />
  );
}
