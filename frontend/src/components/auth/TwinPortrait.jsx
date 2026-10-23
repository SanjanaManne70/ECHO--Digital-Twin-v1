/*
 * Left-hand composition for the auth screens: a human profile with a luminous
 * digital-twin silhouette emerging from it.
 *
 * Drop a photo at src/assets/login-twin.(png|jpg|jpeg|webp|avif) (a profile
 * facing right, dark background) and it replaces the silhouette automatically;
 * the hologram layers on top either way.
 */
const photos = import.meta.glob("../../assets/login-twin.jpg", {
  eager: true,
  import: "default",
});
const photo = Object.values(photos)[0];

const HEAD =
  "M120 156 C116 84 176 42 238 54 C290 64 312 108 310 154 C310 172 318 186 330 212 L350 246 C352 254 344 259 331 260 C335 267 335 273 330 277 C335 281 335 287 329 290 C331 302 327 312 315 322 C308 330 304 342 300 356 L304 392 C340 404 392 420 420 452 L420 560 L30 560 L30 452 C62 420 126 402 168 388 C166 350 158 326 144 306 C124 276 116 214 120 156 Z";

/* Photo mode: the supplied portrait is the hero. Edges are feathered so it melts
   into the page, with a slow breathing glow and a light sweep over the twin. */
function PhotoPortrait({ className }) {
  // Fade each edge independently so the interior stays fully bright.
  const feather =
    "linear-gradient(90deg, #000 0%, #000 78%, transparent 100%), linear-gradient(180deg, #000 0%, #000 88%, transparent 100%)";
  return (
    <div className={`relative flex h-full w-full flex-col items-center justify-center ${className}`}>
      <div className="relative w-full max-w-none lg:max-w-[1040px]">
        <img
          src={photo}
          alt="A woman in profile beside her glowing holographic digital twin, surrounded by memories, goals, habits, and insights"
          className="block h-auto w-full select-none mix-blend-screen"
          style={{
            WebkitMaskImage: feather,
            maskImage: feather,
            WebkitMaskComposite: "source-in",
            maskComposite: "intersect",
          }}
          draggable="false"
        />

        {/* Breathing glow on the twin side */}
        <div
          aria-hidden="true"
          className="pointer-events-none absolute inset-0 animate-echo-breathe mix-blend-screen"
          style={{
            background:
              "radial-gradient(ellipse 28% 38% at 70% 44%, rgba(96,165,250,.28), transparent 70%)",
          }}
        />

        {/* Light sweep, confined to the twin */}
        <div
          aria-hidden="true"
          className="pointer-events-none absolute bottom-[6%] left-[48%] top-[6%] w-[34%] overflow-hidden"
          style={{
            WebkitMaskImage: "linear-gradient(90deg, transparent, #000 25%, #000 75%, transparent)",
            maskImage: "linear-gradient(90deg, transparent, #000 25%, #000 75%, transparent)",
          }}
        >
          <div
            className="holo-sweep h-28 w-full mix-blend-screen"
            style={{
              background:
                "linear-gradient(180deg, transparent, rgba(125,211,252,.30) 50%, transparent)",
            }}
          />
        </div>
      </div>

    </div>
  );
}

export default function TwinPortrait({ className = "" }) {
  if (photo) return <PhotoPortrait className={className} />;

  return (
    <div className={`relative flex h-full w-full flex-col items-center justify-center ${className}`}>
      <div className="relative w-full max-w-none lg:max-w-[1040px]">
        <svg
          viewBox="-20 0 540 560"
          className="h-auto w-full overflow-visible"
          role="img"
          aria-label="A human profile with a glowing holographic digital twin forming beside it"
        >
          <defs>
            <linearGradient id="tp-human" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#1b2740" />
              <stop offset="100%" stopColor="#0a1020" />
            </linearGradient>
            <linearGradient id="tp-holo" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="#22d3ee" />
              <stop offset="55%" stopColor="#3b82f6" />
              <stop offset="100%" stopColor="#8b5cf6" />
            </linearGradient>
            <linearGradient id="tp-band" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#22d3ee" stopOpacity="0" />
              <stop offset="50%" stopColor="#67e8f9" stopOpacity=".38" />
              <stop offset="100%" stopColor="#22d3ee" stopOpacity="0" />
            </linearGradient>
            <radialGradient id="tp-aura" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#3b82f6" stopOpacity=".34" />
              <stop offset="55%" stopColor="#8b5cf6" stopOpacity=".12" />
              <stop offset="100%" stopColor="#070b16" stopOpacity="0" />
            </radialGradient>
            <pattern id="tp-mesh" width="11" height="11" patternUnits="userSpaceOnUse">
              <circle cx="1.5" cy="1.5" r=".9" fill="#67e8f9" opacity=".7" />
            </pattern>
            <pattern id="tp-scan" width="6" height="6" patternUnits="userSpaceOnUse">
              <rect width="6" height="1" fill="#22d3ee" opacity=".16" />
            </pattern>
            <filter id="tp-blur" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="9" />
            </filter>
            <clipPath id="tp-twin-clip">
              <path d={HEAD} />
            </clipPath>
            <linearGradient id="tp-fade" x1="0" y1="0" x2="0" y2="1">
              <stop offset="70%" stopColor="#fff" />
              <stop offset="100%" stopColor="#000" />
            </linearGradient>
            <mask id="tp-bottom-fade" maskUnits="userSpaceOnUse" x="-20" y="0" width="540" height="560">
              <rect x="-20" width="540" height="560" fill="url(#tp-fade)" />
            </mask>
            <linearGradient id="tp-side" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stopColor="#000" />
              <stop offset="14%" stopColor="#fff" />
              <stop offset="86%" stopColor="#fff" />
              <stop offset="100%" stopColor="#000" />
            </linearGradient>
            <mask id="tp-side-fade" maskUnits="userSpaceOnUse" x="-20" y="0" width="540" height="560">
              <rect x="-20" width="540" height="560" fill="url(#tp-side)" />
            </mask>
          </defs>

          <circle cx="270" cy="250" r="340" fill="url(#tp-aura)" />

          <g mask="url(#tp-side-fade)">
          <g mask="url(#tp-bottom-fade)">
            {/* Human */}
            {photo ? (
              <image href={photo} x="0" y="0" width="480" height="560" preserveAspectRatio="xMidYMid slice" />
            ) : (
              <g transform="translate(-10 6)">
                <path d={HEAD} fill="url(#tp-human)" stroke="rgba(148,163,184,.5)" strokeWidth="1.5" />
                <path
                  d="M310 154 C310 172 318 186 330 212 L350 246 C352 254 344 259 331 260"
                  fill="none"
                  stroke="#67e8f9"
                  strokeOpacity=".55"
                  strokeWidth="1.5"
                />
              </g>
            )}

            {/* Digital twin */}
            <g className="holo-breathe" transform="translate(78 -10) scale(.98)">
              <path d={HEAD} fill="none" stroke="url(#tp-holo)" strokeWidth="10" opacity=".5" filter="url(#tp-blur)" />
              <path d={HEAD} fill="rgba(34,211,238,.06)" stroke="url(#tp-holo)" strokeWidth="1.6" />

              <g clipPath="url(#tp-twin-clip)">
                <rect width="480" height="560" fill="url(#tp-mesh)" opacity=".55" />
                <rect width="480" height="560" fill="url(#tp-scan)" />
                {/* Neural nodes inside the head */}
                <g stroke="#67e8f9" strokeOpacity=".5" strokeWidth=".8" fill="none">
                  <path d="M190 120 L240 98 L276 140 L232 170 Z M240 98 L232 170 M190 120 L232 170 M276 140 L300 190 L232 170 M200 210 L232 170 L262 228 L300 190" />
                </g>
                <g fill="#a5f3fc">
                  {[[190, 120], [240, 98], [276, 140], [232, 170], [300, 190], [200, 210], [262, 228]].map(([x, y]) => (
                    <circle key={`${x}-${y}`} cx={x} cy={y} r="2.6" />
                  ))}
                </g>
                {/* Scan band */}
                <rect className="holo-sweep" x="0" y="0" width="480" height="120" fill="url(#tp-band)" />
              </g>
            </g>
          </g>
          </g>
        </svg>
      </div>

    </div>
  );
}
