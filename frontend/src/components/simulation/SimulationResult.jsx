import OverallCard from "./OverallCard";
import DomainCard from "./DomainCard";
import GoalPredictionCard from "./GoalPredictionCard";
import BenefitsCard from "./BenefitsCard";
import RisksCard from "./RisksCard";
import RecommendationCard from "./RecommendationCard";

export default function SimulationResult({ result }) {

    if (!result) return null;

    return (

    <div className="space-y-8 mt-10 animate-fade-in">

        <OverallCard
            overall={result.overall}
        />

        <div>

            <h2 className="text-3xl font-bold mb-5">

                📊 Life Domains

            </h2>

            <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">

                {result.domains?.map((domain, index) => (

                    <DomainCard
                        key={index}
                        domain={domain}
                    />

                ))}

            </div>

        </div>

        {

            result.goals?.length > 0 &&

            <div>

                <h2 className="text-3xl font-bold mb-5">

                    🎯 Goal Predictions

                </h2>

                <div className="grid md:grid-cols-2 gap-6">

                    {

                        result.goals.map((goal, index) => (

                            <GoalPredictionCard

                                key={index}

                                goal={goal}

                            />

                        ))

                    }

                </div>

            </div>

        }

        <div className="grid lg:grid-cols-3 gap-6">

            <BenefitsCard

                benefits={result.benefits}

            />

            <RisksCard

                risks={result.risks}

            />

            <RecommendationCard

                recommendations={result.recommendations}

            />

        </div>

    </div>

);

}