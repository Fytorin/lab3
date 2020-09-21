from random import randrange
import random
import time

import sys


class FileWrirteRedirector(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y%m%d %I:%M %p', prop)


def repasts():
    print('''
INSERT INTO Repasts
VALUES ('завтрак'), ('обед') , ('ужин') , ('полдник') , ('второй завтрак') , ('предужин') , 
('перекус') , ('дозатврак') , ('доужин') , ('послеужин') ''')


def menu_standart():
    print('\ninsert into MenuToStandartPassengers \nvalues')
    for i in range(100):
        repast_id = randrange(1, 8)
        meal_option = "meal_option - " + str(randrange(20))
        print("(", repast_id, ", '", meal_option,  "') ")
        if i != 99:
            print(",", end='')


def part_of_portion():
    print('\ninsert into PartOfPortion \nvalues')
    for i in range(100):
        part = "part - " + str(randrange(100))
        print("('", part, "')")
        if i != 99:
            print(",", end='')


def airplanes():
    print('''
INSERT INTO Airplanes
VALUES ('Б777'), ('СУ-42') , ('Б737') , ('А330') , ('А350') , ('А321') , 
('А320') , ('ССГ-100') , ('Боинг') , ('Аэробус') ''')


def passenger():
    print('\ninsert into Passenger \nvalues')
    for i in range(100):
        tick = random.choice(['Б', 'П', 'Э'])
        last_name = "last_name - " + str(randrange(1000))
        first_name = "first_name - " + str(randrange(1000))
        phone = randrange(700000000000000, 89999999999999999)
        print("( '", tick, "' ,'", last_name, "', '", first_name, "', '", phone, "')")
        if i != 99:
            print(",", end='')

#
def flights():
    print('\ninsert into Flights \nvalues')
    for i in range(100):
        airplane_id = randrange(1, 10)
        departure_time = random_date("20080101 1:30 PM", "20090101 4:50 AM", random.random())
        place = "strip - " + str(randrange(1, 20))
        print("(", airplane_id, ",'", departure_time, "', '", place, "')")
        if i != 99:
            print(",", end='')


def flight_passengers_standart_individual_passenger():
    for i in range(40):
        passenger_id = randrange(35) + 3
        flight_id = randrange(35) + 3
        meal_option_id = randrange(9) + 1
        num = randrange(4) + 1
        part_id = randrange(70) + 20
        repast_id = randrange(9) + 1
        print('insert into FlightPassengers values')
        print("(", passenger_id, ", ", flight_id, ");")
        print('insert into PortionsToStandartPassengers values')
        print("(", passenger_id, ", ", flight_id, ", ", meal_option_id, ", ", num,  " );")
        print('insert into PortionsToIndividualPassengers values')
        print("(", repast_id, ",", passenger_id, ", ", flight_id, ", ", part_id, ", ", num,  " );")


def suppliers():
    print('\ninsert into Suppliers \nvalues')
    for i in range(100):
        supplier_name = "supplier_name - " + str(randrange(1000))
        address = "address: street  - " + str(randrange(1, 1000)) + "; house - " + str(randrange(1, 1000))
        phone = randrange(700000000000000, 89999999999999999)
        print("( ' ", supplier_name, "', '", address, "', '", phone, "')")
        if i != 99:
            print(",", end='')


def storages():

    print('\ninsert into Storages \nvalues')
    for i in range(100):
        open_time = random_date("20080101 1:30 PM", "20080130 4:50 AM", random.random())
        close_time = random_date("20080201 1:30 PM", "20090202 4:50 AM", random.random())
        print("( ' storage_name - ", randrange(1000),
              "', 'address: street  - ", randrange(1000), "; house - ", randrange(1000), "', '",
              randrange(700000000000000, 89999999999999999), "', '", open_time, "', '", close_time, "')")
        if i != 99:
            print(",", end='')


def product():
    print('\ninsert into Products \nvalues')
    for i in range(100):
        product_name = "product - " + str(randrange(1, 1000))
        type = random.choice(("кг", "г", "т"))
        print("( ' ", product_name, "', '", type, "')")
        if i != 99:
            print(",", end='')


def available_products():
    print('\ninsert into AvailableProducts \nvalues')
    for i in range(100):
        date_of_arrival = random_date("20080101 1:30 PM", "20080130 4:50 AM", random.random())
        storage_id = randrange(1, 100)
        product_id = randrange(1, 100)
        supplier_id = randrange(1, 100)
        expiration_time = random_date("20080301 1:30 PM", "20080730 4:50 AM", random.random())
        num_of_avail_units = randrange(1, 44)
        purchase_price_of_unit = randrange(10, 20)
        print("( ", product_id, ", ", storage_id, ", '", date_of_arrival, "', ", supplier_id, ", '", expiration_time,
              "', ", num_of_avail_units, ", ", purchase_price_of_unit, ")")
        if i != 99:
            print(",", end='')


def product_to_part_and_portion():
    for i in range(100):
        product_id = randrange(35) + 3
        part_id = randrange(1, 10)
        meal_option_id = randrange(1, 9)
        num = randrange(1, 4)
        print('\ninsert into ProductsToPortion values')
        print("(", product_id, ", ", meal_option_id, ", ", num, " );")
        print('insert into ProductToPart values')
        print("(", product_id, ", ", part_id, ", ", num, " );")
        if i != 99:
            print(",", end='')


if __name__ == '__main__':
    sys.stdout = sys.stderr = FileWrirteRedirector("res.sql")
    repasts()
    airplanes()
    menu_standart()
    part_of_portion()
    passenger()
    flights()
    flight_passengers_standart_individual_passenger()
    suppliers()
    storages()
    product()
    available_products()