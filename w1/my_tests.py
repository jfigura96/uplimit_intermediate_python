import os
import sys

# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current script
parent_directory = os.path.dirname(current_script_path)

# Add the parent directory to sys.path
sys.path.append(parent_directory)


from utils import DataReader
import constants
from global_utils import blockPrint, enablePrint
from pprint import pprint

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(CURRENT_FOLDER)


col_names = [constants.OutDataColNames.STOCK_CODE, constants.OutDataColNames.DESCRIPTION,
                constants.OutDataColNames.UNIT_PRICE, constants.OutDataColNames.QUANTITY,
                constants.OutDataColNames.TOTAL_PRICE, constants.OutDataColNames.COUNTRY,
                constants.OutDataColNames.INVOICE_NO, constants.OutDataColNames.DATE]

# blockPrint()
data_reader = DataReader(fp=os.path.join(CURRENT_FOLDER, '..', 'data', 'tst', '2015.csv'), sep=',',
                            col_names=col_names)


# print(data_reader._fp)
# def __iter__():
#     for n_row, row in enumerate(open(data_reader._fp, "r")):
#         row_vals = row.strip('\n').split(data_reader._sep)
#         temp_dict = {data_reader._col_names[i]: val for i, val in enumerate(row_vals)}
#         print(temp_dict)
#         yield temp_dict

# for i in data_reader.__iter__():
    # print(i)

data_gen = (row for row in data_reader.__iter__())
print(type(data_gen))
print(type(data_reader.__iter__()))
# for i in data_reader.__iter__():
#     print(i)

# for i in data_gen:
#     print(i)
# # print(data_gen)
# print('')
# print(next(data_gen))
# print('')
# print(next(data_gen))
# print('')
# print(next(data_gen))