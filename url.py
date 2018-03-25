#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 00:58:27 2018

@author: saadsaleem
"""

def TEXTviaURL(URL):
    '''
    takes a URL string as input 
    and produces a string of the 
    text on the webpage
    '''
    
    from bs4 import BeautifulSoup
    from bs4.element import Comment
    import urllib.request
    
    
    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    
    
    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)
    
    html = urllib.request.urlopen(URL).read()
    
    #print(text_from_html(html))
    return text_from_html(html)


def wordSearch(input_string):
    '''
    takes string as input and searches 
    for the presence of keywords, then 
    makes a neew string of sentencences
    the contain keywords.
    '''
    
    search_result = ''
    breakdown_string = input_string.split('.')
    #print (breakdown_string)
    
    for part in breakdown_string:
        #print(part)
        if "privacy" in part or 'Privacy' in part:
            search_result = search_result + '. ' + part 
        elif "third party" in part:
            search_result = search_result + '. ' + part 
        elif "arbitration" in part:
            search_result = search_result + '. ' + part 
        elif "waiver" in part:
            search_result = search_result + '. ' + part 
        elif "affiliates" in part:
            search_result = search_result + '. ' + part 
        elif "opt-out" in part:
            search_result = search_result + '. ' + part 
        elif "Opt-out" in part:
            search_result = search_result + '. ' + part 
        elif "waive" in part:
            search_result = search_result + '. ' + part 
            
    return search_result
    

def wordSearch(input_string):
    '''
    takes string as input and searches 
    for the presence of keywords, then 
    makes a neew string of sentencences
    the contain keywords.
    '''
    
    search_result = ''
    breakdown_string = input_string.split('.')
    #print (breakdown_string)
    
    for part in breakdown_string:
        #print(part)
        if "privacy" in part or 'Privacy' in part:
            search_result = search_result + '. ' + part 
        elif "third party" in part or 'Third party' in part \
        or 'Third-party' in part or 'third-party' in part:
            search_result = search_result + '. ' + part 
        elif "arbitration" in part or 'Arbitration' in part:
            search_result = search_result + '. ' + part 
        elif "waiver" in part or 'Waiver' in part:
            search_result = search_result + '. ' + part 
        elif "affiliates" in part or 'Affiliates' in part:
            search_result = search_result + '. ' + part 
        elif "opt-out" in part:
            search_result = search_result + '. ' + part 
        elif "Opt-out" in part:
            search_result = search_result + '. ' + part 
        elif "waive" in part or 'Waive' in part:
            search_result = search_result + '. ' + part 
            
    return search_result
    

def summarize(selected_text, n=3):
    from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
    from sumy.nlp.tokenizers import Tokenizer 
    from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in
    
    output = ''
    
    parser = PlaintextParser(selected_text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    
    summary = summarizer(parser.document, n) #Summarize the document with 2 sentences
    
    for sentence in summary:
        output += str(sentence)
    
    return output


            
            
            
            
            
            