| Programming task |                              #1                              |
| :--------------: | :----------------------------------------------------------: |
|      **By**      | **-Adel Mostafa **<br /> **-Mahmoud Abdelrhman **<br /> **-Mohamed Kamal** <br /> **-Mohamed Yasser** |
|      **To**      |                  **Prof/ Inas A. Yassine**                   |

> ------
>
> # [Bulk magnetization vector]()
>
> ​		**There are three functions used to rotate the bulk magnetization vector and plot its trajectory:**
>
> 1. **[Excitation:]() It's used to rotate the bulk magnetization and it's trajectory during excitation process.**
>
>    ![](/images/Exitation.gif)
>
> 2. **[Relaxation:]() It's used to rotate the bulk magnetization and it's trajectory during relaxation process.**
>
>    ![](/images/Relaxition.gif)
>
> 3. **[Update_line:]() It's used to update the plotted data.**
>
>    **In addition to  [get_param]() used to get parameters by console**.
>
>    **This video is to simulate Bulk magnetization vector rotation**.
>
>    ![](/images/simulation.gif)
>
> ------
>
> # [Fourier Transform of an Image]()
>
> ​		**The FT of this Image is calculated using the function [np.fft.fft2()](), once we got the result, zero frequency component (DC component) will be at top left corner. We need to shift the result by N/2 in both the directions. This is simply done by the function, [np.fft.fftshift()](). (It is more easier to analyze).** 
>
> ​		**The next two /images are and image and its FT.**
>
> ![](/images/cairo.jpg)
>
> ![](/images/FT_of_the_image.PNG)

> ------
>
> # [Simulation of the nonuniform external magnetic field]()
>
> ![](/images/nonuniform_B.PNG)
>
> ​		**This graph simulate the non-homogeneity of the external magnetic field that is at every point at *[z]()* there is  a different value for *[B0]()* which is the case when applying the external magnetic field to the body in MRI.**
>
