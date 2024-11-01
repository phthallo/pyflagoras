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
    """Calculates the similarity of two colours in RGB format by positioning them as points in 3D space, then finding the Euclidian distance.
    
    Arguments:
    rgb1 (tuple[int]): The first RGB value.
    rgb2 (tuple[int]): The second RGB value.
    """
    return (rgb1, 
            rgb2, 
            math.sqrt((rgb2[0]-rgb1[0])**2+(rgb2[1]-rgb1[1])**2+(rgb2[2]-rgb1[2])**2))

# Cielab conversions from this point on!
# Calculates the similarity of two colours in RGB format by converting to the CIELAB colour space
# Helpful resource: http://www.easyrgb.com/en/math.php 

def __xyzconverted(rgb: tuple[int]) -> tuple[float]:
    """Converts RGB colours to the D65/2° illuminant standard. 
    
    Arguments:
    rgb (tuple[int]): A standard RGB colour tuple.
    """
    var_r = ( rgb[0] / 255 )
    var_g = ( rgb[1] / 255 )
    var_b = ( rgb[2] / 255 )

    if ( var_r > 0.04045 ):
        var_r = ( ( var_r + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_r = var_r / 12.92
    if ( var_g > 0.04045 ):
        var_g = ( ( var_g + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_g = var_g / 12.92
    if ( var_b > 0.04045 ):
        var_b = ( ( var_b + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_b = var_b / 12.92

    var_r = var_r * 100
    var_g = var_g * 100
    var_b = var_b * 100

    x = var_r * 0.4124 + var_g * 0.3576 + var_b * 0.1805
    y = var_r * 0.2126 + var_g * 0.7152 + var_b * 0.0722
    z = var_r * 0.0193 + var_g * 0.1192 + var_b * 0.9505
    return (x, y, z)

def __cieconverted(xyz: tuple[float]) -> tuple[float]:
    """Converts D65/2° illuminant standard colours to the CIEL*a*b* device agnostic colour space.
    
    Arguments:
    xyz (tuple[float]): A D65/2° illuminant standard tuple.
    """
    var_X = xyz[0] / 94.811
    var_Y = xyz[1] / 100.000
    var_Z = xyz[2] / 107.304

    if ( var_X > 0.008856 ):
        var_X = var_X ** ( 1/3 )
    else:
        var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ):
        var_Y = var_Y ** ( 1/3 )
    else:
        var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ):
        var_Z = var_Z ** ( 1/3 )
    else:
        var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    cie_l = ( 116 * var_Y ) - 16
    cie_a = 500 * ( var_X - var_Y )
    cie_b = 200 * ( var_Y - var_Z )
    return (cie_l, cie_a, cie_b)

def _cielab(rgb1: tuple[float], rgb2: tuple[float]) -> tuple: 
    """
    Alternative way of determining colour similarity, via converting into a different colour space 
    (as opposed to weighting certain main colours less or more.)
    """
    lab1, lab2 = __cieconverted(__xyzconverted(rgb1)), __cieconverted(__xyzconverted(rgb2))
    return (rgb1, 
            rgb2, 
            math.sqrt((lab2[0]-lab1[0])**2+(lab2[1]-lab1[1])**2+(lab2[2]-lab1[2])**2))

