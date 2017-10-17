########
Overview
########

.. attention::

    THIS NAPP IS STILL EXPERIMENTAL AND IT'S EVENTS, METHODS AND STRUCTURES MAY
    CHANGE A LOT ON THE NEXT FEW DAYS/WEEKS, USE IT AT YOUR OWN DISCERNEMENT

The NApp **kytos/pathfinder** is a NApp responsible to create a graph using the
devices and links belong to the network and provide a rest endpoints to
calculate the best path between two devices. In the graph of the network each
device represents a node and each link represents a edge between two nodes. In
the network each device is a host or a switch and each link is a connection
between two devices.

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
Listen the event reporting that the topology was updated. With the most updated
topology this NApp will create a graph to be easy to calculate the best paths.

Content
-------

.. code-block:: python3

  {
    'devices': [<list_of_devices>]
    'links': [<list_of_links_between_interfaces>]
  }

########
Rest API
########

You can find a list of the available endpoints and example input/output in the
'REST API' tab in this NApp's webpage in the `Kytos NApps Server
<https://napps.kytos.io/kytos/pathfinder>`_.
