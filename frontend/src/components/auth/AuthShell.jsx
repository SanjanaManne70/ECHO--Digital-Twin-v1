import ParticleField from "./ParticleField";
import TwinPortrait from "./TwinPortrait";
import EchoLogo from "../brand/EchoLogo";

/** Cinematic split-screen brand layout shared by the authentication screens. */
export default function AuthShell({ heading, subheading, children }) {
  return (
    <main className="auth-scene relative isolate min-h-dvh overflow-hidden bg-ink-950 text-white">
      <div aria-hidden="true" className="auth-ambient absolute inset-0 -z-20" />
      <div aria-hidden="true" className="auth-vignette pointer-events-none absolute inset-0 -z-10" />
      <ParticleField className="auth-particle-canvas z-0 opacity-100" />

      <div className="auth-grid relative mx-auto grid min-h-dvh w-full max-w-[1920px] lg:grid-cols-[1.18fr_.82fr]">
        <section aria-label="The ECHO digital twin" className="auth-art relative order-1 flex min-h-[340px] items-center justify-center px-0 pb-0 pt-2 sm:min-h-[440px] sm:px-1 lg:min-h-dvh lg:px-0 lg:py-2">
          <div aria-hidden="true" className="auth-art-orb" />
          <TwinPortrait className="auth-twin relative z-10 h-auto w-full max-h-none sm:max-h-none lg:max-h-none" />
          <div aria-hidden="true" className="auth-art-caption hidden lg:block">
            <span className="auth-caption-line" />
            <span>MEMORY · PATTERN · POSSIBILITY</span>
          </div>
        </section>

        <section className="auth-panel relative order-2 flex items-center justify-center px-5 pb-10 pt-4 sm:px-8 lg:min-h-dvh lg:px-8 lg:py-8 xl:px-12">
          <div className="auth-panel-glow" aria-hidden="true" />
          <div className="auth-content stagger relative z-10 w-full max-w-[500px]">
            <header style={{ "--i": 1 }} className="mb-6 text-center lg:mb-7">
              <div className="mb-1 flex justify-center lg:justify-start">
                <EchoLogo size="lg" className="auth-wordmark" />
              </div>
              <p className="auth-brand-subtitle mt-3 text-xs font-semibold uppercase text-signal-cyan sm:text-sm">
                Your digital twin
              </p>
              <p className="auth-brand-tagline mx-auto mt-4 max-w-[370px] text-base leading-7 text-slate-300 sm:text-lg lg:mx-0">
                “Your experiences today,<br /> <span className="text-slate-200"><strong>a better you</strong> tomorrow.”</span>
              </p>
            </header>

            <div style={{ "--i": 2 }} className="auth-card glass relative rounded-[28px] p-6 sm:p-8 lg:p-9">
              <div aria-hidden="true" className="auth-card-edge" />
              <div className="relative z-10">
                <div className="mb-6">
                  <h1 className="font-display text-2xl font-semibold tracking-tight text-white sm:text-[28px]">{heading}</h1>
                  {subheading && <p className="mt-2 text-base leading-6 text-slate-300">{subheading}</p>}
                </div>
                {children}
              </div>
            </div>

            <p className="mt-6 text-center text-[11px] text-slate-600">
              ECHO V2 <span className="mx-2 text-slate-700">•</span> A more personal kind of intelligence
            </p>
          </div>
        </section>
      </div>
    </main>
  );
}
