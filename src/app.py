import datetime
import os
from PIL import Image
import argparse


class App():
    def __init__(self):
        # parser get the arguments from console
        parser = argparse.ArgumentParser(description="Guide to use images utils",
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument(
            "-m", "--mode", help="select mode to parse", choices=["2png","2webp", "2jpg", "p2w", "p2j", "w2p", "w2j", "j2p", "j2w"], default="p2w")
        parser.add_argument("src", help="Source location")
        parser.add_argument("dest", help="Destination location")
        args = parser.parse_args()
        config = vars(args)
        self.start_parsing(config)

    def start_parsing(self, config):
        print("Parsing ...")
        format = self.get_format(config["mode"])
        og_format = self.get_original_format(config["mode"])
        if os.path.isfile(config["src"]):
            if og_format in config["src"]:
                self.parse_image(config["src"], config["dest"], format)
            else:
                print("Error: Entry Image Format Invalid")
                os._exit(0)
        else:
            self.convert_images(
                config["src"], config["dest"], format, og_format)
        print("Parse Completed Succesfully")

    def get_format(self, mode):
        if mode == "2webp" or mode == "p2w" or mode == "j2w":
            return "webp"
        elif mode == "2png" or mode == "w2p" or mode == "j2p":
            return "png"
        elif mode == "2jpg" or mode == "p2j" or mode == "w2j":
            return "jpg"

    def get_original_format(self, mode):
        if mode == "w2p" or mode == "w2j":
            return "webp"
        elif mode == "p2w" or mode == "p2j":
            return "png"
        elif mode == "j2p" or mode == "j2w":
            return "jpg"
        else:
            return "all"

    def convert_images(self, src, dest, format, og_format):
        files = os.listdir(src)
        for file in files:
            filepath = f"{src}/{file}"
            if os.path.isfile(filepath):
                if og_format in filepath or og_format == "all":
                    self.parse_image(filepath, dest, format)

    def parse_image(self, filename, dest, format):
        if self.is_image(filename):
            if not os.path.exists(dest):
                os.makedirs(dest)
            name = self.create_name(filename, dest, format)
            image = self.open_image(filename)
            if format == "jpg":
                image = image.convert("RGB")
            self.save_image(image, name)

    def is_image(self, filename):
        return (filename.endswith(".jpg") or filename.endswith(
            ".png") or filename.endswith(".webp") or filename.endswith(".jpeg"))

    def create_name(self, filename, dest, format):
        name, ext = os.path.splitext(filename)
        name = name.split("/")[-1]
        if os.path.exists(f"{dest}/{name}.{format}"):
            name = f"{name}-{datetime.datetime.now()}"
        return f"{dest}/{name}.{format}"

    def open_image(self, filename):
        return Image.open(filename)

    def save_image(self, image, filename):
        image.save(filename)
        image.close()


if __name__ == "__main__":
    app = App()
