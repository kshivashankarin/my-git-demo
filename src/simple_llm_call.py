from openai import OpenAI

client = OpenAI(
    api_key = 'PASTE_YOUR_KEY_HERE'
)

response = client.responses.create(
    model = 'gpt-5.4-mini',
    input = "Illaya thalapathy Vijay - Tamil Actor"
)

print(response.output_text)