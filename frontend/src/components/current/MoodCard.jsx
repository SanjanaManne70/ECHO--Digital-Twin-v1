import StatCard from "../ui/StatCard";

function MoodCard({value}) {
  return (
    <StatCard
      title="Mood"
      value={value}
      color="border-yellow-500"
    />
  );
}

export default MoodCard;