# from llama_cpp import Llama # I use `codellama-13b-instruct.Q5_K_M.gguf`
import openai
from openai import OpenAI

from secret_information import *
import re

"""
デバッグ出力とエラー出力
"""
debug = False
def debug_print(a):
    if debug:
        print("# # # # # #")
        print(a)
        print("# # # # # #")

def error_print(s: str):
    print("error: " + s)

"""
インタプリタクラスの補助クラス
"""
class inner_transpiler_class():
    def __init__(self, base_lang: str) -> None:
        self.base_lang = base_lang
        self.history = []

    # llm = Llama(model_path=LLAMA_PATH, seed=0, verbose=debug, n_gpu_layers=-1, n_ctx=2048)
    llm = OpenAI(api_key=SECRET_API_KEY)
    def query(self, s: str) -> str:
        messages = self.history
        messages.append({
            # "role" : "user", "content" : f"Please translate this \"new_lang\" code to {self.base_lang}:\n```\n{s}\n```",
            "role" : "user", "content" : f"この「new_lang」コードを {self.base_lang} のプログラムに翻訳してください。:\n```\n{s}\n```",
        })
        # streamer = self.llm.create_chat_completion(messages)
        ret = self.llm.chat.completions.create(messages=messages, model="gpt-3.5-turbo", temperature=0.0)
        # ret = self.llm.create_chat_completion(messages, temperature=0)
        debug_print(ret)
        ans = ret.choices[0].message.content
        # ans = ret["choices"][0]["message"]["content"]
        # ans = ""
        # for msg in streamer:
        #     message = msg["choices"][0]["delta"]
        #     if "content" in message:
        #         ans += message["content"]

        debug_print(ans)
        return ans

"""
インタプリタクラス
"""
class transpiler_class():
    def __init__(self, base_lang: str) -> None:
        self.base_lang = base_lang
        self.inner_transpiler = inner_transpiler_class(base_lang=base_lang)
        self.inner_transpiler.history.append({"role" : "system", "content" : \
    f"assistantとuser間の対話の記録です。 \"new_lang\" はとあるプログラミング言語です。assistantは「new_lang」コードを {base_lang} に翻訳します。結果がそのまま実行またはコンパイルができるように翻訳します。"})
        # self.inner_transpiler.history.append({"role" : "user", "content" : f"Please translate some programming codes to {base_lang}.\n"})
        # self.inner_transpiler.history.append({"role" : "assistant", "content" : "Ok.\n"})

    def add_example(self, before: str, after: str) -> None:
        # self.inner_transpiler.history.append({"role" : "user", "content" : f"Please translate this \"new_lang\" code to {self.base_lang}:\n```\n{before}\n```"})
        self.inner_transpiler.history.append({"role" : "user", "content" : f"この「new_lang」コードを {self.base_lang} のプログラムに翻訳してください。:\n```\n{before}\n```"})
        self.inner_transpiler.history.append({"role" : "assistant", "content" : f"\n```\n{after}\n```"})

    def transpile_code(self, code: str) -> str:
        debug_print(self.inner_transpiler.history)
        ret = self.inner_transpiler.query(s=code)
        matches = re.findall(r'```\w*\n*(.*?)```', ret, re.DOTALL)
        # matches = re.findall(r'```(.*?)```', ret, re.DOTALL)
        if len(matches) == 0:
            error_print("INNER ERROR (not matched)")
            return ""
        return matches[0]

    def make_documents(self) -> str:
        pass # TODO
