# pyflagoras
🏳️‍🌈 A Python command line interface tool to generate pride flags from images.

https://github.com/phthallo/pyflagoras/assets/84078890/5440a9d3-2c49-4200-a52a-f4896956ece0

## Installation 
You can install this package from [pypi.org](https://pypi.org)! Open a terminal and run the following:
```
pip install pyflagoras
```

## Usage
```
$ pyflagoras --help
usage: pyflagoras [-h] [-f FLAG] [-n NAME] [--verbose] [--version] [-l] image

A command line interface tool to generate pride flags from images.

positional arguments:
  image                 Path to the image to generate a flag from.
                        Examples:
                            image.png
                            foo/bar/image.jpg

options:
  -h, --help            show this help message and exit
  -f FLAG, --flag FLAG  The ID (<flag_name>_<year_of_release>) of the flag to generate.
                        Examples:
                            intersexInclusive_2021
                            nonbinary_2014
                        Default:
                            progressPride_2018
  -n NAME, --name NAME  Customise the name of the final .svg. The following can be used as part of the file name:
                        Format placeholders:
                            {n}: File name (e.g celeste_classic)
                            {N}: File name (full) (e.g celeste_classic.png)
                            {f}: Flag name (e.g Progress Pride)
                            {F}: Flag ID (e.g progressPride_2018)
                        Examples:
                            pyflagoras celeste_classic.png -n "{f}_{n}" [renders Progress Pride_celeste_classic.svg]
                        Default:
                            {n}_{F} [renders celeste_classic_progressPride_2018.svg]

  --verbose             Enable verbosity (for general info and debugging)
  --version             show the program's version number and exit
  -l, --list            show all flag ids and exit

Documentation, issues and more: https://github.com/phthallo/pyflagoras
```

## Development
Substitute `py` for `python3` as necessary.
1. Clone the repository.
    ```
    git clone https://github.com/phthallo/pyflagoras
    ```
2. Install the build tool.
    ```
    py -m pip install --upgrade build
    ```
3. `cd` to the root of the repository and build the package.
    ```
    py -m build
    ```
4. Both the source distribution (`pyflagoras-x.x.x-tar.gz`) and the built distribution (`pyflagoras-x.x.x-py3-none-any.whl`) will be found under the `/dist` subdirectory. You can then install the wheel using:
    ```bash
    py -m pip install dist/pyflagoras-x.x.x-py3-none-any.whl
    ```

## Adding other flags 
The current pride flags are sourced from @/JoeHart's [Pride Flag API](https://github.com/JoeHart/pride-flag-api). 

To add a new flag, open a pull request with the file name `<flag_name>_<year_of_release>.json`. Make sure this `.json` file follows the format of the other flags under `/src/pyflagoras/flags`. At the very least, the file must contain the flag's name, its ID, and the flag in `.svg` format.  

## Notes
- The name `pyflagoras` comes from **py**thon, pride **flag**, and the basic colour similarity algorithm being a 3D application of Pythagoras' theorem. 
- See also the [prideflagbot](https://twitter.com/prideflagbot) account (gone but not forgotten!) run by @/michalpazur, which was a big inspiration for this project.

