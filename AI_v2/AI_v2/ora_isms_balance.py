import cx_Oracle
import ora_isms_con_base
import isms_gateway


def isms_blnc(SID, msisdn):
    result = ""
    con = ora_isms_con_base.isms_ora()
    cur = con.cursor()
    cur.execute("select sum(available_sms) from BULKUSER.TBL_STAKEHOLDER_CR_INFO where stakeholder_name = :1 AND status in ('RUNNING','BALANCE')", [SID])
    rows = cur.fetchone()
    cur.close()
    con.close()
    #sreturnrows[0])
    if rows[0] == 0 or rows[0] == None:
        result = result + "Balance 0 for the stakeholder: "+SID +"\n"
    else:
        result = result + isms_gateway.is_masking(SID, msisdn) +"\n"

    return result

def isms_blnc1(SID):
    result = ""
    conn = OracleDBConnection("smsai", "SmsAI12k32", "192.168.81.14", "1521", "PUSHCORE")
    #print(conn)
    cur = conn.connect()
    # Executing a query (make sure to create the appropriate table)
    rows = conn.execute_query("select sum(available_sms) from BULKUSER.TBL_STAKEHOLDER_CR_INFO where stakeholder_name = 'CBLCBS' AND status in ('RUNNING','BALANCE')")
    #sreturnrows[0])
    if rows[0] == 0 or rows[0] == None:
        result = result + "Balance 0 for the stakeholder: "+SID +"\n"
    else:
        result = result + "Goooooooooooooo..........." +"\n"
    conn.close_connection()

    return result


