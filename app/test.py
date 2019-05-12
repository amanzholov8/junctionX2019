from utils import nlp, mediator

print(nlp.identify('Go back to previous paragraph'))
response_body = mediator.sendChunkText('McGregor started his MMA career in 2008 and, in 2012, he won both the Cage Warriors Featherweight and Lightweight Championships, holding both titles simultaneously before vacating them to sign with the UFC. In 2015, at UFC 194, he defeated José Aldo for the UFC Featherweight Championship via knockout 13 seconds into the first round, which is the fastest victory in UFC title fight history.[12] Upon defeating Eddie Alvarez for the UFC Lightweight Championship at UFC 205, McGregor became the first fighter in UFC history to hold titles in two weight divisions simultaneously.')
with open('1111.mp3', 'wb') as f:
    f.write(response_body)