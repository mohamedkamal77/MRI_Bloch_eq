
| Programming task |                             #1                              |
| :--------------: | :----------------------------------------------------------: |
|      **By**      | **-Adel Moustafa**<br /> **-Mahmoud Abdelrhman**<br /> **-Mohamed Kamal**<br /> **-Mohamed Yasser** |
|      **To**      |                  **Prof/ Inas A. Yassine**                   |



# Bulk magnetization vector
 ​There are three functions used to rotate the bulk magnetization vector and plot its trajectory:

**1.Excitation:** It's used to rotate the bulk magnetization and it's trajectory during excitation process

**2.Relaxation:** It's used to rotate the bulk magnetization and it's trajectory during relaxation process.

**3.Update_line:** It's used to update the plotted data.

In addition to **get_param()** used to get parameters by console.
   
This GIFs is to simulate Bulk magnetization vector rotation.


![Image](Images/simulation.gif)

**Exitation GIF**


![Image](Images/Exitation.gif)


**Relaxition GIF**


![Image](Images/Relaxition.gif)




# Fourier Transform of an Image 

The FT of this Image is calculated using the function **np.fft.fft2()**, once we got the result, zero frequency component (DC component) will be at top left corner.we need to shift the result by N/2 in both the directions. This is simply done by the function, **np.fft.fftshift()**.(It is more easier to analyze). 

![Image](Images/cairo.jpg)

and this is FT of the Image. 

![Image](Images/FT_of_the_image.png)


# Simulation of the nonuniform external magnetic field

![Image](Images/nonuniform_B.png)

this graph simulate the unhomogeneity of the external magnetic field that is at every point at **z** there is  a different value for **B0** which is the case when applying the external magnetic field to the body in MRI.


