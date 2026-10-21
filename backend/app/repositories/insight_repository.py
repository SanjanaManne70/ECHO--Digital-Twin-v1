from app.models.insight import Insight


class InsightRepository:

    def create(self, db, insight: Insight, commit: bool = True):
        db.add(insight)

        if commit:
            db.commit()
            db.refresh(insight)

        return insight

    def get_by_user(
        self,
        db,
        user_id,
    ):

        return (
            db.query(Insight)
            .filter(
                Insight.user_id == user_id
            )
            .order_by(
                Insight.created_at.desc()
            )
            .all()
        )

    def mark_as_read(
        self,
        db,
        insight_id,
    ):

        insight = (
            db.query(Insight)
            .filter(
                Insight.id == insight_id
            )
            .first()
        )

        if insight:

            insight.is_read = True

            db.commit()

            db.refresh(insight)

        return insight
    
    def latest_by_user(
        self,
        db,
        user_id,
    ):

        return (

            db.query(Insight)

            .filter(
                Insight.user_id == user_id
            )

            .order_by(
                Insight.created_at.desc()
            )

            .first()

        )
    
    def get_recent(
        self,
        db,
        user_id,
        limit=30,
    ):

        return (
            db.query(Insight)
            .filter(
                Insight.user_id == user_id,
            )
            .order_by(
                Insight.created_at.desc(),
            )
            .limit(limit)
            .all()
        )