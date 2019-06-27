#TODO:
# 1) install dataset
# 2) look for dats-descriptor.json file
# 3) validate dats model
# 4) run generic JSON-LD extractor on dats-descriptor.json and see how it behaves
# 5) investigate on how this/extracted content impacts the search when you want to quary some fileds form the extracted content


import os.path as op
import logging
import dats.dats_model as dats_model
from datalad_metalad.extractors.custom import CustomMetadataExtractor
from rdflib import Graph
from datalad.api import install
import tempfile
import os
from subprocess import call



def install_dataset():
    data_dir = tempfile.mkdtemp()
    try:
        dataset = install(data_dir, "///openfmri/ds000164")
    except Exception as e:
        logging.error("Failed to install dataset: " + str(e))
    else:
        try:
            dataset.get("sub-001/func/")
        except Exception as e:
            logging.error("Failed to get dataset content: " + str(e))


def validate_dats(ds, data_dir):

    """ Validates DATS JSON schemas and the DATS JSON instances against the schemas
    :param ds:
    :param path: path to json-ld file
    :return:
    """

    datspath = op.join(data_dir, "descriptor-dats.json")
    if op.exists(datspath):
        dats_model.validate_schema(datspath)
    else:
        dats_model.validate_schema(op.dirname(__file__), 'descriptor-dats.json')

    return []


def validate_dats_graph(path):
    with open(path, "r") as j:
        dats_agr = j.read()
        print(dats_agr)
        g = Graph().parse(data=dats_agr, format='json-ld')
        print(g.serialize(format='n3', indent=4))
        j.close()


def run_extractor(ds):
    # run extractor
    c = CustomMetadataExtractor()
    if ds.is_installed():
        content = c.get_required_content(ds, process_type="dataset", status=["ok"])

    return content


search_dataset()