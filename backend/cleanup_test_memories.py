
from app.database.session import SessionLocal
from sqlalchemy import text

EXPECTED = 43

SELECT_IDS = text("""
    SELECT id
    FROM memory_events
    WHERE user_id = 2
      AND title = 'V2 Multi Agent Test'
      AND description = 'Today I completed the multi-agent architecture for ECHO and connected the digital twin with decision making.'
    ORDER BY id
    FOR UPDATE
""")

db = SessionLocal()

try:
    ids = [row[0] for row in db.execute(SELECT_IDS).all()]

    if len(ids) != EXPECTED:
        raise RuntimeError(
            f"Expected {EXPECTED} test memories, found {len(ids)}. "
            "Nothing will be committed."
        )

    analysis_count = db.execute(
        text("""
            SELECT COUNT(*)
            FROM memory_analysis
            WHERE memory_id = ANY(:ids)
        """),
        {"ids": ids},
    ).scalar_one()

    if analysis_count != EXPECTED:
        raise RuntimeError(
            f"Expected {EXPECTED} analysis rows, found {analysis_count}. "
            "Nothing will be committed."
        )

    deleted_analysis = db.execute(
        text("""
            DELETE FROM memory_analysis
            WHERE memory_id = ANY(:ids)
        """),
        {"ids": ids},
    ).rowcount

    deleted_memories = db.execute(
        text("""
            DELETE FROM memory_events
            WHERE id = ANY(:ids)
              AND user_id = 2
              AND title = 'V2 Multi Agent Test'
              AND description = 'Today I completed the multi-agent architecture for ECHO and connected the digital twin with decision making.'
        """),
        {"ids": ids},
    ).rowcount

    if deleted_analysis != EXPECTED or deleted_memories != EXPECTED:
        raise RuntimeError(
            f"Unexpected deletion counts: analysis={deleted_analysis}, "
            f"memories={deleted_memories}. Rolling back."
        )

    db.commit()
    print("Cleanup committed successfully.")
    print("Deleted test memories:", deleted_memories)
    print("Deleted linked analysis records:", deleted_analysis)

except Exception:
    db.rollback()
    raise

finally:
    db.close()
