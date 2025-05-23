"""구성 정보의 타입을 지정합니다.

hydra가 config/config.yaml에서 자동으로 생성하는 구성 정보의 타입을 지정합니다.
정밀한 타입 힌트 지원을 위해 사용합니다.

Usage:

    config = Config()
    config.name         # str
"""



from dataclasses import dataclass
from omegaconf import DictConfig

@dataclass
class Config(DictConfig):
    ...