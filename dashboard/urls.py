from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Index, PropertyCreate, CleaningCreate, CreateEmployee, EmployeeList, CreateCleaning, CreateRoom, UpdateDynamicSelectBox, UpdateStaticFieldsAndSelectElements, DeleteEmployee, CleaningList, DeleteCleaning, Dashboard, DeleteRoom
from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('propertycreate/', PropertyCreate.as_view(), name='property_create'),
    path('redirectprocessor/', views.processor, name='redirectprocessor'),
    path('dashboard/updatedynamicvalue/', UpdateDynamicSelectBox.as_view(), name='ajax_update_dynamic_value'),
    path('dashboard/updatestaticvalue/', UpdateStaticFieldsAndSelectElements.as_view(), name='ajax_update_static_value'),
    path('dashboard/deleteemployee/', DeleteRoom.as_view(), name='ajax_delete_room'),
    path('dashboard/addemployee/', CreateEmployee.as_view(), name='ajax_create_employee'),
    path('dashboard/addcleaning/', CreateCleaning.as_view(), name='ajax_create_cleaning'),
    path('dashboard/addroom/', CreateRoom.as_view(), name='ajax_create_room'),
    path('dashboard/deleteroom/', DeleteCleaning.as_view(), name='ajax_delete_cleaning'),
    path('dashboard/deletecleaning/', DeleteCleaning.as_view(), name='ajax_delete_cleaning'),
    path('dashboard/<slug:tidentifier>/', Dashboard.as_view(), name='dashboard'),
    path('dashboard/<slug:tidentifier>/employeelist/', EmployeeList.as_view(), name='employeelist'),
    path('dashboard/<slug:tidentifier>/cleaninglist/', CleaningList.as_view(), name='cleaninglist'), 
]