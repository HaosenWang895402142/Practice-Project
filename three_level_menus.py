#__author: Haosen Wang
#Date: 12/15/2017

menu= {
    'California':{
        'Los Angeles':{
            '1990':{'3,485,398'},
            '2000':{'3,694,820'},
            '2010':{'3,792,621'},
        },
        'San Diego':{
            '1990':{'1,110,549'},
            '2000':{'1,223,400'},
            '2010':{'1,307,402'},
        },
    },
    'New York':{
        'New York City':{
            '1990':{'7,322,564'},
            '2000':{'8,008,278'},
            '2010':{'8,175,133'},
        },
        'Buffalo':{
            '1990':{'328,123'},
            '2000':{'292,648'},
            '2010':{'261,310'},
        },
    },
    'Pennsylvania':{
        'Philadelphia':{
            '1990':{'1,585,577'},
            '2000':{'1,517,550'},
            '2010':{'1,526,006'},
        },
        'Pittsburgh':{
            '1990':{'369,879'},
            '2000':{'334,563'},
            '2010':{'305,704'},
        },
    },
}

while True:
    for key in menu:
        print(key)
    choice = input('\nEnter State: ').strip()
    if choice in menu:
        while True:
            for key2 in menu[choice]:
                print(key2)
            choice2 = input('\nEnter City: ').strip()
            if choice2 in menu[choice]:
                while True:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input('\nEnter year: ').strip()
                    if choice3 in menu[choice][choice2]:
                        print(menu[choice][choice2][choice3])
                        exit()
                    else:
                        print('\nYear not in List\n')
                        continue

        else:
                print('\nCity not in List\n')
                continue
    else:
        print('\nState not in List\n')
        continue

