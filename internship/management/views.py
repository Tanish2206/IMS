from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        loginprn = request.POST['prn']
        print(loginprn)
        loginpass = request.POST['pass']
        print(loginpass)

        user = Login.objects.filter(Loginid=loginprn, Password=loginpass)
        print(user)

        if user.exists():

            supervi = CollegeSuper.objects.filter(CO_email=loginprn)
            if supervi.exists():
                for i in supervi:
                    a = i.Co_id
                students = Student.objects.filter(SCO_id=a)
                return render(request, 'home.html', {'stu': students})
        else:
            return redirect('login')
    return render(request, 'login.html')


def details(request, id):
    detai = Student.objects.get(S_id=id)
    return render(request, 'details.html', {'det': detai})


def midterm(request, id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')
        mark7 = request.POST.get('mark7')

        sub = mideterm(domainandtech=mark1,
                       profesethi=mark2,
                       interpersonatl=mark3,
                       presentation=mark4,
                       communication=mark5,
                       taskcompleted=mark6,
                       questionans=mark7,
                       total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5)+int(mark6)+int(mark7),
                       SM_id=id)

        sub.save()
        detai = Student.objects.get(S_id=id)
        return render(request, 'details.html', {'det': detai})

    mid = mideterm.objects.filter(SM_id=id)
    if mid.exists():
        return render(request, 'midform.html')

    return render(request, 'midformdet.html', {'id': id})


def endterm(request,id):
    if request.method == 'POST':
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')
        mark7 = request.POST.get('mark7')
        mark8 = request.POST.get('mark8')
        mark9 = request.POST.get('mark9')
        mark10 = request.POST.get('mark10')

        sub = Endterm(background=mark1,
                       scopeandobj=mark2,
                       implemen=mark3,
                       observa=mark4,
                       domain=mark5,
                      presentation=mark6,
                       communic=mark7,
                       interper=mark8,
                       profess=mark8,
                        qanda=mark8,
                       E_total=int(mark1)+int(mark2)+int(mark3) +
                       int(mark4)+int(mark5)+int(mark6)+int(mark7)+int(mark8)+int(mark9)+int(mark10),
                       SE_id=id)

        sub.save()
        detai = Student.objects.get(S_id=id)
        return render(request, 'details.html', {'det': detai})

    end = Endterm.objects.filter(SE_id=id)
    if end.exists():
        return render(request, 'endform.html')

    return render(request, 'endformdet.html', {'id': id})