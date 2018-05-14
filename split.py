import os


def remove_chars(value):
    delete_chars = '\/:*?"<>|'
    for c in delete_chars:
        value = str(value).replace(c, '')
    return value


def split(df, column_name, output_dir=os.getcwd()):
    for item in df[column_name].unique():
        print('Processing ' + str(item) + '.csv')
        df[df[column_name] == item].to_csv(os.path.join(output_dir, str(remove_chars(item)) + '.csv'))
