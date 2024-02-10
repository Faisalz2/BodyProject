from django.http import HttpResponse
def BODY_name(request):
    name = request.GET.get("name") or 'Workout'
    return HttpResponse("This page displays information about {}".format(name))