#WAP to create a class train which has method to book ticket, get info and get status of the train.
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fom, to):
        print(f"Your ticket is booked from {fom} to {to} on train number {self.trainNo}")

    def getStatus(self, fom, to):
        print(f"Train number {self.trainNo} which runs from {fom} to {to} is on time.")

    def getFare(self, fom, to):
        print(f"Fare for the train {self.trainNo} from {fom} to {to} is {randint(250, 555)}")

a = Train(101)
a.bookTicket("Ktm", "Pokhara")
a.getStatus("Ktm", "Pokhara")
a.getFare("Ktm", "Pokhara")