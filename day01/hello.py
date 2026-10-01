import anthropic
from dotenv import load_dotenv

load_dotenv()                      # harmless if you used Option A
client = anthropic.Anthropic()     # reads ANTHROPIC_API_KEY automatically

msg = client.messages.create(
    model="claude-haiku-4-5-20251001",   # cheapest model, ideal for tests
    max_tokens=200,
    messages=[{"role": "user", "content": "Explain month-end close in two sentences."}],
)
print(msg.content[0].text)
print("Tokens used:", msg.usage.input_tokens, "+", msg.usage.output_tokens)