from general.models import DDList


class Airport:

    def __init__(self):
        self.airports = DDList()

    def find(self, data):
        return self.airports.find(data.get('airportName'))

    def insert(self, data):
        self.airports.append({
            'name': data.get('airportName'),
            'actualCountry': data.get('actualCountry'),
            'password': data.get('password')
        })

