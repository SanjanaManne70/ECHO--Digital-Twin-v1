import { getMonthTheme } from "./MonthCard";

export default function WeekCard({ week, monthIndex, isExpanded, onClick }) {
    const theme = getMonthTheme(monthIndex);

    return (
        <button
            onClick={onClick}
            className={`w-full text-left rounded-2xl p-5 bg-white/80 backdrop-blur-sm border
                border-[#2B2A4C]/10 shadow-sm hover:shadow-md transition-all duration-300
                ${isExpanded ? "ring-2 " + theme.ring : ""}`}
        >
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                    <span className={`w-2.5 h-2.5 rounded-full ${theme.dot}`} />
                    <h4 className="font-display text-lg font-semibold text-[#2B2A4C]">
                        {week.label}
                    </h4>
                </div>
                <span className="font-hand text-base text-[#2B2A4C]/60">
                    {isExpanded ? "▾" : "▸"}
                </span>
            </div>

            <p className="font-body text-xs text-[#2B2A4C]/60 mt-1 ml-4.5">
                {week.range} · {week.memories.length} {week.memories.length === 1 ? "entry" : "entries"}
            </p>
        </button>
    );
}