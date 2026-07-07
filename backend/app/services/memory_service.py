from app.models.memory_event import MemoryEvent
from app.models.memory_analysis import MemoryAnalysis

from app.repositories.memory_repository import MemoryRepository
from app.repositories.memory_analysis_repository import MemoryAnalysisRepository

from app.ai.memory_analyzer import MemoryAnalyzer


from app.events.event_bus import event_bus
from app.events.events import MemoryProcessedEvent
class MemoryService:

    def __init__(self):
        self.repository = MemoryRepository()
        self.analyzer = MemoryAnalyzer()
        self.analysis_repository = MemoryAnalysisRepository()
    def remember(
        self,
        db,
        user_id,
        title,
        description,
    ):

        print("\n========== REMEMBER STARTED ==========\n")

        analysis = self.analyzer.analyze(
            title=title,
            description=description,
        )

        print("\n========== AI ANALYSIS ==========")
        print(analysis)
        print("================================\n")

        memory = MemoryEvent(
            user_id=user_id,
            title=title,
            description=description,
        )

        memory = self.repository.create(
            db,
            memory,
        )

        analysis_record = MemoryAnalysis(
            memory_id=memory.id,
            sentiment=analysis.sentiment,
            emotion=analysis.emotion,
            confidence=analysis.confidence,
            severity=analysis.severity,
            reason=analysis.reason,
        )

        self.analysis_repository.create(
            db,
            analysis_record,
        )

        event_bus.publish(

            MemoryProcessedEvent(

                db=db,

                user_id=user_id,

                memory_id=memory.id,

                analysis=analysis,

            )

        )
        return memory
    
    def get_by_id(
        self,
        db,
        memory_id,
    ):
        return (
            db.query(MemoryEvent)
            .filter(MemoryEvent.id == memory_id)
            .first()
        )
    
    def get_all(
        self,
        db,
        user_id,
    ):

        return self.repository.get_all(
            db=db,
            user_id=user_id,
        )