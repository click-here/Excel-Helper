# guess file size : https://softwareengineering.stackexchange.com/q/204417

# https://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

# def fsize(file_path):
#     sizeof_fmt(self.size)
#     if self.size > 1000000000:
#         print('File is larger than 1 GB')
#     else:
#         print('File smaller than 1 GB')
