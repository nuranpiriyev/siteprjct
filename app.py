from flask import Flask, render_template, request

app = Flask(__name__)

def search_products(query):
   
    products = [
    
    
        'Mr.Mezahir Memishov',
        'Mr.Ismayil Ismayilov',
        'Aghakerim Abbasov',
        'Ravan Babayev',
        
    ]
    
    filtered_products = [product for product in products if query.lower() in product.lower()]
    return filtered_products

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    products = search_products(query)
    return render_template('search_results.html', query=query, products=products)

if __name__ == '__main__':
    app.run(debug=True)
