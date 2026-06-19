__version__ = "4.0.30.9454"

if __package__ or "." in __name__:
    from . import _DynamsoftLicense
else:
    import _DynamsoftLicense
from typing import Tuple

class LicenseManager:
    """
    The LicenseManager class provides a set of APIs to manage SDK licensing.

    Methods:
        init_license(license: str) -> Tuple[int, str]: Initializes the license using a license key.
        set_device_friendly_name(name: str) -> Tuple[int, str]: Sets the friendly name of the device.
        set_max_concurrent_instance_count(count_for_this_device: int) -> Tuple[int, str]: Sets the maximum number of allowed instances for the given device and process.
        get_device_uuid(uuid_generation_method: int) -> Tuple[int, str, str]: Gets the unique identifier of the device.
        set_license_cache_path(directory_path: str) -> Tuple[int, str]: Sets the directory path for the license cache.
    """
    _thisown = property(
        lambda self: self.this.own(),
        lambda self, value: self.this.own(value),
        doc="The membership flag",
    )

    @staticmethod
    def init_license(license: str) -> Tuple[int, str]:
        """
        Initializes the license using a license key.

        Args:
            license (str): The license key as a string.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftLicense.CLicenseManager_InitLicense(license)

    @staticmethod
    def set_device_friendly_name(name: str) -> Tuple[int, str]:
        """
        Sets the friendly name of the device.

        Args:
            name (str): The friendly name of the device.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftLicense.CLicenseManager_SetDeviceFriendlyName(name)

    @staticmethod
    def set_max_concurrent_instance_count(count_for_this_device: int) -> Tuple[int, str]:
        """
        Sets the maximum number of allowed instances for the given device.

        Args:
            count_for_this_device (int): The maximum number of allowed instances for the device.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftLicense.CLicenseManager_SetMaxConcurrentInstanceCount(
            count_for_this_device
        )

    @staticmethod
    def get_device_uuid(uuid_generation_method: int) -> Tuple[int, str, str]:
        """
        Gets the unique identifier of the device.

        Args:
            uuid_generation_method (int): The method to generate the UUID.
            - 1: Generates UUID with random values.
            - 2: Generates UUID based on hardware info.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
            - uuid <str>: The unique identifier of the device.
        """
        return _DynamsoftLicense.CLicenseManager_GetDeviceUUID(uuid_generation_method)

    @staticmethod
    def set_license_cache_path(directory_path: str) -> Tuple[int, str]:
        """
        Sets the directory path for the license cache.

        Args:
            directory_path (str): The directory path for the license cache.

        Returns:
            A tuple containing following elements:
            - error_code (int): The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftLicense.CLicenseManager_SetLicenseCachePath(directory_path)

    def __init__(self):
        _DynamsoftLicense.Class_init(
            self, _DynamsoftLicense.new_CLicenseManager()
        )

    __destroy__ = _DynamsoftLicense.delete_CLicenseManager


_DynamsoftLicense.CLicenseManager_register(LicenseManager)


class LicenseModule:
    """
    The LicenseModule class represents the Dynamsoft License module.

    Methods:
        get_version() -> str: Gets the version of the Dynamsoft License module.
    """
    _thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Gets the version of the Dynamsoft License module.

        Returns:
            A string representing the version of the Dynamsoft License module.
        """
        return __version__ + " (Algorithm " + _DynamsoftLicense.CLicenseModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftLicense.Class_init(
            self, _DynamsoftLicense.new_CLicenseModule()
        )

    __destroy__ = _DynamsoftLicense.delete_CLicenseModule


_DynamsoftLicense.CLicenseModule_register(LicenseModule)
