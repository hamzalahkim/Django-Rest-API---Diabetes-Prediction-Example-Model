from django.shortcuts import render
from django.http import JsonResponse
from .apps import PimaConfig
# Create your views here.
from rest_framework.views import APIView
from .models import Patient


class Callmodel(APIView):

	def get(self, request):

		if request.method == 'GET':
			name = request.GET.get('name')
			assert isinstance(name, str)
			pregnancies =  int(request.GET.get('pregnancies'))
			glucose =  float(request.GET.get('glucose'))
			bloodpressure = float(request.GET.get('bloodpressure'))
			skinthickness = float(request.GET.get('skinthickness'))
			insulin = float(request.GET.get('insulin'))
			bmi = float(request.GET.get('bmi'))
			diabetespedigree = float(request.GET.get('diabetespedigree'))
			age = int(request.GET.get('age'))

			response = PimaConfig.predictor_model.predict([[6., 154.,  74.,  32., 193.,  29.3, 0.839, 39.]])[0]

			patient = Patient()
			patient.name, patient.pregnancies, patient.glucose, patient.bloodpressure, patient.skinthickness, patient.insulin, patient.bmi, patient.diabetespedigree, patient.age, patient.diagnosis  = name, pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age, bool(response)
			patient.save()

			if response == 1:
				return JsonResponse({"result": 'The patient probably has diabetes'})
			if response == 0:
				return JsonResponse({"result": 'The patient probably doesnt have diabetes'})

class Requestdb(APIView):

	def get(self, request):
		if request.method == 'GET':

			_id = request.GET.get('id')

			try:
				patient = Patient.objects.get(id=_id)
				return JsonResponse({'patient name': patient.name, 'patient diagnosis': 'The patient probably has diabetes' if patient.diagnosis else 'The patient probably does not have diabetes'})

			except:
				return JsonResponse({'Error': 'The patient id does not exist'})
		

