import DashboardLayout from "../../components/layout/DashboardLayout";

import GoalCard from "../../components/goals/GoalCard";
import GoalModal from "../../components/goals/GoalModal";

import useGoals from "../../hooks/useGoals";
import { deleteGoal } from "../../services/goalService";

export default function Goals() {

    const {

        goals,

        loading,

        refresh,

    } = useGoals();

    async function handleDelete(id) {

        await deleteGoal(id);

        refresh();

    }

    if (loading) {

        return (

            <DashboardLayout>

                <h2 className="text-2xl p-8">

                    Loading Goals...

                </h2>

            </DashboardLayout>

        );

    }

    if (goals.length === 0) {

        return (

            <DashboardLayout>

                <div className="text-center py-24">

                    <h2 className="text-3xl font-bold">

                        🎯 No Goals Yet

                    </h2>

                    <p className="text-gray-500 mt-3">

                        Create your first goal and let ECHO track it automatically.

                    </p>

                    <div className="mt-10 flex justify-center">

                        <GoalModal

                            onSaved={refresh}

                        />

                    </div>

                </div>

            </DashboardLayout>

        );

    }

    return (

        <DashboardLayout>

            <div className="bg-gradient-to-r from-emerald-600 to-green-600 text-white rounded-2xl p-8 mb-8">

                <h1 className="text-4xl font-bold">

                    🎯 Goals

                </h1>

                <p className="mt-2 opacity-90">

                    Your AI-powered roadmap.

                </p>

            </div>

            <div className="mb-8">

                <GoalModal

                    onSaved={refresh}

                />

            </div>

            <div className="grid grid-cols-2 gap-6">

                {

                    goals.map((goal) => (

                        <GoalCard

                            key={goal.id}

                            goal={goal}

                            onDelete={handleDelete}

                        />

                    ))

                }

            </div>

        </DashboardLayout>

    );

}