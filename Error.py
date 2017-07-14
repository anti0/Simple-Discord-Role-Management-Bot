class Error:
    def __init__(self, success, value):
        self.status = { success: success,
                        value: value }