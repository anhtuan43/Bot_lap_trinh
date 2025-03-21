class Reflection:
    """
    A callable class that extracts the last N items from the chat history.

    Attributes:
        lastItemsConsidereds (int): Number of most recent messages to keep.
    """

    def __call__(self, chatHistory, lastItemsConsidereds=8):
        """
        Extracts the last `lastItemsConsidereds` messages from the chat history.

        :param chatHistory: List of chat messages.
        :param lastItemsConsidereds: Number of recent messages to keep.
        :return: A truncated chat history containing only the last `lastItemsConsidereds` messages.
        """
        return chatHistory[-lastItemsConsidereds:]