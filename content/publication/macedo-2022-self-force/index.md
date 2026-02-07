---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Hyperboloidal method for frequency-domain self-force calculations
subtitle: ''
summary: ''
authors:
- Rodrigo Panosso Macedo
- Benjamin Leather
- Niels Warburton
- Barry Wardell
- Anıl Zenginoğlu
tags: []
categories: []
date: '2022-02-01'
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
- "article-journal"
abstract: >
  Gravitational self-force theory is the leading approach for modeling gravitational wave emission from small mass-ratio compact binaries. This method perturbatively expands the metric of the binary in powers of the mass ratio. The source for the perturbations depends on the orbital configuration, calculational approach, and the order of the perturbative expansion. These sources fall into three broad classes: (i) distributional, (ii) worldtube, and (iii) unbounded support. The latter, in particular, is important for emerging second-order (in the mass ratio) calculations. Traditional frequency domain approaches employ the variation of parameters method and compute the perturbation on standard time slices with numerical boundary conditions supplied at finite radius from series expansions of the asymptotic behavior. This approach has been very successful, but the boundary conditions calculations are tedious, and the approach is not well suited to unbounded sources where homogeneous solutions must be computed at all radii. This work develops an alternative approach where hyperboloidal slices foliate the spacetime, and compactifying coordinates simplify the boundary treatment. We implement this approach with a multi-domain spectral solver with analytic mesh refinement and use the scalar-field self-force on circular orbits around a Schwarzschild black hole as an example problem. The method works efficiently for all three source classes encountered in self-force calculations and has distinct advantages over the traditional approach. For example, our code efficiently computes the perturbation for orbits with extremely large orbital radii ($r_p>10^5 M$) or modes with very high spherical harmonic mode index ($\ell \geq 100$). Our results indicate that hyperboloidal methods can play an essential role in self-force calculations. 
publication: '*Physical Review D*'
url_pdf: https://arxiv.org/pdf/2202.01794.pdf
links:
  - name: Journal
    url: https://journals.aps.org/prd/abstract/10.1103/PhysRevD.105.104033
---
