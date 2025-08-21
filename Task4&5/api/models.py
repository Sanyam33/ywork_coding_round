from django.db import models
import uuid
# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    baseSal = models.IntegerField()
    depId = models.ForeignKey("Department",on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) +' '+self.name+' '+str(self.baseSal)+' '+str(self.depId)
    
class Department(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.id) +' '+self.name
    
class LeaveApplication:
    empId = models.ForeignKey("Employee", on_delete=models.CASCADE)
    month = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    leaves = models.IntegerField(default=0)
    
    def __str__(self):
        return self.empId +' '+self.month+' '+self.year+' '+self.leaves