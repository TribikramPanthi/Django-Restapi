from django.contrib import admin
from .models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
	#list to be displayed on admin site
	list_display = ('first_name','last_name','email')
	#This cause to appear a search field based on author name
	search_fields = ('first_name','last_name')


class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	#This produce a filter list on side
	list_filter = ('publication_date',)	
	#Note: date_hierarchy receives string but not a tuple.
	#This shows a date at the top of model data.
	date_hierarchy='publication_date'
	ordering = ('-publication_date',)
	#This show only the given field in the given order
	fields = ('title','author','publisher','publication_date')
	#This show a horizontal filter for selecting multiple authors
	#and this only works with many to many field
	filter_horizontal =('author',)
	#for foreign key it is better to use below field, because as publisher 
	#-grows thousand the <select> could be more expensive. SO instead we will use <intput type ='text'> as
	raw_id_fields = ('publisher',)


admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)

# Register your models here.
