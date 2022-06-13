# --*--coding : utf-8--*--

import pandas
import numpy
import matplotlib.pyplot as plt
import csv


class dataAnalysis:
    def __init__(self, file_name, js_date_file, js_data_file):
        self.file_name = file_name
        self.js_date_file = js_date_file
        self.js_data_file = js_data_file

    def get_row(self, df, column):
        (df[column].to_csv(self.file_name, index=False))

    def make_js_programing(self, column_num, file_name):
        write_file = open('../javascript/%s.js' % file_name, mode='w')
        with open(self.file_name) as reader_file:
            csv_reader = csv.reader(reader_file)
            write_file.write('date = [')
            row_count = 0
            for row in csv_reader:
                if row_count == 0:
                    row_count += 1
                    continue
                write_file.write(row[column_num]+',')
            write_file.write('];')
        write_file.close()

    def main(self):
        df = pandas.read_csv('GOOG.csv')
        column_list = df.columns
        print(numpy.max(df[column_list[1]]))
        print(df[df[column_list[1]] == numpy.max(df[column_list[1]])])
        self.get_row(df=df, column=[column_list[0], column_list[1]])
        self.make_js_programing(0, self.js_date_file)
        self.make_js_programing(1, self.js_data_file)


if __name__ == '__main__':
    main_process = dataAnalysis('open.csv', 'date_src', 'data_src')
    main_process.main()
