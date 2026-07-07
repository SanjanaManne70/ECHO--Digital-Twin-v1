import StatCard from "../ui/StatCard";

function HealthCard({value}) {
  return (
    <StatCard
      title="Health"
      value={value}
      color="border-green-500"
    />
  );
}

export default HealthCard;