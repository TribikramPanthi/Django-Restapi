from django.shortcuts import render
from .form import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','anthi.tri@gmail.com'),
				['siteowner@gmail.com'],
				)
			return HttpResponseRedirect('/contact/thanks')
	else:
		form=ContactForm(initial={'subject':'I love your site!'})
		#This above is a optional initial field on subject

	return render(request,'contact_form.html',{'form':form})	
			
