import datetime
import math
import os
from PIL import Image
import argparse
import pillow_avif


class App():
    def __init__(self):
        # parser get the arguments from console
        parser = argparse.ArgumentParser(description="Guide to use images utils",
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument(
            "-m", "--mode", help="select mode to parse", choices=["2png", "2webp", "2jpg", "p2w", "p2j" ,"p2a", "w2p", "w2j","w2a", "j2p", "j2w","j2a", "a2p", "a2w", "a2j"], default="p2w")
        parser.add_argument("-q", "--quality", type=int, choices=range(0, 101),
                            metavar="[0-100]",
                            help='select quality output (0-100)', default=100)
        parser.add_argument("-hs", "--height", type=int, choices=range(0, 8001), metavar="[0-8000]",
                   help='select height output (0-8000) 0 is auto', default=0)

        parser.add_argument("-ws", "--width", type=int, choices=range(1, 8001), metavar="[0-8000]",
                   help='select width output (0-8000) 0 is auto', default=0)

        parser.add_argument("-t", "--thumbnail",action="store_true", default=False, help="conserve proportions")
        parser.add_argument("src", help="Source location")
        parser.add_argument("dest", help="Destination location")
        args = parser.parse_args()
        if (args.thumbnail and not args.width) and (args.thumbnail and not args.height):
            parser.error("El argumento -t no se puede usar sin -hs o -ws")
        config = vars(args)
        self.mode = config["mode"]
        self.format = self.get_format(config["mode"])
        self.og_format = self.get_original_format(config["mode"])
        self.mode = self.get_format(config["mode"])
        self.src = os.path.abspath(config["src"])
        self.dest = os.path.abspath(self.get_dest(config))
        self.width = config["width"]
        self.height = config["height"]
        self.thumb = config["thumbnail"]
        self.quality = math.floor(((config["quality"] - 0) / (100 - 0)) * (100 - 20) + 20)
        self.start_parsing()
        
    def get_format(self, mode):
        if mode == "2webp" or mode == "p2w" or mode == "j2w" or mode == "a2w":
            return "webp"
        elif mode == "2avif" or mode == "w2a" or mode == "j2a" or mode == "p2a":
            return "avif"
        elif mode == "2png" or mode == "w2p" or mode == "j2p" or mode == "a2p":
            return "png"
        elif mode == "2jpg" or mode == "p2j" or mode == "w2j" or mode == "a2j":
            return "jpg"
    
    def get_original_format(self, mode):
        if mode == "a2w" or mode == "a2p" or mode == "a2j":
            return "avif"
        elif mode == "w2p" or mode == "w2j" or mode == "w2a":
            return "webp"
        elif mode == "p2w" or mode == "p2j" or mode == "p2a":
            return "png"
        elif mode == "j2p" or mode == "j2w" or mode == "j2a":
            return "jpg"
        else:
            return "all"

    def get_dest(self, config):
        if config["dest"] == ".":
            if os.path.isdir(config["src"]):
                return config["src"]
            else:
                folder, _ = os.path.split(config["src"])
                return folder
        else:
            if os.path.isdir(config["dest"]):
                return config["dest"]
            else:
                folder, _ = os.path.split(config["dest"])
                return folder

    def start_parsing(self):
        print("Parsing ...")
        if os.path.isfile(self.src):
            if self.og_format in self.src or self.og_format == "all":
                self.parse_image(self.src)
            else:
                print("Error: Entry Image Format Invalid")
                os._exit(0)
        else:
            self.convert_images()
        print("Parse Completed Succesfully")

    def parse_image(self, filename):
        if self.is_image(filename):
            if not os.path.exists(self.dest):
                os.makedirs(self.dest)
            name = self.create_name(filename, self.dest, self.format)
            image = self.open_image(filename)
            image = self.resize_image(image)
            if self.format == "jpg":
                image = image.convert("RGBX")
            self.save_image(image, name, self.quality)
            
    def resize_image(self, image):
        ws, hs = image.size
        nw =  self.height if self.width == 0 else self.width 
        nh =  self.width if self.height == 0 else self.height
        size = (nw, nh)
        if self.thumb:
            size = (size[0],int(hs * size[0] / ws)) if ws > hs else (int(ws * size[0] / hs),size[0])
        if self.width > 0 or self.height > 0:
            image = image.resize(size)
        return image

    def convert_images(self):
        files = os.listdir(self.src)
        for file in files:
            filepath = os.path.join(self.src, file)
            if os.path.isfile(filepath):
                if self.og_format in filepath or self.og_format == "all":
                    self.parse_image(filepath)

    def is_image(self, filename):
        return (filename.endswith(".jpg") or filename.endswith(
            ".png") or filename.endswith(".webp") or filename.endswith(".jpeg") or filename.endswith(".avif"))

    def create_name(self, fullpath, dest, format):
        filename = os.path.basename(fullpath)
        name, ext = os.path.splitext(filename)
        new_dest = os.path.join(dest, f"{name}.{format}")
        if os.path.exists(new_dest):
            name = f"{name}-{datetime.datetime.now().strftime('%a%d%b%Y,%I:%M%p')}"
        return os.path.join(dest, f"{name}.{format}")

    def open_image(self, filename):
        try:
            return Image.open(filename)
        except (TypeError, FileNotFoundError, OSError) as e:
            if(e.__class__.__name__ == "TypeError"):
                print("Error: File type not supported")
            elif(e.__class__.__name__ == "FileNotFoundError"):
                print("Error: File not found")
            elif(e.__class__.__name__ == "UnidentifiedImageError"):
                print("Error: Can not identify image file")
            else:
                print("Error: Something went wrong")
            os._exit(0)

    def save_image(self, image, filename, quality):
        image.save(filename, quality=quality, optimize=True)
        image.close()


if __name__ == "__main__":
    app = App()
