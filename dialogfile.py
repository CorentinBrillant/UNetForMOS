import tkinter.filedialog as fd

image = fd.askopenfilename(initialdir='./images')

image = image.split("/")[-1]
print(image)