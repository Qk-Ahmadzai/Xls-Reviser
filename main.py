import pandas as pd

structure_number = "Structure Number"
parent_index = "_parent_index"


def reviser(xl_file_name):
    df = pd.read_excel(xl_file_name, index_col=0)
    df = df[df.groupby(structure_number)[parent_index].transform('max') == df[parent_index]]

    df.to_excel("Revised " + xl_file_name)
    print("Revised excel file is created.")


if __name__ == '__main__':
    while True:
        excel_file_name = input("Enter excel file name : ")
        reviser(excel_file_name)

    # reviser('Structure List TG.xlsx')

