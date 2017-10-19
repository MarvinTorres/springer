"""Main module of kytos/pathfinder Kytos Network Application."""

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to

# pylint: disable=import-error
from napps.kytos.pathfinder.graph import KytosGraph

# pylint: enable=import-error


class Main(KytosNApp):
    """Main class of kytos/pathfinder NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Create a graph to handle the nodes and edges."""
        self.graph = KytosGraph()

    def execute(self):
        """Do nothing."""
        pass

    def shutdown(self):
        """Shutdown the napp."""
        pass

    @rest('<source>/<destination>')
    def shortest_path(self, source, destination):
        """Calculate the best path between the source and destination."""
        return str(self.graph.shortest_path(source, destination))

    @listen_to('kytos.topology.updated')
    def update_topology(self, event):
        """Update the graph when the network topology was updated.

        Clear the current graph and create a new with the most topoly updated.
        """
        if 'topology' not in event.content:
            return
        topology = event.content['topology']
        self.graph.clear()
        self.graph.update_nodes(topology.devices)
        self.graph.update_links(topology.links)
        log.debug('Topology updated.')
