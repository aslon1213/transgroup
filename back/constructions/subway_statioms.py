from dataclasses import dataclass



class LineOfSubway:
    def __init__(self, name, stations):
        self.name = name
        self.stations = stations
    
    def __repr__(self):
        return f"Line {self.name} with stations {self.stations}"


class GraphOfSubwayStations:
    def __init__(self):
        self.all_stations = {}
        self.lines = None
        self.graph = []
        self.last_index = 0


    def RegisterLine(self, line : LineOfSubway):
        pass


    def RegisterStation(self, station_name, line_name, neighbours):
            # find all indexes of neighbours
            neighbour_indexes = [] 
            for neighbour in neighbours:    
                neighbour_indexes.append( self.all_stations[neighbour]["index"])

            self.all_stations[station_name] = {"line_name": line_name, "index": self.last_index + 1, "neighbours":neighbour_indexes}


    def findShortestPath(self, station1, station2):
        index_1 = self.all_stations[station1]["index"]
        index_2 = self.all_stations[station2]["index"]

        # use 
        pass
        self.last_index += 1

    def RegisterStation(self, station, line_name, line_index):
        self.stations.append(station)
            



    def getFromOneStationtoAnother(self, station1, station2):
        get_number_of_station1 = self.all_stations[station1]["line_index"]
        get_number_of_station2 = self.all_stations[station2]["line_index"]
        return None

    



