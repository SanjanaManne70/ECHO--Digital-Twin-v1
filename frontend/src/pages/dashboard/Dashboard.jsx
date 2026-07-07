import DashboardLayout from "../../components/layout/DashboardLayout";

import HeroCard from "../../components/dashboard/HeroCard";
import ReflectionCard from "../../components/dashboard/ReflectionCard";
import InsightDashboardCard from "../../components/dashboard/InsightDashboardCard";

import useDashboard from "../../hooks/useDashboard";

export default function Dashboard() {

    const {

        loading,

        state,

        reflection,

        insight,
        user,

    } = useDashboard();

    if (loading) {

        return (

            <DashboardLayout>

                <div className="p-8">

                    <h2 className="text-2xl font-semibold">

                        Loading Dashboard...

                    </h2>

                </div>

            </DashboardLayout>

        );

    }

    return (

        <DashboardLayout>

            <HeroCard

                state={state}
                user={user}


            />

            <div className="grid lg:grid-cols-3 gap-6 mt-8">

                <div className="lg:col-span-2">

                    <ReflectionCard

                        reflection={reflection?.reflection}

                    />

                </div>

                <div>

                    <InsightDashboardCard

                        insight={insight}

                    />

                </div>

            </div>

        </DashboardLayout>

    );

}