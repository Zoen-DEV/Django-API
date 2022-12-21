from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

# Create your views here.

class UserView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # GET request
    def get(self,request,id=0):
        if id>0:
            user = list(User.objects.filter(id=id).values())
            if len(user) > 0:
                datos={'message':"Success", 'User': user[0]}
            else:
                datos={'message':"This user doesn't exist"}
            return JsonResponse(datos)
        else:
            users = list(User.objects.values())
            if len(users)>0:
                datos={'message':"Success", 'Users':users}
            else:
                datos={'message':"Any user to show", 'Users': len(users)}
            return JsonResponse(datos)
    
    # POST request
    def post(self,request):
        res = json.loads(request.body)
        User.objects.create(
            name=res['name'],
            website=res['website'],
            founded=res['founded']
        )
        datos={'message':"User registered successfully"}
        return JsonResponse(datos)
    
    # PUT request
    def put(self,request,id):
        res = json.loads(request.body)
        user = list(User.objects.filter(id=id).values())[0]
        if len(user) > 0:
            user = User.objects.get(id=id)
            user.name=res['name']
            user.website=res['website']
            user.save()
            datos={'message':"Success"}
        else:
            datos = {'message':"This user doesn't exist"}
        return JsonResponse(datos)
    
    # DELETE request
    def delete(self,request,id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.get(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message': "This user doesn't exist"}
        return JsonResponse(datos)