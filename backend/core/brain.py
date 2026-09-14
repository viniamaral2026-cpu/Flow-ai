import os
import base64
from openai import OpenAI

API_KEY = os.environ.get("NVIDIA_API_KEY") or "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"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY,
)

ROUTER = {
    "code": "openai/gpt-oss-20b",
    "fast": "openai/gpt-oss-20b",
    "strong": "openai/gpt-oss-20b",
    "vision": "meta/llama-3.2-11b-vision-instruct",
    "vision_fallback": "meta/llama-3.2-90b-vision-instruct",
}


def think(messages, task="strong", max_tokens=600, temperature=0.4):
    model = ROUTER.get(task, ROUTER["strong"])
    try:
        r = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return r.choices[0].message.content.strip()
    except Exception as e:
        if task == "vision" and ROUTER.get("vision_fallback"):
            r = client.chat.completions.create(
                model=ROUTER["vision_fallback"],
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return r.choices[0].message.content.strip()
        raise


def think_stream(messages, task="strong", max_tokens=600, temperature=0.4):
    model = ROUTER.get(task, ROUTER["strong"])
    r = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        stream=True,
    )
    for chunk in r:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


def ver(imagem_base64, pergunta="Descreva o que está na tela do computador do usuário."):
    modelo = ROUTER["vision"]
    for tentativa in range(2):
        try:
            r = client.chat.completions.create(
                model=modelo,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": pergunta},
                        {"type": "image_url", "image_url": {
                            "url": "data:image/png;base64," + imagem_base64}},
                    ],
                }],
                max_tokens=600,
                temperature=0.2,
            )
            return r.choices[0].message.content.strip()
        except Exception as e:
            ultimo = e
            if modelo == ROUTER["vision_fallback"]:
                break
            modelo = ROUTER["vision_fallback"]
    raise ultimo