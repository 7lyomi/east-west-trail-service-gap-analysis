from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def call(script: Path, *args: str) -> None:
    cmd = [sys.executable, str(script), *args]
    print("[RUN]", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="동서트레일 최종 분석 전체 재현")
    parser.add_argument("--raw-root", type=Path, required=True, help="사용자 제공 원자료가 있는 상위 폴더")
    parser.add_argument("--clean", action="store_true", help="기존 outputs/figures/report/qa를 삭제하고 처음부터 실행")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    src = root / "src"
    inputs = root / "inputs"
    outputs = root / "outputs"
    figures = root / "figures"
    report = root / "report"
    qa = root / "qa"
    if args.clean:
        for p in (outputs, figures, report, qa):
            if p.exists():
                shutil.rmtree(p)
    for p in (outputs, figures, report, qa):
        p.mkdir(parents=True, exist_ok=True)

    call(src / "survey_analysis.py", "--raw-root", str(args.raw_root), "--output-dir", str(outputs))
    call(src / "tourism_analysis.py", "--inputs-dir", str(inputs), "--output-dir", str(outputs))
    call(src / "spatial_preprocess.py", "--raw-root", str(args.raw_root), "--inputs-dir", str(inputs), "--output-dir", str(outputs))
    call(src / "scoring.py", "--raw-root", str(args.raw_root), "--inputs-dir", str(inputs), "--output-dir", str(outputs))
    call(src / "figures.py", "--raw-root", str(args.raw_root), "--csv-dir", str(outputs), "--fig-dir", str(figures))
    call(src / "report_builder.py", "--csv-dir", str(outputs), "--fig-dir", str(figures), "--inputs-dir", str(inputs), "--report-dir", str(report))
    call(src / "qa_checks.py", "--outputs", str(outputs), "--figures", str(figures), "--report", str(report), "--qa-dir", str(qa))
    print("전체 분석·보고서·QA 완료", flush=True)


if __name__ == "__main__":
    main()
