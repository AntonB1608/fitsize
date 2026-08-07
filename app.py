from PIL import Image
from io import BytesIO


ziel = 5000 * 1024
niedrig_quali = 30
hohe_quali = 95
local = True
if local:
    img = Image.open("original.jpg")
else:
    img = request.form("img")


def compress_to_target(ziel, niedrig_quali, hohe_quali):
    
    img = Image.open("original.jpg")   
    
    if img.mode in ("RGBA", "P", "LA"):   
        img = img.convert("RGB")  
    
    beste_quali = None
    beste_groesse = None
    bester_buffer = None
    kleiner = None
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
           
    
    if not beste_quali is None:
        erfolg = True
        return erfolg, beste_quali, beste_groesse, bester_buffer, None
    

    while not size >= 600:
        size = height * width
        if size > 600:
            erfolg = True
            kleiner = img.resize((height, width))
            height * 
            return erfolg, None, None, None
        else:
            erfolg = False
            return erfolg, None, None, None, kleiner





        
        


erfolg, beste_quali, beste_groesse, bester_buffer = compress_to_target(ziel, niedrig_quali, hohe_quali)

if erfolg:
    print(f"Qualität {quali}, {groesse} Bytes")
    with open("ergebnis.jpg", "wb") as f:
        f.write(buffer.getvalue())
else:
    print("Zielgröße nicht erreichbar")
    
    
    






