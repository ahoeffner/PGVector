from .Api import Api
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import Optional
import base64


app = FastAPI(title="Embedding Service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/createEmbeddings")
async def createEmbeddings(file: Optional[UploadFile] = File(None), text: Optional[str] = Form(None)):
    """Accept only multipart/form-data: either a `text` form field or a `file` upload.

    If a file is provided its contents will be decoded as UTF-8 if possible; otherwise the function
    will receive a base64-prefixed payload so downstream can detect binary content.
    """
    if not file and not text:
        raise HTTPException(status_code=422, detail="Provide either a 'text' form field or upload a 'file'.")

    if file:
        data = await file.read()
        print(f"Received file: {file.filename} ({file.content_type}) ({file.size})")
        try:
            content = data.decode("utf-8")
        except Exception:
            content = "__base64__:" + base64.b64encode(data).decode("ascii")
        input_name = file.filename
    else:
        content = text
        input_name = text

    result = Api.createEmbeddings(content)
    return {"input": input_name, "result": result}
