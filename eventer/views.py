from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Address, Event
from .forms import EventForm
from django.views.decorators.csrf import csrf_exempt
#  displays all events on platform
def all_events(request):
    events=Event.objects.all()
    form=EventForm()
    return render(request,'all_events.html',context={"events":events,"form":form})

# adds a new event
def add_event(request):
    if request.method == 'POST':
        rq_form=EventForm(request.POST,request.FILES)
        if(rq_form.is_valid):
            print('entered')
            data=request.POST
            print(data['image'])
            address=Address.objects.get_or_create(
                address1=data['address1']
                ,address2=data['address1']
                ,zip_code=data['zip_code'],
                city=data['city']
            )
            print(request.FILES)
            event=Event.objects.get_or_create(
                name=data['name'],
                description=data['description'],
                date=data['date'],
                time=data['time'],
                location=address[0],
                image=data['image']
            )
            return HttpResponse(event,status=200)
        else:
            return HttpResponse("Unsuccessful",status=500)
    else:
        return HttpResponse("Unsuccessful",status=500)

# lists all liked events
def list_liked(request):
    events=Event.objects.all().filter(is_liked=True)
    return render(request,"liked.html",context={"events":events}) 

# likes a event
@csrf_exempt
def like_event(request):
    if request.method == 'GET':
        event_id = request.GET['event_id']
        event=Event.objects.get(id=event_id)
        event.is_liked=not event.is_liked
        event.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse("unsuccessful", status=500)




