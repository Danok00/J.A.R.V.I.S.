import openai

openai.api_key = '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'

models = openai.Model.list()
#print(models)


def handle_input(user_input):
    compiletion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo', messages=[{'role': 'user', 'content': user_input}]
    )
    return compiletion

