---
title: Jealous of hyperbolic fish
subtitle: Time transformations make space hyperbolic 
summary: If you are a physicist jealous of hyperbolic fish living in [Escher](https://en.wikipedia.org/wiki/M._C._Escher)'s [Circle Limit III](https://en.wikipedia.org/wiki/Circle_Limit_III), I have good news for you! The asymptotic geometry of space is hyperbolic if you want it to be.

projects: []
date: "2022-01-23T00:00:00Z"
lastmod: "2022-01-23T00:00:00Z"
draft: false
math: true
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
- infinity
- hyperboloidal
- hyperbolic
- 
categories:
- Research
---

Inspired by the following tweet from the great [Quanta Magazine](https://www.quantamagazine.org/).
{{< tweet 1478861128553971718 >}}

### Kusturica against Wallace
The featured image on the tweet above shows [Escher](https://en.wikipedia.org/wiki/M._C._Escher) 's [Circle Limit III](https://en.wikipedia.org/wiki/Circle_Limit_III) depicting the Poincaré model of hyperbolic geometry. Escher made [four](https://mathstat.slu.edu/escher/index.php/Circle_Limit_Exploration) such demonstrations of hyperbolic geometry. These woodcuts are fruits of a collaboration between Escher and the brilliant geometer [Coxeter](https://en.wikipedia.org/wiki/Harold_Scott_MacDonald_Coxeter). Coxeter was fascinated by Escher's drawings and sent him a reprint of one of his lectures, which kindled Escher's interest in constructing an infinitely repeating pattern in a finite figure. The [story](http://www.ams.org/publicoutreach/feature-column/fcarc-circle-limit) of how Escher managed to draw these images, is fascinating.

The original [Quanta article](https://www.quantamagazine.org/cosmologists-close-in-on-logical-laws-for-the-big-bang-20211110/) in the tweet above reports the difficulties in constructing something like the AdS/CFT correspondence for physical spacetimes. While we have a satisfying realization of holographic duality on anti-de Sitter spacetimes, a similar construction on flat or de Sitter spacetimes has been elusive, supposedly because these spacetimes do not possess hyperbolic geometry. A week after the tweet above, there was another [Quanta article](https://www.quantamagazine.org/symmetries-reveal-clues-about-the-holographic-universe-20220112/) with hyperbolic geometry as its featured image. There is some hype around hyperbolic geometry.

The main argument is that spatial slices of AdS are hyperbolic, which seems to be essential for the construction of AdS/CFT, so living in hyperbolic geometry would make it easier to construct quantum gravity. The fish in Escher's drawing may already know quantum gravity.

>The fish doesn't think because the fish knows everything.
>
> [Kusturica](https://en.wikipedia.org/wiki/Emir_Kusturica) (1993) from the movie [Arizona Dream](https://en.wikipedia.org/wiki/Arizona_Dream)

We are, however, not like those fish; we want to discover quantum gravity. The obstacle remains that our physical models for spacetime are either asymptotically flat (for isolated systems) or de Sitter (for cosmology).

I argue below that there is no need to be jealous of the fish. We do live in hyperbolic geometry; we just don't know it yet. 

> There are these two young fish swimming along and they happen to meet an older fish swimming the other way, who nods at them and says "Morning, boys. How's the water?" And the two young fish swim on for a bit, and then eventually one of them looks over at the other and goes "What the hell is water?"
>
> [Wallace](https://en.wikipedia.org/wiki/David_Foster_Wallace) (2005) from his commencement speech [This Is Water](https://en.wikipedia.org/wiki/This_Is_Water).

### Little fish, big fish

Let's start with a short review of the hyperbolic fish in Escher's drawing. Hyperbolic geometry is typically introduced in a fictitious higher dimensional Minkowski space using the equation for a hyperboloid in Cartesian coordinates. I'll be using spherical coordinates foreshadowing an application below, so we have the Minkowski space with line element
$$ ds^2_{\rm{Mink}} = -dt^2 + dr^2 + r^2 d\sigma^2,$$
where $d\sigma^2=d\sigma^2+\sin^2\theta \ d\varphi^2$ is the metric on the usual unit sphere. 

Just like the unit sphere is the set of points at unit Euclidean distance from the origin, the unit hyperboloid is the set of points at unit Minkowski distance from the origin: the hyperboloid is simply a (pseudo)sphere of Minkowski spacetime 
$$-t^2+r^2=-1. \tag{1} \label{1}$$

We already have the first hint that we live in hyperbolic geometry! The hyperboloid describes the [kinematic space of special relativity](../../hyperbolic-relativity/). But this was rather anticlimactic so let's go a bit further.

We can derive and represent the intrinsic metric of hyperbolic geometry in various equivalent ways. For example, setting $t=\cosh \xi$ and $r=\sinh \xi$ satisfies the equation for the hyperboloid (\ref{1}) identically, and gives us the hyperbolic line element
$$ ds^2_{\mathbb{H}^3} = d\xi^2+ \sinh^2\xi \ d\sigma^2.$$
Note the similarity of this hyperbolic metric with the metric on the unit sphere.
We will use slightly different coordinates. Instead of introducing hyperbolic functions, we solve (\ref{1}) directly
$$ t = \sqrt{1+r^2}. \tag{2} \label{2} $$
Replacing the $dt$ term with the differential of this relation in the Minkowski metric, we get
$$ ds^2_{\mathbb{H}^3} = \textcolor{purple}{\frac{1}{1+r^2}dr^2 + r^2 d\sigma^2}.  \tag{3} \label{3} $$

Escher's image shows hyperbolic geometry not in the hyperboloid model but as a disk. To map the hyperboloid model with its infinite range in $r$ to the unit [Poincaré disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model), we relabel the radial points using
$$ r = \frac{2\rho}{1-\rho^2}. \tag{4}\label{4}$$
We get the familiar [line element for the Poincaré ball](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model#Metric_and_curvature)[^1]
$$ ds^2_{\mathbb{H}^3} = \textcolor{darkorange}{\frac{4}{1-\rho^2}\left( d\rho^2 + \rho^2 d\sigma^2 \right)}. $$
The metric blows up near the boundary, which is how Escher packs the infinitely many fish in a repeating pattern into the disk. Remember that the fish have the same size. The Poincaré disk is a conformal model of hyperbolic geometry distorting sizes but keeping the shapes (or rather local angles) invariant, so the fish actually don't know that they are packed so densely, contrary to claims about their omniscient nature[^2]. As far as the fish are concerned, they might think they live in flat space :wink:.

### Swimming in anti-de Sitter
The reason for all the hype around hyperbolic geometry among quanta is that spatial cuts of AdS are hyperbolic. In fact, AdS is introduced very similarly to hyperbolic geometry: starting with a fictitious higher dimensional Minkowski space. This Minkowski space, however, has two time dimensions (which is rather awkward): $ds^2 = -dt_1^2 - dt_2^2 + dr^2 + r^2 d\sigma^2$. We write the hyperboloid as $-t_1^2-t_2^2+r^2=-1$. This relation is solved identically by $t_1 = \sqrt{1+r^2} \cos t$ and $t_2 = \sqrt{1+r^2} \sin t$, giving the [AdS metric in global coordinates](https://en.wikipedia.org/wiki/Anti-de_Sitter_space#Global_coordinates)
$$ ds^2_{\rm{AdS}} = - \left(1+r^2\right) dt^2 + \textcolor{purple}{\frac{1}{1+r^2} dr^2 + r^2 d\sigma^2},$$
AdS spacetime has many [counterintuitive aspects]((https://arxiv.org/abs/1611.01118)); it's not even stable against [perturbations](https://arxiv.org/abs/1312.5544). But you can immediately see that its $t$ slices have hyperbolic geometry by comparing them to the metric (\ref{3}). The hyperbolic geometry of the $t$ slices is the crucial aspect for quantum gravity.

I promised you an end to jealousy, but so far, I've just been pressing on the wound. The question remains: how do we obtain from our usual flat spacetime with line element
$$ ds^2_{\rm{Mink}} = -dt^2 + dr^2 + r^2 d\sigma^2$$
the hyperbolic three-metric as time slices? Yes, we get the kinematic space of special relativity, but that's not a spacetime metric; time is missing! Considering the usual time slices, there is nothing hyperbolic about the flat geometry of $dr^2 + r^2 d\sigma^2$. 

### Time heals all wounds

In relativity, there is no notion of absolute time; we can develop our own simultaneity to connect observers and call it a proper day. The geometry of the three-space is not invariant but depends on a choice of time. Many familiar notions such as simultaneity, volume, area become unfamiliar through such reparametrizations of spacetime. 

The choice of time also determines whether the geometry of the three-space is Euclidean or hyperbolic. You are free to pick your preferred time coordinate so let's pick a time that makes space hyperbolic and end the jealousy.

We've already seen this when we encountered the kinematic space of special relativity in our derivation of the hyperboloid model of hyperbolic geometry. Now, instead of finding intrinsic coordinates as in (\ref{2}), we introduce a new time coordinate as
$$ \tau = t - \sqrt{1+r^2}. \tag{5} \label{5} $$
The resulting metric is not a two-dimensional intrinsic spatial metric but a transformed Minkowski metric with timelike, null, and spacelike directions
$$ ds^2 = -d\tau^2 - \frac{2r}{\sqrt{1+r^2}} d\tau dr + \textcolor{purple}{\frac{1}{1+r^2} dr^2 + r^2 d\sigma^2}.$$
Voilà! The $\tau$ slices have hyperbolic geometry. The transformation (\ref{4}) brings us to a foliation whose sections are given by the Poincaré ball
$$ ds^2 = -d\tau^2 + \frac{8\rho}{(1-\rho^2)^2} d\tau d\rho + \textcolor{darkorange}{\frac{4}{(1-\rho^2)^2} \left( d\rho^2 + \rho^2 d\sigma^2\right)}.$$
Note that this metric is still the flat Minkowski metric with all its usual geometric properties, such as vanishing curvature. The difference is that the points along the [ideal boundary](https://en.wikipedia.org/wiki/End_(topology)) do not sit on spatial infinity but null infinity. In fact, the cuts $\rho=1$ along each $\tau$ slice corresponds to what is nowadays called a celestial sphere. These transformations 

The ideal boundary seems like an ideal place for quantum gravity.

### Hyperbolic de Sitter
The Quanta article discusses the difficulties in constructing an AdS/CFT correspondence in de Sitter spacetimes. One can use coordinates to make the time slices hyperbolic. In this case, the transformations are a bit more tricky. Consider the de Sitter metric in static coordinates
$$ ds^2_{\rm{dS}} = - \left(1-r^2\right) dt^2 + \frac{1}{1-r^2} dr^2 + r^2 d\sigma^2.$$
The metric is singular at $r=1$, corresponding to the [cosmological horizon](https://en.wikipedia.org/wiki/Cosmological_horizon). The horizon singularity is a coordinate singularity similar to the singularity at the black hole horizon of Schwarzschild spacetime.

The de Sitter space has a very different conformal geometry. For one, infinity is spacelike (as opposed to timelike for AdS and null for Minkowski). This throws people off, but there is a solution: the cosmological horizon.

Here's the monstrous transformation that gets us to hyperbolic time slices
$$ r = \sinh \xi \sinh \tau, \qquad t = \mathrm{arccosh} \left(\frac{\cosh \tau}{\sqrt{1-\sinh^2 \xi \sinh^2\tau}}\right) $$
The transformed metric is comparatively simple
$$ ds^2_{\rm{dS}} = - d\tau^2 + \sinh ^2 \tau \left( d\xi^2 + \sinh^2\xi\ d\sigma^2 \right).$$
We recognize the hyperbolic geometry on $\tau=$const. slices. Abusing notation and using the same letter for $r=\sinh\xi$, we get
$$ ds^2_{\rm{dS}} = - d\tau^2 + \sinh ^2 \tau \left( \textcolor{purple}{\frac{1}{1+r^2} dr^2 + r^2 d\sigma^2} \right).$$
Again, we recognize the hyperbolic metric in purple. The Poincaré disk follows from a simple relabeling of the radial points (\ref{4}). This representation of the de Sitter metric is called [open slicing](https://en.wikipedia.org/wiki/De_Sitter_space#Open_slicing). I'm ignoring subtleties, such as the domain of transformations and the region covered by coordinates in the conformal diagram. My goal is simply to demonstrate that you can choose to live in hyperbolic geometry if you want to, even in de Sitter spacetimes.

The problem with the de Sitter metric in open slicing is its time-dependence. Especially for numerical studies, coordinates in which the metric is explicitly static are preferable. A better approach to construct a hyperbolic slicing is to consider the static patch and make a transformation similar to the flat case. First we push the horizon to infinity 
$$ r_* = \int \frac{1}{1-r^2}dr = \rm{arctanh} \ r $$
The de Sitter metric on the static patch becomes
$$ ds^2_{\rm{dS}} = \frac{1}{\cosh^2 r_*} \left(-dt^2 + dr_*^2 \right)  +\tanh^2 r_* d\sigma^2. $$
Now we can do the same transformation as in (\ref{5}), take $\tau=$const., and get the following metric on the time slices
<!-- $$ ds^2_{\rm{dS}} = \frac{1}{\cosh^2 r_*} \left(-d\tau^2 - \frac{2r_*}{\sqrt{1+r_*^2}} d\tau dr + \frac{1}{1+r_*^2} dr_*^2 \right)  +\tanh^2 r_* d\sigma^2. $$ -->
$$ \frac{1}{\cosh^2 r_*} \left(\frac{1}{1+r_*^2} dr_*^2 + \sinh^2 r_* d\sigma^2 \right). $$
This is not quite the hyperbolic metric, but has other nice properties for numerical calculations that I'll write about in another post.


### This is Water
The point of this post is that you can find a suitable time slice on which space is hyperbolic. There is nothing to be jealous about the little fish, big fish, swimming in Escher's hyperbolic space. It may well be that physically motivated time slices of flat spacetime are naturally hyperbolic but we don't experience it because the speed of light is so large. 

Are these time transformations physically motivated? What do they mean? Doesn't a preferred time slice contradict the principle of covariance? I'll leave those questions for another post. 

Enjoy the swim.


[^1]: To get the disk model, just replace $d\sigma^2$ with $d\theta^2$.
[^2]: The fish could, in principle, find out that they do live in hyperbolic space by making local measurements of curvature.
