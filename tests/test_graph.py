"""Module to test the Graph"""
import unittest
from graph import KytosGraph

class TestKytosGraph(unittest.TestCase):
    """Class to test KytosGraph class."""

    def setUp(self):
        """Create a custom KytosGraph, nodes and links.

           1      2      3       4       5
           0 ---- 0 ---- 0 ----- 0 ----- 0
                  |              |
                  ---------------

        """
        self.graph = KytosGraph()
        self.custom_nodes = [
            { "device_id": "00:00:00:00:00:00:00:01", "ports": [1]},
            { "device_id": "00:00:00:00:00:00:00:02", "ports": [1,2]},
            { "device_id": "00:00:00:00:00:00:00:03", "ports": [1,2]},
            { "device_id": "00:00:00:00:00:00:00:04", "ports": [1,2]},
            { "device_id": "00:00:00:00:00:00:00:05", "ports": [1]}
        ]
        self.custom_links = [
            {'source': "00:00:00:00:00:00:00:01",
             'destination': "00:00:00:00:00:00:00:02",
             'custom_attributes': 0.05
            },
            {'source': "00:00:00:00:00:00:00:02",
             'destination': "00:00:00:00:00:00:00:03",
             'custom_attributes': 0.05
            },
            {'source': "00:00:00:00:00:00:00:03",
             'destination': "00:00:00:00:00:00:00:04",
             'custom_attributes': 0.05
            },
            {'source': "00:00:00:00:00:00:00:02",
             'destination': "00:00:00:00:00:00:00:04",
             'custom_attributes': 0.05
            },
            {'source': "00:00:00:00:00:00:00:04",
             'destination': "00:00:00:00:00:00:00:05",
             'custom_attributes': 0.05
            }
        ]

    def test_update_nodes_with_none(self):
        """Test update nodes with None."""
        self.graph.update_nodes(None)
        self.assertEqual(self.graph.graph.number_of_nodes(), 0)

    def test_update_links_with_none(self):
        """Test update links with None."""
        self.graph.update_links(None)
        self.assertEqual(self.graph.graph.number_of_edges(), 0)

    def test_update_nodes(self):
        """Test update nodes."""
        self.graph.update_nodes(self.custom_nodes)
        nodes = ["00:00:00:00:00:00:00:01", "00:00:00:00:00:00:00:02",
                 "00:00:00:00:00:00:00:03","00:00:00:00:00:00:00:04",
                 "00:00:00:00:00:00:00:05"]

        self.assertEqual(self.graph.graph.number_of_nodes(), 5)
        self.assertEqual(list(self.graph.graph.nodes), nodes)

    def test_update_nodes_with_attributes(self):
        """Test update nodes and verify the node attribute."""
        nodes = ["00:00:00:00:00:00:00:01", "00:00:00:00:00:00:00:02",
                 "00:00:00:00:00:00:00:03","00:00:00:00:00:00:00:04",
                 "00:00:00:00:00:00:00:05"]
        self.graph.update_nodes(self.custom_nodes)
        self.assertEqual(list(self.graph.graph.nodes), nodes)

        self.assertEqual(self.graph.graph.number_of_nodes(), 5)
        self.assertEqual(self.custom_nodes[0],
                         self.graph.graph.nodes["00:00:00:00:00:00:00:01"])
        self.assertEqual(self.custom_nodes[1],
                         self.graph.graph.nodes["00:00:00:00:00:00:00:02"])

    def test_update_links(self):
        """Test update links."""
        self.graph.update_nodes(self.custom_nodes)
        self.graph.update_links(self.custom_links)
        self.assertEqual(self.graph.graph.number_of_nodes(), 5)
        self.assertEqual(self.graph.graph.number_of_edges(), 5)


    def test_update_links_with_attributes(self):
        """Test update links and verify the edge attributes."""
        self.graph.update_nodes(self.custom_nodes)
        self.graph.update_links(self.custom_links)
        self.assertEqual(self.graph.graph.number_of_nodes(), 5)
        self.assertEqual(self.graph.graph.number_of_edges(), 5)

        edge = self.graph.graph.edges[("00:00:00:00:00:00:00:03",
                                      "00:00:00:00:00:00:00:04")]
        expected = {
                    'source': "00:00:00:00:00:00:00:03",
                    'destination': "00:00:00:00:00:00:00:04",
                    'custom_attributes': 0.05
                   }
        self.assertEqual(edge.get('object'), expected)
