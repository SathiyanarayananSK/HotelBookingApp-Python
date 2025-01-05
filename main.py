from AppClasses import df, Hotel, ReservationTicket, SecureCreditCard

print(df)
hotel_id = int(input("Enter the id of the hotel: "))

# Check hotel availability
hotel = Hotel(hotel_id)

if hotel.is_available():
    # Get user details and credit card information
    name = input("Enter your name: ")
    cc_num, exp, holder, cvc = input("Enter Credit card number, expiry date, holder, cvv (Separated by comma): ").split(",")
    credit_card = SecureCreditCard(cc_num, exp, holder, cvc)

    # Validate and authenticate credit card
    if credit_card.validate():
        given_password = input("Enter your password: ")
        if credit_card.authenticate(given_password):
            # Book the hotel and generate a reservation ticket
            hotel.book()
            reservation_ticket = ReservationTicket(name, hotel)
            ticket = reservation_ticket.generate()
            print(ticket)
        else:
            print("Credit card authentication failed!")
    else:
        print("There is a problem with your payment!")
else:
    print("Sorry, Hotel is unavailable!")
