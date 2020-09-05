from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import render
from contactform.models import Student
from django.core.mail import send_mail


# Create your views here.
class ContactView(CreateView):
	model = Student
	template_name = 'contact.html'
	success_url = '/thanks/'
	fields = ['name','email','college','message','file']

	'''
	def form_valid(self, form):
		
		message = """Hello {name}
Thank you for your interest in our company, we'll get back to you shortly!

Best Regards
Your name""".format(name=form.cleaned_data.get('name'))
		send_mail(
			subject="Thanks for contacting Startup name",
			message=message,
			from_email='Your Name<youremail@yourdomain.com>',
			recipient_list=[form.cleaned_data.get('email')],)
		return super().form_valid(form)


	'''