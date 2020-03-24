---
layout: post
title: Flat Earth Physics
excerpt: Have you ever wondered what it'd be like to throw a ball on flat earth? In this computer simulation, a partner and I modeled how a projectile would fly on a flat earth. Optimal parameters were calculated such that the projectile would come back to the launch site.
short_desc: Have you ever wondered what it'd be like to throw a ball on flat earth?
categories: [Software, Simulation]
date_string: December, 2017
image: flat-earth-physics/flat_earth.png
alt: pic02.jpg
github: https://github.com/jzerez/ModSim-Project3
---
## Inspiration

This project was done in the context of a kinematics project for a modeling and simulation class. Modeling something on flat earth was not only a very funny and entertaining idea, but it offered the opportunity to explore some really counter-intuitive physics.

## Background

What exactly about flat earth is interesting to model? Well, flat earthers believe that the earth is accelerating upwards at 9.8 meters per second squared, which is how they explain why things accelerate towards the ground at that rate. We called this effective gravity in the model. However, they also believe in gravity. These two beliefs introduce a very interesting environment, as the gravity vector acting upon any projectile can change quite drastically over time in both magnitude and direction.

This project was made using Python. In order to model flat earth, we took the surface area of earth, the average density of the earth, and the weight of the earth and calculated the radius and thickness of a flat earth. We also treated the earth as a point mass in the center of the disk. In hindsight, this is a really unrealistic way to model a flat earth. In the future, assuming all throws are precisely radial, it would be much more effective to model the earth as a series of masses in a line, with the magnitude of each mass following a cosine distribution: the center of the line would be the most massive, and each end would approach zero mass.

## Results

This project produced some really interesting results. The complex nature of the environment that we modeled led to some quite counter-intuitive results.

![](../../img/flat-earth-physics/distance_vs_time1.png) ![](../../img/flat-earth-physics/trajectory1.png)

These two graphs show the trajectory of a standard baseball when thrown at 60 degrees relative to horizontal with an initial velocity of 120 meters per second (a bit unrealistic, yes), 240,000 meters away from the north pole, which is the center of flat earth. Under these conditions, the ball will come back to the launch site, as the vector sum of drag, gravity, and effective gravity are roughly 60 degrees throughout the flight of the ball. As such, the ball returns to the original position with about the same velocity and angle.

![](../../img/flat-earth-physics/trajectory2.png)

This graph shows the trajectory of a ball thrown 80 degrees to horizontal very close to the pole. Because of the force of gravity, it actually ends up _behind_ the throwing position.

![](../../img/flat-earth-physics/graph2.png)

In this graph, we swept parameters for throwing distance from the pole as well as throwing angle relative to horizontal. A negative value on the y axis corresponds to the ball landing behind the original throwing position.

![](../../img/flat-earth-physics/help_heat_1.png)

This heat map is a sweep of both initial velocity and throwing angle with a constant distance from the pole. Cool colors represent large absolute distances between the throwing position, and landing position while warm colors represent small absolute distances. It really shows the counter-intuitive nature of physics on a flat earth, as one would normally expect a pretty uniform transition from hot to cold as the velocities increase, however this is not the case
