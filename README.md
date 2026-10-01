# id clinic FINE COLUMN

무료 배포 주소: https://hwsr6028-source.github.io

## 대량 칼럼 발행
1. bulk_columns.csv에 글 추가
2. python tools/import_columns.py 실행
3. 생성된 _posts/*.md 커밋
4. main 브랜치에 반영되면 GitHub Pages 자동 배포

## SEO 구조
- 글별 고유 URL
- SEO title / meta description / canonical
- Article JSON-LD
- sitemap.xml 자동 생성
- rss.xml 자동 생성
- robots.txt
- 관련 글 내부 링크

## 최초 GitHub Pages 설정
Settings > Pages > Build and deployment > Source에서 GitHub Actions를 선택하세요.
<!-- redeploy trigger -->
