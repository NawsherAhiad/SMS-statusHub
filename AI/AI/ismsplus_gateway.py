import cx_Oracle
import ora_ismsplus_con_base
import mysql.connector
import num_valid

def is_masking(STK, msisdn):
	result = ""
	SID = STK.upper()
	#print(SID)
	mydb = mysql.connector.connect(
				host="192.168.81.10",
				user="smsai",
				password="SmsAI12k!@%32",
				database="ismsplusdb"
	)
	mycursor = mydb.cursor()
	sql = "SELECT is_masking from stakeholders where name = %s"
	val = (SID,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchone()
	mycursor.close()
	print(Log)
	if Log[0] == 0:
		result = result + isms_non_mask(SID)
		#return result
	else:
		telco = num_valid.telco_name(msisdn)
		#print(telco_name)
		result = result + isms_mask(SID, telco)
		#print("Masking")
	return result


def isms_non_mask(SID):
    result = ""
    con = ora_ismsplus_con_base.isms_ora()
    cur = con.cursor()
    cur.execute("select outgoing_telco from BULKSMSPLUS.STAKEHOLDER_CTRL where stakeholder_uid = :1", [SID])
    rows = cur.fetchone()
    cur.close()
    con.close()
    #print(rows[0])
    if rows[0] == 'SSLTEL':
        result = result + "Gateway Disable for SID: "+SID +"\n"
    else:
        result = result + "Gateway Enabled for SID: "+SID +"\n"
    #print(result)
    return result

def isms_mask(SID, telco):
    result = ""
    #print(telco)
    con = ora_ismsplus_con_base.isms_ora()
    cur = con.cursor()
    cur.execute("select out_telco from BULKSMSPLUS.tbl_routing_table where request_from = :1 and in_telco = :2", [SID, telco])
    rows = cur.fetchone()
    cur.close()
    con.close()
    #print(rows)
    if rows[0] == 'SSLTEL':
        result = result + telco +" Gateway Disable for SID: "+SID +"\n"
    else:
        result = result + telco +" Gateway Enabled for SID: "+SID +"\n"
    #print(result)
    return result


#print(is_masking('OLWEL', '8801717418655'))


#print(isms_non_mask('CBL'))