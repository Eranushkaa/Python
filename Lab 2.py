print('''
----------------------------
BUS ROUTE MANAGEMENT SYSTEM
---------------------------- 
''')
route=int(input('Enter the route number: '))

if route==1:
    print('''
    -------------------------------------
    Buses On the Route
    -------------------------------------
    1. Marvel
    2. Volvo
    3. Tata
    -------------------------------------
    ''')

    choice=input('do you want to know the bus timings? (y/n): ')
    if choice=='y':
        print('''
        -------------------------------------
        Timming of Buses
        -------------------------------------
        1. MARVEL 10:00 AM
        2. VOLVO  11:00 AM
        3. TATA   12:00 PM
        -------------------------------------
        ''')

elif route==2:
    print('''
        -------------------------------------
        Buses On the Route
        -------------------------------------
        1. Marvel
        2. Volvo
        3. Tata
        -------------------------------------
        ''')
    
    Choice=input('do you want to know the bus timings? (y/n): ')
    if choice=='y':
            print('''
            -------------------------------------
            Timming of Buses
            -------------------------------------
            1. MARVEL 10:00 AM
            2. VOLVO  11:00 AM
            3. TATA   12:00 PM
            -------------------------------------
            ''')

    elif route==3:
         print('Invalid route number')