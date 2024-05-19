# pyflagoras
🏳️‍🌈 A Python command line interface tool to generate pride flags from images.

https://github.com/phthallo/pyflagoras/assets/84078890/5440a9d3-2c49-4200-a52a-f4896956ece0

## Installation 
You can install this package from [pypi.org](https://pypi.org)! Open a terminal and run the following:
```python
pip install pyflagoras
```

## Development
Substitute `py` for `python3` as necessary.
1. Clone the repository.
    ```python
    git clone https://github.com/phthallo/pyflagoras
    ```
2. Install the build tool.
    ```python
    py -m pip install --upgrade build
    ```
3. `cd` to the root of the repository and build the package.
    ```python
    py -m build
    ```
4. Both the source distribution (`pyflagoras-x.x.x-tar.gz`) and the built distribution (`pyflagoras-x.x.x-py3-none-any.whl`) will be found under the `/dist` subdirectory. You can then install the wheel using:
    ```python
    py -m pip install dist/pyflagoras-x.x.x-py3-none-any.whl
    ```

## Adding other flags 
The current pride flags are sourced from @/JoeHart's [Pride Flag API](https://github.com/JoeHart/pride-flag-api). 

To add a new flag, open a pull request with the file name `<flag_name>_<year_of_release>.json`. Make sure this `.json` file follows the format of the other flags under `/src/pyflagoras/flags`

## Notes
- The name `pyflagoras` comes from **py**thon, pride **flag**, and the basic colour similarity algorithm being a 3D application of Pythagoras' theorem. 
- See also the [prideflagbot](https://twitter.com/prideflagbot) account (gone but not forgotten!) run by @/michalpazur, which was a big inspiration for this project.

