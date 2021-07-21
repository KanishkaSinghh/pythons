def matchingwords(sentences1,sentences2):
    score=0
    words1=sentences1.split(" ")
    words2=sentences2.split(" ")
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                score+=1
    return score
if __name__ == '__main__':
    sentences=[This is good ,python is good]