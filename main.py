from page import render_pages
from search import render_searchpage
from index import render_index
from utils import copyallfiles, delete_folder, processimages, create_folder, delete_folder
from site_map import render_site_map
import pathlib

'''
Settings
'''
input = pathlib.Path("/yournotes")
output = pathlib.Path("public")
images = pathlib.Path("/yournotes._resources")

''' 
Prep
'''
delete_folder(output)
create_folder(output)

'''
Main
'''
pages = render_pages(input, output)
render_searchpage(pages, output / "search.html")
render_index(pages, output / "index.html")
render_site_map(output, output, images.stem)
'''
Assets
'''
#copyallfiles(images, output / images.stem)
processimages(images, output / images.stem)
