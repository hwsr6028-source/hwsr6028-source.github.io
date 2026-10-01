---
layout: default
title: "FINE COLUMN"
description: "피부 시술과 피부 고민을 쉽고 정확하게 설명하는 id clinic 칼럼"
permalink: /
---
<main>
<section class="hero"><div class="hero-copy"><p class="eyebrow">FINE BEAUTY BY id</p><h1>검색에서 시작해<br>신뢰로 이어지는<br>FINE COLUMN</h1><p>리프팅, 스킨부스터, 색소, 여드름, 톡신·필러 등 피부 고민에 필요한 정보를 주제별로 확인해보세요.</p><a class="btn" href="{{ '/column/' | relative_url }}">전체 칼럼 보기</a></div><div class="hero-card"><span>SEO CONTENT HUB</span><h2>한 번 쓰고 끝나는 글이 아닌<br>계속 쌓이는 의료정보 자산</h2><p>각 칼럼은 독립 URL, SEO 제목, 설명문, 구조화 데이터와 함께 생성됩니다.</p></div></section>
<section class="section soft"><div class="section-head"><div><p class="eyebrow">LATEST</p><h2>최근 칼럼</h2></div><a href="{{ '/column/' | relative_url }}">전체보기 →</a></div><div class="article-grid">{% for post in site.posts limit:6 %}<article class="article-card"><a href="{{ post.url | relative_url }}"><div class="thumb"></div><span class="tag">{{ post.category }}</span><h3>{{ post.title }}</h3><p>{{ post.description }}</p><small>{{ post.date | date: "%Y.%m.%d" }}</small></a></article>{% endfor %}</div></section>
</main>