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
    precio_unitario = 9000
    resultado = errores = None

    if request.method == "POST":
        nombre = (request.form.get("nombre") or "").strip()
        edad_raw = request.form.get("edad") or ""
        cant_raw = request.form.get("cantidad") or ""
        errores = []

        try:
            edad = int(edad_raw)
            if edad < 0:
                errores.append("La edad no puede ser negativa.")
        except ValueError:
            errores.append("Edad inválida.")
            edad = 0

        try:
            cantidad = int(cant_raw)
            if cantidad <= 0:
                errores.append("La cantidad debe ser mayor a 0.")
        except ValueError:
            errores.append("Cantidad inválida.")
            cantidad = 0

        if not errores and nombre:
            total_sin_desc = cantidad * precio_unitario
            if 18 <= edad <= 30:
                desc_pct = 0.15
            elif edad > 30:
                desc_pct = 0.25
            else:
                desc_pct = 0.0

            descuento = round(total_sin_desc * desc_pct)
            total_con_desc = total_sin_desc - descuento

            resultado = {
                "nombre": nombre,
                "edad": edad,
                "cantidad": cantidad,
                "total_sin_desc": total_sin_desc,
                "descuento_pct": int(desc_pct * 100),
                "descuento": descuento,
                "total_con_desc": total_con_desc,
            }

    return render_template("ejercicio1.html",
                           resultado=resultado,
                           errores=errores,
                           precio_unitario=precio_unitario)
@app.route("/ejercicio2", endpoint="ejercicio2")
def ejercicio2():
    return render_template("ejercicio2.html")


if __name__ == "__main__":
    # Desactiva el reloader para evitar dobles registros mientras debuggeas
    app.run(debug=True, use_reloader=False)


