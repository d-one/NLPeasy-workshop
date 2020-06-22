import os
c.ServerProxy.servers = {
  'kibana': {
        'command': None,    # connect to the running server - by our changed jupyter_server_proxy
        'launcher_entry': {
            'title': 'Kibana',
            'icon_path': os.path.join(os.path.expanduser("~"), '.jupyter', 'kibana.svg')
        },
        "absolute_url": False,
        "port": 5601,
        "new_browser_tab": False,
    }
}

