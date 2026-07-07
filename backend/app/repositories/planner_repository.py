from app.models.planner_task import PlannerTask


class PlannerRepository:

    def create(
        self,
        db,
        task,
    ):

        db.add(task)

        db.commit()

        db.refresh(task)

        return task

    def get_pending(
        self,
        db,
        user_id,
    ):

        return (
            db.query(PlannerTask)
            .filter(
                PlannerTask.user_id == user_id,
                PlannerTask.completed == False,
            )
            .order_by(
                PlannerTask.created_at.desc()
            )
            .all()
        )
    
    def get_recent(
        self,
        db,
        user_id,
        limit=30,
    ):

        return (
            db.query(PlannerTask)
            .filter(
                PlannerTask.user_id == user_id,
            )
            .order_by(
                PlannerTask.created_at.desc(),
            )
            .limit(limit)
            .all()
        )

    def get_completed(
        self,
        db,
        user_id,
    ):

        return (
            db.query(PlannerTask)
            .filter(
                PlannerTask.user_id == user_id,
                PlannerTask.completed == True,
            )
            .order_by(
                PlannerTask.created_at.desc(),
            )
            .all()
        )


    def get_by_id(
        self,
        db,
        task_id,
    ):

        return (
            db.query(PlannerTask)
            .filter(
                PlannerTask.id == task_id,
            )
            .first()
        )


    def update(
        self,
        db,
        task,
    ):

        db.commit()

        db.refresh(task)

        return task
    
    def delete_completed(
        self,
        db,
        user_id,
    ):

        (
            db.query(PlannerTask)

            .filter(

                PlannerTask.user_id == user_id,

                PlannerTask.completed == True,

            )

            .delete()

        )

        db.commit()
