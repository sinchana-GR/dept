from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.


def insert_dept(request):
    if request.method=='POST':
        dn=request.POST['dn']
        n=request.POST['n']
        l=request.POST['l']
        dt=Dept.objects.get_or_create(deptno=dn,dname=n,loc=l)[0]
        dt.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_dept.html')


def retrive_dept(request):
    rdo=Dept.objects.all()
    d={'rdo':rdo}
    if request.method=='POST':
        MSTS=request.POST.getlist('dn')
        print(MSTS)
        RWOS=Dept.objects.none()
        for i in MSTS:
            RWOS=RWOS|Dept.objects.filter(deptno=i)
        d1={'RWOS':RWOS}
        return render(request,'display_dept.html',d1)

    return render(request,'retrive_dept.html',d)

def update_dept(request):
    RWOS=Dept.objects.all()
    Dept.objects.filter(dname='accounting').update(loc='turkey')
    d={'RWOS':RWOS}

    return render(request,'display_dept.html',d)





def insert_emp(request):
    dn=Dept.objects.all()
    d={'dn':dn}
    if request.method=='POST':
        dn=request.POST['dn']
        en=request.POST['en']
        ena=request.POST['ena']
        j=request.POST['j']
        mg=request.POST['mg']
        hd=request.POST['hd']
        s=request.POST['s']
        c=request.POST['c']
        dt=Dept.objects.get(deptno=dn)
        dt.save()
        eo=Emp.objects.get_or_create(deptno=dt,empno=en,ename=ena,job=j,mgr=mg,hiredate=hd,sal=s,comm=c)[0]
        eo.save()

        return HttpResponse('data is inserted')
    



def retrive_emp(request):
    LDO=Dept.objects.all()
    d={'LDO':LDO}

    if request.method=='POST':
        MSTS=request.POST.getlist('dn')
        print(MSTS)
        RWOS=Emp.objects.none()
        for i in MSTS:
            RWOS=RWOS|Emp.objects.filter(deptno=i)
        d1={'RWOS':RWOS}
        return render(request,'display_emp.html',d1)
        
    
    return render(request,'retrive_emp.html',d)








