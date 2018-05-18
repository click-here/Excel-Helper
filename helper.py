import pandas as pd
import os
import profiler as pf
from split import split


# https://stackoverflow.com/a/312464
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class File:
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
        column_count = self.df.shape[1]

        print('%s column(s)' % column_count)

        chunked_columns = list(chunks(self.df.columns, 10))

        for chunk in chunked_columns:
            d = dict(enumerate(chunk))
            for k, v in d.items():
                print('[%s]' % k, v)

            col = input('Pick a column number > ')
            if col.lower() == 'q':
                break
            elif not col.isdigit():
                print('Must input a column number or "q" for quit')
                pass
            else:
                col = int(col)
                print('\n*50')  # clear the console
                print('Random sample of first %s lines of %s' % (preview_row_count, d[col]))
                print(self.df[d[col]].sample(20))
                break


f = File('../TestData/npi.csv')
f.specs(.7)
