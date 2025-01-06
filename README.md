# TPC 182 Tools
WIP.

## Data Readers & Writers
- [x] Write `WIBEthFrameReader` class.
  - Extends `DAQHDF5Reader`:
    - WIBEth frame reading (requires `fddetdataformats.WIBEthFrame`).
    - Requires channel mapping (requires `channelmaps.py`).
- [x] Write `HDF5Transcoder` class.
  - Write the contents to a general HDF5 file.
    - Centralizes when the `.bin` files come through the external trigger.
  - Does not require the DUNE DAQ environment to operate.
  - Uses `WIBEthFrameReader` to get the appropriate file contents.
- [x] Write `HDF5Reader` class.
  - Read the contents of a general HDF5 file.
  - Does not require the DUNE DAQ environment to operate.
  - Must give the same result as `WIBEthFrameReader` on the original HDF5 file.
  - _Could this have a better name?_
  - How can a user identify the difference between the data files?
    - Attach an attribute to the general files. If the user tries the DUNE DAQ reader and this attribute is present, raise an exception. Do the inverse for trying the general reader on DUNE DAQ HDF5s.
- [x] Write channel maps.
  - Useful for the DUNE DAQ HDF5 files.
  - Available as global variables in `channelmaps.py`.
  - Needs to feature 3 view 50 L TPC, 2 view 50 L TPC, and 2 view 2T TPC.
    - `50-UVX`,
    - `50-UX`,
    - `2T-UX`.
- [x] Write channel--plane maps.
  - Available as global variable in `channelmaps.py`.

## Data Plotting
It would be useful to have a CLI that plots simple quality checks, such as event displays, FFT, and RMS.
- [ ] Write the CLI interface.
- [ ] Write a configuration parser and base config file.
  - Provide a default `plot_config.toml`.
  - Allow a primary `~/.config/tpc182tools/plot_config.toml`.
  - Allow an optional `<command> -c/--config plot_config.toml`.
  - Allow optional overrides per command, e.g., `<command> --vmin -100`.
