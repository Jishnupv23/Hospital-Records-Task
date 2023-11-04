from .views import DepartmentView, DoctorView, DoctorDetailView, PatientView,PatientDetailView, PatientRecordsView,UserRegistrationView,UserLoginView,DeleteTokenView
from django.urls import path  
  
urlpatterns = [  
    path('departments/', DepartmentView.as_view()),
    path('doctors/', DoctorView.as_view()),
    path('doctors/<int:id>', DoctorDetailView.as_view()),
    path('patients/', PatientView.as_view()),
    path('patients/<int:id>', PatientDetailView.as_view()),
    path('patient_records/', PatientRecordsView.as_view()),
    path('department/<int:pk>/doctors', DepartmentView.as_view()),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('register/', UserRegistrationView.as_view(), name='register'),
    # path('logout/', DeleteTokenView.as_view(), name='logout'),
    

]  
