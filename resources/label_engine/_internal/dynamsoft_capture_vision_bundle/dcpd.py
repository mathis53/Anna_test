__version__ = "3.0.30.9454"

if __package__ or "." in __name__:
    from . import _DynamsoftCodeParserDedicator
else:
    import _DynamsoftCodeParserDedicator


class DynamsoftCodeParserDedicatorModule:
    """
    The DynamsoftCodeParserDedicatorModule class represents the Dynamsoft Code Parser Dedicator module.
    """
    @staticmethod
    def get_version() -> str:
        """
        Gets the version of the Dynamsoft Code Parser Dedicator module.

        Returns:
            A string representing the version of the Dynamsoft Code Parser Dedicator module.
        """
        return __version__ + " (Algorithm " + _DynamsoftCodeParserDedicator.getversion() + ")"
