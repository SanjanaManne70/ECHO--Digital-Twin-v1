import Card from "../ui/Card";
import Icon from "../ui/Icon";

const TONES = {
    good: { icon: "check", accent: "text-emerald-300", border: "border-t-emerald-400/60" },
    risk: { icon: "alert", accent: "text-amber-300", border: "border-t-amber-400/60" },
    next: { icon: "spark", accent: "text-sky-300", border: "border-t-sky-400/60" },
};

/** Shared list card behind Benefits, Risks and Recommendations. */
export default function InsightList({ title, items = [], tone = "good" }) {

    if (!items.length) return null;

    const t = TONES[tone];

    return (
        <Card className={`border-t-2 p-6 ${t.border}`}>
            <h3 className={`font-display text-base font-semibold ${t.accent}`}>{title}</h3>
            <ul className="mt-4 space-y-3">
                {items.map((item, i) => (
                    <li key={i} className="flex gap-3 text-[15px] leading-7 text-slate-300">
                        <Icon name={t.icon} size={17} className={`mt-1.5 shrink-0 ${t.accent}`} />
                        <span>{item}</span>
                    </li>
                ))}
            </ul>
        </Card>
    );
}
