---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Swarm-Based Gradient Descent Method for Non-Convex Optimization
subtitle: ''
summary: ''
authors:
- Jingcheng Lu 
- Eitan Tadmor
- Anıl Zenginoğlu
tags: []
categories: []
date: '2022-11-01'
lastmod: 
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: ''
publication_types:
- '3'
abstract: >
  We introduce a new Swarm-Based Gradient Descent (SBGD) method for non-convex optimization. The swarm consists of agents, each is identified with a position, $\mathbf{x}$, and mass, $m$. The key to their dynamics is communication: masses are being transferred from agents at high ground to low(-est) ground. At the same time, agents change positions with step size, $h=h(\mathbf{x},m)$, adjusted to their relative mass: heavier agents proceed with small time-steps in the direction of local gradient, while lighter agents take larger time-steps based on a backtracking protocol. Accordingly, the crowd of agents is dynamically divided between "heavier'' leaders, expected to approach local minima, and "lighter'' explorers. With their large-step protocol, explorers are expected to encounter improved position for the swarm; if they do, then they assume the role of `heavy' swarm leaders and so on. Convergence analysis and numerical simulations in one-, two-, and 20-dimensional benchmarks demonstrate the effectiveness of SBGD as a global optimizer.
publication: ''
url_pdf: https://arxiv.org/pdf/2211.17157.pdf
# links:
#   - name: Journal
#     url: https://iopscience.iop.org/article/10.1088/0264-9381/25/19/195025/meta
---
