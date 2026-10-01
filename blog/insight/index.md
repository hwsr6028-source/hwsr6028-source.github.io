---
layout: default
title: "인사이트"
seo_title: "병원정보 칼럼 | 피부 시술 인사이트"
description: "피부 고민과 시술 정보를 주제별로 정리한 병원정보 칼럼입니다."
permalink: /blog/insight/
---
<main class="insight-page">
  <section class="insight-hero">
    <p class="eyebrow">MEDICAL INFORMATION COLUMN</p>
    <h1>병원정보 칼럼</h1>
    <p>피부 고민과 시술에 대해 알아두면 좋은 정보를<br>주제별로 쉽고 정확하게 정리했습니다.</p>
  </section>

  <section class="insight-wrap">
    <div class="insight-filter" id="categories">
      <a class="filter active" href="#all" data-filter="all">전체</a>
      <a class="filter" href="#lifting" data-filter="리프팅">리프팅</a>
      <a class="filter" href="#skinbooster" data-filter="스킨부스터">스킨부스터</a>
      <a class="filter" href="#pigmentation" data-filter="색소">색소</a>
      <a class="filter" href="#acne" data-filter="여드름">여드름</a>
      <a class="filter" href="#tox-filler" data-filter="톡신/필러">톡신/필러</a>
      <a class="filter" href="#hair-removal" data-filter="제모">제모</a>
      <a class="filter" href="#body" data-filter="바디">바디</a>
      <a class="filter" href="#skin-care" data-filter="피부관리">피부관리</a>
    </div>

    <div class="insight-list" id="insightList">
      {% for post in site.posts %}
      <article class="insight-row" data-category="{{ post.category | escape }}">
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
      <p class="insight-empty" id="insightEmpty" hidden>해당 카테고리의 칼럼이 아직 없습니다.</p>
    </div>
  </section>
</main>

<script>
document.addEventListener('DOMContentLoaded', function () {
  const buttons = Array.from(document.querySelectorAll('.insight-filter .filter'));
  const rows = Array.from(document.querySelectorAll('.insight-row'));
  const empty = document.getElementById('insightEmpty');

  const hashMap = {
    '#all': 'all',
    '#lifting': '리프팅',
    '#skinbooster': '스킨부스터',
    '#pigmentation': '색소',
    '#acne': '여드름',
    '#tox-filler': '톡신/필러',
    '#hair-removal': '제모',
    '#body': '바디',
    '#skin-care': '피부관리'
  };

  function applyFilter(category) {
    let visible = 0;

    rows.forEach(function (row) {
      const show = category === 'all' || row.dataset.category === category;
      row.hidden = !show;
      if (show) visible += 1;
    });

    buttons.forEach(function (button) {
      button.classList.toggle('active', button.dataset.filter === category);
    });

    if (empty) empty.hidden = visible !== 0;
  }

  function applyHash() {
    const category = hashMap[window.location.hash] || 'all';
    applyFilter(category);
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      applyFilter(button.dataset.filter);
    });
  });

  window.addEventListener('hashchange', applyHash);
  applyHash();
});
</script>
