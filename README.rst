########
Overview
########

.. attention::

    THIS NAPP IS STILL EXPERIMENTAL AND IT'S EVENTS, METHODS AND STRUCTURES MAY
    CHANGE A LOT ON THE NEXT FEW DAYS/WEEKS, USE IT AT YOUR OWN DISCERNEMENT

The NApp **kytos/pathfinder** is a NApp responsible for creating a graph with
the latest network topology and providing rest endpoint to calculate the best
path between two devices. In the network, each device is a host or a switch and
each link is a connection between two devices. In the graph, each device
represents a node and each link represents an edge between two nodes.

The NApp learns custom properties from the topology, being able to define the
best paths based on a weighted parmeter. Please see the Rest API documentation
for details.

##########
Installing
##########

All of the Kytos Network Applications are located in the NApps online
repository. To install this NApp, run:

.. code:: shell

   $ kytos napps install kytos/pathfinder

######
Events
######

******
Listen
******

kytos/topology.updated
======================

*buffer*: ``app``

Listening on this event will make sure that this NApp has the lateste topology.


Content
-------

.. code-block:: python3

  {
    'topology': <Topology object>
  }

########
Rest API
########

You can find a list of the available endpoints and example input/output in the
'REST API' tab in this NApp's webpage in the `Kytos NApps Server
<https://napps.kytos.io/kytos/pathfinder>`_.
