from flask import Flask, render_template, request

app = Flask(__name__)

@app.template_filter("clp")
def clp(value):
    try:
        n = float(value)
    except (TypeError, ValueError):
        n = 0
    return "$" + f"{n:,.0f}".replace(",", ".")

@app.route("/", endpoint="home")
def home():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"], endpoint="ejercicio1")
def ejercicio1():
    @app.route("/ejercicio2", endpoint="ejercicio2")
    def ejercicio2():
        return render_template("ejercicio1.html")
@app.route("/ejercicio2", endpoint="ejercicio2")
def ejercicio2():
    return render_template("ejercicio2.html")

if __name__ == "__main__":
    # Desactiva el reloader para evitar dobles registros mientras debuggeas
    app.run(debug=True, use_reloader=False)


