import pandas as pd
import os

#guess file size :https://softwareengineering.stackexchange.com/questions/204417/what-is-the-most-optimal-algorithm-for-counting-lines-of-text-in-a-file

class file:

    def __init__(self, fpath):
        self.fpath = fpath
        self.size = os.stat(fpath).st_size
        if self.size > 1000000000:
            print('File is larger than 1 GB')
        else:
            print('File smaller than 1 GB')

    def specs(self, dropna_thresh = 0, preview_row_count = 5000):
        """preview_row_count: load nrows of file.
        dropna_thresh: 0.7 would remove
        columns where < 70% of the rows are NaN
        """
        self.df = pd.read_csv(self.fpath, nrows = preview_row_count)
        self.df = self.df.dropna(axis=1, how='all',thresh = dropna_thresh * preview_row_count)
        print('%s column(s)' % self.df.shape[1])
        for col in self.df.columns:
            if len(self.df[col].unique()) <= 10:
                print(col, self.df[col].unique())

        
f = file('../TestData/npi.csv')
