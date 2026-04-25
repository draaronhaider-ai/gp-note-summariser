import anthropic
import os
import gradio as gr
from dotenv import load_dotenv

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base, ".env"))

def load_system_prompt():
    base = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base, "prompts", "system_prompt_v9.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def summarise_note(note_text):
    if not note_text.strip():
        return "Please enter a clinical note to summarise."
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    system_prompt = load_system_prompt()
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {"role": "user", "content": note_text}
        ]
    )
    
    return message.content[0].text

demo = gr.Interface(
    fn=summarise_note,
    inputs=gr.Textbox(
        lines=20,
        placeholder="Paste a GP consultation note here...",
        label="Clinical Note Input"
    ),
    outputs=gr.Markdown(
        label="SOAP Summary Output"
    ),
    title="GP Note Summariser",
    description=(
        "Paste a GP consultation note and receive a structured SOAP summary. "
        "This tool is a portfolio demonstration only and is not validated for clinical use. "
        "Always refer to the original note — do not use this output as a substitute for clinical documentation."
    ),
    examples=[
        ["Date: 14/04/2026\nGP: Dr. S. Patel\nPatient: Male, 58 years old\n\nPresenting complaint:\nPatient attends for routine review. Complains of increasing shortness of breath on exertion over the past 3 weeks, particularly when climbing stairs. Also reports mild ankle swelling bilaterally, worse in the evenings. Denies chest pain or palpitations.\n\nBackground:\nHypertension - on Amlodipine 5mg OD\nType 2 Diabetes - on Metformin 1g BD\n\nExamination:\nBP 148/92, HR 88 regular, RR 16, Sats 96% on air\nMild pitting oedema to mid-shin bilaterally\n\nAssessment:\nPossible early cardiac failure\n\nPlan:\nBloods requested - BNP, U&E, FBC\nReview in 2 weeks"]
    ],
    flagging_mode="never"
)

if __name__ == "__main__":
    demo.launch()