''' edit the index page here '''

from template import indexpage
from page  import pagesbydate

def render_latest(pages):
    html =  '''   
    <h3>Latest notes</h3><ul>'''

    for p in pages[:10]:
        html += f'''

        <li><small>[{p.page['date']}]</small> <a href="./{p.url}">{p.page['title']}</a> in {p.parent}</li>

        '''
    html += '''</ul>'''
    
    return html

def site_map(pages):
    parents =[]
    for p in pages:
        pass

def render_index(pages, save_to):
    sorted = pagesbydate(pages)

    i = indexpage(render_latest(sorted))
    with open(save_to, 'w') as file:
        file.write(i)

