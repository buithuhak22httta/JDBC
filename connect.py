from unittest import result
import jaydebeapi
from contextlib import closing
import pandas as pd
import csv
import sys

jdbc_driver_name = "com.netsuite.jdbc.openaccess.OpenAccessDriver"
jdbc_driver_loc = "C:\\Program Files (x86)\\NetSuite\\NetSuite JDBC Drivers\\NQjc.jar"

url = "jdbc:ns://4975572.connect.api.netsuite.com:1708;ServerDataSource=NetSuite2.com;Encrypted=1;CustomProperties=(AccountID=4975572;RoleID=1153)"
login = "minh.le@vuanem.com"
psw = "BI.vuanem$123"

sql = "SELECT * FROM  classification"

conn = jaydebeapi.connect(jdbc_driver_name, url, [login, psw], jdbc_driver_loc)


with closing(conn) as conn:
    with closing(conn.cursor()) as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        column_names = [i[0] for i in cur.description]
        fp = open('Result_Set.csv','w', encoding="utf-8")
        myFile = csv.writer(fp, lineterminator = '\n') #use lineterminator for windows
        myFile.writerow(column_names)
        myFile.writerows(rows)
        fp.close()


# if rows:        
#     result = list()
#     column_names = list()
#     for i in cur.description:
#         column_names.append(i[0])

#     result.append(column_names)

#     for row in rows:
#         result.append(row)
#         results = pd.Series(result)
            
#     with open('G:\DE\JDBC\DataClasses.csv', 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         for row in results:
#             csvwriter.writerow(row)    

# else:
#     sys.exit("No rows found for query: {}".format(sql))        
