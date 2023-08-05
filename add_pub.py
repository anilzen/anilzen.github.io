import os
import arxiv
import requests
import sys

# Get the ArXiv ID of the paper from the command line.
arxiv_id = sys.argv[1]

# Search for the paper by its ID.
search = arxiv.Search(id_list=[arxiv_id])
paper = next(search.results())

# Create a directory with the authors' last names and the year.
lastnames = [author.name.split(" ")[-1] for author in paper.authors]
dirname = os.path.join("content/publication/" +
                       str(paper.published.year) + "-" + "-".join(lastnames))
# Create directory if it doesn't exist.
if not os.path.exists(dirname):
    os.makedirs(dirname)

# Query the BibTex citation at https://arxiv.org/bibtex/2305.16710
response = requests.get("https://arxiv.org/bibtex/"+arxiv_id)
# Write the response to a file named cite.bib
with open(dirname+"/cite.bib", "w") as f:
    f.write(response.text)

# Get the title and authors of the paper.
title = paper.title
authors = "\n  ".join([f"- {author.name}" for author in paper.authors])
# Get the date of publication.
date = paper.published.strftime("%Y-%m-%d")
# Get the abstract of the paper.
abstract = paper.summary.replace("\n", " ")
# Get the journal reference if it exists, otherwise use the arXiv ID.
if paper.journal_ref:
    publication = paper.journal_ref
    pub_type = "2"
else:
    publication = "arXiv:"+arxiv_id
    pub_type = "3"

# Generate the text of the index.md file.
text_of_index = f"""---
title: {title}
subtitle: ''
summary: ''
authors:
  {authors}
tags:
categories: []
date: '{date}'
lastmod: {date}T19:33:00-05:00
featured: false
draft: false
projects: []
publishDate: '{date}T00:33:00.091248Z'
publication_types:
  - '{pub_type}'
abstract: "{abstract}"
publication: '{publication}'
url_pdf: https://arxiv.org/pdf/{arxiv_id}.pdf
# links:
#   - name: Journal
#     url: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.107.012209
---
"""

# Write the index.md file.
with open(dirname+"/index.md", "w") as f:
    f.write(text_of_index)
