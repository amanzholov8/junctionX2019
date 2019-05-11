def identify(user_message):
    return {'category': 'question_message'}

    '''textList = user_message.split()
    textDict = dict()
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    nums = num_dict.keys
    amount = 0

    for word in textList:
        if word.lower() in nums:
            amount = nums[word.lower()]
        textDict[word.lower()] = 1

    if 'go' in textDict:
        res =  {'category': 'navigation_message'}

        if 'back' in textDict or 'previous' in textDict:
            res['dir'] = 'back'
        else:
            res['dir'] = 'forward'

        if 'sentence' in textDict or 'sentences' in textDict:
            res['measure'] = 'sentence'
        else:
            res['measure'] = 'paragraph'

        if 'previous' in textDict:
            res['amount'] = 1
        else:
            res['amount'] = amount

        return res

    #elif 'search for' in textDict:

    #else:
    '''