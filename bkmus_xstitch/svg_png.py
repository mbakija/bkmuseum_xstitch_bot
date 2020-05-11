# convert SVG file to PNG file

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# insert SVG file and filename for PNG file
art = svg2rlg("YOUR_SVG_FILE_GOES_HERE.svg")
renderPM.drawToFile(art, "YOUR_PNG_FILENAME_GOES_HERE.png", fmt="PNG")
