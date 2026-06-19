__version__ = "4.0.40.9454"

import sys

module_name = "runtime_data_dynamsoft"
module = sys.modules.setdefault(module_name, type(sys)(module_name))

if __package__ or "." in __name__:
    from . import _DynamsoftCore
else:
    import _DynamsoftCore

from typing import List, Tuple
from enum import Enum, IntEnum
from abc import ABC, abstractmethod

class EnumErrorCode(IntEnum):
    EC_OK = _DynamsoftCore.EC_OK
    EC_UNKNOWN = _DynamsoftCore.EC_UNKNOWN
    EC_NO_MEMORY = _DynamsoftCore.EC_NO_MEMORY
    EC_NULL_POINTER = _DynamsoftCore.EC_NULL_POINTER
    EC_LICENSE_INVALID = _DynamsoftCore.EC_LICENSE_INVALID
    EC_LICENSE_EXPIRED = _DynamsoftCore.EC_LICENSE_EXPIRED
    EC_FILE_NOT_FOUND = _DynamsoftCore.EC_FILE_NOT_FOUND
    EC_FILE_TYPE_NOT_SUPPORTED = _DynamsoftCore.EC_FILE_TYPE_NOT_SUPPORTED
    EC_BPP_NOT_SUPPORTED = _DynamsoftCore.EC_BPP_NOT_SUPPORTED
    EC_INDEX_INVALID = _DynamsoftCore.EC_INDEX_INVALID
    EC_CUSTOM_REGION_INVALID = _DynamsoftCore.EC_CUSTOM_REGION_INVALID
    EC_IMAGE_READ_FAILED = _DynamsoftCore.EC_IMAGE_READ_FAILED
    EC_TIFF_READ_FAILED = _DynamsoftCore.EC_TIFF_READ_FAILED
    EC_DIB_BUFFER_INVALID = _DynamsoftCore.EC_DIB_BUFFER_INVALID
    EC_PDF_READ_FAILED = _DynamsoftCore.EC_PDF_READ_FAILED
    EC_PDF_DLL_MISSING = _DynamsoftCore.EC_PDF_DLL_MISSING
    EC_PAGE_NUMBER_INVALID = _DynamsoftCore.EC_PAGE_NUMBER_INVALID
    EC_CUSTOM_SIZE_INVALID = _DynamsoftCore.EC_CUSTOM_SIZE_INVALID
    EC_TIMEOUT = _DynamsoftCore.EC_TIMEOUT
    EC_JSON_PARSE_FAILED = _DynamsoftCore.EC_JSON_PARSE_FAILED
    EC_JSON_TYPE_INVALID = _DynamsoftCore.EC_JSON_TYPE_INVALID
    EC_JSON_KEY_INVALID = _DynamsoftCore.EC_JSON_KEY_INVALID
    EC_JSON_VALUE_INVALID = _DynamsoftCore.EC_JSON_VALUE_INVALID
    EC_JSON_NAME_KEY_MISSING = _DynamsoftCore.EC_JSON_NAME_KEY_MISSING
    EC_JSON_NAME_VALUE_DUPLICATED = _DynamsoftCore.EC_JSON_NAME_VALUE_DUPLICATED
    EC_TEMPLATE_NAME_INVALID = _DynamsoftCore.EC_TEMPLATE_NAME_INVALID
    EC_JSON_NAME_REFERENCE_INVALID = _DynamsoftCore.EC_JSON_NAME_REFERENCE_INVALID
    EC_PARAMETER_VALUE_INVALID = _DynamsoftCore.EC_PARAMETER_VALUE_INVALID
    EC_DOMAIN_NOT_MATCH = _DynamsoftCore.EC_DOMAIN_NOT_MATCH
    EC_RESERVED_INFO_NOT_MATCH = _DynamsoftCore.EC_RESERVED_INFO_NOT_MATCH
    EC_LICENSE_KEY_NOT_MATCH = _DynamsoftCore.EC_LICENSE_KEY_NOT_MATCH
    EC_REQUEST_FAILED = _DynamsoftCore.EC_REQUEST_FAILED
    EC_LICENSE_INIT_FAILED = _DynamsoftCore.EC_LICENSE_INIT_FAILED
    EC_SET_MODE_ARGUMENT_ERROR = _DynamsoftCore.EC_SET_MODE_ARGUMENT_ERROR
    EC_LICENSE_CONTENT_INVALID = _DynamsoftCore.EC_LICENSE_CONTENT_INVALID
    EC_LICENSE_KEY_INVALID = _DynamsoftCore.EC_LICENSE_KEY_INVALID
    EC_LICENSE_DEVICE_RUNS_OUT = _DynamsoftCore.EC_LICENSE_DEVICE_RUNS_OUT
    EC_GET_MODE_ARGUMENT_ERROR = _DynamsoftCore.EC_GET_MODE_ARGUMENT_ERROR
    EC_IRT_LICENSE_INVALID = _DynamsoftCore.EC_IRT_LICENSE_INVALID
    EC_FILE_SAVE_FAILED = _DynamsoftCore.EC_FILE_SAVE_FAILED
    EC_STAGE_TYPE_INVALID = _DynamsoftCore.EC_STAGE_TYPE_INVALID
    EC_IMAGE_ORIENTATION_INVALID = _DynamsoftCore.EC_IMAGE_ORIENTATION_INVALID
    EC_CONVERT_COMPLEX_TEMPLATE_ERROR = _DynamsoftCore.EC_CONVERT_COMPLEX_TEMPLATE_ERROR
    EC_CALL_REJECTED_WHEN_CAPTURING = _DynamsoftCore.EC_CALL_REJECTED_WHEN_CAPTURING
    EC_NO_IMAGE_SOURCE = _DynamsoftCore.EC_NO_IMAGE_SOURCE
    EC_READ_DIRECTORY_FAILED = _DynamsoftCore.EC_READ_DIRECTORY_FAILED
    EC_MODULE_NOT_FOUND = _DynamsoftCore.EC_MODULE_NOT_FOUND
    EC_MULTI_PAGES_NOT_SUPPORTED = _DynamsoftCore.EC_MULTI_PAGES_NOT_SUPPORTED
    EC_FILE_ALREADY_EXISTS = _DynamsoftCore.EC_FILE_ALREADY_EXISTS
    EC_CREATE_FILE_FAILED = _DynamsoftCore.EC_CREATE_FILE_FAILED
    EC_IMAGE_DATA_INVALID = _DynamsoftCore.EC_IMAGE_DATA_INVALID
    EC_IMAGE_SIZE_NOT_MATCH = _DynamsoftCore.EC_IMAGE_SIZE_NOT_MATCH
    EC_IMAGE_PIXEL_FORMAT_NOT_MATCH = _DynamsoftCore.EC_IMAGE_PIXEL_FORMAT_NOT_MATCH
    EC_SECTION_LEVEL_RESULT_IRREPLACEABLE = (
        _DynamsoftCore.EC_SECTION_LEVEL_RESULT_IRREPLACEABLE
    )
    EC_AXIS_DEFINITION_INCORRECT = _DynamsoftCore.EC_AXIS_DEFINITION_INCORRECT
    EC_RESULT_TYPE_MISMATCH_IRREPLACEABLE = (
        _DynamsoftCore.EC_RESULT_TYPE_MISMATCH_IRREPLACEABLE
    )
    EC_PDF_LIBRARY_LOAD_FAILED = _DynamsoftCore.EC_PDF_LIBRARY_LOAD_FAILED
    EC_LICENSE_WARNING = _DynamsoftCore.EC_LICENSE_WARNING
    EC_UNSUPPORTED_JSON_KEY_WARNING = _DynamsoftCore.EC_UNSUPPORTED_JSON_KEY_WARNING
    EC_MODEL_FILE_NOT_FOUND = _DynamsoftCore.EC_MODEL_FILE_NOT_FOUND
    EC_PDF_LICENSE_NOT_FOUND = _DynamsoftCore.EC_PDF_LICENSE_NOT_FOUND
    EC_RECT_INVALID = _DynamsoftCore.EC_RECT_INVALID
    EC_TEMPLATE_VERSION_INCOMPATIBLE = _DynamsoftCore.EC_TEMPLATE_VERSION_INCOMPATIBLE
    EC_NO_LICENSE = _DynamsoftCore.EC_NO_LICENSE
    EC_HANDSHAKE_CODE_INVALID = _DynamsoftCore.EC_HANDSHAKE_CODE_INVALID
    EC_LICENSE_BUFFER_FAILED = _DynamsoftCore.EC_LICENSE_BUFFER_FAILED
    EC_LICENSE_SYNC_FAILED = _DynamsoftCore.EC_LICENSE_SYNC_FAILED
    EC_DEVICE_NOT_MATCH = _DynamsoftCore.EC_DEVICE_NOT_MATCH
    EC_BIND_DEVICE_FAILED = _DynamsoftCore.EC_BIND_DEVICE_FAILED
    EC_LICENSE_CLIENT_DLL_MISSING = _DynamsoftCore.EC_LICENSE_CLIENT_DLL_MISSING
    EC_INSTANCE_COUNT_OVER_LIMIT = _DynamsoftCore.EC_INSTANCE_COUNT_OVER_LIMIT
    EC_LICENSE_INIT_SEQUENCE_FAILED = _DynamsoftCore.EC_LICENSE_INIT_SEQUENCE_FAILED
    EC_TRIAL_LICENSE = _DynamsoftCore.EC_TRIAL_LICENSE
    EC_LICENSE_VERSION_NOT_MATCH = _DynamsoftCore.EC_LICENSE_VERSION_NOT_MATCH
    EC_LICENSE_CACHE_USED = _DynamsoftCore.EC_LICENSE_CACHE_USED
    EC_LICENSE_AUTH_QUOTA_EXCEEDED = _DynamsoftCore.EC_LICENSE_AUTH_QUOTA_EXCEEDED
    EC_LICENSE_RESULTS_LIMIT_EXCEEDED = _DynamsoftCore.EC_LICENSE_RESULTS_LIMIT_EXCEEDED
    EC_FAILED_TO_REACH_DLS = _DynamsoftCore.EC_FAILED_TO_REACH_DLS
    EC_BARCODE_FORMAT_INVALID = _DynamsoftCore.EC_BARCODE_FORMAT_INVALID
    EC_QR_LICENSE_INVALID = _DynamsoftCore.EC_QR_LICENSE_INVALID
    EC_1D_LICENSE_INVALID = _DynamsoftCore.EC_1D_LICENSE_INVALID
    EC_PDF417_LICENSE_INVALID = _DynamsoftCore.EC_PDF417_LICENSE_INVALID
    EC_DATAMATRIX_LICENSE_INVALID = _DynamsoftCore.EC_DATAMATRIX_LICENSE_INVALID
    EC_CUSTOM_MODULESIZE_INVALID = _DynamsoftCore.EC_CUSTOM_MODULESIZE_INVALID
    EC_AZTEC_LICENSE_INVALID = _DynamsoftCore.EC_AZTEC_LICENSE_INVALID
    EC_PATCHCODE_LICENSE_INVALID = _DynamsoftCore.EC_PATCHCODE_LICENSE_INVALID
    EC_POSTALCODE_LICENSE_INVALID = _DynamsoftCore.EC_POSTALCODE_LICENSE_INVALID
    EC_DPM_LICENSE_INVALID = _DynamsoftCore.EC_DPM_LICENSE_INVALID
    EC_FRAME_DECODING_THREAD_EXISTS = _DynamsoftCore.EC_FRAME_DECODING_THREAD_EXISTS
    EC_STOP_DECODING_THREAD_FAILED = _DynamsoftCore.EC_STOP_DECODING_THREAD_FAILED
    EC_MAXICODE_LICENSE_INVALID = _DynamsoftCore.EC_MAXICODE_LICENSE_INVALID
    EC_GS1_DATABAR_LICENSE_INVALID = _DynamsoftCore.EC_GS1_DATABAR_LICENSE_INVALID
    EC_GS1_COMPOSITE_LICENSE_INVALID = _DynamsoftCore.EC_GS1_COMPOSITE_LICENSE_INVALID
    EC_DOTCODE_LICENSE_INVALID = _DynamsoftCore.EC_DOTCODE_LICENSE_INVALID
    EC_PHARMACODE_LICENSE_INVALID = _DynamsoftCore.EC_PHARMACODE_LICENSE_INVALID
    EC_BARCODE_READER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_BARCODE_READER_LICENSE_NOT_FOUND
    EC_CHARACTER_MODEL_FILE_NOT_FOUND = _DynamsoftCore.EC_CHARACTER_MODEL_FILE_NOT_FOUND
    EC_TEXT_LINE_GROUP_LAYOUT_CONFLICT = (
        _DynamsoftCore.EC_TEXT_LINE_GROUP_LAYOUT_CONFLICT
    )
    EC_TEXT_LINE_GROUP_REGEX_CONFLICT = _DynamsoftCore.EC_TEXT_LINE_GROUP_REGEX_CONFLICT
    EC_LABEL_RECOGNIZER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_LABEL_RECOGNIZER_LICENSE_NOT_FOUND
    EC_QUADRILATERAL_INVALID = _DynamsoftCore.EC_QUADRILATERAL_INVALID
    EC_DOCUMENT_NORMALIZER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_DOCUMENT_NORMALIZER_LICENSE_NOT_FOUND
    EC_PANORAMA_LICENSE_INVALID = _DynamsoftCore.EC_PANORAMA_LICENSE_INVALID
    EC_RESOURCE_PATH_NOT_EXIST = _DynamsoftCore.EC_RESOURCE_PATH_NOT_EXIST
    EC_RESOURCE_LOAD_FAILED = _DynamsoftCore.EC_RESOURCE_LOAD_FAILED
    EC_CODE_SPECIFICATION_NOT_FOUND = _DynamsoftCore.EC_CODE_SPECIFICATION_NOT_FOUND
    EC_FULL_CODE_EMPTY = _DynamsoftCore.EC_FULL_CODE_EMPTY
    EC_FULL_CODE_PREPROCESS_FAILED = _DynamsoftCore.EC_FULL_CODE_PREPROCESS_FAILED
    EC_ZA_DL_LICENSE_INVALID = _DynamsoftCore.EC_ZA_DL_LICENSE_INVALID
    EC_AAMVA_DL_ID_LICENSE_INVALID = _DynamsoftCore.EC_AAMVA_DL_ID_LICENSE_INVALID
    EC_AADHAAR_LICENSE_INVALID = _DynamsoftCore.EC_AADHAAR_LICENSE_INVALID
    EC_MRTD_LICENSE_INVALID = _DynamsoftCore.EC_MRTD_LICENSE_INVALID
    EC_VIN_LICENSE_INVALID = _DynamsoftCore.EC_VIN_LICENSE_INVALID
    EC_CUSTOMIZED_CODE_TYPE_LICENSE_INVALID = (
        _DynamsoftCore.EC_CUSTOMIZED_CODE_TYPE_LICENSE_INVALID
    )
    EC_CODE_PARSER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_CODE_PARSER_LICENSE_NOT_FOUND


class EnumImagePixelFormat(IntEnum):
    IPF_BINARY = _DynamsoftCore.IPF_BINARY
    IPF_BINARYINVERTED = _DynamsoftCore.IPF_BINARYINVERTED
    IPF_GRAYSCALED = _DynamsoftCore.IPF_GRAYSCALED
    IPF_NV21 = _DynamsoftCore.IPF_NV21
    IPF_RGB_565 = _DynamsoftCore.IPF_RGB_565
    IPF_RGB_555 = _DynamsoftCore.IPF_RGB_555
    IPF_RGB_888 = _DynamsoftCore.IPF_RGB_888
    IPF_ARGB_8888 = _DynamsoftCore.IPF_ARGB_8888
    IPF_RGB_161616 = _DynamsoftCore.IPF_RGB_161616
    IPF_ARGB_16161616 = _DynamsoftCore.IPF_ARGB_16161616
    IPF_ABGR_8888 = _DynamsoftCore.IPF_ABGR_8888
    IPF_ABGR_16161616 = _DynamsoftCore.IPF_ABGR_16161616
    IPF_BGR_888 = _DynamsoftCore.IPF_BGR_888
    IPF_BINARY_8 = _DynamsoftCore.IPF_BINARY_8
    IPF_NV12 = _DynamsoftCore.IPF_NV12
    IPF_BINARY_8_INVERTED = _DynamsoftCore.IPF_BINARY_8_INVERTED


class EnumGrayscaleTransformationMode(IntEnum):
    GTM_INVERTED = _DynamsoftCore.GTM_INVERTED
    GTM_ORIGINAL = _DynamsoftCore.GTM_ORIGINAL
    GTM_AUTO = _DynamsoftCore.GTM_AUTO
    GTM_REV = _DynamsoftCore.GTM_REV
    GTM_END = _DynamsoftCore.GTM_END
    GTM_SKIP = _DynamsoftCore.GTM_SKIP


class EnumGrayscaleEnhancementMode(IntEnum):
    GEM_AUTO = _DynamsoftCore.GEM_AUTO
    GEM_GENERAL = _DynamsoftCore.GEM_GENERAL
    GEM_GRAY_EQUALIZE = _DynamsoftCore.GEM_GRAY_EQUALIZE
    GEM_GRAY_SMOOTH = _DynamsoftCore.GEM_GRAY_SMOOTH
    GEM_SHARPEN_SMOOTH = _DynamsoftCore.GEM_SHARPEN_SMOOTH
    GEM_REV = _DynamsoftCore.GEM_REV
    GEM_END = _DynamsoftCore.GEM_END
    GEM_SKIP = _DynamsoftCore.GEM_SKIP


class EnumPDFReadingMode(IntEnum):
    PDFRM_VECTOR = _DynamsoftCore.PDFRM_VECTOR
    PDFRM_RASTER = _DynamsoftCore.PDFRM_RASTER
    PDFRM_REV = _DynamsoftCore.PDFRM_REV


class EnumRasterDataSource(IntEnum):
    RDS_RASTERIZED_PAGES = _DynamsoftCore.RDS_RASTERIZED_PAGES
    RDS_EXTRACTED_IMAGES = _DynamsoftCore.RDS_EXTRACTED_IMAGES


class EnumCapturedResultItemType(IntEnum):
    CRIT_ORIGINAL_IMAGE = _DynamsoftCore.CRIT_ORIGINAL_IMAGE
    CRIT_BARCODE = _DynamsoftCore.CRIT_BARCODE
    CRIT_TEXT_LINE = _DynamsoftCore.CRIT_TEXT_LINE
    CRIT_DETECTED_QUAD = _DynamsoftCore.CRIT_DETECTED_QUAD
    CRIT_DESKEWED_IMAGE = _DynamsoftCore.CRIT_DESKEWED_IMAGE
    CRIT_PARSED_RESULT = _DynamsoftCore.CRIT_PARSED_RESULT
    CRIT_ENHANCED_IMAGE = _DynamsoftCore.CRIT_ENHANCED_IMAGE


class EnumBufferOverflowProtectionMode(IntEnum):
    BOPM_BLOCK = _DynamsoftCore.BOPM_BLOCK
    BOPM_UPDATE = _DynamsoftCore.BOPM_UPDATE


class EnumImageTagType(IntEnum):
    ITT_FILE_IMAGE = _DynamsoftCore.ITT_FILE_IMAGE
    ITT_VIDEO_FRAME = _DynamsoftCore.ITT_VIDEO_FRAME


class EnumVideoFrameQuality(IntEnum):
    VFQ_HIGH = _DynamsoftCore.VFQ_HIGH
    VFQ_LOW = _DynamsoftCore.VFQ_LOW
    VFQ_UNKNOWN = _DynamsoftCore.VFQ_UNKNOWN


class EnumImageCaptureDistanceMode(IntEnum):
    ICDM_NEAR = _DynamsoftCore.ICDM_NEAR
    ICDM_FAR = _DynamsoftCore.ICDM_FAR


class EnumColourChannelUsageType(IntEnum):
    CCUT_AUTO = _DynamsoftCore.CCUT_AUTO
    CCUT_FULL_CHANNEL = _DynamsoftCore.CCUT_FULL_CHANNEL
    CCUT_Y_CHANNEL_ONLY = _DynamsoftCore.CCUT_Y_CHANNEL_ONLY
    CCUT_RGB_R_CHANNEL_ONLY = _DynamsoftCore.CCUT_RGB_R_CHANNEL_ONLY
    CCUT_RGB_G_CHANNEL_ONLY = _DynamsoftCore.CCUT_RGB_G_CHANNEL_ONLY
    CCUT_RGB_B_CHANNEL_ONLY = _DynamsoftCore.CCUT_RGB_B_CHANNEL_ONLY
class EnumCornerType(IntEnum):
    CT_NORMAL_INTERSECTED = _DynamsoftCore.CT_NORMAL_INTERSECTED
    CT_T_INTERSECTED = _DynamsoftCore.CT_T_INTERSECTED
    CT_CROSS_INTERSECTED = _DynamsoftCore.CT_CROSS_INTERSECTED
    CT_NOT_INTERSECTED = _DynamsoftCore.CT_NOT_INTERSECTED
class EnumSectionType(IntEnum):
    ST_NULL = _DynamsoftCore.ST_NULL
    ST_REGION_PREDETECTION = _DynamsoftCore.ST_REGION_PREDETECTION
    ST_BARCODE_LOCALIZATION = _DynamsoftCore.ST_BARCODE_LOCALIZATION
    ST_BARCODE_DECODING = _DynamsoftCore.ST_BARCODE_DECODING
    ST_TEXT_LINE_LOCALIZATION = _DynamsoftCore.ST_TEXT_LINE_LOCALIZATION
    ST_TEXT_LINE_RECOGNITION = _DynamsoftCore.ST_TEXT_LINE_RECOGNITION
    ST_DOCUMENT_DETECTION = _DynamsoftCore.ST_DOCUMENT_DETECTION
    ST_DOCUMENT_DESKEWING = _DynamsoftCore.ST_DOCUMENT_DESKEWING
    ST_IMAGE_ENHANCEMENT = _DynamsoftCore.ST_IMAGE_ENHANCEMENT
class EnumIntermediateResultUnitType(IntEnum):
    IRUT_NULL = _DynamsoftCore.IRUT_NULL
    IRUT_COLOUR_IMAGE = _DynamsoftCore.IRUT_COLOUR_IMAGE
    IRUT_SCALED_COLOUR_IMAGE = _DynamsoftCore.IRUT_SCALED_COLOUR_IMAGE
    IRUT_GRAYSCALE_IMAGE = _DynamsoftCore.IRUT_GRAYSCALE_IMAGE
    IRUT_TRANSFORMED_GRAYSCALE_IMAGE = _DynamsoftCore.IRUT_TRANSFORMED_GRAYSCALE_IMAGE
    IRUT_ENHANCED_GRAYSCALE_IMAGE = _DynamsoftCore.IRUT_ENHANCED_GRAYSCALE_IMAGE
    IRUT_PREDETECTED_REGIONS = _DynamsoftCore.IRUT_PREDETECTED_REGIONS
    IRUT_BINARY_IMAGE = _DynamsoftCore.IRUT_BINARY_IMAGE
    IRUT_TEXTURE_DETECTION_RESULT = _DynamsoftCore.IRUT_TEXTURE_DETECTION_RESULT
    IRUT_TEXTURE_REMOVED_GRAYSCALE_IMAGE = _DynamsoftCore.IRUT_TEXTURE_REMOVED_GRAYSCALE_IMAGE
    IRUT_TEXTURE_REMOVED_BINARY_IMAGE = _DynamsoftCore.IRUT_TEXTURE_REMOVED_BINARY_IMAGE
    IRUT_CONTOURS = _DynamsoftCore.IRUT_CONTOURS
    IRUT_LINE_SEGMENTS = _DynamsoftCore.IRUT_LINE_SEGMENTS
    IRUT_TEXT_ZONES = _DynamsoftCore.IRUT_TEXT_ZONES
    IRUT_TEXT_REMOVED_BINARY_IMAGE = _DynamsoftCore.IRUT_TEXT_REMOVED_BINARY_IMAGE
    IRUT_CANDIDATE_BARCODE_ZONES = _DynamsoftCore.IRUT_CANDIDATE_BARCODE_ZONES
    IRUT_LOCALIZED_BARCODES = _DynamsoftCore.IRUT_LOCALIZED_BARCODES
    IRUT_SCALED_BARCODE_IMAGE = _DynamsoftCore.IRUT_SCALED_BARCODE_IMAGE
    IRUT_DEFORMATION_RESISTED_BARCODE_IMAGE = _DynamsoftCore.IRUT_DEFORMATION_RESISTED_BARCODE_IMAGE
    IRUT_COMPLEMENTED_BARCODE_IMAGE = _DynamsoftCore.IRUT_COMPLEMENTED_BARCODE_IMAGE
    IRUT_DECODED_BARCODES = _DynamsoftCore.IRUT_DECODED_BARCODES
    IRUT_LONG_LINES = _DynamsoftCore.IRUT_LONG_LINES
    IRUT_CORNERS = _DynamsoftCore.IRUT_CORNERS
    IRUT_CANDIDATE_QUAD_EDGES = _DynamsoftCore.IRUT_CANDIDATE_QUAD_EDGES
    IRUT_DETECTED_QUADS = _DynamsoftCore.IRUT_DETECTED_QUADS
    IRUT_LOCALIZED_TEXT_LINES = _DynamsoftCore.IRUT_LOCALIZED_TEXT_LINES
    IRUT_RECOGNIZED_TEXT_LINES = _DynamsoftCore.IRUT_RECOGNIZED_TEXT_LINES
    IRUT_DESKEWED_IMAGE = _DynamsoftCore.IRUT_DESKEWED_IMAGE
    IRUT_SHORT_LINES = _DynamsoftCore.IRUT_SHORT_LINES
    IRUT_RAW_TEXT_LINES = _DynamsoftCore.IRUT_RAW_TEXT_LINES
    IRUT_LOGIC_LINES = _DynamsoftCore.IRUT_LOGIC_LINES
    IRUT_ENHANCED_IMAGE = _DynamsoftCore.IRUT_ENHANCED_IMAGE
    IRUT_ALL = _DynamsoftCore.IRUT_ALL
class EnumRegionObjectElementType(IntEnum):
    ROET_PREDETECTED_REGION = _DynamsoftCore.ROET_PREDETECTED_REGION
    ROET_LOCALIZED_BARCODE = _DynamsoftCore.ROET_LOCALIZED_BARCODE
    ROET_DECODED_BARCODE = _DynamsoftCore.ROET_DECODED_BARCODE
    ROET_LOCALIZED_TEXT_LINE = _DynamsoftCore.ROET_LOCALIZED_TEXT_LINE
    ROET_RECOGNIZED_TEXT_LINE = _DynamsoftCore.ROET_RECOGNIZED_TEXT_LINE
    ROET_DETECTED_QUAD = _DynamsoftCore.ROET_DETECTED_QUAD
    ROET_DESKEWED_IMAGE = _DynamsoftCore.ROET_DESKEWED_IMAGE
    ROET_SOURCE_IMAGE = _DynamsoftCore.ROET_SOURCE_IMAGE
    ROET_TARGET_ROI = _DynamsoftCore.ROET_TARGET_ROI
    ROET_ENHANCED_IMAGE = _DynamsoftCore.ROET_ENHANCED_IMAGE
    ROET_AUXILIARY_REGION = _DynamsoftCore.ROET_AUXILIARY_REGION
class EnumTransformMatrixType(IntEnum):
    TMT_LOCAL_TO_ORIGINAL_IMAGE = _DynamsoftCore.TMT_LOCAL_TO_ORIGINAL_IMAGE
    TMT_ORIGINAL_TO_LOCAL_IMAGE = _DynamsoftCore.TMT_ORIGINAL_TO_LOCAL_IMAGE
    TMT_ROTATED_TO_ORIGINAL_IMAGE = _DynamsoftCore.TMT_ROTATED_TO_ORIGINAL_IMAGE
    TMT_ORIGINAL_TO_ROTATED_IMAGE = _DynamsoftCore.TMT_ORIGINAL_TO_ROTATED_IMAGE
    TMT_LOCAL_TO_SECTION_IMAGE = _DynamsoftCore.TMT_LOCAL_TO_SECTION_IMAGE
    TMT_SECTION_TO_LOCAL_IMAGE = _DynamsoftCore.TMT_SECTION_TO_LOCAL_IMAGE
class EnumCrossVerificationStatus(IntEnum):
    CVS_NOT_VERIFIED = _DynamsoftCore.CVS_NOT_VERIFIED
    CVS_PASSED = _DynamsoftCore.CVS_PASSED
    CVS_FAILED = _DynamsoftCore.CVS_FAILED
class EnumImageFileFormat(IntEnum):
    IFF_JPEG = _DynamsoftCore.IFF_JPEG
    IFF_PNG = _DynamsoftCore.IFF_PNG
    IFF_BMP = _DynamsoftCore.IFF_BMP
    IFF_PDF = _DynamsoftCore.IFF_PDF

IDENTITY_MATRIX = [
    1.0, 0.0, 0.0,
    0.0, 1.0, 0.0,
    0.0, 0.0, 1.0
]

class CoreModule:
    """
    The CoreModule class defines general functions in the core module.

    Methods:
        get_version() -> str: Returns a string representing the version of the core module.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns a string representing the version of the core module.

        Returns:
            str: A string representing the version of the core module.
        """
        return __version__ + " (Algorithm " + _DynamsoftCore.CCoreModule_GetVersion() + ")"


    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CCoreModule())

    __destroy__ = _DynamsoftCore.delete_CCoreModule


_DynamsoftCore.CCoreModule_register(CoreModule)


class Point:
    """
    A class representing a point in 2D space.

    Attributes:
        x (int): The x coordinate of the point.
        y (int): The y coordinate of the point.

    Methods:
        distance_to(self, pt: 'Point') -> float: Calculates the distance between the current point and the specified target point.
        transform_coordinates(original_point: 'Point', transformation_matrix: List[float]) -> 'Point': Transforms the coordinates of a point using a given transformation matrix.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    __destroy__ = _DynamsoftCore.delete_CPoint

    x: int = property(_DynamsoftCore.CPoint_Getx, _DynamsoftCore.CPoint_Setx)
    y: int = property(_DynamsoftCore.CPoint_Gety, _DynamsoftCore.CPoint_Sety)

    def __init__(self, x: int = 0, y: int = 0):
        """
        Constructs a Point object.

        Args:
            x (int, optional): The x coordinate of the point. Defaults to 0.
            y (int, optional): The y coordinate of the point. Defaults to 0.
        """
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CPoint(x,y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, pt: "Point") -> float:
        """
        Calculates the distance between the current point and the specified target point.

        Args:
            pt: The target point to which the distance is calculated.

        Returns:
            A value representing the distance between the current point and the specified target point.
        """
        return _DynamsoftCore.CPoint_DistanceTo(self, pt)

    @staticmethod
    def transform_coordinates(original_point: "Point", transformation_matrix: List[float]) -> "Point":
        """
        Transforms the coordinates of a point using a given transformation matrix.

        Args:
            original_point: The original point to transform.
            transformation_matrix: The transformation matrix to apply to the coordinates.

        Returns:
            A new Point object with the transformed coordinates.
        """
        return _DynamsoftCore.CPoint_TransformCoordinates(
            original_point, transformation_matrix
        )


_DynamsoftCore.CPoint_register(Point)

class Rect:
    """
    The Rect class represents a rectangle in 2D space.

    Attributes:
        top (int): The top coordinate of the rectangle.
        left (int): The left coordinate of the rectangle.
        right (int): The right coordinate of the rectangle.
        bottom (int): The bottom coordinate of the rectangle.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    top: int = property(_DynamsoftCore.CRect_top_get, _DynamsoftCore.CRect_top_set)
    left: int = property(_DynamsoftCore.CRect_left_get, _DynamsoftCore.CRect_left_set)
    right: int = property(_DynamsoftCore.CRect_right_get, _DynamsoftCore.CRect_right_set)
    bottom: int = property(_DynamsoftCore.CRect_bottom_get, _DynamsoftCore.CRect_bottom_set)
    id: int = property(_DynamsoftCore.CRect_id_get, _DynamsoftCore.CRect_id_set)

    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CRect())

    def __repr__(self):
        return f"Rect(top={self.top}, left={self.left}, right={self.right}, bottom={self.bottom})"

    __destroy__ = _DynamsoftCore.delete_CRect


_DynamsoftCore.CRect_register(Rect)

class Quadrilateral:
    """
    A quadrilateral.

    Attributes:
        points: A Point list of length 4 that define the quadrilateral.
        id: The ID of the quadrilateral.
    Methods:
        contains(self, point: 'Point') -> bool: Determines whether a point is inside the quadrilateral.
        get_area(self) -> int: Gets the area of the quadrilateral.
        get_bounding_rect(self) -> Rect: Gets the bounding rectangle of the quadrilateral.
    """

    class _OwnerList(List):
        def __init__(self,owner, list):
            self._owner = owner
            super().__init__(list)

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )



    def __init__(self):
        """
        Initializes a new instance of the Quadrilateral class with default values.
        """
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CQuadrilateral())
        self._point_list = None

    def __repr__(self):
        list_repr = ", ".join(f"({obj.x}, {obj.y})" for obj in self.points)
        return f"Quadrilateral[{list_repr}]"

    id: int = property(_DynamsoftCore.CQuadrilateral_id_get, _DynamsoftCore.CQuadrilateral_id_set)

    @property
    def points(self) -> List[Point]:
        if not hasattr(self, '_point_list') or self._point_list is None:
            self._point_list = Quadrilateral._OwnerList(self,_DynamsoftCore.CQuadrilateral_points_get(self))
        return self._point_list

    @points.setter
    def points(self, point_list):
        if not hasattr(self, '_point_list') or self._point_list is None:
            self._point_list = Quadrilateral._OwnerList(self,_DynamsoftCore.CQuadrilateral_points_get(self))
        _DynamsoftCore.CQuadrilateral_points_set(self, point_list)
        self._point_list = point_list

    def contains(self, point: "Point") -> bool:
        """
        Determines whether a point is inside the quadrilateral.

        Args:
            point: The point to test.

        Returns:
            True if the point inside the quadrilateral, False otherwise.
        """
        return _DynamsoftCore.CQuadrilateral_Contains(self, point)

    def get_area(self) -> int:
        """
        Gets the area of the quadrilateral.

        Returns:
            The area of the quadrilateral.
        """
        return _DynamsoftCore.CQuadrilateral_GetArea(self)

    def get_bounding_rect(self) -> Rect:
        """
        Gets the bounding rectangle of the quadrilateral.

        Returns:
            The bounding rectangle of the quadrilateral.
        """
        return _DynamsoftCore.CQuadrilateral_GetBoundingRect(self)

    __destroy__ = _DynamsoftCore.delete_CQuadrilateral

_DynamsoftCore.CQuadrilateral_register(Quadrilateral)



class ImageTag(ABC):
    """
    ImageTag represents an image tag that can be attached to an image in a system.
    It contains information about the image, such as the image ID and the image capture distance mode.

    Methods:
        __init__(self): Initializes a new instance of the ImageTag class.
        get_type(self) -> int: Gets the type of the image tag.
        clone(self) -> ImageTag: Creates a copy of the image tag.
        get_image_id(self) -> int: Gets the ID of the image.
        set_image_id(self, imgId: int) -> None: Sets the ID of the image.
        get_image_capture_distance_mode(self) -> int: Gets the capture distance mode of the image.
        set_image_capture_distance_mode(self, mode: int) -> None: Sets the capture distance mode of the image.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        """
        Initializes a new instance of the ImageTag class.
        """

        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CImageTag(self))

    __destroy__ = _DynamsoftCore.delete_CImageTag

    @abstractmethod
    def get_type(self) -> int:
        """
        Gets the type of the image tag.

        Returns:
            int: The type of the image tag.
        """
        pass

    @abstractmethod
    def clone(self) -> "ImageTag":
        """
        Creates a copy of the image tag.

        Returns:
            ImageTag: A copy of the ImageTag object.
        """
        pass

    def get_image_id(self) -> int:
        """
        Gets the ID of the image.

        Returns:
            int: The ID of the image.
        """
        return _DynamsoftCore.CImageTag_GetImageId(self)

    def set_image_id(self, imgId: int) -> None:
        """
        Sets the ID of the image.

        Args:
            imgId (int): The ID of the image.
        """
        return _DynamsoftCore.CImageTag_SetImageId(self, imgId)

    def get_image_capture_distance_mode(self) -> int:
        """
        Gets the capture distance mode of the image.

        Returns:
            int: The capture distance mode of the image.
        """
        return _DynamsoftCore.CImageTag_GetImageCaptureDistanceMode(self)

    def set_image_capture_distance_mode(self, mode: int) -> None:
        """
        Sets the capture distance mode of the image.

        Args:
            mode (int): The capture distance mode of the image.
        """
        return _DynamsoftCore.CImageTag_SetImageCaptureDistanceMode(self, mode)

_DynamsoftCore.CImageTag_register(ImageTag)

class FileImageTag(ImageTag):
    """
    FileImageTag represents an image tag that is associated with a file.
    It inherits from the ImageTag class and adds two attributes, a file path and a page number.

    Methods:
        __init__(file_path: str, page_number: int, total_pages: int):Initializes a new instance of the FileImageTag class.
        get_type(self) -> int: Gets the type of the image tag.
        clone(self) -> FileImageTag: Creates a copy of the image tag.
        get_file_path(self) -> str: Gets the file path of the image.
        get_page_number(self) -> int: Gets the page number of the current image in the Multi-Page image file.
        get_total_pages(self) -> int: Gets the total page number of the Multi-Page image file.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self, file_path: str, page_number: int, total_pages: int):
        """
        Initializes a new instance of the FileImageTag class.

        Args:
            file_path (str): The file path.
            page_number (int): The page number of the file image.
            total_pages (int): The total pages of the file image.
        """
        _DynamsoftCore.Class_init(
            self, _DynamsoftCore.new_CFileImageTag(self, file_path, page_number, total_pages)
        )

    __destroy__ = _DynamsoftCore.delete_CFileImageTag

    def get_type(self) -> int:
        """
        Gets the type of the image tag.

        Returns:
            int: The type of the image tag.
        """
        return _DynamsoftCore.CFileImageTag_GetType(self)

    def clone(self) -> "FileImageTag":
        """
        Creates a copy of the image tag.

        Returns:
            FileImageTag: A copy of the FileImageTag object.
        """
        return _DynamsoftCore.CFileImageTag_Clone(self)

    def get_file_path(self) -> str:
        """
        Gets the file path of the image.

        Returns:
            str: The file path of the image.
        """
        return _DynamsoftCore.CFileImageTag_GetFilePath(self)

    def get_page_number(self) -> int:
        """
        Gets the page number of the current image in the Multi-Page image file.

        Returns:
            int: The page number of the current image in the Multi-Page image file.
        """
        return _DynamsoftCore.CFileImageTag_GetPageNumber(self)

    def get_total_pages(self) -> int:
        """
        Gets the total page number of the Multi-Page image file.

        Returns:
            int: The total page number of the Multi-Page image file.
        """
        return _DynamsoftCore.CFileImageTag_GetTotalPages(self)

_DynamsoftCore.CFileImageTag_register(FileImageTag)

class VideoFrameTag(ImageTag):
    """
    VideoFrameTag represents a video frame tag, which is a type of image tag that is used to store additional information about a video frame.

    Methods:
        __init__(self, quality: int, is_cropped: bool, crop_region: Rect, original_width: int, original_height: int): Initializes a new instance of the VideoFrameTag class.
        get_video_frame_quality(self) -> int: Gets the quality of the video frame.
        is_cropped(self) -> bool: Determines whether the video frame is cropped.
        get_crop_region(self) -> Rect: Gets the crop region of the video frame.
        get_original_width(self) -> int: Gets the original width of the video frame.
        get_original_height(self) -> int: Gets the original height of the video frame.
        get_type(self) -> int: Gets the type of the image tag.
        clone(self) -> VideoFrameTag: Creates a copy of the image tag.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def get_video_frame_quality(self) -> int:
        """
        Gets the quality of the video frame.

        Returns:
            The quality of the video frame.
        """
        return _DynamsoftCore.CVideoFrameTag_GetVideoFrameQuality(self)

    def is_cropped(self) -> bool:
        """
        Determines whether the video frame is cropped.

        Returns:
            True if the video frame is cropped, False otherwise.
        """
        return _DynamsoftCore.CVideoFrameTag_IsCropped(self)

    def get_crop_region(self) -> Rect:
        """
        Gets the crop region of the video frame.

        Returns:
            A Rect object that represents the crop region of the video frame. It may be null.
        """
        return _DynamsoftCore.CVideoFrameTag_GetCropRegion(self)

    def get_original_width(self) -> int:
        """
        Gets the original width of the video frame.

        Returns:
            The original width of the video frame.
        """
        return _DynamsoftCore.CVideoFrameTag_GetOriginalWidth(self)

    def get_original_height(self) -> int:
        """
        Gets the original height of the video frame.

        Returns:
            The original height of the video frame.
        """
        return _DynamsoftCore.CVideoFrameTag_GetOriginalHeight(self)

    def get_type(self) -> int:
        """
        Gets the type of the image tag.

        Returns:
            The type of the image tag.
        """
        return _DynamsoftCore.CVideoFrameTag_GetType(self)

    def clone(self) -> "VideoFrameTag":
        """
        Creates a copy of the image tag.

        Returns:
            A copy of the VideoFrameTag object.
        """
        return _DynamsoftCore.CVideoFrameTag_Clone(self)

    def __init__(
        self,
        quality: int,
        is_cropped: bool,
        crop_region: Rect,
        original_width: int,
        original_height: int,
    ):
        """
        Initializes a new instance of the VideoFrameTag class.

        Args:
            quality (int): The quality of the video frame.
            is_cropped (bool): A boolean value indicating whether the video frame is cropped.
            crop_region (Rect): A Rect object that represents the crop region of the video frame.
            original_width (int): The original width of the video frame.
            original_height (int): The original height of the video frame.
        """
        _DynamsoftCore.Class_init(
            self,
            _DynamsoftCore.new_CVideoFrameTag(
                self, quality, is_cropped, crop_region, original_width, original_height
            ),
        )

    __destroy__ = _DynamsoftCore.delete_CVideoFrameTag


_DynamsoftCore.CVideoFrameTag_register(VideoFrameTag)

class ImageData:
    """
    This class represents image data, which contains the image bytes, width, height, stride, pixel format, orientation, and a tag.

    Methods:
        __init__(self, bytes: bytes, width: int, height: int, stride: int, format: int, orientation: int = 0, tag: ImageTag = None): Initializes an ImageData object.
        get_bytes(self) -> bytes: Returns the image bytes.
        get_width(self) -> int: Returns the width of the image.
        get_height(self) -> int: Returns the height of the image.
        get_stride(self) -> int: Returns the stride of the image.
        get_image_pixel_format(self) -> int: Returns the pixel format of the image.
        get_orientation(self) -> int: Returns the orientation of the image.
        get_image_tag(self) -> ImageTag: Returns the tag of the image.
        set_image_tag(self, tag: ImageTag): Sets the tag of the image.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(
        self,
        bytes: bytes,
        width: int,
        height: int,
        stride: int,
        format: int,
        orientation: int = 0,
        tag: ImageTag = None,
    ):
        """
        Initializes an ImageData object.

        Args:
            bytes: The image byte array.
            width: The width of the image.
            height: The height of the image.
            stride: The stride of the image.
            format: The pixel format of the image.
            orientation: The orientation of the image.
            tag: The tag of the image.
        """
        _DynamsoftCore.Class_init(
            self,
            _DynamsoftCore.new_CImageData(
                bytes, width, height, stride, format, orientation, tag
            ),
        )

    __destroy__ = _DynamsoftCore.delete_CImageData

    def get_bytes(self) -> bytes:
        """
        Gets the image byte array.

        Returns:
            The image byte array.
        """
        return _DynamsoftCore.CImageData_GetBytes(self)

    def get_width(self) -> int:
        """
        Gets the width of the image.

        Returns:
            The width of the image.
        """
        return _DynamsoftCore.CImageData_GetWidth(self)

    def get_height(self) -> int:
        """
        Gets the height of the image.

        Returns:
            The height of the image.
        """
        return _DynamsoftCore.CImageData_GetHeight(self)

    def get_stride(self) -> int:
        """
        Gets the stride of the image.

        Returns:
            The stride of the image.
        """
        return _DynamsoftCore.CImageData_GetStride(self)

    def get_image_pixel_format(self) -> EnumImagePixelFormat:
        """
        Gets the pixel format of the image.

        Returns:
            The pixel format of the image.
        """
        return _DynamsoftCore.CImageData_GetImagePixelFormat(self)

    def get_orientation(self) -> int:
        """
        Gets the orientation of the image.

        Returns:
            The orientation of the image.
        """
        return _DynamsoftCore.CImageData_GetOrientation(self)

    def get_image_tag(self) -> ImageTag:
        """
        Gets the tag of the image.

        Returns:
            The tag of the image.
        """
        return _DynamsoftCore.CImageData_GetImageTag(self)

    def set_image_tag(self, tag: ImageTag) -> None:
        """
        Sets the tag of the image.

        Args:
            tag: The tag of the image.
        """
        return _DynamsoftCore.CImageData_SetImageTag(self, tag)

_DynamsoftCore.CImageData_register(ImageData)

class CapturedResultItem:
    """
    The CapturedResultItem class represents an item in a captured result.
    It is an abstract base class with multiple subclasses, each representing a different type of captured item such as barcode, text line, detected quad, normalized image, raw image, parsed item, etc.

    Methods:
    get_type(self): Gets the type of the captured result item.
    get_reference_item(self): Gets the referenced item in the captured result item.
    get_target_roi_def_name(self): Gets the name of the target ROI definition.
    get_task_name(self): Gets the name of the task.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    __destroy__ = _DynamsoftCore.CCapturedResultItem_Release

    def __init__(self):
        """
        Initializes an instance of the CapturedResultItem class.

        Raises:
            AttributeError: If the constructor is called directly.
        """
        raise AttributeError("No constructor defined - class is abstract")

    def get_type(self) -> int:
        """
        Gets the type of the captured result item.

        Returns:
            int: The type of the captured result item.
        """
        return _DynamsoftCore.CCapturedResultItem_GetType(self)

    def get_reference_item(self) -> "CapturedResultItem":
        """
        Gets the referenced item in the captured result item.

        Returns:
            CapturedResultItem: The referenced item in the captured result item.
        """
        if not hasattr(self, '_ref_item'):
            self._ref_item = _DynamsoftCore.CCapturedResultItem_GetReferenceItem(self)
        return self._ref_item

    def get_target_roi_def_name(self) -> str:
        """
        Gets the name of the target ROI definition.

        Returns:
            str: The name of the target ROI definition.
        """
        return _DynamsoftCore.CCapturedResultItem_GetTargetROIDefName(self)

    def get_task_name(self) -> str:
        """
        Gets the name of the task.

        Returns:
            str: The name of the task.
        """
        return _DynamsoftCore.CCapturedResultItem_GetTaskName(self)


_DynamsoftCore.CCapturedResultItem_register(CapturedResultItem)

class OriginalImageResultItem(CapturedResultItem):
    """
    The OriginalImageResultItem class represents a captured original image result item. It is a derived class of CapturedResultItem and provides a class to get the image data.

    Methods:
    get_image_data(self): Gets the image data for the OriginalImageResultItem.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        """
        Initializes a new instance of the OriginalImageResultItem class.

        Raises:
            AttributeError: If the constructor is called.
        """
        raise AttributeError("No constructor defined - class is abstract")

    def get_image_data(self) -> ImageData:
        """
        Gets the image data for the OriginalImageResultItem.

        Returns:
            ImageData: The ImageData object that contains the image data for the OriginalImageResultItem.
        """
        return _DynamsoftCore.COriginalImageResultItem_GetImageData(self)


_DynamsoftCore.COriginalImageResultItem_register(OriginalImageResultItem)

#new
class CapturedResultBase:
    """
    The CapturedResultBase class is an abstract base class for captured results.

    Methods:
        get_original_image_hash_id(self) -> str: Gets the hash ID of the original image.
        get_original_image_tag(self) -> ImageTag: Gets the tag of the original image.
        get_rotation_transform_matrix(self) -> List[float]: Gets the rotation transform matrix.
        get_error_code(self) -> int: Gets the error code of the detection operation.
        get_error_string(self) -> str: Gets the error string of the detection operation.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )
    def __init__(self):
        """
        Initializes a new instance of the OriginalImageResultItem class.

        Raises:
            AttributeError: If the constructor is called.
        """
        raise AttributeError("No constructor defined - class is abstract")

    def get_original_image_hash_id(self) -> str:
        """
        Gets the hash ID of the original image.

        Returns:
            The hash ID of the original image as a string.
        """
        return _DynamsoftCore.CCapturedResultBase_GetOriginalImageHashId(
            self
        )

    def get_original_image_tag(self) -> ImageTag:
        """
        Gets the tag of the original image.

        Returns:
            An ImageTag object containing the tag of the original image.
        """
        return _DynamsoftCore.CCapturedResultBase_GetOriginalImageTag(self)

    def get_rotation_transform_matrix(self) -> List[float]:
        """
        Gets the 3x3 rotation transformation matrix of the original image relative to the rotated image.

        Returns:
            A float list of length 9 which represents a 3x3 rotation matrix.
        """
        return _DynamsoftCore.CCapturedResultBase_GetRotationTransformMatrix(
            self
        )

    def get_error_code(self) -> int:
        """
        Gets the error code of the detection operation.

        Returns:
            The error code of the detection operation.
        """
        return _DynamsoftCore.CCapturedResultBase_GetErrorCode(self)

    def get_error_string(self) -> str:
        """
        Gets the error message of the detection operation.

        Returns:
            The error message of the detection operation as a string.
        """
        return _DynamsoftCore.CCapturedResultBase_GetErrorString(self)

_DynamsoftCore.CCapturedResultBase_register(CapturedResultBase)
#end new

class ImageSourceErrorListener(ABC):
    """
    The ImageSourceErrorListener class defines a listener for receiving error notifications from an image source.

    Methods:
        on_error_received(self, error_code: int, error_message: str) -> None: Called when an error is received.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCore.Class_init(
            self, _DynamsoftCore.new_CImageSourceErrorListener(self)
        )

    @abstractmethod
    def on_error_received(self, error_code: int, error_message: str) -> None:
        """
        Called when an error is received from the image source.

        Args:
            error_code (int): The integer error code indicating the type of error.
            error_message(str): A string containing the error message providing additional information about the error.
        """

        pass

    __destroy__ = _DynamsoftCore.delete_CImageSourceErrorListener

_DynamsoftCore.CImageSourceErrorListener_register(ImageSourceErrorListener)


class ImageSourceAdapter(ABC):
    """
    This class provides an interface for fetching and buffering images.
    It is an abstract class that needs to be implemented by a concrete class to provide actual functionality.

    Methods:
        add_image_to_buffer(self, image: ImageData) -> None: Adds an image to the buffer.
        has_next_image_to_fetch(self) -> bool: Checks if there is the next image to fetch.
        start_fetching(self) -> None: Starts fetching images.
        stop_fetching(self) -> None: Stops fetching images.
        get_image(self) -> ImageData: Gets an image from the buffer.
        set_max_image_count(self, count: int) -> None: Sets the maximum count of images in the buffer.
        get_max_image_count(self) -> int: Gets the maximum count of images in the buffer.
        set_buffer_overflow_protection_mode(self, mode: int) -> None: Sets the mode of buffer overflow protection.
        get_buffer_overflow_protection_mode(self) -> int: Gets the mode of buffer overflow protection.
        has_image(self, image_id: int) -> bool: Checks if there is an image with the specified ID in the buffer.
        set_next_image_to_return(self, image_id: int, keep_in_buffer: bool = True) -> bool: Sets the next image to return and optionally keeps it in the buffer.
        get_image_count(self) -> int: Gets the number of images in the buffer.
        is_buffer_empty(self) -> bool: Checks if the buffer is empty.
        clear_buffer(self) -> None: Clears the buffer.
        set_colour_channel_usage_type(self, type: int) -> None: Sets the usage type of a color channel in images.
        get_colour_channel_usage_type(self) -> int: Gets the usage type of a color channel in images.
        set_error_listener(self, listener: ImageSourceErrorListener) -> None: Sets an error listener object that will receive notifications when errors occur during image source operations.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCore.Class_init(
            self, _DynamsoftCore.new_CImageSourceAdapter(self)
        )

    __destroy__ = _DynamsoftCore.delete_CImageSourceAdapter

    def add_image_to_buffer(self, image: ImageData) -> None:
        """
        Adds an image to the buffer.

        Args:
            image (ImageData): The image to be added.
        """
        return _DynamsoftCore.CImageSourceAdapter_AddImageToBuffer(self, image)

    @abstractmethod
    def has_next_image_to_fetch(self) -> bool:
        """
        Checks if there is the next image to fetch.

        Returns:
            bool: True if there is the next image to fetch, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_HasNextImageToFetch(self)

    def start_fetching(self) -> None:
        """
        Starts fetching images.
        """
        return _DynamsoftCore.CImageSourceAdapter_StartFetching(self)

    def stop_fetching(self) -> None:
        """
        Stops fetching images.
        """
        return _DynamsoftCore.CImageSourceAdapter_StopFetching(self)

    def get_image(self) -> ImageData:
        """
        Gets an image from the buffer.

        Returns:
            ImageData: The image from the buffer.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetImage(self)

    def set_max_image_count(self, count: int) -> None:
        """
        Sets the maximum count of images in the buffer.

        Args:
            count (int): The maximum count of images.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetMaxImageCount(self, count)

    def get_max_image_count(self) -> int:
        """
        Gets the maximum count of images in the buffer.

        Returns:
            int: The maximum count of images.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetMaxImageCount(self)

    def set_buffer_overflow_protection_mode(self, mode: int) -> None:
        """
        Sets the mode of buffer overflow protection.

        Args:
            mode (int): The mode of buffer overflow protection.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetBufferOverflowProtectionMode(
            self, mode
        )

    def get_buffer_overflow_protection_mode(self) -> int:
        """
        Gets the mode of buffer overflow protection.

        Returns:
            int: The mode of buffer overflow protection.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetBufferOverflowProtectionMode(self)

    def has_image(self, image_id: int) -> bool:
        """
        Checks if there is an image with the specified ID in the buffer.

        Args:
            image_id (int): The ID of the image to check.

        Returns:
            bool: True if there is the image with the specified ID, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_HasImage(self, image_id)

    def set_next_image_to_return(
        self, image_id: int, keep_in_buffer: bool = True
    ) -> bool:
        """
        Sets the next image to return and optionally keeps it in the buffer.

        Args:
            image_id (int): The ID of the image to set as the next image to return.
            keep_in_buffer (bool, optional): Whether to keep the image in the buffer. Defaults to True.

        Returns:
            bool: True if the image is set as the next image to return, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetNextImageToReturn(
            self, image_id, keep_in_buffer
        )

    def get_image_count(self) -> int:
        """
        Gets the number of images in the buffer.

        Returns:
            int: The number of images in the buffer.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetImageCount(self)

    def is_buffer_empty(self) -> bool:
        """
        Checks if the buffer is empty.

        Returns:
            bool: True if the buffer is empty, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_IsBufferEmpty(self)

    def clear_buffer(self) -> None:
        """
        Clears the buffer.
        """
        return _DynamsoftCore.CImageSourceAdapter_ClearBuffer(self)

    def set_colour_channel_usage_type(self, type: int) -> None:
        """
        Sets the usage type of a color channel in images.

        Args:
            type (int): The usage type of a color channel in images.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetColourChannelUsageType(self, type)

    def get_colour_channel_usage_type(self) -> int:
        """
        Gets the usage type of a color channel in images.

        Returns:
            int: The usage type of a color channel in images.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetColourChannelUsageType(self)

    def set_error_listener(self, listener: ImageSourceErrorListener) -> None:
        """
        Sets an error listener object that will receive notifications when errors occur during image source operations.

        Args:
            listener (ImageSourceErrorListener): The listening object of the type ImageSourceErrorListener that will handle error notifications.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetErrorListener(self, listener)


_DynamsoftCore.CImageSourceAdapter_register(ImageSourceAdapter)


class PDFReadingParameter:
    """
    The PDFReadingParameter class represents the parameters for reading a PDF file.
    It contains the mode of PDF reading, the DPI (dots per inch) value, and the raster data source type.

    Attributes:
        mode (int): The mode used for PDF reading. This is one of the values of the EnumPDFReadingMode enumeration.
        dpi (int): The DPI (dots per inch) value.
        raster_data_source (int): The raster data source type. This is one of the values of the EnumRasterDataSource enumeration.
    Methods:
        __init__(self): Initializes a new instance of the PDFReadingParameter class.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    mode: int = property(
        _DynamsoftCore.CPDFReadingParameter_mode_get,
        _DynamsoftCore.CPDFReadingParameter_mode_set,
    )
    dpi: int = property(
        _DynamsoftCore.CPDFReadingParameter_dpi_get,
        _DynamsoftCore.CPDFReadingParameter_dpi_set,
    )
    raster_data_source: int = property(
        _DynamsoftCore.CPDFReadingParameter_rasterDataSource_get,
        _DynamsoftCore.CPDFReadingParameter_rasterDataSource_set,
    )

    def __init__(self):
        """
        Initializes a new instance of the PDFReadingParameter class.

        This constructor initializes the properties with default values:
        mode: 2 (EnumPDFReadingMode.PDFRM_RASTER.value)
        dpi: 300
        raster_data_source: 0 (EnumRasterDataSource.RDS_RASTERIZED_PAGES.value)
        """
        _DynamsoftCore.Class_init(
            self, _DynamsoftCore.new_CPDFReadingParameter()
        )

    __destroy__ = _DynamsoftCore.delete_CPDFReadingParameter


_DynamsoftCore.CPDFReadingParameter_register(PDFReadingParameter)

class Contour:
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    __destroy__ = _DynamsoftCore.delete_CContour

    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CContour())
    def __repr__(self):
        points = self.get_points()
        list_repr = ", ".join(f"({obj.x}, {obj.y})" for obj in points)
        return f"Contour[{list_repr}]"
    def set_points(self, points: List[Point]) -> None:
        _DynamsoftCore.CContour_SetPoints(self, points)

    def get_points(self) -> List[Point]:
        return _DynamsoftCore.CContour_GetPoints(self)

_DynamsoftCore.CContour_register(Contour)
class Vector4:
    """
    The CVector4 class represents a four-dimensional vector.

    Attributes:
        value (List[int]): A list of four integer values representing the components of the vector.

    Methods:
        Set(self, v1: int, v2: int, v3: int, v4: int) -> None: Sets the components value of a four-dimensional vector.
        __getitem__(self, index: int) -> int: Gets the component value at the specified index in the CVector4.
        __setitem__(self, index: int, value: int) -> None: Sets the component value at the specified index in the CVector4.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    value = property(_DynamsoftCore.CVector4_value_get, _DynamsoftCore.CVector4_value_set)

    def __init__(self, v1: int, v2: int, v3: int, v4: int):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CVector4(v1, v2, v3, v4))
    __destroy__ = _DynamsoftCore.delete_CVector4

    def Set(self, v1: int, v2: int, v3: int, v4: int) -> None:
        """
        Sets the components value of a four-dimensional vector.

        Args:
            v1 (int): The first component value of the four-dimensional vector.
            v2 (int): The second component value of the four-dimensional vector.
            v3 (int): The third component value of the four-dimensional vector.
            v4 (int): The fourth component value of the four-dimensional vector.
        """
        return _DynamsoftCore.CVector4_Set(self, v1, v2, v3, v4)

    def __getitem__(self, index: int) -> int:
        if index < 0 or index > 3:
            raise IndexError("Index out of range")
        return _DynamsoftCore.CVector4_GetItem(self, index)

    def __setitem__(self, index: int, value: int) -> None:
        if index < 0 or index > 3:
            raise IndexError("Index out of range")
        _DynamsoftCore.CVector4_SetItem(self, index, value)

_DynamsoftCore.CVector4_register(Vector4)

class LineSegment:
    """
    The LineSegment class represents a line segment in 2D space.
    It contains two CPoint objects, which represent the start point and end point of the line segment.

    Attributes:
        start_point (Point): The start point of the line segment.
        end_point (Point): The end point of the line segment.
        id (int): The ID of the line segment.

    Methods:
        __repr__(self) -> str: Returns a string representation of the LineSegment object.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    start_point: Point = property(_DynamsoftCore.CLineSegment_GetStartPoint, _DynamsoftCore.CLineSegment_SetStartPoint)
    end_point: Point = property(_DynamsoftCore.CLineSegment_GetEndPoint, _DynamsoftCore.CLineSegment_SetEndPoint)
    id: int = property(_DynamsoftCore.CLineSegment_GetId, _DynamsoftCore.CLineSegment_SetId)

    def __init__(self, start_point: Point, end_point: Point, line_id: int = -1):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CLineSegment(start_point, end_point, line_id))

    def __repr__(self):
        return f"LineSegment[start_point=({self.start_point.x},{self.start_point.y}), end_point=({self.end_point.x},{self.end_point.y})]"

    __destroy__ = _DynamsoftCore.delete_CLineSegment

_DynamsoftCore.CLineSegment_register(LineSegment)
class Corner:
    """
    Corner is a structure in an image consisting of two line segments and intersection point. A Corner represents a point at which the image's brightness or color sharply changes.

    Attributes:
        type (int): The type of the corner.
        intersection (Point): The intersection point of the two line segments.
        line1 (LineSegment): The first line segment.
        line2 (LineSegment): The second line segment.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    type: int = property(_DynamsoftCore.CCorner_type_get, _DynamsoftCore.CCorner_type_set)
    intersection: Point = property(_DynamsoftCore.CCorner_intersection_get, _DynamsoftCore.CCorner_intersection_set)
    line1: LineSegment = property(_DynamsoftCore.CCorner_line1_get, _DynamsoftCore.CCorner_line1_set)
    line2: LineSegment = property(_DynamsoftCore.CCorner_line2_get, _DynamsoftCore.CCorner_line2_set)
    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CCorner())
    __destroy__ = _DynamsoftCore.delete_CCorner

_DynamsoftCore.CCorner_register(Corner)
class Edge:
    """
    CEdge is a structure composed of two Corner points in an image.
    A Corner represents a point at which the image's brightness or color sharply changes.
    Therefore, a CEdge is a line segment connecting two such points that have been identified as Corners.

    Attributes:
        start_corner (Corner): The start corner of the edge.
        end_corner (Corner): The end corner of the edge.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    start_corner: Corner = property(_DynamsoftCore.CEdge_startCorner_get, _DynamsoftCore.CEdge_startCorner_set)
    end_corner: Corner = property(_DynamsoftCore.CEdge_endCorner_get, _DynamsoftCore.CEdge_endCorner_set)

    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CEdge())
    __destroy__ = _DynamsoftCore.delete_CEdge

_DynamsoftCore.CEdge_register(Edge)

class IntermediateResultExtraInfo:
    """
    The IntermediateResultExtraInfo class represents the extra information for generating an intermediate result unit.

    Attributes:
        target_roi_def_name (str): Specifies the name of the TargetROIDef object that generates the intermediate result.
        task_name (str): Specifies the name of the task that generates the intermediate result.
        is_section_level_result (bool): Specifies whether the intermediate result is section-level result.
        section_type (int): Specifies the SectionType that generates the intermediate result.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    target_roi_def_name: str = property(_DynamsoftCore.IntermediateResultExtraInfo_targetROIDefName_get, _DynamsoftCore.IntermediateResultExtraInfo_targetROIDefName_set)
    task_name: str = property(_DynamsoftCore.IntermediateResultExtraInfo_taskName_get, _DynamsoftCore.IntermediateResultExtraInfo_taskName_set)
    is_section_level_result: bool = property(_DynamsoftCore.IntermediateResultExtraInfo_isSectionLevelResult_get, _DynamsoftCore.IntermediateResultExtraInfo_isSectionLevelResult_set)
    section_type: int = property(_DynamsoftCore.IntermediateResultExtraInfo_sectionType_get, _DynamsoftCore.IntermediateResultExtraInfo_sectionType_set)

    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_IntermediateResultExtraInfo())
    __destroy__ = _DynamsoftCore.delete_IntermediateResultExtraInfo

_DynamsoftCore.IntermediateResultExtraInfo_register(IntermediateResultExtraInfo)

class RegionObjectElement:
    """
    The RegionObjectElement class represents an element of a region object in 2D space. It is an abstract class that provides the interface for region object elements.

    Methods:
        get_location(self) -> Quadrilateral: Gets the location of the region object element.
        get_referenced_element(self) -> RegionObjectElement: Gets the referenced element of the region object element.
        get_element_type(self) -> int: Gets the type of the region object element.
        clone(self) -> RegionObjectElement: Clones the region object element.
        get_image_data(self) -> ImageData: Gets the image data of the region object element.
        """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    __destroy__ = _DynamsoftCore.CRegionObjectElement_Release

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_location(self) -> Quadrilateral:
        """
        Gets the location of the region object element.

        Returns:
            A Quadrilateral object which represents the location of the region object element.
        """
        return _DynamsoftCore.CRegionObjectElement_GetLocation(self)

    def get_referenced_element(self) -> "RegionObjectElement":
        """
        Gets the referenced element of the region object element.

        Returns:
            A RegionObjectElement object which represents the referenced element of the region object element.
        """
        return _DynamsoftCore.CRegionObjectElement_GetReferencedElement(self)

    def get_element_type(self) -> int:
        """
        Gets the type of the region object element.

        Returns:
            An integer which represents the type of the region object element.
        """
        return _DynamsoftCore.CRegionObjectElement_GetElementType(self)

    def clone(self) -> "RegionObjectElement":
        """
        Clones the region object element.

        Returns:
            A copy of the region object element.
        """
        return _DynamsoftCore.CRegionObjectElement_Clone(self)

    def get_image_data(self) -> ImageData:
        """
        Gets the image data for the RegionObjectElement.

        Returns:
            An ImageData object that contains the image data for the RegionObjectElement.
        """
        return _DynamsoftCore.CRegionObjectElement_GetImageData(self)

_DynamsoftCore.CRegionObjectElement_register(RegionObjectElement)
class PredetectedRegionElement(RegionObjectElement):
    """
    The PredetectedRegionElement class represents a region element that has been pre-detected in an image.
    It is a subclass of the CRegionObjectElement.

    Methods:
        get_mode_name(self) -> str: Gets the name of the detection mode used to detect this region element.
        set_location(self, loc: Quadrilateral) -> int: Sets the location of the region object element.
        get_label_id(self) -> int: Gets the label ID of the predetected region element.
        get_label_name(self) -> str: Gets the label name of the predetected region element.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.CImageProcessingModule_CreatePredetectedRegionElement())

    def get_mode_name(self) -> str:
        """
        Gets the name of the detection mode used to detect this region element.

        Returns:
            The name of the detection mode used to detect this region element.
        """
        return _DynamsoftCore.CPredetectedRegionElement_GetModeName(self)

    def set_location(self, loc: Quadrilateral) -> int:
        """
        Sets the location of the region object element.

        Args:
            loc(Quadrilateral): The location of the predetected region element.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CPredetectedRegionElement_SetLocation(self, loc)

    def get_label_id(self) -> int:
        """
        Gets the label ID of the predetected region element.

        Returns:
            The label ID of the predetected region element.
        """
        return _DynamsoftCore.CPredetectedRegionElement_GetLabelId(self)

    def get_label_name(self) -> str:
        """
        Gets the label name of the predetected region element.

        Returns:
            The label name of the predetected region element.
        """
        return _DynamsoftCore.CPredetectedRegionElement_GetLabelName(self)

_DynamsoftCore.CPredetectedRegionElement_register(PredetectedRegionElement)

class AuxiliaryRegionElement(RegionObjectElement):
    """
    The AuxiliaryRegionElement class represents a region element that is auxiliary to a predetected region element.
    It is a subclass of the CRegionObjectElement.

    Methods:
        get_name(self) -> str: Gets the name of this auxiliary region.
        get_confidence(self) -> int: Gets the confidence level of this auxiliary region detection.
        set_name(self, name: str) -> None: Sets the name/type of this auxiliary region.
        set_location(self, location: Quadrilateral) -> int: Sets the location of the auxiliary region element.
        set_confidence(self, confidence: int) -> None: Sets the confidence level of this auxiliary region detection.
    """
    def __init__(self):
        _DynamsoftCore.Class_init(self, _DynamsoftCore.CImageProcessingModule_CreateAuxiliaryRegionElement())

    def get_name(self) -> str:
        """
        Gets the name of this auxiliary region.

        Returns:
            Returns a string representing the region name (e.g., "PortraitZone", "SignatureArea").
        """
        return _DynamsoftCore.CAuxiliaryRegionElement_GetName(self)

    def get_confidence(self) -> int:
        """
        Gets the confidence level of this auxiliary region detection.

        Returns:
            Returns the confidence value, typically in the range [0, 100].
        """
        return _DynamsoftCore.CAuxiliaryRegionElement_GetConfidence(self)

    def set_name(self, name: str) -> None:
        """
        Sets the name/type of this auxiliary region.

        Args:
            name(str): The region name to set (e.g., "PortraitZone", "SignatureArea").
        """
        _DynamsoftCore.CAuxiliaryRegionElement_SetName(self, name)

    def set_location(self, location: Quadrilateral) -> int:
        """
        Sets the location of this auxiliary region.

        Args:
            location(Quadrilateral): A quadrilateral defining the region boundaries.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CAuxiliaryRegionElement_SetLocation(self, location)

    def set_confidence(self, confidence: int) -> None:
        """
        Sets the confidence level of this auxiliary region detection.

        Args:
            confidence(int): The confidence value to set, typically in the range [0, 100].
        """
        return _DynamsoftCore.CAuxiliaryRegionElement_SetConfidence(self, confidence)

_DynamsoftCore.CAuxiliaryRegionElement_register(AuxiliaryRegionElement)

class IntermediateResultUnit:
    """
    The IntermediateResultUnit class represents an intermediate result unit used in image processing.
    It is an abstract base class with multiple subclasses, each representing a different type of unit such as pre-detected regions, localized barcodes, decoded barcodes, localized text lines, binary image, gray image, etc.

    Methods:
        get_hash_id(self) -> str: Gets the hash ID of the intermediate result unit.
        get_original_image_hash_id(self) -> str: Gets the hash ID of the original image.
        get_original_image_tag(self) -> ImageTag: Gets the image tag of the original image.
        get_transform_matrix(self, matrix_type: EnumTransformMatrixType) -> List[float]: Gets the transformation matrix via EnumTransformMatrixType.
        get_type(self) -> int: Gets the type of the intermediate result unit.
        clone(self) -> IntermediateResultUnit: Creates a copy of the intermediate result unit.
        replace(self, unit: IntermediateResultUnit) -> int: Replaces the specified IntermediateResultUnit object with the current IntermediateResultUnit object.
        get_usage_count(self) -> int: Gets the usage count of the intermediate result unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    __destroy__ = _DynamsoftCore.CIntermediateResultUnit_Release

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_hash_id(self) -> str:
        """
        Gets the hash ID of the intermediate result unit.

        Returns:
            The hash ID of the intermediate result unit.
        """
        return _DynamsoftCore.CIntermediateResultUnit_GetHashId(self)

    def get_original_image_hash_id(self) -> str:
        """
        Gets the hash ID of the original image.

        Returns:
            The hash ID of the original image.
        """
        return _DynamsoftCore.CIntermediateResultUnit_GetOriginalImageHashId(self)

    def get_original_image_tag(self) -> ImageTag:
        """
        Gets the image tag of the original image.

        Returns:
            The image tag of the original image.
        """
        return _DynamsoftCore.CIntermediateResultUnit_GetOriginalImageTag(self)

    def get_transform_matrix(self, matrix_type: EnumTransformMatrixType) -> List[float]:
        """
        Gets the transformation matrix via EnumTransformMatrixType.

        Args:
            matrix_type(EnumTransformMatrixType): The type of the transformation matrix.

        Returns:
            A float array which represents the transform matrix.
        """
        return _DynamsoftCore.CIntermediateResultUnit_GetTransformMatrix(self, matrix_type)

    def get_type(self) -> int:
        """
        Gets the type of the intermediate result unit.

        Returns:
            The type of the intermediate result unit.
        """
        return _DynamsoftCore.CIntermediateResultUnit_GetType(self)

    def clone(self) -> "IntermediateResultUnit":
        """
        Creates a copy of the intermediate result unit.

        Returns:
            A copy of the intermediate result unit.
        """
        return _DynamsoftCore.CIntermediateResultUnit_Clone(self)

    def replace(self, unit: "IntermediateResultUnit") -> int:
        """
        Replaces the specified IntermediateResultUnit object with the current IntermediateResultUnit object.

        Args:
            unit(IntermediateResultUnit): The IntermediateResultUnit object to be replaced.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CIntermediateResultUnit_Replace(self, unit)

    def get_usage_count(self) -> int:
        """
        Gets the usage count of the intermediate result unit.

        Returns:
            The usage count of the intermediate result unit.
        """
        return _DynamsoftCore.CIntermediateResultUnit_GetUsageCount(self)

_DynamsoftCore.CIntermediateResultUnit_register(IntermediateResultUnit)
class IntermediateResult:
    """
    The IntermediateResult class represents a container containing a collection of IntermediateResultUnit objects.

    Methods:
        get_intermediate_result_units(self) -> List[IntermediateResultUnit]: Gets a list of IntermediateResultUnit objects in the collection.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_intermediate_result_units(self) -> List[IntermediateResultUnit]:
        """
        Gets a list of IntermediateResultUnit objects in the collection.

        Returns:
            A list of IntermediateResultUnit objects.
        """
        list = []
        count = _DynamsoftCore.CIntermediateResult_GetCount(self)
        for i in range(count):
            list.append(_DynamsoftCore.CIntermediateResult_GetIntermediateResultUnit(self, i))
        return list

_DynamsoftCore.CIntermediateResult_register(IntermediateResult)

class ColourImageUnit(IntermediateResultUnit):
    """
    The ColourImageUnit class represents a unit that contains color image.
    It is derived from the IntermediateResultUnit class.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of the colour image unit.
        set_image_data(self, img_data: ImageData) -> int: Sets the image data of the color image unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the image data of the colour image unit.

        Returns:
            the ImageData object that contains the image data of the color image unit.
        """
        return _DynamsoftCore.CColourImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the image data of the color image unit.

        Args:
            img_data(ImageData): The image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CColourImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CColourImageUnit_register(ColourImageUnit)
class ScaledColourImageUnit(IntermediateResultUnit):
    """
    The ScaledColourImageUnit class represents an intermediate result unit that contains scaled color image.
    It is derived from the IntermediateResultUnit class.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of the scaled color image unit.
        set_image_data(self, img_data: ImageData) -> int: Sets the image data of the scaled color image unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the image data of the scaled color image unit.

        Returns:
            the ImageData object that contains the image data of the scaled color image unit.
        """
        return _DynamsoftCore.CScaledColourImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the image data of the scaled color image unit.

        Args:
            img_data(ImageData): The image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CScaledColourImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CScaledColourImageUnit_register(ScaledColourImageUnit)
class GrayscaleImageUnit(IntermediateResultUnit):
    """
    The GrayscaleImageUnit class represents a grayscale image unit.
    It is a subclass of IntermediateResultUnit.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of the grayscale image unit.
        set_image_data(self, img_data: ImageData) -> int: Sets the image data of the grayscale image unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the image data of the grayscale image unit.

        Returns:
            the ImageData object that contains the image data of the grayscale image unit.
        """
        return _DynamsoftCore.CGrayscaleImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the image data of the grayscale image unit.

        Args:
            img_data(ImageData): The image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CGrayscaleImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CGrayscaleImageUnit_register(GrayscaleImageUnit)
class TransformedGrayscaleImageUnit(IntermediateResultUnit):
    """
    The TransformedGrayscaleImageUnit class is a subclass of IntermediateResultUnit that represents a transformed grayscale image.
    It may be the original grayscale image or the inverted image of the original grayscale image.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of the transformed grayscale image unit.
        set_image_data(self, img_data: ImageData) -> int: Sets the image data of the transformed grayscale image unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the image data of the transformed grayscale image unit.

        Returns:
            the ImageData object that contains the image data of the transformed grayscale image unit.
        """
        return _DynamsoftCore.CTransformedGrayscaleImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the image data of the transformed grayscale image unit.

        Args:
            img_data(ImageData): The image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CTransformedGrayscaleImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CTransformedGrayscaleImageUnit_register(TransformedGrayscaleImageUnit)
class PredetectedRegionsUnit(IntermediateResultUnit):
    """
    The PredetectedRegionsUnit class represents a unit that contains a collection of pre-detected regions.
    It inherits from the IntermediateResultUnit class and stores the result of image color pre-detection.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of pre-detected regions in the collection.

        Returns:
            The number of pre-detected regions in the collection.
        """
        return _DynamsoftCore.CPredetectedRegionsUnit_GetCount(self)

    def get_predetected_region(self, index: int) -> PredetectedRegionElement:
        """
        Gets a pre-detected region in the collection.

        Args:
            index(int): The index of the pre-detected region to get.

        Returns:
            The pre-detected region at the specified index.
        """
        return _DynamsoftCore.CPredetectedRegionsUnit_GetPredetectedRegion(self, index)

    def remove_all_predetected_regions(self) -> None:
        """
        Removes all pre-detected regions in the unit.
        """
        return _DynamsoftCore.CPredetectedRegionsUnit_RemoveAllPredetectedRegions(self)

    def remove_predetected_region(self, index: int) -> int:
        """
        Removes a pre-detected region in the unit at the specified index.

        Args:
            index(int): The index of the pre-detected region to remove.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CPredetectedRegionsUnit_RemovePredetectedRegion(self, index)

    def add_predetected_region(self, element: PredetectedRegionElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX):
        """
        Adds a pre-detected region to the unit.

        Args:
            element(PredetectedRegionElement): The pre-detected region to add.
            matrix_to_original_image(List[float]): The transformation matrix from the pre-detected region to the original image.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CPredetectedRegionsUnit_AddPredetectedRegion(self, element, matrix_to_original_image)

    def set_predetected_region(self, index: int, element: PredetectedRegionElement, matrix_to_original_image: List[float] = IDENTITY_MATRIX):
        """
        Sets a pre-detected region in the unit at the specified index.

        Args:
            index(int): The index of the pre-detected region to set.
            element(PredetectedRegionElement): The pre-detected region to set.
            matrix_to_original_image(List[float]): The transformation matrix from the pre-detected region to the original image.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CPredetectedRegionsUnit_SetPredetectedRegion(self, index, element, matrix_to_original_image)

_DynamsoftCore.CPredetectedRegionsUnit_register(PredetectedRegionsUnit)
class EnhancedGrayscaleImageUnit(IntermediateResultUnit):
    """
    The EnhancedGrayscaleImageUnit class represents an intermediate result unit that contains an enhanced grayscale image data.
    Gray enhancement methods include gray equalization, gray smoothing, gray sharpening and smoothing.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of the enhanced grayscale image unit.
        set_image_data(self, img_data: ImageData) -> int: Sets the image data of the enhanced grayscale image unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the image data of the enhanced grayscale image unit.

        Returns:
            the ImageData object that contains the image data of the enhanced grayscale image unit.
        """
        return _DynamsoftCore.CEnhancedGrayscaleImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the image data of the enhanced grayscale image unit.

        Args:
            img_data(ImageData): The image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CEnhancedGrayscaleImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CEnhancedGrayscaleImageUnit_register(EnhancedGrayscaleImageUnit)
class BinaryImageUnit(IntermediateResultUnit):
    """
    The BinaryImageUnit class represents a binary image unit that inherits from IntermediateResultUnit.
    It inherits from the IntermediateResultUnit class and stores binary image data.

    Methods:
        get_image_data(self) -> ImageData: Gets the image data of the binary image unit.
        set_image_data(self, img_data: ImageData) -> int: Sets the image data of the binary image unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the image data of the binary image unit.

        Returns:
            the ImageData object that contains the image data of the binary image unit.
        """
        return _DynamsoftCore.CBinaryImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the image data of the binary image unit.

        Args:
            img_data(ImageData): The image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CBinaryImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CBinaryImageUnit_register(BinaryImageUnit)
class TextureDetectionResultUnit(IntermediateResultUnit):
    """
    The TextureDetectionResultUnit class represents an intermediate result unit for texture detection.
    It is derived from the IntermediateResultUnit class and contains the x-direction spacing and y-direction spacing of the texture stripes.

    Methods:
        get_x_spacing(self) -> int: Gets the x-direction spacing of the texture stripes.
        get_y_spacing(self) -> int: Gets the y-direction spacing of the texture stripes.
        set_x_spacing(self, x_spacing: int): Sets the x-direction spacing of the texture stripes.
        set_y_spacing(self, y_spacing: int): Sets the y-direction spacing of the texture stripes.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_x_spacing(self) -> int:
        """
        Gets x-direction spacing of the texture stripes.

        Returns:
            The x-direction spacing of the texture stripes.
        """
        return _DynamsoftCore.CTextureDetectionResultUnit_GetXSpacing(self)

    def get_y_spacing(self) -> int:
        """
        Gets y-direction spacing of the texture stripes.

        Returns:
            The y-direction spacing of the texture stripes.
        """
        return _DynamsoftCore.CTextureDetectionResultUnit_GetYSpacing(self)

    def set_x_spacing(self, x_spacing: int) -> None:
        """
        Sets the x-direction spacing of the texture stripes.

        Args:
            x_spacing (int): The x-direction spacing of the texture stripes.
        """
        return _DynamsoftCore.CTextureDetectionResultUnit_SetXSpacing(self, x_spacing)

    def set_y_spacing(self, y_spacing: int) -> None:
        """
        Sets the y-direction spacing of the texture stripes.

        Args:
            y_spacing (int): The y-direction spacing of the texture stripes.
        """
        return _DynamsoftCore.CTextureDetectionResultUnit_SetYSpacing(self, y_spacing)

_DynamsoftCore.CTextureDetectionResultUnit_register(TextureDetectionResultUnit)
class TextureRemovedGrayscaleImageUnit(IntermediateResultUnit):
    """
    The TextureRemovedGrayscaleImageUnit class represents an intermediate result unit that contains grayscale image data with textures removed.

    Methods:
        get_image_data(self) -> ImageData: Gets the grayscale image data with textures removed.
        set_image_data(self, img_data: ImageData) -> int: Sets the grayscale image data with textures removed.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the grayscale image data with textures removed.

        Returns:
            the ImageData object that contains the grayscale image data with textures removed.
        """
        return _DynamsoftCore.CTextureRemovedGrayscaleImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the grayscale image data with textures removed.

        Args:
            img_data(ImageData): The grayscale image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CTextureRemovedGrayscaleImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CTextureRemovedGrayscaleImageUnit_register(TextureRemovedGrayscaleImageUnit)
class TextureRemovedBinaryImageUnit(IntermediateResultUnit):
    """
    The TextureRemovedBinaryImageUnit class represents an intermediate result unit that stores binary image data with texture removed.

    Methods:
        get_image_data(self) -> ImageData: Gets the binary image data with texture removed.
        set_image_data(self, img_data: ImageData) -> int: Sets the binary image data with texture removed.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_image_data(self) -> ImageData:
        """
        Gets the binary image data with texture removed.

        Returns:
            the ImageData object that contains the binary image data with texture removed.
        """
        return _DynamsoftCore.CTextureRemovedBinaryImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the binary image data with texture removed.

        Args:
            img_data(ImageData): The binary image data to set.

        Returns:
            Returns 0 if success, otherwise an error code.
        """
        return _DynamsoftCore.CTextureRemovedBinaryImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CTextureRemovedBinaryImageUnit_register(TextureRemovedBinaryImageUnit)
class TextZone(object):
    """
    The TextZone class represents a text zone.

    Methods:
        get_location(self) -> Quadrilateral: Gets the location of the text zone.
        set_location(self, loc: Quadrilateral) -> None: Sets the location of the text zone.
        get_char_contours_indices(self) -> List[int]: Gets the indices of the character contours.
        set_char_contours_indices(self, char_contours_indices: List[int]): Sets the indices of the character contours.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, loc: Quadrilateral = None, char_contours_indices: List[int] = None):
        if char_contours_indices is not None and loc is None:
            raise ValueError("If char_contours_indices is not None, loc should not be None")
        _DynamsoftCore.Class_init(self, _DynamsoftCore.new_CTextZone(loc, char_contours_indices))

    def get_location(self) -> Quadrilateral:
        """
        Gets the location of the text zone.

        Returns:
            The location of the text zone.
        """
        return _DynamsoftCore.CTextZone_GetLocation(self)

    def set_location(self, loc: Quadrilateral) -> None:
        """
        Sets the location of the text zone.

        Args:
            loc(Quadrilateral): The location of the text zone.
        """
        return _DynamsoftCore.CTextZone_SetLocation(self, loc)

    def get_char_contours_indices(self) -> List[int]:
        """
        Gets the indices of the character contours.

        Returns:
            The indices of the character contours.
        """
        return _DynamsoftCore.CTextZone_GetCharContoursIndices(self)

    def set_char_contours_indices(self, char_contours_indices: List[int]) -> None:
        """
        Sets the indices of the character contours.

        Args:
            char_contours_indices(List[int]): The indices of the character contours.
        """
        return _DynamsoftCore.CTextZone_SetCharContoursIndices(self, char_contours_indices)

    __destroy__ = _DynamsoftCore.delete_CTextZone

_DynamsoftCore.CTextZone_register(TextZone)
class TextZonesUnit(IntermediateResultUnit):
    """
    The TextZonesUnit class represents a unit that contains text zones.
    It is derived from IntermediateResultUnit class and provides methods to retrieve the count and details of text zones.

    Methods:
        get_count(self) -> int: Gets the number of text zones in the unit.
        get_text_zone(self, index: int) -> Tuple[int, TextZone]: Gets the quadrilateral shape of the text zone at the specified index.
        remove_all_text_zones(self) -> None: Removes all text zones from the unit.
        remove_text_zone(self, index: int) -> int: Removes the text zone at the specified index.
        add_text_zone(self, text_zone: TextZone, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:  Adds a text zone to the unit.
        set_text_zone(self, index: int, text_zone: TextZone, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the text zone at the specified index.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of text zones in the unit.

        Returns:
            The number of text zones in the unit.
        """
        return _DynamsoftCore.CTextZonesUnit_GetCount(self)

    def get_text_zone(self, index: int) -> Tuple[int, TextZone]:
        """
        Gets the quadrilateral shape of the text zone at the specified index.

        Args:
            index(int): The index of the text zone.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation, returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
            - text_zone (TextZone): The quadrilateral shape of the text zone at the specified index.
        """
        return _DynamsoftCore.CTextZonesUnit_GetTextZone(self, index)

    def remove_all_text_zones(self) -> None:
        """
        Removes all text zones from the unit.
        """
        return _DynamsoftCore.CTextZonesUnit_RemoveAllTextZones(self)

    def remove_text_zone(self, index: int) -> int:
        """
        Removes the text zone at the specified index.

        Args:
            index(int): The index of the text zone.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CTextZonesUnit_RemoveTextZone(self, index)

    def add_text_zone(self,text_zone: TextZone, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a text zone to the unit.

        Args:
            text_zone(TextZone): The text zone to add.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CTextZonesUnit_AddTextZone(self, text_zone, matrix_to_original_image)

    def set_text_zone(self, index: int, text_zone: TextZone, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the text zone at the specified index.

        Args:
            index(int): The index of the text zone.
            text_zone(TextZone): The text zone to set.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CTextZonesUnit_SetTextZone(self, index, text_zone, matrix_to_original_image)

_DynamsoftCore.CTextZonesUnit_register(TextZonesUnit)
class TextRemovedBinaryImageUnit(IntermediateResultUnit):
    """
    The TextRemovedBinaryImageUnit class represents an intermediate result unit that contains a binary image with the text removed.

    Methods:
        get_image_data(self) -> ImageData: Gets the binary image data.
        set_image_data(self, img_data: ImageData) -> int: Sets the binary image data.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_image_data(self) -> ImageData:
        """
        Gets the binary image data with the text removed.

        Returns:
            The binary image data with the text removed.
        """
        return _DynamsoftCore.CTextRemovedBinaryImageUnit_GetImageData(self)

    def set_image_data(self, img_data: ImageData) -> int:
        """
        Sets the binary image data with the text removed.

        Args:
            img_data(ImageData): The binary image data with the text removed.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CTextRemovedBinaryImageUnit_SetImageData(self, img_data)

_DynamsoftCore.CTextRemovedBinaryImageUnit_register(TextRemovedBinaryImageUnit)
class ContoursUnit(IntermediateResultUnit):
    """
    The ContoursUnit class represents a unit that contains contours as intermediate results.
    It is derived from the IntermediateResultUnit class.

    Methods:
        get_contours(self) -> Tuple[int, List[Contour], List[Vector4]]: Gets the contours and hierarchies in the unit.
        set_contours(self, contours: List[Contour], hierarchies: List[Vector4], matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the contours and hierarchies in the unit.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_contours(self) -> Tuple[int, List[Contour], List[Vector4]]:
        """
        Gets the contours and hierarchies in the unit.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation, returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
            - contours <List[Contour]>: The contours in the unit.
            - hierarchies <List[Vector4]>: AThe hierarchies in the unit.
        """
        return _DynamsoftCore.CContoursUnit_GetContours(self)

    def set_contours(self, contours: List[Contour], hierarchies: List[Vector4], matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the contours and hierarchies in the unit.

        Args:
            contours(List[Contour]): The contours to set.
            hierarchies(List[Vector4]): The hierarchies to set.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CContoursUnit_SetContours(self, contours, hierarchies, matrix_to_original_image)

_DynamsoftCore.CContoursUnit_register(ContoursUnit)
class LineSegmentsUnit(IntermediateResultUnit):
    """
    The LineSegmentsUnit class represents a collection of line segments in 2D space. It is a derived class of IntermediateResultUnit.

    Methods:
        get_count(self) -> int: Gets the number of line segments in the collection.
        get_line_segment(self, index: int) -> LineSegment: Gets the line segment at the specified index.
        remove_all_line_segments(self) -> None: Removes all line segments from the unit.
        remove_line_segment(self, index: int) -> int: Removes the line segment at the specified index.
        add_line_segment(self, line : LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Adds a line segment to the unit.
        set_line_segment(self, index: int, line : LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the line segment at the specified index.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of line segments in the collection.

        Returns:
            The number of line segments in the collection.
        """
        return _DynamsoftCore.CLineSegmentsUnit_GetCount(self)

    def get_line_segment(self, index: int) -> LineSegment:
        """
        Gets the line segment at the specified index.

        Args:
            index(int): The index of the line segment to retrieve.

        Returns:
            The line segment at the specified index.
        """
        return _DynamsoftCore.CLineSegmentsUnit_GetLineSegment(self, index)

    def remove_all_line_segments(self) -> None:
        """
        Removes all line segments from the unit.
        """
        return _DynamsoftCore.CLineSegmentsUnit_RemoveAllLineSegments(self)

    def remove_line_segment(self, index: int) -> int:
        """
        Removes the line segment at the specified index.

        Args:
            index(int): The index of the line segment to remove.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CLineSegmentsUnit_RemoveLineSegment(self, index)

    def add_line_segment(self, line : LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a line segment to the unit.

        Args:
            line(LineSegment): The line segment to add.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CLineSegmentsUnit_AddLineSegment(self, line, matrix_to_original_image)

    def set_line_segment(self, index: int, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the line segment at the specified index.

        Args:
            index(int): The index of the line segment to set.
            line(LineSegment): The line segment to set.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CLineSegmentsUnit_SetLineSegment(self, index, line, matrix_to_original_image)

_DynamsoftCore.CLineSegmentsUnit_register(LineSegmentsUnit)
class ShortLinesUnit(IntermediateResultUnit):
    """
    The ShortLinesUnit class represents a collection of short lines in 2D space.
    It is a derived class of IntermediateResultUnit.

    Methods:
        get_count(self) -> int: Gets the number of short lines in the collection.
        get_short_line(self, index: int) -> LineSegment: Gets the short line at the specified index.
        remove_all_short_lines(self) -> None: Removes all short lines from the unit.
        remove_short_line(self, index: int) -> int: Removes the short line at the specified index.
        add_short_line(self, line : LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Adds a short line to the unit.
        set_short_line(self, index: int, line : LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int: Sets the short line at the specified index.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")


    def get_count(self) -> int:
        """
        Gets the number of short lines in the collection.

        Returns:
            The number of short lines in the collection.
        """
        return _DynamsoftCore.CShortLinesUnit_GetCount(self)

    def get_short_line(self, index: int) -> LineSegment:
        """
        Gets the short line at the specified index.

        Args:
            index(int): The index of the short line to get.

        Returns:
            The short line at the specified index.
        """
        return _DynamsoftCore.CShortLinesUnit_GetShortLine(self, index)

    def remove_all_short_lines(self) -> None:
        """
        Removes all short lines from the unit.
        """
        return _DynamsoftCore.CShortLinesUnit_RemoveAllShortLines(self)

    def remove_short_line(self, index: int) -> int:
        """
        Removes the short line at the specified index.

        Args:
            index(int): The index of the short line to remove.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CShortLinesUnit_RemoveShortLine(self, index)

    def add_short_line(self, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Adds a short line to the unit.

        Args:
            line(LineSegment): The short line to add.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CShortLinesUnit_AddShortLine(self, line, matrix_to_original_image)

    def set_short_line(self, index: int, line: LineSegment, matrix_to_original_image: List[float] = IDENTITY_MATRIX) -> int:
        """
        Sets the short line at the specified index.

        Args:
            index(int): The index of the short line to set.
            line(LineSegment): The short line to set.
            matrix_to_original_image(List[float]): The matrix to original image.

        Returns:
            Returns 0 if the operation succeeds, or a nonzero error code if the operation fails.
        """
        return _DynamsoftCore.CShortLinesUnit_SetShortLine(self, index, line, matrix_to_original_image)

_DynamsoftCore.CShortLinesUnit_register(ShortLinesUnit)
class ObservationParameters:
    """
    The ObservationParameters class is used to set filter conditions for the IntermediateReusltReceiver, so that only intermediate results meeting specific conditions will be called back.

    Methods:
        set_observed_result_unit_types(self, types: int) -> None: Sets the types of intermediate result units that have been observed.
        get_observed_result_unit_types(self) -> int: Gets the types of intermediate result units that have been observed.
        is_result_unit_type_observed(self, type: int) -> bool: Determines whether the specified result unit type was observed.
        def add_observed_task(self, task_name: str) ->None: Adds observed task name to be notified when relevant results are available.
        def remove_observed_task(self, task_name: str) -> None:Removes observed task name to be notified when relevant results are available.
        is_task_observed(self, task_name: str) -> bool: Determines whether the specified task was observed.
        set_result_unit_types_only_for_input(self, types: int) -> None: Sets the type of intermediate result unit that indicates skipping default calculations and replacing with input data units.
        get_result_unit_types_only_for_input(self) -> int: Gets the type of intermediate result unit that indicates skipping default calculations and replacing with input data units.
        is_result_unit_type_only_for_input(self, type: int) -> bool: Determines whether the specified type of intermediate result unit indicates skipping default calculations and replacing with input data units.
    """
    _thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftCore.delete_CObservationParameters

    def set_observed_result_unit_types(self, types: int) -> None:
        """
        Sets the types of intermediate result units that have been observed.

        Args:
            types(int): The observed types of intermediate result units.
        """
        return _DynamsoftCore.CObservationParameters_SetObservedResultUnitTypes(self, types)

    def get_observed_result_unit_types(self) -> int:
        """
        Gets the types of intermediate result units that have been observed.

        Returns:
            The observed types of intermediate result units.
        """
        return _DynamsoftCore.CObservationParameters_GetObservedResultUnitTypes(self)

    def is_result_unit_type_observed(self, type: int) -> bool:
        """
        Determines whether the specified result unit type was observed.

        Args:
            type(int): The type of the result unit to check.

        Returns:
            Returns a boolean value indicating whether the specified result unit type was observed.
        """
        return _DynamsoftCore.CObservationParameters_IsResultUnitTypeObserved(self, type)

    def add_observed_task(self, task_name: str) ->None:
        """
        Adds observed task name to be notified when relevant results are available.

        Args:
            task_name(str): The specified task name.
        """
        return _DynamsoftCore.CObservationParameters_AddObservedTask(self, task_name)

    def remove_observed_task(self, task_name: str) -> None:
        """
        Removes observed task name to be notified when relevant results are available.

        Args:
            task_name(str): The specified task name.
        """
        return _DynamsoftCore.CObservationParameters_RemoveObservedTask(self, task_name)

    def is_task_observed(self, task_name: str) -> bool:
        """
        Determines whether the specified task was observed.

        Args:
            task_name(str): The specified task name.

        Returns:
            Returns a boolean value indicating whether the specified task was observed.
        """
        return _DynamsoftCore.CObservationParameters_IsTaskObserved(self, task_name)

    def set_result_unit_types_only_for_input(self, types: int) -> None:
        """
        Sets the type of intermediate result unit that indicates skipping default calculations and replacing with input data units.

        Args:
            types(int): The type of intermediate result unit that serves as the combination value of EnumIntermediateResultUnitType.
        """
        return _DynamsoftCore.CObservationParameters_SetResultUnitTypesOnlyForInput(self, types)

    def get_result_unit_types_only_for_input(self) -> int:
        """
        Gets the type of intermediate result unit that indicates skipping default calculations and replacing with input data units.

        Returns:
            Returns the type of intermediate result unit that serves as the combination value of IntermediateResultUnitType.
        """
        return _DynamsoftCore.CObservationParameters_GetResultUnitTypesOnlyForInput(self)

    def is_result_unit_type_only_for_input(self, type: int) -> bool:
        """
        Determines whether the specified type of intermediate result unit indicates skipping default calculations and replacing with input data units.

        Args:
            type(int): The type of intermediate result unit to check.

        Returns:
            Returns a boolean value indicating whether the specified type of intermediate result unit indicates skipping default calculations and replacing with input data units.
        """
        return _DynamsoftCore.CObservationParameters_IsResultUnitTypeOnlyForInput(self, type)

_DynamsoftCore.CObservationParameters_register(ObservationParameters)