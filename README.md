NLPeasy Workshop
================

> Build NLP pipelines the easy way

Repository for the NLPeasy workshop.

For the workshop you have 2 possibilities to participate.

## Mybinder.org

Online version so now installation needed on your laptop - might even work on a laptop ;-)

> <https://mybinder.org/v2/gh/d-one/NLPeasy-workshop/master?urlpath=lab> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/d-one/NLPeasy-workshop/master?urlpath=lab)

However, there is only 1-2 GB of RAM available, which is tough for our example. Also if you loose your connection or close your laptop for 10 minutes your session is lost.

## Own Laptop

You can work on your own laptop or server. For this you need:
- This Repository
- A Python Environment (>=3.6)
- Access to an Elasticsearch and Kibana Server: NLPeasy supports both connecting to an existing one or it can start one for you on docker. For this install **one of the following**:

- **Docker** <https://www.docker.com/get-started>, direct download links for
    [Mac (DMG)](https://download.docker.com/mac/stable/Docker.dmg) and
    [Windows (exe)](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe).
- **Elasticsearch** and **Kibana**:
    <https://www.elastic.co/downloads/> or
    <https://www.elastic.co/downloads/elasticsearch-oss> (pure Apache licensed version, does not include Java SDK!)

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
### Start Jupyter Lab

Still in the activated virtual env `venv` you now can start jupyter lab
```bash
jupyter lab
```
and navigate to the `hands-on-1.ipynb` Notebook.
