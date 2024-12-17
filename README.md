# Project BIO485 - MR Aceleration - Solving a inverse problem

Magnetic Resonance Imaging (MRI) is a crucial diagnostic tool that allows us to capture detailed images of the inside of our body. However, acquiring these images often takes a long time. One way to speed up this process is by skipping certain lines in the k-space data beyond the Nyquist limit. While this reduces scanning time, it also introduces undesirable artifacts in the images.  

This project explores a method to skip lines in the k-space domain by treating the problem as an inverse problem. The goal is to reconstruct the best high-resolution image (\(x\)) from the undersampled k-space data (\(s\)). This problem can be expressed mathematically as:  

$$
f(x) = \min \|s - Ex\|_2^2 + \lambda \|x\|_2^2
$$  

Where:  
- \(s\) is the undersampled data,  
- \(x\) is the high-resolution image,  
- \(E\) combines the undersampling mask, coil sensitivity, and Fourier transform,  
- \(\lambda\) is a regularization term.  

The project explores simple 1D and 2D examples to address this problem. It focuses on reconstructing \(x\) (the high-resolution image) using methods such as the pseudoinverse matrix and gradient descent.  

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Contributing](#contributing)

## Features
- List the main features of your project. This project has 3 main codes

-1D_Toy_Remasterd -> 1D Numerical Solution
-Gradient Descent Numpy -> 2D Gradient descent exampl
-Gradient Descent Torch -> 2D Gradient descent example
-Sigpy SENSE -> SENSE library
-Data -> Contain Sensitivity Maps and Knee images
-Utils -> Contain usefull functions.

## Installation
Provide step-by-step instructions to set up the project:

-pip install sigpy
-conda install maplotlib-pyplot
-conda install numpy
-pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

Clone the repository
git clone [https://github.com/username/repo.git](https://github.com/Jhersin/Project-BIO485.git)

## Contributing
- Robert Reyther
- Owen Shin
- Jhersin Garcia
