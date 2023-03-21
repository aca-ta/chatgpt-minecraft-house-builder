""" chatgpt-minecraft """
import re
import os

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


def main():
    """Main."""
    ask = """
    You are an excellent Python engineer and an excellent Minecraft Developer.
    Can you create python codes which makes house with mcpi? 
    Pleas add following codes. "mc = Minecraft.create("localhost", 4711)".
    """

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": ask},
        ],
        temperature=0,
    )

    codes = res["choices"][0]["message"]["content"]
    trimed = re.findall(r"^```[\w]*\n([\s\S]*?)\n```$", codes, re.MULTILINE)
    print(trimed[0])


if __name__ == "__main__":
    main()
