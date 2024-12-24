from AppClasses import df, Hotel, ReservationTicket

print(df)
hotel_id = int(input("Enter the id of the hotel: "))

hotel = Hotel(hotel_id)

if hotel.is_available():
    name = input("Enter your name: ")
    hotel.book()
    reservation_ticket = ReservationTicket(name, hotel)
    ticket = reservation_ticket.generate()
    print(ticket)

else:
    print("Sorry, Hotel is unavailable!")