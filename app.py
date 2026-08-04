from PIL import Image
from io import BytesIO


ziel = 800 * 1024
niedrig_quali = 1
hohe_quali = 95


def compress_to_target(ziel, niedrig_quali, hohe_quali):
    
    img = Image.open("test.jpg")   
    
    if img.mode in ("RGBA", "P", "LA"):   
        img = img.convert("RGB")  
    
    runden = 0
    beste_quali = None
    beste_groesse = None
    while niedrig_quali <= hohe_quali:
        mitte = (niedrig_quali + hohe_quali) // 2

        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=mitte)
        groesse = buffer.tell()

        if groesse <= ziel:
            beste_quali = mitte
            beste_groesse = groesse
            bester_buffer = buffer
            with open("ergebnis.jpg", "wb") as f:
                f.write(bester_buffer.getvalue())
            niedrig_quali = mitte + 1
            runden += 1
        else:
            hohe_quali = mitte - 1
            runden += 1
    print(f"beste Qualität: {beste_quali}, Größe: {beste_groesse} Bytes, Runden: {runden}")

compress_to_target(ziel, niedrig_quali, hohe_quali)

    
    
    






