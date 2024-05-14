from src.services.process import ServiceProcess
class Process:
    def __init__(self):
        self.process = ServiceProcess()

    def get(self, params):
        response = self.process.listProcess()
        return response

    def getFilter(self):
        pass