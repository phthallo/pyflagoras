from .pyflagoras import Pyflagoras 
from pyflagoras import __version__, __list__
import argparse
import logging

parser = argparse.ArgumentParser(
                    prog='pyflagoras',
                    description='A command line interface tool for theming .svg files using user-provided images.',
                    epilog="Documentation, issues and more: https://github.com/phthallo/pyflagoras",
                    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument(
    'image', 
    help='''Path to the image to generate a flag from.
Examples:
    image.png
    foo/bar/image.jpg''',
    type=str
) 

parser.add_argument(
    '-f', 
    '--flag',
    default="progresspride",
    help=
    '''The alias of the flag to generate OR path to a custom .svg file.
Examples:
    intersexinclusive
    /foo/bar/file.svg
Default:
    progresspride''',
    type=str
) 

parser.add_argument(
    '-o',
    '--output',
    default="{n}_{F}",
    help=
    '''Customise the name of the final .png. The following can be used as part of the file name: 
Format placeholders:
    {n}: File name (e.g celeste_classic)
    {N}: File name (full) (e.g celeste_classic.png) 
    {f}: Flag name (e.g Progress Pride) [N/A for custom .svg]
    {F}: Flag ID (e.g progressPride_2018) [N/A for custom .svg]
Examples:
    pyflagoras celeste_classic.png -n "{f}_{n}" [renders Progress Pride_celeste_classic.png]
Default:
    {n}_{F} [renders celeste_classic_progressPride_2018.png]
    '''
)

parser.add_argument('-a',
                    '--algorithm',
                    default="cielab",
                    choices=["low_cost", "pythagoras", "cielab"],
                    help="Change the algorithm used to determine colour similarity.")

parser.add_argument('--verbose', 
                    action="store_const",
                    help="Enable verbosity (for general info and debugging)",
                    const=logging.INFO)

parser.add_argument('--svg', 
                    action="store_true",
                    help="Generate the flag's .svg file in addition to the .png")

parser.add_argument('--highlight', 
                    action="store_true",
                    help="Generate an image to highlight where the similar colours were found.")

parser.add_argument('--version', action='version',
                    version=__version__, help="show the program's version number and exit")

parser.add_argument('-l',
                    '--list',
                    action='version',
                    version=__list__,
                    help='show all flag aliases and exit')

def main() -> None:
    args = parser.parse_args()
    pyflag = Pyflagoras(
        image=args.image, # The image to source the resultant file's colours from.
        flag=args.flag, # .svg to use as a 'template' 
        output=args.output, # The file name of the resultant file.
        algorithm=args.algorithm, # Algorithm to use when determining similarity.
        svg=args.svg, # Enable saving of the .svg (intemediary step) of the resultant file, or go straight to rendering .png.
        verbose = args.verbose, # Enable logging for debugging.
        highlight = args.highlight # Enable generation of another image showing locations of similar colours
    )
    logging.basicConfig(level=args.verbose, format="🏳️‍🌈\033[38;5;173m%(funcName)17s()\033[0m %(message)s")

    pyflag.run()

if __name__ == "__main__":
    main()
