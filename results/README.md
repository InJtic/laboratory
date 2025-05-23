# 📊 results/

> 이 디렉토리는 실험 실행 결과를 저장하고 정리하는 공간입니다.  
> 각 실험은 고유의 하위 폴더 (`experiment1/`, `experiment2/` 등)로 분리되며,  
> 설정, 로그, 요약 문서를 포함한 실험 메타데이터를 함께 보관합니다.

---

## 📁 디렉토리 구조

각 실험은 다음과 같은 구조를 가집니다:
```
experimentN/  
├── config.yaml       ← 실험에 사용된 설정 (Hydra에서 자동 저장)  
├── log               ← 로그 파일 또는 디렉토리 (logging 모듈 기반)  
├── README.md         ← 해당 실험에 대한 간단한 설명 (수동 작성 또는 자동 생성)  
└── ... (선택적 출력 파일)
```
예시:  
```
results/  
└── experiment1/  
    ├── config.yaml  
    ├── log  
    ├── README.md  
    └── metrics.json (선택 사항)  
```
---

## 📝 각 파일 설명

- `config.yaml`:  
 Hydra가 실험 실행 시 자동 저장한 설정 파일입니다.  
 이 파일만 있으면 실험 재현이 가능합니다.

- `log`:  
 Python logging 모듈을 사용해 기록된 로그 출력입니다.  
 텍스트 파일 혹은 디렉토리일 수 있으며, 실험 중 발생한 메시지를 담습니다.

- `README.md`:  
 각 실험의 목적, 변경된 설정, 주요 결과 등을 정리합니다.  
 수동 작성이 기본이나, 일부 내용은 자동 생성될 수 있습니다.

- 기타 결과 파일들 (`metrics.json`, `output.txt`, etc.):  
 모델 성능, 예측 결과 등 필요한 항목은 자유롭게 포함 가능합니다.

---

## 🔁 실험 재현 방법

어떤 실험이든 다음 과정을 통해 동일하게 재현할 수 있습니다:

1. 해당 실험 폴더의 `config.yaml` 파일을 복사하거나 참조합니다.  
2. `run.py`를 실행할 때 해당 설정을 명시합니다.  

예:  
```python run.py --config-path results/experiment1 --config-name config``` 

또는, 실험 내용을 `config/config.yaml`에 복사하여 기본 실행으로 재현 가능합니다.

---

## 📌 참고 사항

- `experiment1`, `experiment2` 등 폴더 네이밍은 수동으로 관리됩니다.  
- 동일한 설정이라도 다른 시드나 상황에서 실행될 수 있으므로,  
 동일한 구성으로 여러 번 실험할 경우 `experiment1a`, `experiment1b` 등으로 나눌 수 있습니다.

---

## 🧼 정리 팁

- 실험이 끝난 후에는 꼭 `README.md`를 채워 주세요.  
- 요약에는 다음 정보를 포함하는 것을 권장합니다:  
 - 변경된 설정 값  
 - 주요 성능 지표 (accuracy, loss 등)  
 - 이 실험에서 시도한 의도 또는 특징  

---

## 🧠 예시: experiment1/README.md

실험 목적:
- 모델 hidden_dim을 256에서 512로 변경  
- batch size를 16 → 32로 증가  

결과 요약:  
- val_loss: 1.13 → 0.98  
- EM score: 76.3%  
- 실행 시간: 약 14분  

특이사항:  
- 학습 초반 loss 진동 있음  
- gradient clipping을 고려할 필요 있음

---
