"""Command-line demo for OS Resource Guardian Agent."""

from __future__ import annotations

import argparse

from src.analyzer import analyze_snapshot
from src.collector import collect_snapshot
from src.recommender import build_genai_prompt, generate_recommendations
from src.reporter import format_report, save_json_report, save_text_report


def main() -> None:
    parser = argparse.ArgumentParser(description="OS Resource Guardian Agent CLI")
    parser.add_argument("--save", action="store_true", help="Save text and JSON reports into the reports folder.")
    parser.add_argument("--genai-prompt", action="store_true", help="Print a GenAI prompt for ChatGPT/Claude/Perplexity.")
    parser.add_argument("--limit", type=int, default=5, help="Number of top processes to display.")
    args = parser.parse_args()

    snapshot = collect_snapshot(limit=args.limit)
    analysis = analyze_snapshot(snapshot)
    recommendations = generate_recommendations(snapshot, analysis)
    report = format_report(snapshot, analysis, recommendations)

    print(report)

    if args.genai_prompt:
        print("\n" + "=" * 58)
        print("GenAI Prompt for Explanation")
        print("=" * 58)
        print(build_genai_prompt(snapshot, analysis))

    if args.save:
        txt_path = save_text_report(report)
        json_path = save_json_report(snapshot, analysis, recommendations)
        print(f"\nSaved text report: {txt_path}")
        print(f"Saved JSON report: {json_path}")


if __name__ == "__main__":
    main()
