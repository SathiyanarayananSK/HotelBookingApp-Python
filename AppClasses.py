import pandas


df = pandas.read_csv("hotels.csv")


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



class ReservationTicket:
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