from src.connectors.base import TargetConnector

class FileTargetConnector(TargetConnector):
    def write(self, data):
        for row in data:
            print(row)
