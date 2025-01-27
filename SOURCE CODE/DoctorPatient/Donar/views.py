from django.shortcuts import render
import pymysql

# Create your views here.

def donarlogin(request):
  return render(request,'Donar/login.html')
def donarreg(request):
  return render(request,'Donar/register.html')
def PRegAction(request):
	name=request.POST['name']
	email=request.POST['email']
	mobile=request.POST['mobile']
	address=request.POST['address']
	username=request.POST['username']
	password=request.POST['password']
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	i=cur.execute("insert into donar values(null,'"+name+"','"+email+"','"+mobile+"','"+address+"','"+username+"','"+password+"')")
	con.commit()
	if i>0:
		context={'data':'Registration Successful...!!'}
		return render(request,'Donar/register.html',context)
	else:
		context={'data','Registration Failed...!!'}
		return render(request,'Donar/register.html',context)
def LogAction(request):
  username=request.POST.get('username')
  password=request.POST.get('password')
  request.session['user']=username
  request.session['username']=username
  con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
  cur=con.cursor()
  cur.execute("select * from donar where username='"+username+"'and password='"+password+"'")
  data=cur.fetchone()
  if data is not None:
    request.session['user']=username
    request.session['userid']=data[0]
    return render(request,'Donar/DonarHome.html')
  else:
    context={'data':'Login Failed ....!!'}
    return render(request,'Donar/login.html',context)

def donateorgan(request):
	return render(request,'Donar/DonateOrgan.html')
def donateorganaction(request):
	name=request.POST['name']
	organname=request.POST['organname']
	date=request.POST['date']
	description=request.POST['description']
	mobile=request.POST['mobile']
	userid=str(request.session['userid'])
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	i=cur.execute("insert into donation values(null,'"+name+"','"+organname+"','"+date+"','"+description+"','"+mobile+"','"+userid+"')")
	con.commit()
	if i>0:
		context={'data':'Donation Successful...!!'}
		return render(request,'Donar/DonateOrgan.html',context)
	else:
		context={'data','Donation Failed...!!'}
		return render(request,'Donar/DonateOrgan.html',context)
def viewmydonation(request):
	con=pymysql.connect(host="localhost",user="root",password="root",port=3306,database="doctor-patient",charset='utf8')
	cur=con.cursor()
	userid=str(request.session['userid'])
	cur.execute("select *  from donation where donarid='"+userid+"'")
	data=cur.fetchall()
	strdata="<table border='1'  style='margin-bottom:100px;'><tr><th>Donar</th><th>Organ name</th><th>Donated Date</th><th>Mobile</th><th>Description</th></tr>"
	for i in data:
		strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[5])+"</td><td>"+str(i[4])+"</td></tr>"
	context={'data':strdata}
	return render(request,'Donar/MyDonations.html',context)
