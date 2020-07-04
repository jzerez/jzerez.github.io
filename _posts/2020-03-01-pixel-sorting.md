---
layout: post
title: Pixel Sorting
excerpt: "This computational art project allows you to create glitchy looking images through pixel sorting. In pixel sorting, you first iterate through the image, and identify intervals of pixels that fall within a certain threshold for some value (ex: pixel intensity). Afterwards, you sort the pixels within each interval."
short_desc: "A computational art project to make images look  [G L I T C H Y]"
categories: [Software, Art]
featured: false
date_string: March, 2020
image: cherry_blossom_glitch.jpg
alt: pic05.jpg
github: https://github.com/jzerez/pixel_sorting
instagram: https://www.instagram.com/zomogr.art/
---
I created this project mainly for fun. I saw some examples of pixel sorting online and thought that it would be pretty fun and easy to replicate it! The project was created in python, using primarily `numpy` and `pillow` to open and process through images.

It works by opening images and converting them into numpy arrays. The user specifies a pixel attribute to evaluate (ex: pixel intensity, hue, or saturation), as well as upper and lower thresholds for that attribute. The program then iterates through each row of the the array and denotes intervals of pixels that are within those thresholds. Then, for each interval, the pixels are sorted, usually by the same attribute used for determining intervals. The result is really cool images that look like they're melting away. Below is a gallery of my favorite image created by the script!

| ![cherry blossoms](../../img/pixel-sorting/cherry_blossom_comparison.jpg) | ![temple](../../img/pixel-sorting/fake_temple_comparison.jpg)   | ![taipei 101](../../img/pixel-sorting/taipei101_glitch.jpg)   |
| ![jiufen](../../img/pixel-sorting/jiufen_glitch.jpg) | ![alley](../../img/pixel-sorting/alley_glitch.jpg)   | ![neon city](../../img/pixel-sorting/taipei_neon_city_glitch.jpg)|
| ![nebula](../../img/pixel-sorting/nebula_glitch.jpg) | ![orchid](../../img/pixel-sorting/orchid_glitch_hue.jpg)| ![nebula1](../../img/pixel-sorting/nebula1_glitch_redux.jpg) |
