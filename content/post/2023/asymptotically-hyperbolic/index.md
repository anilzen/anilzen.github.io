---
title: Hyperboloidal surfaces are asymptotically hyperbolic
subtitle: 
summary: A frequently asked objection to hyperboloidal surfaces is that they are asymptotically null. This is not true.

projects: []
date: "2023-10-03T00:01:00Z"
draft: true
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
  
categories:
---

A fairly common confusion about hyperboloidal surfaces is their causal nature at infinity. 

## Objection
This confusion already arises for the standard hyperboloid
$$ t^2-r^2 = 1.  \tag{1} \label{1} $$
Looking at this surface on a $t$-$r$ diagram, it clearly looks like it approaches the outgoing null cone emanating from the origin.


Ok, so maybe that's just a silly argument based on simple high-school math. The hyperbola has the asymptote $t=r$, which is null, so the hyperboloid must be asymptotically null. Duh! 

But we are trained relativists. Let's do something a bit more sophisticated and demonstrate once and for all that these surfaces are indeed asymptotically null.

The causal nature of a surface can be determined by calculating the norm of its normal vector, which is simply the gradient of the defining function. Consider the defining function for the hyperboloid
$$ \tau(t,r) = t - \sqrt{1+r^2} $$
The normal to this hypersurface is proportional to the gradient
$$ n_\mu \sim \partial_\mu \tau = \left(1, -\frac{r}{\sqrt{1+r^2}}\right). $$
This surface is spacelike for any finite $r$ but clearly the normal approaches a null vector as $\lim_{r\to\infty} n_\mu = (1,-1)$. We must admit that the surface is asymptotically null.


## Resolution

### Penrose diagram
If you're familiar with Penrose diagrams, you can immediately see that the hyperboloid does not become null anywhere. 


### Conformal structure
The standard coordinates are not suitable for discussing asymptotic causal structure. Instead, we need to use the conformal metric $\bar{g}$, which is related to the physical metric $g$ by
$$ \bar{g} = \Omega^2 g, $$
where $\Omega$ is a conformal factor. 

### Hyperbolic geometry
The hyperboloid in \eqref{1} gives the hyperboloid model for hyperbolic space. It's a textbook example when mathematicians with little interest in relativity discuss hyperbolic geometry.

Hyperbolic space is a Riemannian manifold. Its boundary is referred to as the ideal boundary. Now, the remarkable thing about hyperbolic space is that it's a homogeneous manifold. Specifically, it's the unique homogeneous space with constant negative curvature. 

If the hyperboloid _were_ to be asymptotically null, the surface would not be homogeneous. Instead, it would have a location dependent extrinsic curvature. Specifically, the mean extrinsic curvature would be unbounded. 



### An asymptotically null surface
To provide contrast and build intuition, here's an asymptotically null surface.
$$ w = t - \sqrt{\frac{1}{r}+r^2}. $$
The Penrose diagram for this surface is shown below.

<!-- ![Penrose diagram for asymptotically null surface](asymptotically-null.png) -->

The mean curvature of this surface is unbounded as the geometric intuition suggests.
$$ K = \frac{1}{2r^2\sqrt{r}+1}. $$



