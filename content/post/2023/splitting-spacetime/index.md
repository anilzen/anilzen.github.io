---
title: Splitting spacetime
subtitle: How space and time may arise from bubble clusters constituting the quantum foam.
summary: Hyperboloidal hypersurfaces provide a *natural* way to split spacetime into space and time. Their mathematical definition connects to a physical principle that may be useful in understanding the quantum foam.

projects: []
date: "2023-09-18T00:01:00Z"
draft: false
featured: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 0
  preview_only: true

authors:
- anil

tags:
- hyperboloidal
- holography

categories:
---

## Predicting the future
Contrary to common belief, physicists are in the business of making predictions more than fortune tellers or astrologers. The hows and whys, the fundamentals and principles, "[whether or not the world has three dimensions](https://www.azquotes.com/quote/351820)," all boil down to one question: Can you predict the future?

Predicting the future for a physicist is, of course, a much more accurate undertaking than for fortune tellers, astrologers, or [economists](https://www.yahoo.com/news/finance/news/wall-street-economists-consistently-wrong-171740454.html). We want to say what happens to certain well-defined variables describing the mathematical idealization of a natural system given a snapshot in time[^snap]. 

We call this process "solving an initial value problem." We solve an equation of motion, typically a partial differential equation (PDE), with prescribed initial data. The PDE is our model of the physical system. That's where all the whys and hows go. It describes how the chosen variables of the system vary in relation to each other. The initial data is the snapshot of these variables at a given time. The solution to this initial value problem is our prediction of the future.

The language of a snapshot in time refers to a distinction between time and space. But didn't special relativity teach us that time and space are not separate? Well, it did, and it didn't. Special relativity taught us that the notion of time and simultaneity is observer-dependent. But time is still a special dimension in a relativistic spacetime, distinct from its spatial friends. For example, the dimension with the opposite sign in the metric signature, $(-+++)$, is the time dimension. Time is special.

To formulate an initial value problem, we need to split spacetime into space and time. In relativity, there are three approaches to splitting spacetime to formulate an initial value problem: Cauchy, characteristic, and hyperboloidal. To demonstrate these approaches in a simple case, take the flat, 1+1 dimensional spacetime. In standard coordinates $(t,r)$, the flat metric reads
$$ ds^2 = -dt^2 + dr^2 \tag{1} \label{1} $$ 
The immediate approach is to take the snapshot at $t=0$. The corresponding surface is called a [Cauchy surface](https://en.wikipedia.org/wiki/Cauchy_surface) and has specific desirable properties that generalize to more interesting cases. The associated [Cauchy problem](https://ems.press/books/esi/66) plays a central role in mathematical and numerical relativity.

We also have null surfaces in relativity. This null cone is fundamental in many aspects. First, it provides the [causal structure of spacetime](https://plato.stanford.edu/entries/spacetime-singularities/lightcone.html). Secondly, it plays a fundamental role in describing the propagation of disturbances. In particular, massless fields propagate along the null cone. Even before the advent of relativity, it was known that disturbances to solutions of wave equations propagate along these special surfaces called characteristics: $t\pm r$. One can provide data on such characteristic surfaces and solve a [characteristic evolution problem](https://link.springer.com/article/10.12942/lrr-2012-2). This approach is particularly valuable in the modern era of gravitational-wave astronomy because gravitational waves are only defined at infinity along these null directions.

## Hyperboloidal surfaces

The hyperboloidal approach is the odd one. You take a spacetime hyperboloid, say 
$t^2 - r^2 = 1,$
and give initial data on the surface defined by 
$t(r) = \sqrt{1+r^2}.$ 
This construction seems weird and arbitrary when you first encounter it. Why would you do something like this? Is the surface even spacelike everywhere? Why not pick another transformation?

Many people feel that hyperboloidal surfaces are somewhat unnatural, lacking the elegance and simplicity of the Cauchy or characteristic approaches. Below, I compile a list of arguments for the naturalness and effectiveness of hyperboloidal surfaces in splitting spacetime into space and time. These arguments shall not only answer the above questions but also provide a deeper understanding of the nature of spacetime.

### Mathematical definition
_Hyperboloids correspond to spheres in spacetime._

![Hyperboloid](./hyperboloid.png "A spacetime hyperboloid. Time's up.")

The circle has one of the purest definitions in mathematics: a circle is a set of points equidistant from a given point. To derive the equation for a circle, consider the Euclidean metric in two dimensions
$$ ds^2 = dx^2 + dy^2. $$
The set of points that are at a distance $R$ from the origin is given by 
$$ x^2 + y^2 = R^2. $$
The curvature of the circle is the reciprocal of its radius, $K=1/R$. This is the simplest nontrivial example of a constant curvature surface.

Now, let's ask ourselves the corresponding question in relativity: what is the set of points equidistant from a given point? In the relativistic setting, the distance refers to proper time. The set of points that are at proper time $T$ from the origin for the Minkowski metric in \eqref{1} is given by
$$ - t^2 + r^2 = \pm T^2. $$
This equation describes a spacetime hyperbola. The sign in the equation determines whether the hyperbola is spacelike or timelike[^sign]. The future sheet of the spacelike hyperbola 
$$ t = \sqrt{T^2+r^2},$$
consists of the set of points at proper time $T$ from the origin. This surface also has constant curvature, $K=1/T$, just like the circle above. Just like the higher dimensional analog of a circle is the sphere, the higher dimensional version of a hyperbola is the hyperboloid.

We see that hyperboloids are the relativistic analogs of spheres. Hyperboloids are as natural in Lorentzian manifolds as spheres are in Riemannian manifolds.

### Physical principle
_Hyperboloids correspond to soap bubbles in spacetime._

![Soap bubble cluster](./featured.jpg "A soap bubble cluster as a mental image for quantum foam. By [Kym Cox](https://www.kymcox.com/work-statement-exhibitions).")

The circle has another attractive property: among all figures with a given area, the circle has the smallest perimeter. We've known this for over 2,000 years[^zenod]. The corresponding statement for the sphere has only been proven in the 19th century by [Schwarz](https://en.wikipedia.org/wiki/Hermann_Schwarz). This kind of optimization problem appears in many areas, from economics to biophysics. One that is familiar to most people, starting with early childhood, is the soap bubble.

In mathematical terms, soap bubbles are minimal surfaces enclosing a fixed air volume. This variational problem has the following action
$$ S = Area + \lambda \cdot Volume. \tag{2} \label{2} $$
The task is to minimize the area with the constraint that the volume is fixed. The mathematics of soap bubbles is a fascinating topic with many [recent developments](https://www.quantamagazine.org/monumental-math-proof-solves-triple-bubble-problem-and-more-20221006/). Frank Morgan, who proved the [double bubble theorem](https://en.wikipedia.org/wiki/Double_bubble_theorem), has a wonderful lecture on the topic.

{{< youtube CbpfpxOdUzU >}}
<br>
Here's a particularly nice quote from the lecture

> "If you want to understand the universe, start out by understanding the soap bubble."
> 
> Frank Morgan

So, let's try to understand the universe by understanding the soap bubble. First, we must answer the following question:

**What is the relativistic analog of a soap bubble?** 

Formally, we can simply use the action for the soap bubble \eqref{2} and go one dimension higher.
$$ S = V + \lambda \cdot W, \tag{3}\label{3} $$
where we denote $V$ for volume and $W$ for spacetime volume. There is a geometric (coordinate-free) approach to discuss these terms, but we'll stick to coordinates. We compute the relativistic volume by integrating the square root of the determinant of the metric[^asd]. Denoting the determinant of the induced metric on the hypersurface by $h$ and the determinant of the spacetime metric by $g$, we have 
$$ S = \int \sqrt{h}\ d^3x + \lambda \int \sqrt{-g}\ d^4x. $$
The extremization of this action leads to the requirement of constant mean curvature: $K = \lambda$, where $K$ is the trace of the extrinsic curvature[^brill]. 

Let's do this for the 1+1 Minkowski metric to find an expression for the maximizer. We are looking for an embedding, $t=t(r)$, that extremizes (maximizes in this case) the action for the relativistic bubble. The induced metric is given by
$$ ds^2 = -dt^2 + dr^2 = \left(-t'^2 + 1\right) dr^2, $$
where $t'\equiv dt(r)/dr$. We have
$$ V = \int \sqrt{h} \ dr = \int_0^R \sqrt{1-t'^2}\ dr. $$
To calculate the spacetime volume, we need a reference surface. It turns out that it doesn't matter what that surface is for our purposes, so let's just take the surface $t=0$. The spacetime volume is then given by 
$$ W = \int \sqrt{-g}\ d^2x = \int_0^R dr \int_0^{t(r)} dt = \int_0^R t(r) dr. $$
Bringing these expressions together in the action \eqref{3}, we can read off the Lagrangian density
$$ \mathscr{L} = \sqrt{1-t'^2} + \lambda t. $$
The Euler-Lagrange equation for varying $t(r)$ with respect to the parameter $r$ reads
$$ \frac{d}{dr} \frac{\partial\mathscr{L}}{\partial t'} = \frac{\partial \mathscr{L}}{\partial t}.$$
We get
$$ \frac{d}{dr} \frac{t'}{\sqrt{1-t'^2}} = \lambda. $$
Integrate by $r$ and solve for $t'$ to get (up to constants of integration)
$$ t'(r) = \pm \frac{\lambda r}{\sqrt{1+ \lambda^2 r^2}}. $$
By choosing the positive sign and integrating again, we get the equation for the spacetime hyperboloid 
$$ t(r) = \sqrt{\frac{1}{\lambda^2} + r^2}. $$
We recognize the mean extrinsic curvature as $K=1/\lambda$ from our previous discussion on the relativistic analog of a circle. The hyperboloid is the relativistic analog of a soap bubble.

You may wonder what determines the value of the constant mean curvature. It is the spacetime volume. The larger the spacetime volume, the smaller the constant mean curvature. This is the same as for a soap bubble. The larger the volume of air that the bubble needs to enclose, the smaller the curvature of the bubble, which generalizes to bubble clusters enclosing multiple volumes of air. 

## Quantum foam

It has been long predicted that spacetime shouldn't be smooth at the Planck scale due to quantum fluctuations. It should be "foamy," or "bubbly," or "grainy," or whatever you want to call it. Wheeler, the naming authority of theoretical physics, called this the [quantum foam](https://en.wikipedia.org/wiki/Quantum_foam). A foam is defined as a dispersion of bubbles, and we have just seen that the relativistic generalization of a bubble is a hyperboloid. 

We don't know how the quantum foam can be formalized or tested. You can imagine that a spacetime bubble forms through a quantum fluctuation and splits into space and time through the attachment of constant mean curvature hypersurfaces, which, as a spacetime bubble cluster, form a hyperboloidal surface. I find this a helpful mental image to represent the quantum foam. And as usual, the mental image gives rise to further questions. What is the mechanism for the formation of such hyperboloids?

One idea is that the hypersurface arises through entanglement. I've written about [hyperboloidal holography](../../hyperboloidal-holography/), where I argued that holographic entanglement entropy naturally extends to flat spacetime if we use spacetime hyperboloids as the time slices. The extremum principle for the hypersurface indicates that these surfaces could also be useful in the context of [quantum complexity](https://www.quantamagazine.org/in-new-paradox-black-holes-appear-to-evade-heat-death-20230606/). 

Bubble clusters may indeed be the key to understanding how space and time arise from spacetime.

![](./foam.jpg)

[^snap]: To be fair, not all physical theories focus on snapshots in time. There are theories formulated in terms of statistical ensembles, boundary value problems, or, as discussed in this post, variational principles. But there is a sense in which all these also arise from initial value problems under certain conditions. 
[^sign]: Timelike hyperbolas describe observers with uniform acceleration, called [Rindler observers](https://en.wikipedia.org/wiki/Rindler_coordinates), and play an important role in quantum field theory in curved spacetimes, among others.
[^zenod]: This statement in a slightly different form was first asserted by [Zenodorus](https://en.wikipedia.org/wiki/Zenodorus_(mathematician)), who stated that a circle has a greater area than any polygon with the same perimeter. You can find a lovely account of the evolution of the isoperimetric problem [here](https://maa.org/sites/default/files/pdf/upload_library/22/Ford/blasjo526.pdf).
[^asd]: To understand this formula, you need to learn about [volume forms](https://en.wikipedia.org/wiki/Volume_form).
[^brill]: I'm not going through the general calculation here but it's very short and can be found, for example, in the paper by [Brill, Cavallo, and Isenberg](https://pubs.aip.org/aip/jmp/article-abstract/21/12/2789/444574/K-surfaces-in-the-Schwarzschild-space-time-and-the) from 1980. 
