from PIL import Image
from io import BytesIO


ziel = 300 * 1024
img = Image.open("original.jpg")   
def find_quali(img, ziel):
    niedrig_quali = 30
    hohe_quali = 95
   
    
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
    
    if beste_quali is not None:

        erfolg = True
        return erfolg, beste_quali, beste_groesse, bester_buffer
    erfolg = False 
    return erfolg, beste_quali, beste_groesse, bester_buffer
def compress_to_target(img, ziel):
    erfolg, beste_quali, beste_groesse, bester_buffer = find_quali(img, ziel)

    if erfolg:
        return erfolg, beste_quali, beste_groesse, bester_buffer
        
    if erfolg == False:
        
        breite, hoehe = img.size
        while breite >= 600:
            
            img = img.resize((int(breite * 0.9), int(hoehe * 0.9)))
            breite, hoehe = img.size
            erfolg, beste_quali, beste_groesse, bester_buffer = find_quali(img, ziel)


            if erfolg:
                return erfolg, beste_quali, beste_groesse, bester_buffer
        erfolg = False
        return erfolg, beste_quali, beste_groesse, bester_buffer

print(compress_to_target(img, ziel))


    
    
    
    






