import os
import openai
openai.api_key = "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"


def productDescription(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate a detailed product description for {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer
    

def tweetIdeas(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate a detailed product description for {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer

def coldEmails(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate professional cold email about {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer


def businessPitch(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate a compelling business pitch for {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer


def videoIdeas(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate ideas for video on {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer


def socialMedia(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate social media post promoting {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer ='Sorry, you beat the AI this time!'
    return answer


def keywordGenerator(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate keyword related to {}".format(query),
        temperature = 0.5,
        max_tokens = 50,
        top_p = 1,
        frequency_penalty =00,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer


def taglineGenerator(query):
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt="Generate a tagline for a {}".format(query),
        temperature = 0.5,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty =0,
        presence_penalty = 0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer  = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time!'
    else:
        answer = 'Sorry, you beat the AI this time!'
    return answer

if __name__ == "__main__":
     main()
