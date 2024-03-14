#  api usage
from openai import OpenAI

client = OpenAI(
    api_key="123",
    # Change the API base URL to the local interference API
    base_url="http://localhost:1337/v1"
    
)

response = client.chat.completions.create(
    #   model="gpt-3.5-turbo",
      model="gpt-4",
      messages=[{"role": "user", "content": ""}],
      stream=True,
  )

if isinstance(response, dict):
      # Not streaming
      print(response.choices[0].message.content)
else:
      # Streaming
      for token in response:
          content = token.choices[0].delta.content
          if content is not None:
              print(content, end="", flush=True)