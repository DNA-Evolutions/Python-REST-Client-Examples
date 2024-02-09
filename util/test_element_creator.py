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

from util.test_position_input import TestPositionsInput

class TestElementsCreator:
    
    @staticmethod
    def conv_poss_to_ress(poss) -> List[Resource]:
        resources = []
        for i, pos in enumerate(poss):
            resource_id = pos.location_id  # or any other logic to create a unique ID
            resource = TestElementsCreator.default_capacity_resource(pos, resource_id)
            resources.append(resource)
        return resources
    
    @staticmethod
    def conv_poss_to_nodes(poss) -> List[Node]:
        nodes = []
        for i, pos in enumerate(poss):
            node_id = pos.location_id  # or any other logic to create a unique ID
            node = TestElementsCreator.default_geo_node(pos, node_id)
            nodes.append(node)
            
            #print("pos: " + pos.to_str())
            #print("node: " + node.to_str())
        
        return nodes
    
    @staticmethod
    def ress_to_string(ress: List[Resource]) -> str:
        return ', '.join(str(res) for res in ress)
    
    @staticmethod
    def nodes_to_string(nodes: List[Node]) -> str:
        return ', '.join(str(node) for node in nodes)


    # Create Resource
    
    @staticmethod
    def default_capacity_resource(pos, id, working_hours=None) -> Resource:
        
        if working_hours is None:
            working_hours = TestElementsCreator.default_test_workinghours()
            
            
        max_time = "PT12H"
        max_distance = "1200.0 km"
        

        cap_part = CapacityResource(typeName="Capacity")
        
        res_instance = Resource(
            id=id,
            type=cap_part,
            workingHours=working_hours,
            position = pos,
            maxTime = max_time,
            maxDistance = max_distance
            
            )
        
        return res_instance

    @staticmethod
    def default_test_workinghours():
        zone = "Europe/Berlin"
        num_days = 5
        return [TestElementsCreator.create_working_hours(
                    datetime(2030, 1, 1, 8, 0) + timedelta(days=ii),
                    datetime(2030, 1, 1, 20, 0) + timedelta(days=ii),
                    zone) 
                for ii in range(num_days)]

    @staticmethod
    def create_working_hours(begin, end, zone_id):
        return WorkingHours(begin=begin, end=end, zoneId=zone_id)


    # Node Creation

    @staticmethod
    def default_geo_node(pos, id, opening_hours=None) -> Node:
        
        if opening_hours is None:
            opening_hours = TestElementsCreator.default_test_opening_hours()
            
        visit_duration = "PT30M"
        priority = 1
        geo_part = GeoNode(position = pos, typeName = "Geo" )

        #print("geo_part test node: " + geo_part.to_str())

        node_instance = Node(
            id=id,
            type=geo_part,
            openingHours=opening_hours,
            visitDuration=visit_duration,
            priority = priority
            )
        
        return node_instance
    
    # @staticmethod
    # def default_geo_node2(pos, id, opening_hours=None) -> Node:
    #
    #     if opening_hours is None:
    #         opening_hours = TestElementsCreator.default_test_opening_hours()
    #
    #     # Create a Position instance
    #     position_instance = Position(
    #         latitude=51.0,
    #         longitude=52.0,
    #         locationId="TestNode"
    #     )
    #
    #     # Create a GeoNode instance
    #     geo_node_instance = GeoNode(
    #         position=position_instance,
    #         typeName="Geo"  # or another appropriate type name if needed
    #     )
    #
    #     #print(geo_node_instance)
    #
    #     # Create a Node instance
    #     node_instance = Node(
    #         id="your_node_id",
    #         type=geo_node_instance,
    #         openingHours=opening_hours,  # your opening hours data
    #         visitDuration="PT30M",
    #         priority=1,
    #         # include other necessary attributes here
    #     )
    #
    #     #print(node_instance)
    #
    #     return node_instance
        

    @staticmethod
    def default_test_opening_hours():
        zone = "Europe/Berlin"
        num_days = 5
        return [TestElementsCreator.create_opening_hours(
                        datetime(2030, 1, 1, 8, 0) + timedelta(days=ii),
                        datetime(2030, 1, 1, 20, 0) + timedelta(days=ii),
                        zone) 
                    for ii in range(num_days)]
        
    @staticmethod    
    def create_opening_hours(begin, end, zone_id):
        return OpeningHours(begin=begin, end=end, zoneId=zone_id)
    
    
## ------- Main program -------
if __name__ == "__main__":

    node = TestElementsCreator.default_geo_node(Position(latitude=51.0, longitude=52.0, locationId="TestNode"), "TestNode")
    print("Created test node:")
    print(node)
    
    # res = TestElementsCreator.default_capacity_resource(Position(latitude=51.0, longitude=52.0), "TestRes")
    # print("Created test res: " + res.to_str())
    #
    # ress = TestElementsCreator.conv_poss_to_ress(TestPositionsInput.default_sydney_resource_positions())
    # print("Created test ress: " + TestElementsCreator.ress_to_string(ress))
    #
    # nodes = TestElementsCreator.conv_poss_to_nodes(TestPositionsInput.default_sydney_node_positions())
    # print("Created test nodes: " + TestElementsCreator.nodes_to_string(nodes))
