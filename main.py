"""Main module of kytos/pathfinder Kytos Network Application."""

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to
from napps.kytos.pathfinder import settings
from napps.kytos.pathfinder.graph import KytosGraph

class Main(KytosNApp):
    """Main class of kytos/pathfinder NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Create a graph to handle the nodes and edges."""
        self.graph = KytosGraph()

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        pass

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass

    @rest('<source>/<destination>')
    def short_path(self, source, destination):
        """Calculate the best path between the source and destination."""
        return self.graph.short_path()

    @listen_to('kytos/topology.updated')
    def update_topology(self, event):
        """Update the graph when the network topology was updated.

        Clear the current graph and create a new with the most topoly updated.
        """
        topology = event.content.get('topology', {})
        if not topology:
            return
        self.graph.clear()
        self.graph.update_nodes(topology.get('devices',[]))
        self.graph.update_links(topology.get('links',[]))
