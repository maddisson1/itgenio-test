import pickle

class Autobus:
    def __init__(self, number, start, stop, time):
        self.number = number
        self.start = start
        self.stop = stop
        self.time = time
        
    def info(self):
        print(f"----------------\n"
              f"Route number: {self.number}\n"
              f"Starting point: {self.start}\n"
              f"Destination point: {self.stop}\n"
              f"Travel time: {self.time}\n"
              f"----------------")
    
    def set_number(self, number):
        self.number = number
        
    def set_start(self, start):
        self.start = start

    def set_stop(self, stop):
        self.stop = stop

    def set_time(self, time):
        self.time = time
        
    def get_number(self):
        return self.number

    def get_start(self):
        return self.start

    def get_stop(self):
        return self.stop

    def get_time(self):
        return self.time 
    


buses = []
filename = ""
def create_autopark():
    global buses, filename
    n = int(input('Enter the number of buses: '))
    for i in range(n):
        print('----------------------')
        number = int(input(f"Enter the route number of {i+1} bus: "))
        start = input(f"Enter the starting point of {i+1} bus: ")
        stop = input(f"Enter the destination point of {i+1} bus: ")
        time = input(f"Enter the travel time of {i+1} bus: ")
        bus = Autobus(number, start, stop, time)
        buses.append(bus)
    filename = input("Enter the name of file: ")
    with open(filename+'.txt', 'wb') as file:
        pickle.dump(buses, file)


def show_autopark():
    global buses, filename
    try:
        with open(filename+'.txt', 'rb') as file:
            buses = pickle.load(file)
        for bus in buses:
            bus.info()
    except FileNotFoundError:
        print(f"File {filename} not found")


def sort_by_number():
    global buses
    buses.sort(key=lambda bus: bus.number, reverse=True)
    for bus in buses:
        bus.info()


def search_by_point(stop_name):
    global buses
    found_buses = [bus for bus in buses if bus.start == stop_name or bus.stop == stop_name]
    if found_buses:
        for bus in found_buses:
            bus.info()
    else:
        print("Not found")  

while True:
    print('-------------------------------------')
    print("1. Create autopark\n2. Show autopark\n3. Sort by number\n4. Search by point")
    option = int(input('Choose an option, please: '))
    if option == 1:
        create_autopark()
    elif option == 2:
        show_autopark()
    elif option == 3:
        sort_by_number()
    elif option == 4:
        stop_name = input('Enter the destination name: ')
        search_by_point(stop_name)
    else:
        print('Please, enter the right option')
