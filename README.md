# gimp-plug-ins
<h3>Plug-ins for GIMP</h3>

<h4>1. python-color-enhance.py</h4>

Python script to enhance colors in images.  It consists of the following steps:

  1. Duplicate layer twice.
  2. Desaturate top layer based in luminosity.
  3. Invert colors
  4. Gaussian blur - user defined radius (default = 20)
  5. Reduce top layer opacity - user defined, default = 30%
  6. Merge down.
  7. Set top layer to 50% opacity
  

The final merge down in not performed to allow for a final opacity tweak to the upper layer before merging down.


