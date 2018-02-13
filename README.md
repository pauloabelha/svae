Forked from mattjj/svae by pauloabelha

The purpose of this forking is to maintain a version that I can easily run while also documenting the steps required to make it run from scratch. 

This repo contains a frozen (commit 0f026ab) version of autograd to ensure code is stable (see original README below).

I tested the steps below on a fresh version of Ubuntu 16. I will write in baby steps to be clear. Better safe than sorry.

TL;DR - I want to run this ting!
In order to get up and running a demo (assuming you cloned the repo to ~/svae):

1) Install Anaconda:
  - https://conda.io/docs/user-guide/install/download.html#anaconda-or-miniconda
  - When installing, I recommend saying Yes to the Great Serpent everytime she asks you something
  - Everytime you say no to some default path you are at your own peril
2) Open a new terminal
3) Create a python2 environment
  - `conda create -n py27 python=2.7 anaconda`
4) Install dependencies:
  - `conda install --name py27 future`
5) Activate the environment:
  - `source activate py27`
6) Run an experiment:
  - `cd ~/svae/experiments`
  - `python gmm_svae_synth.py`



README before forking:

Code for [Composing graphical models with neural networks for structured representations and fast inference](http://arxiv.org/abs/1603.06277), a.k.a. structured variational autoencoders.

**NOTE:** This code isn't yet compatible with a recent rewrite of autograd. To
use an older, compatible version of autograd, clone
[autograd](https://github.com/hips/autograd) and check out commit 0f026ab.


###Abstract

We propose a general modeling and inference framework that composes probabilistic graphical models with deep learning methods and combines their respective strengths.
Our model family augments graphical structure in latent variables with neural network observation models.
For inference we extend variational autoencoders to use graphical model approximating distributions, paired with recognition networks that output conjugate potentials.
All components of these models are learned simultaneously with a single
objective, giving a scalable algorithm that leverages stochastic
variational inference, natural gradients, graphical model message passing, and
the reparameterization trick.
We illustrate this framework with several example models and an application to
mouse behavioral phenotyping.


By

* [Matthew James Johnson](http://www.mit.edu/~mattjj/)
* [David Duvenaud](http://people.seas.harvard.edu/~dduvenaud/)
* [Alexander B. Wiltschko](https://github.com/alexbw)
* [Sandeep R. Datta](http://datta.hms.harvard.edu/)
* [Ryan P. Adams](https://www.seas.harvard.edu/directory/rpa)
