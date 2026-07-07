import StatCard from "../ui/StatCard";

function LearningCard({value}) {
  return (
    <StatCard
      title="Learning"
      value={value}
      color="border-blue-500"
    />
  );
}

export default LearningCard;