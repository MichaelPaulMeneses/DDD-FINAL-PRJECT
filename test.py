import tkinter as tk
import sqlite3


class AirportManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title('Airport Management System')
        self.master.geometry('800x600')

        # create a database connection
        self.conn = sqlite3.connect('airport.db')
        self.cursor = self.conn.cursor()

        # create a table to store passenger information
        self.cursor.execute('CREATE TABLE IF NOT EXISTS passengers (name text, flight_number text, seat_number text)')

        # create the GUI
        self.create_widgets()

    def create_widgets(self):
        # create labels and entry fields for passenger information
        tk.Label(self.master, text='Name:').grid(row=0, column=0)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.master, text='Flight Number:').grid(row=1, column=0)
        self.flight_entry = tk.Entry(self.master)
        self.flight_entry.grid(row=1, column=1)

        tk.Label(self.master, text='Seat Number:').grid(row=2, column=0)
        self.seat_entry = tk.Entry(self.master)
        self.seat_entry.grid(row=2, column=1)

        # create buttons for adding and searching passengers
        tk.Button(self.master, text='Add Passenger', command=self.add_passenger).grid(row=3, column=0)
        tk.Button(self.master, text='Search Passengers', command= self.search_passengers).grid(row=3, column=1)

        # create a text widget to display search results
        self.search_results = tk.Text(self.master, height=10, width=65)
        self.search_results.grid(row=4, column=0, columnspan=2)

    def add_passenger(self):
        name = self.name_entry.get()
        flight_number = self.flight_entry.get()
        seat_number = self.seat_entry.get()

        # insert passenger information into the database
        self.cursor.execute('INSERT INTO passengers VALUES (?, ?, ?)', (name, flight_number, seat_number))
        self.conn.commit()

        # clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.flight_entry.delete(0, tk.END)
        self.seat_entry.delete(0, tk.END)

    def search_passengers(self):
        flight_number = self.flight_entry.get()

        # search for all passengers on a given flight
        self.cursor.execute('SELECT * FROM passengers WHERE flight_number=?', (flight_number,))
        rows = self.cursor.fetchall()

        # display the search results in the text widget
        self.search_results.delete(0.0, tk.END)
        for row in rows:
            self.search_results.insert(tk.END, f"{row[0]} - Flight Number: {row[1]}, Seat Number: {row[2]}\n")


if __name__ == '__main__':
    root = tk.Tk()
    app = AirportManagementSystem(root)
    root.mainloop()