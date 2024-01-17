from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login_url")
def home(request):
    tempale_name = "base.html"
    context = {}
    return render(request,tempale_name,context)

@login_required(login_url="login_url")
def CreateRecipe(request):
    form = RecipeForm() 
    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect("show_url")
        else:
            return HttpResponse(f"Error: {form.errors}")
        
    template_name = 'app/create.html'
    context = {'form':form}
    return render(request,template_name,context)


def Display(request):
    obj = Recipe.objects.all() 
    template_name = "app/display.html"
    context = {'data' : obj}
    return render(request,template_name,context)

def contentView(request,id):
    obj = Recipe.objects.get(id = id)
    template_name = "app/content.html"
    context = {'data' : obj}
    return render(request,template_name,context)    

@login_required(login_url="login_url")
def UpdateRecepe(request,id):
    obj = Recipe.objects.get(id = id)
    form = RecipeForm(instance=obj) 
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        else:
            # Form is not valid, render the template with the form and errors
            template_name = "app/create.html"
            context = {"form": form  
                       }
            return render(request, template_name, context)

    # Render the template with the form for both GET and valid POST requests
    template_name = "app/create.html"
    context = {"form": form}
    return render(request, template_name, context)

@login_required(login_url="login_url")
def DeleteCard(request,id):
    obj = Recipe.objects.get(id=id)
    obj.delete()
    return redirect("show_url")