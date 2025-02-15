import os
import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI

# Crear la instancia de FastAPI
app = FastAPI()

# Ruta GET
@app.get("/slogan")
async def get_slogan():
  client = OpenAI(api_key = "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")
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system", 
          "content": "Eres un experto generando un slogan basado en la descripción de la compañía"
        },
        {
          "role": "user", 
          "content": "Una compañía que vende helados"
        }
      ],
      temperature=1,
      max_tokens=100,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0
  )
  return {
    "mensaje": response.choices[0].message.content
  } 

# Ruta POST
@app.post("/slogan")
async def post_slogan(request: Request):
  json_data = await request.json()
  descripcion = json_data.get("descripcion")
  client = OpenAI(api_key = "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")
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system", 
          "content": "Eres un experto generando un slogan basado en la descripción de la compañía"
        },
        {
          "role": "user", 
          "content": descripcion
        }
      ],
      temperature=1,
      max_tokens=100,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0
  )
  return {
    "mensaje": response.choices[0].message.content
  }

