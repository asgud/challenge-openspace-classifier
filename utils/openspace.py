import random 

from utils.table import Table


import random 

class Openspace:
    def __init__(self,number_of_tables: int, amount_seat: int) -> None:
        """
        Creates a Openspace with a given number of tables. 
        Args: 
            number_of_tables: How many tables to create
            amount_seat: How many seats each table should have
        """
        self.tables = [Table(amount_seat) for n in range(number_of_tables)]      # This creates a list of Table objects, each with the specified number of seats


    def organize(self, names: list[str]) -> None:
        """
        Randomly assign people to available seats across all tables.
        """
        # Shuffle the list of names to randomize order
        random.shuffle(names)

        all_seats = []                     # step 1 - empty list
        for table in self.tables:          # step 2 - go through each table and seat, and them to all_seats
            for seat in table.seats:
                all_seats.append(seat)

        for name in names:                #  step 3 - go through each person and assign them to a random free seat
            free_seats = []               #  make an empty list to collect all free seats
            for seat in all_seats:
                if seat.is_free():
                    free_seats.append(seat)

            if len(free_seats) == 0:
                print(f"No more free seats! Could not assign {name}")
                break
        
            chosen_seat = random.choice(free_seats)
            print(chosen_seat.set_occupant(name))

    
    def display(self) -> None:
        """
        Show all tables and their occupants in a simple and readable way.
        """
        print("\n--- OpenSpace Seating Plan ---")

        # Go through each table and print out its seats
        for table_number, table in enumerate(self.tables, start=1):
            print(f"\nTable {table_number}:")  # print table number

            # Go through the seats in that table
            for seat_number, seat in enumerate(table.seats, start=1):
                if seat.is_free():
                    print(f"  Seat {seat_number}: [Empty]")
                else:                    print(f"  Seat {seat_number}: {seat.occupant}")

        print("\n-----------------------------")

    def store(self, filename: str) -> None:
        """
        Save the seating plan into a text file.
        """
        # Open the file in write mode (this creates or replaces the file)
        file = open(filename, "w")

        file.write("--- OpenSpace Seating Plan ---\n")

        # Go through all tables and write their info into the file
        for table_number, table in enumerate(self.tables, start=1):
            file.write(f"\nTable {table_number}:\n")
            for seat_number, seat in enumerate(table.seats, start=1):
                if seat.is_free():
                    file.write(f"  Seat {seat_number}: [Empty]\n")
                else:
                    file.write(f"  Seat {seat_number}: {seat.occupant}\n")

        file.write("\n-----------------------------\n")

        # Close the file
        file.close()

        print(f"Seating plan saved to '{filename}' successfully!")
