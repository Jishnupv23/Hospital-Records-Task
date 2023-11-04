from .views import DepartmentView, DoctorView, DoctorDetailView, PatientView,PatientDetailView, PatientRecordsView,UserRegistrationView,UserLoginView,DeleteTokenView
from django.urls import path  
  
urlpatterns = [  
    path('departments/', DepartmentView.as_view(), name='departments'),
    path('doctors/', DoctorView.as_view(), name='doctors'),
    path('doctors/<int:id>', DoctorDetailView.as_view(), name='doctors'),
    path('patients/', PatientView.as_view(), name='patients'),
    path('patients/<int:id>', PatientDetailView.as_view(), name='patientsid'),
    path('patient_records/', PatientRecordsView.as_view(), name='patient_records'),
    path('department/<int:pk>/doctors', DepartmentView.as_view(), name='departmentdoctors'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', DeleteTokenView.as_view(), name='logout'),
    

]  