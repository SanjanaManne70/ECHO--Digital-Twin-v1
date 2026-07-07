from app.models.twin_snapshot import TwinSnapshot


class TwinSnapshotRepository:

    def create(
        self,
        db,
        snapshot: TwinSnapshot,
    ):

        db.add(snapshot)

        db.commit()

        db.refresh(snapshot)

        return snapshot
    
    def get_latest(
        self,
        db,
        user_id,
    ):

        return (
            db.query(TwinSnapshot)
            .filter(
                TwinSnapshot.user_id == user_id
            )
            .order_by(
                TwinSnapshot.created_at.desc()
            )
            .first()
        )


    def get_history(
        self,
        db,
        user_id,
        limit=30,
    ):

        return (
            db.query(TwinSnapshot)
            .filter(
                TwinSnapshot.user_id == user_id
            )
            .order_by(
                TwinSnapshot.created_at.desc()
            )
            .limit(limit)
            .all()
        )