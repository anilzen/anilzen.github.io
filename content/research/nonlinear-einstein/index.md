---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Nonlinear Einstein Equations for Gravitational Wave Astronomy"
summary: ""
authors: []
tags: []
categories: []
show_date: false
reading_time: false  # Show estimated reading time?
share: false  # Show social sharing links?
profile: false  # Show author profile?
comments: false  # Show comments?
weight: 50

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

One of the most important open problems with the hyperboloidal method is its application to the nonlinear Einstein equations for gravitational wave astronomy. The problem is that the compactification introduces formally singular terms that are numerically unstable.

I proposed an approach for the ["Hyperboloidal evolution with the Einstein equations"](/publication/zenginoglu-2008-einstein/) in 2008. The idea is to prescribe the conformal factor explicitly and choose a gauge that ensures the regularity of each of the formally singular terms. I had implemented this approach in spherical symmetry in my [thesis](/publication/zenginoglu-2007-conformal/) but the method was not sufficiently robust. I spent many years trying to improve the method but without success.

In the recent years, Alex Vañó-Viñuales made [significant progress](https://arxiv.org/abs/2304.05384) on this problem. A related approach based on the [dual-frame formalism](https://arxiv.org/abs/1509.02071) is pursued by David Hilditch and collaborators.

I still consider the application of hyperboloidal compactification to a common formulation of the nonlinear Einstein equations as the most important open problem in the field. My goal in this project is to contribute to the solution of this problem. While this is a high-risk project, a successful implementation would lead to a breakthrough in the numerical computation of astrophysically relevant spacetimes.