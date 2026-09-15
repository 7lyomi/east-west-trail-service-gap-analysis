# Input Guide

원자료와 검토용 중간 입력은 데이터 제공기관의 이용조건을 고려해 이 저장소에 포함하지 않습니다.

`run_all.py`는 두 종류의 입력을 사용합니다.

## 1. `--raw-root` 아래에서 탐색하는 원자료

파일명 전체가 동일할 필요는 없지만 코드가 다음 키워드로 파일을 탐색합니다.

- `2025_총괄_20260730_40682` — 산림휴양복지활동조사 CSV
- `2025년_산림휴양복지활동조사_파일설계서` — 조사 파일설계서 XLSX
- `1~12`, `47~55`, `전체구간` — 동서트레일 GPX
- `문화`, `농어촌민박업` — 농어촌민박 CSV
- `문화`, `숙박업` — 일반숙박 CSV
- `문화`, `일반야영장업` — 야영장 CSV
- `전국`, `버스정류장`, `위치정보` — 버스정류장 CSV
- `필독`, `파일열람방법` — 상가정보 ZIP

## 2. `inputs/`에 준비하는 정제·검토 입력

```text
route_metadata_official.csv
region_tourism_monthly_clean.csv
tourism_category_shares.csv
endpoint_food_supply_reviewed.csv
named_facility_validation_reviewed.csv
backpacking_support_reviewed.csv
transport_verification_reviewed.csv
reference_list.csv
```

이 파일들은 공식 구간정보, 관광자료 정리본, 상위구간 시설 재검토 결과 등 프로젝트 분석 과정에서 확정한 입력입니다.

> 원자료 자체를 GitHub에 추가하기 전에는 반드시 각 제공기관의 재배포 조건을 다시 확인하세요.
