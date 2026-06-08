# GPT-based Prediction Program

## ver.Kor

# GPT 기반 예측 프로그램

## 소개

이 프로젝트는 GPT를 활용하여 사용자가 입력한 데이터를 분석하고, 이를 기반으로 예측 결과를 제공하는 프로그램입니다.  
입력된 정보에서 의미 있는 패턴을 파악하고, 자연어 기반의 분석 결과를 함께 제공하여 사용자가 예측 결과를 쉽게 이해할 수 있도록 돕는 것을 목표로 합니다.

## 주요 기능

- GPT 기반 데이터 분석 및 예측 결과 생성
- 입력 데이터에 대한 자연어 기반 해석 제공
- 사용자가 이해하기 쉬운 형태의 결과 출력
- 다양한 입력값을 활용한 예측 시나리오 지원
- 간단한 실행 방식으로 누구나 쉽게 사용 가능

## 사용 방법

1. 프로젝트 다운로드

```bash
git clone https://github.com/MyoungSeok-Song/Song.gpt.ai-best.git
```

2. 프로젝트 폴더로 이동

```bash
cd Song.gpt.ai-best
```

3. 필요한 라이브러리 설치

```bash
python3 -m pip install -r requirements.txt
```

4. OpenAI API 키 설정

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

5. 프로그램 실행

```bash
python3 main.py --scenario sales --data "지난 4주 매출: 120, 135, 128, 160. 광고비는 3주차부터 증가."
```

파일 입력도 사용할 수 있습니다.

```bash
python3 main.py --scenario study --file sample.txt
```

JSON 그대로 출력하려면 `--json` 옵션을 추가합니다.

```bash
python3 main.py --scenario finance --data "..." --json
```

기본 모델은 `gpt-5.5`이며, 필요하면 `OPENAI_MODEL` 환경변수나 `--model` 옵션으로 바꿀 수 있습니다.

## 라이선스

MIT License

이 프로젝트는 MIT License를 따릅니다.  
자유롭게 사용, 수정, 배포할 수 있습니다.

---

## ver.Eng

# GPT-based Prediction Program

## Introduction

This project is a prediction program that uses GPT to analyze user-provided data and generate prediction results.  
It aims to identify meaningful patterns from the input data and provide natural language explanations so that users can easily understand the prediction results.

## Key Features

- GPT-based data analysis and prediction generation
- Natural language explanation of input data and prediction results
- Easy-to-understand result output
- Support for various prediction scenarios using different types of input data
- Simple execution process for easy use

## How to Use

1. Download the project

```bash
git clone https://github.com/MyoungSeok-Song/Song.gpt.ai-best.git
```

2. Move to the project folder

```bash
cd Song.gpt.ai-best
```

3. Install the required libraries

```bash
python3 -m pip install -r requirements.txt
```

4. Set your OpenAI API key

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

5. Run the program

```bash
python3 main.py --scenario sales --data "Last 4 weeks of revenue: 120, 135, 128, 160. Ad spend increased from week 3."
```

You can also read input from a file.

```bash
python3 main.py --scenario study --file sample.txt
```

Use `--json` to print the raw JSON result.

```bash
python3 main.py --scenario finance --data "..." --json
```

The default model is `gpt-5.5`. You can change it with the `OPENAI_MODEL` environment variable or the `--model` option.

## License

MIT License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project.
