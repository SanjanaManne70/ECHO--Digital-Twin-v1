function formatDay(date) {
    return date.toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

/**
 * Groups a flat memories array into:
 * [ { year, months: [ { key, year, monthIndex, label, count, weeks: [
 *     { weekIndex, label, range, memories } ] } ] } ]
 *
 * Weeks are day-of-month buckets: 1-7, 8-14, 15-21, 22-28, 29-end.
 * Years, months, and weeks are all sorted most-recent-first.
 */
export function groupMemoriesByTime(memories) {
    const yearMap = new Map();

    memories.forEach((memory) => {
        const date = new Date(memory.created_at);
        if (isNaN(date)) return;

        const year = date.getFullYear();
        const monthIndex = date.getMonth();
        const day = date.getDate();
        const weekIndex = Math.min(Math.ceil(day / 7), 5);

        if (!yearMap.has(year)) yearMap.set(year, new Map());
        const monthMap = yearMap.get(year);

        if (!monthMap.has(monthIndex)) monthMap.set(monthIndex, new Map());
        const weekMap = monthMap.get(monthIndex);

        if (!weekMap.has(weekIndex)) weekMap.set(weekIndex, []);
        weekMap.get(weekIndex).push(memory);
    });

    const years = Array.from(yearMap.keys()).sort((a, b) => b - a);

    return years.map((year) => {
        const monthMap = yearMap.get(year);
        const monthIndices = Array.from(monthMap.keys()).sort((a, b) => b - a);

        const months = monthIndices.map((monthIndex) => {
            const weekMap = monthMap.get(monthIndex);
            const weekIndices = Array.from(weekMap.keys()).sort((a, b) => b - a);
            const daysInMonth = new Date(year, monthIndex + 1, 0).getDate();

            const weeks = weekIndices.map((weekIndex) => {
                const startDay = (weekIndex - 1) * 7 + 1;
                const endDay = Math.min(weekIndex * 7, daysInMonth);
                const startDate = new Date(year, monthIndex, startDay);
                const endDate = new Date(year, monthIndex, endDay);

                const items = weekMap
                    .get(weekIndex)
                    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

                return {
                    weekIndex,
                    label: `Week ${weekIndex}`,
                    range: `${formatDay(startDate)} – ${formatDay(endDate)}`,
                    memories: items,
                };
            });

            const monthDate = new Date(year, monthIndex, 1);
            const count = weeks.reduce((sum, w) => sum + w.memories.length, 0);

            return {
                key: `${year}-${monthIndex}`,
                year,
                monthIndex,
                label: monthDate.toLocaleDateString("en-US", { month: "long" }),
                count,
                weeks,
            };
        });

        return { year, months };
    });
}