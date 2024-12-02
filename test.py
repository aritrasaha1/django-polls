class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)

    def display_logs(self):
        return "\n".join(self.logs)

# Client code
logger1 = Logger()
logger1.log("User logged in.")
logger2 = Logger()
logger2.log("Commit made to the project.")

# Both logger1 and logger2 refer to the same instance
print(logger1.display_logs())
