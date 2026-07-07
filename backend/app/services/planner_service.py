from app.agents.planner_agent import PlannerAgent
from app.ai.planner_response_parser import PlannerResponseParser
from app.ai.reflection_context_builder import ReflectionContextBuilder
from app.models.planner_task import PlannerTask
from app.repositories.planner_repository import PlannerRepository


class PlannerService:

    def __init__(self):

        self.agent = PlannerAgent()

        self.parser = PlannerResponseParser()

        self.context_builder = ReflectionContextBuilder()

        self.repository = PlannerRepository()

    def generate(
        self,
        db,
        user_id,
        analysis,
    ):

        context = self.context_builder.build(
            db=db,
            user_id=user_id,
        )

        twin = ""

        for state in context["current"]:

            twin += (
                f"{state.domain}: "
                f"{state.value}\n"
            )

        memories = ""

        for memory in context["memories"]:

            memories += (
                f"- {memory.title}: "
                f"{memory.description}\n"
            )

        response = self.agent.generate(

            analysis=analysis,

            context={

                "twin": twin,

                "memories": memories,

            },

        )

        task = self.parser.parse(
            response,
        )

        planner = PlannerTask(

            user_id=user_id,

            title=task["title"],

            description=task["description"],

            priority=task["priority"],

        )

        return self.repository.create(
            db,
            planner,
        )
    
    def create_manual_task(
        self,
        db,
        user_id,
        title,
    ):

        planner = PlannerTask(

            user_id=user_id,

            title=title,

            description="",

            priority="Medium",

            completed=False,

        )

        return self.repository.create(
            db,
            planner,
        )


    def complete_task(
        self,
        db,
        task_id,
    ):

        task = self.repository.get_by_id(
            db,
            task_id,
        )

        if not task:

            return None

        task.completed = True

        return self.repository.update(
            db,
            task,
        )


    def get_completed(
        self,
        db,
        user_id,
    ):

        return self.repository.get_completed(
            db,
            user_id,
        )
    def clear_completed(

        self,

        db,

        user_id,

    ):

        self.repository.delete_completed(

            db,

            user_id,

        )