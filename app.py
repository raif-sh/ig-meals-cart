from flask import Flask, render_template, jsonify

app = Flask(__name__)

MEALS = [
  {
    'id': 1,
    'name': 'Pizza',
    'ingredients':
    {
      'dough': '1 cup',
      'sauce': '100 ml',
      'cheese': '50 gram',
      'toppings': '300 gram'
    },
    'link': 'https://www.pizzahut.co.uk/pizza/pizza-hut-pizza'
  },
  {
    'id': 2,
    'name': 'Burger',
    'ingredients':
    {
      'meat': '1 kg',
      'vegetables': '1 kg',
      'sauce': '100 ml',
      'buns': '2 pieces'
    },
    'link': 'https://www.burgerking.co.uk/menu/burger-king-menu'
  }
]


@app.route("/")
def index():
  return render_template("home.html", meals=MEALS)

@app.route("/api/meals")
def list_meals():
  return jsonify(MEALS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
