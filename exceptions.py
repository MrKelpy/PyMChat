class LogsNotFoundError(BaseException):

    """
    Occurs when a file isn't present at the set destination for the logs file.
    """


class MinecraftWindowNotFoundError(BaseException):

    """
    Occurs when the Minecraft Window configured is not found upon trying to send a message.
    """