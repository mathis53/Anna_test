__version__ = "4.0.30.9454"

if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftLabelRecognizer
else:
    import _DynamsoftLabelRecognizer

from typing import List,Tuple

from enum import IntEnum

class EnumRawTextLineStatus(IntEnum):
    RTLS_LOCALIZED = _DynamsoftLabelRecognizer.RTLS_LOCALIZED
    RTLS_RECOGNITION_FAILED = _DynamsoftLabelRecognizer.RTLS_RECOGNITION_FAILED
    RTLS_RECOGNITION_SUCCEEDED = _DynamsoftLabelRecognizer.RTLS_RECOGNITION_SUCCEEDED

class SimplifiedLabelRecognizerSettings:
    """
    The SimplifiedLabelRecognizerSettings class contains settings for label recognition.
    It is a sub-parameter of SimplifiedCaptureVisionSettings.

    Attributes:
        grayscale_transformation_modes(List[int]): Specifies how grayscale transformations should be applied, including whether to process inverted grayscale images and the specific transformation mode to use.
        grayscale_enhancement_modes(List[int]): Specifies how to enhance the quality of the grayscale image.
        character_model_name(str): Specifies a character model by its name.
        line_string_regex_pattern(str): Specifies the RegEx pattern of the text line string to filter out the unqualified results.
        max_threads_in_one_task(int): Specifies the maximum available threads count in one label recognition task.
        scale_down_threshold(int): Specifies the threshold for the image shrinking.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @property
    def grayscale_transformation_modes(self) -> List[int]:
        if not hasattr(self, "_grayscale_transformation_modes") or self._grayscale_transformation_modes is None:
            self._grayscale_transformation_modes = _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_grayscaleTransformationModes_get(self)
        return self._grayscale_transformation_modes
    @grayscale_transformation_modes.setter
    def grayscale_transformation_modes(self, value):
        if not hasattr(self, "_grayscale_transformation_modes") or self._grayscale_transformation_modes is None:
            self._grayscale_transformation_modes = _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_grayscaleTransformationModes_get(self)
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_grayscaleTransformationModes_set(self, value)
        self._grayscale_transformation_modes = value

    @property
    def grayscale_enhancement_modes(self) -> List[int]:
        if not hasattr(self, "_grayscale_enhancement_modes") or self._grayscale_enhancement_modes is None:
            self._grayscale_enhancement_modes = _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_grayscaleEnhancementModes_get(self)
        return self._grayscale_enhancement_modes
    @grayscale_enhancement_modes.setter
    def grayscale_enhancement_modes(self, value):
        if not hasattr(self, "_grayscale_enhancement_modes") or self._grayscale_enhancement_modes is None:
            self._grayscale_enhancement_modes = _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_grayscaleEnhancementModes_get(self)
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_grayscaleEnhancementModes_set(self, value)
        self._grayscale_enhancement_modes = value

    character_model_name: str = property(
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_characterModelName_get,
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_characterModelName_set,
        doc="Specifies a character model by its name.",
    )
    line_string_regex_pattern: str = property(
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_lineStringRegExPattern_get,
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_lineStringRegExPattern_set,
        doc="Specifies the RegEx pattern of the text line string to filter out the unqualified results.",
    )
    max_threads_in_one_task: int = property(
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_maxThreadsInOneTask_get,
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_maxThreadsInOneTask_set,
        doc="""
            Specifies the maximum available threads count in one label recognition task.
            Value Range: [1, 256]
            Default value: 4
            """,
    )
    scale_down_threshold: int = property(
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_scaleDownThreshold_get,
        _DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_scaleDownThreshold_set,
        doc="""
            Specifies the threshold for the image shrinking.
            Value Range: [512, 0x7fffffff]
            Default Value: 2300
            """,
    )

    def __init__(self):
        _DynamsoftLabelRecognizer.Class_init(
            self, _DynamsoftLabelRecognizer.new_SimplifiedLabelRecognizerSettings()
        )

    __destroy__ = _DynamsoftLabelRecognizer.delete_SimplifiedLabelRecognizerSettings


_DynamsoftLabelRecognizer.SimplifiedLabelRecognizerSettings_register(
    SimplifiedLabelRecognizerSettings
)

class CharacterResult:
    """
    The CharacterResult class represents the result of a character recognition process.
    It contains the characters recognized (high, medium, and low confidence), their respective confidences, and the location of the character in a quadrilateral shape.

    Attributes:
        character_h(str): The character with high confidence.
        character_m(str): The character with medium confidence.
        character_l(str): The character with low confidence.
        location(Quadrilateral): The location of the character in a quadrilateral shape.
        character_h_confidence(int): The confidence of the character with high confidence.
        character_m_confidence(int): The confidence of the character with medium confidence.
        character_l_confidence(int): The confidence of the character with low confidence.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    character_h: str = property(
        _DynamsoftLabelRecognizer.CCharacterResult_characterH_get,
        _DynamsoftLabelRecognizer.CCharacterResult_characterH_set,
        doc="The character with high confidence."
    )
    character_m: str = property(
        _DynamsoftLabelRecognizer.CCharacterResult_characterM_get,
        _DynamsoftLabelRecognizer.CCharacterResult_characterM_set,
        doc="The character with medium confidence."
    )
    character_l: str = property(
        _DynamsoftLabelRecognizer.CCharacterResult_characterL_get,
        _DynamsoftLabelRecognizer.CCharacterResult_characterL_set,
        doc="The character with low confidence."
    )
    location: Quadrilateral = property(
        _DynamsoftLabelRecognizer.CCharacterResult_location_get,
        _DynamsoftLabelRecognizer.CCharacterResult_location_set,
        doc="The location of the character in a quadrilateral shape."
    )
    character_h_confidence: int = property(
        _DynamsoftLabelRecognizer.CCharacterResult_characterHConfidence_get,
        _DynamsoftLabelRecognizer.CCharacterResult_characterHConfidence_set,
        doc="The confidence of the character with high confidence."
    )
    character_m_confidence: int = property(
        _DynamsoftLabelRecognizer.CCharacterResult_characterMConfidence_get,
        _DynamsoftLabelRecognizer.CCharacterResult_characterMConfidence_set,
        doc="The confidence of the character with medium confidence."
    )
    character_l_confidence: int = property(
        _DynamsoftLabelRecognizer.CCharacterResult_characterLConfidence_get,
        _DynamsoftLabelRecognizer.CCharacterResult_characterLConfidence_set,
        doc="The confidence of the character with low confidence."
    )

    def __init__(self):
        _DynamsoftLabelRecognizer.Class_init(
            self, _DynamsoftLabelRecognizer.new_CCharacterResult()
        )

    __destroy__ = _DynamsoftLabelRecognizer.delete_CCharacterResult


_DynamsoftLabelRecognizer.CCharacterResult_register(CharacterResult)

class TextLineResultItem(CapturedResultItem):
    """
    The TextLineResultItem class represents a text line result item recognized by the library. It is derived from CapturedResultItem.

    Methods:
        get_text(self) -> str: Gets the text content of the text line.
        get_location(self) -> Quadrilateral: Gets the location of the text line in the form of a quadrilateral.
        get_confidence(self) -> int: Gets the confidence of the text line recognition result.
        get_character_results(self) -> List[CharacterResult]: Gets all the character results.
        get_specification_name(self) -> str: Gets the name of the text line specification that generated this item.
        get_raw_text(self) -> str: Gets the recognized raw text, excluding any concatenation separators.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_text(self) -> str:
        """
        Gets the text content of the text line.

        Returns:
            The text content of the text line.
        """
        return _DynamsoftLabelRecognizer.CTextLineResultItem_GetText(self)

    def get_location(self) -> Quadrilateral:
        """
        Gets the location of the text line in the form of a quadrilateral.

        Returns:
            The location of the text line in the form of a quadrilateral.
        """
        return _DynamsoftLabelRecognizer.CTextLineResultItem_GetLocation(self)

    def get_confidence(self) -> int:
        """
        Gets the confidence of the text line recognition result.

        Returns:
            The confidence of the text line recognition result.
        """
        return _DynamsoftLabelRecognizer.CTextLineResultItem_GetConfidence(self)

    def get_character_results(self) -> List[CharacterResult]:
        """
        Gets all the character results.

        Returns:
            All the character results as a CharacterResult list.
        """
        list = []
        count = _DynamsoftLabelRecognizer.CTextLineResultItem_GetCharacterResultsCount(
            self
        )
        for i in range(count):
            list.append(
                _DynamsoftLabelRecognizer.CTextLineResultItem_GetCharacterResult(
                    self, i
                )
            )
        return list

    def get_specification_name(self) -> str:
        """
        Gets the name of the text line specification that generated this item.

        Returns:
            The name of the text line specification that generated this item.
        """
        return _DynamsoftLabelRecognizer.CTextLineResultItem_GetSpecificationName(self)

    def get_raw_text(self) -> str:
        """
        Gets the recognized raw text, excluding any concatenation separators.

        Returns:
            The recognized raw text.
        """
        return _DynamsoftLabelRecognizer.CTextLineResultItem_GetRawText(self)


_DynamsoftLabelRecognizer.CTextLineResultItem_register(TextLineResultItem)


class RecognizedTextLinesResult(CapturedResultBase):
    """
    The RecognizedTextLinesResult class represents the result of a text recognition process.
    It provides access to information about the recognized text lines, the original image, and any errors that occurred during the recognition process.

    Methods:
        get_items(self) -> List[TextLineResultItem]: Gets all the text line result items.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftLabelRecognizer.CRecognizedTextLinesResult_Release

    def get_items(self) -> List[TextLineResultItem]:
        """
        Gets all the text line result items.

        Returns:
            A TextLineResultItem list.
        """
        list = []
        count = _DynamsoftLabelRecognizer.CRecognizedTextLinesResult_GetItemsCount(self)
        for i in range(count):
            list.append(
                _DynamsoftLabelRecognizer.CRecognizedTextLinesResult_GetItem(self, i)
            )
        return list

_DynamsoftLabelRecognizer.CRecognizedTextLinesResult_register(RecognizedTextLinesResult)


class LabelRecognizerModule:
    """
    The LabelRecognizerModule class represents a label recognizer module.

    Methods:
        get_version() -> str: Gets the version of the label recognizer module.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Gets the version of the label recognizer module.

        Returns:
            A string representing the version of the label recognizer module.
        """
        return __version__ + " (Algorithm " + _DynamsoftLabelRecognizer.CLabelRecognizerModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftLabelRecognizer.Class_init(
            self, _DynamsoftLabelRecognizer.new_CLabelRecognizerModule()
        )

    __destroy__ = _DynamsoftLabelRecognizer.delete_CLabelRecognizerModule


_DynamsoftLabelRecognizer.CLabelRecognizerModule_register(LabelRecognizerModule)


class BufferedCharacterItem:
    """
    The BufferedCharacterItem class represents a text line result item recognized by the library. It is derived from CapturedResultItem.

    Methods:
        get_character(self) -> str: Gets the buffered character value.
        get_image(self) -> ImageData: Gets the image data of the buffered character.
        get_features(self) -> List[Tuple[int, float]]: Gets all the features formatted with id and value of the buffered character.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftLabelRecognizer.delete_CBufferedCharacterItem

    def get_character(self) -> str:
        """
        Gets the buffered character value.

        Returns:
            The buffered character value.
        """
        return _DynamsoftLabelRecognizer.CBufferedCharacterItem_GetCharacter(self)

    def get_image(self) -> ImageData:
        """
        Gets the image data of the buffered character.

        Returns:
            The image data of the buffered character.
        """
        return _DynamsoftLabelRecognizer.CBufferedCharacterItem_GetImage(self)

    def get_features(self) -> List[Tuple[int, float]]:
        """
        Gets all the features formatted with id and value of the buffered character.

        Returns:
            A tuple list while each item contains following elements.
            - feature_id <int>: The feature id.
            - feature_value <float>: The feature value.
        """
        list = []
        count = _DynamsoftLabelRecognizer.CBufferedCharacterItem_GetFeaturesCount(self)
        for i in range(count):
            err,id,feature = _DynamsoftLabelRecognizer.CBufferedCharacterItem_GetFeature(self, i)
            list.append([id,feature])
        return list


_DynamsoftLabelRecognizer.CBufferedCharacterItem_register(BufferedCharacterItem)


class CharacterCluster:
    """
    The CharacterCluster class represents a character cluster generated from the buffered character items. These buffered items will be clustered based on feature similarity to obtain cluster centers.

    Methods:
        get_character(self) -> str: Gets the character value of the cluster.
        get_mean(self) -> BufferedCharacterItem: Gets the mean of the cluster.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftLabelRecognizer.delete_CCharacterCluster

    def get_character(self) -> str:
        """
        Gets the character value of the cluster.

        Returns:
            The character value of the cluster.
        """
        return _DynamsoftLabelRecognizer.CCharacterCluster_GetCharacter(self)

    def get_mean(self) -> BufferedCharacterItem:
        """
        Gets the mean of the cluster.

        Returns:
            The mean of the cluster which is a BufferedCharacterItem object.
        """
        return _DynamsoftLabelRecognizer.CCharacterCluster_GetMean(self)


_DynamsoftLabelRecognizer.CCharacterCluster_register(CharacterCluster)


class BufferedCharacterItemSet:
    """
    The BufferedCharacterItemSet class represents a collection of buffered character items and associated character clusters.

    Methods:
        get_items(self) -> List[BufferedCharacterItem]: Gets all the buffered items.
        get_character_clusters(self) -> List[CharacterCluster]: Gets all the character clusters.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftLabelRecognizer.CBufferedCharacterItemSet_Release

    def get_items(self) -> List[BufferedCharacterItem]:
        """
        Gets all the buffered items.

        Returns:
            A BufferedCharacterItem list.
        """
        list = []
        count = _DynamsoftLabelRecognizer.CBufferedCharacterItemSet_GetItemsCount(self)
        for i in range(count):
            list.append(
                _DynamsoftLabelRecognizer.CBufferedCharacterItemSet_GetItem(self, i)
            )
        return list

    def get_character_clusters(self) -> List[CharacterCluster]:
        """
        Gets all the character clusters.

        Returns:
            A CharacterCluster list.
        """
        list = []
        count = _DynamsoftLabelRecognizer.CBufferedCharacterItemSet_GetCharacterClustersCount(
            self
        )
        for i in range(count):
            list.append(
                _DynamsoftLabelRecognizer.CBufferedCharacterItemSet_GetCharacterCluster(
                    self, i
                )
            )
        return list


_DynamsoftLabelRecognizer.CBufferedCharacterItemSet_register(BufferedCharacterItemSet)


#new

class LocalizedTextLineElement(RegionObjectElement):
    """
    The LocalizedTextLineElement class represents a localized text line element. It inherits from the RegionObjectElement class.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        _DynamsoftLabelRecognizer.Class_init(
            self, _DynamsoftLabelRecognizer.CLabelRecognizerModule_CreateLocalizedTextLineElement()
        )

    def get_character_quads_count(self) -> int:
        """
        Gets the number of character quads in the text line.

        Returns:
            The number of character quads in the text line.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLineElement_GetCharacterQuadsCount(self)

    def get_character_quad(self, index: int) -> Tuple[int, Quadrilateral]:
        """
        Gets the quadrilateral of a specific character in the text line.

        Args:
            index (int): The index of the character.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation, returns 0 if successful, otherwise returns a negative value.
            - quadrilateral (Quadrilateral): The quadrilateral of the character.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLineElement_GetCharacterQuad(self, index)

    def get_row_number(self) -> int:
        """
        Gets the row number of the text line.

        Returns:
            The row number of the text line.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLineElement_GetRowNumber(self)

    def set_location(self, location: Quadrilateral) -> int:
        """
        Sets the location of the text line.

        Args:
            location (Quadrilateral): The location of the text line.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLineElement_SetLocation(self, location)

_DynamsoftLabelRecognizer.CLocalizedTextLineElement_register(LocalizedTextLineElement)
class RecognizedTextLineElement(RegionObjectElement):
    """
    The RecognizedTextLineElement class represents a recognized text line element. It inherits from the RegionObjectElement class.

    Methods:
        get_text(self) -> str: Gets the recognized text.
        get_confidence(self) -> int: Gets the confidence level of the recognized text.
        get_character_results_count(self) -> int: Gets the number of individual character recognition results in the line.
        get_row_number(self) -> int: Gets the row number of the recognized text line.
        get_character_result(self, index: int) -> CharacterResult: Gets the character recognition result at the specified index.
        set_text(self, text: str): Sets the recognized text.
        get_specification_name(self) -> str: Gets the name of the text line specification that generated this element.
        get_raw_text(self) -> str: Gets the recognized raw text, excluding any concatenation separators.
        set_location(self, location: Quadrilateral) -> int: Sets the location of the recognized text line element.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        _DynamsoftLabelRecognizer.Class_init(
            self, _DynamsoftLabelRecognizer.CLabelRecognizerModule_CreateRecognizedTextLineElement()
        )

    def get_text(self) -> str:
        """
        Gets the recognized text.

        Returns:
            The recognized text.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetText(self)

    def get_confidence(self) -> int:
        """
        Gets the confidence level of the recognized text.

        Returns:
            The confidence level of the recognized text.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetConfidence(self)

    def get_character_results_count(self) -> int:
        """
        Gets the number of individual character recognition results in the line.

        Returns:
            The number of individual character recognition results in the line.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetCharacterResultsCount(self)

    def get_row_number(self) -> int:
        """
        Gets the row number of the text line within the image.

        Returns:
            The row number of the text line within the image.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetRowNumber(self)

    def get_character_result(self, index: int) -> CharacterResult:
        """
        Gets the character recognition result at the specified index.

        Args:
            index (int): The index of the character recognition result to retrieve.

        Returns:
            The character result.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetCharacterResult(self, index)

    def set_text(self, text: str) -> None:
        """
        Sets the recognized text.

        Args:
            text (str): The recognized text.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_SetText(self, text)

    def get_specification_name(self) -> str:
        """
        Gets the name of the text line specification that generated this element.

        Returns:
            The name of the text line specification that generated this element.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetSpecificationName(self)

    def get_raw_text(self) -> str:
        """
        Gets the recognized raw text, excluding any concatenation separators.

        Returns:
            The recognized raw text.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_GetRawText(self)

    def set_location(self, location: Quadrilateral) -> int:
        """
        Sets the location of the recognized text line element.

        Args:
            location (Quadrilateral): The location of the recognized text line element.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLineElement_SetLocation(self, location)

_DynamsoftLabelRecognizer.CRecognizedTextLineElement_register(RecognizedTextLineElement)
class LocalizedTextLinesUnit(IntermediateResultUnit):
    """
    The LocalizedTextLinesUnit class represents a unit that contains localized text lines. It inherits from the IntermediateResultUnit class.

    Methods:
        get_count(self) -> int: Gets the number of localized text lines in the unit.
        get_localized_text_line(self, index: int) -> LocalizedTextLineElement: Gets the localized text line at the specified index.
        remove_all_localized_text_lines(self): Removes all localized text lines.
        remove_localized_text_line(self, index: int) -> int: Removes the localized text line at the specified index.
        add_localized_text_line(self, localized_text_line: LocalizedTextLineElement) -> int: Adds a localized text line to the unit.
        set_localized_text_line(self, index: int, element: LocalizedTextLineElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the localized text line at the specified index.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of localized text lines in the unit.

        Returns:
            The number of localized text lines in the unit.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_GetCount(self)

    def get_localized_text_line(self, index: int) -> LocalizedTextLineElement:
        """
        Gets the localized text line at the specified index.

        Args:
            index (int): The index of the localized text line to retrieve.

        Returns:
            The localized text line.

        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_GetLocalizedTextLine(self, index)

    def remove_all_localized_text_lines(self) -> None:
        """
        Removes all localized text lines.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_RemoveAllLocalizedTextLines(self)

    def remove_localized_text_line(self, index: int) -> int:
        """
        Removes the localized text line at the specified index.

        Args:
            index (int): The index of the localized text line to remove.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_RemoveLocalizedTextLine(self, index)

    def add_localized_text_line(self, element: LocalizedTextLineElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a localized text line to the unit.

        Args:
            element (LocalizedTextLineElement): The localized text line to add.
            matrix_to_original_image (List[float], optional): The matrix to transform the localized text line to the original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """

        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_AddLocalizedTextLine(self, element, matrix_to_original_image)

    def set_localized_text_line(self, index: int, element: LocalizedTextLineElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the localized text line at the specified index.

        Args:
            index (int): The index of the localized text line to set.
            element (LocalizedTextLineElement): The localized text line to set.
            matrix_to_original_image (List[float], optional): The matrix to transform the localized text line to the original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_SetLocalizedTextLine(self, index, element, matrix_to_original_image)

    def get_auxiliary_region_elements_count(self) -> int:
        """
        Gets the count of auxiliary region elements in the unit.

        Returns:
            Returns the number of auxiliary region elements.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_GetAuxiliaryRegionElementsCount(self)

    def get_auxiliary_region_element(self, index: int) -> AuxiliaryRegionElement:
        """
        Gets the auxiliary region element at the specified index.

        Args:
            index (int): The zero-based index of the auxiliary region element to retrieve.

        Returns:
            Returns a pointer to the CAuxiliaryRegionElement object, or NULL if the index is out of range.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_GetAuxiliaryRegionElement(self, index)

    def set_auxiliary_region_element(self, index: int, element: AuxiliaryRegionElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets or replaces the auxiliary region element at the specified index.

        Args:
            index (int): The zero-based index where the element should be set.
            element (CAuxiliaryRegionElement): The auxiliary region element to set.
            matrix_to_original_image (List[float], optional): The matrix to original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_SetAuxiliaryRegionElement(self, index, element, matrix_to_original_image)

    def add_auxiliary_region_element(self, element: AuxiliaryRegionElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a new auxiliary region element to this unit.

        Args:
            element (AuxiliaryRegionElement): The auxiliary region element to add.
            matrix_to_original_image (List[float], optional): The matrix to original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_AddAuxiliaryRegionElement(self, element, matrix_to_original_image)

    def remove_auxiliary_region_element(self, index: int) -> int:
        """
        Removes the auxiliary region element at the specified index.

        Args:
            index (int): The zero-based index of the auxiliary region element to remove.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_RemoveAuxiliaryRegionElement(self, index)

    def remove_all_auxiliary_region_elements(self):
        """
        Removes all auxiliary region elements from this unit.
        """
        return _DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_RemoveAllAuxiliaryRegionElements(self)

_DynamsoftLabelRecognizer.CLocalizedTextLinesUnit_register(LocalizedTextLinesUnit)
class RecognizedTextLinesUnit(IntermediateResultUnit):
    """
    The RecognizedTextLinesUnit class represents an intermediate result unit containing recognized text lines. It inherits from the IntermediateResultUnit class.

    Methods:
        get_count(self) -> int: Gets the number of recognized text lines in the unit.
        get_recognized_text_line(self, index: int) -> RecognizedTextLineElement: Gets the recognized text line at the specified index.
        remove_all_recognized_text_lines(self): Removes all recognized text lines.
        remove_recognized_text_line(self, index: int) -> int: Removes the recognized text line at the specified index.
        add_recognized_text_line(self, recognized_text_line: RecognizedTextLineElement): Adds a recognized text line.
        set_recognized_text_line(self, index: int, element: RecognizedTextLineElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the recognized text line at the specified index.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of recognized text lines in the unit.

        Returns:
            The number of recognized text lines in the unit.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_GetCount(self)

    def get_recognized_text_line(self, index: int) -> RecognizedTextLineElement:
        """
        Gets the RecognizedTextLineElement object at the specified index.

        Args:
            index (int): The index of the desired CRecognizedTextLineElement object.

        Returns:
            The RecognizedTextLineElement object at the specified index.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_GetRecognizedTextLine(self, index)

    def remove_all_recognized_text_lines(self) -> None:
        """
        Removes all recognized text lines.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_RemoveAllRecognizedTextLines(self)

    def remove_recognized_text_line(self, index: int) -> int:
        """
        Removes the recognized text line at the specified index.

        Args:
            index (int): The index of the recognized text line to remove.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_RemoveRecognizedTextLine(self, index)

    def add_recognized_text_line(self, element: RecognizedTextLineElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a recognized text line.

        Args:
            element (RecognizedTextLineElement): The recognized text line to add.
            matrix_to_original_image (List[float], optional): The matrix to transform the recognized text line to the original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_AddRecognizedTextLine(self, element, matrix_to_original_image)

    def set_recognized_text_line(self, index: int, element: RecognizedTextLineElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the recognized text line at the specified index.

        Args:
            index (int): The index of the recognized text line to set.
            element (RecognizedTextLineElement): The recognized text line to set.
            matrix_to_original_image (List[float], optional): The matrix to transform the recognized text line to the original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_SetRecognizedTextLine(self, index, element, matrix_to_original_image)

_DynamsoftLabelRecognizer.CRecognizedTextLinesUnit_register(RecognizedTextLinesUnit)
class RawTextLine:
    """
    The RawTextLine class represents a text line in an image.
    It can be in one of the following states:
    - `RTLS_LOCALIZED`: Localized but recognition not performed.
    - `RTLS_RECOGNITION_FAILED`: Recognition failed.
	- `RTLS_RECOGNITION_SUCCESSFULLY`: Successfully recognized.

    Methods:
        get_text(self) -> str: Gets the recognized text.
        get_confidence(self) -> int: Gets the confidence level of the recognized text.
        get_character_results_count(self) -> int: Gets the number of individual character recognition results in the line.
        get_row_number(self) -> int: Gets the row number of the text line within the image.
        get_character_result(self, index: int) -> CharacterResult: Gets the character recognition result at the specified index.
        set_text(self, text: str): Sets the recognized text.
        get_specification_name(self) -> str: Gets the name of the text line specification that generated this element.
        get_location(self) -> Quadrilateral: Gets the location of the text line.
        set_location(self, location: Quadrilateral) -> int: Sets the location of the text line.
        get_status(self) -> int: Gets the status of the text line.
        clone(self) -> "RawTextLine": Clones the RawTextLine object.
        set_row_number(self, row_number: int) -> int: Sets the row number of the text line within the image.
        set_specification_name(self, specification_name: str) -> int: Sets the name of the text line specification that generated this element.
        set_character_results(self, char_array: List[CharacterResult]) -> int: Sets the character recognition results for the text line.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        _DynamsoftLabelRecognizer.Class_init(
            self, _DynamsoftLabelRecognizer.CLabelRecognizerModule_CreateRawTextLine()
        )
    __destroy__ = _DynamsoftLabelRecognizer.CRawTextLine_Release

    def get_text(self) -> str:
        """
        Gets the recognized text.

        Returns:
            The recognized text.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetText(self)

    def get_confidence(self) -> int:
        """
        Gets the confidence level of the recognized text.

        Returns:
            An integer value representing the confidence level of the recognized text.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetConfidence(self)

    def get_character_results_count(self) -> int:
        """
        Gets the number of individual character recognition results in the line.

        Returns:
            An integer value representing the number of individual character recognition results.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetCharacterResultsCount(self)

    def get_row_number(self) -> int:
        """
        Gets the row number of the text line within the image.

        Returns:
            An integer value representing the row number of the text line within the image.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetRowNumber(self)

    def get_character_result(self, index: int) -> CharacterResult:
        """
        Gets the character recognition result at the specified index.

        Args:
            index (int): The index of the character recognition result to retrieve.

        Returns:
            The character recognition result at the specified index.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetCharacterResult(self, index)

    def set_text(self, text: str) -> None:
        """
        Sets the recognized text.

        Args:
            text (str): The recognized text to set.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_SetText(self, text)

    def get_specification_name(self) -> str:
        """
        Gets the name of the text line specification that generated this element.

        Returns:
            The name of the text line specification.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetSpecificationName(self)

    def get_location(self) -> Quadrilateral:
        """
        Gets the location of the text line.

        Returns:
            A Quadrilateral object which represents the location of the text line.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetLocation(self)

    def set_location(self, location: Quadrilateral) -> int:
        """
        Sets the location of the text line.

        Args:
            location (Quadrilateral): The location of the text line to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_SetLocation(self, location)

    def get_status(self) -> int:
        """
        Gets the status of the text line.

        Returns:
            The status of the text line.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_GetStatus(self)

    def clone(self) -> "RawTextLine":
        """
        Clones the RawTextLine object.

        Returns:
            A copy of the RawTextLine object.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_Clone(self)

    def set_row_number(self, row_number: int) -> int:
        """
        Sets the row number of the text line within the image.

        Args:
            row_number (int): The row number to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_SetRowNumber(self, row_number)

    def set_specification_name(self, specification_name: str) -> int:
        """
        Sets the name of the text line specification that generated this element.

        Args:
            specification_name (str): The name of the text line specification to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_SetSpecificationName(self, specification_name)

    def set_character_results(self, char_array: List[CharacterResult]) -> int:
        """
        Sets the character recognition results for the text line.

        Args:
            char_array (List[CharacterResult]): The character recognition results to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftLabelRecognizer.CRawTextLine_SetCharacterResults(self, char_array)

_DynamsoftLabelRecognizer.CRawTextLine_register(RawTextLine)
class RawTextLinesUnit(IntermediateResultUnit):
    """
    The RawTextLinesUnit class represents an intermediate result unit containing raw text lines. It inherits from the IntermediateResultUnit class.

    Methods:
        get_count(): Gets the number of raw text lines in the unit.
        get_raw_text_line(index): Gets the raw text line at the specified index.
        remove_all_raw_text_lines(): Removes all raw text lines from the unit.
        remove_raw_text_line(self, index: int) -> int: Removes the raw text line at the specified index.
        add_raw_text_line(self, text_line: RawTextLine, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Adds a raw text line.
        set_raw_text_line(self, index: int, text_line: RawTextLine, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the raw text line at the specified index.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of raw text lines in the unit.

        Returns:
            The number of raw text lines in the unit.
        """
        return _DynamsoftLabelRecognizer.CRawTextLinesUnit_GetCount(self)

    def get_raw_text_line(self, index: int) -> RawTextLine:
        """
        Gets the raw text line at the specified index.

        Args:
            index (int): The index of the raw text line.

        Returns:
            the RawTextLine object at the specified index.
        """
        return _DynamsoftLabelRecognizer.CRawTextLinesUnit_GetRawTextLine(self, index)

    def remove_all_raw_text_lines(self) -> None:
        """
        Removes all raw text lines from the unit.
        """
        return _DynamsoftLabelRecognizer.CRawTextLinesUnit_RemoveAllRawTextLines(self)

    def remove_raw_text_line(self, index: int) -> int:
        """
        Removes the raw text line at the specified index.

        Args:
            index (int): The index of the raw text line to remove.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CRawTextLinesUnit_RemoveRawTextLine(self, index)

    def add_raw_text_line(self, text_line: RawTextLine, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a raw text line.

        Args:
            text_line (RawTextLine): The raw text line to add.
            matrix_to_original_image (List[float], optional): The matrix to transform the raw text line to the original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CRawTextLinesUnit_AddRawTextLine(self, text_line, matrix_to_original_image)

    def set_raw_text_line(self, index: int, text_line: RawTextLine, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the raw text line at the specified index.

        Args:
            index (int): The index of the raw text line to set.
            text_line (RawTextLine): The raw text line to set.
            matrix_to_original_image (List[float], optional): The matrix to transform the raw text line to the original image. Defaults to IDENTITY_MATRIX.

        Returns:
            Returns 0 if successful, otherwise returns a negative value.
        """
        return _DynamsoftLabelRecognizer.CRawTextLinesUnit_SetRawTextLine(self, index, text_line, matrix_to_original_image)

_DynamsoftLabelRecognizer.CRawTextLinesUnit_register(RawTextLinesUnit)