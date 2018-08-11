# coding:utf-8
import codecs
import time
import os
import csv
class DataOutput(object):
    def creat_new_file(self,filename,index_row):
        try:
            with open(filename,'w',newline='') as ff_csv:
                ff_writer = csv.writer(ff_csv)
                ff_writer.writerows(index_row)
        except Exception as e:
            print('creat_new_file:%s'%e)
    def creat_old_file(self,filename):
        try:
            ff_csv=open(filename,'w',newline='')
            ff_csv.close()
        except Exception as e:
            print('creat_old_file:%s'%e)

    def data_writerows(self,name,rows):
        try:
            with open(name,'a',newline='') as ff_csv:
                ff_writer = csv.writer(ff_csv)
                ff_writer.writerows(rows)
        except Exception as e:
            print('data_writerows:%s' % e)

    def data_writerow(self,name,row):
        try:
            with open(name,'a',newline='') as ff_csv:
                ff_writer = csv.writer(ff_csv)
                ff_writer.writerow(row)
        except Exception as e:
            print('data_writerow:%s'%e)



