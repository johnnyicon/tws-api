# TWS API

This contains copies of the TWS API packages that are available for download from Interactive Brokers.  The TWS API is used to connect to the TWS trading platform and submit orders.  The TWS API is also used to retrieve market data.  The TWS API is written in Java and is available for download from Interactive Brokers.  The TWS API is also available for download from GitHub: https://interactivebrokers.github.io/

They've been cloned to make it easier for other projects to include them as dependencies.

# Installation

To install the TWS API, run the following command from the root of this project:

1. Create an environment (e.g., `conda create -n twsapi python=3.9`)
2. Activate the environment (e.g., `conda activate twsapi`)
3. Install the TWS API in development mode (e.g., `pip install -e .` - the `-e` flag installs in editable mode)

## Uninstall existing ibapi from pypi

The version of TWS API (9.81.0) on pypi.org is deprecated and no longer supported by Interactive Brokers.  To uninstall the existing ibapi, run the following command:

```bash
pip uninstall ibapi
```

If you have a conda environment, you can uninstall the existing ibapi by running the following command:

```bash
conda remove ibapi
```

# Usage

For usage examples and documentation, refer to the [Interactive Brokers TWS API documentation](https://interactivebrokers.github.io/).
