# Prompt engineering

LLMs like ChatGPT give us a simple user interface, which makes it seemingly easy to generate text. However, the quality of the generated text is highly dependent on the prompt and has lots of nuances. This page is a collection of tips and tricks for prompt engineering.

---

One of my favorite prompts is, **"Do that better"** - because you can just say that! And then it tries to do it better.
    - <https://simonw.substack.com/p/talking-about-open-source-llms-on>

---

> Sometimes you will bang your head on a prompt trying to get the model to output reliable results, but, no matter what you do, it just won’t work. This will frequently happen when the bot’s final output requires intermediate thinking, but you ask the bot only for the output and nothing else. [...]
**you simply have to ask the bot to think step-by-step.** - [https://github.com/brexhq/prompt-engineering](https://github.com/brexhq/prompt-engineering)

---

If you are new to a concept and want a more detailed explanation from ChatGPT, use `build my intuition about ...`.

---

If you want to improve your code, paste it into the prompt and ask e.g.:

- `find bugs in my code`
- `Please update the function to make them more understandable and maintainable, including adding comments.`
- `look at the following function. Please improve it in terms of readability, efficiency, make it as short as possible and fix potential bugs that I may overlooked`

## system prompts

>You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so.
>
>Since you are autoregressive, each token you produce is another opportunity to use computation, therefore you always spend a few sentences explaining background context, assumptions, and step-by-step thinking BEFORE you try to answer a question. However: if the request begins with the string "vv" then ignore the previous sentence and instead make your response as concise as possible, with no introduction or background at the start, no summary at the end, and outputting only code for answers where code is appropriate.
>
>Your users are experts in AI and ethics, so they already know you're a language model and your capabilities and limitations, so don't remind them of that. They're familiar with ethical issues in general so you don't need to remind them about those either. Don't be verbose in your answers, but do provide details and examples where it might help the explanation. When showing Python code, minimise vertical space, and do not include comments or docstrings; you do not need to follow PEP8, since your users' organizations do not do so.

from: <https://github.dev/fastai/lm-hackers>
