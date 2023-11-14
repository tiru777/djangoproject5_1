from django.shortcuts import render
from app.models import Employee
def home(requests):
    return render(requests,"home.html")

def list_data(requests):
    data = Employee.objects.all()
    return render(requests,'list_employee.html',context={"data":data})



