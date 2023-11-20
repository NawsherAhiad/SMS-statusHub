import cx_Oracle
import sys
import os
import oracledb

def isms_ora2():
    try:
        #cx_Oracle.init_oracle_client(lib_dir="C:\\oml4rclient_install_dir\\instantclient_12_2")
        cx_Oracle.init_oracle_client(lib_dir="/Users/root/downloads/instantclient_19_8")
    except Exception as err:
        print("Whoops!")
        print(err)
        sys.exit(1)
    return cx_Oracle.connect('smsai/SmsAI12k32@192.168.81.14:1521/PUSHCORE')


def isms_ora3():
    try:
        #cx_Oracle.init_oracle_client(lib_dir="C:\\oml4rclient_install_dir\\instantclient_12_2")
        cx_Oracle.init_oracle_client(lib_dir="/Users/root/downloads/instantclient_19_8")
    except Exception as err:
        print("Whoops!")
        print(err)
        sys.exit(1)
    return cx_Oracle.connect("smsai", "SmsAI12k32", "ismsdemo")


def isms_ora():
    user = "smsai"
    dns = '192.168.81.14:1521/PUSHCORE'
    pw = 'SmsAI12k32'

    return oracledb.connect(user = user, password = pw, dsn = dns)

    
