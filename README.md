# TPC 182 Tools

A general package for processing data generated from TPCs in CERN B182.

This package provides:
* DUNE-DAQ HDF5 file reading (must be in a DUNE-DAQ environment),
  * Transcoding these files into a self-contained format,
* Reading `tpc182tools` HDF5 format files.

It does not provide analysis procedures or algorithms that one may want to apply to the data that was read. It is currently expected that the user understands the returned contents and may manipulate how they wish.

## File Formats
### DUNE-DAQ
The TPCs in 182 have so far been generating data files using the DUNE-DAQ system. This comes with a proprietary format that requires being in a DUNE-DAQ environment to be able to reasonably read these files. This package provides a bare-bones way of reading and reformatting (apply channel maps and other utilities) the data available in these files. These data files may be read by using `tpc182tools.readers.WIBEthFrameReader`.

### `tpc182tools` HDF5
To avoid the DUNE-DAQ environment requirement, this package also provides a centralized transcoder `tpc182tools.transcoders.HDF5Transcoder`. This reads and transcodes the data into an HDF5 format that does not require the DUNE-DAQ environment while preserving all the data from the `WIBEthFrame`s.

These data files can be read using `tpc182tools.readers.HDF5Reader` with many of the same methods as the `WIBEthFrameReader`. Since generating the transcoded files does not make use of any proprietary data format, these HDF5 files may be read by any file reader. If a user has access to a transcoded data file, they may use ROOT, C++, etc. with the appropriate h5 library to read the data in their preferred way.

These files **do not** feature the DUNE-DAQ trigger data (`TriggerPrimitive`, `TriggerActivity`, `TriggerCandidate`). These data structures are seen as niche and proprietary to the DUNE-DAQ environment, so these were left out (though, they may be added later).
