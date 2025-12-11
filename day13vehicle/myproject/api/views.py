from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle
import json


@csrf_exempt
def vehicle(request):
    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Vehicle.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Vehicle.objects.create(
            number_plate=body["number_plate"],
            vehicle_type=body["vehicle_type"],
            manufacturer=body["manufacturer"],
            year=body["year"]

        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        pd = Vehicle.objects.get(id=body["id"])
        pd.number_plate = body["number_plate"]
        pd.vehicle_type = body["vehicle_type"]
        pd.manufacturer = body["manufacturer"]
        pd.year = body["year"]
        pd.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        pd = Vehicle.objects.get(id=body["id"])
        pd.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)