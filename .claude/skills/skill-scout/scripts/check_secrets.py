#!/usr/bin/env python3
"""
push前の秘密情報チェック。
git diff --cached (ステージされた追加行) を対象に、公開してはいけないパターンを検出する。
検出したら exit code 1 で終了する。ルーティン・pre-pushフックの両方から呼ぶ想定。

正規表現で機械的に拾えるのは一部だけ。企業名・顧客名・実案件の中身は
このスクリプトでは検出できないため、必ず人間 (またはルーティンの目視レビュー) と併用する。
"""
import re
import subprocess
import sys

PATTERNS = {
    "メールアドレス": re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}"),
    "日本の電話番号": re.compile(r"0\d{1,4}-\d{1,4}-\d{3,4}"),
    "郵便番号": re.compile(r"〒?\d{3}-\d{4}"),
    "AWSアクセスキー": re.compile(r"AKIA[0-9A-Z]{16}"),
    "GitHubトークン": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "OpenAI/Anthropicキー": re.compile(r"sk-(ant-)?[A-Za-z0-9_-]{20,}"),
    "Slackトークン": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    "秘密鍵ヘッダー": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "汎用シークレット変数": re.compile(
        r"(?i)(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*['\"][A-Za-z0-9/+_=-]{12,}['\"]"
    ),
}

# ファイル名だけで即アウトにするもの
DANGEROUS_FILENAMES = re.compile(r"(^|/)(\.env(\..*)?|.*\.pem|.*\.key|id_rsa.*)$")


def get_staged_diff() -> str:
    result = subprocess.run(
        ["git", "diff", "--cached", "-U0"],
        capture_output=True, encoding="utf-8", errors="replace", check=True,
    )
    return result.stdout or ""


def get_staged_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True, encoding="utf-8", errors="replace", check=True,
    )
    return [f for f in (result.stdout or "").splitlines() if f]


def main() -> int:
    findings = []

    for f in get_staged_files():
        if DANGEROUS_FILENAMES.search(f):
            findings.append(f"[危険なファイル名] {f}")

    diff = get_staged_diff()
    added_lines = [
        line[1:] for line in diff.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    ]

    for label, pattern in PATTERNS.items():
        for line in added_lines:
            m = pattern.search(line)
            if m:
                findings.append(f"[{label}] {m.group(0)[:40]}")

    if findings:
        print("push前チェックで疑わしい内容が見つかりました。コミット・pushを中止してください:")
        for item in dict.fromkeys(findings):  # 重複除去、順序維持
            print(f"  - {item}")
        return 1

    print("push前チェック: 疑わしいパターンは見つかりませんでした。")
    print("(注意: 企業名・顧客名・実案件の中身は機械的に検出できません。目視でも確認してください)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
