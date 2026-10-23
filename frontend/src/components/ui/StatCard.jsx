function StatCard({ title, value, color }) {
  const numericValue = Number(value);
  const hasNumericValue = Number.isFinite(numericValue);
  const progress = hasNumericValue ? Math.max(0, Math.min(100, numericValue)) : null;

  return (
    <div className={`echo-metric-card bg-white rounded-xl shadow-md p-6 border-l-4 ${color}`}>
      <div className="echo-metric-heading">
        <h3 className="text-gray-500 text-sm">{title}</h3>
        <span className="echo-metric-mark" aria-hidden="true" />
      </div>

      <p className="echo-metric-value text-3xl font-bold mt-2">{value}</p>

      {progress !== null && (
        <div
          className="echo-metric-track"
          role="progressbar"
          aria-label={`${title} score`}
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={progress}
        >
          <span style={{ width: `${progress}%` }} />
        </div>
      )}
    </div>
  );
}

export default StatCard;
