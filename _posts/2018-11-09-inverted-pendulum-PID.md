---
layout: post
title: Inverted Pendulum Control
excerpt: A partner and I created and tuned a PI controller to effectively maneuver a segway-like inverted pendulum robot. We tuned the controller analytically by viewing the transfer function of the system in the s-domain.
short_desc: Implemented a PI controller to keep segway-like robot standing
categories: [Mechanical, Software]
featured: true
date_string: November, 2018
image: ../../img/inverted-pendulum-PID/rocky.png
alt: pic05.jpg
report: ../../assets/QEA_Rocky_Report.pdf
---

|---|---|
This project was completed for my Quantitative Engineering Analysis course. In this module, pairs of students were required to derive and implement a controller to keep an inverted pendulum segway robot, named Rocky, upright. See image to the right. Additional challenges included tuning the controller to make the robot drive as fast as possible while remaining upright, as well as spin as fast as possible while remaining upright. The full report can be found above. <br/> <br/>To tackle this challenge, we first derived a block diagram for the physical system to illustrate and understand how it would interact with our various controllers. In the end, we implemented controllers for robot angle, position, and velocity, as well as motor speed. The final block diagram is shown below. | ![rocky](../../img/inverted-pendulum-PID/rocky.png)

![block diagram](../../img/inverted-pendulum-PID/block_diagram.png)

Using our block diagram, we calculated the transfer function for the entire system. We used Mathematica to find the poles of the transfer function, allowing us to quickly determine the long-term stability behavior of any set of controller constants by evaluating the signs and magnitudes of the real and imaginary components of the poles. [Linked is a demo video of our robot "sprinting"](https://www.youtube.com/watch?v=KrbPwAjVmfA). Camera work done by yours truly :) 