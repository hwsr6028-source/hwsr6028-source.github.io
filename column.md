---
layout: default
title: "FINE COLUMN"
description: "id clinic의 피부·시술 정보 칼럼 전체 목록"
permalink: /column/
---
<main><section class="column-hero"><p class="eyebrow">FINE COLUMN</p><h1>궁금한 피부 정보를<br>쉽고 정확하게</h1><p>검색 사용자에게 실제 도움이 되는 질문형·정보형 칼럼을 축적합니다.</p></section>
<section class="section" id="categories"><div class="filters"><a class="filter active" href="{{ '/column/' | relative_url }}">전체</a><span class="filter">리프팅</span><span class="filter">스킨부스터</span><span class="filter">색소</span><span class="filter">여드름</span><span class="filter">톡신/필러</span></div>
<div class="article-list">{% for post in site.posts %}<a class="list-card" href="{{ post.url | relative_url }}"><div class="thumb"></div><div><span class="tag">{{ post.category }}</span><h2>{{ post.title }}</h2><p>{{ post.description }}</p><small>{{ post.date | date: "%Y.%m.%d" }} · id clinic</small></div></a>{% endfor %}</div></section></main>