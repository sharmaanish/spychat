from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

f1= Spy('sia', 'Ms.', 7.9, 37)
f2 = Spy('lil', 'Mr.', 9.9, 41)
f3 = Spy('kim', 'ms', 8.5, 27)


friends = [f1, f2, f3]