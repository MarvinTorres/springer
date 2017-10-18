from networkx import Graph, shortest_path
from networkx.exception import NodeNotFound, NetworkXNoPath
from kytos.core.switch import Switch

class KytosGraph:

    graph = None

    def __init__(self):
        self.graph = Graph()

    def clear(self):
        """Remove all nodes and links registered."""
        self.graph.clear()

    def update_nodes(self, nodes=[]):
        """Update all nodes inside the graph."""
        if not nodes:
            return
        for node in nodes:
            if isinstance(node, Switch):
                node_id = node.dpid
            else:
                node_id = node.id
            self.graph.add_node(node_id)

    def update_links(self, links=[]):
        """Update all links inside the graph."""
        if not links:
            return
        for source, destination in links:

            node_id = self.node_from_id(source)
            self.graph.add_edge(node_id, source)

            node_id = self.node_from_id(destination)
            self.graph.add_edge(node_id, destination)

            self.graph.add_edge(source, destination)

    def node_from_id(self, identifier):
        """Get a node based on source or destination identifier."""
        if len(identifier) > 17:
            return ':'.join(identifier.split(':')[:-1])
        return identifier

    def shortest_path(self, source, destination):
        """Calculate the shortest path and return it."""
        path = None
        try:
            path = shortest_path(self.graph, source, destination)
        except (NodeNotFound, NetworkXNoPath):
            path = f"The shortest path between {source} and {destination}"
            path += " can't be found."
        return path
