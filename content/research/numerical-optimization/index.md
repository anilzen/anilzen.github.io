---
title: "Numerical Optimization"
summary: "Swarm-based optimization for non-convex functions"
lastmod: "2026-09-14"
authors: []
tags: []
categories: []
show_date: false
reading_time: false  # Show estimated reading time?
share: false  # Show social sharing links?
profile: false  # Show author profile?
comments: false  # Show comments?
weight: 80

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Optional external URL for project (replaces project detail page).
external_link: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

With Eitan Tadmor and Jingcheng Lu, I study swarm-based methods for non-convex optimization. The methods use communicating agents whose positions and masses evolve together: mass transfer favors agents with lower objective values, while the agents' masses control their step sizes.

## Publications

[*Swarm-Based Gradient Descent Method for Non-Convex Optimization*](/publication/2022-lu-swarm-gradient-descent/) (*Communications of the American Mathematical Society*, 2024) introduces the method, combining convergence analysis with numerical benchmarks.

With Eitan Tadmor, I extend the approach to randomized descent directions in [*Swarm-Based Optimization with Random Descent*](/publication/2023-tadmor-swarm-random-descent/) (*Acta Applicandae Mathematicae*, 2024), allowing agents to explore directions around the gradient while preserving descent.

## Software

The [SwarmPy documentation](https://anilzen.github.io/swarmpy/) introduces the algorithms and provides code and examples.
