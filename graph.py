from networkx import Graph

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
            self.graph.add_node(node.get('device_id'), **node)

    def update_links(self, links=[]):
        """Update all links inside the graph."""
        if not links:
            return

        for link in links:
            source = link.get('source')
            destination = link.get('destination')
            self.graph.add_edge(source, destination, object=link)

    def short_path(self):
        """Calculate the short path and return it."""
        pass
