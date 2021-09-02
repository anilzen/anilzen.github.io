---
title: How far is infinity?
subtitle: Infinity may be closer than you think
summary: Infinity may be closer than you think

projects: []
date: "2021-05-01T00:00:00Z"
lastmod: "2021-05-01T00:00:00Z"
draft: false
math: true
featured: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: '' #'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- anil

tags:
- 

categories:
- 
---
Most of my research uses infinity in numerical computations. When presenting my work, I often encounter the objection that infinity is not physical. But not all infinities are created equal, and some are more physical than others. In fact, we can **experimentally verify** that we are at infinity with respect to distant sources of radiation.

Below I collect some thoughts on infinity and the relation between mathematical models and physical reality. Feel free to skip my ramblings and go directly to the [experiment](#a-thought-experiment).

### We don't need no infinity

Physicists are generally uncomfortable with infinity. First, it is argued, infinity cannot be the outcome of a physical experiment. Second, infinity as the outcome of a calculation indicates problems with the theory. Resolving such problems may initiate interesting research directions such as [renormalization techniques](https://en.wikipedia.org/wiki/Renormalization). Since infinity doesn't make sense in experiment and should be avoided in theory, physicists are skeptical when it appears in mathematical descriptions of physical phenomena. For example, Max Tegmark argues that infinity is an idea that should be [retired from physics](https://www.edge.org/response-detail/25344). Nicolas Gisin aims to [understand time](https://www.quantamagazine.org/does-time-really-flow-new-clues-come-from-a-century-old-approach-to-math-20200407/) without relying on infinitely precise numbers. Here is a quote from [The physics of infinity](https://www.nature.com/articles/s41567-018-0238-1) by Ellis, Meissner, and Nicolai:
>We maintain that in each physical case where $\infty$ is used in a discussion, greater insight is attained by considering what large number $N$ will suffice instead, because real physics is embodied in that number.


This uneasiness of physicists with infinity is shared with some mathematicians as well. There are mathematical philosophies and formalisms without infinity that physicists can rely on, such as [finitism](https://en.wikipedia.org/wiki/Finitism) or [intuitionism](https://en.wikipedia.org/wiki/Intuitionism). I was attracted to similar ideas when I was in college, so I went down the rabbit hole of [fuzzy numbers](https://en.wikipedia.org/wiki/Fuzzy_number). They seemed like a "natural" way to represent physical measurements which are not real numbers with infinite precision but fuzzy numbers with uncertainties. However, the more I learned about fuzzy numbers, the less I was convinced of their general utility. They seemed rather cumbersome and did not ease calculations in most cases. I learned, by way of fuzzy numbers, that successful mathematical representations do not necessarily match our physical intuitions. We should use the most powerful mathematical tools that give us the best quantitative description of our measurements. That's why we should keep infinity around. 

### Empirical infinity
Aristotle distinguishes [two notions of infinity](https://en.wikipedia.org/wiki/Actual_infinity): actual and potential. Potential infinity is what children learn first: numbers just keep going "forever". Actual infinity is the completion of this process: the set of all numbers as a mathematical object.

We do not observe infinity directly. But we can use it to represent our impression. For example, in projective geometry the point at which two parallel lines meet is infinitely far away. When you're painting, you may allow both sides of a road to meet on your canvas to indicate an endless road. We all know that the road ends somewhere but the painting suggests that the meeting point is beyond the horizon of perception. The mathematical representation for the idea of "far" on your canvas is infinity. 

I think the infinity represented on your canvas is neither actual nor potential, but empirical. Empirical concepts are abstracted from individual perceptions. Infinity is the best canvas representation of your perception looking down a long, unending road. You don't know how far you can see, and you don't care about representing that particular detail in your painting. You just want to express that it's very far. 

### A thought experiment

The experiment involves perturbing a black hole and measuring how these perturbations decay at astronomical distances from the black hole. Luckily, we don't have to perturb the black hole ourselves, astrophysics takes care of it. But to measure the perturbations I'm talking about, you would need very accurate gravitational wave detectors. We are not there yet, so I'm just describing a reasonable thought experiment.

The experiment uses the difference between observations of black hole perturbations at infinity and at a finite distance. After some oscillations, perturbations of a black hole decay with a power-law $ \sim 1/t^p$ where $t$ is time as measured by the observer and $p$ is the decay rate[^1]. Surprisingly, the decay rate is different depending on where you observe the perturbations. Focusing on the lowest mode perturbations, at finite distances the asymptotic decay rate is 3 whereas at infinity the decay rate is 2. The slower decay rate at infinity is surprising. Before the calculation of the decay rate at infinity in 1994[^2], some even argued that the decay is non-radiative, in the sense that it wouldn't be detected at infinity. There are explanations of this slower decay in terms of accumulation of backscattering off of curvature towards infinity, but this is not our main concern. Given that the rates at finite distances and at infinity are different, we can ask the following question:

Which decay rate would we observe?

The answer determines whether infinity is the appropriate model for where we are in relation to the source of the radiation. And, as you may have guessed, we would observe the decay rate associated with infinity. 


### Wrap-up


I think most people agree that actual infinity does not exist in the real world. But one can also argue that the number 3 doesn't exist in the real world. Numbers are useful concepts abstracted from observations and represented in mathematical models. Similarly, infinity is a useful concept in describing astrophysical observations. We should embrace empirical infinity and its appearance in our formalisms. Especially if it improves our calculations.





[^1]: This was first discussed in detail by Richard Price in his 1972 paper [Nonspherical Perturbations of Relativistic Gravitational Collapse. I. Scalar and Gravitational Perturbations](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.5.2419). The power-law decay was part of an important theorem which stated that inhomogeneities in a black hole spacetime are radiated away. 
[^2]: C. Gundlach, R. H. Price, and J. Pullin. [Late-time behavior of stellar collapse and explosions. I. Linearized perturbations.](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.49.883) Physical Review D 49.2, 883 (1994).
[^3]: G. F. R. Ellis, K. A. Meissner, and H. Nicolai. . Nature Physics 14, 770–772 (2018). 
