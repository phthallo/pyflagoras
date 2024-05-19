import math
def _low_cost(rgb1: tuple[int], rgb2: tuple[int]) -> tuple:
    """
    Calculates the similarity of two colours in RGB format using the low-cost approximation here: https://www.compuphase.com/cmetric.htm
    See the note at the top of the linked page describing about how the human eye interprets colours makes this somewhat difficult.
    A lower distance value means a more similar colour; a higher distance value means a more dissimilar colour.

    Arguments:
    rgb1 (tuple[int]): The first RGB value.
    rgb2 (tuple[int]): The second RGB value.
    """
    mean_red = (rgb1[0]+rgb2[0])/2
    range_red = rgb1[0]-rgb2[0]
    range_green = rgb1[1]-rgb2[1]
    range_blue = rgb1[2]-rgb2[2]
    return (rgb1, 
            rgb2,
            math.sqrt((2+ mean_red/256) * (range_red)**2 + 4 * (range_green)**2 + (2 + (255-mean_red)/256) * (range_blue)**2)
    )


def _pythagoras(rgb1: tuple[int], rgb2: tuple[int]) -> tuple:
    """Calculates the similarity of two colours in RGB format by positioning them as points on a 3D vector plane, then finding the Euclidian distance.
    
    Arguments:
    rgb1 (tuple[int]): The first RGB value.
    rgb2 (tuple[int]): The second RGB value.
    """
    return (rgb1, 
            rgb2, 
            math.sqrt((rgb2[0]-rgb1[0])**2+(rgb2[1]-rgb1[1])**2+(rgb2[2]-rgb1[2])**2))

def _weighted(rgb1: tuple[int], rgb2: tuple[int]) -> list[tuple]: 
    """Calculates the similarity of two colours in RGB format by """
    pass