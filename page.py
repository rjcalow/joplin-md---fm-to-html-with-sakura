''' edit pages here '''
import pathlib
import glob
import markdown
import frontmatter 
from utils import create_folder, urlsafe, compress
from template import default, searchTemplate
from datetime import datetime
from markdown.extensions.wikilinks import WikiLinkExtension
from md_ex.mdx_urlize import UrlizeExtension


class Page:
      def __init__(self, f, save_to, url):
        with open(f, 'r') as file: self.page = frontmatter.load(f) 
        
        self.loc = pathlib.Path(save_to)
        self.url = url
        self.page['date'] = self.page['created'].strftime("%Y-%m-%d")
        searchurl = "search.html?="
        for i in range(len(save_to.parts) - 2):   
            searchurl = "../" + searchurl

        self.html = markdown.markdown(self.page.content, extensions=[WikiLinkExtension(base_url=searchurl, end_url=''), UrlizeExtension()])
        #self.html = compress(self.html)
        self.parent = f.parts[-2]


def pagesbydate(pages):
    #return sorted(pages, key=lambda page: datetime.strptime(
        #str(page.page['date']), "%Y-%m-%d "), reverse=True)
    return sorted(pages, key=lambda page: page.page['date'], reverse=True)

def render_pages(input, output):
    pages = []
    
    files = input.rglob('*/*.md')

    for f in files:
        url = urlsafe(f.relative_to(input).parent) + "/" + urlsafe(f.stem) + ".html"
        save_to = output / urlsafe(f.relative_to(input).parent) / (str(f.stem).replace(" ", "").lower() + ".html")
        pages.append(Page(f, save_to, url))
        create_folder(output / urlsafe(f.relative_to(input).parent)) 
    
    for p in pages:
        r=default(p.page,p.html)
        r= compress(r)
        with open(p.loc, 'w') as file:
            file.write(r)
    
    
    return pages
    