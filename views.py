from django.shortcuts import render,redirect
from django.http import HttpResponse 
from Myapp.models import Student

def sample(request):
	return HttpResponse("welcome to Django workshop")
# Create your views here.
def hello(request):
	return HttpResponse("<h2 style=background-color:blue;color:red;font-size:70px;font-style:italic>welcome django session</h2>")
def dynamic(request,id):
	return HttpResponse("<h2 style=background-color:blue;color:red;font-size:70px;font-style:italic>My Roll number is:{}</h2>".format(id))
def task(request,name):
	return HttpResponse("My name is:{}".format(name))
def home(request,id,name):
	return HttpResponse("My rollnumber is :{},My name is:{}".format(id,name))

def temp(request):
	return render(request,'Myapp/temp.html')

def table(request):
	return render(request,'Myapp/table.html')

def inline(request):
	return render(request,'Myapp/inline.html')

def internal(request):
	return render(request,'Myapp/internal.html')

def external(request):
	return render(request,'Myapp/external.html')

def boot(request):
	return render(request,'Myapp/boot.html')

def register(request):
	return render(request,'Myapp/register.html')

def offline(request):
	return render(request,'Myapp/offline.html')


def register1(request):
	if request.method=="POST":
		na=request.POST['name']
		num=request.POST['rollnum']
		age=request.POST['age']
		mob=request.POST['mobile']
		em=request.POST['email']
		addr=request.POST['address']
		Student.objects.create(name=na,rollnum=num,age=age,mobile=mob,email=em,address=addr)
		return HttpResponse("your data is submitted successfully")
		#return redirect('/details')
	return render(request,'Myapp/register1.html')







	

