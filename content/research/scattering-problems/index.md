---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Scattering Problems for Engineering"
summary: "Computing scattering and far-field patterns with infinity as a computational boundary."
lastmod: "2026-09-14"
authors: []
tags: []
categories: []
show_date: false
reading_time: false  # Show estimated reading time?
share: false  # Show social sharing links?
profile: false  # Show author profile?
comments: false  # Show comments?

weight: 30

# Optional external URL for project (replaces project detail page).
external_link: ""

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

Wave propagation problems on unbounded domains are ubiquitous in computational mathematics, engineering, and technology, appearing in various domains such as ultrasonics, seismics, underwater acoustics, and electrodynamics. As a concrete example, consider the numerical computation of the radar cross-section of aircraft. Maxwell equations are solved numerically for the interaction of an incident electromagnetic wave with the aircraft.

![Scattering problem for an aircraft](./ka6d-arrows.webp "Scattering problem for an aircraft. Image from [0911.3456](https://arxiv.org/abs/0911.3456).")

Scattering observables depend on the radiation field far from the source. My approach uses compactification and a rescaling of the outgoing field to make infinity a computational boundary, giving direct access to far-field information.

## Results and current work

[*A null infinity layer for wave scattering*](/publication/2021-zenginoglu-null-infinity-layer/) (*SIAM Journal on Scientific Computing*, 2026) develops this approach for time-harmonic scattering. The transformations are restricted to a layer around the interior domain, and the paper demonstrates several numerical discretizations in one and two dimensions.

With Markus Wess, I extend the construction to conforming finite elements in [*Finite Elements for Helmholtz Scattering with Infinity as a Computational Boundary*](/publication/2026-wess-helmholtz-finite-elements/) (2026 preprint). We compare the method with perfectly matched layers in two- and three-dimensional Helmholtz benchmarks, including trapping geometries and a submarine benchmark.

[*From Penrose to Melrose: Computing Scattering Amplitudes at Infinity for Unbounded Media*](/publication/2026-zenginoglu-penrose-melrose/) (2026 preprint) treats variable media, including media with long-range asymptotics. It constructs a solver near infinity that can be coupled to an interior solver through domain decomposition.

## Online book and code

Our book [*Hyperboloidal Compactification in NGSolve*](https://markuswess.github.io/hypFEM/intro.html) explains the finite element implementation and includes executable frequency-domain and time-domain examples. The [hypFEM repository](https://github.com/markuswess/hypFEM) contains the source code. The demonstrated Helmholtz problems provide a basis for exploring further applications in acoustics and other areas of wave propagation.
