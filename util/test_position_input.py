import time

from touroptimizer_py_client.models.geo_node import GeoNode
from touroptimizer_py_client.models.node import Node

from touroptimizer_py_client.models.capacity_resource import CapacityResource
from touroptimizer_py_client.models.resource import Resource

from datetime import datetime, timedelta

from touroptimizer_py_client.models.position import Position

from touroptimizer_py_client.models.node_type import NodeType

from touroptimizer_py_client.models.opening_hours import OpeningHours
from touroptimizer_py_client.models.working_hours import WorkingHours

from typing import List


class TestPositionsInput:

    @staticmethod
    def default_sydney_node_positions() -> List[Position]:
        poss = []
        poss.append(Position(latitude=-34.052052, longitude=150.668724, locationId="Node_0"))
        poss.append(Position(latitude=-34.052518, longitude=150.709943, locationId="Node_1"))
        poss.append(Position(latitude=-34.051988, longitude=150.71981, locationId="Node_2"))
        poss.append(Position(latitude=-34.04213, longitude=150.729568, locationId="Node_3"))
        poss.append(Position(latitude=-34.042063, longitude=150.739632, locationId="Node_4"))

        return poss

    @staticmethod
    def default_sydney_resource_positions() -> List[Position]:
        poss = []
        poss.append(Position(latitude=-34.052052, longitude=150.668724, locationId="Resource_0"))
        poss.append(Position(latitude=-34.052518, longitude=150.709943, locationId="Resource_1"))
        poss.append(Position(latitude=-34.051988, longitude=150.71981, locationId="Resource_2"))
        poss.append(Position(latitude=-34.052015, longitude=150.999808, locationId="Resource_3"))

        return poss
    
    @staticmethod
    def positions_to_string(positions: List[Position]) -> str:
        return ', '.join(str(pos) for pos in positions)
    
    
## ------- Main program -------
if __name__ == "__main__":

    poss = TestPositionsInput.default_sydney_node_positions()
    print("Created test positions: " + TestPositionsInput.positions_to_string(poss))
