import datetime
import mysql.connector
import chk_reporting
import ora_isms_balance



def block_msisdn(msisdn):
	result = ""
	mydb = mysql.connector.connect(
				host="192.168.81.10",
				user="smsai",
				password="SmsAI12k!@%32",
				database="ismsplusdb"
	)
	mycursor = mydb.cursor()
	sql = "SELECT block_status, in_time, stakeholder, update_time FROM `block_multiple` WHERE msisdn = %s"
	val = (msisdn,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	#print(Log)
	for x in Log:
		if str(x[0]) == "1":
			result = result + "MSISDN: "+msisdn+" is BLOCKED for the SID: "+x[2]+" at "+str(x[1])+"\n"
		elif str(x[0]) == "2":
			result = "MSISDN: "+msisdn+" is UNBLOCKED for the SID: "+x[2]+" at "+str(x[3])+"\n"

			break
	return result


