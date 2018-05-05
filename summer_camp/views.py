from .forms import DocumentForm
from django.shortcuts import redirect, render

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = DocumentForm()
    return render(request, 'assignment_form.html', {'form': form})