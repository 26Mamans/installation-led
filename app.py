from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = "leads.xlsx"

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        telephone = request.form.get("telephone")
        email = request.form.get("email")
        code_postal = request.form.get("code_postal")
        endroit = request.form.get("endroit")
        surface = request.form.get("surface")

        # Sauvegarde dans Excel
        try:
            df = pd.DataFrame([[nom, prenom, telephone, email, code_postal, endroit, surface]],
                              columns=["Nom", "Prénom", "Téléphone", "Email", "Code Postal", "Endroit", "Surface"])
            try:
                existing_df = pd.read_excel(EXCEL_FILE)
                df = pd.concat([existing_df, df], ignore_index=True)
            except FileNotFoundError:
                pass
            df.to_excel(EXCEL_FILE, index=False)
            message = "Formulaire envoyé avec succès !"
        except Exception as e:
            message = f"Erreur : {e}"

    return render_template("formulaire.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
