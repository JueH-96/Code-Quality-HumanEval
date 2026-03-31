def split_words(txt):
    # Split by spaces, comma or default to upper case words only when not found any other methods are available (e.g., odd-order alphabetical sequence) 
     if ',' in txt:  
         return [s for s in re.split('[ ,]',txt)][-1], len(set([c.lower() for c in list(filter(str.isupper,re.findall("[A-Z]*",txt)))])%2 != 0)  # assuming import of 're'
     elif ('\s+' in txt):  
         return [s for s in re.split('[\s\,]',txt)][-1], len(set([c.lower() for c in list(filter(str.isupper,re.findall("[A-Z]*",txt)))])%2 != 0)  # assuming import of 're'
     else:  
         return [s for s in re.split('[\W_]', txt)][-1], len([c.lower() for c in list(filter(str.isupper, re.findall("[A-Z]*",txt)))])%2 != 0  # assuming import of 're'