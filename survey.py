class AnonymousSurvey():
    """Contains anonymous answers to survey question."""

    def __init__(self, question):
        """Contains question and prepares to store answer."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Displays survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Stores one answer to survey question."""
        self.responses.append(new_response)

    def show_results(self):
        """Displays all given answers."""
        print("Here are survey results:")
        for response in self.responses:
            print(f"- {response}")