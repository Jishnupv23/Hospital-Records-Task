from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Department(models.Model):
    Name = models.CharField(max_length=200)
    Diagnostics = models.TextField()
    Location = models.CharField(max_length=200)
    Specialization = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.Name}"
    
    class Meta:
        verbose_name_plural = "Departments"

class Patient_Record(models.Model):
    Record_id = models.BigAutoField(primary_key=True)
    Patient_id = models.ForeignKey(User, verbose_name="Patient", related_name="patient", on_delete=models.CASCADE, limit_choices_to={"groups__name": 'Patients'})
    Doctor_id = models.ForeignKey(User, verbose_name="Doctor", related_name="doctor", on_delete=models.CASCADE, limit_choices_to={"groups__name": 'Doctors'})
    Created_date = models.DateTimeField(auto_now_add=True)
    Diagnostics = models.TextField()
    Observation = models.TextField()
    Treatments = models.TextField()
    Department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    Misc = models.TextField(verbose_name="Miscellaneous")
    


    def __str__(self):
        return f"{self.Created_date} - {self.Diagnostics} - {self.Treatments}"
    
    class Meta:
        verbose_name_plural = "Patient Records"

