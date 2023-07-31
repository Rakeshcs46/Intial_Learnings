from flask import Flask , render_template ,request,jsonify
import psycopg2
import psycopg2.extras

DB_HOST = "localhost"
DB_NAME = "taxcredit_db"
DB_USER = "postgres"
DB_PASS = "postgres"
          
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

app = Flask(__name__)

@app.route('/')
def main():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select * from carmake order by make_id")
    carmake= cur.fetchall()
    return render_template('index.html', carmake=carmake)

@app.route("/carmodel",methods=["POST","GET"])
def carbrand():  
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        category_id = request.form['category_id'] 
        print(category_id)  
        cur.execute("SELECT  * FROM car_model WHERE make_id = %s ORDER BY car_model ASC", [category_id] )
        car_model = cur.fetchall()  
        OutputArray = []
        for row in car_model:
            outputObj = {
                'id': row['make_id'],
                'name': row['car_models']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)


# @app.route("/caryear",methods=["POST","GET"])
# def caryear():  
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if request.method == 'POST':
#         category_id = request.form['category_id'] 
#         print(category_id)  
#         cur.execute("SELECT  * FROM car_model WHERE make_id = %s ORDER BY car_model ASC", [category_id] )

# @app.route("/calculate",methods=["POST","GET"])
# def carbrand():  
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if request.method == 'POST':
#                 cur.execute("SELECT  * FROM car_model WHERE make_id = %s ORDER BY car_model ASC", [category_id] )

  
    

if __name__ == "__main__":
    app.run(debug=True)