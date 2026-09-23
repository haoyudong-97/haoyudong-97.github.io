---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a final-year Ph.D. candidate in Electrical & Computer Engineering at Duke University, advised by [Prof. Maciej A. Mazurowski](https://sites.duke.edu/mazurowski/). I develop foundation models and agentic AI systems that reason across images and language, use specialized tools, and adapt to complex real-world tasks.

My work spans LLM-agent optimization at Meta, in-context 3D medical image segmentation at Siemens Healthineers, and large-scale multimodal learning at Duke. I previously earned my M.S. in Computer Science at Duke, where I worked with [Prof. Guillermo Sapiro](https://scholar.google.com/citations?user=ISRNX3gAAAAJ&hl=en), and B.S. degrees in Mathematics–Computer Science and Cognitive Science at UC San Diego, where I worked with [Prof. Zhuowen Tu](https://pages.ucsd.edu/~ztu/).

**I am seeking research scientist, applied scientist, and research engineering positions starting in Summer 2027.**

<a href="/assets/haoyudong_resume.pdf" class="btn btn--primary">Download résumé</a>

<h2 id="selected-work">Selected Work</h2>

### Meta-Harness — LLM agent optimization

Improved Meta-Harness's algorithm-evolution pipeline by evolving agent trajectories and dynamically adapting training data. Increased performance from **49% to 62%** on math-solving tasks and from **68% to 71.3%** on Terminal-Bench 2.

### In-context 3D segmentation of unseen anatomies

Developed a 3D nnU-Net framework with multi-stage cross-attention that segments new anatomical structures from annotated support examples without retraining. Curated **14,934 CT volumes** spanning **92 structures** and achieved **52.1% Dice** on held-out unseen anatomies, compared with **36.7%** for the strongest prior in-context learning baseline. A systematic support-selection study revealed a **21-point Dice** performance range. Co-inventor on the resulting **patent-pending** technology assigned to Siemens Medical Solutions USA, Inc.

### [MRI-CORE](https://arxiv.org/abs/2506.12186) — MRI foundation model

Pretrained a foundation model on **7M MRI slices**, improving few-shot downstream segmentation by **5 Dice points** over SAM, and extended this direction toward multimodal 3D MRI and radiology-report alignment.

### [MMedAgent](https://aclanthology.org/2024.findings-emnlp.510/) — Multimodal medical agent

Developed a multimodal agent that coordinates specialized medical tools across imaging and language tasks; published in **Findings of EMNLP 2024**.

Experience
======

**Software Engineering Intern**, [Meta](https://www.meta.com) · May 2026 – Present<br>
Worked on algorithm evolution for LLM agents, making trajectories evolvable and adapting training data to strengthen optimization signals.

**AI Research Intern**, [Siemens Healthineers](https://www.siemens-healthineers.com/) · June 2025 – August 2025<br>
Developed a 3D in-context segmentation framework for unseen anatomies, built and evaluated on 14,934 CT volumes across 92 structures; the work resulted in **patent-pending technology** assigned to Siemens Medical Solutions USA, Inc.

Recent News
======

* **[Sep. 2026]** Our work on [learning CT representations across anatomy and disease](https://arxiv.org/abs/2605.21906) was accepted to *npj Digital Medicine*.
* **[Sep. 2026]** Our work on [muscle segmentation across anatomical regions in MRI](https://arxiv.org/abs/2506.22467) was accepted to *Computers in Biology and Medicine*.
* **[Jan. 2026]** Our work on [Fréchet Radiomic Distance](https://doi.org/10.1016/j.media.2026.103943) was published in *Medical Image Analysis*.
* **[Jan. 2026]** Our work applying [SAM 2 to 2D and 3D medical images](https://arxiv.org/abs/2408.00756) was published in *IEEE Transactions on Biomedical Engineering*.
* **[Dec. 2025]** Our work on [breast MRI registration](https://arxiv.org/abs/2505.13414) was published in *IEEE Journal of Biomedical and Health Informatics*.
* **[Oct. 2025]** Our work on [AI-based breast density quantification](https://www.nature.com/articles/s41523-025-00789-w) was published in *npj Breast Cancer*.
* **[Oct. 2025]** Our work on [volumetric annotation with SAM 2](https://arxiv.org/abs/2505.01854) was published in *IEEE Transactions on Medical Imaging*.
* **[July 2025]** We released [MRI-CORE](https://arxiv.org/abs/2506.12186), a foundation model for magnetic resonance imaging.

<details>
<summary><strong>Earlier news</strong></summary>
<ul>
  <li><strong>[May 2025]</strong> Our study of <a href="https://www.melba-journal.org/papers/2025:006.html">SAM fine-tuning strategies</a> was published in <em>MELBA</em>.</li>
  <li><strong>[April 2025]</strong> <a href="https://www.sciencedirect.com/science/article/pii/S1361841525000170">SegmentAnyBone</a> was published in <em>Medical Image Analysis</em>.</li>
  <li><strong>[Dec. 2024]</strong> The <a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/1b8726b572e0dfa72793f9f6590664fd-Paper-Datasets_and_Benchmarks_Track.pdf">Touchstone benchmark</a> was published at NeurIPS Datasets and Benchmarks.</li>
  <li><strong>[Oct. 2024]</strong> <a href="https://aclanthology.org/2024.findings-emnlp.510/">MMedAgent</a> was published in Findings of EMNLP.</li>
  <li><strong>[June 2024]</strong> Our work on <a href="https://arxiv.org/abs/2402.05210">anatomically controllable medical image generation</a> was published at MICCAI.</li>
  <li><strong>[March 2024]</strong> <a href="https://openaccess.thecvf.com/content/CVPR2024W/DEF-AI-MIA/papers/Dong_Medical_Image_Segmentation_with_InTEnt_Integrated_Entropy_Weighting_for_Single_CVPRW_2024_paper.pdf">InTEnt</a> was presented as an oral at a CVPR workshop.</li>
  <li><strong>[March 2024]</strong> Our <a href="https://www.nature.com/articles/s41598-024-54048-2">breast MRI segmentation model and dataset</a> were published in <em>Scientific Reports</em>.</li>
  <li><strong>[March 2024]</strong> Our work on <a href="https://www.sciencedirect.com/science/article/pii/S0925231224001450">confidence-guided radiology report generation</a> was published in <em>Neurocomputing</em>.</li>
  <li><strong>[Sep. 2023]</strong> <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10766076/">SWSSL</a> was published in <em>IEEE Transactions on Medical Imaging</em>.</li>
  <li><strong>[Aug. 2023]</strong> Our <a href="https://www.sciencedirect.com/science/article/pii/S1361841523001780">SAM evaluation for medical imaging</a> was published in <em>Medical Image Analysis</em>.</li>
  <li><strong>[April 2023]</strong> Our work on <a href="https://www.sciencedirect.com/science/article/pii/S1361841523000968">pluralistic image completion</a> was published in <em>Medical Image Analysis</em>.</li>
</ul>
</details>
