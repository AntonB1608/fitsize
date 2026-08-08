from PIL import Image
from io import BytesIO


ziel = 50 * 1024
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
           
    
    if not beste_quali is None:

        erfolg_quali = True
        return erfolg_quali, beste_quali, beste_groesse, bester_buffer
    else:
        erfolg_quali = False
        return erfolg_quali, beste_quali, beste_groesse, bester_buffer





erfolg_quali, beste_quali, beste_groesse, bester_buffer = find_quali(img, ziel)
if erfolg_quali:
    print(f"Qualität {beste_quali}, {beste_groesse} Bytes")
    
    
    






