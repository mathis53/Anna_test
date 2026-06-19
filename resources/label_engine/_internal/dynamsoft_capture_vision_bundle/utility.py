__version__ = "2.0.40.9454"

if __package__ or "." in __name__:
    from .cvr import *
else:
    from cvr import *

if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftUtility
else:
    import _DynamsoftUtility


from abc import ABC, abstractmethod
from typing import List, Tuple, Union
from enum import IntEnum

class FilterType(IntEnum):
    FT_HIGH_PASS = _DynamsoftUtility.FT_HIGH_PASS
    FT_SHARPEN = _DynamsoftUtility.FT_SHARPEN
    FT_SMOOTH = _DynamsoftUtility.FT_SMOOTH

class UtilityModule:
    """
    The UtilityModule class contains utility functions.

    Methods:
        get_version() -> str: Returns the version of the utility module.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns the version of the utility module.

        Returns:
            A string representing the version of the utility module.
        """
        return __version__ + " (Algorithm " + _DynamsoftUtility.CUtilityModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CUtilityModule()
        )

    __destroy__ = _DynamsoftUtility.delete_CUtilityModule


_DynamsoftUtility.CUtilityModule_register(UtilityModule)

class MultiFrameResultCrossFilter(CapturedResultFilter):
    """
    The MultiFrameResultCrossFilter class is responsible for filtering captured results.
    It contains several callback functions for different types of results, including raw image, decoded barcodes, recognized text lines, detected quads, deskewed images, and parsed results.

    Methods:
        enable_result_cross_verification(self, result_item_types: int, enabled: bool) -> None: Enables result cross verification feature to improve the accuracy of video streaming recognition results.
        is_result_cross_verification_enabled(self, type: int) -> bool: Determines whether the result cross verification feature is enabled for the specific captured result item type.
        enable_result_deduplication(self, result_item_types: int, enabled: bool) -> None: Enables result deduplication feature to filter out the duplicate results in the period of duplicateForgetTime for video streaming recognition.
        is_result_deduplication_enabled(self, type: int) -> bool: Determines whether the result deduplication feature is enabled for the specific result item type.
        set_duplicate_forget_time(self, result_item_types: int, duplicate_forget_time: int) -> None: Sets the duplicate forget time for the specific captured result item types.
        get_duplicate_forget_time(self, type: int) -> int: Gets the duplicate forget time for a specific captured result item type.
        set_max_overlapping_frames(self, result_item_types: int, max_overlapping_frames: int) -> None: Sets the max referencing frames count for the to-the-latest overlapping feature.
        get_max_overlapping_frames(self, type: int) -> int: Gets the max referencing frames count for the to-the-latest overlapping feature.
        enable_latest_overlapping(self, result_item_types: int, enable: bool) -> None: Enables to-the-latest overlapping feature. The output decoded barcode result will become a combination of the recent results if the  latest frame is proved to be similar with the previous.
        is_latest_overlapping_enabled(self, type: int) -> bool: Determines whether the to-the-latest overlapping feature is enabled for the specific result item type.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self, cvr: CaptureVisionRouter = None):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CMultiFrameResultCrossFilter(cvr)
        )

    __destroy__ = _DynamsoftUtility.delete_CMultiFrameResultCrossFilter

    def enable_result_cross_verification(
        self, result_item_types: int, enabled: bool
    ) -> None:
        """
        Enables result cross verification feature to improve the accuracy of video streaming recognition results.

        Args:
            result_item_types (int): A bitwise OR combination of one or more values from the EnumCapturedResultItemType enumeration.
            enabled (bool): Set whether to enable result verification.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_EnableResultCrossVerification(
            self, result_item_types, enabled
        )

    def is_result_cross_verification_enabled(self, type: int) -> bool:
        """
        Determines whether the result cross verification feature is enabled for the specific captured result item type.

        Args:
            type (int): The specific captured result item type. It is a value from the EnumCapturedResultItemType enumeration.

        Returns:
            A bool value indicating whether result verification is enabled for the specific captured result item type.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_IsResultCrossVerificationEnabled(
            self, type
        )

    def enable_result_deduplication(self, result_item_types: int, enabled: bool) -> None:
        """
        Enables result deduplication feature to filter out the duplicate results in the period of duplicateForgetTime for video streaming recognition.

        Args:
            result_item_types (int): A bitwise OR combination of one or more values from the EnumCapturedResultItemType enumeration.
            enabled (bool): Set whether to enable result result deduplication.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_EnableResultDeduplication(
            self, result_item_types, enabled
        )

    def is_result_deduplication_enabled(self, type: int) -> bool:
        """
        Determines whether the result deduplication feature is enabled for the specific result item type.

        Args:
            type (int): The specific captured result item type. It is a value from the EnumCapturedResultItemType enumeration.

        Returns:
            A bool value indicating whether result deduplication is enabled for the specific result item type.
        """
        return (
            _DynamsoftUtility.CMultiFrameResultCrossFilter_IsResultDeduplicationEnabled(
                self, type
            )
        )

    def set_duplicate_forget_time(self, result_item_types: int, time: int) -> None:
        """
        Sets the duplicate forget time for the specific captured result item types. The same captured result item will be returned only once during the period if deduplication feature is enabled. The default value is 3000ms.

        Args:
            result_item_types (int): A bitwise OR combination of one or more values from the EnumCapturedResultItemType enumeration.
            time (int): The duplicate forget time measured in milliseconds. The value rang is [1, 180000].
        """

        return _DynamsoftUtility.CMultiFrameResultCrossFilter_SetDuplicateForgetTime(
            self, result_item_types, time
        )

    def get_duplicate_forget_time(self, type: int) -> int:
        """
        Gets the duplicate forget time for a specific captured result item type.

        Args:
            type (int): The specific captured result item type. It is a value from the EnumCapturedResultItemType enumeration.

        Returns:
            The duplicate forget time for the specific captured result item type.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_GetDuplicateForgetTime(
            self, type
        )

    def set_max_overlapping_frames(self, result_item_types: int, max_overlapping_frames: int) -> None:
        """
        Sets the max referencing frames count for the to-the-latest overlapping feature.

        Args:
            result_item_types (int): Specifies one or multiple specific result item types, which can be defined using CapturedResultItemType.
            max_overlapping_frames (int): The max referencing frames count for the to-the-latest overlapping feature.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_SetMaxOverlappingFrames(
            self, result_item_types, max_overlapping_frames
        )

    def get_max_overlapping_frames(self, type: int) -> int:
        """
        Gets the max referencing frames count for the to-the-latest overlapping feature.

        Args:
            type (int): Specifies a specific result item type, which can be defined using CapturedResultItemType.

        Returns:
            The max referencing frames count for the to-the-latest overlapping feature.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_GetMaxOverlappingFrames(
            self, type
        )

    def enable_latest_overlapping(self, result_item_types: int, enabled: bool) -> None:
        """
        Enables to-the-latest overlapping feature. The output decoded barcode result will become a combination of the recent results if the  latest frame is proved to be similar with the previous.

        Args:
            result_item_types (int): The or value of the captured result item types.
            enable (bool): Set whether to enable to-the-latest overlapping.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_EnableLatestOverlapping(
            self, result_item_types, enabled
        )

    def is_latest_overlapping_enabled(self, type: int) -> bool:
        """
        Determines whether the to-the-latest overlapping feature is enabled for the specific result item type.

        Args:
            type (int): The specific captured result item type.

        Returns:
            A bool value indicating whether to-the-latest overlapping is enabled for the specific captured result item type.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_IsLatestOverlappingEnabled(
            self, type
        )

    def set_result_cross_verification_criteria(self, result_item_types: int, frame_window: int, min_consistent_frames: int) -> None:
        """
        This function allows customization of the multi-frame verification parameters,
        controlling how many frames are analyzed and how many consistent results are required.

        Args:
            result_item_types (int): A bitwise OR combination of one or more values from the EnumCapturedResultItemType enumeration.
            frame_window (int): The number of frames to consider for cross-verification.
            min_consistent_frames (int): The minimum number of frames that must contain consistent results for verification to succeed.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_SetResultCrossVerificationCriteria(self, result_item_types, frame_window, min_consistent_frames)

    def get_result_cross_verification_criteria(self, result_item_type: EnumCapturedResultItemType) -> Tuple[int, int]:
        """
        Gets the cross-verification criteria for a specified result item type.

        Args:
            result_item_type (int): The result item type to query (CapturedResultItemType value).

        Returns:
            A tuple containing the frame window size and the minimum consistent frames.
        """
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_GetResultCrossVerificationCriteria(self, result_item_type)

_DynamsoftUtility.CMultiFrameResultCrossFilter_register(MultiFrameResultCrossFilter)

class ProactiveImageSourceAdapter(ImageSourceAdapter, ABC):
    """
    The ProactiveImageSourceAdapter class is an abstract class that extends the ImageSourceAdapter class. It provides classs for proactively fetching images in a separate thread.

    Methods:
        _fetch_image(): This method needs to be implemented in the derived class. It is called in a loop in the Fetching thread to obtain images.
        set_image_fetch_interval(self, milliseconds: int) -> None: Sets the time interval for the ImageSource to wait before attempting to fetch another image to put in the buffer.
        get_image_fetch_interval(self) -> int: Gets the time interval for the ImageSource to wait before attempting to fetch another image to put in the buffer.
        has_next_image_to_fetch(self) -> bool: Determines whether there are more images left to fetch.
        start_fetching(self) -> None: Starts fetching images.
        stop_fetching(self) -> None: Stops fetching images.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CProactiveImageSourceAdapter(self)
        )

    __destroy__ = _DynamsoftUtility.delete_CProactiveImageSourceAdapter

    @abstractmethod
    def _fetch_image():
        """
        This method needs to be implemented in the derived class. It is called in a loop in the Fetching thread to obtain images.
        """
        pass

    def has_next_image_to_fetch(self) -> bool:
        """
        Determines whether there are more images left to fetch.

        Returns:
            True if there are more images left to fetch, false otherwise.
        """
        return _DynamsoftUtility.CProactiveImageSourceAdapter_HasNextImageToFetch(self)

    def set_image_fetch_interval(self, milliseconds: int) -> None:
        """
        Sets the time interval for the ImageSource to wait before attempting to fetch another image to put in the buffer.

        Args:
            milliseconds (int): Specifies the wait time in milliseconds. If setting to -1, the ImageSource does not proactively fetch images.
        """
        return _DynamsoftUtility.CProactiveImageSourceAdapter_SetImageFetchInterval(
            self, milliseconds
        )

    def get_image_fetch_interval(self) -> int:
        """
        Gets the time interval for the ImageSource to wait before attempting to fetch another image to put in the buffer.

        Returns:
            The wait time in milliseconds. If the value is -1, the ImageSource does not proactively fetch images.
        """
        return _DynamsoftUtility.CProactiveImageSourceAdapter_GetImageFetchInterval(
            self
        )

    def start_fetching(self) -> None:
        """
        Starts fetching images.
        """
        return _DynamsoftUtility.CProactiveImageSourceAdapter_StartFetching(self)

    def stop_fetching(self) -> None:
        """
        Stops fetching images.
        """
        return _DynamsoftUtility.CProactiveImageSourceAdapter_StopFetching(self)


_DynamsoftUtility.CProactiveImageSourceAdapter_register(ProactiveImageSourceAdapter)

class DirectoryFetcher(ProactiveImageSourceAdapter):
    """
    The DirectoryFetcher class is a utility class that retrieves a list of files from a specified directory based on certain criteria. It inherits from the ProactiveImageSourceAdapter class.

    Methods:
        set_directory(self, path: str, filter: str) -> Tuple[int, str]: Sets the directory path and filter for the file search.
        set_pdf_reading_parameter(self, para: PDFReadingParameter) -> Tuple[int, str]: Sets the parameters for reading PDF files.
        set_pages(self, pages: List[int]) -> Tuple[int, str]: Sets the 0-based page indexes of a file (.tiff or .pdf) for barcode searching.
        has_next_image_to_fetch(self) -> bool: Determines whether there are more images left to fetch.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CDirectoryFetcher()
        )

    __destroy__ = _DynamsoftUtility.delete_CDirectoryFetcher

    def _fetch_image():
        pass
    def set_directory(self, *args) -> Tuple[int, str]:
        """
        Sets the directory path and filter for the file search.

        Args:
            path (str): The path of the directory to search.
            filter (str, optional): A string that specifies file extensions. For example: "*.BMP;*.JPG;*.GIF", or "*.*", etc. The default value is "*.bmp;*.jpg;*.jpeg;*.tif;*.png;*.tiff;*.gif;*.pdf".
            recursive (bool, optional): Specifies whether to load files recursively. The default value is False.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CDirectoryFetcher_SetDirectory(self, *args)

    def set_pdf_reading_parameter(self, para: PDFReadingParameter) -> Tuple[int, str]:
        """
        Sets the parameters for reading PDF files.

        Args:
            para (PDFReadingParameter): A PDFReadingParameter object with PDF files reading parameters.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CDirectoryFetcher_SetPDFReadingParameter(self, para)

    def has_next_image_to_fetch(self) -> bool:
        """
        Determines whether there are more images left to fetch.

        Returns:
            True if there are more images left to fetch, false otherwise.
        """
        return _DynamsoftUtility.CDirectoryFetcher_HasNextImageToFetch(self)

    def set_pages(self, pages: List[int]) -> Tuple[int, str]:
        """
        Sets the 0-based page indexes of a file (.tiff or .pdf). By default, there is no restriction on the number of pages that can be processed in a single file.

        Args:
            pages (List[int]): An integer list containing the page information to be set.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CDirectoryFetcher_SetPages(self, pages, len(pages))


_DynamsoftUtility.CDirectoryFetcher_register(DirectoryFetcher)


class FileFetcher(ImageSourceAdapter):
    """
    The FileFetcher class is a utility class that partitions a multi-page image file into multiple independent ImageData objects. It inherits from the ImageSourceAdapter class.

    Methods:
        set_file(self, path: str) -> Tuple[int, str]: Sets the file using a file path.
        set_pdf_reading_parameter(self, para: PDFReadingParameter) -> Tuple[int, str]: Sets the parameters for reading PDF files.
        set_pages(self, pages: List[int]) -> Tuple[int, str]: Sets the 0-based page indexes of a file (.tiff or .pdf) for barcode searching.
        has_next_image_to_fetch(self) -> bool: Determines whether there are more images left to fetch.
        get_image(self) -> ImageData: Gets the next image.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.Class_init(self, _DynamsoftUtility.new_CFileFetcher())

    __destroy__ = _DynamsoftUtility.delete_CFileFetcher

    def set_file(self, *args) -> Tuple[int, str]:
        """
        Sets the file using a file path, file bytes or an ImageData object.

        Args:
            A variable-length argument list. Can be one of the following:
            - file_path (str): Specifies the path of the file to process.
            - file_bytes (bytes): Specifies the image file bytes in memory to process.
            - image_data (ImageData): Specifies the image data to process.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CFileFetcher_SetFile(self, *args)

    def set_pdf_reading_parameter(self, para: PDFReadingParameter) -> Tuple[int, str]:
        """
        Sets the parameters for reading PDF files.

        Args:
            para (PDFReadingParameter): A PDFReadingParameter object with PDF files reading parameters.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CFileFetcher_SetPDFReadingParameter(self, para)

    def has_next_image_to_fetch(self) -> bool:
        """
        Determines whether there are more images left to fetch.

        Returns:
            True if there are more images left to fetch, False otherwise.
        """
        return _DynamsoftUtility.CFileFetcher_HasNextImageToFetch(self)

    def get_image(self) -> ImageData:
        """
        Gets the next image.

        Returns:
            The next image.
        """
        return _DynamsoftUtility.CFileFetcher_GetImage(self)

    def set_pages(self, pages: List[int]) -> Tuple[int, str]:
        """
        Sets the 0-based page indexes of a file (.tiff or .pdf). By default, there is no restriction on the number of pages that can be processed in a single file.

        Args:
            pages (List[int]): An integer list containing the page information to be set.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CFileFetcher_SetPages(self, pages, len(pages))


_DynamsoftUtility.CFileFetcher_register(FileFetcher)


class ImageIO:
    """
    The ImageIO class is a utility class for reading and writing images.

    Methods:
        save_to_file(self, image_data: ImageData, path: str, overwrite: bool = True) -> Tuple[int, str]: Saves an image to a file.
        read_from_file(self, file_path: str) -> Tuple[int, ImageData]: Reads an image from a file.
        read_from_memory(self, image_file_bytes: bytes) -> Tuple[int, ImageData]: Reads an image from a file in memory.
        save_to_memory(self, image_data: ImageData,image_format: EnumImageFileFormat) -> Tuple[int, bytes]: Saves an image to memory in the specified format.
        read_from_numpy(self, image: "np.ndarray", image_pixel_format: EnumImagePixelFormat) -> Tuple[int, str, ImageData]: Reads an image from a numpy array.
        save_to_numpy(self, image_data: ImageData) -> Tuple[int, str, "np.ndarray"]: Saves an image to a numpy array.
    """

    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CImageIO()
        )
    def save_to_file(
        self, image_data: ImageData, path: str, overwrite: bool = True
    ) -> Tuple[int, str]:
        """
        Saves an image to a file.

        Args:
            image_data (ImageData): The image data to be saved.
            path (str): The targeting file path with the file name and extension name.
            overwrite (bool, optional): A flag indicating whether to overwrite the file if it already exists. Defaults to true.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftUtility.CImageIO_SaveToFile(
            self, image_data, path, overwrite
        )

    def read_from_file(self, file_path: str) -> Tuple[int, ImageData]:
        """
        Reads an image from a file.
        If the file format is gif, pdf or tiff, we read the first page of the image file.
        The caller is responsible for freeing the memory allocated for the image.

        Args:
            file_path (str): The path of the image file.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - image_data (ImageData): An ImageData object representing the image if succeeds, None otherwise.
        """
        return _DynamsoftUtility.CImageIO_ReadFromFile(self, file_path)

    def read_from_memory(self, image_file_bytes: bytes) -> Tuple[int, ImageData]:
        """
        Reads an image from a file in memory.
        If the file format is gif, pdf or tiff, we read the first page of the image file.
        The caller is responsible for freeing the memory allocated for the image.

        Args:
            image_file_bytes (bytes): A bytes representing the image file in memory.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - image_data (ImageData): An ImageData object representing the image if succeeds, None otherwise.
        """
        return _DynamsoftUtility.CImageIO_ReadFromMemory(self, image_file_bytes)

    def save_to_memory(self, image_data: ImageData,image_format: EnumImageFileFormat) -> Tuple[int, bytes]:
        """
        Saves an image to memory in the specified format.

        Args:
            image_data (ImageData): The image data to be saved.
            image_format (EnumImageFileFormat): The desired image format.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - image_file_bytes (bytes): The byte array representing the saved image file if succeeds, None otherwise.
        """
        return _DynamsoftUtility.CImageIO_SaveToMemory(self, image_data, image_format)

    def read_from_numpy(self, image: "numpy.ndarray", image_pixel_format: EnumImagePixelFormat) -> Tuple[int, str, ImageData]:
        """
        Reads an image from a numpy array.

        Args:
            image (np.ndarray): A numpy array representing the image.
            image_pixel_format (EnumImagePixelFormat): The pixel format of the numpy array.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
            - image_data (ImageData): An ImageData object representing the image if succeeds, None otherwise.
        """
        return 0, "Success.", ImageData(image.tobytes(),image.shape[1],image.shape[0],image.strides[0], image_pixel_format)

    def save_to_numpy(self, image_data: ImageData) -> Tuple[int, str, "numpy.ndarray"]:
        """
        Saves an image to a numpy array.

        Args:
            image_data (ImageData): The image data to be saved.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
            - image (np.ndarray): A numpy array representing the saved image if succeeds, None otherwise.
        """
        import numpy as np
        width = image_data.get_width()
        height = image_data.get_height()
        image_bytes = image_data.get_bytes()
        format = image_data.get_image_pixel_format()
        err = 0
        err_str = "Success."
        if format == EnumImagePixelFormat.IPF_RGB_888:
            arr = np.frombuffer(image_bytes, dtype=np.uint8).reshape((height, width, 3))
        elif format == EnumImagePixelFormat.IPF_BGR_888:
            arr = np.frombuffer(image_bytes, dtype=np.uint8).reshape((height, width, 3))
            arr = arr[:, :, ::-1]
        elif format == EnumImagePixelFormat.IPF_GRAYSCALED \
            or format == EnumImagePixelFormat.IPF_BINARY \
                or format == EnumImagePixelFormat.IPF_BINARYINVERTED \
                    or format == EnumImagePixelFormat.IPF_BINARY_8 \
                        or format == EnumImagePixelFormat.IPF_BINARY_8_INVERTED:
            arr = np.frombuffer(image_bytes, dtype=np.uint8).reshape((height, width))
        else:
            err = EnumErrorCode.EC_IMAGE_PIXEL_FORMAT_NOT_MATCH
            if __package__ or "." in __name__:
                from . import _DynamsoftCore
            else:
                import _DynamsoftCore
            err_str = _DynamsoftCore.DC_GetErrorString(err)
            arr = None
        return err, err_str, arr

    __destroy__ = _DynamsoftUtility.delete_CImageIO

_DynamsoftUtility.CImageIO_register(ImageIO)

class ImageDrawer:
    """
    The ImageDrawer class provides methods for drawing various shapes on an image.

    Attributes:
        AnyShape: A type representing any shape that can be drawn on an image.

    Methods:
        draw_on_image(self, image: ImageData, shapes: List[AnyShape], color: int = 0xFFFF0000, thickness: int = 1) -> ImageData: Draws various shapes on an image.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )
    def __init__(self):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CImageDrawer()
        )

    def draw_on_image(
        self,
        image: ImageData,
        shapes: Union[
            List[Quadrilateral],
            List[LineSegment],
            List[Contour],
            List[Corner],
            List[Edge],
        ],
        color: int = 0xFFFF0000,
        thickness: int = 1,
    ) -> ImageData:
        """
        Draws various shapes on an image.

        Args:
            image (ImageData): The image to draw on.
            shapes (Union[Quadrilateral, LineSegment, Contour, Corner, Edge]): The shapes to draw.
            color (int, optional): The color of the shapes. Defaults to 0xFFFF0000 (red).
            thickness (int, optional): The thickness of the lines. Defaults to 1.

        Returns:
            An ImageData object to the modified image data.
        """
        return _DynamsoftUtility.CImageDrawer_DrawOnImage(self, image, shapes, color, thickness)

    __destroy__ = _DynamsoftUtility.delete_CImageDrawer

_DynamsoftUtility.CImageDrawer_register(ImageDrawer)

class ImageProcessor:
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.Class_init(
            self, _DynamsoftUtility.new_CImageProcessor()
        )

    def crop_image(self, image_data:ImageData, crop_form: Union[Rect,Quadrilateral]) -> Tuple[int, ImageData]:
        """
        Crops an image.
        The caller is resposible for freeing the memory allocated for the cropped image.
        The function will automatically calculate the perspective transform matrix and use it to crop the image.

        Args:
            image_data (ImageData): The image data to be cropped.
            crop_form (Union[Rect, Quadrilateral]): The cropping form.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - cropped_image_data (ImageData): An ImageData object representing the cropped image if succeeds, None otherwise.
        """
        if isinstance(crop_form, Rect):
            return _DynamsoftUtility.CImageProcessor_CropImageWithRect(self, image_data, crop_form)
        elif isinstance(crop_form, Quadrilateral):
            import warnings
            warnings.warn(
                "Function 'crop_image' with parameter type `Quadrilateral` is deprecated and will be removed in future versions. Please use `crop_and_deskew_image` function instead.",
                DeprecationWarning,
                stacklevel=2
            )
            return _DynamsoftUtility.CImageProcessor_CropImageWithQuadrilateral(self, image_data, crop_form)
        else:
            raise TypeError("Unsupported crop form type")

    def crop_and_deskew_image(self, image_data: ImageData, crop_form: Quadrilateral, destination_width: int = 0, destination_height: int = 0, padding: int = 0) -> Tuple[int, ImageData]:
        """
        Crops and deskews a region from the input image based on the specified quadrilateral.

        Args:
            image_data (ImageData): The image data to be cropped and deskewed.
            crop_form (Quadrilateral): Quad A quadrilateral defining the region of interest to extract.
            destination_width (int, optional): The width of the output image. If set to 0, the width and height will be automatically calculated.
            destination_height (int, optional): The height of the output image. If set to 0, the width and height will be automatically calculated.
            padding (int, optional): Extra padding (in pixels) applied to expand the boundaries of the extracted region. Default is 0.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - cropped_image_data (ImageData): An ImageData object representing the cropped and deskewed image if succeeds, None otherwise.

        Notes:
            The caller is responsible for freeing the memory allocated for the cropped image.
            The function will automatically calculate the perspective transform matrix and use it to crop the image.
            If the specified quadrilateral exceeds the image boundaries, white will be used to fill the exceeding area.
        """
        return _DynamsoftUtility.CImageProcessor_CropAndDeskewImage(self, image_data, crop_form, destination_width, destination_height, padding)
    def adjust_brightness(self, image_data: ImageData, brightness: int) -> ImageData:
        """
        Adjusts the brightness of the image.

        Args:
            image_data (ImageData): The image data to be adjusted.
            brightness (int): The brightness adjustment value (positive values increase brightness, negative values decrease brightness).

        Returns:
            An ImageData object after brightness adjustment.
        """
        return _DynamsoftUtility.CImageProcessor_AdjustBrightness(self, image_data, brightness)

    def adjust_contrast(self, image_data: ImageData, contrast: int) -> ImageData:
        """
        Adjusts the contrast of the image.

        Args:
            image_data (ImageData): The image data to be adjusted.
            contrast (int): The contrast adjustment value (positive values enhance, negative values reduce contrast).

        Returns:
            An ImageData object after contrast adjustment.
        """
        return _DynamsoftUtility.CImageProcessor_AdjustContrast(self, image_data, contrast)

    def filter_image(self, image_data: ImageData, filter_type: FilterType) -> ImageData:
        """
        Applies a specified image filter to an input image and returns the filtered result.

        Args:
            image_data (ImageData): The image data to be filtered.
            filter_type (FilterType): Specifies the type of filter to apply to the input image.

        Returns:
            An ImageData object after filtering operation.
        """
        return _DynamsoftUtility.CImageProcessor_FilterImage(self, image_data, filter_type)

    def convert_to_gray(self, image_data: ImageData, r: float = 0.3, g: float = 0.59, b: float = 0.11) -> ImageData:
        """
        Converts a colour image to grayscale using the given weights.

        Args:
            image_data (ImageData): The image data to be converted.
            r (float): Weight for red channel (default value: 0.3).
            g (float): Weight for green channel (default value: 0.59).
            b (float): Weight for blue channel (default value: 0.11).

        Returns:
            An ImageData object after grayscale conversion.
        """
        return _DynamsoftUtility.CImageProcessor_ConvertToGray(self, image_data, r, g, b)

    def convert_to_binary_global(self, image_data: ImageData, threshold: int = -1, invert: bool = False) -> ImageData:
        """
        Converts a grayscale image to binary image using a global threshold.

        Args:
            image_data (ImageData): The image data to be converted.
            threshold (int): Global threshold for binarization (default is -1, automatic calculate the threshold).
            invert (bool): If true, invert the binary image (black becomes white and white becomes black).

        Returns:
            An ImageData object after binary conversion.
        """
        return _DynamsoftUtility.CImageProcessor_ConvertToBinaryGlobal(self, image_data, threshold, invert)

    def convert_to_binary_local(self, image_data: ImageData, block_size: int = 0, compensation: int = 10, invert: bool = False) ->ImageData:
        """
        Converts a grayscale image to binary image using local (adaptive) binarization.

        Args:
            image_data (ImageData): The image data to be converted.
            block_size (int): Size of the block for local binarization (default is 0).
            compensation (int): Adjustment value to modify the threshold (default is 10).
            invert (bool): If true, invert the binary image (black becomes white and white becomes black).

        Returns:
            An ImageData object after binary conversion.
        """
        return _DynamsoftUtility.CImageProcessor_ConvertToBinaryLocal(self, image_data, block_size, compensation, invert)
    __destroy__ = _DynamsoftUtility.delete_CImageProcessor


_DynamsoftUtility.CImageProcessor_register(ImageProcessor)
