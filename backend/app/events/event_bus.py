class EventBus:

    def __init__(self):

        self.subscribers = {}

    def subscribe(
        self,
        event_type,
        handler,
    ):

        self.subscribers.setdefault(
            event_type,
            [],
        ).append(handler)

    def publish(
        self,
        event,
    ):

        handlers = self.subscribers.get(
            type(event),
            [],
        )

        for handler in handlers:

            handler(event)

event_bus = EventBus()