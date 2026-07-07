import { useMemo, useState } from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import useTimeline from "../../hooks/useTimeline";

import YearCard from "../../components/timeline/YearCard";
import MonthCard from "../../components/timeline/MonthCard";
import DayCard from "../../components/timeline/DayCard";

import { groupTimeline } from "../../utils/timelineGrouping";

export default function Timeline() {

    const {

        timeline,

        loading,

    } = useTimeline();

    const groupedTimeline = useMemo(

        () => groupTimeline(timeline),

        [timeline]

    );

    const [

        expandedYear,

        setExpandedYear,

    ] = useState(null);

    const [

        expandedMonth,

        setExpandedMonth,

    ] = useState(null);

    if (loading) {

        return (

            <DashboardLayout>

                <h2 className="text-2xl">

                    Loading Journey...

                </h2>

            </DashboardLayout>

        );

    }

    if (timeline.length === 0) {

        return (

            <DashboardLayout>

                <div className="text-center py-24">

                    <h2 className="text-3xl font-bold">

                        No Journey Yet 📝

                    </h2>

                    <p className="text-gray-500 mt-3">

                        Start writing memories and ECHO will build your story.

                    </p>

                </div>

            </DashboardLayout>

        );

    }

    return (

        <DashboardLayout>

            <div className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-2xl p-8 mb-10">

                <h1 className="text-4xl font-bold">

                    📖 Your Journey

                </h1>

                <p className="mt-2 opacity-90">

                    Explore how you've grown over time.

                </p>

            </div>

            <div className="space-y-8">

                {

                    groupedTimeline.map((year)=>{

                        const activeDays = year.months.reduce(

                            (count, month)=>count + month.days.length,

                            0

                        );

                        return(

                            <YearCard

                                key={year.year}

                                year={year.year}

                                activeDays={activeDays}

                                expanded={expandedYear===year.year}

                                onClick={()=>{

                                    setExpandedYear(

                                        expandedYear===year.year

                                        ? null

                                        : year.year

                                    );

                                    setExpandedMonth(null);

                                }}

                            >

                                {

                                    year.months.map((month)=>{

                                        const monthKey =

                                            `${year.year}-${month.month}`;

                                        return(

                                            <MonthCard

                                                key={monthKey}

                                                month={month.month}

                                                activeDays={month.days.length}

                                                expanded={

                                                    expandedMonth===monthKey

                                                }

                                                onClick={()=>{

                                                    setExpandedMonth(

                                                        expandedMonth===monthKey

                                                        ? null

                                                        : monthKey

                                                    );

                                                }}

                                            >

                                                {

                                                    month.days.map((day)=>(

                                                        <DayCard

                                                            key={day.dateKey}

                                                            day={day}

                                                        />

                                                    ))

                                                }

                                            </MonthCard>

                                        );

                                    })

                                }

                            </YearCard>

                        );

                    })

                }

            </div>

        </DashboardLayout>

    );

}