"""Simple implementation of wlformat.prov_exe schema using dicts
"""


class Provenance(object):
    """Simple object to store provenance results
    """

    def __init__(self):
        pass

    def before_eval(self, df, vid):
        """Function called just before evaluating a node

        Args:
            df (CompositeNode): workflow currently under evaluation
            vid (vid): id of node to be evaluated

        Returns:
            None
        """
        pass

    def after_eval(self, df, vid):
        """Function called just after evaluating a node

        Args:
            df (CompositeNode): workflow currently under evaluation
            vid (vid): id of node to be evaluated

        Returns:
            None
        """
        pass
