from django.shortcuts import render
from .forms import FormEmployeeForm
from .models import Employee


def showempform(request):
    form = FormEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'Registration.html', context)




def display(request):

	emp=Employee.objects.all() # Collect all records from table
	return render(request,'display.html',{'emp':emp})









