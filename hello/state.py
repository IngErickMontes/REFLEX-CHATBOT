import reflex as rx


class State (rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot is not very smart right now...
        answer = "gustavo come nepe"
        self.chat_history.append((self.question, answer))
        self.question = "aa"