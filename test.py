# Subject (TeamProgress)
class TeamProgress:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, commit_message):
        for observer in self._observers:
            observer.update(commit_message)

# Observer (TA)
class TA:
    def update(self, commit_message):
        print(f"New commit update: {commit_message}")

# Client code
team_progress = TeamProgress()

# TAs subscribe to the progress updates
ta1 = TA()
ta2 = TA()

team_progress.add_observer(ta1)
team_progress.add_observer(ta2)

# Notify observers of a new commit
team_progress.notify_observers("Commit #123: Finished implementing login functionality")
