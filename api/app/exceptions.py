class MessageException(Exception):
  def __init__(self, code: int, message: str, exception: str = None):
    self.code = code
    self.message = message
    self.exception = exception