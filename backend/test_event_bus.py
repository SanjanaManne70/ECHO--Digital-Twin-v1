from app.events.event_bus import event_bus
from app.events.events import MemoryCreatedEvent
from app.events.handlers import twin_update_handler


event_bus.subscribe(
    MemoryCreatedEvent,
    twin_update_handler,
)

event_bus.publish(

    MemoryCreatedEvent(

        user_id=1,

        memory_id=100,

    )

)