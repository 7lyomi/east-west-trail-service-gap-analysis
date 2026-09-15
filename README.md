# 🌲 East-West Trail Service Gap Analysis

> **긴 구간이 아니라, 비어 있는 기능이 우선순위다.**  
> 동서트레일 공개구간의 이동부담과 시·종점 주변 서비스 접근성을 결합해 숙박·식음·보급·교통의 공백을 진단하고, 구간별 보완 우선순위와 운영모델을 제안한 프로젝트입니다.

## Project Info

- **Type**: 2-person team project
- **Team**: [7lyomi](https://github.com/7lyomi), [jaebok1211](https://github.com/jaebok1211)
- **Period**: 2026
- **Domain**: Forestry statistics / Spatial analysis / Tourism policy
- **Tech**: Python, Pandas, NumPy, Statsmodels, GeoPandas, Shapely, Matplotlib

> 이 저장소는 2인 팀 프로젝트의 **7lyomi 포트폴리오 정리본**입니다. 분석 아이디어와 산출물은 팀 공동 프로젝트이며, 개인 단독 프로젝트로 표시하지 않습니다.

---

## Problem

장거리 트레일에서 단순히 “구간이 길다”는 이유만으로 시설 투자 우선순위를 정하면 실제 이용자가 필요한 기능과 어긋날 수 있습니다.

> **이동부담이 큰 구간 중 숙박·식음·보급·교통 가운데 실제로 부족한 기능은 무엇이며, 어느 구간을 먼저 보완해야 하는가?**

## Data

- **개인 단위**: 산림휴양복지활동조사
- **구간 단위**: 동서트레일 공식 코스 정보, 거리·시간·난이도·GPX
- **시설 단위**: 숙박·음식·상점·버스정류장 등 공공데이터
- **시·군 단위**: 한국관광 데이터랩의 방문·체류·소비 관련 지표

원자료는 데이터 제공기관의 이용조건을 고려해 재배포하지 않습니다.

## Analysis Framework

```text
숙박형 산림활동 수요 특성 분석
        ↓
공개구간 이동부담 계산
        ↓
시·종점 주변 서비스 접근성 분석
        ↓
숙박·식음·보급·교통별 기능 공백 산출
        ↓
구간별 최대 공백 기준 우선순위 선정
        ↓
지역 시장여건·기존자원 확인
        ↓
구간별 맞춤형 운영모델 제안
```

### Mobility Need

```text
체류·보급 필요도
= (거리 백분위 + 소요시간 백분위 + 난이도 환산값) / 3
```

### Service Accessibility

시작점과 종점 **모두**를 확인하고 두 끝점 중 더 낮은 접근성을 구간 접근성으로 사용했습니다. 숙박·보급·교통은 1km/3km 기준, 식음은 거리와 이용 가능한 시설 수를 함께 고려했습니다.

### Functional Service Gap

```text
기능별 공백 = 이동부담 × (1 - 기능별 접근성)
```

## Key Findings

- 숙박형 이용자의 1인 1회 평균 소비는 약 **18.1만 원**, 당일형은 약 **6.2만 원**으로 나타났습니다.
- 최대 서비스 공백 기준 상위 구간은 **54, 53, 51, 12, 47구간** 등이었고, 상위 5개 중 4개가 봉화·울진의 동부권에 위치했습니다.
- 물리적 이동부담이 높더라도 시·종점 주변 서비스가 충분하면 최종 공백순위는 낮아졌습니다.

## Recommended Operation Models

- **보급 지원형**: 식사·식수·기초 보급 지원
- **상업숙박·마을서비스 전환형**: 마을민박·대피소 등 기존 자원 연계
- **기본관리·기존자원 연계형**: 신규시설보다 정보·예약 연결 강화
- **교통 추가확인형**: 노선·배차·막차 확인 후 필요 시 셔틀 실증

## Validation

- 공식 GPX 시·종점 및 방향 재확인
- 시설 좌표·중복·영업상태·행정경계 검토
- 우선순위 상위구간 시설 재확인
- 대표 난이도와 보수적 난이도 가정 비교를 통한 **민감도 분석**
- 별도 QA 스크립트를 통한 결과 검증

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── run_all.py
├── DATA_POLICY.md
├── src/
│   ├── common.py
│   ├── survey_analysis.py
│   ├── tourism_analysis.py
│   ├── spatial_preprocess.py
│   ├── scoring.py
│   ├── figures.py
│   ├── report_builder.py
│   └── qa_checks.py
├── figures/
└── docs/
    ├── report.pdf
    └── presentation.pdf
```

## Run

```bash
pip install -r requirements.txt
python run_all.py --raw-root /path/to/raw_data
```

## Limitations

- 숙박형 이용자의 소비 분석은 동서트레일 이용객의 실제 소비를 직접 추적한 결과가 아닙니다.
- 통계모형의 Odds Ratio는 관련성을 나타내며 인과관계를 의미하지 않습니다.
- 개인·구간·시설·시군 데이터는 단위가 달라 무리하게 하나의 단일 지수로 합치지 않았습니다.
- 교통은 정류장 위치 중심 분석이므로 실제 노선·배차·막차 확인이 추가로 필요합니다.
