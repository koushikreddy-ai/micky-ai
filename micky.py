import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datetime import datetime
import pytz

print("Loading Micky AI model (CPU mode)... Please wait.")

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

print("Micky is ready! Type 'exit' to quit.\n")

chat_history_ids = None

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Micky: Bye! 👋")
        break

    # ---- TIME LOGIC (India) ----
    if "time" in user_input.lower() and "india" in user_input.lower():
        india_tz = pytz.timezone("Asia/Kolkata")
        india_time = datetime.now(india_tz).strftime("%I:%M %p")
        print(f"Micky: The current time in India is {india_time}")
        continue

    # ---- GPT CHAT ----
    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token,
        return_tensors="pt"
    )

    if chat_history_ids is not None:
        bot_input_ids = torch.cat(
            [chat_history_ids, new_input_ids], dim=-1
        )
    else:
        bot_input_ids = new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=600,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print("Micky:", response)
