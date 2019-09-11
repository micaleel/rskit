import os
from urllib.request import urlretrieve

from tqdm import tqdm


class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""

    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize


eg_link = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
with TqdmUpTo(
    unit="B", unit_scale=True, miniters=1, desc=eg_link.split("/")[-1]
) as t:  # all optional kwargs
    urlretrieve(eg_link, filename=os.devnull, reporthook=t.update_to, data=None)
