# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Lyrics dataset parsed from Genius"""


import csv
import json
import os
import gzip

import datasets


_CITATION = """\
@InProceedings{huggingartists:dataset,
title = {Lyrics dataset},
author={Aleksey Korshuk
},
year={2021}
}
"""


_DESCRIPTION = """\
This dataset is designed to generate lyrics with HuggingArtists.
"""

# Add a link to an official homepage for the dataset here
_HOMEPAGE = "https://github.com/AlekseyKorshuk/huggingartists"

# Add the licence for the dataset here if you can find it
_LICENSE = "All rights belong to copyright holders"

_URL = "https://huggingface.co/datasets/huggingartists/MODEL_NAME/resolve/main/datasets.json"

# Name of the dataset
class LyricsDataset(datasets.GeneratorBasedBuilder):
    """Lyrics dataset"""

    VERSION = datasets.Version("1.0.0")

    def _info(self):
        # This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset
        features = datasets.Features(
                {
                    "text": datasets.Value("string"),
                }
            )
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # This defines the different columns of the dataset and their types
            features=features,  # Here we define them above because they are different between the two configurations
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=None,
            # Homepage of the dataset for documentation
            homepage=_HOMEPAGE,
            # License for the dataset if available
            license=_LICENSE,
            # Citation for the dataset
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # This method is tasked with downloading/extracting the data and defining the splits depending on the configuration
        # If several configurations are possible (listed in BUILDER_CONFIGS), the configuration selected by the user is in self.config.name

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLs
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        data_dir = dl_manager.download_and_extract(_URL)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": data_dir,
                    "split": "train",
                },
            ),
        ]
        

    def _generate_examples(self, filepath, split):
        """Yields examples as (key, example) tuples."""
        # This method handles input defined in _split_generators to yield (key, example) tuples from the dataset.
        
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
            for id, pred in enumerate(data[split]):
                yield id, {"text": pred}