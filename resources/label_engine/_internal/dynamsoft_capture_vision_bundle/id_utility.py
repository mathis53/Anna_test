__version__ = "1.0.10.9454"

if __package__ or "." in __name__:
    from .cvr import *
else:
    from cvr import *

if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftIdentityUtility
else:
    import _DynamsoftIdentityUtility
from typing import Tuple
class IdentityUtilityModule:
    """
    The IdentityUtilityModule class provides common functions of the identity utility module.

    Methods:
        get_version() -> str: Returns the version of the identity utility module.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns the version of the identity utility module.

        Returns:
            A string representing the version of the identity utility module.
        """
        return __version__ + " (Algorithm " + _DynamsoftIdentityUtility.CIdentityUtilityModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftIdentityUtility.Class_init(
            self, _DynamsoftIdentityUtility.new_CIdentityUtilityModule()
        )

    __destroy__ = _DynamsoftIdentityUtility.delete_CIdentityUtilityModule

_DynamsoftIdentityUtility.CIdentityUtilityModule_register(IdentityUtilityModule)

class IdentityProcessor:
    """
    The IdentityProcessor class provides functions to process identity documents, such as locating portrait zones with higher precision.

    Methods:
        find_portrait_zone(
            self,
            scaled_colour_img_unit: ScaledColourImageUnit,
            localized_text_lines_unit: LocalizedTextLinesUnit,
            recognized_text_lines_unit: RecognizedTextLinesUnit,
            detected_quads_unit: DetectedQuadsUnit,
            deskewed_image_unit: DeskewedImageUnit
        ) -> Tuple[int, Quadrilateral]: Finds the location of the portrait zone on an identity document.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftIdentityUtility.Class_init(
            self, _DynamsoftIdentityUtility.new_CIdentityProcessor()
        )

    __destroy__ = _DynamsoftIdentityUtility.delete_CIdentityProcessor

    def find_portrait_zone(
        self,
        scaled_colour_img_unit:'ScaledColourImageUnit',
        localized_text_lines_unit:'LocalizedTextLinesUnit',
        recognized_text_lines_unit: 'RecognizedTextLinesUnit',
        detected_quads_unit:'DetectedQuadsUnit',
        deskewed_image_unit:'DeskewedImageUnit'
    ) -> Tuple[int, 'Quadrilateral']:
        """
       Finds the location of the portrait zone on an identity document.

        Args:
            scaled_colour_img_unit(ScaledColourImageUnit): The scaled colour image unit containing the source image.
            localized_text_lines_unit(LocalizedTextLinesUnit): The localized text lines unit containing MRZ/text regions.
            recognized_text_lines_unit(RecognizedTextLinesUnit): The recognized text lines unit for document type identification.
            detected_quads_unit(DetectedQuadsUnit): The detected quads unit containing document boundaries.
            deskewed_image_unit(DeskewedImageUnit): The deskewed image unit for coordinate transformation.

        Returns:
            error_code(int): Returns 0 if successful, otherwise returns an error code.
            portrait_zone(Quadrilateral): The output quadrilateral representing the portrait zone location. Returns None if not found.
        """
        return _DynamsoftIdentityUtility.CIdentityProcessor_FindPortraitZone(
            self, scaled_colour_img_unit, localized_text_lines_unit, recognized_text_lines_unit, detected_quads_unit, deskewed_image_unit
        )
_DynamsoftIdentityUtility.CIdentityProcessor_register(IdentityProcessor)