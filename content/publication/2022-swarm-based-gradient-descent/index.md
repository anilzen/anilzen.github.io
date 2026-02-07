---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Swarm-Based Gradient Descent Method for Non-Convex Optimization"
authors: 
- Jingcheng Lu
- Eitan Tadmor
- Anıl Zenginoğlu

date: 2022-11-01T16:52:40-05:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-12-07T16:52:40-05:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: "We introduce a new Swarm-Based Gradient Descent (SBGD) method for non-convex optimization. The swarm consists of agents, each is identified with a position, $x$, and mass, $m$. The key to their dynamics is communication: masses are being transferred from agents at high ground to low(-est) ground. At the same time, agents change positions with step size, $h=h(x,m)$, adjusted to their relative mass: heavier agents proceed with small time-steps in the direction of local gradient, while lighter agents take larger time-steps based on a backtracking protocol. Accordingly, the crowd of agents is dynamically divided between 'heavier' leaders, expected to approach local minima, and 'lighter' explorers. With their large-step protocol, explorers are expected to encounter improved position for the swarm; if they do, then they assume the role of 'heavy' swarm leaders and so on. Convergence analysis and numerical simulations in one-, two-, and 20-dimensional benchmarks demonstrate the effectiveness of SBGD as a global optimizer. "

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://arxiv.org/pdf/2211.17157.pdf
links:
  - name: arXiv
    url: https://arxiv.org/abs/2211.17157

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
