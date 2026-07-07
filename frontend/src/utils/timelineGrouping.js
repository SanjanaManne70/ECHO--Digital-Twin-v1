export function groupTimeline(timeline) {

    const years = {};

    timeline.forEach((day) => {

        const date = new Date(day.date);

        const year = date.getFullYear();

        const month = date.toLocaleString("default", {

            month: "long",

        });

        const monthIndex = date.getMonth();

        if (!years[year]) {

            years[year] = {};

        }

        if (!years[year][month]) {

            years[year][month] = {

                month,

                monthIndex,

                days: [],

            };

        }

        years[year][month].days.push({

            ...day,

            dateKey: day.date,

        });

    });

    return Object.entries(years)

        .sort((a, b) => Number(b[0]) - Number(a[0]))

        .map(([year, months]) => ({

            year,

            months: Object.values(months).sort(

                (a, b) => b.monthIndex - a.monthIndex

            ),

        }));

}