from .forms import DocumentForm
from django.shortcuts import redirect, render

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # print(form.cleaned_data['name'])
        if form.is_valid():
            sub_name = form.cleaned_data['name']
            file_name = request.FILES['document'].name
            form.save()
            return render(request, 'successful.html',{'name': sub_name, 'filename': file_name})
    else:
        form = DocumentForm()
    return render(request, 'assignment_form.html', {'form': form})