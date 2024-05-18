from pyflagoras.pyflagoras import Pyflagoras

import argparse
parser = argparse.ArgumentParser(
                    prog='pyflagoras',
                    description='Generates pride flags colourpicked from images')

parser.add_argument(
    'image', 
    help='Path to the image to generate a flag from',
    type=str
) 

parser.add_argument(
    'flag', 
    help='Pride flag to generate',
    default='progressPride_2018',
    type=str
) 

def main() -> None:
    args = parser.parse_args()
    pyflag = Pyflagoras(
        image=args.image,
        flag=args.flag
    )
    pyflag.run()

if __name__ == "__main__":
    main()
