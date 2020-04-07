from django.shortcuts import render, HttpResponse, redirect
import requests

base_url = 'https://api.spoonacular.com/recipes'

def index(request):
  if not 'ingredients_list' in request.session:
    request.session['ingredients_list'] = []
  if not 'cards_list' in request.session:
    request.session['cards_list'] = []
  return render(request, "index.html")
  
def add_ingredient(request):
  addIngredientToSession(request)
  recipes = getRecipes(request.session['ingredients_list'])
  cards = recipeCards(recipes)
  request.session['cards_list'] = cards
  request.session.modified = True
  return redirect("/")

def reset(request):
  request.session['ingredients_list'] = []
  request.session['cards_list'] = []
  return redirect("/")

  

# help functions

def addIngredientToSession(request):
  ingredient = request.POST['ingredient']
  if not 'ingredients_list' in request.session:
    request.session['ingredients_list'] = []
  request.session['ingredients_list'].append(ingredient)
  request.session.modified = True

def getRecipes(ingredients):
  endpoint = '/findByIngredients'
  params = {'number':3, 'apiKey':'1f885b8157ab4f0e8c5cf1e6e8b1849f'}
  for ingr in ingredients:
    if not 'ingredients' in params:
      params['ingredients'] = ingr
    else:
      params['ingredients'] += ',' + ingr
  request = requests.get(url=base_url+endpoint, params = params)
  data = request.json()
  return data

def recipeCards(recipes):
  Cards = []
  for recipe in recipes:
    image = recipe['image']
    title = recipe['title']
    id = recipe['id']
    additionalIngr = []
    for ingredient in recipe["missedIngredients"]:
      additionalIngr.append(ingredient['originalString'])
    Cards.append({
      "title":title,
      "image":image,
      "url":getRecipeLink(id),
      "additionalIngr":additionalIngr
    })
  return Cards

def getRecipeLink(id):
  endpoint = '/information'
  params = {'apiKey':'1f885b8157ab4f0e8c5cf1e6e8b1849f', 'includeNutrition':'false'}
  request = requests.get(url=base_url+'/'+str(id)+endpoint, params=params)
  data = request.json()
  url = data['sourceUrl']
  return url

  
  
