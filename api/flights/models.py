
from general.models import AVLTree


class Flight:
    def __init__(self):
        self.flights = AVLTree()

    def find(self, flight_id):
        return self.flights.find(flight_id)

    def insert(self, flight_id, data):
        self.flights.insert(
            flight_id, {
                'name'
            }
        )
