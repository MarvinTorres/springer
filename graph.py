import networkx as nx
from networkx.exception import NodeNotFound, NetworkXNoPath
from kytos.core.switch import Switch

class KytosGraph:

    def __init__(self):
        self.graph = nx.Graph()

    def clear(self):
        """Remove all nodes and links registered."""
        self.graph.clear()

    def update_topology(self, topology):
        """Update all nodes and links inside the graph."""
        self.graph.clear()
        self.update_nodes(topology.devices)
        self.update_links(topology.links)

    def update_nodes(self, nodes):
        """Update all nodes inside the graph."""
        for node in nodes:
            self.graph.add_node(node.id)

    def update_links(self, links):
        """Update all links inside the graph."""
        for source, destination in links:

            node_id = self.node_from_id(source)
            self.graph.add_node(source)
            self.graph.add_edge(node_id, source)

            node_id = self.node_from_id(destination)
            self.graph.add_node(destination)
            self.graph.add_edge(node_id, destination)

            self.graph.add_edge(source, destination)

    def node_from_id(self, identifier):
        """Get a node based on source or destination identifier."""
        if len(identifier) > 17:
            return ':'.join(identifier.split(':')[:-1])
        return identifier

    def shortest_paths(self, source, destination):
        """Calculate the shortest paths and return them."""
        try:
            paths = list(nx.shortest_simple_paths(self.graph,
                                                  source,
                                                  destination))
        except (NodeNotFound, NetworkXNoPath):
            return []
        return paths
