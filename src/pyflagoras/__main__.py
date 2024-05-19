from .pyflagoras import Pyflagoras 
from pyflagoras import __version__ 
import argparse

parser = argparse.ArgumentParser(
                    prog='pyflagoras',
                    description='A command line interface tool to generate pride flags from images.',
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
    default="progressPride_2018",
    help=
    '''The ID (<flag_name>_<year_of_release>) of the flag to generate.
Examples:
    intersexInclusive_2021
    nonbinary_2014
Default:
    progressPride_2018\nSee https://github.com/phthallo/pyflagoras/blob/main/dev/flag_list.txt for a complete list of flag IDs.''',
    type=str
) 

parser.add_argument(
    '-n',
    '--name',
    default="{n}_{F}",
    help=
    '''Customise the name of the final .svg. The following can be used as part of the file name: 
Format placeholders:
    {n}: File name (e.g celeste_classic)
    {N}: File name (full) (e.g celeste_classic.png) 
    {f}: Flag name (e.g Progress Pride)
    {F}: Flag ID (e.g progressPride_2018)
Examples:
    pyflagoras celeste_classic.png -n "{f}_{n}" [renders Progress Pride_celeste_classic.svg]
Default:
    {n}_{F} [renders celeste_classic_progressPride_2018.svg]
    '''
)

parser.add_argument('-v', '--version', action='version',
                    version=__version__, help="show the program's version number and exit")

def main() -> None:
    args = parser.parse_args()
    pyflag = Pyflagoras(
        image=args.image,
        flag=args.flag,
        output=args.output
    )
    pyflag.run()

if __name__ == "__main__":
    main()
