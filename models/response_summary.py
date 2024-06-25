class ResponseSummary:
    def __init__(self, summary: str):
        self.summary = summary

    def to_dict(self):
        return {
            'summary': self.summary
        }