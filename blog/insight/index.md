---
layout: default
title: "인사이트"
seo_title: "피부 시술 인사이트 | id clinic"
description: "피부 고민과 시술에 대한 정보를 id clinic의 관점으로 정리한 인사이트입니다."
permalink: /blog/insight/
---
<main class="insight-page">
  <section class="insight-hero">
    <p class="eyebrow">FINE BEAUTY INSIGHT</p>
    <h1>인사이트</h1>
    <p>피부 고민과 시술에 대해 알아두면 좋은 정보를<br>쉽고 정확하게 정리했습니다.</p>
  </section>

  <section class="insight-wrap">
    <div class="insight-filter">
      <span class="filter active">전체</span>
      <span class="filter">리프팅</span>
      <span class="filter">스킨부스터</span>
      <span class="filter">색소</span>
      <span class="filter">여드름</span>
      <span class="filter">톡신/필러</span>
      <span class="filter">피부관리</span>
    </div>

    <div class="insight-list">
      {% for post in site.posts %}
      <article class="insight-row">
        <a href="{{ post.url | relative_url }}">
          <div class="insight-row-main">
            <h2>{{ post.title }}</h2>
            <p>{{ post.description }}</p>
          </div>
          <div class="insight-row-meta">
            <span>인사이트 · {{ post.category }}</span>
            <time>{{ post.date | date: "%Y-%m-%d" }}</time>
          </div>
        </a>
      </article>
      {% endfor %}
    </div>
  </section>
</main>
