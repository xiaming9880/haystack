import logging

import pandas as pd
from haystack.finder import Finder

pd.options.display.max_colwidth = 80

logger = logging.getLogger(__name__)

logging.getLogger('farm').setLevel(logging.WARNING)
logging.getLogger('farm.infer').setLevel(logging.INFO)
logging.getLogger('transformers').setLevel(logging.WARNING)
logging.getLogger('farm.eval').setLevel(logging.INFO)


