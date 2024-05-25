
# total = 0
# correct = 0
# EM = 0
# BLEU = 0
# bblleeuu = 0
# errors = []

# dataset = load_dataset("squad")
# # train = dataset['train']
# validation = dataset['validation']

# for record in tqdm(validation):
#         # try:
#                 total += 1
#                 if (total % 1000 == 0):
#                         print(f"Correct:\t\t {correct}, out of {total}: {100*correct/total}%")
#                         print(f"EM:\t\t\t {EM}, out of {total}: {100*EM/total}%")
#                         print(f"BLEU:\t\t\t {BLEU}, out of {total}: {100*BLEU/total}%")
#                         print(f"BLEU Score:\t\t {bblleeuu}, out of {total}: {100*bblleeuu/total}%")
#                 result = question_answerer(question=record['question'], context=record['context'], truncation=True, padding=True, return_tensors='pt')
#                 # result = QA(model, tokenizer,record['question'], record['context'])
#                 n = min(len(result['answer'].split()), 4)
#                 # n = min(len(result.split()), 4)
#                 if n == 0:
#                         BLEUscore = 0
#                 else:
#                         weights = [1.0/n]*n
#                         BLEUscore = nltk.translate.bleu_score.sentence_bleu([record['answers']['text'][0].lower()], result['answer'].lower(), weights=weights)
#                         # BLEUscore = nltk.translate.bleu_score.sentence_bleu([record['answers']['text'][0].lower()], result.lower(), weights=weights)
#                 if result['answer'] != '' and (result['answer'].lower() in record['answers']['text'][0].lower() or record['answers']['text'][0].lower() in result['answer'].lower()):
#                 # if result != '' and (result.lower() in record['answers']['text'][0].lower() or record['answers']['text'][0].lower() in result.lower()):
#                         correct += 1
#                 if record['answers']['text'][0].lower() == result['answer'].lower():
#                 # if record['answers']['text'][0].lower() == result.lower():
#                         EM += 1
#                 if BLEUscore > 0.5:
#                         BLEU += 1
#                 bblleeuu += BLEUscore
                 
#         # except Exception as e:
#         #         errors.append(total)
#         #         print(f"Error at {total}: {e}")
#         #         continue
# print(f"Correct: {correct}, out of {total}: {100*correct/total}%")
# print(f"EM: {EM}, out of {total}: {100*EM/total}%")
# print(f"BLEU: {BLEU}, out of {total}: {100*BLEU/total}%")
# print(f"BLEU Score: {bblleeuu}, out of {total}: {100*bblleeuu/total}%")

