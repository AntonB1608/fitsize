from PIL import Image
from io import BytesIO


img = Image.open("test.jpg")     
print("Modus:", img.mode)        

if img.mode in ("RGBA", "P", "LA"):   
    img = img.convert("RGB")          





ziel = 800 * 1024
niedrig = 1
hoch = 95
bestes = None


while niedrig <= hoch:
    mitte = (niedrig + hoch) // 2

    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=mitte)
    groesse = buffer.tell()

    print(f"probiere {mitte} → {groesse} Bytes")

    if groesse <= ziel:
        bestes = mitte
        niedrig = mitte + 1
    else:
        hoch = mitte - 1

print("beste Qualität:", bestes)