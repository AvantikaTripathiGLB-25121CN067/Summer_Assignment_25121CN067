class TicketBooking:
    def __init__(self,total_seats):
        self.seats={i:"Available" for i in range(1,total_seats+1)}

    def book_seat(self,seat_number):
        if self.seats.get(seat_number)=="Available":
            self.seats[seat_number]="Booked"
            return f"Seat {seat_number} booked successfully!"
        return "Seat not vacant or invalid!"
    
train=TicketBooking(50)
print(train.book_seat(5))
