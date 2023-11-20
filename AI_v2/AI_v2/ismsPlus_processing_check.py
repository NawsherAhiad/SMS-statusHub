import datetime
import mysql.connector
import chk_reporting
import ora_ismsplus_balance



def isms_bulklog(msisdn, fsendtime, tsendtime):
	result = ""
	mydb = mysql.connector.connect(
				host="192.168.91.150",
				user="smsai",
				password="SmsAI12k!@%32",
				database="bulkinfoplus"
	)
	mycursor = mydb.cursor()
	sql = "SELECT USER, msisdn, in_time, response, status_code FROM `bulksms_log` WHERE msisdn = %s and DATE(in_time) Between %s and %s ORDER BY in_time DESC"
	val = ('88'+msisdn, fsendtime, tsendtime,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	print("ismsplus log",Log)
	#Sprint("new")
	#return Log[0]
	len(Log)
	for x in Log:
		print(x)
		if str(x[4]) == "1":
			result = result + chk_reporting.chk_report(msisdn, str(x[2]))
			#print("tarpor", result)
			result = result + "Stakeholder:  "+x[0]+ " SMS for MSISDN: "+msisdn+" is Successful! at "+str(x[2])+"\n"
		else:
			res = str(x[3])
			#return res)
			response = res[:16]
			
			if response =='Response : FAIL|':
				
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				print("ismsplus success hoile result: ", result)
				#return str(x[2]))
			else:
				#return x[0])
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				result = result + ora_ismsplus_balance.isms_blnc(x[0], msisdn)
				print(" isms plus success hoile : ", result)
				break
	val = (msisdn, fsendtime, tsendtime,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	#return Log)
	#return Log[0]
	for x in Log:
		if str(x[4]) == "1":
			result = result + chk_reporting.chk_report(msisdn, str(x[2]))
			result = result + "Stakeholder: "+x[0]+ " SMS for MSISDN: "+msisdn+" is Successful! at "+str(x[2]) +"\n"
		else:
			res = str(x[3])
			#return res)
			response = res[:16]
			if response =='Response : FAIL|':
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				
			else:
				#return x[0])
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				result = result + ora_ismsplus_balance.isms_blnc(x[0], msisdn)
				break
	val = (msisdn[3:], fsendtime, tsendtime,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	#return Log)
	#return Log[0]
	for x in Log:
		if str(x[4]) == "1":
			result = result + chk_reporting.chk_report(msisdn, str(x[2]))
			result = result + "Stakeholder: yo"+x[0]+ " SMS for MSISDN: "+msisdn+" is Successful! at "+str(x[2]) +"\n"
		else:
			res = str(x[3])
			#return res)
			response = res[:16]
			if response =='Response : FAIL|':
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				#return str(x[2]))
			else:
				#return x[0])
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				result = result + ora_ismsplus_balance.isms_blnc(x[0], msisdn)
				break
	return result

