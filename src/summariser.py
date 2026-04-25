import anthropic
import os
from dotenv import load_dotenv

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base, ".env"))

def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def summarise_note(note_text, system_prompt):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {"role": "user", "content": note_text}
        ]
    )
    
    print("Raw response:", message.content)
    return message.content[0].text

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("Base dir:", base_dir)
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    print("API key found:", api_key is not None)
    
    note = load_text(os.path.join(base_dir, "data", "sample_notes", "note_003.txt"))
    print("Note loaded, length:", len(note))
    
    system_prompt = load_text(os.path.join(base_dir, "prompts", "system_prompt_v1.txt"))
    print("Prompt loaded, length:", len(system_prompt))
    
    print("\n=== INPUT NOTE ===")
    print(note)
    print("\n=== SOAP SUMMARY ===")
    
    summary = summarise_note(note, system_prompt)
    print(summary)

if __name__ == "__main__":
    main()    