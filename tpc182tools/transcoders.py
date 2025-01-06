"""
Data transcoders from the original DUNE DAQ HDF5 format.
"""

__all__ = ["HDF5Transcoder"]

# TPC 182 Tools
from .readers import WIBEthFrameReader as _WIBEthFrameReader

# Third-party Modules
import h5py as _h5py
import numpy as _np
from numpy.typing import NDArray as _NDArray

# In-built Modules
import os as _os


class HDF5Transcoder(_WIBEthFrameReader):
    """
    This class transcodes a given DUNE DAQ HDF5 file to a more general
    HDF5 format. This comes with the cost of some additional padding
    per trigger record, but lightens by reducing some of the data
    fragment and trigger fragment preservations.
    """

    def __init__(self, filename: str, map_name: str = "2T-UX") -> None:
        """
        Load the given data file in :filename: and set some preliminary attributes.

        Parameter:
            filename (str) : Path of data file to process.
            map_name (str) : Channel map to use when reading. Defaults to latest map available.
        """
        # Initialize the base reader.
        super().__init__(filename, map_name)

        # Prepare the transcode file.
        full_path: str = _os.path.expanduser(filename)
        base_path: str = _os.path.dirname(full_path)
        transcode_name: str = f"182enc_{self.run_id:06}-{self.file_index:06}_{self.creation_timestamp}.hdf5"
        self._transcode_path: str = _os.path.join(base_path, transcode_name)
        self._transcode_file: _h5py.File = _h5py.File(self._transcode_path, mode='x')

        # Make the transcode file identifiable at the top level.
        self._transcode_file.attrs['tpc182tools'] = True
        self._transcode_file.attrs['creation_timestamp'] = self.creation_timestamp
        self._transcode_file.attrs['run_id'] = self.run_id
        self._transcode_file.attrs['file_index'] = self.file_index
        return

    def transcode_record(self, record: tuple[int, int]) -> None:
        """
        Transcode the given record.

        Parameter:
            record (tuple[int, int]) : Record identifier.
        """
        # Module that only gets used here. Allows for optional dependencies.
        from daqdataformats import Fragment  # Required to get the fragment timestamp.

        # Get the record contents.
        adcs: _NDArray[_np.int_] = self.read_record(record)

        # Get the TriggerRecordHeader at its 0th component and save its window start time.
        # All components should have the same window_begin value.
        window_begin: int = self._h5_file.get_trh(record).at(0).window_begin

        # Transcode and save some metadata.
        record_number: int = record[0]  # Only first value is the record number.
        dset: _h5py.Dataset = self._transcode_file.create_dataset(f"Record{record_number:04}",
                                                                  data=adcs.astype(_np.uint16),
                                                                  compression='gzip',
                                                                  compression_opts=9)
        dset.attrs['record_number'] = record_number
        dset.attrs['timestamp'] = window_begin
        return

    def transcode_file(self) -> None:
        """
        Transcode the initialized data file.
        """
        for record in self.records:
            self.transcode_record(record)
        return
