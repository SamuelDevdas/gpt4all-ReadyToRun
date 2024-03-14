from g4f.client import Client
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini

client = Client(
    provider=OpenaiChat,
    image_provider=Gemini,
)
response = client.images.generate(
  model="Gemini",
  prompt="a white siamese cat",

)
print(response.data[0].url)


# response = client.images.generate(
#     model="dall-e-3",
#     prompt="a white siamese cat",

# )

# print(response.data[0].url)