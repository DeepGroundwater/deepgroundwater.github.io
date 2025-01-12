---
date: 2025-01-12
created: 2025-01-11
authors:
- RY4GIT
---

# Soils Animated: Part 1

Animation is a powerful tool for demonstrating scientific concepts. It is engaging, simplifies abstract ideas, and makes them accessible to a wide audience.

In hydrology, one of the most simple yet elegant conceptualization of soil-water dynamics is the **soil moisture loss function**, a model developed by Laio et al. (2001) and Rodriguez-Iturbe et al. (1999). This model abstract complex soil processes at the field scale into a few key variables, providing ecohydrologists with a powerful 'toy model' for conducting a variety of interesting experiments. For example, Entekhabi and Rodriguez-Iturbe (1994) explored the impacts of spatio-temporal aggregation on characterizing heterogeneity of soil moisture dynamics. D'Odorico and Porporato (2004) used it to explain soil moisture seasonality.  

In this blog post, I'll animate this soil dynamics model, with Part 1 focusing on the basic concepts. 
Animations in this blog post will illustrate how hydrologists conceptualize the soil processes happening just above and beneath our feet, 
while also exploring how these processes unfolds across different conceptual spaces. 

<!-- more -->


## Soil Moisture Loss Function to Describe the Dynamics
The soil moisture loss function (Laio et al., 2001);Rodriguez-Iturbe et al., 1999) relates the rate of loss from soil volume ($-\frac{d\theta}{dt}$) at a given soil moisture level ($\theta$). It is a type of Storage-Flux relation model in Hydrology, linking how Fluxes (in this case, drainage and evapotranspiration) are regulated by Storage (soil moisture) availability. The model describes two key stages: **Drainage** and **Evapotranspiration** (note: For simplicity, hygroscopic water are neglected in this blog post).

### Drainage Stage 
Imagine the soil after a rainstorm. Immediately after rainfall ceases, soil is saturated or extremely wet—if you step on it, it is muddy and squishy. In this state, both soil macropores and micropores are filled with water, and water in the macropores drains quickly due to gravity. Some water may also run off the surface. The first stage of the loss function represents this state, and this rapid processes are expressed as an exponential function. 

<p align="center">
  <img src="https://github.com/DeepGroundwater/DeepGroundwater.github.io/blob/master/docs/blog/posts/pics/soil_drainage.png?raw=true" alt="An animation illustrating the soil moisture loss function and the corresponding drydown curve during the Drainage stage" width="500"/>
  <br>
  <em>Figure 1: Simulated soil moisture dynamics during the Drainage stage in two different conceptual spaces. </em>
</p>


### Evapotranspiration Stage
After a few days, the soil transitions to a semi-dry state—it still feels moist to the touch, but no water seeps out. At this point, water in the soil macropores are mostly drained, and water is held against gravity in the soil micropores due to soil suction forces.

In this stage, the dominant flux is evapotranspiration (ET). Initially, when the soil is wet, ET occurs at its maximum rate because plant stomata are fully, open, and the transpiration process reaches its maximum rate (note: though evaporation can continue independently; Krell et al., 2021). As the soil dries, a critical soil moisture threshold $\theta^*$ is reached, where plants begin to experience water stress. Below that point, ET decreases proportionally with soil moisture level (although this can be nonlinear; Araki et al., 2024). These ET dynamics are represented by the piecewise-linear function in the loss function space. This is much slower process compared to the Drainage, as you can see below: 

<p align="center">
  <img src="https://github.com/DeepGroundwater/DeepGroundwater.github.io/blob/master/docs/blog/posts/pics/soil_ET.png?raw=true" alt="An animation illustrating the soil moisture loss function and the corresponding drydown curve during the Evapotranspiration stage" width="500"/>
  <br>
  <em>Figure 2: Simulated soil moisture dynamics during the Evapotranspiration stage in two different conceptual spaces. </em>
</p>

## Usefulness of the Soil Moisture Loss Function
This loss function model treats soil volume as a system responding to pulse inputs of rainfall (which I plan to elaborate on and animate in Part 2). The model describes how soil responds in a prescribed manner based on the combination of its physical properties, external forcing, and current  state. The drydown curve is the realization of the system partially activated by a rainfall pulse. 

Because the loss function is an ordinary differential equation (ODE), we can transition between two perspectives. 


1. **System Space (Left panels in the above animations)**: represents general patterns of the soil system, i.e., the loss function. 

2. **Observable Space (Right panels in the above animations)**: describes soil moisture drying behavior, which are measurable with sensors. This drydown model is the analytical solution of the loss function ODE.

One of the biggest advantages of moving between these spaces is dealing with uncertainties in model estimation. 

In system space (loss function), both the x- and y-variables are subject to observation errors in $\theta$, making it prone to uncertainties. The animation below shows how Gaussian noise in the sample observation points  impacts loss estimates. This situation calls for bivariate analysis but they are more difficult to implement. One of the ways to deal with the bivariate uncertainties is to use the Bayesian approaches as implemented by Bassiouni et al., (2020).

<p align="center">
  <img src="https://github.com/DeepGroundwater/DeepGroundwater.github.io/blob/master/docs/blog/posts/pics/soil_est_v1.png?raw=true" alt="An animation illustrating how estimating the loss function from the drydown can be impacted by noise" width="500"/>
  <br>
  <em>Figure 3: Estimating the soil moisture loss function from a sample point with Gaussian noise, from the loss function space. </em>
</p>

In the observable space (which is the analytical solution of the loss function), the x-variable becomes sampling timing—a deterministic quantity. This reduces uncertainty to just the y-variable ($\theta$), allowing the application of the simpler nonlinear least-squares fitting.

<p align="center">
  <img src="https://github.com/DeepGroundwater/DeepGroundwater.github.io/blob/master/docs/blog/posts/pics/soil_est_v2.png?raw=true" alt="An animation illustrating how estimating the loss function from the drydown can be impacted by noise" width="500"/>
  <br>
  <em>Figure 4: Estimating the soil moisture loss function from a sample point with Gaussian noise, from the drydown space. </em>
</p>

## The Power of the Animation
Science requires abstraction of processes, and we use models for that purpose. With the use of animation, we can easily visualize the model behavior and visualize more abstracted spaces. Animation helps us to wrap around our head to move between observation space and theoretical spaces, just like the drydown space and the loss function space. 

Platforms like DeepGroundwater enable us to share these visualizations (a shameless plug)! While animations are difficult to include in traditional scientific formats like PDFs, this platform freely accommodates images, animations, videos, and even JavaScript animations to share ideas. We welcome scientific & artistic contributions here.

Part 2 of this blog post will explore the challenges of using this soil moisture loss function model—which is ultimately a bucket model that is an oversimplification of the reality as pointed out in [our first blogpost](https://deepgroundwater.com/blog/hydrology-is-flat-and-its-buckets-all-the-way-down/). I plan to describe how loss function plays out in longer timeseries with multiple pulse rainfall pulses, and discuss how we may or may not be able to derive information from it (with animations, of course!). Stay tuned.

## Code Availability 
These animations come to life thanks to Python's matplotlib, which you can access the code here: <https://github.com/RY4GIT/drydown-viz>.

## Reference & Acknolwegements
This blog post builds on ideas from discussions with my advisors and collaborators, especially Hilary, Kelly, Bryn, and the Editorial Board members—thank you all!

Laio, F., Porporato, A., Fernandez-Illescas, C. P., & Rodriguez-Iturbe, I. (2001). Plants in water-controlled ecosystems: Active role in hydrologic processes and responce to water stress IV. Discussion of real cases. Advances in Water Resources, 24(7), 745–762. <https://doi.org/10.1016/S0309-1708(01)00007-0>

Rodriguez-Iturbe, I., Porporato, A., Ridolfi, L., Isham, V., & Coxi, D. R. (1999). Probabilistic modelling of water balance at a point: the role of climate, soil and vegetation. Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences. <https://doi.org/10.1098/rspa.1999.0477>

D'Odorico, P., & Porporato, A. (2004). Preferential states in soil moisture and climate dynamics. Proceedings of the National Academy of Sciences of the United States of America, 101(24), 8848–8851. <https://doi.org/10.1073/pnas.0401428101>

Entekhabi, D., & Rodriguez-Iturbe, I. (1994). Analytical framework for the characterization of the space-time variability of soil moisture. Advances in Water Resources, 17(1), 35–45. <https://doi.org/10.1016/0309-1708(94)90022-1>

Krell, N. T., Morgan, B. E., Gower, D., & Caylor, K. K. (2021). Consequences of dryland maize planting decisions under increased seasonal rainfall variability. Water Resources Research, 57(9). <https://doi.org/10.1029/2020wr029362>

Araki, R., Morgan, B., McMillan, H. K., & Caylor, K. (2024). Nonlinear soil moisture loss function reveals vegetation responses to water availability. Authorea Preprints. <https://doi.org/10.22541/essoar.172251989.99347091>

Bassiouni, M., Higgins, C. W., Still, C. J., & Good, S. P. (2018). Probabilistic inference of ecohydrological parameters using observations from point to satellite scales. Hydrology and Earth System Sciences, 22(6), 3229–3243. <https://doi.org/10.5194/hess-22-3229-2018>

