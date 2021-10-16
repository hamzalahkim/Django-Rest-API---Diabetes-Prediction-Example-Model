from django.shortcuts import render
from django.http import JsonResponse
from .apps import PimaConfig
# Create your views here.
from rest_framework.views import APIView



class call_model(APIView):

	def get(self, request):

		if request.method == 'GET':
			pregnancies =  request.GET.get('pregnancies')
			glucose =  request.GET.get('glucose')
			bloodpressure = request.GET.get('bloodpressure')
			skinthickness = request.GET.get('skinthickness')
			insulin = request.GET.get('insulin')
			bmi = request.GET.get('bmi')
			diabetespedigree = request.GET.get('diabetespedigree')
			age = request.GET.get('age')


			response = PimaConfig.predictor_model.predict([[6., 154.,  74.,  32., 193.,  29.3, 0.839, 39.]])[0]

			if response == 1:
				return JsonResponse({"result": 'The patient probably has diabetes'})
			if response == 0:
				return JsonResponse({"result": 'The patient probably doesnt have diabetes'})
