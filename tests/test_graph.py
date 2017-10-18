"""Module to test the KytosGraph in graph.py."""
from unittest import TestCase
from unittest.mock import Mock

from graph import KytosGraph


class TestKytosGraph(TestCase):
    """Class to test KytosGraph class."""

    def setUp(self):
        """Create a custom KytosGraph, nodes and links.

        1      2      3       4     5
        0 ---- 0 ---- 0 ----- 0 --- 0
               |              |
               ---------------
        """
        self.graph = KytosGraph()
        self.nodes = self.create_custom_nodes()
        self.links = self.create_custom_links()

    @staticmethod
    def create_custom_nodes():
        """Create custom nodes."""
        nodes = []
        for number in range(1, 6):
            device_id = "00:00:00:00:00:00:00:0"+str(number)
            ports = [{'number': 65534}, {'number': 1},
                     {'number': 2}, {'number': 3}]
            node = Mock(device_id=device_id, ports=ports)
            nodes.append(node)
        return nodes

    def create_custom_links(self):
        """Create custom links between nodes."""
        links = []
        for number in range(1, 3):
            interface_one = Mock(device=self.nodes[number], port_id=2)
            interface_two = Mock(device=self.nodes[number+1], port_id=1)
            link = Mock(interface_one=interface_one,
                        interface_two=interface_two)
            links.append(link)

        interface_one = Mock(device=self.nodes[1], port_id=3)
        interface_two = Mock(device=self.nodes[3], port_id=3)
        shortest_link = Mock(interface_one=interface_one,
                             interface_two=interface_two)
        links.append(shortest_link)

        interface_one = Mock(device=self.nodes[0], port_id=1)
        interface_two = Mock(device=self.nodes[1], port_id=1)
        host_link = Mock(interface_one=interface_one,
                         interface_two=interface_two)
        links.append(host_link)

        interface_one = Mock(device=self.nodes[3], port_id=1)
        interface_two = Mock(device=self.nodes[4], port_id=2)
        host_link = Mock(interface_one=interface_one,
                         interface_two=interface_two)
        links.append(host_link)

        return links

    def test_update_nodes(self):
        """Test update nodes using custom_nodes."""
        self.graph.update_nodes(self.nodes)
        self.assertEqual(self.graph.graph.number_of_nodes(), 5)

    def test_update_links(self):
        """Test update links between nodes using custom links."""
        self.graph.update_links(self.links)
        self.assertEqual(self.graph.graph.number_of_edges(), 5)

    def test_shortest_path(self):
        """Test calculate shortest path with valid source and destination."""
        self.graph.update_nodes(self.nodes)
        self.graph.update_links(self.links)
        path = self.graph.shortest_path('00:00:00:00:00:00:00:01',
                                        '00:00:00:00:00:00:00:05')
        expected_path = ['00:00:00:00:00:00:00:01', '00:00:00:00:00:00:00:02',
                         '00:00:00:00:00:00:00:04', '00:00:00:00:00:00:00:05']
        self.assertEqual(path, expected_path)

    def test_unreachable_path(self):
        """Test calculate shorts path with invalid destination."""
        self.graph.update_nodes(self.nodes)
        self.graph.update_links(self.links)
        source = '00:00:00:00:00:00:00:01'
        destination = '00:00:00:00:00:00:00:06'
        path = self.graph.shortest_path(source, destination)
        expected_path = "The shortest path between {} and {} can't be found."
        self.assertEqual(expected_path.format(source, destination), path)
