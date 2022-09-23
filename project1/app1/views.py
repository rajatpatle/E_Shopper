from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.
def EmployeeView(request):
    form = EmployeeForm()
    template_name = 'app1/hello.html'
    context = {'form':form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Data saved Successfully!!</h1>')
    return render(request, template_name, context)