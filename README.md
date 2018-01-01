# OCR Image Processing 
## Read out the captcha

Author: Lin Dong

Date: July 22nd, 2016

## Prerequisites

```
# MAC
brew install imagemagick
brew install tesseract --all-languages

# Linux
sudo apt-get install imagemagick
sudo apt update sudo apt install tesseract-ocr

# The next thing to do is install the language packs. Tesseract is very robust and it can extract over 100 different languages, provided # the language packs are downloaded. You can download a particular language pack by using the generic command below:
# sudo apt-get install tesseract-ocr-[lang]
sudo apt-get install tesseract-ocr-eng sudo apt-get install tesseract-ocr-por

# Windows, MAC or Linux.
pip install Pillow
pip install pytesseract
```
Need Install tesseract windows executable:<br>
download and install:<br>
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.01.exe<br>
** Need add path of tesseract in environment variable path.<br>
windows path:
"C:\Program Files (x86)\Tesseract-OCR"

### Tools:

1. Tesseract
2. Imagemagick
3. Pytesseract
4. Pillow,  PIL(python image processing)

## Instructions

Just run: `python main.py`

* `iteration.py`: iterate multiple times of original image
* `convert_to_text.py`: read out the string from white-gray image,

## Screenshots

Progressive Iterations: 

Iteration 1: ![](./screenshots/iteration_0.jpeg)

Iteration 2: ![](./screenshots/iteration_1.jpeg)

Iteration 3: ![](./screenshots/iteration_2.jpeg)

# References
1. [python 识别验证码](https://segmentfault.com/q/1010000005686388)
2. [OCR on OS X with tesseract Raw](https://gist.github.com/henrik/1967035)
3. http://www.pythonware.com/products/pil/
4. https://github.com/UB-Mannheim/tesseract/wiki

