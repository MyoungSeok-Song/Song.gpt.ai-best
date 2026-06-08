"""GPT-based prediction CLI using the OpenAI Responses API."""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_MODEL = "gpt-5.5"


@dataclass
class PredictionRequest:
    scenario: str
    data: str
    output_language: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze user-provided data and generate GPT-based predictions.",
    )
    parser.add_argument(
        "-d",
        "--data",
        help="Input data to analyze. If omitted, the program reads from standard input.",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=Path,
        help="Path to a text file containing input data.",
    )
    parser.add_argument(
        "-s",
        "--scenario",
        default="general",
        help="Prediction scenario, such as sales, health, study, finance, or general.",
    )
    parser.add_argument(
        "-l",
        "--language",
        default="Korean",
        help="Output language for the prediction report.",
    )
    parser.add_argument(
        "-m",
        "--model",
        default=os.getenv("OPENAI_MODEL", DEFAULT_MODEL),
        help="OpenAI model to use. Defaults to OPENAI_MODEL or gpt-5.5.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the raw JSON prediction object instead of a formatted report.",
    )
    return parser.parse_args()


def load_input(args: argparse.Namespace) -> str:
    if args.file:
        if not args.file.exists():
            raise FileNotFoundError(f"Input file not found: {args.file}")
        return args.file.read_text(encoding="utf-8").strip()

    if args.data:
        return args.data.strip()

    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    print("Enter input data. Press Ctrl+D when finished:")
    return sys.stdin.read().strip()


def build_prompt(request: PredictionRequest) -> str:
    return f"""
You are a careful prediction analyst.

Analyze the user's data and create a practical prediction report.
Use the requested scenario to decide what outcomes are most relevant.

Scenario: {request.scenario}
Output language: {request.output_language}

Return only valid JSON with this exact shape:
{{
  "summary": "short explanation of the input data",
  "prediction": "main prediction result",
  "confidence": "low | medium | high",
  "key_patterns": ["pattern 1", "pattern 2", "pattern 3"],
  "risks": ["risk 1", "risk 2"],
  "recommended_actions": ["action 1", "action 2", "action 3"]
}}

User data:
{request.data}
""".strip()


def generate_prediction(model: str, request: PredictionRequest) -> dict[str, Any]:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "The OpenAI Python package is not installed. Run: python3 -m pip install -r requirements.txt"
        ) from exc

    client = OpenAI()
    response = client.responses.create(
        model=model,
        input=build_prompt(request),
    )
    output_text = response.output_text.strip()

    try:
        parsed = json.loads(output_text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Model did not return valid JSON:\n{output_text}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("Model response JSON must be an object.")

    return parsed


def format_report(result: dict[str, Any]) -> str:
    key_patterns = "\n".join(f"- {item}" for item in result.get("key_patterns", []))
    risks = "\n".join(f"- {item}" for item in result.get("risks", []))
    actions = "\n".join(f"- {item}" for item in result.get("recommended_actions", []))

    return f"""
Summary
{result.get("summary", "")}

Prediction
{result.get("prediction", "")}

Confidence
{result.get("confidence", "")}

Key Patterns
{key_patterns}

Risks
{risks}

Recommended Actions
{actions}
""".strip()


def main() -> int:
    args = parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.", file=sys.stderr)
        return 1

    try:
        data = load_input(args)
        if not data:
            print("Error: input data is empty.", file=sys.stderr)
            return 1

        request = PredictionRequest(
            scenario=args.scenario,
            data=data,
            output_language=args.language,
        )
        result = generate_prediction(args.model, request)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_report(result))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
