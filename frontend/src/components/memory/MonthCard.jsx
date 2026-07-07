const THEMES = [
    { grad: "from-[#FFD9C0] to-[#FFB4A2]", ring: "ring-[#FFB4A2]/50", dot: "bg-[#E8846B]", icon: "🌸" }, // Jan
    { grad: "from-[#CFE8E0] to-[#A9D6C9]", ring: "ring-[#A9D6C9]/50", dot: "bg-[#4F9C85]", icon: "❄️" }, // Feb
    { grad: "from-[#D6CDEA] to-[#C4B5F0]", ring: "ring-[#C4B5F0]/50", dot: "bg-[#8267C9]", icon: "🌱" }, // Mar
    { grad: "from-[#FFE3AE] to-[#FFD37E]", ring: "ring-[#FFD37E]/50", dot: "bg-[#E0A526]", icon: "🌷" }, // Apr
    { grad: "from-[#C9E4CA] to-[#A9D8AB]", ring: "ring-[#A9D8AB]/50", dot: "bg-[#4C9354]", icon: "🌼" }, // May
    { grad: "from-[#BEE3F8] to-[#9BD1F2]", ring: "ring-[#9BD1F2]/50", dot: "bg-[#2E8FC4]", icon: "☀️" }, // Jun
    { grad: "from-[#FFD3D3] to-[#FFADAD]", ring: "ring-[#FFADAD]/50", dot: "bg-[#E05656]", icon: "🍉" }, // Jul
    { grad: "from-[#FFE8B0] to-[#FFD37E]", ring: "ring-[#FFD37E]/50", dot: "bg-[#DE9A1F]", icon: "🌻" }, // Aug
    { grad: "from-[#F3D9C4] to-[#E9BFA0]", ring: "ring-[#E9BFA0]/50", dot: "bg-[#B9713D]", icon: "🍂" }, // Sep
    { grad: "from-[#F0C9D9] to-[#E5A9C4]", ring: "ring-[#E5A9C4]/50", dot: "bg-[#C1548A]", icon: "🎃" }, // Oct
    { grad: "from-[#D9D3E8] to-[#C1B6DD]", ring: "ring-[#C1B6DD]/50", dot: "bg-[#7A649E]", icon: "🍁" }, // Nov
    { grad: "from-[#D6E4F0] to-[#B7D0E8]", ring: "ring-[#B7D0E8]/50", dot: "bg-[#3E71A3]", icon: "❄️" }, // Dec
];

export function getMonthTheme(monthIndex) {
    return THEMES[monthIndex % THEMES.length];
}

export default function MonthCard({ month, isExpanded, onClick }) {
    const theme = getMonthTheme(month.monthIndex);

    return (
        <button
            onClick={onClick}
            className={`corner-fold paper-grain text-left w-full rounded-3xl p-6 bg-gradient-to-br ${theme.grad}
                shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300
                ring-2 ${isExpanded ? theme.ring : "ring-transparent"}`}
        >
            <div className="flex items-start justify-between">
                <span className="text-3xl">{theme.icon}</span>
                <span className="font-hand text-lg text-[#2B2A4C]/70">
                    {isExpanded ? "close ✦" : "open →"}
                </span>
            </div>

            <h3 className="font-display text-3xl font-semibold text-[#2B2A4C] mt-4">
                {month.label}
            </h3>

            <p className="font-body text-sm text-[#2B2A4C]/70 mt-1">
                {month.year} · {month.count} {month.count === 1 ? "memory" : "memories"}
            </p>
        </button>
    );
}