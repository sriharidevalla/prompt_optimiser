
"""A small command-line tool to optimize prompts for large language models."""

from __future__ import annotations

import argparse
import json
import os
from typing import Dict, Iterable, List


DEFAULT_PROFILE: Dict[str, object] = {
    "base_instructions": [
        "Use clear and concise language",
        "Provide examples when relevant",
        "Structure the response in short paragraphs",
    ],
    "tone_specific": {
        "formal": ["Maintain a professional tone."],
        "creative": [
            "Feel free to use expressive language and imagery.",
            "Incorporate metaphors or analogies where appropriate.",
        ],
        "informal": ["Write in a friendly and conversational style."],
    },
}


class PromptOptimizer:
    """Optimize prompts using configurable instruction profiles."""

    def __init__(self, profile: Dict[str, object] | None = None) -> None:
        self.profile = profile or DEFAULT_PROFILE

    @classmethod
    def from_file(cls, path: str) -> "PromptOptimizer":
        """Load a profile from a JSON file."""
        with open(path, "r", encoding="utf-8") as fh:
            profile = json.load(fh)
        return cls(profile)

    def _gather_instructions(self, tone: str) -> Iterable[str]:
        base: List[str] = self.profile.get("base_instructions", [])
        tone_map: Dict[str, List[str]] = self.profile.get("tone_specific", {})
        return list(base) + tone_map.get(tone, [])

    def optimize(self, prompt: str, tone: str = "formal") -> str:
        base_prompt = prompt.strip().rstrip(".?!")
        instructions = "\n- ".join(self._gather_instructions(tone))
        return (
            "Please respond to the following prompt with a detailed and well-structured answer.\n"
            f"Prompt: {base_prompt}.\n\nInstructions for the response:\n- {instructions}"
        )


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Optimize prompts for LLMs")
    parser.add_argument("prompt", nargs="?", help="Prompt text. If omitted, read from stdin")
    parser.add_argument(
        "--tone",
        choices=["formal", "creative", "informal"],
        default="formal",
        help="Instruction style to apply",
    )
    parser.add_argument(
        "--profile",
        help="Path to JSON file with instruction profile",
    )
    parser.add_argument(
        "--output-file",
        help="Write the optimized prompt to this file",
    )
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)

    prompt_text = args.prompt
    if prompt_text is None:
        prompt_text = input("Enter a prompt: ")

    optimizer = (
        PromptOptimizer.from_file(args.profile) if args.profile else PromptOptimizer()
    )
    optimized = optimizer.optimize(prompt_text, tone=args.tone)

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as fh:
            fh.write(optimized)
    else:
        print(optimized)


if __name__ == "__main__":
    main()
