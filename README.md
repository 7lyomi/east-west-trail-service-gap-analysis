# East-West Trail Service Gap Analysis

산림청이 주최한 2026 임업통계 활용 경진대회에 2인 팀으로 참가하여 동서트레일 공개구간의 이동부담과 시·종점 주변 서비스 접근성을 결합해 숙박·식음·보급·교통 공백을 분석하고 보완 우선순위를 제안한 프로젝트입니다.

- **Team**: [7lyomi](https://github.com/7lyomi), [jaebok1211](https://github.com/jaebok1211)
- **Year**: 2026
- **Result**: 장려상
- **Data**: 산림휴양복지활동조사, 동서트레일 코스·GPX, 숙박·상가·교통 공공데이터, 한국관광 데이터랩
- **Tech**: Python, Pandas, NumPy, Statsmodels, scikit-learn, pyproj, Matplotlib

## Contribution

- 문제 정의 및 분석 프레임 설계
- 서비스 공백 결과 해석과 구간별 운영모델 정리
- 보고서·발표 구성

## 분석 목표

구간 길이나 난이도만으로 시설 투자 우선순위를 정하지 않고, **이용 부담이 큰 구간에서 실제로 부족한 서비스가 무엇인지**를 구분하는 것을 목표로 했습니다.

## 분석 흐름

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
구간별 운영모델 제안
```

### 이동부담

```text
체류·보급 필요도
= (거리 백분위 + 소요시간 백분위 + 난이도 환산값) / 3
```

### 서비스 접근성

시작점과 종점을 모두 확인하고, 두 끝점 중 더 낮은 접근성을 해당 구간의 접근성으로 사용했습니다.

- 숙박·보급·교통: 1km / 3km 기준
- 식음: 거리와 이용 가능한 시설 수를 함께 반영

### 기능별 서비스 공백

```text
기능별 공백 = 이동부담 × (1 - 기능별 접근성)
```

## 주요 결과

- 숙박형 산림활동 이용자의 1인 1회 평균 소비는 약 **18.1만 원**, 당일형은 약 **6.2만 원**으로 나타났습니다.
- 최대 서비스 공백 기준 상위 구간은 **54, 53, 51, 12, 47구간** 등이었습니다.
- 상위 5개 구간 중 4개가 봉화·울진의 동부권에 위치했습니다.
- 이동부담이 높더라도 시·종점 주변 서비스가 충분하면 최종 공백순위는 낮아졌습니다.


<img width="2267" height="1128" alt="trail_overall_priority_map" src="https://github.com/user-attachments/assets/04ce1c84-5866-48ba-9665-2dd8dea4c926" />

분석 결과에 따라 구간별 대응방식도 구분했습니다.

- **보급 지원형**: 식사·식수·기초 보급 지원
- **숙박·마을서비스 연계형**: 마을민박·대피소 등 기존 자원 활용
- **기존자원 연계형**: 신규시설보다 정보·예약 연결 강화
- **교통 추가확인형**: 노선·배차·막차 확인 후 필요 시 셔틀 검토

<img width="2041" height="1090" alt="trail_need_gap_typology" src="https://github.com/user-attachments/assets/810a1867-5da9-4d53-ba81-a7189dbde4a4" />

## 검증

- 공식 GPX 시·종점 및 방향 재확인
- 시설 좌표·중복·영업상태·행정경계 검토
- 우선순위 상위구간 시설 재확인
- 대표 난이도와 보수적 난이도 가정을 비교한 민감도 분석
- 별도 QA 스크립트를 통한 산출물 검증

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── run_all.py
├── DATA_POLICY.md
├── inputs/
│   └── README.md
└── src/
    ├── common.py
    ├── survey_analysis.py
    ├── tourism_analysis.py
    ├── spatial_preprocess.py
    ├── scoring.py
    ├── figures.py
    ├── report_builder.py
    └── qa_checks.py
```

`run_all.py` 실행 시 `outputs/`, `figures/`, `report/`, `qa/`가 로컬에서 생성됩니다. 원자료와 생성 산출물은 저장소에 커밋하지 않습니다.

## Run

```bash
pip install -r requirements.txt
python run_all.py --raw-root /path/to/raw_data
```

필요한 로컬 입력 파일은 [`inputs/README.md`](inputs/README.md)에 정리했습니다.

보고서 PDF 생성과 QA까지 실행하려면 로컬 환경에 **LibreOffice (`soffice`)**와 **Poppler (`pdfinfo`)**가 필요합니다.

## Limitations

- 숙박형 이용자의 소비 분석은 동서트레일 이용객의 실제 소비를 직접 추적한 결과가 아닙니다.
- 통계모형의 Odds Ratio는 관련성을 나타내며 인과관계를 의미하지 않습니다.
- 개인·구간·시설·시군 데이터는 분석 단위가 달라 하나의 단일 지수로 직접 합치지 않았습니다.
- 교통 분석은 정류장 위치 중심이므로 실제 노선·배차·막차 확인이 추가로 필요합니다.
