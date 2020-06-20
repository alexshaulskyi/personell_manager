from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

class DeleteMixin:

    model = None
    order_key = None
    template = None

    def post(self, request):

        obj = get_object_or_404(self.model, id=request.POST.get('object_id', ''))
        obj.delete()

        queryset = self.model.objects.filter(property_id=self.request.user.property_id).order_by(self.order_key)
        data = render_to_string(self.template, {'object_list': queryset})
        return JsonResponse({'data': data})