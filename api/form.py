from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	#similarly we can set minimum length as min_length
	email =forms.EmailField(required =False)
	message = forms.CharField(widget=forms.Textarea)