import cx_Oracle
import sys
import os
import oracledb

def isms_ora():
    user = "smsai"
    dns = '192.168.81.30:1521/PUSHCORE'
    pw = 'SmsAI12k32'

    return oracledb.connect(user = user, password = pw, dsn = dns)

    
