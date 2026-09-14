---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Nonlinear Einstein Equations for Gravitational Wave Astronomy"
summary: "Connecting numerical relativity to null infinity through hyperboloidal evolution and gravitational-wave extraction."
lastmod: "2026-09-14"
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

Developing robust hyperboloidal evolutions of the nonlinear Einstein equations for gravitational-wave astronomy is a central goal of my research. Compactification introduces formally singular terms near null infinity, so the formulation and gauge choices must preserve regularity and numerical stability.

I proposed an approach for the ["Hyperboloidal evolution with the Einstein equations"](/publication/2008-zenginoglu-hyperboloidal-einstein-evolution/) in 2008. The idea is to prescribe the conformal factor explicitly and choose a gauge that ensures the regularity of each of the formally singular terms. I had implemented this approach in spherical symmetry in my [thesis](/publication/2007-zenginoglu-conformal-numerical-relativity/) but the method was not sufficiently robust. I spent many years trying to improve the method but without success.

Work in the wider community includes Alex Vañó-Viñuales's [hyperboloidal black-hole evolutions in spherical symmetry](https://arxiv.org/abs/2304.05384) and David Hilditch's [dual-foliation formulations](https://arxiv.org/abs/1509.02071). Our [2025 topical collection](/publication/2025-hilditch-hyperboloidal-collection/) provides an overview of developments connecting mathematical relativity, numerical methods, and astrophysics.

## Recent results

In [*Perturbative Hyperboloidal Extraction of Gravitational Waves in 3+1 Numerical Relativity*](/publication/2025-bernuzzi-hyperboloidal-extraction/) (*Physical Review D*, 2025), we use data from an interior numerical relativity simulation to drive a perturbative evolution reaching null infinity. This provides a practical connection between existing simulations and hyperboloidal wave extraction. The exterior propagation is perturbative and does not capture nonlinear propagation effects.

Our study [*Late-time tails in nonlinear evolutions of merging black holes*](/publication/2024-de-amicis-late-time-tails/) (*Physical Review Letters*, 2025) identifies late-time gravitational-wave tails in fully nonlinear simulations and compares them with perturbative calculations. This comparison helps connect the asymptotic behavior predicted by perturbation theory with signals from nonlinear spacetimes.

## Longer-term goal

My goal is to contribute to hyperboloidal formulations that evolve the full nonlinear spacetime through to null infinity. This involves resolving questions of gauge choice, regularity, and stability while retaining the computational efficiency needed for astrophysical simulations.
