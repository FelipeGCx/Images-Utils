# Images Utils

### this project is created to parsed the format in images or resizes them. i'm tired of websites that don't enable parsed more than five images at same time.

# ℹ️ Notes

- if you can contribuite with a new endpoints or logic, send a pull request.
- if you like this repo and it's usefull for your, give me a start 🌟

---

# 🚀 Getting started

### Install virtual enviroment if you don't have one

```bash
pip install virtualenv
```

### Create your virtual enviroment

```bash
virtualenv venv -p python3
```

### Init your virtual enviroment

```bash
source venv/bin/activate
```

### Install the requirement.txt

```bash
pip install -r requirements.txt
```

### Run the app helper

```bash
python3 src/app.py -h
```

![image with use options](/readme/first.png)

- use the modes starting with 2 to infer the image file format, if you only need to convert a specific format use the other modes such as p2w (png to wepb)

### Example to parsing one image from png to webp

```bash
python3 src/app.py -m="p2w" /home/user/pictures/img-01.png /home/user/pictures/
```

### Example to parsing images from a folder from any format to webp

```bash
python3 src/app.py -m="2webp" /home/user/pictures/ /home/user/pictures/
```

### Example to parsing images from a folder from jpg to png, excluiding rest images formats

```bash
python3 src/app.py -m="2png" /home/user/pictures/ /home/user/pictures/pngs
```
