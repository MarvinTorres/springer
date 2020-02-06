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

    def test_setup(self):
        """Created to debug the test setup"""
        self.setup()
        print(self.graph.graph)



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

        links = {}

        links["S1-L1<->S2-L1"] = Link(interfaces["S1-L1"], interfaces["S2-L1"])
        links["S3-L1<->S2-L2"] = Link(interfaces["S3-L1"], interfaces["S2-L2"])
        links["S1-L2<->S3-L2"] = Link(interfaces["S1-L2"], interfaces["S3-L2"])

        return (switches,links)

    @staticmethod
    def createSwitch(name,switches):
        switches[name] = Switch(name)
        print("Creating Switch: ", name)

    @staticmethod
    def addInterfaces(count,switch,interfaces):
        for x in range(1,count + 1):
            str1 = "{}-L{}".format(switch.dpid,x)
            print("Creating Interface: ", str1)
            iFace = Interface(str1,x,switch)
            interfaces[str1] = iFace
            switch.update_interface(iFace)

