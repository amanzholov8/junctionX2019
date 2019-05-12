from deeppavlov import build_model, configs

model = build_model(configs.squad.squad, download=False)
#model.save()
#print(model(['DeepPavlov is library for NLP and dialog systems.'], ['What is DeepPavlov?']))

def get_model():
    return model
    #model = build_model(configs.squad.squad, download=False)

def answer(text, question, model):
    return model([text], [question])
    #return 'hello world'