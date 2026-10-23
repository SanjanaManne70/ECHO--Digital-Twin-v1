import Card from "../ui/Card";
import RadialGauge from "../ui/RadialGauge";

/** Gauge card for one 0-100 twin metric. Shows "—" if the backend returns no value. */
export default function MetricCard({ title, value, tone = "cyan", note }) {
  return (
    <Card interactive className="flex flex-col items-center p-6 text-center">
      <RadialGauge value={value} label={title} tone={tone} size={136} />
      <h3 className="mt-4 font-display text-base font-semibold text-white">{title}</h3>
      {note && <p className="mt-1 text-xs text-slate-400">{note}</p>}
    </Card>
  );
}
