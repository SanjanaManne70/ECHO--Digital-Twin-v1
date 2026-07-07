import { useMemo, useState } from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";
import useMemories from "../../hooks/useMemories";

import MemoryCard from "../../components/memory/MemoryCard";
import MonthCard from "../../components/memory/MonthCard";
import WeekCard from "../../components/memory/WeekCard";
import NewMemoryModal from "../../components/memory/NewMemoryModal";

import { groupMemoriesByTime } from "../../utils/memoryGrouping";

import "../../styles/diary-theme.css";

export default function Memory() {

    const {

        memories,

        loading,

        addMemory,

    } = useMemories();

    const [

        isNewMemoryOpen,

        setIsNewMemoryOpen,

    ] = useState(false);

    const [

        expandedMonthKey,

        setExpandedMonthKey,

    ] = useState(null);

    const [

        expandedWeekIndex,

        setExpandedWeekIndex,

    ] = useState(null);

    const yearGroups = useMemo(

        () => groupMemoriesByTime(memories),

        [memories]

    );

    function toggleMonth(key) {

        setExpandedWeekIndex(null);

        setExpandedMonthKey(

            prev => prev === key ? null : key

        );

    }

    function toggleWeek(index) {

        setExpandedWeekIndex(

            prev => prev === index ? null : index

        );

    }

    if (loading) {

        return (

            <DashboardLayout>

                <div className="flex items-center justify-center h-64">

                    <p className="font-display text-2xl text-[#2B2A4C]/70 animate-pulse">

                        Turning the pages...

                    </p>

                </div>

            </DashboardLayout>

        );

    }

    return (

        <DashboardLayout>

            {/* Hero */}

            <div className="paper-grain relative overflow-hidden rounded-3xl bg-[#FBF7F0] border border-[#2B2A4C]/10 p-8 mb-10 shadow-sm">

                <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-6">

                    <div>

                        <p className="font-hand text-xl text-[#C1548A]">

                            Your story, one page at a time

                        </p>

                        <h1 className="font-display text-5xl font-semibold text-[#2B2A4C] mt-1">

                            🧠 Memory Vault

                        </h1>

                        <p className="font-body mt-3 text-[#2B2A4C]/70">

                            Every experience your Digital Twin remembers,

                            organized like a journal.

                        </p>

                    </div>

                    <button

                        onClick={() => setIsNewMemoryOpen(true)}

                        className="font-body font-semibold px-6 py-3 rounded-full bg-[#2B2A4C] text-[#FBF7F0]
                        hover:bg-[#3d3c66] transition-all duration-300 shadow-md
                        hover:shadow-lg hover:-translate-y-0.5"

                    >

                        + New Memory

                    </button>

                </div>

            </div>

            {

                memories.length === 0 ? (

                    <div className="text-center py-20">

                        <p className="font-display text-2xl text-[#2B2A4C]/60">

                            This journal is blank so far.

                        </p>

                        <p className="font-body text-[#2B2A4C]/50 mt-2">

                            Write your first memory to begin.

                        </p>

                    </div>

                ) : (

                    <div className="space-y-12">

                        {

                            yearGroups.map(({ year, months }) => (

                                <section key={year}>

                                    <h2 className="font-hand text-3xl text-[#2B2A4C]/60 mb-4">

                                        {year}

                                    </h2>

                                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">

                                        {

                                            months.map(month => {

                                                const expanded = expandedMonthKey === month.key;

                                                return (

                                                    <div

                                                        key={month.key}

                                                        className={expanded ? "sm:col-span-2 lg:col-span-3" : ""}

                                                    >

                                                        <MonthCard

                                                            month={month}

                                                            isExpanded={expanded}

                                                            onClick={() => toggleMonth(month.key)}

                                                        />

                                                        <div className={`accordion-wrapper ${expanded ? "is-expanded" : ""}`}>

                                                            <div className="accordion-inner">

                                                                <div className="pt-5 pl-6 border-l-2 border-[#2B2A4C]/10 ml-4 space-y-4">

                                                                    {

                                                                        month.weeks.map(week => {

                                                                            const weekExpanded = expandedWeekIndex === week.weekIndex;

                                                                            return (

                                                                                <div key={week.weekIndex}>

                                                                                    <WeekCard

                                                                                        week={week}

                                                                                        monthIndex={month.monthIndex}

                                                                                        isExpanded={weekExpanded}

                                                                                        onClick={() => toggleWeek(week.weekIndex)}

                                                                                    />

                                                                                    <div className={`accordion-wrapper ${weekExpanded ? "is-expanded" : ""}`}>

                                                                                        <div className="accordion-inner">

                                                                                            <div className="grid gap-4 pt-4">

                                                                                                {

                                                                                                    week.memories.map(memory => (

                                                                                                        <MemoryCard

                                                                                                            key={memory.id}

                                                                                                            memory={memory}

                                                                                                        />

                                                                                                    ))

                                                                                                }

                                                                                            </div>

                                                                                        </div>

                                                                                    </div>

                                                                                </div>

                                                                            );

                                                                        })

                                                                    }

                                                                </div>

                                                            </div>

                                                        </div>

                                                    </div>

                                                );

                                            })

                                        }

                                    </div>

                                </section>

                            ))

                        }

                    </div>

                )

            }

            {

                isNewMemoryOpen && (

                    <NewMemoryModal

                        onClose={() => setIsNewMemoryOpen(false)}

                        onSave={async (memory) => {

                            await addMemory(memory);

                            setIsNewMemoryOpen(false);

                        }}

                    />

                )

            }

        </DashboardLayout>

    );

}