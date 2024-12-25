import pandas
from abc import ABC, abstractmethod


df = pandas.read_csv("hotels.csv")
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_id]["name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def is_available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id]["available"].squeeze()
        print(availability)
        if availability == "yes":
            return True
        else:
            return False

class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, cust_name, hotel_obj):
        self.cust_name = cust_name
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.cust_name}
        Hotel name: {self.hotel.hotel_name}
        """
        return content


class CreditCard:
    def __init__(self, cc_num, exp, holder, cvc):
        self.cc_num = cc_num
        self.exp = exp
        self.holder = holder
        self.cvc = cvc

    def validate(self):
        card_data = {"number":self.cc_num, "expiration": self.exp,
                     "holder": self.holder, "cvc": self.cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.cc_num, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False
