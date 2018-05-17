#!/usr/bin/env python

"""This is a python script for gimp that enhances the color in a photo"""

import math
from gimpfu import *

def python_color_enhance(img,drawable,blur_rad,opacity):
    

    layer = img.active_layer
    
    #duplicate the layer twice
    layer2 = pdb.gimp_layer_copy(layer,FALSE)
    pdb.gimp_image_add_layer(img,layer2,0)  #need to add to image. 
    layer3 = pdb.gimp_layer_copy(layer,FALSE)
    pdb.gimp_image_add_layer(img,layer3,0)
    pdb.gimp_image_set_active_layer(img,layer3)
    #top layer desaturate luminosity
    pdb.gimp_desaturate_full(layer3,1)  #type 1 is luminosity
    #invert
    pdb.gimp_invert(layer3)
    #gaussian blur. Using iir instead of rle (better for non-CG images)
    pdb.plug_in_gauss_iir(img, layer3, blur_rad, 1, 1)
    #opacity 30%...or user selectable 
    pdb.gimp_layer_set_opacity(layer3,opacity)
    #merge down
    layer_merge = pdb.gimp_image_merge_down(img,layer3,1)
    #blend mode grain merge
    pdb.gimp_layer_set_mode(layer_merge,21)       
    pdb.gimp_layer_set_opacity(layer_merge,50)
    #img.flatten()  #turn off if want to compare
    
    gimp.delete(img)

register(
        "python-color-enhance",
        "Color enhancement script for photographs",
        "Color enhancement script for photographs",
        "Jon Blanchard",
        "Jon Blanchard",
        "2018",
        "<Image>/Filters/Enhance/_Color Enhance...",
        "RGB*, GRAY*",
        [
#                (PF_IMAGE, "image",       "Input image", None),
#                (PF_DRAWABLE, "drawable", "Input drawable", None),
                (PF_INT, "blur_rad", "Blur Radius", 20),
                (PF_INT, "opacity", "Opacity", 30),
#                (PF_INT, "elevation", "Elevation", 45),
#                (PF_INT, "depth", "Depth", 3)
        ],
        [],
        python_color_enhance)

main()