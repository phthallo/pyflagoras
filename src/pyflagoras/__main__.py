from .pyflagoras import Pyflagoras 
from pyflagoras import __version__, __list__
import argparse
import logging

parser = argparse.ArgumentParser(
                    prog='pyflagoras',
                    description='A command line interface tool for generating pride flags from images.',
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
    '''The alias of the flag to generate.
Examples:
    intersexinclusive
    nonbinary
Default:
    progresspride''',
    type=str
) 

parser.add_argument(
    '-n',
    '--name',
    default="{n}_{F}",
    help=
    '''Customise the name of the final .png. The following can be used as part of the file name: 
Format placeholders:
    {n}: File name (e.g celeste_classic)
    {N}: File name (full) (e.g celeste_classic.png) 
    {f}: Flag name (e.g Progress Pride)
    {F}: Flag ID (e.g progressPride_2018)
Examples:
    pyflagoras celeste_classic.png -n "{f}_{n}" [renders Progress Pride_celeste_classic.png]
Default:
    {n}_{F} [renders celeste_classic_progressPride_2018.png]
    '''
)

parser.add_argument('--verbose', 
                    action="store_const",
                    help="Enable verbosity (for general info and debugging)",
                    const=logging.INFO)

parser.add_argument('--svg', 
                    action="store_true",
                    help="Generate the flag's .svg file in addition to the .png")

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
        image=args.image,
        flag=args.flag,
        name=args.name,
        svg=args.svg,
    )
    logging.basicConfig(level=args.verbose, format="🏳️‍🌈%(funcName)17s() %(message)s")

    pyflag.run()

if __name__ == "__main__":
    main()
