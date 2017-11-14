import networkx as nx
from networkx.exception import NodeNotFound, NetworkXNoPath


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
        if hasattr(topology, 'circuits'):
            self.set_links_properties(topology.circuits)

    def update_nodes(self, nodes):
        """Update all nodes inside the graph."""
        for node in nodes:
            try:
                self.graph.add_node(node.id)

                for interface in node.interfaces.values():
                    self.graph.add_node(interface.id)
                    self.graph.add_edge(node.id, interface.id)

            except AttributeError:
                pass

    def update_links(self, links):
        """Update all links inside the graph."""
        for source, destination in links:
            self.graph.add_edge(source, destination)

    def set_links_properties(self, circuits):
        """Set properties for links in the graph."""
        for circuit in circuits:
            self._remove_switch_hops(circuit)
            if len(circuit['hops']) == 2:
                self.set_link_properties(circuit)
        if circuits:
            self._set_switch_links_properties(circuits[0]['custom_properties'])

    def set_link_properties(self, circuit):
        """Set properties for a single link in the graph."""
        hop_a = circuit['hops'][0]
        hop_b = circuit['hops'][1]
        if [hop_a, hop_b] in self.graph.edges:
            for prop, value in circuit['custom_properties'].items():
                self.graph[hop_a][hop_b][prop] = value

    def _set_switch_links_properties(self, properties):
        """Set properties to interface-to-switch link abstractions.

        The value is zero to make those irrelevant in pathfinding.
        """
        for prop in properties:
            for a,b in self.graph.edges:
                if prop not in self.graph[a][b]:
                    self.graph[a][b][prop] = 0


    @staticmethod
    def _remove_switch_hops(circuit):
        """Remove switch hops from a circuit hops list."""
        for hop in circuit['hops']:
            if len(hop.split(':')) == 8:
                circuit['hops'].remove(hop)

    def shortest_paths(self, source, destination, parameter=None):
        """Calculate the shortest paths and return them."""
        try:
            paths = list(nx.shortest_simple_paths(self.graph,
                                                  source,
                                                  destination, parameter))
        except (NodeNotFound, NetworkXNoPath):
            return []
        return paths
