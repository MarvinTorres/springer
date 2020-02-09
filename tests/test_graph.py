"""Module to test the KytosGraph in graph.py."""
from unittest import TestCase
from unittest.mock import Mock

from flask import request

# module under test
from graph import KytosGraph

# Core modules to import
from kytos.core.switch import Switch
from kytos.core.interface import Interface
from kytos.core.link import Link
from kytos.core import KytosEvent

class TestKytosGraph(TestCase):

    def setup(self):
        """Setup for most tests"""
        switches, links = self.generateTopology()
        self.graph = KytosGraph()
        self.graph.clear()
        self.graph.update_nodes(switches)
        self.graph.update_links(links)

    def get_path(self, source, destination):
        print(f"Attempting path between {source} and {destination}.")
        result = self.graph.shortest_paths(source,destination)
        print(f"Path result: {result}")
        return result

    def test_setup(self):
        """Provides information on default test setup"""
        self.setup()
        print("Nodes in graph")
        for node in self.graph.graph.nodes:
            print(node)
        print("Edges in graph")
        for edge in self.graph.graph.edges:
            print(edge)
    
    def test_path1(self):
        """Tests a simple, definetly possible path"""
        self.setup()
        result = self.get_path("S1","S2")
        self.assertNotEqual(result, [])

    def test_path2(self):
        """Tests a simple, impossible path"""
        self.setup()
        result = self.get_path("S1","S4")
        self.assertEqual(result, [])



    @staticmethod
    def generateTopology():
        """Generates a predetermined topology"""
        switches = {}
        interfaces = {}

        TestKytosGraph.createSwitch("S1",switches)
        TestKytosGraph.addInterfaces(2, switches["S1"], interfaces)

        TestKytosGraph.createSwitch("S2",switches)
        TestKytosGraph.addInterfaces(3, switches["S2"], interfaces)

        TestKytosGraph.createSwitch("S3",switches)
        TestKytosGraph.addInterfaces(2, switches["S3"], interfaces)

        TestKytosGraph.createSwitch("S4",switches)
        TestKytosGraph.addInterfaces(2, switches["S4"], interfaces)

        links = {}

        links["S1:1<->S2:1"] = Link(interfaces["S1:1"], interfaces["S2:1"])
        links["S3:1<->S2:2"] = Link(interfaces["S3:1"], interfaces["S2:2"])
        links["S1:2<->S3:2"] = Link(interfaces["S1:2"], interfaces["S3:2"])

        return (switches,links)

    @staticmethod
    def createSwitch(name,switches):
        switches[name] = Switch(name)
        print("Creating Switch: ", name)

    @staticmethod
    def addInterfaces(count,switch,interfaces):
        for x in range(1,count + 1):
            str1 = "{}:{}".format(switch.dpid,x)
            print("Creating Interface: ", str1)
            iFace = Interface(str1,x,switch)
            interfaces[str1] = iFace
            switch.update_interface(iFace)

