---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* BSc in Information Engineering, University of Padova, 2016
* MSc in Bioengineering, University of Padova, 2019
* PhD in Information Engineering (Bioengineering curricula), University of Padova, 2020

Academic experience
======
* 2025-now: Junior PostDoc Research Fellow
  * Department of Information Engineering, University of Padova, Padova, Italy
  * Project: Development of a clinical decision support system for data interpretation and therapy management in pediatric patients with type 1 diabetes
  * Supervisor: Prof. Andrea Facchinetti
  

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  