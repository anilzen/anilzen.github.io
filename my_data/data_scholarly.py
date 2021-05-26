from scholarly import scholarly

author = scholarly.search_author_id('M8NnUIQAAAAJ')
scholarly.fill(author)
for pub in author['publications']:
    scholarly.fill(pub)
pubs = author['publications']

for i, p in enumerate(pubs):
    if 'pub_url' in p:
        p['bib']['pub_url']=p['pub_url']
    if 'eprint_url' in p:
        p['bib']['eprint_url']=p['eprint_url']
    p['bib']['ENTRYTYPE']='article'
    p['bib']['ID']=i

bibtex_text=''
for p in pubs:
    bibtex_text+=scholarly.bibtex(p)

with open('bibtex.bib','w') as bibtex_file:
    bibtex_file.write(bibtex_text)
