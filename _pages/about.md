---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: false
classes: wide
redirect_from: 
  - /about/
  - /about.html
---

<section class="home-hero">
  <div class="home-hero-main">
    <div class="hero-avatar">
      <img src="/images/zm7.jpg" alt="Mengqi Zhang">
    </div>
    <div class="hero-identity">
      <h1>Mengqi Zhang <span>张孟奇</span></h1>
      <p class="home-lead">Assistant Professor · M.Sc. Supervisor · General Artificial Intelligence Laboratory</p>
      <div class="home-actions">
        <a href="mailto:mengqi.zhang@sdu.edu.cn">Email</a>
        <a href="https://scholar.google.com.hk/citations?user=8-tCnnUAAAAJ&hl=zh-CN">Google Scholar</a>
        <a href="https://github.com/ZM7">GitHub</a>
      </div>
    </div>
    <div class="hero-snapshot" aria-label="Profile summary">
      <p><span>School</span> Computer Science and Technology, SDU</p>
      <p><span>Lab</span> General Artificial Intelligence Laboratory</p>
      <p><span>Ph.D.</span> CASIA, 2023</p>
      {% assign scholar = site.data.scholar %}
      <div class="scholar-stats" aria-label="Google Scholar metrics">
        <a href="{{ scholar.source | default: 'https://scholar.google.com/citations?user=8-tCnnUAAAAJ&hl=en' }}">Google Scholar Metrics</a>
        <span><strong>{{ scholar.citations | default: "—" }}</strong><em>Citations</em></span>
        <span><strong>{{ scholar.h_index | default: "—" }}</strong><em>h-index</em></span>
        <span><strong>{{ scholar.i10_index | default: "—" }}</strong><em>i10-index</em></span>
      </div>
    </div>
  </div>
</section>

<section class="home-section home-intro">
  <p>
    I am <strong>Mengqi Zhang (张孟奇)</strong>, an Assistant Professor and M.Sc. Supervisor in the
    <a href="https://www.cs.sdu.edu.cn/">School of Computer Science and Technology, Shandong University</a>,
    and a member of the <a href="https://gail.sdu.edu.cn/">General Artificial Intelligence Laboratory</a>. I received my Ph.D. degree in 2023 from the State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences (CASIA), under the supervision of Prof. <a href="https://scholar.google.com.hk/citations?user=8kzzUboAAAAJ&hl=zh-CN">Liang Wang</a>
    <span class="intro-note">(NSFC Distinguished Young Scholar, IEEE Fellow)</span>, and was co-advised by
    Prof. <a href="https://scholar.google.com.hk/citations?user=qVge6YYAAAAJ&hl=zh-CN">Shu Wu</a> and
    Prof. <a href="https://scholar.google.com.hk/citations?user=D-lKLcMAAAAJ&hl=zh-CN">Qiang Liu</a>.
  </p>

</section>

<section class="home-section research-focus">
  <h2>Research Interests</h2>
  <p>
    My current research centers on <strong>trustworthy and controllable large language models (LLMs)</strong>,
    with particular interests in <strong>LLM agents, knowledge editing, agentic RAG, interpretability, and model safety and alignment</strong>. Previously, I have also conducted extensive research in
    temporal knowledge graph reasoning and recommender systems.
  </p>
</section>

<section class="home-callout">
  <div class="callout-head">
    <strong>招生信息 <span>Recruitment</span></strong>
    <em>Open to students</em>
  </div>
  <p>I am always looking for self-motivated students to work on LLMs. Feel free to reach out if you are interested in pursuing a Master's degree, a Ph.D., an undergraduate research assistant position, or exploring potential collaborations.</p>
  <p>欢迎对大模型研究感兴趣的同学（保研、考研或本科生科研助理）通过邮件与我联系，也欢迎任何形式的学术探讨与合作！</p>
</section>

Preprint
------

<div class="preprint-list">

<article class="preprint-item">
  <h3>On the Hidden Costs of Counterfactual Knowledge Training in LLM Unlearning.</h3>
  <p class="pub-meta"><span class="pub-venue">Preprint</span><span class="pub-rank">LLM Unlearning</span></p>
  <p class="pub-authors">Xiaotian Ye, Xiaohan Wang, <strong>Mengqi Zhang</strong>, Shu Wu</p>
</article>

<article class="preprint-item">
  <h3>Uncovering Entity Identity Confusion in Multimodal Knowledge Editing.</h3>
  <p class="pub-meta"><span class="pub-venue">Preprint</span><span class="pub-rank">Multimodal Knowledge Editing</span></p>
  <p class="pub-authors">Shu Wu, Xiaotian Ye, Xinyu Mou, Dongsheng Liu, Xiaohan Wang, <strong>Mengqi Zhang</strong></p>
</article>

<article class="preprint-item">
  <h3>Uncovering Context Reliance in Unstructured Knowledge Editing.</h3>
  <p class="pub-meta"><span class="pub-venue">Preprint</span><span class="pub-rank">LLM Knowledge Editing</span></p>
  <p class="pub-authors">Zisheng Zhou, <strong>Mengqi Zhang</strong>, Shiguang Wu, Xiaotian Ye, Chi Zhang, Zhumin Chen, Pengjie Ren.</p>
</article>

<article class="preprint-item">
  <h3>Open Problems and a Hypothetical Path Forward in LLM Knowledge Paradigms.</h3>
  <p class="pub-meta"><span class="pub-venue">Preprint</span><span class="pub-rank">LLM Knowledge</span></p>
  <p class="pub-authors">Xiaotian Ye, <strong>Mengqi Zhang</strong>, Shu Wu</p>
</article>

</div>

<h2 id="publications">Selected Publications <span class="section-link-note">Full list: <a href="https://scholar.google.com.hk/citations?user=8-tCnnUAAAAJ&hl=zh-CN">Google Scholar</a> or <a href="/publications/">Publications</a></span></h2>

<p class="publication-note"><span>*</span> equal contribution &nbsp;&nbsp; <span>#</span> corresponding author</p>

<div class="publication-list">

<article class="publication-item">
  <h3>Disentangling Knowledge Representations for Large Language Model Editing.</h3>
  <p class="pub-meta"><span class="pub-venue">ICLR 2026</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>*, Zisheng Zhou*, Xiaotian Ye, Qiang Liu, Zhaochun Ren, Zhumin Chen, Pengjie Ren</p>
</article>

<article class="publication-item">
  <h3>Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse.</h3>
  <p class="pub-meta"><span class="pub-venue">ACL 2026</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors">Chi Zhang, <strong>Mengqi Zhang</strong>#, Xiaotian Ye, Runxi Cheng, Zisheng Zhou, Ying Zhou, Pengjie Ren, Zhumin Chen.</p>
</article>

<article class="publication-item">
  <h3>LLM Unlearning Should Be Form-Independent.</h3>
  <p class="pub-meta"><span class="pub-venue">IEEE S&amp;P 2026</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors">Xiaotian Ye, <strong>Mengqi Zhang</strong>#, Shu Wu</p>
</article>

<article class="publication-item featured-publication">
  <h3>Uncovering Overfitting in Large Language Model Editing.</h3>
  <p class="pub-meta"><span class="pub-venue">ICLR 2025</span><span class="pub-rank">CCF-A</span><span class="pub-award">Spotlight · Top 5.1%</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>*, Xiaotian Ye*, Qiang Liu, Shu Wu, Pengjie Ren, Zhumin Chen</p>
</article>

<article class="publication-item">
  <h3>KELE: Residual Knowledge Erasure for Enhanced Multi-hop Reasoning in Knowledge Editing.</h3>
  <p class="pub-meta"><span class="pub-venue">Findings of EMNLP 2025</span><span class="pub-rank">CCF-B</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>*, Bowen Fang*, Qiang Liu, Xiaotian Ye, Pengjie Ren, Shu Wu, Zhumin Chen, Liang Wang</p>
</article>

<article class="publication-item">
  <h3>UIPE: Enhancing LLM Unlearning by Removing Knowledge Related to Forgetting Targets.</h3>
  <p class="pub-meta"><span class="pub-venue">Findings of EMNLP 2025</span><span class="pub-rank">CCF-B</span></p>
  <p class="pub-authors">Wenyu Wang, <strong>Mengqi Zhang</strong>#, Xiaotian Ye, Zhaochun Ren, Pengjie Ren, Zhumin Chen</p>
</article>

<article class="publication-item">
  <h3>ExcluIR: Exclusionary Neural Information Retrieval.</h3>
  <p class="pub-meta"><span class="pub-venue">AAAI 2025</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors">Wenhao Zhang, <strong>Mengqi Zhang</strong>#, Shiguang Wu, Jiahuan Pei, Zhaochun Ren, Maarten de Rijke, Zhumin Chen, Pengjie Ren</p>
</article>

<article class="publication-item">
  <h3>Knowledge Graph Enhanced Large Language Model Editing.</h3>
  <p class="pub-meta"><span class="pub-venue">EMNLP 2024</span><span class="pub-rank">CCF-B</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>*, Xiaotian Ye*, Qiang Liu, Pengjie Ren, Shu Wu, and Zhumin Chen.</p>
</article>

<article class="publication-item featured-publication">
  <h3>Generative Retrieval as Multi-Vector Dense Retrieval.</h3>
  <p class="pub-meta"><span class="pub-venue">SIGIR 2024</span><span class="pub-rank">CCF-A</span><span class="pub-award">Best Paper Honorable Mention · 最佳论文提名奖</span></p>
  <p class="pub-authors">Shiguang Wu, Wenda Wei, <strong>Mengqi Zhang</strong>, Zhumin Chen, Jun Ma, Zhaochun Ren, Maarten de Rijke, Pengjie Ren.</p>
</article>

<article class="publication-item">
  <h3>Learning Long- and Short-term Representations for Temporal Knowledge Graph Reasoning.</h3>
  <p class="pub-meta"><span class="pub-venue">WWW 2023</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>, Yuwei Xia, Qiang Liu, Shu Wu, and Liang Wang.</p>
</article>

<article class="publication-item">
  <h3>Learning Latent Relations for Temporal Knowledge Graph Reasoning.</h3>
  <p class="pub-meta"><span class="pub-venue">ACL 2023</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>, Yuwei Xia, Qiang Liu, Shu Wu, and Liang Wang.</p>
</article>

<article class="publication-item featured-publication">
  <h3>Dynamic Graph Neural Networks for Sequential Recommendation.</h3>
  <p class="pub-meta"><span class="pub-venue">IEEE TKDE 2023</span><span class="pub-rank">CCF-A</span><span class="pub-award">ESI Highly Cited Paper</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>, Shu Wu, Xueli Yu, Qiang Liu, and Liang Wang.</p>
</article>

<article class="publication-item">
  <h3>Deep Contrastive Multiview Network Embedding.</h3>
  <p class="pub-meta"><span class="pub-venue">CIKM 2022</span><span class="pub-rank">CCF-B</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>, Yanqiao Zhu, Qiang Liu, Shu Wu, and Liang Wang.</p>
</article>

<article class="publication-item">
  <h3>Personalized Graph Neural Networks with Attention Mechanism for Session-Aware Recommendation.</h3>
  <p class="pub-meta"><span class="pub-venue">IEEE TKDE 2020</span><span class="pub-rank">CCF-A</span></p>
  <p class="pub-authors"><strong>Mengqi Zhang</strong>, Shu Wu, Meng Gao, Xin Jiang, Ke Xu, and Liang Wang.</p>
</article>

<article class="publication-item">
  <h3>Dynamic Graph Collaborative Filtering.</h3>
  <p class="pub-meta"><span class="pub-venue">ICDM 2020</span><span class="pub-type">Regular Paper</span><span class="pub-rank">CCF-B</span></p>
  <p class="pub-authors">Xiaohan Li*, <strong>Mengqi Zhang</strong>*, Shu Wu, Zheng Liu, Liang Wang, and Philip S Yu.</p>
</article>

</div>

<h2 id="honors-and-awards">Honors and Awards</h2>

<div class="honor-list">
  <div><span>2026</span><p>Shandong Provincial Young Science and Technology Talent Support Project <em>山东省青年科技人才托举工程</em></p></div>
  <div><span>2024</span><p>SIGIR Best Paper Honorable Mention <em>最佳论文提名奖</em></p></div>
  <div><span>2023</span><p>CAS Presidential Scholarship <em>中国科学院院长奖</em></p></div>
  <div><span>2023</span><p>Beijing Outstanding Graduate Student Awards <em>北京市优秀毕业生</em></p></div>
  <div><span>2023</span><p>University of CAS Outstanding Graduate Student Awards <em>中国科学院大学优秀毕业生</em></p></div>
</div>

<h2 id="experiences">Experiences</h2>

<div class="home-timeline">

<div class="timeline-item">
  <h3>School of Computer Science and Technology, Shandong University</h3>
  <p><span>2023.07 -- Present</span> Assistant Professor</p>
</div>

<div class="timeline-item">
  <h3>School of Artificial Intelligence, University of Chinese Academy of Sciences</h3>
  <h3>Institute of Automation, Chinese Academy of Sciences</h3>
  <p><span>2019.09 -- 2023.06</span> Ph.D. in Computer Application Technology</p>
  <p class="timeline-advisor">Advisor: Professor Liang Wang</p>
</div>

<div class="timeline-item">
  <h3>School of Mathematics and Systems Science, Beihang University</h3>
  <p><span>2016.09 -- 2019.01</span> M.Sc. in Mathematics</p>
  <p class="timeline-advisor">Advisor: Professor Xin Jiang</p>
</div>

<div class="timeline-item">
  <h3>School of Mathematics and Computational Science, Xiangtan University</h3>
  <p><span>2012.09 -- 2016.06</span> B.Sc. in Mathematics</p>
  <p class="timeline-advisor">Advisor: Professor Huayi Wei</p>
</div>

</div>

<h2 id="professional-services">Professional Services</h2>

<div class="service-grid">
  <div class="service-card">
    <span>Area Chair</span>
    <p>ACL Rolling Review</p>
  </div>
  <div class="service-card">
    <span>Conference Reviewer</span>
    <p>NeurIPS, ICLR, ICML, KDD, SIGIR, AAAI, ACL, EMNLP, etc.</p>
  </div>
  <div class="service-card">
    <span>Journal Reviewer</span>
    <p>IEEE TKDE, TOIS, Pattern Recognition, IEEE TBD, Neural Networks, etc.</p>
  </div>
</div>
