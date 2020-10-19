

import numpy as np


from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer()
# docs is the text from the highest rated review of the movie (The Shawshank Redemption)
docs = (['The Shawshank Redemption is written and directed by Frank Darabont. It is an adaptation of the Stephen King novella Rita Hayworth and Shawshank Redemption. Starring Tim Robbins and Morgan Freeman, the film portrays the story of Andy Dufresne (Robbins), a banker who is sentenced to two life sentences at Shawshank State Prison for apparently murdering his wife and her lover. Andy finds it tough going but finds solace in the friendship he forms with fellow inmate Ellis "Red" Redding (Freeman). While things start to pick up when the warden finds Andy a prison job more befitting his talents as a banker. However, the arrival of another inmate is going to vastly change things for all of them. There was no fanfare or bunting put out for the release of the film back in 94, with a title that didnt give much inkling to anyone about what it was about, and with Columbia Pictures unsure how to market it,Shawshank Redemption barely registered at the box office. However, come Academy Award time the film received several nominations, and although it won none, it stirred up interest in the film for its home entertainment release. The rest, as they say, is history. For the film finally found an audience that saw the film propelled to almost mythical proportions as an endearing modern day classic. Something that has delighted its fans, whilst simultaneously baffling its detractors. One thing is for sure, though, is that which ever side of the Shawshank fence you sit on, the film continues to gather new fans and simply will never go away or loose that mythical status. Its possibly the simplicity of it all that sends some haters of the film into cinematic spasms. The implausible plot and an apparent sentimental edge that makes a nonsense of prison life, are but two chief complaints from those that dislike the film with a passion. Yet when characters are this richly drawn, and so movingly performed, it strikes me as churlish to do down a human drama that is dealing in hope, friendship and faith. The sentimental aspect is indeed there, but that acts as a counterpoint to the suffering, degradation and shattering of the soul involving our protagonist. The need for human connection is never more needed than during incarceration. And given the quite terrific performances of Robbins (never better) & Freeman (sublimely making it easy), its the easiest thing in the world to warm to Andy and Red.Those in support arent faring too bad either. Bob Gunton is coiled spring smarm as Warden Norton, James Whitmore is heart achingly great as the Birdman Of Shawshank, Clancy Brown is menacing as antagonist Capt. Byron Hadley, William Sadler amusing as Heywood & Mark Rolston is impressively vile as Bogs Diamond. Then theres Roger Deakins lush cinematography as the camera gracefully glides in and out of the prison offering almost ethereal hope to our characters. The music pings in conjunction with the emotional flow of the movie too. Thomas Newmans score is mostly piano based, dovetailing neatly with Andys state of mind, while the excellently selected soundtrack ranges from the likes of Hank Williams to the gorgeous Le Nozze di Figaro by Mozart. If you love Shawshank then its a love that lasts a lifetime. Every viewing brings the same array of emotions - anger - revilement - happiness - sadness - inspiration and a warmth that can reduce the most hardened into misty eyed wonderment. Above all else, though, Shawshank offers hope - not just for characters in a movie - but for a better life and a better world for all of us.'])
bag = count.fit_transform(docs)
# 
print(count.vocabulary_)
# 
print(bag.toarray())


from sklearn.feature_extraction.text import TfidfTransformer
np.set_printoptions(precision=2)
tfidf = TfidfTransformer(use_idf=True, norm= 'l2', smooth_idf=True)

print(tfidf.fit_transform(bag).toarray())


# import re
# def preprocessor(text):
#     text =re.sub('<[^>]*>', '', text)
#     emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
#     text = re.sub('[\W]+', '', text.lower()) + ''.join(emoticons).replace('-', '')
#     return text
#     preprocessor('This is a :) test :-( !')

# from nltk.stem.porter import PorterStemmer
# porter = PorterStemmer()
# def tokenizer(text):
#     return text.split()
# tokenizer('runners like running thus they run')
