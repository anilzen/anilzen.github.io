---
title: Symmetric integration of the 1+1 Teukolsky equation on hyperboloidal foliations of Kerr spacetimes
subtitle: ''
summary: ''
authors:
  - Charalampos Markakis
  - Sean Bray
  - Anıl Zenginoğlu
tags: [perturbation-theory]
categories: [NSF Award]
date: '2023-03-14'
lastmod: 2023-03-14T19:33:00-05:00
featured: false
draft: false
projects: [Perturbation Theory]
publishDate: '2023-03-14T00:33:00.091248Z'
publication_types:
  - '3'
abstract: "This work outlines a fast, high-precision time-domain solver for scalar, electromagnetic and gravitational perturbations on hyperboloidal foliations of Kerr space-times. Time-domain Teukolsky equation solvers have typically used explicit methods, which numerically violate Noether symmetries and are Courant-limited. These restrictions can limit the performance of explicit schemes when simulating long-time extreme mass ratio inspirals, expected to appear in LISA band for 2-5 years. We thus explore symmetric (exponential, Padé or Hermite) integrators, which are unconditionally stable and known to preserve certain Noether symmetries and phase-space volume. For linear hyperbolic equations, these implicit integrators can be cast in explicit form, making them well-suited for long-time evolution of black hole perturbations. The 1+1 modal Teukolsky equation is discretized in space using polynomial collocation methods and reduced to a linear system of ordinary differential equations, coupled via mode-coupling arrays and discretized (matrix) differential operators. We use a matricization technique to cast the mode-coupled system in a form amenable to a method-of-lines framework, which simplifies numerical implementation and enables efficient parallelization on CPU and GPU architectures. We test our numerical code by studying late-time tails of Kerr spacetime perturbations in the sub-extremal and extremal cases."
publication: 'arXiv:2303.08153'
url_pdf: https://arxiv.org/pdf/2303.08153.pdf
# links:
#   - name: Journal
#     url: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.107.012209
---
