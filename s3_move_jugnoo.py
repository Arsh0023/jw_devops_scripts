import os
import sys
import subprocess

#mysqldump -uroot -pqR7BPkadHJCvsorS --databases jugnoo_analytics --tables tb_jugnootaxi_livepanel_five --where="timing >= '{start_date} 00:00:00' AND timing < '{end_date} 00:00:00'" > /apps/jugnoo_analytics_2019-07-30-2019-08-03.sql

start_date = sys.argv[1]
end_date = sys.argv[2]


def get_ouput(command):
    '''Runs the command in linux terminal and returns the output'''
    output = subprocess.getoutput(command)
    return output

if __name__ == '__main__':
    command = f"mysqldump -uroot -pqR7BPkadHJCvsorS --databases jugnoo_analytics --tables tb_jugnootaxi_livepanel_five --where=\"timing >= '{start_date} 00:00:00' AND timing < '{end_date} 00:00:00'\" > /apps/jugnoo_analytics_FROM_{start_date}_to_{end_date}.sql"
    #print(get_ouput(command))
    print(command)
