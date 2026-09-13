# スキル化バックログ

`skill-scout` スキルが見つけた「汎用スキル化できそうな作業」を貯める場所。フォーマットは `skill-scout/SKILL.md` 参照。

---

## 2026-09-11（クロスセッション由来：別マシンの「フリーランスから正社員への転職検討」セッションから共有）

同一ユーザーが別マシン上でも同名「AI作業場所」プロジェクトを運用しており、そちらで育っていた型を共有してもらった。

- **[company-scoring-sheet]** 応募企業を「本人適性軸11項目」「客観軸6項目」の2枚のシートでスコアリングし、比較・優先順位づけする型
  - きっかけ：ピアセッションからの共有（企業別_AI独自総合評価／企業別_一般評価ランキング）
  - ステータス：ドラフト作成済み（→ `skill-scout/drafts/company-scoring-sheet`）
- **[company-analysis-full]** 面接確定企業ごとに、基礎情報・DXニュース・自分との接点・推し話・ボトルネック仮説までまとめるフル版分析シート。`job-hunt-kit`②の発展版
  - きっかけ：ピアセッションからの共有（企業分析_◯◯シート）
  - DXボトルネックの7パターン（①PJが進まない／②成果が出ない／③定着しない／④既存システム・データが足かせ／⑤人材・体制不足／⑥費用対効果不明／⑦PoCから本番に進めない）も反映済み。各社への当てはめは`knowledge/user-profile.md`に記録
  - ステータス：ドラフト作成済み・内容確定（→ `skill-scout/drafts/company-analysis-full`）

## 2026-09-11
- **[転職活動フォーマット]** 面接想定問答（自己紹介・転職理由・志望動機・自己PR・実績エピソード・逆質問）を「核」として作り、企業ごとに差分カスタマイズする型。エージェント・企業への返信文面、応募企業一覧の更新も含む。
  - きっかけ：`02_面接対策` フォルダの直近10日分（9/1〜9/11、6社分の面接対策資料）を確認して抽出
  - ステータス：スキル化済み（→ `job-hunt-kit`）
- **[汎用リサーチ]** 企業研究・業界トレンド調査・情報整理を「目的設定→収集→整理→ファクトチェック」の型でテンプレ化
  - きっかけ：転職活動の企業研究と、note記事のジャンル調査（`note-research`）が同じ骨格を持っていることに気づいた
  - ステータス：スキル化済み（→ `research-kit`）
- **[スキル化の仕組みそのもの]** 日々の作業からスキル化候補を見つけて貯める仕組み
  - きっかけ：ユーザーからの依頼「スキル化考案チームを作ってほしい」
  - ステータス：スキル化済み（→ `skill-scout`。このファイル自体がその成果物）

## ネタ帳（自分の作業とは無関係でも着想として貯める欄）

### 2026-09-11 調査担当エージェントによる収集分（3カテゴリ）

**転職活動**
- [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)：ATS対策・面接準備のスキル集
- [interview-coach-skill](https://github.com/noamseg/interview-coach-skill)：求人票分析→模擬面接→交渉まで、想定問答のスコアリング発想が参考
- [The Claude Code Job Search OS](https://www.news.aakashg.com/p/job-search-os)：18スキルで転職活動をエンドツーエンド自動化
- [linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)：求人・企業情報の自動収集（⚠️LinkedIn利用規約要確認）
- [Claude Projectで転職活動を一元管理した実例](https://ai-tenshoku-lab.com/articles/claude-project-jobhunt)：応募企業一覧管理の運用改善に直接参考 ★
- [Claude Codeカスタムコマンドで応募書類自動生成（Qiita）](https://qiita.com/claude_iruka/items/f5c721f2acf2241e6d11)

**個人の業務効率**
- [Executive Assistant Persona](https://mcpmarket.com/tools/skills/executive-assistant-persona)：Google Workspace連携で朝レポート・受信箱仕分け自動化 ★
- [Claude Blattman Executive Assistant Toolkit](https://claudeblattman.com/toolkit/executive-assistant/)：非エンジニア向けにAI運用を組む手順。発信スタイルの参考にも ★
- [Email Triage Commander](https://mcpmarket.com/tools/skills/email-triage-commander)：受信メールの自動分類・要約
- [Google Workspace MCP Server](https://www.mindstudio.ai/blog/google-workspace-mcp-server-claude-code-codex)：Gmail/Calendar連携の拡張
- [Notion MCP連携](https://composio.dev/toolkits/notion/framework/claude-code)：タスク・DB管理

**チームの業務効率**
- [議事録→Issue自動起票（techaide.jp）](https://techaide.jp/blog/claude-code-meeting-action-automation/)：「30分→5分」の具体的短縮事例 ★
- [Claude Code×Notion MCPで議事録自動化（Qiita）](https://qiita.com/hikariclaude01/items/ca5abb0df6c4b859f335)：週5時間削減
- [Slack公式MCPの導入と実践（Zenn）](https://zenn.dev/genda_jp/articles/2b073c49e31d9e)
- [Top 15 Claude Tag Use Cases for Teams in Slack](https://explainx.ai/blog/top-15-claude-tag-use-cases-slack-team-ai-2026)：Async Standupで月180時間削減という事例（数字は未検証、鵜呑み厳禁）
- [claude-skills/project-management](https://github.com/alirezarezvani/claude-skills/tree/main/project-management)：pm-ai-kitとの機能重複比較用
- [Claude Code部署別・業種別活用事例10選](https://uravation.com/media/claude-code-use-cases-10-by-department-industry-2026/)：業種別トークの元ネタ

ステータス：全て「ネタ帳」段階（未導入）。★3つが優先検討候補。実際の導入・スキル化はユーザー確認の上で進める。

## 2026-09-11（追記）
- **[外部公式スキルの導入]** Anthropic公式`anthropics/skills`から `skill-creator` / `mcp-builder` / `web-artifacts-builder` / `webapp-testing` の4つを導入。
  - きっかけ：ユーザーが比較表を持ち込み、導入を検討
  - 判断：Hugging Face公式`huggingface/skills`の3つ(model-trainer/datasets/evaluation)はHF_TOKEN必須＋クラウドGPU課金の可能性があり、今のnote/転職活動という方向性とも遠いため見送り
  - ステータス：導入済み（pluginではなく該当フォルダのみを`.claude/skills/`に直接配置。plugin経由だと`anthropics/skills`内の無関係な15スキルも同梱されるため）

## 2026-09-11（ChatGPT knowledge inbox由来：`knowledge/inbox/chatgpt/2026-09-11.md`）

既存スキルへの統合可否を判断した上で、統合できなかった／独立させる価値がある候補のみ残す。

**既存スキルに統合済み（新規スキル化は不要）**
- job-interview-prep → `job-hunt-kit`①②に統合（14項目構成・志望動機生成ルール・面接回答の原則を追記）
- job-company-research → `research-kit`①に統合（IR資料・企業との接点の観点を追記）
- job-mail-triage（軽量版：優先度判定ルールのみ）→ `job-hunt-kit`④に統合

**新規スキル候補（優先度A：転職活動の自動化を一歩進める／AIコンサル方向）**
- **job-daily-planner**：Google Calendar＋Gmail＋応募企業一覧から「今日の面接・準備・提出物・返信・企業研究・面接後フォロー」を生成し、過密日は必須/できれば/後回しに3分類する。Gmail/Calendar MCP連携（既存のjob_hunt_tracker基盤）を使えば実装できそう。ステータス：ドラフト作成済み（→ `skill-scout/drafts/job-daily-planner`）
- **dx-consulting-framework**：DX案件を「業務・人・組織・技術・定着・成果」の6視点で分析するフレームワーク。AIコンサルタント就業という目標に直結。ステータス：ドラフト作成済み（→ `skill-scout/drafts/dx-consulting-framework`）
- **ai-workflow-redesign**：ある業務を「人・顧客・AI・システム」の誰に任せるべきか再設計する型（負担移転ではなく負担消滅を目指す思想つき）。note記事のネタにもなる。ステータス：ドラフト作成済み（→ `skill-scout/drafts/ai-workflow-redesign`）

**新規スキル候補（優先度B）**
- **salary-negotiation**：年収証憑（`lessons-learned.md`の年収証明知見を活用）＋市場価値＋求人レンジから年収交渉戦略を作る。ステータス：未着手
- **secure-document-prep**：PDFマスキング→再レンダリング目視確認→ZIP暗号化→解凍確認→メール文作成（`lessons-learned.md`のPDFマスキング失敗事例が土台）。ステータス：未着手
- **meeting-to-action**：議事録→課題→Action→担当→期限→Issue化。`pm-ai-kit`①議事録整理の拡張として統合するか、独立スキルにするか要検討。ステータス：未着手
- **ai-onboarding-agent**：会社固有のルール・文化・判断基準をAIに蓄積し新人OJTを支援。将来AIコンサルとしてクライアント先に提案するネタ。ステータス：未着手

次回の「いつものルーティーン」Step3で、優先度Aから順にドラフト（`drafts/`配下）を作成予定。

## 2026-09-12（副業収益化の方向転換）

ユーザーから「note記事課金・アフィリエイトでは収益化に程遠い。PM含め爆速で売上を出すチームを組んでほしい。コンサルもできるか」という相談。診断の結果、300円記事だけで月5万円には167本販売が必要で非現実的と判断。方向転換を提案し合意：**noteを「読み物」から「スポット相談(コンサル)商品への導線」に位置づけ直す**。

- **[dx-consulting-framework]** ドラフトから正式スキルへ昇格（→ `.claude/skills/dx-consulting-framework`）。スポット相談の診断レポート作成に使う
- **[ai-workflow-redesign]** ドラフトから正式スキルへ昇格（→ `.claude/skills/ai-workflow-redesign`）。診断後の改善提案パートに使う
- **[spot-consulting-kit]** 新規スキルとして作成（→ `.claude/skills/spot-consulting-kit`）。商品設計・出品文・問い合わせ対応・診断レポート・収益トラッキングを一気通貫で扱う。初期商品：ミニ相談3,000円、AI活用診断12,000円
- 制約：ハンドルネーム運用・経歴伏せ気味を維持（転職活動中のため）。この方針は`spot-consulting-kit`のSKILL.md冒頭に明記済み
- ステータス：スキル化済み・実運用開始（`spot-consulting/`フォルダに出品文2本・収益トラッカーを作成済み。問い合わせ実績はまだ0件）

## 2026-09-12（追記：クラウドソーシング受託への展開）

ユーザーから「ココナラ・クラウドワークスで自動化完結できる案件を見つけて実行・納品したい、そのノウハウをスキル化して売りたい」という相談。ログイン・応募・メッセージ送信・報酬受取はAIが代行できない（対外的コミットメントのため）ことを明示した上で、「適性判定→提案文作成→納品物作成」を支援するスキルを作成。

- **[gig-work-kit]** 新規スキル（→ `.claude/skills/gig-work-kit`）。既存の`pm-ai-kit`/`research-kit`/`job-hunt-kit`をそのまま納品物作成のエンジンとして再利用する設計
- 収益記録は`spot-consulting/収益トラッカー.md`の「経路」列を共用（新しいトラッカーは作らず一元管理）
- 注意点：note(スポット相談導線)・アフィリエイト・転職活動と並行する4本目の施策になるため、まず1案件を試験受注して時間対効果を検証してから広げる方針をスキル内に明記
- 2026-09-12、3時間おきの自律リサーチ（ローカル`/loop`、ジョブID`8f44f2b9`、`knowledge/gig-work-research.md`に蓄積）を開始。1回目の知見を`gig-work-kit`SKILL.mdに反映済み（出品メニューの絞り方・応募数の目安・AIっぽさ対策チェックリスト）
- 2回目（同日）：クラウドワークスの危険案件の見分け方（外部ツール誘導・極端な低単価・個人情報要求・評価0〜5件の依頼者等）を`gig-work-kit`①案件の適性判定の前段に「危険信号チェック」として追加反映済み
- 3回目（同日）：パワポ提案書の型（背景・課題→解決策→効果→実行計画、結論先出し、配色4色以内）と、AIっぽさの原因を語尾/接続詞/主語/抽象度/構成の5要素に整理した具体的リライト技術を`gig-work-kit`に反映済み

## 2026-09-12（ChatGPT側「副業自動化PM」フレームワークとの統合）

`knowledge/inbox/chatgpt/2026-09-12.md`（ChatGPTが並行して検討していた副業自動化のPMフレームワーク）を処理。

**`gig-work-kit`へ統合済み**：Job Scoutスコアリング（Revenue/Automation/Reuse/Proof/Fit/Expansion 6軸30点＋Competition Penalty＋Hard Gate）、共通業務Workflow（DISCOVER→...→PACKAGE）、対象外の明確化（コーディング講師業除外、低期待値案件の除外条件）、共通QAルール、Learning Loop（correction→reason→reusable_rule→skill_update）、経済性評価式（Expected Profit / Skill Investment Value）

**既存スキルでカバー済み（新規スキル化は不要）**：`Career_Application_Agent`構想→[[job-hunt-kit]]で概ねカバー（転職支援を副業として売るサービス化は将来検討）、`Meeting_Followup_Agent`構想→[[pm-ai-kit]]＋`gig-work-kit`⑤に統合、`Research_to_Report`構想→[[research-kit]]でカバー

**新規スキル候補（未着手、優先度検討）**
- **[Web_Writer_Agent]** IT/DX/AI/キャリア等の専門テーマで、外部クライアント向けに継続的な有料記事執筆を代行するサービス。既存`note-writer`は自分のnote用なので別物。Pipeline案：Brief Parser→Search Intent Analyst→Researcher→Outline Writer→Draft Writer→Fact Checker→Editor→Requirement Checker→Human Gate→Learn。目標：1記事5,000円以上、週2〜3本の継続案件化。ChatGPT側は優先度A評価
- **[SNS_Weekly_Operator]** 他社・クライアントのSNS運用（Instagram/X/Threads等）を「市場調査→企画→制作→QA→分析→改善」の一連ワークフローとして代行するサービス。既存`note-promoter`は自分のnote宣伝用なので別物。ChatGPT側は優先度B評価（今回新たに有望と判断された）

**価格の食い違い→解決済み（2026-09-12）**：`spot-consulting/出品文_議事録整理代行.md`の2,000円〜はユーザー確定で継続。ChatGPT側のHard Gate（単発粗利3,000円以上）に対する意図的な戦略的例外（実績ゼロ期のレビュー集め優先）として`gig-work-kit`②に明記済み
- 4回目（同日、ローカル`/loop`）：クラウドワークス提案文の「冒頭の課題復唱＋4パート構成＋個別カスタマイズ」型と、資料作成・議事録代行の必須ヒアリング5項目（基本情報/課題/予算・納期/ゴール/意思決定者）を`gig-work-kit`④⑤に反映済み
- 5回目（同日、ローカル`/loop`）：ココナラのタイトル最適化式（検索キーワード＋ベネフィット）と、クラウドワークスのリピート化条件（納期厳守・早め連絡・返信12〜24時間以内）を`gig-work-kit`⑦に反映済み
- 6回目（2026-09-13、ローカル`/loop`）：クラウドワークスの単価交渉術（時給700〜900円で信頼構築を優先→実績後に交渉）と、AI検出の技術的仕組み（Perplexity/Burstiness）を`gig-work-kit`④⑥に反映済み

## 2026-09-13（NotebookLM knowledge inbox：外部Claude Codeノウハウ資料の取り込み）

ユーザーが複数の外部資料（有料勉強会特典・会員限定コース等）のClaude Code活用ノウハウを、NotebookLM経由で理解した上でスキル化したいと相談。ただし**「内部的知見を貯めるだけにとどめてください」という方針決定（2026-09-13）**により、この一連の取り込みは`.claude/skills/`（公開リポジトリ）へのドラフト化・categories.md/xlsx反映は行わず、`knowledge/inbox/notebooklm/`配下（非公開）への要約蓄積のみに留める。

- 詳細は `knowledge/inbox/notebooklm/2026-09-13.md`（Claude in Chrome拡張の活用）、`2026-09-13_2.md`（Claude Code×Codex連携でのスライド自動生成）を参照
- 既存ドラフト`skill-scout/drafts/chrome-browser-control`は上記方針決定に伴い削除済み（内容は上記inboxファイルに残る）
- 今後同種の資料が来ても、同じ方針（`knowledge/inbox/notebooklm/`への要約保存のみ）で処理する。ユーザーが明示的に「スキル化して」と言った場合のみ、この節を参照してdraft化を検討する

## 2026-09-13（ChatGPT・A-3班の役割分担確定）

ChatGPT提案「案件入口駅＝ChatGPT（探索・一次評価）／制作・納品駅＝A-3班＝gig-work-kit（技術評価・制作・学習）、実績を相互フィードバック」で合意。`gig-work-kit`のSKILL.mdに正式反映済み。ChatGPT→A-3の経路は既存の`knowledge/inbox/chatgpt/`、A-3→ChatGPTの新しい経路として`knowledge/a3-execution-learnings.md`を新設（Public repoで追跡、まだ実案件の記載なし）。

## 2026-09-13（gig-work-research 7回目、ローカル`/loop`）

ココナラの高評価の集め方（納品時に一言評価依頼を添える、初期は匿名評価も許容）と、クラウドワークスの継続契約化の正しい手順（新規契約の結び直し／マイルストーン払い。メッセージのみでの継続はガイドライン違反リスク）を`gig-work-kit`⑦に反映済み。

## 2026-09-13（gig-work-research 8回目、ローカル`/loop`）

副業の確定申告基準（副業所得20万円超で必須、住民税は別途申告要）を`gig-work-kit`③に、ココナラのトークルーム利用ルール（取引目的外利用・外部公開禁止、送信取り消し不可）を⑥に反映済み。

## 2026-09-13（ChatGPT → Claude Codeの情報経路を3本化、outbox新設）

ユーザーから「ChatGPT側に、Gitで共有できていない情報を共有したい」という依頼を受け、`knowledge/outbox/chatgpt/2026-09-13.md`（初回・全量サマリー版）を作成。ChatGPT側から経路設計への承認と、運用改善の詳細フィードバックが返ってきた（`knowledge/inbox/chatgpt/2026-09-13_2.md`）。

- **経路を3本に整理**：`inbox/chatgpt/`（ChatGPT→Claude Code、方針・市場知見）／`outbox/chatgpt/`（Claude Code→ChatGPT、差分型6項目フォーマット、22-23時想定）／`a3-execution-learnings.md`（A-3→ChatGPT、Public公開の実行知見）。詳細は`skill-scout/SKILL.md`「ChatGPTとの3つの情報経路」参照
- **gig-work-kitへ反映**：Exception Rate（例外率）を優先判断軸に追加（③）、Creation より Transformation優先の具体例リスト（①）、Common Core構想（Input Contract→...→Abstracted Learning、実案件が増えたら移行する将来設計として明記）
- **user-profile.mdへ反映**：AIチーム役割分担を5層（ChatGPT/Claude Code/Codex/A-3 subagents/NotebookLM）に更新
- ステータス：運用ルール確定・反映済み

## 2026-09-13（gig-work-research 9回目、ローカル`/loop`）

ココナラの本人確認要件（出品は不要だが振込申請には必須）を`gig-work-kit`⑦に、議事録代行のNDA基礎（対象範囲・期間の確認、CONFIDENTIAL明記の重要性）を⑥に反映済み。4テーマの基本知見は一通り出尽くした感触。実案件が入り次第、リサーチより`knowledge/a3-execution-learnings.md`への実績記録を優先する方針（前回提案通り）。

## 2026-09-13（gig-work-research 10回目、ローカル`/loop`）

実績ゼロ期のポートフォリオ作り方（架空プロジェクト可・自作素材のみ）と、修正回数上限・検収条件を契約前に明記する重要性を`gig-work-kit`④に反映済み。

## 2026-09-13（gig-work-research 11回目、ローカル`/loop`）

プラットフォーム3社の使い分け（案件型＝クラウドワークス/ランサーズ、出品型＝ココナラ）と、クラウドワークスの「プロクラウドワーカー」認定制度を`gig-work-kit`⑦に反映済み。
