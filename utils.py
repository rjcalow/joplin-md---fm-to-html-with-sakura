import shutil
import urllib.parse
from img_process import IMG_process
from pathlib import Path

def processimages(source, destination):
    create_folder(destination)
    for f in source.glob("*"):
        if ".jpg" or ".jpeg" or ".png" in str(f.name).lower():

            d = destination / f.name
            if d.exists() == False:
                IMG_process(1000, f, d)

def copyallfiles(source, destination):
    create_folder(destination)
    print(destination)
    for f in source.glob('*'):
        d = destination / f.name
        if d.exists() == False:
            copy(f, d)


def copy(source, destination):
    shutil.copy(str(source), str(destination))

def create_folder(path):
    if path.exists() == False:
        path.mkdir(parents=True, exist_ok=True)

    return

def urlsafe(path):
    return urllib.parse.quote(str(path).replace(" ", "").lower())

def compress(html):
    import minify_html
    return minify_html.minify(html)    

##needs work
def delete_folder(pth) :
    for sub in pth.iterdir() :
        if sub.is_dir() :
            delete_folder(sub)
        else :
            sub.unlink()    