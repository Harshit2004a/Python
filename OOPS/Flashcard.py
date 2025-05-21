class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

flashcards = [
    Flashcard("What is the capital of France?", "Paris"),
    Flashcard("What is 2 + 2?", "4"),
    Flashcard("Who wrote 'Hamlet'?", "William Shakespeare")
]

for card in flashcards:
    print(f"Question: {card.question}")
    input("Press Enter to see the answer...")
    print(f"Answer: {card.answer}")
    print("-" * 30)
    
# Code by Harshit