"""Module to test Pathfinder"""
from unittest import TestCase
from unittest.mock import Mock

from flask import request

from graph import KytosGraph
from main import Main

# from napps.kytos.topology import settings
from napps.kytos.topology.models import Topology


# Need to figure out an alternative
from kytos.core.switch import Switch
from kytos.core.interface import Interface
from kytos.core.link import Link

class TestPathfinder(TestCase):

    def restEmptyRequestTest(self):
        """Tests calling the rest API when request body is empty"""
        result = None
        main = Main()
        main.setup()

        with test_request_context():
            result = main.get_path()

    @staticmethod
    def generateTopology():
        """Generates a predetermined topology"""
        switches = {}
        interfaces = {}

        createSwitch("S1",switches)
        addInterfaces(2, switches["S1"], interfaces)

        createSwitch("S2",switches)
        addInterfaces(3, switches["S2"], interfaces)

        createSwitch("S3",switches)
        addInterfaces(2, switches["S2"], interfaces)

        links = {}

        links["S1-L1<->S2-L1"] = Link(interfaces["S1-L1"], interfaces["S2-L1"])
        links["S3-L1<->S2-L2"] = Link(interfaces["S3-L1"], interfaces["S2-L2"])
        links["S1-L2<->S3-L2"] = Link(interfaces["S1-L2"], interfaces["S3-L2"])

        return Topology(switches,links)

    @staticmethod
    def createSwitch(name,switches):
        switches[name] = Switch(name)

    @staticmethod
    def addInterfaces(count,switch,interfaces):
        str0 = "{}-{}".format(switch.dpid)
        for x in range(1,count):
            str1 = str0.format(x)
            iFace = Interface(str1,x,switch)
            interfaces[str1] = iFace
            switch.update_interface(iFace)

