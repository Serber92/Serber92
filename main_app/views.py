from django.shortcuts import render, HttpResponse, redirect

def index(request):
  if not 'ingredients_list' in request.session:
    request.session['ingredients_list'] = []
  return render(request, "index.html")
  
def add_ingredient(request):
  ingredient = request.POST['ingredient']
  if not 'ingredients_list' in request.session:
    request.session['ingredients_list'] = []
  request.session['ingredients_list'].append(ingredient)
  request.session.modified = True
  return redirect("/")

def reset(request):
  request.session['ingredients_list'] = []
  return redirect("/")

