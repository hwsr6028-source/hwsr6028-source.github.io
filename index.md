---
layout: default
title: "병원정보 칼럼"
description: "피부 시술과 피부 고민을 쉽고 정확하게 설명하는 병원정보 칼럼"
permalink: /
---
<main>
<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">MEDICAL INFORMATION COLUMN</p>
    <h1>피부·시술 정보를<br>쉽고 정확하게</h1>
    <p>리프팅, 스킨부스터, 색소, 여드름, 톡신·필러 등 피부 고민에 필요한 정보를 주제별로 확인해보세요.</p>
    <a class="btn" href="{{ '/blog/insight/' | relative_url }}">전체 칼럼 보기</a>
  </div>
  <div class="hero-card">
    <span>INFORMATION ARCHIVE</span>
    <h2>궁금한 피부 정보를<br>한곳에서 확인하세요</h2>
    <p>각 칼럼은 주제별로 정리되어 독립된 페이지에서 확인할 수 있습니다.</p>
  </div>
</section>

<section class="section soft">
  <div class="section-head">
    <div>
      <p class="eyebrow">LATEST</p>
      <h2>최근 칼럼</h2>
    </div>
    <a href="{{ '/blog/insight/' | relative_url }}">전체보기 →</a>
  </div>

  <div class="article-grid">
    {% for post in site.posts limit:6 %}
    <article class="article-card">
      <a href="{{ post.url | relative_url }}">
        {% if post.thumbnail %}
        <div class="thumb thumb-image">
          <img src="{{ post.thumbnail }}" alt="{{ post.title }}">
        </div>
        {% else %}
        <div class="thumb thumb-empty">
          <span>병원정보 칼럼</span>
        </div>
        {% endif %}
        <span class="tag">{{ post.category }}</span>
        <h3>{{ post.title }}</h3>
        <p>{{ post.description }}</p>
        <small>{{ post.date | date: "%Y.%m.%d" }}</small>
      </a>
    </article>
    {% endfor %}
  </div>
</section>
</main>
