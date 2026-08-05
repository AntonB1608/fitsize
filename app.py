from PIL import Image
from io import BytesIO


ziel = 5000 * 1024
niedrig_quali = 30
hohe_quali = 95


def compress_to_target(ziel, niedrig_quali, hohe_quali):
    
    img = Image.open("test.jpg")   
    
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
            
    
    if beste_quali is None:
        erfolg = False
        return erfolg, None, None, None
    else:
        erfolg = True
        return erfolg, beste_quali, beste_groesse, bester_buffer


erfolg, beste_quali, beste_groesse, bester_buffer = compress_to_target(ziel, niedrig_quali, hohe_quali)

if erfolg:
    print(f"Qualität {quali}, {groesse} Bytes")
    with open("ergebnis.jpg", "wb") as f:
        f.write(buffer.getvalue())
else:
    print("Zielgröße nicht erreichbar")
    
    
    






