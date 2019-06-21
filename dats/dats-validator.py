#TODO:
# 1) install dataset
# 2) look for dats-descriptor.json file
# 3) validate dats model
# 4) run generic JSON-LD extractor on dats-descriptor.json and see how it behaves

# datalad install[-h][-s SOURCE] [-d DATASET][-g][-D DESCRIPTION] [-r][--recursion - limit LEVELS] [--nosave][--reckless][-J NJOBS] [PATH[PATH...]]

from datalad.api import Dataset
import os.path as op
import logging
import dats.dats_model as dats_model

from rdflib import Graph

dats_model.validate_schema(op.dirname(__file__), 'visual-working-memory-dats.json')

with open("./visual-working-memory-dats.json", "r") as j:
    dats_agr = j.read()
    g = Graph().parse(data=dats_agr, format='json-ld')
    # print(g.serialize(format='n3', indent=4))

v = op.join(op.dirname(__file__), "../json-schemas")
print(v)


# def install_datasets(path, source):
#
#     ds = Dataset(path)
#     ds.install(path=path, source=source)
#     res = ds.get
#
#     # look for dats model file such as res.contains(.../dats-model-file), otherwise add it
#     datspath = op.join(op.dirname(__file__), 'visual-working-memory-dats.json')
#     ds.add(datspath)
#
#     success = False
#
#     try:
#         success = True
#
#     except Exception as e:
#         logging.error('Error ' + str(e))
#
#     return success


def validate_dats(ds, path):

    """ Validates DATS JSON schemas and the DATS JSON instances against the schemas
    :param ds:
    :param path: path to json-ld file
    :return:
    """
    with open("./visual-working-memory-dats.json", "r") as j:
        dats_agr = j.read()
        print(dats_agr)
        g = Graph().parse(data=dats_agr, format='json-ld')
        print(g.serialize(format='n3', indent=4))

    return []