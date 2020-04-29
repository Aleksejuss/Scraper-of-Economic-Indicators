def cleaning_data(column_name):
    cleaning_data =  df[column_name].replace('', np.nan, inplace=True)
    cleaning_data =  df.dropna(subset=[column_name], inplace=True)
    return cleaning_data

def chg_type_and_cleaning_ch(column_name):
    df[column_name] = df[column_name].str.replace('%', '').str.replace('K', '').str.replace('B', '').str.replace('M', '').str.replace('T', '').str.replace('-', '').astype(float)
    return df[column_name]


def filtration(column_name1, criteria1, column_name2, criteria2):
    return df[df[column_name1].str.contains(criteria1) & df[column_name2].str.contains(criteria2)]
