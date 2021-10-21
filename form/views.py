from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def student_list(request):
	context = {'student_list': Student.objects.all()}
	return render(request, "stundent_list.html", context)
def student_form(request,id=0):
	if request.method == "POST":
		if id == 0:
			name = request.POST.get('name')
			branch = request.POST.get('Branch')
			sapid = request.POST.get('Sapid')
			contact = request.POST.get('contactno')
			emailid = request.POST.get('email')
			details = Student(Name= name,Branch=branch,Sapid=sapid,contactno=contact,emailid=emailid)
			details.save()
			return render(request,"student_form.html")
		else:	
			student = Student.objects.get(pk=id)
			form = StudentForm(instance=student)
			return render(request, "student_form.html", {'form': form})
	else:
		if id == 0:
			form = StudentForm(request.POST)
		else:
			student = Student.objects.get(pk=id)
			form = StudentForm(request.POST,instance= student)
		if form.is_valid():
			form.save()
		return render(request,"student_form.html")

def student_delete(request,id):
	student = Student.objects.get(pk=id)
	student.delete()
	return redirect('list/')