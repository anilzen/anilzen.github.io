---
title: "Numerical Analysis"
summary: "Regularity, convergence, and efficient discretization of wave equations on compactified domains."
lastmod: "2026-09-14"
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

Hyperboloidal compactification represents an unbounded wave problem on a finite domain. The transformation brings infinity onto the grid, but the quality of a numerical solution still depends on regularity at the compactified boundary, the choice of coordinates, and the discretization. My work studies these connections between geometry and numerical analysis.

## Recent results

In [*A null infinity layer for wave scattering*](/publication/2021-zenginoglu-null-infinity-layer/) (*SIAM Journal on Scientific Computing*, 2026), I develop a compactified formulation of time-harmonic scattering and demonstrate finite difference, spectral, and finite element implementations.

With Markus Wess, I derive a conforming finite element formulation with bounded coefficients in [*Finite Elements for Helmholtz Scattering with Infinity as a Computational Boundary*](/publication/2026-wess-helmholtz-finite-elements/) (2026 preprint). The formulation includes a boundary term at compactified infinity and gives access to the far-field pattern. Our [online book](https://markuswess.github.io/hypFEM/intro.html) provides implementations and examples in NGSolve.

Two further 2026 preprints address time-domain evolution. With Ekrem Demirboğa, I study [scalar scattering across matched compactified domains](/publication/2026-demirboga-scalar-scattering/), including the effect of boundary regularity on convergence. With Sebastiano Bernuzzi and Andrea Nützi, I develop [homothetic hyperboloidal coordinates for semilinear wave tails](/publication/2026-zenginoglu-homothetic-tails/), adapting the coordinates to the scaling of the tail to make very late times accessible.

## Questions guiding the work

The central questions concern which compactifications preserve sufficient regularity, how to choose transformations for efficient computation, and how these choices interact with finite difference, spectral, and finite element methods. The goal is to understand both the capabilities and the limits of a numerical formulation, including cases where nonlinear terms reduce convergence near infinity.
