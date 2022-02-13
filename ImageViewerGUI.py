####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_visualization
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
from PIL import Image

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import Tk, filedialog, Entry, Button, StringVar, Toplevel, Label
from tkinter.ttk import Combobox
from functools import partial
from PIL import ImageTk
import numpy as np


# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):

	####### CODE REQUIRED (START) #######
	# This function should pop-up a dialog for the user to select an input image file.
	# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
	# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
	# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
	# To have a better clarity, please check out the sample video.

	global img
	try:
		img = Image.open(filedialog.askopenfilename(defaultextension=".jpg", filetypes=[("All image files", "*.jpg *.jpeg *.png"), ("JPG image", "*.jpg"), ("PNG annotation", "*.png")], initialdir="./data/imgs", title="Select Image"))
	except IOError:
		status['text'] = "File not read! Please retry."
		return
	src = np.asarray(img).transpose((2, 0, 1))/255
	pred_boxes, pred_masks, pred_class, pred_score = segmentor(src)
	plot_visualization(src, pred_masks[:3], pred_boxes[:3], pred_class[:3], './output/')
	print("Image uploaded! You can process now.")
	status['text'] = "Image uploaded! You can process now."

	####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):

	####### CODE REQUIRED (START) #######
	# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
	# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
	# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.

	try:
		img
	except:
		print("File not selected! Choose an image to process")
		status['text'] = "Image not uploaded! Please upload an image first."
		return
	else:
		file = {"Segmentation":'masked_result', "Bounding-box":'bbox_result', "Segmentation + Bounding-box":'complete'}
		panel = Toplevel(root)
		panel.title("Image for comparison")
		global img1, img2
		img1 = ImageTk.PhotoImage(img)
		img2 = ImageTk.PhotoImage(Image.open('./output/'+file[clicked.get()]+'.jpg'))
		p1 = Label(panel, image= img1)
		p1.grid(row=0, column=0)
		p2 = Label(panel, image= img2)
		p2.grid(row=0, column=2)

	####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':

	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.
	
	root = Tk()
	root.title("Image identifier model")
	status = Label(root, pady=5,text='Status will be displayed here')
	status.grid(row=1, column=0, columnspan=4)

	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model.
	annotation_file = './data/annotations.jsonl'
	transforms = []

	# Instantiate the segmentor model.
	segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
	dataset = Dataset(annotation_file, transforms=transforms)
	
	# Declare the options.
	options = ["Segmentation", "Bounding-box", "Segmentation + Bounding-box"]
	clicked = StringVar()
	clicked.set(options[2])

	e = Entry(root, width=70, state='disabled')
	e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
	source = Button(root, text= "Choose image", command= lambda: fileClick(clicked, dataset, segmentor))
	source.grid(row=0, column=1)
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
	list = Combobox(root, textvariable= clicked, state= 'readonly', values= options, width=30).grid(row=0, column=2)
	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality
	myButton = Button(root, text="Process", command=partial(process, clicked))
	myButton.grid(row=0, column=3)
	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
	root.mainloop()
	####### CODE REQUIRED (END) #######