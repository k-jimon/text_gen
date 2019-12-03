# -*- coding: utf-8 -*-
import re
import random
from collections import deque

import MeCab
 
class MarkovChain(object):
    def __init__(self, order=2):
        self.order = order
        self.model = {}
    
    def one_sentence_generator(self, long_text):
        sentences = re.findall(".*?。", long_text)
        for sentence in sentences:
            yield sentence
            
    def wakati(self, text):
        t = MeCab.Tagger("-Owakati")
        parsed_text = ""
        for one_line_text in self.one_sentence_generator(text):
            parsed_text += " "
            parsed_text += t.parse(one_line_text)
        wordlist = parsed_text.rstrip("\n").split(" ")
        return wordlist
    
    def make_model(self, text):
        wordlist = self.wakati(text)
        queue = deque([], self.order)
        queue.append("[BOS]")
        for markov_value in wordlist:
            if len(queue) == self.order:
                if queue[-1] == "。":
                    markov_key = tuple(queue)
                    if markov_key not in self.model:
                        self.model[markov_key] = []
                    self.model[markov_key].append("[BOS]")
                    queue.append("[BOS]")
                
                markov_key = tuple(queue)      
                if markov_key not in self.model:
                    self.model[markov_key] = []
                self.model[markov_key].append(markov_value)
            queue.append(markov_value)
    
    def make_sentence(self, sentence_num=5, seed="[BOS]", max_words = 1000):    
        sentence_count = 0

        key_candidates = [key for key in self.model if key[0] == seed]
        if not key_candidates:
            print("Not find Keyword")
            return
        markov_key = random.choice(key_candidates)
        queue = deque(list(markov_key), self.order)
        
        sentence = "".join(markov_key)
        for _ in range(max_words):
            markov_key = tuple(queue)
            next_word = random.choice(self.model[markov_key])
            sentence += next_word
            queue.append(next_word)
           
            if next_word == "。":
                sentence_count += 1
                if sentence_count == sentence_num:
                    break
        return sentence


if __name__ == "__main__":
    text = 'なるべく長い日本語の文章。'
    marmodel = MarkovChain(order=2)
    marmodel.make_model(text)
    print(marmodel.make_sentence())

