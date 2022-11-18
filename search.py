from template import searchTemplate
from utils import compress 

def generate_entries(page, html, i):
    
    return f''' <li data-question-id="{i}">
            <p>
            <a href="./{page.url}"
                >{page.page["title"]}</a>
            </p>
  
            <section>
            <div class="snippet">
                {page.page["title"]} </br> {html}
            </div>
            </section>
        </li>
        
        '''
 
def render_searchpage(pages, save_to):
    i = 100
    entries = ""
    print(type(pages))
    for page in pages:
        entries += generate_entries(page, page.html, i)
        i += 1


        ## minify html
    entries=compress(entries)      
    s=searchTemplate(entries)

  
    with open (save_to, 'w') as file:
        file.write(s)
    

