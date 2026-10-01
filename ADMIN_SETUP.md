# FINE COLUMN 관리자 최초 설정

관리자 주소:
https://hwsr6028-source.github.io/admin/

현재 관리자 UI는 설치되어 있습니다.
로그인과 실제 저장을 활성화하려면 Decap Turbo 무료 설정 1회가 필요합니다.

1. https://decapcms.org/turbo/ 에서 무료 계정 생성
2. Organization 생성
3. GitHub 연결
4. 저장소 hwsr6028-source/hwsr6028-source.github.io 선택
5. Site 생성
   - Branch: main
   - Config path: admin/config.yml
   - Admin interface URL: https://hwsr6028-source.github.io/admin/
6. 생성된 Site ID(UUID)를 복사
7. admin/config.yml의 REPLACE_WITH_DECAP_TURBO_SITE_ID 부분을 해당 Site ID로 교체

교체 후 /admin/에서 로그인 → 새 칼럼 → 작성 → 발행이 가능합니다.
