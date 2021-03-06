import datetime as dt

from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View

from dashboard.mixins import DeleteMixin
from dashboard.forms import AddEmployee, CleaningCreate, RoomCreate
from dashboard.models import Hotel, Cleaning, Room
from users.models import User, title_choices

class Index(TemplateView):
    template_name = 'index.html'

#Employees section. Display, create and delete actions.
class EmployeeList(ListView):
    model = User
    template_name = 'employeelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tidentifier'] = self.kwargs.get('tidentifier')
        context['object_list'] = self.model.objects.filter(property_id=self.request.user.property_id).order_by('first_name')
        return context

    def dispatch(self, request, tidentifier):
        hotel = get_object_or_404(Hotel, slug=tidentifier)
        if request.user.works_for != hotel.name or request.user.property_id != hotel.property_id:
            return redirect('redirectprocessor')
        if request.user.job_title != 'MG':
            return redirect('dashboard', tidentifier=tidentifier)
        return super(EmployeeList, self).dispatch(request)

class CreateEmployee(View):

    def get(self, request):
        if not request.is_ajax():
            hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
            return redirect('dashboard', tidentifier=hotel.slug)
        data = dict()
        form = AddEmployee()
        context = {'form': form}
        data.update({'html_form': render_to_string('partial_employee_create.html', context, request=request)})
    
        return JsonResponse(data)

    def post(self, request):
        data = dict()
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.works_for = request.user.works_for
            form.instance.property_id = request.user.property_id
            form.save()
            data.update({'form_is_valid': True})

            employees = User.objects.filter(property_id=request.user.property_id).order_by("first_name")
            data.update({'html_employee_list': render_to_string('partial_employeelist.html', {'object_list': employees})})
        else:
            data.update({'form_is_valid': False})
        
        return JsonResponse(data)

class DeleteEmployee(DeleteMixin, View):

    model = User
    order_key = 'first_name'
    template = 'partial_employeelist.html'

#Cleaning section. Display, create and delete actions.

class CleaningList(ListView):
    model = Cleaning
    template_name = 'cleaninglist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tidentifier'] = self.kwargs.get('tidentifier')
        context['object_list'] = self.model.objects.filter(property_id=self.request.user.property_id).order_by('name')
        return context

    def dispatch(self, request, tidentifier):
        hotel = get_object_or_404(Hotel, slug=tidentifier)
        if request.user.works_for != hotel.name or request.user.property_id != hotel.property_id:
            return redirect('redirectprocessor')
        if request.user.job_title != 'MG':
            return redirect('dashboard', tidentifier=tidentifier)
        return super(CleaningList, self).dispatch(request)

class CreateCleaning(View):

    def get(self, request):
        if not request.is_ajax():
            hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
            return redirect('dashboard', tidentifier=hotel.slug)
        data = dict()
        form = CleaningCreate()
        context = {'form': form}
        data.update({'html_form': render_to_string('partial_cleaning_create.html', context, request=request)})
    
        return JsonResponse(data)

    def post(self, request):
        data = dict()
        hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
        form = CleaningCreate(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.property_id = request.user.property_id
            form.instance.hotel = hotel
            form.save()
            data.update({'form_is_valid': True})

            cleanings = Cleaning.objects.filter(property_id=request.user.property_id).order_by("name")
            data.update({'html_cleaning_list': render_to_string('partial_cleaninglist.html', {'object_list': cleanings})})
        else:
            data.update({'form_is_valid': False})
        
        return JsonResponse(data)

class DeleteCleaning(DeleteMixin, View):

    model = Cleaning
    order_key = 'name'
    template = 'partial_cleaninglist.html'

#Dashboard section. Display, create and delete actions.

class Dashboard(View):

    def get(self, request, tidentifier):
        hotel = Hotel.objects.get(slug=tidentifier)
        if not request.user.is_authenticated or request.user.works_for != hotel.name or request.user.property_id != hotel.property_id:
            return redirect('index')
        if request.user.job_title in ['MG', 'AD']:
            rooms = Room.objects.filter(property_id=request.user.property_id).order_by('number')
        else:
            rooms = Room.objects.filter(property_id=request.user.property_id, maid_id=request.user.id).order_by('number')
        return render(request, 'dashboard.html', {'object_list': rooms, 'hotel': hotel, 'tidentifier': tidentifier})

class CreateRoom(View):

    def get(self, request):
        if not request.is_ajax():
            hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
            return redirect('dashboard', tidentifier=hotel.slug)
        data = dict()
        form = RoomCreate()
        hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
        form.fields["building"].queryset = hotel.buildings.all()
        context = {'form': form}
        data.update({'html_form': render_to_string('partial_room_create.html', context, request=request)})
    
        return JsonResponse(data)

    def post(self, request):
        data = dict()
        hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
        form = RoomCreate(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.hotel = hotel
            form.instance.property_id = request.user.property_id
            form.save()
            data.update({'form_is_valid': True})

            rooms = hotel.rooms.all().order_by('number')
            data.update({'html_room_list': render_to_string('partial_roomlist.html', {'object_list': rooms})})
        else:
            data.update({'form_is_valid': False})
        
        return JsonResponse(data)

class DeleteRoom(DeleteMixin, View):

    model = Room
    order_key = 'number'
    template = 'partial_roomlist.html'

""" Dynamic select boxes are those which modify only
foreign key fields."""

class UpdateDynamicSelectBox(View):

    def get(self, request):

        if not request.is_ajax():
            hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
            return redirect('dashboard', tidentifier=hotel.slug)

        model_name = request.GET.get('options_model_name', '') #Name of a model selected options belongs to
        order_key = request.GET.get('order_key', '') #Value to order queryset

        if request.user.job_title == 'ST':
            data = {'error': 'У вас недостаточно прав для совершения данного действия'}
            return JsonResponse(data)

        if model_name == 'User':
            model = apps.get_model('users', model_name)
            queryset = model.objects.filter(property_id=request.user.property_id).exclude(job_title__in=['MG', 'AD']).order_by(order_key)
            data = {'data': [{'object_id': obj.id, 'object_text': f'{obj.first_name} {obj.last_name}'} for obj in queryset]}
            data['None'] = 'Не назначено'
            return JsonResponse(data)
        model = apps.get_model('dashboard', model_name)
        queryset = model.objects.filter(property_id=request.user.property_id).order_by(order_key)
        data = {'data': [{'object_id': obj.id, 'object_text': obj.name} for obj in queryset]}
        data['None'] = 'Не назначено'
        return JsonResponse(data)

    def post(self, request):

        if not 'set_none' in request.POST:
            selected_option_object_id = request.POST.get('selected_option_object_id', '') #Id of a newly selected object (new object to be related to a model which is being changed)
        selected_option_model = request.POST.get('selected_option_object_model', '') #Model of a newly selected object
        model_name = request.POST.get('model_name', '') #Name of a model which newly selected object is related to (model of an object which is actually being changed)
        model_field_name = request.POST.get('model_field_name', '') # Name of a field which is being changed
        model_instance_id = request.POST.get('model_instance_id', '') # Id of an object which is being changed


        if selected_option_model == 'User':
            new_object_model = apps.get_model('users', selected_option_model) #Retrieving model of the selected option object for User objects
        else:
            new_object_model = apps.get_model('dashboard', selected_option_model) #Retrieving model of the selected option object for other objects
        if not 'set_none' in request.POST:
            new_object = get_object_or_404(new_object_model, id=selected_option_object_id) #Retrieving newly selected object
        else:
            new_object = None
        update_object_model = apps.get_model('dashboard', model_name) #Retrieving model of an object which is being updated
        update_object = get_object_or_404(update_object_model, id=model_instance_id) #Retrieving object which is being updated
        setattr(update_object, model_field_name, new_object)

        update_object.save()

        if selected_option_model == 'User':
            if 'set_none' in request.POST:
                data = {'object_text': 'Не назначено', 'object_id': None}
            else:
                data = {'object_text': f'{new_object.first_name} {new_object.last_name}', 'object_id': new_object.id}
            return JsonResponse(data)

        else:
            if 'set_none' in request.POST:
                data = {'object_text': 'Не назначено', 'object_id': None}
            else:
                data = {'object_text': new_object.name, 'object_id': new_object.id}
        return JsonResponse(data)

""" Following class is responsible for updating regular input
fields and static (options are not dependant on request.user)
select boxes """

class UpdateStaticFieldsAndSelectElements(View):

    def get(self, request):
        
        hotel = get_object_or_404(Hotel, property_id=request.user.property_id)
        return redirect('dashboard', tidentifier=hotel.slug)


    def post(self, request):

        new_value = request.POST.get('new_value', '')
        model_name = request.POST.get('model_name', '')
        model_field_name = request.POST.get('model_field_name', '')
        model_instance_id = request.POST.get('model_instance_id', '')

        if request.user.job_title == 'ST' and model_field_name != 'status':
            data = {'error': 'У вас не достаточно прав для совершения данного действия'}
            return JsonResponse(data)

        if model_name == 'User':
            update_object_model = apps.get_model('users', model_name)
        else:
            update_object_model = apps.get_model('dashboard', model_name)
        
        update_object = get_object_or_404(update_object_model, id=model_instance_id)

        if new_value == '':
            if model_field_name in ['checkin_date', 'checkout_date']:
                setattr(update_object, model_field_name, None)
            else:
                data = {'error': 'Это поле не может быть пустым, изменения не будут применены'}
                return JsonResponse(data)
        else:
            setattr(update_object, model_field_name, new_value)
        update_object.save()

        data = {'object_text': getattr(update_object, model_field_name)}

        return JsonResponse(data)

class DeleteEmployee(DeleteMixin, View):

    model = User
    order_key = 'first_name'
    template = 'partial_employeelist.html'

def processor(request):
    property_id = request.user.property_id
    if not Hotel.objects.filter(property_id=property_id).exists():
        return redirect('index')
    hotel = get_object_or_404(Hotel, property_id=property_id)
    slug = hotel.slug
    return redirect('dashboard', tidentifier=slug)

class CleaningAssigner(View):

    def get(self, request, tidentifier):
        
        return redirect('dashboard', tidentifier=tidentifier)

    def post(self, request, tidentifier):

        if request.user.job_title == 'ST':
            data = {'error': 'У вас недостаточно прав для совершения этого действия'}
            return JsonResponse(data)
        
        rooms = Room.objects.filter(property_id=request.user.property_id)
        
        for room in rooms:
            if room.checkin_date:

                difference = dt.datetime.now().date() - room.checkin_date
                int_difference = difference.days
                if Cleaning.objects.filter(property_id=request.user.property_id, frequency=int_difference).exists():
                    
                    cleaning = Cleaning.objects.get(property_id=request.user.property_id, frequency=int_difference)
                    room.cleaning_type=cleaning
                    room.save()
                
                else:
                    
                    pass
                
            else:

                room.cleaning_type=None
                room.save()
        
        rooms = Room.objects.filter(property_id=request.user.property_id).order_by('number')
        data = {'html_room_list': render_to_string('partial_roomlist.html', {'object_list': rooms})}
        return JsonResponse(data)