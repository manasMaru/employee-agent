class SourceConnector:
    def read(self):
        raise NotImplementedError


class TargetConnector:
    def write(self, data):
        raise NotImplementedError
