from django.shortcuts import render
import pymysql

# Create your views here.
def index(request):
  return render(request,'Patients/index.html')
def login(request):
  return render(request,'Patients/login.html')
def patientreg(request):
  return render(request,'Patients/register.html')
def PRegAction(request):
	name=request.POST['name']
	email=request.POST['email']
	mobile=request.POST['mobile']
	address=request.POST['address']
	username=request.POST['username']
	password=request.POST['password']
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient", charset='utf8')
	cur=con.cursor()
	i=cur.execute("insert into patient values(null,'"+name+"','"+email+"','"+mobile+"','"+address+"','"+username+"','"+password+"')")
	con.commit()
	if i>0:
		context={'data':'Registration Successful...!!'}
		return render(request,'Patients/register.html',context)
	else:
		context={'data','Registration Failed...!!'}
		return render(request,'Patients/register.html',context)
def LogAction(request):
  username=request.POST.get('username')
  password=request.POST.get('password')
  con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient", charset='utf8')
  cur=con.cursor()
  cur.execute("select *  from patient where username='"+username+"'and password='"+password+"'")
  data=cur.fetchone()
  if data is not None:
    request.session['user']=username
    request.session['userid']=data[0]
    return render(request,'Patients/PatientHome.html')
  else:
    context={'data':'Login Failed ....!!'}
    return render(request,'Patients/login.html',context)

def bookslot(request):
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient", charset='utf8')
	cur=con.cursor()
	cur.execute("select *  from Doctor")
	data=cur.fetchall()
	strdata="</tr><th>Select Doctor:</th><td><select name='doctor'>"
	for i in data:
          strdata+="<option value='"+str(i[7])+"'>"+str(i[1])+","+str(i[7])+"</option>"
	strdata+="</select></td></tr>"
	context={'data':strdata}
	return render(request,'Patients/ViewAllDoctors.html',context)
def BookAction(request):
	doctor=request.POST['doctor']
	content=request.POST['content']
	date=request.POST['date']
	time=request.POST['time']
	user=request.session['user']
	userid=str(request.session['userid'])
	conn=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient", charset='utf8')
	curr=conn.cursor()
	i=curr.execute("insert into bookslot values(null,'"+user+"','"+doctor+"','"+content+"','"+date+"','"+time+"','waiting','"+userid+"')")
	conn.commit()
	if i>0:
            context={'message':'Booking Successful...!!'}
            return render(request,'Patients/PatientHome.html',context)
	else:
            context={'message','Booking Failed...!!'}
            return render(request,'Patients/PatientHome.html',context)
def pviewslotstatus(request):
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient", charset='utf8')
	cur=con.cursor()
	userid=str(request.session['userid'])
	cur.execute("select *  from bookslot where patientid='"+userid+"'")
	data=cur.fetchall()
	strdata="<table border='1'  style='margin-bottom:100px;'><tr><th>Doctor Specialization</th><th>Description</th><th>Booking Date</th><th>Booking Time</th><th>Status</th></tr>"
	for i in data:
		strdata+="<tr><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td></tr>"
	context={'data':strdata}
	return render(request,'Patients/PViewBookingSlots.html',context)
def viewDonation(request):
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient", charset='utf8')
	cur=con.cursor()
	cur.execute("select *  from donation")
	data=cur.fetchall()
	strdata="<table border='1'  style='margin-bottom:100px;'><tr><th>Donar</th><th>Organ name</th><th>Donated Date</th><th>Mobile</th><th>Description</th></tr>"
	for i in data:
		strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[5])+"</td><td>"+str(i[4])+"</td></tr>"
	context={'data':strdata}
	return render(request,'Patients/ViewDonations.html',context)
