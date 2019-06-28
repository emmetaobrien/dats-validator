# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""BIDS metadata extractor (http://bids.neuroimaging.io)"""

from __future__ import absolute_import
from math import isnan

# use pybids to evolve with the standard without having to track it too much
import json

from io import open
from os.path import exists
from datalad.metadata.extractors.base import BaseMetadataExtractor
from datalad.metadata.definitions import vocabulary_id
from os.path import join

import logging
from datalad.log import log_progress
lgr = logging.getLogger('datalad.metadata.extractors.dats')


context = {
    'dats': {
        '@id': 'http://w3id.org/dats/context/sdo#',
        'description': 'Data Tag Suite (DATS) context mapping to Schema.org',
        'type': vocabulary_id}
}


class MetadataExtractor(BaseMetadataExtractor):

    _dsdescr_fname = 'dataset_description_dats.json'


    def get_metadata(self, dataset, content = False):

        self.path = "./dataset.json"  # temporary
        try:
            exists(self.path)
        except FileNotFoundError:
            logging.error('The %s dataset is missing a DATs based json description file at %s path' % (self.ds, self.path)) # for now we use a sample path but may be many
        else:
            return \
                self._get_dataset_metadata() if dataset else None, \
                ((k, v) for k, v in self._get_content_metadata()) if content else None


        # TODO: Maybe check that it is a valid json format, so add !try and catch!
        # TODO: question, if to substitute @context with context and $schema with schema, o where to add anything else

    def _get_dataset_metadata(self):
        with open(self.path) as json:
            dsmeta = json.load(json)
            json.close()
            print(dsmeta)
        return dsmeta

    # def _get_content_metadata(self):




