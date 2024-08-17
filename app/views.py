from .forms import FileUploadForm
from django.http import HttpResponse

import tempfile
import os

#views.py
from django.http import JsonResponse

from django.conf import settings


from sklearn.preprocessing import StandardScaler
#
from django.core.files.storage import FileSystemStorage

from docx import Document

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from io import BytesIO
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse
import re
from .models import MyModel3
from .models import Applicant
from .forms import ResumeForm


import pandas as pd
from django.shortcuts import render
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
from joblib import dump, load
import os

#from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

#pdf miner 
from pdfminer.layout import LAParams
from pdfminer.high_level import extract_text_to_fp
#from pdfminer.high_level import extract_text

# pdf miner


#from .models import Document



import nltk
nltk.download('stopwords')

import os
from django.conf import settings
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Create your views here.
import os
from django.shortcuts import render
#from .models import load_models, classify,  preprocessed_data
import pandas as pd


def home(request):

    return render(request,'app/index.html')


def career(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/career.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def drivers(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/drivers.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def chatbot(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chatbot.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def details(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/details.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

@require_http_methods(["POST"])
def submit_form(request):
    # Create a model instance with form data
    new_entry = MyModel3(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'],
                         recentedu=request.POST['recentedu'],
                         relatedexp=request.POST['relatedexp'],companies=request.POST['companies']
                         ,licenseType=request.POST['licenseType'],
                          passdate=request.POST['passdate'],expdate=request.POST['expdate']
       
                          ,cpccard=request.POST['cpccard'],totalcpc=request.POST['totalcpc']
                          ,address=request.POST['address'],city=request.POST['city'],
                          distance=request.POST['distance']
                          )
                 
    new_entry.save()  # Save the model instance to the database
    return redirect('success')


def success(request):

    return render(request,'app/success.html')


def custom_page(reqeust):

    return HttpResponse('Redirecting to the custome page:')






def myadmin(request):
    # Retrieve all records from MyModel3 or use filters as necessary
    data = MyModel3.objects.all()
    return render(request, 'app/myadmin.html', {'data': data})


def shortlist(request):
    data = MyModel3.objects.all()
    return render(request, 'app/shortlist.html', {'data': data})



def test(request):

    return render(request,'app/uploadcandidate.html')




    
    



