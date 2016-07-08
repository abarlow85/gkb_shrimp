from django.shortcuts import render
from django.http import JsonResponse
from .models import BikeOption, BrandOption, CosmeticOption, FeaturesOption, FrameOption, WheelOption, Bike
import requests


# Create your views here.
def home(request):
	return render(request, 'donations/index.html')

def form_data(request):
	context = {
		'bikeType' : serialize_selections(BikeOption.objects.all().values()),
		'wheels' : serialize_selections(WheelOption.objects.all().values()),
		'brand' : serialize_selections(BrandOption.objects.all().values()),
		'cosmetic' : serialize_selections(CosmeticOption.objects.all().values()),
		'frame' : serialize_selections(FrameOption.objects.all().values()),
		'features' : serialize_selections(FeaturesOption.objects.all().values())
	}
	return JsonResponse(context)


def serialize_selections(query_set):
	data = {}

	for obj in query_set:
		data[obj['option']] = {'status' : False, 'price_factor' : obj['price_factor']}

	return data 

def get_inv(request):
	url = 'https://api.merchantos.com/API/Account/132193/Item.json'
	auth = ('22dabb44da10a0d29347905309fd40dc5ad88bc3683927bb6be0d2142ba7c90b', 'apikey')
	inventory = requests.get(url, auth=auth)
	print inventory.content

	return JsonResponse(inventory.content, safe=False)