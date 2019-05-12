from utils import mediator
from utils import askcontext

def identify(paragraph, user_message):
    textList = user_message.split()
    textDict = dict()
    nums = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    amount = 1

    for word in textList:
        if word.lower() in nums:
            amount = nums[word.lower()]
        textDict[word.lower()] = 1

    if 'go' in textDict or 'paragraph' in textDict or 'paragraphs' in textDict:
        res =  {'category': 'navigation'}

        if 'back' in textDict or 'previous' in textDict:
            res['dir'] = 'back'
        else:
            res['dir'] = 'forward'

        if 'sentence' in textDict or 'sentences' in textDict:
            res['measure'] = 'sentence'
        else:
            res['measure'] = 'paragraph'

        if 'previous' in textDict or 'next' in textDict:
            res['amount'] = 1
        else:
            res['amount'] = amount

        return res

    else:
        res = askcontext.answer(paragraph, mediator.generate_question(user_message), askcontext.get_model())
        return {'category': 'context', 'response': res[0][0]}
