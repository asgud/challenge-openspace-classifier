class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        if self.free:
           self.occupant = name
           self.free = False
           return f"seat assigned to {name}"
        else:
            return f"seat occuiped by {self.occupant}"
        
    def remove_occupant(self):
        if self.free == True:
           return "seat already free"
        else:
            pervious = self.occupant
            self.occupant = None
            self.free = True 
            return pervious 
                        
    def read(self):
        return self.occupant
    



class Table: 
    def __init__(self,capacity: int) -> None:
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)] 

    def has_free_spot(self) -> bool:
        # check each seat if it's free
        for seat in self.seats:
            if seat.free == True: 
                return True # As soon as we find one free seat, return True
        
        # If no seat was free, return False
        return False
    
    def assign_seat(self, name: str) -> str:
        # look for free seat 
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        # if loop finsihes, no free seat were found
        return "No free seats available"
    
    def left_capacity(self) -> int:
        count = 0
        for seat in self.seats:
            if seat.free == True:
                count += 1
        return count
    
    def list_occupants(self):
        """Return a list of all current occupants (empty strings for free seats)."""
        return [seat.read() for seat in self.seats]
