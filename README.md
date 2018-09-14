# query-media-wiki-api-category
Query MediaWiki/WikiData by category and its dependents

### TODO

I want to query the follwoing category at wikidata using python tools:

Full list of humans: <https://www.wikidata.org/wiki/Special:WhatLinksHere/Q5>

I want a list of entities from this list, which I can look at various properties.
Tryied wptools and wikidata, but I'm too stupid to get them too extract all entries 
depending on a category Q5 like in link above.

Just to mak sure: we are not talking the data from the source, I need code that allows 
accessing the data from API, aqnd not the web page.

For reference: <https://stackoverflow.com/questions/4017166/how-do-i-get-all-articles-about-people-from-wikipedia>

### Pseudocode

```python
stream = get_items(category="Q9")
item = next(stream)
birth_date = item.get_attr("P569")
# some kind of check to make sure it is a date
assert isinstance(birth_date.year(), int)
```


### Code snippets

```python
# -*- coding: utf-8 -*-
import wptools
p = wptools.page('Mahatma_Gandhi').get()
print(p)


from wikidata.client import Client
client = Client()  
entity = client.get('Q5', load=True)
dir(entity)
```

From gist
---------


Are we documenting past or present? Some reflections on Wikipedia person pages dataset.

<https://stackoverflow.com/questions/4017166/how-do-i-get-all-articles-about-people-from-wikipedia>
<https://stackoverflow.com/questions/30091337/how-to-retrieve-biographical-information-of-a-person-using-wikipedias-web-api>

```python
import wptools
p = wptools.page('Mahatma_Gandhi').get()
print(p)
```





