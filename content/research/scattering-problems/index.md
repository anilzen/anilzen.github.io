---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Scattering Problems for Engineering"
summary: ""
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

The definition of the radar section involves the ratio of the scattered field to the incident field at the limit to infinity. The problem is posed on an unbounded domain. However, numerical computations typically replace the infinite solution domain with a finite numerical domain. The approximate radiation field is then measured just a few wavelengths away from the source based on rules of thumb. Obtaining higher accuracy requires either access to large spatial sections of the solution space, sophisticated extraction procedures, or near-to-far-field transformations.

Hyperboloidal compactification solves this problem efficiently. This project will demonstrate the applications of this relativistic method to scattering problems that arise in engineering and technology.