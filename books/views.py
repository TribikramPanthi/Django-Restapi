from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Author, Publisher, Book

# Create your views here.
#This view is hardcoded view to show all the items in the request.META 
#request.META is a dictionary like object.
def current_url_view(request):
	values = request.META.items()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))



#Now lets get started with form handling in django
#I am connenting below function because this is already accomodated by search function
# def search_form(request):
# 	return render(request,'search_form.html')


def search(request):
	# if 'q' in request.GET:
	# 	message='You searched for: %r' %(request.GET['q'])
	# else:
	# 	message='You submitted an empty form'
	# return HttpResponse(message)

	# if 'q' in request.GET and request.GET['q']:
	# 	q = request.GET['q']
	# 	books = Book.objects.filter(title__icontains=q)
	# 	return render(request, 'search_results.html',
	# 		{'books': books, 'query': q})
	# else:
	# 	#return HttpResponse('Please submit a search term.')	
	# 	return render(request,'search_form.html', {'error':True})


	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html',
			{'books': books, 'query': q})
	return render(request, 'search_form.html',
	{'error': error})



		