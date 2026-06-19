__version__ = "3.0.30.9454"

if __package__ or "." in __name__:
    from . import _DynamsoftImageProcessing
else:
    import _DynamsoftImageProcessing


class DynamsoftImageProcessingModule:
    """
    The DynamsoftImageProcessingModule class represents the Dynamsoft Image Processing module.

    Methods:
        get_version() -> str: Gets the version of the Dynamsoft Image Processing module.
    """
    @staticmethod
    def get_version() -> str:
        """
        Gets the version of the Dynamsoft Image Processing module.

        Returns:
            A string representing the version of the Dynamsoft Image Processing module.
        """
        return __version__ + " (Algorithm " + _DynamsoftImageProcessing.getversion() + ")"
