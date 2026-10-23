import { useMemo, useState } from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import useTimeline from "../../hooks/useTimeline";

import YearCard from "../../components/timeline/YearCard";
import MonthCard from "../../components/timeline/MonthCard";
import DayCard from "../../components/timeline/DayCard";

import { groupTimeline } from "../../utils/timelineGrouping";
import "../../styles/echo-pages.css";

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

                <div className="echo-upgrade echo-timeline"><p className="echo-eyebrow">YOUR STORY, OVER TIME</p><h1 className="echo-page-title">Loading your journey...</h1></div>

            </DashboardLayout>

        );

    }

    if (timeline.length === 0) {

        return (

            <DashboardLayout>

                <div className="echo-upgrade echo-timeline"><div className="echo-empty-state text-center py-24">

                    <h2 className="text-3xl font-bold">

                        No Journey Yet 📝

                    </h2>

                    <p className="text-gray-500 mt-3">

                        Start writing memories and ECHO will build your story.

                    </p>

                </div></div>

            </DashboardLayout>

        );

    }

    return (

        <DashboardLayout>
          <div className="echo-upgrade echo-timeline">
            <div className="echo-page-header echo-hero-panel">

                <div><p className="echo-eyebrow">YOUR STORY, OVER TIME</p><h1>📖 Your Journey</h1><p>Explore the moments, milestones, and small wins that make you.</p></div><span className="echo-orb-icon">⌁</span>
            </div>

            <div className="space-y-6 echo-timeline-list">

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
          </div>
        </DashboardLayout>

    );

}