"""Simple implementation of wlformat.prov_exe schema using dicts
"""


class Provenance(object):
    """Simple object to store provenance results
    """

    def __init__(self):
        self.workflow = None
        self.time_init = None
        self.time_end = None

    def init(self, dataflow):
        """Initialize the provenance with a new dataflow

        Args:
            dataflow (CompositeNode): workflow currently under evaluation

        Returns:
            None
        """
        print "init prov", id(dataflow)

    def before_eval(self, dataflow, vid):
        """Function called just before evaluating a node

        Args:
            dataflow (CompositeNode): workflow currently under evaluation
            vid (vid): id of node to be evaluated

        Returns:
            None
        """
        print "bef eval", id(dataflow), vid

    def after_eval(self, dataflow, vid):
        """Function called just after evaluating a node

        Args:
            dataflow (CompositeNode): workflow currently under evaluation
            vid (vid): id of node to be evaluated

        Returns:
            None
        """
        print "aft eval", id(dataflow), vid
