# UNetForMOS

## Description

This project allows you to easily label pictures to train deep learning segmentation models. In this project the model implemented is UNet.

## Quick installation

To install required dependencies please enter the following command in the root folder of the project
```
pip install -r requirements.txt
```

## Manual

Launch the Interface from the root folder with the following command : 

```
python ./PolyInterfaceUpdate.py
```

### First Step : Choose the image you want to label
![](assets/images/1_step.png)
### Second Step : Load a pre-existing polygon layer with the image
![](assets/images/2_step.png)
### Third Step : Choose your class number by sliding the below horizontal bar and draw polygons
![](assets/images/3_step.png)
### Fourth Step : Choose a folder to save the new ploygon layer
![](assets/images/4_step.png)
### Fiveth Step : Choose a folder to export the mask of this layer
![](assets/images/5_step.png)
