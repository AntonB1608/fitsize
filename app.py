from PIL import Image
from io import BytesIO
from flask import Flask, render_template, send_file, request, flash, redirect
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("secret_key")
app.config['SECRET_KEY'] = os.getenv("secret_key")
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = os.getenv("SESSION_COOKIE_SECURE", "false").lower() == "true"


@app.route("/", methods=["POST", "GET"])
def compress():
    if request.method == "GET":
        return render_template("index.html")
    datei = request.files.get("bild")
    if not datei or datei.filename == "":
        flash("Bitte lade eine Bilddatei hoch.", "fehler")
        return render_template("index.html")
    try:
        ziel = int(request.form.get("zielgroesse")) * 1024
    except (TypeError, ValueError):
        flash("Bitte gib eine Zahl als Zielgröße ein.", "fehler")
        return render_template("index.html") 
    try:
        img = Image.open(datei)
        img.load()
    except Exception:
        flash("Diese Datei konnte nicht als Bild gelesen werden.", "fehler")
        return render_template("index.html") 
    datei.seek(0, 2)     
    datei_groesse = datei.tell()  
    datei.seek(0)   
    if datei_groesse <= ziel:
        datei.seek(0)
        buffer = BytesIO(datei.read())
        return send_file(buffer, mimetype="image/jpeg",
                         as_attachment=True, download_name="fitsize.jpg")
    
    erfolg, _ ,  bester_buffer = compress_to_target(img, ziel)

    if erfolg:
        bester_buffer.seek(0)
        return send_file(bester_buffer, mimetype="image/jpeg",
                        as_attachment=True, download_name="fitsize.jpg")
    else:
        flash("Die Datei konnte nicht auf die gewünschte Größe komprimiert werden.", "fehler")
        return render_template("index.html")

def find_quali(img, ziel):
    niedrig_quali = 30
    hohe_quali = 95
   
    
    if img.mode in ("RGBA", "P", "LA"):  

        img = img.convert("RGB")  
    
    beste_quali = None
    beste_groesse = None
    bester_buffer = None
    while niedrig_quali <= hohe_quali:

        mitte = (niedrig_quali + hohe_quali) // 2

        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=mitte)
        groesse = buffer.tell()

        if groesse <= ziel:

            beste_quali = mitte
            beste_groesse = groesse
            bester_buffer = buffer
            
            niedrig_quali = mitte + 1
            
        else:

            hohe_quali = mitte - 1
    
    if beste_quali is not None:

        erfolg = True
        return erfolg, beste_groesse, bester_buffer
    erfolg = False 
    return erfolg, beste_groesse, bester_buffer

def compress_to_target(img, ziel):
    erfolg, beste_groesse, bester_buffer = find_quali(img, ziel)

    if erfolg:
        return erfolg, beste_groesse, bester_buffer
        
    if erfolg == False:
        
        breite, hoehe = img.size
        while breite >= 600:
            
            img = img.resize((int(breite * 0.7), int(hoehe * 0.7)))
            breite, hoehe = img.size
            erfolg, beste_groesse, bester_buffer = find_quali(img, ziel)


            if erfolg:
                return erfolg, beste_groesse, bester_buffer
        erfolg = False
        return erfolg, beste_groesse, bester_buffer

if __name__ == "__main__":
    app.run(port=5555, debug=True)

    
    
    
    






