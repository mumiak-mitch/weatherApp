from django.shortcuts import render
from asgiref.sync import sync_to_async
from .requests import get_weather_data

async def weather_view(request):
    city = request.GET.get('city', 'Nairobi')
    weather_data = await sync_to_async(get_weather_data)(city)
    context = {'weather': weather_data}
    return render(request, 'index.html', context)
