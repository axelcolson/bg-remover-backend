from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove

app = FastAPI()

@app.post("/remove-bg")
async def remove_background(image: UploadFile = File(...)):
    input_bytes = await image.read()
    output_bytes = remove(input_bytes)
    return StreamingResponse(iter([output_bytes]), media_type="image/png")
