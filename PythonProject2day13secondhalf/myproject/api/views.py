from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json


@csrf_exempt
def product(request):
    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Product.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Product.objects.create(
            name=body["name"],
            price=body["price"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        pd = Product.objects.get(id=body["id"])
        pd.name = body["name"]
        pd.price = body["price"]
        pd.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        pd = Product.objects.get(id=body["id"])
        pd.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)