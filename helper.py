import pandas as pd
import os
import profiler as pf
from split import split


class file:
    def __init__(self, fpath):
        self.fpath = fpath
        self.size = os.stat(fpath).st_size
        self.psize = pf.sizeof_fmt(self.size)

    def specs(self, dropna_thresh=0, preview_row_count=5000):
        """
        preview_row_count: load nrows of file.
        dropna_thresh: 0.7 would remove
        columns where < 70% of the rows are NaN
        """
        if not 0 <= dropna_thresh <= 1:
            return 'dropna_thresh must be >= 0 but <= 1'
        self.df = pd.read_csv(self.fpath, nrows=preview_row_count, low_memory=False)
        self.df = self.df.dropna(axis=1, how='all', thresh=dropna_thresh * preview_row_count)
        print('%s column(s)' % self.df.shape[1])

        for col in self.df.columns:
            if len(self.df[col].unique()) <= 10:
                print(col, self.df[col].unique())


f = file('../TestData/npi.csv')
