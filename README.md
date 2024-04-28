# Images Utils

### this project is created to parsed the format in images or resizes them. i'm tired of websites that don't enable parsed more than five images at same time.
---
## thanks to [Pillow](https://pillow.readthedocs.io/en/stable/) I can create this tool 

## ⚠️ Currently there are problems with images with alpha when parsing them to jpg

# ℹ️ Notes

- if you can contribuite with a new logic, send a pull request.
- if you like this repo and it's usefull for your, give me a start 🌟
-  Added handler to  save parsed images in the same folder, use "."
-  Added compatibility to relatives paths
-  Added quality mode to compress images use -q=""
- ## Added resize mode to resize images use -ws="" and -hs="" 
- ## Added thumbnail mode to conserve aspect images use -t=""

---

# 🚀 Getting started to try or develop

### Install virtual enviroment if you don't have one

```bash
pip install virtualenv
```

### Create your virtual enviroment

```bash
virtualenv venv -p python3
```

### Init your virtual enviroment 

#### Linux
```bash
source venv/bin/activate
```
#### Windows
```bash
.\venv\Scripts\activate
```

### Install the requirement.txt

```bash
pip install -r requirements.txt
```

### Run the app helper

```bash
python3 src/app.py -h
```

---

# 🚀 How Install

### Go to [Releases](https://github.com/FelipeGCx/Images-Utils/releases/tag/imageTool)
Download the version .tar.gz that you want

### Install the .tar.gz in your system
```bash
pip install imgtl-(version).tar.gz
```
### it's Done
### Use the app with the `imgtl` command
```bash
imgtl -h
```

### Examples

![image with use options](/readme/first.png)

- use the modes starting with 2 to infer the image file format, if you only need to convert a specific format use the other modes such as p2w (png to wepb)

### Example to parsing one image from png to webp

```bash
imgtl -m="p2w" /home/user/pictures/img-01.png /home/user/pictures/
```

### Example to parsing images from a folder from any format to webp

```bash
imgtl -m="2webp" /home/user/pictures/ /home/user/pictures/
```

### Example to parsing images from a folder from jpg to png, excluiding rest images formats

```bash
imgtl -m="2png" /home/user/pictures/ /home/user/pictures/pngs
```

### Example to parsing images from a folder from png to webp and usign quality option

```bash
imgtl -m="2webp" -q="50" /home/user/pictures/ . 
```

### Example to parsing images from a folder from jpg and resize 

```bash
imgtl -m="2jpg" -ws="1000" /home/user/pictures/ . 
```
*in this case the output image is 1000x1000 

### Example to parsing images from a folder from jpg and resize and conserve aspect

```bash
imgtl -m="2jpg" -ws="1000" -t /home/user/pictures/ . 
```
*in this case the output image conserve aspect ratio

