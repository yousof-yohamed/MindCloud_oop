class VotingSystem:
    def __init__(self):

        self.__candidates = {}

    def add_candidate(self, name):
        """Add a new candidate if not already present."""
        if name in self.__candidates:
            print(f"Candidate '{name}' already exists.")
        else:
            self.__candidates[name] = 0
            print(f"Candidate '{name}' added.")

    def remove_candidate(self, name):
        """Remove a candidate if they exist."""
        if name in self.__candidates:
            del self.__candidates[name]
            print(f"Candidate '{name}' removed.")
        else:
            print(f"Candidate '{name}' not found.")

    def vote_to_candidate(self, name):
        """Cast a vote for a candidate."""
        if name in self.__candidates:
            self.__candidates[name] += 1
            print(f"Vote cast for '{name}'.")
        else:
            print(f"Candidate '{name}' not found.")

    def display_winner(self):
        """Display the winner based on highest votes."""
        if not self.__candidates:
            print("No candidates available.")
            return

        winner = max(self.__candidates, key=self.__candidates.get)
        votes = self.__candidates[winner]
        print(f"The winner is '{winner}' with {votes} votes.")