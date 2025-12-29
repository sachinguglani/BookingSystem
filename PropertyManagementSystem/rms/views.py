from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import RoomDetail
import sqlite3
from .forms import PostForm


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) # Bind data from the POST request
        if form.is_valid():
            form.save() # Save the new object to the database (for ModelForms)
            return redirect('success_url_name') # Redirect after successful submission
    else:
        form = PostForm() # Create an unbound, empty form

    return render(request, 'form.html', {'form': form})

def RegistrationPage(request):
    context = {
        'message': "This content came from the views.py file!"
    }
    # Render the template with the context
    return render(request, 'UserRegistration.html', context)

def rms(request):
  sqliteConnection = sqlite3.connect('PMS.db')
  cursor = sqliteConnection.cursor()
  statement = 'SELECT * FROM RoomDetailT'
  cursor.execute(statement)
  output = cursor_obj.fetchall()
  connection_obj.commit()
  connection_obj.close()
  template = loader.get_template('rms.html')
  context = {
        'items': output
    }
  
  return HttpResponse(template.render(context, request))

def roomData(request):
    obj = RoomDetail.objects.all().values();
    template = loader.get_template('rms.html')
    context = {
        'items': obj
    }
    return HttpResponse(template.render(context, request))