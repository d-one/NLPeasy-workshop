NLPeasy Workshop
================

> Build NLP pipelines the easy way

Repository for the NLPeasy workshop.

For the workshop you have 2 possibilities to participate.

## Mybinder.org

This is a pure online version so no installation needed on your laptop other than a browser. There might be issues to connect behind company firewalls though

> <https://mybinder.org/v2/gh/d-one/NLPeasy-workshop/master?urlpath=lab> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/d-one/NLPeasy-workshop/master?urlpath=lab)

However, there is only 1-2 GB of RAM available, which is tough for our example. Also if you loose your connection or close your laptop for 10 minutes your session is lost. *During the workshop we will provide you with bigger VMs in our cloud.*

## Own Laptop

You can work on your own laptop or server. For this you need:
- This Repository
- A Python Environment (>=3.6)
- Access to an Elasticsearch and Kibana Server: NLPeasy supports both connecting to an existing one or it can start one for you on docker. For this install **one of the following**:

- **Docker** <https://www.docker.com/get-started>, direct download links for
    [macOS (DMG)](https://download.docker.com/mac/stable/Docker.dmg) and
    [Windows (exe)](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe)
    (On Windows Home Edition make sure to have upgraded since May-2020).
- **Elasticsearch** and **Kibana**:
    <https://www.elastic.co/downloads/> or
    <https://www.elastic.co/downloads/elasticsearch-oss> (pure Apache licensed version, does not include Java SDK on macOS!)

### Setup 

Get this repository:

```bash
git clone https://github.com/d-one/nlpeasy-workshop
cd nlpeasy-workshop
```

Then setup a virtual environment, install requirements and download a spaCy-model:
Then on the terminal issue:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

Also you might want to download some bigger files:
```bash
bash download_files.csv
```
This will download:
- `profiles.csv.zip`: our data for today
- `okc-files.pickle`: the solution that should come out of NLPeasy

    (saving you a couple of hours of computation)
- `elastic-data.zip`: t

### Start Jupyter Lab

Still in the activated virtual env `venv` you now can start jupyter lab
```bash
jupyter lab
```
and navigate to the `hands-on-1.ipynb` Notebook.
