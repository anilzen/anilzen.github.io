---
title: Jealous of hyperbolic fish
subtitle: Time transformations make space hyperbolic 
summary: If you are a physicist jealous of hyperbolic fish living in [Escher](https://en.wikipedia.org/wiki/M._C._Escher)'s [Circle Limit III](https://en.wikipedia.org/wiki/Circle_Limit_III), I have good news for you! The asymptotic geometry of space is hyperbolic if you want it to be.

projects: []
date: "2022-01-23T00:00:00Z"
lastmod: "2022-01-23T00:00:00Z"
draft: false
featured: false

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
{{< tweet user="QuantaMagazine" id="1478861128553971718" >}}

### Kusturica against Wallace
The featured image on the tweet above shows [Escher](https://en.wikipedia.org/wiki/M._C._Escher)'s [Circle Limit III](https://en.wikipedia.org/wiki/Circle_Limit_III) depicting the Poincaré model of hyperbolic geometry. Escher was interested in constructing an infinitely repeating pattern in a finite figure. When the brilliant geometer [Coxeter](https://en.wikipedia.org/wiki/Harold_Scott_MacDonald_Coxeter) shared with him a reprint of one of his lectures on hyperbolic geometry, Escher figured out how to create such [tessalations](https://en.wikipedia.org/wiki/Tessellation). The [story](http://www.ams.org/publicoutreach/feature-column/fcarc-circle-limit) of how Escher managed to create these [four woodcuts](https://mathstat.slu.edu/escher/index.php/Circle_Limit_Exploration) is fascinating.

The original [Quanta article](https://www.quantamagazine.org/cosmologists-close-in-on-logical-laws-for-the-big-bang-20211110/) in the tweet above reports the difficulties in constructing something like the [AdS/CFT correspondence](https://en.wikipedia.org/wiki/AdS/CFT_correspondence) for physical spacetimes. While we have a realization of holographic duality based on anti-de Sitter spacetimes, a similar construction on flat or de Sitter spacetimes has been elusive, supposedly because these spacetimes do not possess hyperbolic geometry. A week after the tweet above, there was another [Quanta article](https://www.quantamagazine.org/symmetries-reveal-clues-about-the-holographic-universe-20220112/) with hyperbolic geometry as its featured image. Clearly, there is some hype around hyperbolic geometry.

The main argument is that spatial slices of AdS are hyperbolic, which seems to be essential for AdS/CFT, so living in hyperbolic geometry makes it easier for the fish in Escher's drawing to know quantum gravity.

>The fish doesn't think because the fish knows everything.
>
> [Kusturica](https://en.wikipedia.org/wiki/Emir_Kusturica) (1993) from the movie [Arizona Dream](https://en.wikipedia.org/wiki/Arizona_Dream)

We are, however, not like those fish; we want to discover quantum gravity. The obstacle remains that our physical models for spacetime are either asymptotically flat (for isolated systems) or de Sitter (for cosmology).

I argue below that there is no need to be jealous of the fish. We do live in hyperbolic geometry; we just don't know it yet. 

> There are these two young fish swimming along and they happen to meet an older fish swimming the other way, who nods at them and says "Morning, boys. How's the water?" And the two young fish swim on for a bit, and then eventually one of them looks over at the other and goes "What the hell is water?"
>
> [Wallace](https://en.wikipedia.org/wiki/David_Foster_Wallace) (2005) from his commencement speech [This Is Water](https://en.wikipedia.org/wiki/This_Is_Water).

### Little fish, big fish

Let's start with a short review of the hyperbolic fish in Escher's drawing. Hyperbolic geometry is typically introduced in a fictitious higher dimensional Minkowski space using the equation for a [hyperboloid](https://en.wikipedia.org/wiki/Hyperboloid) in Cartesian coordinates. I'll be using spherical coordinates foreshadowing an application below, so we have the Minkowski space with line element
$$ ds^2_{\rm{Mink}} = -dt^2 + dr^2 + r^2 d\sigma^2,$$
where $d\sigma^2=d\sigma^2+\sin^2\theta \ d\varphi^2$, the usual metric on the unit sphere. 

Spheres and hyperboloids may seem very different, but they are analogous to each other. Just like the unit sphere is the set of points at unit Euclidean distance from the origin, the unit hyperboloid is the set of points at unit Minkowski distance from the origin: the hyperboloid is simply a (pseudo)sphere of Minkowski space 
$$t^2-r^2=1. \tag{1} \label{1}$$

We already have the first hint that we live in hyperbolic geometry! The hyperboloid describes the [kinematic space of special relativity](../../hyperbolic-relativity/). But this was rather anticlimactic so let's go a bit further.

We can derive and represent the intrinsic metric of hyperbolic geometry in various equivalent ways. For example, setting $t=\cosh \xi$ and $r=\sinh \xi$ satisfies the equation for the hyperboloid (\ref{1}) identically, and gives us the hyperbolic line element
$$ ds^2_{\mathbb{H}^3} = d\xi^2+ \sinh^2\xi \ d\sigma^2.$$
Note the similarity of this hyperbolic metric with the metric on the unit sphere.
Coordinates are labels and it's helpful to see hyperbolic geometry in different representations. Instead of introducing hyperbolic functions, let's solve (\ref{1}) directly
$$ t = \sqrt{1+r^2}. \tag{2} \label{2} $$
Replacing the $dt$ term with the differential of this relation in the Minkowski metric, we get
$$ ds^2_{\mathbb{H}^3} = \textcolor{purple}{\frac{1}{1+r^2}dr^2 + r^2 d\sigma^2}.  \tag{3} \label{3} $$

To get Escher's image of a disk, we need to map the hyperboloid model with its infinite range in $r$ to the unit [Poincaré disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model). We relabel the radial points using
$$ r = \frac{2\rho}{1-\rho^2}, \tag{4}\label{4}$$
and obtain the familiar [line element for the Poincaré ball](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model#Metric_and_curvature)[^1]
$$ ds^2_{\mathbb{H}^3} = \textcolor{darkorange}{\frac{4}{(1-\rho^2)^2}\left( d\rho^2 + \rho^2 d\sigma^2 \right)}. $$
The metric blows up near the boundary, which is how Escher packs the infinitely many fish in a repeating pattern into the disk. Remember that the fish have the same size. The Poincaré disk is a conformal model of hyperbolic geometry distorting sizes but keeping the shapes (or rather local angles) invariant, so the fish actually don't know that they are packed so densely, contrary to claims about their omniscient nature. As far as the fish are concerned, they don't see the distortions and might even think they live in flat space[^2] :wink:.

### Swimming in anti-de Sitter
The hype around hyperbolic geometry among quanta is because cuts of AdS are hyperbolic spaces. In fact, AdS is introduced very similarly to hyperbolic geometry---starting with a fictitious higher dimensional Minkowski space. This Minkowski space, however, has two time dimensions (which is rather awkward): $ds^2 = -dt_1^2 - dt_2^2 + dr^2 + r^2 d\sigma^2$. We write the hyperboloid as $-t_1^2-t_2^2+r^2=-1$. This relation can be solved identically by $t_1 = \sqrt{1+r^2} \cos t$ and $t_2 = \sqrt{1+r^2} \sin t$, giving the [AdS metric in global coordinates](https://en.wikipedia.org/wiki/Anti-de_Sitter_space#Global_coordinates)
$$ ds^2_{\rm{AdS}} = - \left(1+r^2\right) dt^2 + \textcolor{purple}{\frac{1}{1+r^2} dr^2 + r^2 d\sigma^2}.$$
AdS spacetime has many [counterintuitive aspects](https://arxiv.org/abs/1611.01118); it's not even stable against small [perturbations](https://arxiv.org/abs/1312.5544). But you can immediately see that its $t$-slices have hyperbolic geometry by comparing them to the metric (\ref{3}), which is the crucial aspect for quantum gravity.

I promised you to end your jealousy, but so far, I've just been pressing on the wound. The question remains: how do we go from our usual flat spacetime with line element
$$ ds^2_{\rm{Mink}} = -dt^2 + dr^2 + r^2 d\sigma^2$$
to the hyperbolic three-metric as time slices? Yes, we've encountered the kinematic space of special relativity, but that's not a spacetime metric---time is missing! Considering the usual time slices, there is nothing hyperbolic about the flat geometry of $dr^2 + r^2 d\sigma^2$. 

### Time heals all wounds

In relativity, there is no notion of absolute time; we can develop our own simultaneity to connect observers and call it a proper day. Therefore, the geometry of the three-space connecting these observers is also not invariant but depends on a choice of time. Many familiar notions such as simultaneity, volume, area become unfamiliar through such reparametrizations of spacetime. 

The choice of time also determines whether the geometry of the three-space is Euclidean or hyperbolic. We are free to pick our preferred time coordinate, so let's pick a time that makes space hyperbolic and end the jealousy.

We've already seen this when we encountered the kinematic space of special relativity in our derivation of the hyperboloid model of hyperbolic geometry. Now, instead of finding intrinsic coordinates as in (\ref{2}), we introduce a new time coordinate as
$$ \tau = t - \sqrt{1+r^2}. \tag{5} \label{5} $$
The resulting metric is not a three-dimensional intrinsic spatial metric but a transformed Minkowski metric with timelike, null, and spacelike directions
$$ ds^2_{\rm{Mink}} = -d\tau^2 - \frac{2r}{\sqrt{1+r^2}} d\tau dr + \textcolor{purple}{\frac{1}{1+r^2} dr^2 + r^2 d\sigma^2}.$$
Voilà! The $\tau$ slices have hyperbolic geometry. Relabeling the radial points as in (\ref{4}) brings us to a foliation whose sections are the Poincaré balls
$$ ds^2_{\rm{Mink}} = -d\tau^2 + \frac{8\rho}{(1-\rho^2)^2} d\tau d\rho + \textcolor{darkorange}{\frac{4}{(1-\rho^2)^2} \left( d\rho^2 + \rho^2 d\sigma^2\right)}.$$
Note that this metric is still the flat Minkowski metric with all its usual geometric properties, such as vanishing curvature. The important difference is that the points along the [ideal boundary](https://en.wikipedia.org/wiki/End_(topology)) do not sit at spatial infinity but null infinity. The cuts $\rho=1$ along each $\tau$ slice corresponds to what is called a celestial sphere. This allows us to make the connection back to quantum gravity, because the celestial sphere is indeed the stage for an attempt at a [holographic description](../../hyperboloidal-holography/) called [celestial holography](https://arxiv.org/abs/2107.02075).

The ideal boundary seems like an ideal place for quantum gravity.

### Hyperbolic de Sitter
The [Quanta article](https://www.quantamagazine.org/cosmologists-close-in-on-logical-laws-for-the-big-bang-20211110/) discusses the difficulties in constructing an AdS/CFT correspondence in de Sitter spacetimes. Again, we can use coordinates to make the time slices of de Sitter hyperbolic, but the transformations are a bit tricky because de Sitter space has a different conformal geometry. For example, conformal infinity is spacelike (as opposed to timelike for AdS and null for Minkowski). 

There is another infinity in de Sitter that depends on coordinates and is useful for us. Consider the de Sitter metric in static coordinates
$$ ds^2_{\rm{dS}} = - \left(1-r^2\right) dt^2 + \frac{1}{1-r^2} dr^2 + r^2 d\sigma^2.$$
The singularity at $r=1$ corresponds to the [cosmological horizon](https://en.wikipedia.org/wiki/Cosmological_horizon). The horizon singularity is a coordinate singularity similar to the singularity at the black hole horizon of Schwarzschild spacetime.

Here's the transformation that gets us to hyperbolic time slices
$$ r = \sinh \xi \sinh \tau, \qquad \cosh t = \frac{\cosh \tau}{\sqrt{1-\sinh^2 \xi \sinh^2\tau}} $$
The transformed metric is comparatively simple
$$ ds^2_{\rm{dS}} = - d\tau^2 + \sinh ^2 \tau \left( d\xi^2 + \sinh^2\xi\ d\sigma^2 \right).$$
We recognize the hyperbolic geometry on $\tau=$const. slices. Alternatively, we can abuse notation and use the same letter for $r=\sinh\xi$ to get the purple representation of the hyperbolic metric 
$$ ds^2_{\rm{dS}} = - d\tau^2 + \sinh ^2 \tau \left( \textcolor{purple}{\frac{1}{1+r^2} dr^2 + r^2 d\sigma^2} \right).$$
The Poincaré disk follows from a simple relabeling of the radial points (\ref{4}). This representation of the de Sitter metric is called [open slicing](https://en.wikipedia.org/wiki/De_Sitter_space#Open_slicing). I'm ignoring subtleties, such as the domain of transformations and the region covered by coordinates in the conformal diagram. We still see that we can choose to live in hyperbolic geometry if we want to, even in de Sitter spacetimes.

The problem with the de Sitter metric in open slicing is its time-dependence. Especially for numerical studies, coordinates in which the metric is explicitly static are preferable. A better approach to construct a hyperbolic slicing is to consider the static patch and make a transformation similar to the flat case. First we push the horizon to infinity 
$$ r_\ast = \int \frac{1}{1-r^2}dr = \mathrm{arctanh} \ r. $$
The de Sitter metric on the static patch becomes
$$ ds^2_{\mathrm{dS}} = \frac{1}{\cosh^2 r_\ast} \left( -dt^2 + dr_\ast^2 \right) + \tanh^2 r_\ast d\sigma^2. $$
Now we can do the same transformation as in (\ref{5}), take $\tau=$const., and get the following metric on the time slices
$$ \frac{1}{\cosh^2 r_\ast} \left(\frac{1}{1+r_\ast^2} dr_\ast^2 + \sinh^2 r_\ast d\sigma^2 \right). $$
This metric is not quite the hyperbolic metric, but has other nice properties for numerical calculations that I'll write about in another post.


### This is Water
The point of this post is that you can find suitable coordinates that make space hyperbolic. There is nothing to be jealous about Escher's fish. It may well be that physically motivated time slices of flat spacetime are naturally hyperbolic but we don't experience it because the speed of light is so large. 

Are these time transformations physically motivated? What do they mean? Doesn't a preferred time slice contradict the principle of covariance? I'll leave those questions for another post. 

Enjoy the swim.


[^1]: To get the disk model, just replace $d\sigma^2$ with $d\theta^2$.
[^2]: The fish could, in principle, find out that they do live in hyperbolic space by making local measurements of *intrinsic* curvature.


<script src="https://giscus.app/client.js"
        data-repo="anilzen/anilzen.github.io"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzNzExMzY1Njk="
        data-category="General"
        data-category-id="DIC_kwDOFh8YOc4CTAsV"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="1"
        data-input-position="top"
        data-theme="dark"
        data-lang="en"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>