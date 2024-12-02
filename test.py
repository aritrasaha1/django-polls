# Abstract class for Progress (StandUp, Commit, UserStory)
class Progress:
    def display_progress(self):
        pass

# Concrete class for StandUp Progress
class StandUpProgress(Progress):
    def display_progress(self):
        return "Today's Stand-Up: Discussed blockers and progress."

# Concrete class for Commit Progress
class CommitProgress(Progress):
    def display_progress(self):
        return "New Commit: Fixed bug in login module."

# Concrete class for UserStory Progress
class UserStoryProgress(Progress):
    def display_progress(self):
        return "User Story: Task #5 is 50% complete."

# Factory Method to create progress instances
class ProgressFactory:
    def create_progress(self, progress_type):
        if progress_type == "standup":
            return StandUpProgress()
        elif progress_type == "commit":
            return CommitProgress()
        elif progress_type == "userstory":
            return UserStoryProgress()

# Client code
progress_factory = ProgressFactory()

# Create and display different types of progress
standup_progress = progress_factory.create_progress("standup")
print(standup_progress.display_progress())

commit_progress = progress_factory.create_progress("commit")
print(commit_progress.display_progress())

userstory_progress = progress_factory.create_progress("userstory")
print(userstory_progress.display_progress())
