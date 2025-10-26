class Seat:
    def __init__(self):
        self.occupant = ""

    def is_free(self):
        return self.occupant == ""  
    
    def set_occupant(self, name):
        if self.is_free():
           self.occupant = name
           return f"seat assigned to {name}"
        else:
            return f"seat occupied by {self.occupant}"
        
    def remove_occupant(self):
        if self.is_free():
           return "seat already free"
        else:
            previous = self.occupant
            self.occupant = ""
            return f"{previous} removed from seat"

    



class Table: 
    def __init__(self,capacity: int) -> None:
        self.capacity = capacity
        self.seats = [Seat() for i in range(self.capacity)] 

    def has_free_spot(self) -> bool:
        # check each seat if it's free
        for seat in self.seats:
            if seat.is_free():
                return True 
        return False
        
    
    def assign_seat(self, name: str) -> str:
        # look for free seat 
        for seat in self.seats:
            if seat.is_free():
                return seat.set_occupant(name)
        # if loop finsihes, no free seat were found
        return "No free seats available"
    
    def left_capacity(self) -> int:
        count = 0
        for seat in self.seats:
            if seat.is_free():
                count += 1
        return count
    
    def list_occupants(self):
        """Return a list of all current occupants (empty strings for free seats)."""
        return [seat.occupant for seat in self.seats]

    