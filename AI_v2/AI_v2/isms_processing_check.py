import datetime
import mysql.connector
import chk_reporting
import ora_isms_balance



def isms_bulklog(msisdn, fsendtime, tsendtime):
	result = "SMS Response: \n"
	mydb = mysql.connector.connect(
				host="192.168.91.150",
				user="smsai",
				password="SmsAI12k!@%32",
				database="bulkinfo"
	)
	mycursor = mydb.cursor()
	sql = "SELECT USER, msisdn, in_time, response, status_code FROM `bulksms_log` WHERE msisdn = %s and DATE(in_time) Between %s and %s ORDER BY in_time DESC"
	val = ('88'+msisdn, fsendtime, tsendtime,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	len(Log)
	print("log: isms processing check ",str(Log))
	#print("old")
	#return Log[0]
	for x in Log:
		print(str(x[2]))
		if str(x[4]) == "1":
			print("bla bla",chk_reporting.chk_report(msisdn, str(x[2])))
			result = result + chk_reporting.chk_report(msisdn, str(x[2]))
			result = result + "Stakeholder: yo1"+x[0]+ " SMS for MSISDN: "+msisdn+" is Successful! at "+str(x[2])+"\n"
		else:
			res = str(x[3])
			#return res)
			response = res[:16]
			if response =='Response : FAIL|':
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				print("isms failed hoile : ", result)
				#return str(x[2]))
			else:
				#return x[0])
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				result = result + ora_isms_balance.isms_blnc(x[0], msisdn)
				print("isms success hoile : ", result)
				break
	val = (msisdn, fsendtime, tsendtime,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	#return Log)
	#return Log[0]
	for x in Log:
		if str(x[4]) == "1":
			result = result + chk_reporting.chk_report(msisdn, str(x[2]))
			result = result + "Stakeholder: yo2"+x[0]+ " SMS for MSISDN: "+msisdn+" is Successful! at "+str(x[2]) +"\n"
		else:
			res = str(x[3])
			#return res)
			response = res[:16]
			if response =='Response : FAIL|':
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				print("check reprot", result)
			else:
				#return x[0])
				result = result + chk_reporting.chk_report(msisdn, str(x[2]))
				result = result + ora_isms_balance.isms_blnc(x[0], msisdn)
				break
	val = (msisdn[3:], fsendtime, tsendtime,)
	mycursor.execute(sql, val)
	Log=mycursor.fetchall()
	#return Log)
	#return Log[0]
	for x in Log:
		if str(x[4]) == "1":
			result = result + chk_reporting.chk_report(msisdn, str(x[2]))
			result = result + "Stakeholder: yo3"+x[0]+ " SMS for MSISDN: "+msisdn+" is Successful! at "+str(x[2]) +"\n"
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
				result = result + ora_isms_balance.isms_blnc(x[0], msisdn)
				break
	print("isms processing check result ",result)
	return result

