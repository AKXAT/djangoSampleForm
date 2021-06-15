from django.shortcuts import render
from . import NewUser
# Create your views here.

def index(request):
    return render(request,'basiForms/index.html')

def form_name_view(request):
    form = NewUser()

    if request.methode == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error')
    
    return render(request,'basicForms/form.html',{'form':form})
















    '''form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something
            print('success')
            print(form.cleaned_data['name'])



    return render(request,'basicapp/form.html',{'form': form})'''