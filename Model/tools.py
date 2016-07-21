#column names
def print_columns(dataframe):
    i = 0
    for column in dataframe.columns:
        print((i, column))
        i += 1