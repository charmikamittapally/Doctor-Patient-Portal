from django.shortcuts import render
import pymysql

# Create your views here.
def doctorlogin(request):
  return render(request,'Doctor/login.html')
def doctorreg(request):
  return render(request,'Doctor/register.html')
def DoctorRegAction(request):
	name=request.POST['name']
	email=request.POST['email']
	mobile=request.POST['mobile']
	address=request.POST['address']
	username=request.POST['username']
	password=request.POST['password']
	specialist=request.POST['specialist']
	con=pymysql.connect(host="localhost", user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	i=cur.execute("insert into doctor values(null,'"+name+"','"+email+"','"+mobile+"','"+address+"','"+username+"','"+password+"','"+specialist+"')")
	con.commit()
	if i>0:
		context={'data':'Registration Successful...!!'}
		return render(request,'Doctor/register.html',context)
	else:
		context={'data','Registration Failed...!!'}
		return render(request,'Doctor/register.html',context)
def LogAction(request):
        user=request.POST.get('username')
        password=request.POST.get('password')
        con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
        cur=con.cursor()
        cur.execute("select * from doctor where username='"+user+"'and password='"+password+"'")
        data=cur.fetchone()
        if data is not None:
          request.session['user']=user
          request.session['id']=data[0]
          request.session['specialist']=data[7]
          return render(request,'Doctor/DoctorHome.html')
        else:
          context={'data':'Login Failed ....!!'}
          return render(request,'Doctor/login.html',context)
def viewrequest(request):
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	userid=str(request.session['userid'])
	specialist=request.session['specialist']
	cur.execute("select *  from bookslot where specialization='"+specialist+"'")
	data=cur.fetchall()
	strdata="<table border='1' style='margin-bottom:100px;'><tr><th>Specialization</th><th>Description</th><th>Booking Date</th><th>Booking Time</th><th>Status</th><th>Click To Confirm</th></tr>"
	for i in data:
		strdata+="<tr><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td><a href='/doctor/confirm?did="+str(i[0])+"&date="+str(i[4])+"&time="+str(i[5])+"'>Confirm</a></td></tr>"
	context={'data':strdata}
	return render(request,'Doctor/viewrequest.html',context)
def confirm(request):
	doctorid=request.GET['did']
	bdate=request.GET['date']
	btime=request.GET['time']
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	i=cur.execute("update bookslot set status='Confirmed' where id='"+doctorid+"'")
	con.commit()
	if i>0:
		context={'data':'Confirmed Successfully...!!'}
		return render(request,'Doctor/DoctorHome.html',context)
	else:
		context={'data':'Confirmation Failed...!!'}
		return render(request,'Doctor/DoctorHome.html',context)
def viewdonation(request):
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	cur.execute("select *  from donation")
	data=cur.fetchall()
	strdata="<table border='1'  style='margin-bottom:100px;'><tr><th>Donar</th><th>Organ name</th><th>Donated Date</th><th>Mobile</th><th>Description</th></tr>"
	for i in data:
		strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[5])+"</td><td>"+str(i[4])+"</td></tr>"
	context={'data':strdata}
	return render(request,'Doctor/ViewDonations.html',context)
