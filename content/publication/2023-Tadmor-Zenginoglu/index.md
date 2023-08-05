---
title: Swarm-Based Optimization with Random Descent
subtitle: ''
summary: ''
authors:
  - Eitan Tadmor
  - Anil Zenginoglu
tags:
categories: []
date: '2023-07-23'
lastmod: 2023-07-23T19:33:00-05:00
featured: false
draft: false
projects: []
publishDate: '2023-07-23T00:33:00.091248Z'
publication_types:
  - '3'
abstract: "We extend [our study](../2022-swarm-based-gradient-descent) of the swarm-based gradient descent method for non-convex optimization, to allow random descent directions. We recall that the swarm-based approach consists of a swarm of agents, each identified with a position, $x$, and mass, $m$. The key is the transfer of mass from high ground to low(-est) ground. The mass of an agent dictates its step size: lighter agents take larger steps. In this paper, the essential new feature is the choice of direction: rather than restricting the swarm to march in the steepest gradient descent, we let agents proceed in randomly chosen directions centered around -- but otherwise different from -- the gradient direction. The random search secures the descent property while at the same time, enabling greater exploration of ambient space. Convergence analysis and benchmark optimizations demonstrate the effectiveness of the swarm-based random descent method as a multi-dimensional global optimizer."
publication: 'arXiv:2307.12441'
url_pdf: https://arxiv.org/pdf/2307.12441.pdf
# links:
#   - name: Journal
#     url: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.107.012209
---
