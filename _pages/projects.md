---
layout: page
title: Research Topics
permalink: /projects/
description: This is the research directions I have been/am working on.
#A growing collection of your cool projects.
nav: true
nav_order: 4
display_categories: [Foundation Models, Image Harmonization, Anomaly Detection, NLP]
horizontal: false
---

<h2>Foundation Models</h2>
Foundation models are large-scale, pre-trained networks that have proven effective across various applications. My focus in this direction is twofold: (1) adapting foundation models pre-trained on natural images to the medical domain, and (2) developing medical-specific foundation models. In the first direction, we have evaluated the performance of SAM [[PDF]](https://www.sciencedirect.com/science/article/am/pii/S1361841523001780) and SAM2 [[PDF]](https://arxiv.org/pdf/2408.00756) in medical applications. For the second direction, we have fine-tuned foundation models for segmenting bones [[PDF]](https://arxiv.org/pdf/2401.12974) and muscles [ongoing], provide a guideline to fine-tune foundation models [[PDF]](https://arxiv.org/pdf/2404.09957), and are developing a new model that has shown promise for MRI-based segmentation (<b>4% improvement in DSC</b> on average compared to SAM-based finetuning) [ongoing].
<br>
<br>

<h2>Image Harmonization</h2>
Medical images of the same anatomical region can vary significantly in appearance due to differences in acquisition procedures, such as scanner type and protocol. One approach to addressing this variability is image harmonization, \textit{i.e.}, making the appearance of images from different domains similar. To achieve this goal, we have first developed a few intermediate steps, such as generating anatomically-controllable images [[PDF]](https://arxiv.org/pdf/2402.05210) and adapting the networks to different domains during test-time (<b>2.9% improvement in DSC</b> when compared to runner-up) [[PDF]](https://openaccess.thecvf.com/content/CVPR2024W/DEF-AI-MIA/papers/Dong_Medical_Image_Segmentation_with_InTEnt_Integrated_Entropy_Weighting_for_Single_CVPRW_2024_paper.pdf).
<br>
<br>

<h2>Anomaly Detection</h2>
Label acquisition for medical images can be costly. Anomaly detection addresses this challenge by training networks solely on normal images and classifying unseen patterns as abnormalities. In this direction, I have developed two methods to enhance detection performance: (1) sliding-window partitioning (<b>outperforming runner-up method by 8.03% IOU</b>) [[PDF]](https://drive.google.com/file/d/1hrq1bW1-H6Oylbm0heR88BcOoAp5Yo4d/view), and (2) pluralistic image completion [[PDF]](https://www.sciencedirect.com/science/article/pii/S1361841523000968).
<br>
<br>

<h2>Multi-Modal Learning</h2>
In this direction, I am particularly interested in the intersection between vision and language. I have developed a text-guided retrieval algorithm [[PDF]](https://openaccess.thecvf.com/content/CVPR2021W/MULA/papers/Dong_Using_Text_To_Teach_Image_Retrieval_CVPRW_2021_paper.pdf) that and a multi-modal agent that <b>surpasses GPT-4o</b> [[PDF]](https://arxiv.org/pdf/2407.02483).
