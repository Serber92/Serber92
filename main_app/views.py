from django.shortcuts import render, HttpResponse, redirect
import requests

def index(request):
  if not 'ingredients_list' in request.session:
    request.session['ingredients_list'] = []
  return render(request, "index.html")
  
def add_ingredient(request):
  addIngredientToSession(request)
  getRecipes(request.session['ingredients_list'])
  return redirect("/")

def reset(request):
  request.session['ingredients_list'] = []
  return redirect("/")



# help functions

def addIngredientToSession(request):
  ingredient = request.POST['ingredient']
  if not 'ingredients_list' in request.session:
    request.session['ingredients_list'] = []
  request.session['ingredients_list'].append(ingredient)
  request.session.modified = True

def getRecipes(ingredients):
  base_url = 'https://api.spoonacular.com/recipes'
  search_ingr = '/findByIngredients'
  params = {'number':3, 'apiKey':'1f885b8157ab4f0e8c5cf1e6e8b1849f'}
  for ingr in ingredients:
    if not 'ingredients' in params:
      params['ingredients'] = ingr
    else:
      params['ingredients'] += ',' + ingr
  req = requests.get(url = base_url + search_ingr, params = params)
  data = req.json()
  return data
