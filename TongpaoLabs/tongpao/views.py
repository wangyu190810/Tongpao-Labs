from django.shortcuts import render_to_response
from tongpao.models import Member

# Create your views here.

def show_member(request):
	member = Member.objects.all()
	return render_to_response('show_member.html',{'member':member})

def show_index(request):
	return render_to_response('index.html')	
