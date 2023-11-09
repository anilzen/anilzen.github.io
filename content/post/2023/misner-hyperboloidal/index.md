---
title: Misner's work on hyperboloidal surfaces
subtitle: Artificial cosmology over the rainbow
summary: The last three papers by Charles W. Misner were about the hyperboloidal approach. This post is a short review of these papers.

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

I attended the [memorial symposium](https://science.umd.edu/events/misner-memorial.html) for Charles W. Misner at the University of Maryland on November 11, 2023. There were many talks on his contributions to physics. Nobody mentioned his work on the hyperboloidal approach, so I thought I would write a short post on this for those few people who might be interested.

Most relativists know of [Charles W. Misner](https://en.wikipedia.org/wiki/Charles_W._Misner) because of his book MTW[^1].  I consider myself more the Wald type than the MTW so my exposure to Misner's work was first through his papers on the hyperboloidal evolution problem. The last three papers that Misner submitted to the arXiv were on the hyperboloidal approach. 
- [Hyperboloidal Slices and Artificial Cosmology for Numerical Relativity](https://arxiv.org/abs/gr-qc/0409073) (2004) published as part of Deserfest [here](https://www.worldscientific.com/worldscibooks/10.1142/5688)
- [Over the Rainbow: Numerical Relativity beyond Scri+](https://arxiv.org/abs/gr-qc/0512167) (2005)
- [Excising das All: Evolving Maxwell waves beyond scri](https://arxiv.org/abs/gr-qc/0603034) with James R. van Meter and David R. Fiske (2006).

The first two submissions are his thoughts while the last one is a refereed paper published in PRD. The basic ideas are shared in all three papers.

## The coordinates
The main ideas are clearly laid out in his [first paper](https://arxiv.org/abs/gr-qc/0409073) published for Stanley Deser's fest. The rest is commentary, demonstration, and further development.
## The ideas
Future null infinity, affectionately called scri+ by relativists [^2], is an incoming null hypersurface. 

The de Sitter metric in 1+1 dimensions on the static patch reads
$$ ds^2 = - f dt^2 + \frac{1}{f} dr^2, \quad f = 1-\frac{r^2}{L^2}. $$
I'm neglecting the spherical section; it's irrelevant for our discussion. 

I will present the discussion in the framework of [hyperboloidal scri-fixing](publication/zenginoglu-2008-hyperboloidal/). We introduce a new time coordinate
$$ \tau = t + h(r).$$ 
The de Sitter metric becomes
$$ ds^2 = - f d\tau^2 + 2 f H d\tau dr + \frac{1-f^2 H^2}{f} dr^2. $$
The resulting metric is regular at the points where $f$ vanishes if at those points $fH \sim 1$. 

The particular choice below
$$ f H = - \frac{r^2}{L^2}$$ 
takes us to the de Sitter metric in Kerr-Schild form
$$ ds^2 = - f d\tau^2 - \frac{2 r^2}{L^2} d\tau dr + \left(1+\frac{r^2}{L^2}\right) dr^2. $$
To see that this metric has Kerr-Schild form, we write it as
$$ ds^2 = - d\tau^2 + dr^2 + \frac{r^2}{L^2} \left(d\tau - dr\right)^2. $$
The cosmological horizon, $r=L$ is an ingoing null surface, similar to $\mathscr I$. Below is a conformal diagram of the time slices. The metric is manifestly regular at the cosmological horizon. In principle, no further transformations are needed to evolve the spacetime beyond the cosmological horizon. This transformation is already "hyperboloidal."

Misner does another transformation
$$ T = \tau - \sqrt{1+r^2}. $$
This is a hyperboloidal transformation in Minkowski space but it's awkward to apply it in the geometry of de Sitter space because the asymptotic behavior of the transformation doesn't match the causal structure. Even though it's  not helpful, let's write down the metric
$$ ds^2 = -f d\tau^2 - 2 \left( \frac{r}{L^2} + \frac{f}{\sqrt{1+r^2}} \right) d\tau dr $$ 
$$ + \frac{L^2 + r^2 + 2 r^4 - 2r^3\sqrt{1+r^2}}{L^2 (1+r^2)} dr^2. $$
Here is the conformal diagram.

I think this transformation does nothing interesting or useful. The Kerr-Schild form of the de Sitter metric is already hyperboloidal, in the sense that the time slices cross the cosmological horizon regularly as spacelike surfaces. We could leave it there.

Misner introduces the compactification
$$ r = \frac{\rho}{1-\rho^2/4}, $$
which maps $\mathscr I^+$ to $\rho=2$. I won't write down the resulting metric. It's also not clear to me why you would want to compactify. We are interested in the cosmological horizon, and slightly beyond. Bringing the spacelike infinity closer may or may not be a good idea.

## Einstein equations
I've been fairly critical of the transformations employed for the de Sitter metric. It's clear that, if you want to evolve fields accurately in asymptotically de Sitter spacetimes, these are not good choices. But Misner's goal is not to evolve fields on the background of asymptotically de Sitter spacetimes. His goal is to evolve Einstein equations.

In that case, I think adding a small cosmological constant is a very promising idea. Let me first describe how I understand this idea.

#### Small cosmological constant for hyperboloidal evolutions in asymptotically flat spacetimes
We solve the conformal Einstein equations with a small cosmological constant
$$ R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} + \frac{3}{L^2} g_{\mu\nu} = S(\Omega,\nabla), $$
where the conformal source terms are
$$ S(\Omega,\nabla) =  $$
The essential problem in the asymptotically flat case is that the conformal source terms are formally singular at infinity where $\Omega=0$. But with the cosmological constant, we are not interested in the boundary at infinity. Instead, we aim to extract the gravitational waves at the cosmoloigical horizon. At the limit of large $L$, the resulting radiation field should match the radiation field in the asymptotically flat case.

Numerically, the outer boundary is at a spacelike surface where the conformal factor is small but non-vanishing. **The conformal fact doesn’t vanish anywhere on the numerical grid**, so the conformal source functions are regular. As the surface is spacelike, you don’t need boundary conditions. You can then find the ingoing null surface near the outer boundary that corresponds to the cosmological horizon. 

If this works, there will be some questions. 
- Where is the cosmological horizon? Just take the outermost infoing null surface on your grid. 
- How do you define the radiation field? Apply the same construction reading off the analog of a news function at the cosmological horizon.
- Is this procedure is well-defined? Depends on what you mean by well-defined. Mathematically, no. Numerically, yes. If it works, we would just compare the results with the asymptotically flat case and see how close they are for small $L$. 
- Einstein equations don’t have viscosity, but we still add it to simulations. We could show convergence for smaller Lambdas just like we show convergence for small viscosity terms. We could also argue that Lambda doesn’t vanish in the real Universe, even though its impact is insignificant. 

Ok, there's enough to complain about it but we won't know unless we try. Is it worth trying though?

#### Why add a cosmological constant?
- It is well-known that de Sitter spacetimes are “more stable” than asymptotically flat spacetimes. Friedrich demonstrated the stability of asymptotically de Sitter spacetimes in 1986, long before the stability of Minkowski spacetimes was proven. We also know from Bizon and Rostworowski that AdS is globally unstable. The flat case is, in a very imprecise sense, at the edge of stability with respect to the cosmological constant. A positive constant moves us towards better stability.
- This setup emulates excision at the black hole horizon. What happens at spatial infinity with the hyperboloidal approach is causally similar to what happens at the bifurcation sphere with Schwarzschild coordinates. People realized 70 years ago that you could resolve the coordinate singularity at the bifurcation sphere using coordinates known since the golden 20s (Eddington, Gullstrand, and Painleve). The singularity at spatial infinity, however, wasn’t seen. We resolve it using coordinates known since Minkowski himself (hyperboloids). But then we stop. We don’t do what excision does. In numerical relativity, excision came in the late 80’s. They use horizon penetrating coordinates and put their inner boundary somewhere inside the black hole. They don’t try to find the event horizon during the simulation and put the boundary there. This might even be unstable for all I know. Why don’t we do the same? For one, the spacetime beyond infinity is not well-defined. But if we add a cosmological constant, however small, the conformal diagram looks exactly the same as the conformal diagram of a black hole, with the spacelike singularity replaced by a spacelike scri. The cosmological horizon now plays the role of flat scri as an ingoing null hypersurface. If the cosmological constant is sufficiently small, the solution will be sufficiently close to the asymptotically flat case. 





[^1]: The title of the book is [Gravitation](https://en.wikipedia.org/wiki/Gravitation_(book)) but it is known as MTW because of the authors Misner, Thorne, and Wheeler.
[^scri]: In relativity, you get five different types of infinity. Future timelike, future null, spatial, past null, and past timelike. We designate them with various forms of the letter "i" in the diagrams and figures. The "script i" is commonly used for the null infinities. Scri is shortspeak for script i. The future and past scris are distinguished by the plus and minus signs. $\scri$.