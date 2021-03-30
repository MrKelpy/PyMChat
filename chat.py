import time
import os

import pygetwindow
import keyboard

from .exceptions import *


def parse_chat_messages(history: list, limit: int):

    """
    Parses out chat messages from any other types of logs.
    :param history: The latest.log lines
    :param limit: The limit estabilished for returning
    :return:
    """
    messages_request = list()
    counter = 0  # Initiates a counter used to count the amount of valid messages being returned
    for line in reversed(history):

        if "[CHAT]" not in line:
            # Exempts non-chatlogs from being accounted for
            continue

        if counter == limit:
            # Saves time and resources by limiting the amount of lines to loop through
            break

        # Parses out the message content from the line
        line_components = line.split()
        chat_indicator_index = line_components.index("[CHAT]") + 1
        del line_components[:chat_indicator_index]

        # Sorts the products of the algorithm, ready to append to a list.
        message = ' '.join(line_components)

        if not message:
            # Incase the message is empty, skip it.
            continue

        line_number = history.index(line) + 1
        date = line.split(" [")[0][1:-1]

        messages_request.append(Message(message, line_number, date))
        counter += 1

    if not messages_request:
        return None

    return messages_request


class Chat:

    def __init__(self):

        # The constructor method automatically handles the configuration of the settings for various needed assets
        # The aforementioned method can be modified accordingly to one's needs.

        self.default_logs_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "logs", "latest.log")
        self._ensure_log_existance()
        self.chat_key = "t"
        self.window_name = "Minecraft"

    def _ensure_log_existance(self):

        if not os.path.isfile(self.default_logs_path):
            raise LogsNotFoundError(f"Could not find any file at \"{self.default_logs_path}\"")

        return True

    def _get_minecraft_window(self):

        """
        Gets the window accordingly to the self.window_name property.
        :return: Window or None
        """

        if self.window_name in pygetwindow.getActiveWindowTitle():
            return pygetwindow.getActiveWindow()

        for window in pygetwindow.getAllWindows():
            if self.window_name in window.title:
                return window

        raise MinecraftWindowNotFoundError(f"Could not find a Minecraft Window with the title containing \"{self.window_name}\"")

    def get_history(self, limit: int = 50**50):

        """
        :param limit: Limitation on how back the chat history goes
        :return: list or None
        """

        with open(self.default_logs_path, "r") as logs_file:
            log_history = logs_file.readlines()

        message_list = parse_chat_messages(log_history, limit)
        return message_list

    def send(self, message: str):

        """
        Sends a message in chat. Checks for a window with minecraft open on screen,
        if none is to be seen, finds and focuses on one.
        :param message:
        :return:
        """

        saved_window = pygetwindow.getActiveWindow()  # Saves the current active window for later reposition

        minecraft_window = self._get_minecraft_window()
        if not minecraft_window.isActive:
            # Focuses on the minecraft window and presses ESC to exit chat/GUI's

            minecraft_window.activate()
            keyboard.send("ESC")

        # Handles message sending in chat.
        keyboard.send(self.chat_key)
        time.sleep(0.1)
        keyboard.write(message)
        keyboard.send("RETURN")

        # Re-activates the saved window
        saved_window.activate()