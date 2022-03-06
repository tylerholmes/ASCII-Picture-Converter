# ASCII-Picture-Converter

A python application to convert regular images into ASCII text images.

## Installation

To install on command line do:
```python
wget https://github.com/tylerholmes/ASCII-Picture-Converter/blob/main/ascii.py
```
Ensure you have python3 as well as Python Image Library (PIL) downloaded, if not download python3 from https://www.python.org/downloads/
and PIL from https://pillow.readthedocs.io/en/stable/installation.html. 


## Usage

First, ensure you have python3 and pillow To use simply run the ascii.py file either in your IDE or on the command line using ```python3 ascii.py``` and type in the path name of the picture you would like to convert to ascii. On lines 5 and 8 there are two initializations of the ascii_chars variable, the first one is using only 12 ascii characters while the second one on line 8 uses 70 ascii characters. By defauilt it is set to 12 ascii characters as it provides a more clear image, but to change it simply add a `#` at the beginning of line 5 and remove the `#` at the beginning of line 8 and run the program. Once you run the program it will create a text file named `ascii_image.txt`. Open this file to view your ascii image, you may need to zoom out to view the image using either `ctl -` or `command -`.

## Test

![test](https://user-images.githubusercontent.com/71055046/133010419-3940c3a6-ed71-4e4a-babe-18e46816c07a.jpeg)

[ascii_image.txt](https://github.com/tylerholmes/ASCII-Picture-Converter/files/7150727/ascii_image.txt)
