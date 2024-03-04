from pathlib import Path
from oig2p import get_epi
import logging
import pandas as pd

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.handlers[0].setFormatter(logging.Formatter('%(message)s'))

here = Path(__file__).parent
epi = get_epi()
df = pd.read_csv(here / "flexemes.csv")
df["phonological_form"] = df["label"].apply(epi.transliterate)

epi.log_trace()
df.to_csv(here / "flexemes.csv", index=False)


