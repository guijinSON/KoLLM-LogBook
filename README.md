# KoLLM-LogBook 📘

**KoLLM-LogBook**은 Finance, Math, Medical, Programming, Creative Writing 등 15개 분야에서 100개의 프롬프트에 대한 다양한 언어 모델의 답변을 수록하고 있습니다. 
다른 언어 모델들이 같은 질문에 어떠한 방식으로 답하는지 한눈에 보기 쉽게 비교하여, 모델의 한국어 생성 능력을 평가합니다.

## Project Explanation 📄

**KoLLM-LogBook**은 [teknium](https://github.com/teknium1)의 [LLM-Logbook](https://github.com/teknium1/LLM-Logbook)의 한국어 버전으로, 100개의 프롬프트를 통해 언어 모델의 지식, 사고 능력, 창의력 등을 비교하고 있습니다. 

## Prompt Statistics 📄
KoLLM-LogBook은 총 15개 분야에 대해 100개의 프롬프트로 구성되어 있습니다. 프롬프트의 구성은 아래 차트를 참고해주세요.

## Generation Configuration 📄
모든 결과물은 [VLLM](https://github.com/vllm-project/vllm) 패키지와 아래 configuration 을 통해 생성되었습니다. 

```
from vllm import SamplingParams

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens = 512)
```

## How to Navigate 🧭

- [리포트 확인](https://kollm-logbook-qqw6uzf89xizxjilkihjsh.streamlit.app/)

## Adding Models 🤖

추가하고 싶으신 모델이 있으시면 아래 메일로 연락 부탁드립니다.

## License 📝

This project is licensed under the MIT License. For more details, check out the `LICENSE` file.

## Special Thanks to 🙌

- [Teknium1](https://github.com/teknium1) for the contribution to the opensource community and his amazing projects.
- [OneLineAI](https://www.onelineai.com) for supporting my works.

## Contact 📫
질문, 문의 등은 아래 메일로 부탁드립니다.
```
spthsrbwls123@yonsei.ac.kr
```

