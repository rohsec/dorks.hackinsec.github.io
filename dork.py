from pyscript import document, display, HTML
import re
from time import sleep

inp=document.getElementById('inp')
out=document.getElementById('out')
prog=document.getElementById('prog')
sleep(1)
prog.remove()
div=document.getElementById('warn')
domain_pattern = r"^(?![0-9]+$)(?!-)(?:[a-zA-Z0-9-]{0,62}[a-zA-Z0-9]\.)+(?:[a-zA-Z]{2,})$"
with open('dorks1.txt', "r") as f1:
    x1=f1.readlines()

for i in x1:
            if(i.startswith("#")):
                display(HTML(f"<h1 class='subtitle is-primary'>{i[3:]}</h1>"))
            else:
                display(HTML(f"<a class='is-link has-text-link-dark' target='_blank' href='https://google.com/search?q={i[1:]}'>{i[1:]}</a>"))
    
f1.close()
def rm_warn(event):
    out.innerHTML=""

def dorker(event):
    div.innerHTML=""
    if(re.match(domain_pattern,inp.value)):
        out.innerHTML=""
        for i in x1:
            if(i.startswith("#")):
                display(HTML(f"<h1 class='subtitle is-primary'>{i[3:]}</h1>"))
            else:
                display(HTML(f"<a class='is-link has-text-link-dark' target='_blank' href='https://google.com/search?q={i.replace('example.com',inp.value)[1:]}'>{i.replace('example.com',inp.value)[1:]}</a>"))
    # print(x1)
    else:
        div.innerHTML="<p class='has-text-danger px-1'>Please insert a valid domain!!</p>"
        #'''<article id="dng" class="message is-danger">
        #   <div class="message-header">
        #     <p>Invalid Input</p>
        #     <button class="delete" aria-label="delete" py-click="rm_warn"></button>
        #   </div>
        #   <div class="message-body">
        #     <strong>Please enter a valid domain !!</strong>
        #   </div>
        # </article>'''
        # div.append(div)



