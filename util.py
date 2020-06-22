import os
from IPython.display import HTML, Javascript, display

BINDER = 'BINDER_PORT' in os.environ

def kibana_on_binder():
    prefix = os.environ['JUPYTERHUB_SERVICE_PREFIX']
    url = f"https:////hub.gke.mybinder.org/{prefix}/kibana".replace('//','/')
    print(url)
    return(url)

def display_kibana_link():
    script = 'element.innerHTML = \'Kibana on <a href="kibana" target="_blank">./kibana</a>\';'
    display(Javascript(script))
