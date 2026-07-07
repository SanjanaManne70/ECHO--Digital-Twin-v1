class ContextBuilder:

    def build(
        self,
        current_states,
        memories,
    ):

        twin = {}

        for state in current_states:
            twin[state.domain] = state.value

        memory_list = []

        for memory in memories:
            memory_list.append(
                f"- {memory.title}: {memory.description}"
            )

        return {
            "twin": twin,
            "memories": "\n".join(memory_list),
        }