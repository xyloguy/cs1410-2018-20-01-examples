trips = [
    {
        'date': '1/1/2017',
        'miles': 300.0,
        'gallons': 9.68,
    },
    {
        'date': '1/6/2017',
        'miles': 203.7,
        'gallons': 7.58,
    },
    {
        'date': '1/18/2017',
        'miles': 298.7,
        'gallons': 8.7,
    }
]


def milesPerGallon(miles, gallons):
    return miles / gallons


def listTrips(trips):
    l = []
    for trip in trips:
        date = trip['date']
        miles = trip['miles']
        gallons = trip['gallons']
        mpg = round(milesPerGallon(miles, gallons), 2)
        s = 'On ' + date + ': ' + str(miles) \
            + ' miles traveled using ' + str(gallons) \
            + ' gallons. Gas mileage: ' + str(mpg) + ' MPG'
        l.append(s)
    return l


print(listTrips(trips))
print(listTrips([]))