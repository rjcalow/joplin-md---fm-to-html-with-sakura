import re
import pathlib

from template import indexpage


def gettitle(path):
    f = open(path, "r")

    regex = "<title.*?>(.+?)</title>"
    pattern = re.compile(regex)
    title = re.findall(pattern, f.read())[0]
    #print (title)
    return title


def mapdir(directory, base, imagefoldername):
    html = ""

    if len(directory.parts) > 1:
        html = f"<ul><h1>{directory.name}</h1>"
    if len(directory.parts) > 2:
        html = f"<ul><h6>{directory.name}</h6>"

    if len(directory.parts) != 1:
        for h in sorted(directory.glob('*.html')):
            title = gettitle(h)
            url = "./" + str(h.relative_to(base))
            html += f'''<li><a href="{url}">{title}</a></li>'''

    for path in sorted(directory.glob('*')):
        if path.is_dir():
            if imagefoldername not in path.parts:
                html += mapdir(path, base, imagefoldername)
    html += "</ul>"

    return html


def render_site_map(output, base, imagefoldername):
    #html = mapdir (pathlib.Path("public") , pathlib.Path("public") )
    html = mapdir(output, base, imagefoldername)
    i = indexpage(html)
    with open("public/sitemap.html", 'w') as file:
        file.write(i)
