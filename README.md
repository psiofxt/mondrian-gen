# mondrian-gen
Utilizing tkinter, rectangles are recursively drawn to mimic the style
of Mondrian's abstract art.

Images are saved using Ghostscript to the /img folder.

After a new image is generated and saved, the structural similarity of this image
compared to a pool of "base" Mondrian images is calculated in color and in grayscale.
The average ssim value for color and gray is displayed at the top of the window.

## Installation
Python 3.6 is required.

To install Ghoscript (Linux):
```
sudo apt-get install ghostscript
```
Mac:
```
brew install ghostscript
```
Install the image processing requirements:
```
pip install -r requirements.txt
```
Finally, to run the abstract goodness:
```
python mondrian.py
```

## Examples
[image_one]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/example1.jpg "Image One"
[image_two]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/example2.jpg "Image Two"
[image_three]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/example3.jpg "Image Three"
[image_four]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/ssim_example.png "Image Four"
[image_five]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/example4.jpg "Image Five"
[image_six]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/example5.jpg "Image Six"
[image_six]: https://raw.githubusercontent.com/psiofxt/mondrian-gen/master/img/example6.jpg "Image Seven"

![alt text][image_one]

![alt text][image_two]

![alt text][image_three]

![alt text][image_five]

#### Increasing volume of squares
![alt text][image_six]

![alt text][image_seven]

#### Displaying ssim index
![alt text][image_four]
