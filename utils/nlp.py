def identify(text):
    textList = text.split()
    textDict = dict()
    nums = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    amount = 0

    for word in textList:
        if word.lower() in nums:
            amount = nums[word.lower()]
        textDict[word.lower()] = 1

    if 'go' in textDict:
        res =  {'category': 'navigation'}

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

    elif 'definition' in textDict:
        return {'category': 'google', 'text': text}
    
    else:
        return 'Hello World'