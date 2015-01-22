

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
WOLF_file = os.path.join(directory, 'WOLF.jpg')

# Open and show the student image in a new Figure window
WOLF_img = PIL.Image.open(WOLF_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(WOLF_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(WOLF_img, interpolation='none')
fig.show()

# Open, resize, and display earth
YIN_YANG_file = os.path.join(directory, 'YIN&YANG.png')
YIN_YANG_img = PIL.Image.open(YIN_YANG_file)
earth_small = YIN_YANG_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(YIN_YANG_img)
axes2[1].imshow(earth_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
WOLF_img.paste(earth_small, (50, 50), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(WOLF_img, interpolation='none')
axes3[1].imshow(WOLF_img, interpolation='none')
fig3.show()