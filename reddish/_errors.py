class ConnectionClosedError(Exception):
    def __init__(self, msg='Connection closed.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
