# スキル・カテゴリ整理

`.claude/skills/` にあるスキルを「転職活動」「個人の業務効率」「チームの業務効率」「AIコンサルティング/DX」で棚卸しした一覧。新しいスキルを追加/導入したら、ここにも追記する。

---

## 転職活動で使えるもの

| スキル | 何をするか |
|---|---|
| `job-hunt-kit` | 面接想定問答の作成、企業別面接対策資料、エージェント・企業への返信文面、応募企業一覧の更新 |
| `research-kit`(①企業研究) | 求人票・企業研究の整理、逆質問のネタ出し、懸念点の洗い出し |

---

## 個人の業務効率

| スキル | 何をするか |
|---|---|
| `research-kit` | 汎用リサーチ(企業研究・トレンド調査・情報整理)。目的設定→収集→整理→ファクトチェックの型 |
| `pm-ai-kit`(①⑤ 議事録整理・要件整理) | 会議メモ・ヒアリングメモを構造化する下ごしらえ |
| `note-boss`以下(note記事制作チーム) | note記事のリサーチ→企画→執筆→編集→集客までを一気通貫で回す(副業収益化) |
| `note-thumbnail` | note記事のサムネイルをHTML/SVGで作成 |
| `skill-creator` | 自分専用のスキルを対話的に設計・作成する(Anthropic公式) |
| `web-artifacts-builder` | note記事に埋め込む診断ツールなど、凝ったインタラクティブコンテンツを作る(Anthropic公式) |

---

## チームの業務効率

| スキル | 何をするか |
|---|---|
| `pm-ai-kit`(②③④⑥ 言いにくい文面・比較検討・進捗報告・リスク洗い出し) | PM/PL業務で発生する調整・報告系の下ごしらえ。将来クライアント先で提案する際のネタにもなる |
| `mcp-builder` | 外部API/サービスと連携するMCPサーバーを作る(Anthropic公式。将来チーム/クライアントのツール連携提案に使える) |
| `webapp-testing` | Webアプリの動作確認・UIテストを自動化する(Anthropic公式。チーム開発の品質担保) |

---

## メタ（スキル化の仕組みそのもの）

| スキル | 何をするか |
|---|---|
| `skill-scout` | 日々の作業からスキル化候補を見つけて`backlog.md`に貯め、ネットの公開スキル事例も収集する |

---

## AIコンサルティング／DX（AIコンサルタント就業を見据えたチーム/クライアント向け）

| スキル | 何をするか |
|---|---|
| `dx-consulting-framework` | DX案件を業務・人・組織・技術・定着・成果の6視点で分析するフレームワーク。2026-09-12、スポット相談サービスの診断レポート骨格として正式スキル昇格 |
| `ai-workflow-redesign` | ある業務を人・顧客・AI・システムの誰に任せるべきか再設計する型（負担移転ではなく負担消滅を目指す）。2026-09-12、正式スキル昇格 |
| `ai-onboarding-agent`（検討中） | 会社固有のルール・文化・判断基準をAIに蓄積し新人OJTを支援 |

## 副業収益化（2026-09-12、方向転換により新設）

| スキル | 何をするか |
|---|---|
| `spot-consulting-kit` | AI活用相談・業務AI化診断のスポット相談サービスを運営（商品設計・出品文・問い合わせ対応・診断レポート・収益トラッキング）。noteは「読み物」から「相談への導線」に位置づけ直した |

---

## 未導入・検討中（ネット調査 + ChatGPT knowledge由来：2026-09-11時点、以降の「いつものルーティーン」で随時追記。最終更新2026-10-25）

詳細な出典URLは `backlog.md` のネタ帳セクション参照。★は特に有望と判断したもの。

### 転職活動
- interview-coach-skill／The Claude Code Job Search OS：面接想定問答を「スコアリング」する発想、面接準備〜交渉までの工程拡張の参考
- ResumeSkills：ATS(採用管理システム)通過視点の素材
- LinkedIn MCPサーバー：求人・企業情報の自動収集（⚠️LinkedIn利用規約との兼ね合いを要確認。導入するなら本人アカウントでの手動相当の使い方に留めるのが無難）
- ★Claude Projectで転職活動を一元管理した実例：応募企業一覧管理の運用改善に直接参考
- **job-daily-planner**：Calendar＋Gmail＋応募企業一覧から日次の転職活動プランを生成（既存のGmail/Calendar MCP連携基盤で実装できそう）
- **salary-negotiation**：年収証憑（`lessons-learned.md`参照）＋市場価値から交渉戦略を作る
- [転職活動最適化（求人分析・書類カスタマイズ）実践ガイド](https://library.libecity.com/articles/01KQ15KN1N3210WWDFZVBMY320)（2026-10-22調査）：フォルダ運用で複数社の求人比較→書類カスタマイズを繰り返す手順。`job-hunt-kit`の運用改善に参考
- 転職エージェント向けClaude Code活用セミナー（2026-10-22調査）：求職者本人向けではなくエージェント業界側の動向。AIコンサル方向の市場感として一応メモ
- ★[squerne/open-career-skills](https://trendshift.io/repositories/75916)（2026-10-25調査、MITライセンス）：evidence-miner（git履歴・過去資料から実績を自動抽出しSTARストーリー化）という発想が`job-hunt-kit`に無い工程。実績の裏取りをレビュー担当が行う二段構成も品質チェックの参考

### 個人の業務効率
- ★Executive Assistant Persona／Claude Blattmanの非エンジニア向けツールキット：「コードを書かずにAIに運用を任せる」という自分のスタンスに最も近く、note記事の切り口としても使える
- Email Triage Commander：転職エージェントからの連絡整理への応用
- Google Workspace MCP／Notion MCP：Gmail/Calendar連携の拡張、Notionでのタスク・企画管理の選択肢
- **secure-document-prep**：機密資料のPDFマスキング〜ZIP暗号化送付までの自動化（`lessons-learned.md`の失敗事例が土台）
- ★**invoice-tax-prep**（2026-10-22調査・ドラフト作成済み）：請求書・見積書作成のテンプレ化と、確定申告の要否判定・経費仕分けのたたき台作成。`gig-work-kit`/`spot-consulting-kit`の収益記録と直結する副業の定常作業。詳細は`backlog.md`参照

### note・コンテンツ制作
- 過去記事の文体パターンを抽出してスキル化し再利用する事例（2026-10-22調査）：`note-writer`に「自分の過去記事から文体を学習する」工程を追加するアイデア。おすすめ度4
- note記事の執筆〜入稿・公開までの自動化手順（2026-10-22調査）：Playwrightでの自動投稿に触れるが、note利用規約上の扱いが未確認のため「要注意」。公開前の目視確認は必須という立場は`note-boss`の運用方針と一致

### チームの業務効率
- ★議事録→Issue自動起票（techaide.jp／Qiita事例）：「30分→5分」「週5時間削減」という具体的数字付き。pm-ai-kitの議事録整理をMCP連携で完全自動化する設計図であり、AIコンサルとしてクライアントに提案する際の一枚目スライド候補
- Slack公式MCP導入実践／Async Standupワークフロー：チーム向け提案の具体的な導入手順・ROI訴求ネタ
- claude-skills/project-management：pm-ai-kitとの機能重複比較に使える
- Claude Code部署別・業種別活用事例10選：業種別トークの元ネタ
- **meeting-to-action**：議事録→課題→Action→担当→期限→Issue化（`pm-ai-kit`①の拡張候補）
- ★Notion→GitHub Issue→Claude Code Action自動実装事例（2026-10-22調査）：全員がClaude Codeを直接使うハードルを避ける段階的導入の具体例。AIコンサル提案ネタとして有望
- Claude Code×freee/HubSpot/SlackのAPI連携による部門横断automation事例（2026-10-22調査）：`dx-consulting-framework`の提案ネタに使える具体例
- Claude Code×Slack公式連携（2025-12-08研究プレビュー、2026-10-22調査で確認）：コーディングタスク特化のため今回のユーザー業務とはズレるが、開発チームを持つクライアント向けの提案ネタとして一応メモ
- ★[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)（2026-10-25調査、Anthropic公式・Apache-2.0）：営業・法務・財務・データ分析・マーケティング等11分野以上のプラグイン集。Anthropic公式でライセンス的にも取り込みやすく、財務/法務/データ分析系は`dx-consulting-framework`/`spot-consulting-kit`のクライアント提案ネタとして相性が良い。範囲が広いため次回以降に個別プラグインを絞って調査予定
