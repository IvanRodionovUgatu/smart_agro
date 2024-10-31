from django.shortcuts import redirect, render

from .models import Field


def create_field(request):
    if request.method == 'POST':
        location_x = request.POST.get('location_x')
        location_y = request.POST.get('location_y')
        name = request.POST.get('name')  # Если у вас есть поле для ввода имени

        # Создание нового объекта Field
        field = Field(name=name, location_x=location_x, location_y=location_y)
        field.save()

        return redirect('success_url')  # Перенаправление после успешного сохранения

    return render(request, 'core.field.html')
