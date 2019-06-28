#TODO:
# 1) install dataset
# 2) look for dats-descriptor.json file
# 3) validate dats model
# 4) run generic JSON-LD extractor on dats-descriptor.json and see how it behaves
# 5) investigate on how this/extracted content impacts the search when you want to quary some fileds form the extracted content

import logging
import os.path as op
import dats.dats_model as dats_model
from datalad_metalad.extractors.custom import CustomMetadataExtractor
from rdflib import Graph
from datalad.api import install
import tempfile
import os
import shutil


def process_dataset():
    path = tempfile.mkdtemp()
    try:
        # Installation of the visual-working-memory dataset
        dataset = install(path, "///openneuro/ds001634")  # can try other datasets as well, "///openfmri/ds000164"
    except Exception as e:
        logging.error('Failed to install dataset: ' + str(e))
    else:
        logging.info('\n')
        logging.info('Successfully installed\n')
        extract_dats_meta(dataset, path)


def extract_dats_meta(ds, path):

    """ Validates DATS JSON schemas and the DATS JSON instances against the schemas
    :param ds: dataset
    :param path: dataset path
    """

    # The DATS based dataset description is still not part of the dataset, so we will go ahead and add it

    json_file = 'dataset.json'
    # create a path to the .metadata directory
    path = os.path.join(path, ".metadata")
    os.mkdir(path)
    # add path to dataset(may not need it)
    ds.add(path)
    # get current path for the dataset.json DATS file
    json_path = op.join(op.dirname(__file__), json_file)
    # copy current json file to .metadata directory
    new_jason_path = shutil.copy(json_path, path)
    # add new json file path to the dataset
    ds.add(new_jason_path)
    if dats_model.validate_schema(op.dirname(new_jason_path), json_file):
        logging.info(json_file + ' validation went OK\n')
        return run_extractor(ds)
    else:
        logging.error('Validation was not successful')
        return []


# The validate_dats_graph function is a possible addition to validate dats by graph
def validate_dats_graph(path):
    with open(path, "r") as j:
        dats_agr = j.read()
        print(dats_agr)
        g = Graph().parse(data=dats_agr, format='json-ld')
        print(g.serialize(format='n3', indent=4))
        j.close()


def run_extractor(ds):
    # run datalad-metalad custom extractor for json-ld files
    logging.info('Running custom jason-ld extractor \n')
    c = CustomMetadataExtractor()
    content = c.get_required_content(ds, process_type="dataset", status=["ok"])
    logging.info('Content extracted \n')
    return content


process_dataset()
