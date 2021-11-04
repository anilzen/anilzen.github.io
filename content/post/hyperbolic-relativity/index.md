---
title: Special relativity and hyperbolic geometry
subtitle: Hyperboloids as a natural framework for relativity and beyond
summary: Hyperbolic geometry provides a natural setting for special relativity. This viewpoint simplifies calculations, provides insights into the theory, and has applications beyond special relativity in machine learning and general relativity.

projects: []
date: "2021-11-08T00:00:00Z"
lastmod: "2021-11-08T00:00:00Z"
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
- hyperboloidal
- history
- hyperbolic

categories:
- Research
---

The idea that space and time can bend and stretch is wild. I was blown away by it when I first encountered it as a young high schooler interested in physics and philosophy. To me, the recognition that natural laws dynamically govern space and time was a triumph of physics over philosophy, of empirical determination over [synthetic a priori](https://en.wikipedia.org/wiki/Analytic%E2%80%93synthetic_distinction#Kant's_version_and_the_a_priori_/_a_posteriori_distinction), of Einstein over Kant. 

As fascinated as I was by the theory, the formalism seemed relatively obscure. I recognized patterns in the Lorentz transformations but missed a deeper insight into the origins of this structure. At college, I considered various standard derivations of relativistic effects, such as the [relativistic aberration](https://en.wikipedia.org/wiki/Relativistic_aberration) or the [Thomas precession](https://en.wikipedia.org/wiki/Thomas_precession), tedious and boring.

A relatively simple example is Einstein's [velocity-addition formula](https://en.wikipedia.org/wiki/Velocity-addition_formula). In Galilean relativity, which corresponds to our everyday experience, you can simply add velocities. In special relativity, the speed of light is constant, so the addition of velocities must be such that no composition of velocities can get you beyond the speed of light. In the simplest case of collinear motion (velocities pointing in the same direction) velocity addition becomes speed addition and looks like this
$$ \tag{1} \label{1}
u = \frac{u_1+u_2}{1+\tfrac{u_1 u_2}{c^2}} $$
You can see how the speed of light, $c$, can never be exceeded with this composition law. While you can understand the result, it is not intuitively clear how this addition rule is related to the structure of space and time.

It turns out that these calculations have natural interpretations in hyperbolic geometry. This viewpoint not only simplifies the calculations but also provides deeper insights into the theory. Beyond relativity, it has practical applications even in machine learning. And it all starts with Minkowski.

### Hyperbole
In 1908, [Minkowski](https://en.wikipedia.org/wiki/Hermann_Minkowski) gave a [lecture](https://www.math.nyu.edu/~tschinke/papers/yuri/14minkowski/raum-und-zeit.pdf) about a new mathematical model for space and time. In his opening remarks, he stated boldly that space and time are mere shadows of a more fundamental union: spacetime. 

> Henceforth space by itself, and time by itself, are doomed to fade away into mere shadows, and only a kind of union of the two will preserve an independent reality.
>
> [Minkowski](https://en.wikipedia.org/wiki/Hermann_Minkowski) (1908)[^1]

The quote is by now famous. Since it appeared on the cover page of Synge's [textbook on relativity](https://www.amazon.com/Relativity-Special-J-L-Synge/dp/B000GP7PX4) in 1956, it has made its way to various outlets. But when Minkowski made the statement, it was considered hyperbole and encountered resistance from physicists and mathematicians alike.[^2] 

His spacetime view became widely celebrated in a few years after the lecture because of its central role in general relativity. In the same lecture, Minkowski also promoted a non-Euclidean approach to spacetime. As a Göttingen mathematics professor, it was clear to him that the geometry of special relativity is non-Euclidean, in particular, hyperbolic. This idea didn't gain traction as widely as the idea of spacetime. It is only in the last 20 years or so that there is renewed interest into the hyperbolic nature of special relativity. 

To see why hyperbolic geometry is the natural geometry for special relativity, consider a two-dimensional spacetime with coordinates $(t,x)$ and Minkowski metric
$$ ds^2 = -dt^2 + dx^2. $$
A natural object for a given metric is the set of points at unit distance from the origin. In two-dimensional Euclidean space, we get a circle, $x^2+y^2=1$. In two-dimensional Minkowski space, we get a hyperbola  
$$ \tag{2}\label{2} t^2 - x^2 = 1. $$
Minkowski's drawing below shows this hyperbola for $t>0$. In higher dimensions, you get the one-sheeted [hyperboloid](https://en.wikipedia.org/wiki/Hyperboloid), also called the hyperbolic hyperboloid.

![Minkowski Drawing](MinkDrawing.png "Minkowski's drawing depicting hyperbola as the invariant space under Lorentz transformations. <br>From [Minkowski’s modern world](https://halshs.archives-ouvertes.fr/halshs-01234434/) by Scott Walter.")

In his lecture, Minkowski demonstrated that Lorentz transformations are hyperbolic rotations that leave the hyperbola (\ref{2}) invariant. He died in January 1909 before he could develop this idea further, but it was embraced by others, particularly by [Sommerfeld](https://en.wikipedia.org/wiki/Arnold_Sommerfeld), [Varičak](https://en.wikipedia.org/wiki/Vladimir_Vari%C4%87ak), [Robb](https://en.wikipedia.org/wiki/Alfred_Robb), and [Borel](https://en.wikipedia.org/wiki/%C3%89mile_Borel). 

The mathematical formalism for a hyperbolic rotation is just like a regular rotation, except with hyperbolic functions instead of trigonometric functions. [Hyperbolic functions](https://en.wikipedia.org/wiki/Squeeze_mapping) are related to their trigonometric counterparts through [complex angles](https://en.wikipedia.org/wiki/Hyperbolic_functions#Complex_trigonometric_definitions). An intuitive way to think about the hyperbolic rotation is in terms of the [squeeze mapping](https://en.wikipedia.org/wiki/Squeeze_mapping), which should be familiar to anyone who has seen a Lorentz transformation on a space-time diagram.

![Squeeze Mapping](MinkBoost.gif "Lorentz boost as hyperbolic rotation or [squeeze mapping](https://en.wikipedia.org/wiki/Squeeze_mapping). <br>From [Wikimedia](https://commons.wikimedia.org/wiki/File:MinkBoost2.gif).")

We write Lorentz transformations as hyperbolic rotations with angle $w$:
$$ L(w)= \begin{pmatrix}
\cosh w & -\sinh w \\\\
-\sinh w & \cosh w 
\end{pmatrix} $$
The inverse is just rotation with the inverse angle, $L(w)^{-1}=L(-w)$. Multiplication rule goes as $L(w_1+w_2)=L(w_1)L(w_2)$. So you can simply add the hyperbolic angles instead of dealing with weird addition formulas.

We think in terms of velocities and speeds, not hyperbolic angles. Let's see what happens to speeds when we add the angles in hyperbolic geometry. Consider then, the Lorentz boost with relative speed $v$ between frames 
$$ L(v)= \begin{pmatrix}
\gamma & -\gamma \beta \\\\
-\gamma \beta & \gamma 
\end{pmatrix}, $$
where we defined the rescaled speed $\beta:=\tfrac{v}{c}$ and the Lorentz factor $\gamma:=1/\sqrt{1-\beta^2}$, with $c$ denoting the speed of light. The hyperbolic angle is related to the Lorentz factor through $\gamma=\cosh w$, and to the rescaled speed through $\beta=\tanh w$. So the Lorentz transformation is simply a rotation in hyperbolic space with an angle, $w$, related to the observer's speed as $v=c \ \mathrm{arctanh}\ w$.

Now what does the addition of hyperbolic angles, $w=w_1+w_2$, mean in terms of speeds?
$$ \beta = \tanh w = \tanh (w_1+w_2) = \frac{\tanh w_1+\tanh w_2}{1+\tanh w_1 \tanh w_2} = \frac{\beta_1+\beta_2}{1+\beta_1 \beta_2}. $$
Einstein's velocity addition (\ref{1}) becomes a simple consequence of hyperbolic identities. 

There is much more that one can simplify or understand from this viewpoint. For example, the non-commutativity of Lorentz boosts is visually clear: Lorentz boosts do not commute just like rotations do not commute. The formula for the Doppler shift simply becomes $e^w$. Many other calculations and ideas in special relativity become simple geometric exercises in hyperbolic geometry. For historical references, Scott Walter's papers are great: [Hermann Minkowski and the scandal of spacetime.](https://halshs.archives-ouvertes.fr/halshs-00319209/),  ["The Non-Euclidean Style of Minkowskian Relativity"](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.535.6918&rep=rep1&type=pdf), and ["Minkowski’s modern world."](https://halshs.archives-ouvertes.fr/halshs-01234434/). There are some gems in Barrett's [The Hyperbolic Theory of Special Relativity](https://arxiv.org/abs/1102.0462). Rhodes and Semon go into those tedious calculations in [Relativistic velocity space, Wigner rotation and Thomas precession](https://arxiv.org/abs/gr-qc/0501070).

Ungar did probably the most influential and detailed work in this space. Particularly, his books on [gyrovector space](https://en.wikipedia.org/wiki/Gyrovector_space) puts relativistic calculations in hyperbolic geometry into a solid group-theoretical framework. Two of his relevant books are [Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity](https://www.worldscientific.com/worldscibooks/10.1142/6625) from 2008 and [Beyond the Einstein Addition Law and its Gyroscopic Thomas Precession](https://link.springer.com/book/10.1007/0-306-47134-5) from 2012. This work has even found applications in machine learning.

### Beyond special
We associate velocities and propagation speeds with Lorentz transformations. It is natural to think that the Lorentz transformation arises because the universe has a speed limit. But its relation to hyperbolic geometry opens up applications where Lorentz transformations play an essential role.

Hyperbolic geometry underlies [hierarchical relationships and complex networks](https://arxiv.org/abs/1006.5169). [Nickel and Kiela](https://arxiv.org/abs/1705.08039) apply machine learning to complex data structures and demonstrate that hyperbolic geometry is better adapted than Euclidean geometry. In a [follow-up paper](https://arxiv.org/abs/1806.03417) they compare different hyperbolic models for discovering hierarchical relationships and find that the Lorentz model is more efficient than the Poincaré model. Around the same time, [Ganea, Bécigneul, and Hofmann](https://arxiv.org/abs/1805.09112) derive hyperbolic versions of deep learning tools by using Ungar's gyrovector formalism. 

These papers opened up a [new research direction](https://arxiv.org/abs/2101.04562) in machine learning called hyperbolic deep learning. It is fascinating that they use the tools developed specifically for special relativity, such as Lorentz transformations and gyrovector spaces, to improve machine learning algorithms.

Another area closer to my heart is the role that hyperbolic geometry plays in general relativity. When spacetime is curved, the canonical identification of Minkowski space with its tangent space breaks down. We cannot perform global Lorentz transformations or use hyperbolic angles in curved spacetime as we did in flat spacetime. But we can still employ hyperbolic geometry to ease calculations.

Minkowski's hyperbola (\ref{2}) has a clear physical interpretation: the set of points at unit proper time from the origin. Hyperboloids are as natural to Minkowski space as spheres are to Euclidean space.

We can now separate spacetime into hyperbolic space and time by taking one of those surfaces and shifting it along the time direction by a new time coordinate $\tau$
$$ (\tau - t)^2 - x^2 = 1 $$ 
The new time coordinate $\tau$ reads
$$ \tau = t - \sqrt{1+x^2}. $$
The Minkowski metric becomes
$$ ds^2 = -d\tau^2 + \frac{2x}{\sqrt{1+x^2}} d\tau dx + \frac{1}{1+x^2} dx^2.$$
Level sets of $\tau$ are hyperbolic. We can bring it into the more recognizable Poincaré form by $x=2 \rho/(1-\rho^2)$.
$$ ds^2 = -d\tau^2 + \frac{8\rho}{(1-\rho^2)^2} d\tau d\rho + \frac{4}{(1-\rho^2)^4} d\rho^2.$$
This is the construction underlying hyperboloidal foliations and can be generalized to [curved spacetimes](../../publication/zenginoglu-2008-hyperboloidal/). These hyperboloidal slices are hyperbolic manifolds. 

Hyperboloidal coordinates are as natural to Lorentzian geometry as spherical coordinates are to Riemannian geometry. I devoted most of my [work](../../publication/) exploring advantages of these surfaces. 



### Hyperclusion

Physics doesn't care about how we calculate. A glance at the Wikipedia page for [Lorentz transformations](https://en.wikipedia.org/wiki/History_of_Lorentz_transformations) shows many equivalent formalisms. We could keep the usual form of relativistic formulas using velocities and Lorentz factors, or employ [Bondi's $k$-calculus](https://en.wikipedia.org/wiki/Bondi_k-calculus), or [Ungar's gyrovector space](https://en.wikipedia.org/wiki/Gyrovector_space). Why choose one over the other?

To me, it boils down to what we mean by understanding. It is helpful when formalisms lend themselves to connections to other fields because we understand by analogy. 

There is another, much more relevant aspect. As scientists, we want our descriptions to be powerful, meaning that the same thinking should apply to a broad class of phenomena. In other words, we want to avoid overfitting our theories to the phenomena at hand. 

Hyperbolic calculations translates into machine learning, spacetime curvature, and maybe other areas to be discovered. It is fair to say that the non-Euclidean approach with hyperbolic angles is more powerful than the usual approach with velocities.


[^1]: The lecture was given on September 21, 1908 in Köln during a meeting of researchers of nature (the lovely German compound word for such a meeting is Naturforscherversammlung). The [German version](https://www.math.nyu.edu/~tschinke/papers/yuri/14minkowski/raum-und-zeit.pdf) reads: *"Von Stund' an sollen Raum für sich und Zeit für sich völlig zu Schatten herabsinken und nur noch eine Art Union der beiden soll Selbständigkeit bewahren."*
[^2]: Walter, Scott. "[Hermann Minkowski and the scandal of spacetime.](https://halshs.archives-ouvertes.fr/halshs-00319209/)" ESI News 3.1 (2008): 6-8.
<!-- [^3]: Scott Walter wrote a wonderful historical account of these developments in ["The Non-Euclidean Style of Minkowskian Relativity"](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.535.6918&rep=rep1&type=pdf).
[^4]: Walter, Scott. ["Minkowski’s modern world."](https://halshs.archives-ouvertes.fr/halshs-01234434/) Minkowski Spacetime: A Hundred Years Later. Springer, Dordrecht, 2010. 43-61. -->
