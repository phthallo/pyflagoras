# pyflagoras
🏳️‍🌈 A Python command line interface tool for theming `.svg` files using user-provided images. The program accepts any image file, an `.svg` file and outputs the flag as a `.png` file.

https://github.com/phthallo/pyflagoras/assets/84078890/8927779e-5e1c-411e-9d14-6bf1bdb8396d

(To see more examples of flags generated using this program, visit [examples.md](/examples.md)!)

## How does it work?
Pyflagoras, at a minimum, needs the name of a pride flag, or a path to an `.svg`, and a path to an image to work.

It uses [Pillow](https://pillow.readthedocs.io/en/stable/) to generate a list of colours in the image.

The program then obtains the flag's `.svg` file from the alias used, and extracts the all the colours used in the flag. It uses an [algorithm](https://github.com/phthallo/pyflagoras/blob/main/src/pyflagoras/similarity_algorithms.py#L2) to calculate which colours are the most similar based on their RGB codes. 

Finally, the colours are swapped out. The `.svg` is converted into a `.pdf` using [svglib](https://github.com/deeplook/svglib) then into a `.png` using [PyMuPDF](https://github.com/pymupdf/PyMuPDF).

tl;dr - if you ever wanted the Slack logo to have the same colours as a cool photo you took you absolutely can. 

## Installation 
You can install this package from [pypi.org](https://pypi.org)! Open a terminal and run the following:
```
pip install pyflagoras
```

## Usage
```
$ pyflagoras --help
usage: pyflagoras [-h] [-f FLAG] [-n NAME] [-a {low_cost,pythagoras,cielab}] [--verbose] [--svg]
                  [--highlight] [--version] [-l]
                  image

A command line interface tool for theming .svg files using user-provided images.

positional arguments:
  image                 Path to the image to generate a flag from.
                        Examples:
                            image.png
                            foo/bar/image.jpg

options:
  -h, --help            show this help message and exit
  -f FLAG, --flag FLAG  The alias of the flag to generate OR path to a custom .svg file.
                        Examples:
                            intersexinclusive
                            /foo/bar/file.svg
                        Default:
                            progresspride
  -o OUTPUT, --output OUTPUT  
                        Customise the name of the final .png. The following can be used as part of the file name:
                        Format placeholders:
                            {n}: File name (e.g celeste_classic)
                            {N}: File name (full) (e.g celeste_classic.png)
                            {f}: Flag name (e.g Progress Pride) [N/A for custom .svg]
                            {F}: Flag ID (e.g progressPride_2018) [N/A for custom .svg]
                        Examples:
                            pyflagoras celeste_classic.png -n "{f}_{n}" [renders Progress Pride_celeste_classic.png]
                        Default:
                            {n}_{F} [renders celeste_classic_progressPride_2018.png]

  -a {low_cost,pythagoras,cielab}, --algorithm {low_cost,pythagoras,cielab}
                        Change the algorithm used to determine colour similarity.
  --verbose             Enable verbosity (for general info and debugging)
  --svg                 Generate the flag's .svg file in addition to the .png
  --highlight           Generate an image to highlight where the similar colours were found.
  --version             show the program's version number and exit
  -l, --list            show all flag aliases and exit
```

Tip: 
> [!TIP]
> - Using `--verbose` will log the coordinates of where the colours were found on your image!
> - in terms of colour similarity, `cielab` and `low_cost` produce the best results. 

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
5. To preview your changes without having to build, run the following to install Pyflagoras in editable mode.
    ```bash 
    py -m pip install -e .
    ```

## Contributions 
The current 'pre-loaded' `.svg` files are pride flags! They have been sourced from @/JoeHart's [Pride Flag API](https://github.com/JoeHart/pride-flag-api). 

To add a new flag, see [addingflags.md](/addingflags.md).


## Notes
- The name `pyflagoras` comes from **py**thon, pride **flag**, and the basic colour similarity algorithm being a 3D application of Pythagoras' theorem. 
- See also the [prideflagbot](https://twitter.com/prideflagbot) account (gone but not forgotten!) run by @/michalpazur, which was a big inspiration for this project.

