---
title: "Numerical Analysis"
summary: ""
authors: []
tags: []
categories: []
show_date: false
reading_time: false  # Show estimated reading time?
share: false  # Show social sharing links?
profile: false  # Show author profile?
comments: false  # Show comments?

weight: 20

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

The problem of outer boundary conditions for partial differential equations on unbounded domains has a long history that goes back to Sommerfeld. There have been significant developments in the treatment of artificial outer boundaries, particularly since the 1970s, with the rise and prominence of numerical methods. Such boundary treatments have various names, such as absorbing, complete, radiative, non-reflective, and transparent. We group them into two main categories: local and exact. 

Local methods are convenient but approximate; exact methods are accurate but cumbersome.

Geometric intuition and computational experience suggest that **hyperboloical compactification** is unique among the existing treatments of the outer boundary problem in the numerical literature: it is **local _and_ exact**. In addition, the method leads to stable and efficient numerical implementations. This project will demonstrate these properties rigorously and provide guidelines for the optimal choice of free parameters in spacetime transformations.
