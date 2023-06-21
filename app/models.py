from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=50)
    loc=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.dname


class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    mgr=models.CharField(max_length=50)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    dept_id=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ename 
    