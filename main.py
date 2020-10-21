import pandas as pd



def reviser(xl_file_name):
    try:
        df = pd.read_excel(xl_file_name, index_col=0)
        df = df[df.groupby('Structure Number')['_parent_index'].transform('max') == df['_parent_index']]
        df.to_excel("Revised " + xl_file_name)
        print("Revised excel file is created.")
    except pd.exceptions as e:
        return print(e)
    else:
        return True



if __name__ == '__main__':
    while(1):
        excel_file_name = input("Enter excel file name : ")
        reviser('Structure List TG.xlsx')

    # reviser('Structure List TG.xlsx')

