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
from datalad.api import add
import tempfile
import os
import shutil
from subprocess import call


def install_dataset():
    print("IM AM IN")
    data_dir = tempfile.mkdtemp()
    try:
        dataset = install(data_dir, "///openfmri/ds000164")  # visual-working-mem: "///openneuro/ds001634"
    except Exception as e:
        logging.error("Failed to install dataset: " + str(e))
    else:
        try:
            print("ok")
            # extract_dats_meta(dataset, data_dir)
        except Exception as e:
            logging.error("Failed to get dataset content: " + str(e))


def extract_dats_meta(ds, data_dir):

    """ Validates DATS JSON schemas and the DATS JSON instances against the schemas
    :param ds:
    :param path: path to json-ld file
    :return:
    """

    # if op.exists(op.join(data_dir, "dataset.json")):
    #     if dats_model.validate_schema(data_dir, "dataset.json"):
    #         run_extractor(ds, op.join(data_dir, "dataset.json"))
    #     else:
    #         logging.error("Failed to validate dataset.json")
    #
    # else:

    path = os.path.join(data_dir, ".metadata")
    json_path = op.join(op.dirname(__file__), 'dataset.json')
    new_jason_path = shutil.copy(json_path, path)
    ds.add(new_jason_path)
    run_extractor(ds)

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


install_dataset()
