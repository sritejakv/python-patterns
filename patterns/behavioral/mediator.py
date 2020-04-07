"""
:testcase_name mediator
:source https://github.com/faif/python-patterns/blob/master/patterns/behavioral/mediator.py
:description Objects in a system communicate through a Mediator instead of directly with each other.
This reduces the dependencies between communicating objects, thereby reducing coupling.
"""


class ChatRoom:
    """Mediator class"""

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


class User:
    """A class whose instances want to interact with each other"""

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


def main():
    """
    >>> molly = User('Molly')
    >>> mark = User('Mark')
    >>> ethan = User('Ethan')

    >>> molly.say("Hi Team! Meeting at 3 PM today.")
    [Molly says]: Hi Team! Meeting at 3 PM today.
    >>> mark.say("Roger that!")
    [Mark says]: Roger that!
    >>> ethan.say("Alright.")
    [Ethan says]: Alright.
    """


if __name__ == '__main__':
    molly = User('Molly')
    mark = User('Mark')
    ethan = User('Ethan')
    molly.say("Hi Team! Meeting at 3 PM today.")
    mark.say("Roger that!")
    ethan.say("Alright.")
