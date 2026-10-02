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

  <div class="article-grid" id="latest-articles">
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


<script>
(function(){
  const grid=document.getElementById('latest-articles');
  if(!grid) return;

  const api='https://api.github.com/repos/hwsr6028-source/hwsr6028-source.github.io/contents/_posts?ref=main';

  const esc=s=>String(s||'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));

  function parseFrontMatter(text){
    const m=text.match(/^---\s*\n([\s\S]*?)\n---/);
    if(!m) return {};
    const out={};
    m[1].split('\n').forEach(line=>{
      const i=line.indexOf(':');
      if(i<0) return;
      const k=line.slice(0,i).trim();
      let v=line.slice(i+1).trim();
      if((v.startsWith('"')&&v.endsWith('"'))||(v.startsWith("'")&&v.endsWith("'"))) v=v.slice(1,-1);
      out[k]=v.replace(/\\\"/g,'"').replace(/\\\\/g,'\\');
    });
    return out;
  }

  function slugFromName(name){
    return name.replace(/^\d{4}-\d{2}-\d{2}-/,'').replace(/\.md$/,'');
  }

  function card(p){
    const url='/insight/'+encodeURI(p.slug)+'/';
    const thumb=p.thumbnail
      ? '<div class="thumb thumb-image"><img src="'+esc(p.thumbnail)+'" alt="'+esc(p.title)+'"></div>'
      : '<div class="thumb thumb-empty"><span>병원정보 칼럼</span></div>';
    const date=(p.date||'').slice(0,10).replace(/-/g,'.');
    return '<article class="article-card"><a href="'+url+'">'+thumb+
      '<span class="tag">'+esc(p.category||'')+'</span>'+
      '<h3>'+esc(p.title||'')+'</h3>'+
      '<p>'+esc(p.description||'')+'</p>'+
      '<small>'+esc(date)+'</small></a></article>';
  }

  fetch(api,{cache:'no-store'})
    .then(r=>{if(!r.ok) throw new Error('list'); return r.json();})
    .then(files=>{
      const recent=files.filter(f=>f.type==='file'&&f.name.endsWith('.md'))
        .sort((a,b)=>b.name.localeCompare(a.name))
        .slice(0,12);
      return Promise.all(recent.map(f=>fetch(f.download_url,{cache:'no-store'}).then(r=>r.text()).then(t=>{
        const fm=parseFrontMatter(t);
        return {...fm,slug:slugFromName(f.name)};
      })));
    })
    .then(posts=>{
      posts.sort((a,b)=>new Date(b.date||0)-new Date(a.date||0));
      const six=posts.slice(0,6);
      if(six.length) grid.innerHTML=six.map(card).join('');
    })
    .catch(()=>{});
})();
</script>

