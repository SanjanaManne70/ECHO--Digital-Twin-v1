class Edge:
    def __init__(
        self,
        source,
        target,
        weight,
        confidence=1.0,
    ):
        self.source = source

        self.target = target

        self.weight = weight

        self.confidence = confidence

    def __repr__(self):

        return (
            f"{self.source.name}"
            f" -> "
            f"{self.target.name}"
            f" ({self.weight})"
        )