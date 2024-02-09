import time
import json

from touroptimizer_py_client.models.geo_node import GeoNode
from touroptimizer_py_client.models.node import Node

from touroptimizer_py_client.models.capacity_resource import CapacityResource
from touroptimizer_py_client.models.resource import Resource

from datetime import datetime, timedelta

from touroptimizer_py_client.models.position import Position

from touroptimizer_py_client.models.node_type import NodeType

from touroptimizer_py_client.models.opening_hours import OpeningHours
from touroptimizer_py_client.models.working_hours import WorkingHours

from touroptimizer_py_client.models.optimization_options import OptimizationOptions
from touroptimizer_py_client.models.optimization_key_setting import OptimizationKeySetting
from touroptimizer_py_client.models.json_config import JSONConfig
from touroptimizer_py_client.models.rest_optimization import RestOptimization

from util.test_element_creator import TestElementsCreator
from util.test_position_input import TestPositionsInput

from typing import List


class TestRestOptimizationCreator:
    PUBLIC_JSON_LICENSE = json.dumps({
        "version": "1.1",
        "identifier": "PUBLIC-",
        "description": "Key provided to for evaluation purpose from DNA evolutions GmbH.",
        "contact": "www.dna-evolutions.com",
        "modules": [
            {"Module:": "Elements", "max": 15},
            {"Module:": "Date", "creation": "2021-05-25", "due": "2027-05-25"}
        ],
        "key": "PUBLIC-bc799ef350fe9841c1354736d8f863cb85bac88cefd19960c1"
    })
    
    @staticmethod
    def default_touroptimizer_position_test_input(node_positions: List[Position], 
                                         ress_positions: List[Position], 
                                         node_relations=[], 
                                         element_connections=[], 
                                         json_license=None) -> RestOptimization:
        
        
        ress = TestElementsCreator.conv_poss_to_ress(ress_positions)
        nodes = TestElementsCreator.conv_poss_to_nodes(node_positions)
            
        return TestRestOptimizationCreator.default_touroptimizer_test_input(nodes, ress, node_relations, element_connections, json_license)
        

    @staticmethod
    def default_touroptimizer_test_input(nodes: List[Node], ress: List[Resource], 
                                         node_relations=[], element_connections=[], 
                                         json_license=None) -> RestOptimization:
        if json_license is None:
            json_license = TestRestOptimizationCreator.PUBLIC_JSON_LICENSE

        ident = "StandardTouroptimizerTestInput"
        time_out = "PT2H"

        optimization_options = OptimizationOptions(properties=TestRestOptimizationCreator.default_optimization_options_properties())
        key_setting = OptimizationKeySetting(jsonLicense=json_license)
        extension = JSONConfig(keySetting=key_setting, timeOut=time_out)

        # node_relations = []
        # element_connections = []

        my_opti = RestOptimization(
           ident=ident,
           nodes=nodes,
           resources=ress,
           nodeRelations=node_relations,
           elementConnections=element_connections,
           optimizationOptions=optimization_options
           )
        
        my_opti.extension = extension

        return my_opti

    @staticmethod
    def default_optimization_options_properties():
        optimization_options_properties = {}
        optimization_options_properties["JOpt.Algorithm.PreOptimization.SA.NumIterations"] = "100000"
        optimization_options_properties["JOptExitCondition.JOptGenerationCount"] = "1000"

        return optimization_options_properties
    
    
## ------- Main program -------
if __name__ == "__main__":
    
    ress = TestElementsCreator.conv_poss_to_ress(TestPositionsInput.default_sydney_resource_positions())
    nodes = TestElementsCreator.conv_poss_to_nodes(TestPositionsInput.default_sydney_node_positions())
    
    print("Created Nodes for Rest Optimization")
    
    opti = TestRestOptimizationCreator.default_touroptimizer_test_input(nodes, ress)
    
    print("Created Rest Optimization")
    print(opti)
