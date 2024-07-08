import os

import openai
from openai import OpenAI
from config import apikey

openai.api_key = apikey
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "write an email for resignation\n"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "write an email for resignation"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)