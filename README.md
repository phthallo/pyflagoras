# pyflagoras
🏳️‍🌈 A Python command line interface tool for generating pride flags from images. The program accepts any image file and outputs the flag as a `.png` file.

https://github.com/phthallo/pyflagoras/assets/84078890/0d26fe83-374d-45ce-bb8d-ba5be970bd4a

## How does it work?
Pyflagoras, at a minimum, needs the name of a pride flag and a path to an image to work.

It uses [Pillow](https://pillow.readthedocs.io/en/stable/) to generate a list of colours in the image.

The program then obtains the flag's `.svg` file from the alias used, and extracts the all the colours used in the flag. It uses an [algorithm](https://github.com/phthallo/pyflagoras/blob/main/src/pyflagoras/similarity_algorithms.py#L2) to calculate which colours are the most similar based on their RGB codes. 

Finally, the colours are swapped out. The `.svg` is converted into a `.pdf` using [svglib](https://github.com/deeplook/svglib) then into a `.png` using [PyMuPDF](https://github.com/pymupdf/PyMuPDF).

## Installation 
You can install this package from [pypi.org](https://pypi.org)! Open a terminal and run the following:
```
pip install pyflagoras
```

## Usage
```
$ pyflagoras --help
usage: pyflagoras [-h] [-f FLAG] [-n NAME] [--verbose] [--svg] [--version] [-l] image

A command line interface tool for generating pride flags from images.

positional arguments:
  image                 Path to the image to generate a flag from.
                        Examples:
                            image.png
                            foo/bar/image.jpg

options:
  -h, --help            show this help message and exit
  -f FLAG, --flag FLAG  The alias of the flag to generate.
                        Examples:
                            intersexinclusive
                            nonbinary
                        Default:
                            progresspride
  -n NAME, --name NAME  Customise the name of the final .png. The following can be used as part of the file name:
                        Format placeholders:
                            {n}: File name (e.g celeste_classic)
                            {N}: File name (full) (e.g celeste_classic.png)
                            {f}: Flag name (e.g Progress Pride)
                            {F}: Flag ID (e.g progressPride_2018)
                        Examples:
                            pyflagoras celeste_classic.png -n "{f}_{n}" [renders Progress Pride_celeste_classic.png]       
                        Default:
                            {n}_{F} [renders celeste_classic_progressPride_2018.png]

  --verbose             Enable verbosity (for general info and debugging)
  --svg                 Generate the flag's .svg file in addition to the .png
  --version             show the program's version number and exit
  -l, --list            show all flag aliases and exit

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

## Contributions 
The current pride flags have been sourced from @/JoeHart's [Pride Flag API](https://github.com/JoeHart/pride-flag-api). 

To add a new flag, see [addingflags.md](/addingflags.md). 

## Notes
- The name `pyflagoras` comes from **py**thon, pride **flag**, and the basic colour similarity algorithm being a 3D application of Pythagoras' theorem. 
- See also the [prideflagbot](https://twitter.com/prideflagbot) account (gone but not forgotten!) run by @/michalpazur, which was a big inspiration for this project.

