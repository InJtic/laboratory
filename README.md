# 🧪 laboratory <!-- omit in toc -->

> 최신 Python 스타일로 실험 구조를 설계하고 관리하는 **개인 연습용 레포지토리**입니다.  
> 코드 작성 관례, 설정 관리, 결과 기록 등 실험 구성 요소를 체계적으로 정리하는 데 초점을 둡니다.  
> 실험 자체는 단순하며, **구조화와 재현 가능성 확보**에 주안점을 둡니다.

---

## 📚 Table of Contents <!-- omit in toc -->

- [🧭 프로젝트 소개](#-프로젝트-소개)
- [🗂 폴더 구조](#-폴더-구조)
- [🧰 기술 스택](#-기술-스택)
- [🧠 실험 개요](#-실험-개요)
- [⚙️ 설정 관리](#️-설정-관리)
- [📁 결과 저장](#-결과-저장)
- [🚀 실행 방식](#-실행-방식)
- [📄 라이선스](#-라이선스)
- [🙋 기타 안내](#-기타-안내)

---

## 🧭 프로젝트 소개

이 프로젝트는 실험을 다음과 같은 관점에서 체계화하려는 시도입니다:

- 최신 Python 코드 스타일 적용 (type hint, pathlib, logging 등)
- 설정을 중앙 집중화하고, 명시적으로 관리
- 실험 결과를 자동 저장하여 재현 가능성 확보
- 코드-설정-결과를 독립적이면서 유기적으로 구성

코드 실험보다는 "구조 실험"에 가깝습니다.  
결과도 중요하지만, 그보다 **실험을 다루는 방식**에 집중합니다.

---

## 🗂 폴더 구조
```
laboratory/
├── .github/             # GitHub Actions 등 워크플로우 정의  
│   └── workflows/  
│       └── ...  
├── pyscripts/           # 실험 관련 Python 코드  
│   ├── __init__.py  
│   ├── schema.py  
│   ├── model.py  
│   └── ...  
├── config/              # Hydra 기반 설정 파일  
│   ├── config.yaml      # 메인 설정 파일  
│   ├── data/  
│   └── model/  
├── test/                # 테스트 코드  
│   └── ...  
├── utils/               # 공통 유틸리티 함수  
│   └── ...  
├── results/             # 실험 결과 저장소  
│   ├── experiment1/  
│   │   ├── README.md  
│   │   ├── log  
│   │   └── config.yaml  
│   └── ...  
├── run.py               # 실험 실행 진입점  
├── pyproject.toml       # Poetry 기반 메타 설정  
├── requirements.txt     # 의존성 파일 (선택적, 참고용)  
├── LICENSE              # 라이선스 (MIT)  
└── .gitignore           # Git 제외 파일 정의  
```
---

## 🧰 기술 스택

- 🐍 Python 3.12.3  
  - CUDA 11.8 환경과 호환됨  
  - 필요 시 3.11로 하향 가능

- 🔥 PyTorch  
  - 기본적인 Transformer 구현에 사용됨

- 🧪 Hydra  
  - 설정의 선언적 관리  
  - 실험 시점에 설정 복사 자동 저장

- 📦 Poetry  
  - 의존성 및 프로젝트 환경 관리

- 📋 Logging  
  - logging 모듈로 실험 로그 기록  
  - 외부 플랫폼 (ex. wandb)은 사용하지 않음

---

## 🧠 실험 개요

**주제: 영어 질의응답 (QA)**  
- 간단한 Transformer 기반 QA 모델 실험  
- 데이터셋은 샘플 수준으로 구성 예정  
- 복잡한 전처리/후처리 없음  

**목표**  
- 코드 구조화: 실험 코드를 `pyscripts/`로 정리  
- 결과 추적: 각 실험은 `results/experimentN/`에 저장  
- 재현 가능성: config + log + 간단한 README 자동 생성  

---

## ⚙️ 설정 관리

설정은 Hydra를 중심으로 구성되며, 다음과 같은 특징을 가집니다:

- 메인 설정 파일: `config/config.yaml`
- 설정 항목: `model`, `data`, `train`, `logging` 등
- 실험 실행 시, 사용된 설정은 `results/experimentN/config.yaml`로 자동 복사
- 설정 파일만으로 실험 재현 가능

예시 설정 (config.yaml):  
```yaml
model:  
 name: transformer  
 hidden_dim: 256  
 num_layers: 4  

data:  
 path: data/sample.csv  
 batch_size: 16  
```
---

## 📁 결과 저장

모든 실험 결과는 `results/` 폴더에 자동 저장됩니다.

예시 구조:  
```
results/  
└── experiment1/  
    ├── README.md       # 간단한 실험 요약 (수동 작성 or 자동 생성)  
    ├── config.yaml     # 사용된 설정 (Hydra에서 복사됨)  
    └── log             # 로그 파일  
```

이 구조를 통해 다음을 보장합니다:  
- 실험 결과 추적  
- 실험 재현 가능  
- 결과 비교 및 문서화  

---

## 🚀 실행 방식

실험은 `run.py`를 통해 실행되며, Hydra CLI와 통합되어 있습니다.

기본 실행:  
```python run.py```

설정 오버라이드 예시:  
```python run.py model.hidden_dim=512 data.batch_size=32```

---

## 📄 라이선스

이 프로젝트는 MIT License 하에 배포됩니다.  
자세한 내용은 LICENSE 파일을 참고하세요.

---

## 🙋 기타 안내

- 본 프로젝트는 **외부 기여나 배포를 염두에 두지 않습니다.**
- 개인 연습 목적이며, 친분 있는 지인들과의 공유를 위해 문서화된 것입니다.
