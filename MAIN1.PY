from flask import Flask, render_template
import random 



app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return '<h2>Witaj! tutaj możesz dowiedzieć się kilku ciekawostek odnośnie uzależnień od technologi <a href="/random_fact">Zobacz losowy fakt!</a></h2><h1>Spójrz też tutaj!: <a href="/strona">Link</a></h1>'

@app.route("/random_fact")
def fact():
    list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń","Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.","Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi"]
    return f'<p>{random.choice(list)}</p>'

@app.route("/strona")
def start_strona():
    return render_template("Test1.html")

    
   
app.run(debug=True)
