/* Single-source stroke icon set (24px grid, currentColor). */
const PATHS = {
  dashboard: (<><rect x="3" y="3" width="7.5" height="9" rx="2" /><rect x="13.5" y="3" width="7.5" height="5.5" rx="2" /><rect x="13.5" y="11.5" width="7.5" height="9.5" rx="2" /><rect x="3" y="15" width="7.5" height="6" rx="2" /></>),
  twin: (<><circle cx="12" cy="8" r="3.5" /><path d="M5 20c.6-3.6 3.4-5.5 7-5.5s6.4 1.9 7 5.5" /><path d="M16.8 4.6a3.5 3.5 0 0 1 0 6.8" opacity=".55" /></>),
  goals: (<><circle cx="12" cy="12" r="8.5" /><circle cx="12" cy="12" r="4.5" /><circle cx="12" cy="12" r="1" fill="currentColor" /></>),
  timeline: (<><path d="M12 3v18" /><circle cx="12" cy="7" r="2" fill="currentColor" /><circle cx="12" cy="17" r="2" fill="currentColor" /><path d="M14.5 7H20M4 17h5.5" /></>),
  memory: (<><path d="M9 4.5a3 3 0 0 0-3 3v.2A3.2 3.2 0 0 0 4.5 11a3.2 3.2 0 0 0 1.3 2.5A3.3 3.3 0 0 0 9 19.5h.5V4.5H9Z" /><path d="M15 4.5a3 3 0 0 1 3 3v.2a3.2 3.2 0 0 1 1.5 3.3 3.2 3.2 0 0 1-1.3 2.5 3.3 3.3 0 0 1-3.2 6H14.5V4.5h.5Z" /></>),
  simulation: (<><path d="M4 18c3-1 4-9 8-9s5 8 8 6" /><circle cx="4" cy="18" r="1.4" fill="currentColor" /><circle cx="20" cy="15" r="1.4" fill="currentColor" /><path d="M12 3v3M10.5 4.5h3" opacity=".7" /></>),
  history: (<><path d="M4 12a8 8 0 1 0 2.6-5.9" /><path d="M4 4v4.5h4.5" /><path d="M12 8v4.3l2.8 1.7" /></>),
  logout: (<><path d="M9 4H6.5A2.5 2.5 0 0 0 4 6.5v11A2.5 2.5 0 0 0 6.5 20H9" /><path d="M15 8l4 4-4 4M19 12H9" /></>),
  menu: (<path d="M4 7h16M4 12h16M4 17h16" />),
  close: (<path d="M6 6l12 12M18 6 6 18" />),
  plus: (<path d="M12 5v14M5 12h14" />),
  trash: (<><path d="M4 7h16M9 7V4.5h6V7" /><path d="M6.5 7l.8 12.2A1.5 1.5 0 0 0 8.8 20.5h6.4a1.5 1.5 0 0 0 1.5-1.3L17.5 7" /></>),
  check: (<path d="M5 12.5l4.5 4.5L19 7.5" />),
  chevron: (<path d="M9 6l6 6-6 6" />),
  refresh: (<><path d="M20 11a8 8 0 0 0-14-4.5L4 9" /><path d="M4 4v5h5" /><path d="M4 13a8 8 0 0 0 14 4.5L20 15" /><path d="M20 20v-5h-5" /></>),
  spark: (<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3Z" />),
  alert: (<><path d="M12 4 3 19.5h18L12 4Z" /><path d="M12 10v4.5M12 17.2v.1" /></>),
  info: (<><circle cx="12" cy="12" r="8.5" /><path d="M12 11v5M12 8v.1" /></>),
  up: (<path d="M6 14l6-6 6 6" />),
  down: (<path d="M6 10l6 6 6-6" />),
  flat: (<path d="M5 12h14" />),
};

export default function Icon({ name, size = 20, className = "", strokeWidth = 1.6, ...rest }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
      className={className}
      {...rest}
    >
      {PATHS[name] ?? null}
    </svg>
  );
}
