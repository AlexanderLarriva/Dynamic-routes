from flask import Flask, jsonify, make_response   #, abort

from Dynamic_routes.data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return 'open something like (you can change id): /companies/5'


# BEGIN (write your solution here)
@app.route('/companies/<int:id>')
def courses(id):
    for company in companies:
        if company['id'] == id:
            return jsonify(company)
    # abort(404, "Page not found")
    return make_response(('Page not found'), 404)

# END
