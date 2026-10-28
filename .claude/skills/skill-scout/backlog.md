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

## 2026-09-13（gig-work-research 12回目、ローカル`/loop`）

クラウドワークスの契約形式（プロジェクト形式を想定すべき理由）を`gig-work-kit`④に、資料デザインの視線誘導原則（Z/Fの法則）を⑤に反映済み。

## 2026-09-14（gig-work-research 13回目、ローカル`/loop`）

クラウドワークスは本名不要で表示名・ワーカーIDのみで契約完結できること（[[feedback_handle_name_anonymity]]と整合、ただし源泉徴収案件はマイナンバー提出が例外）と、AIスライド作成ツール（Gamma等）の比較情報を`gig-work-kit`④⑤に反映済み。

## 2026-09-14（ChatGPT knowledge inbox：`knowledge/inbox/chatgpt/2026-09-14.md`）

ユーザーの深掘り自己分析（Personality/Operating Profile）とPLAUD NotePin S購入の報告。ユーザー固有情報は`knowledge/user-profile.md`へ反映済み（根本的な価値観、コミュニティとの関わり方、言葉への関心、ASKUL求人、リクルートエージェント面接後アンケートの6項目フォーマット）。後者は汎用テンプレートとして`.claude/skills/job-hunt-kit`⑤にも反映済み。

**新規スキル候補（未着手、ドラフト化はユーザー確認後）**
- **[self-discovery-agent]** SNS・過去文章・履歴書・職務経歴・日記・AI会話履歴等を横断分析し、Self Discovery／Career Translation／Self Operating Systemを出力する自己理解支援ツール。一般的なMBTI型診断との差別化は「質問票だけでなく実際の行動・文章データを使う」点。副業の新規事業候補としてChatGPT側が提案
- **[real-world-to-knowledge]** PLAUD NotePin S（音声入力デバイス）→文字起こし→ChatGPT Knowledge Inbox→レビュー→Claude CodeでSkill/Rule/Template化、という「現実世界の発言を自動でナレッジ化する」パイプライン構想。Highlight機能を「人間が重要と感じた箇所のラベル」として優先処理に使うアイデアつき

**保留（今は実施しない）**：ChatGPT側からuser-profile.mdを`knowledge/user-profile/`配下に`personality.md`/`values.md`/`decision_patterns.md`/`motivation.md`/`risks.md`/`ai_interaction_policy.md`へ分割する提案があったが、現時点では単一ファイルのまま運用を継続する判断（理由：分割による恩恵より、既存の相互参照・[[リンク]]の張り替えコストが今は上回る）。内容量がさらに増えて参照しづらくなったら再検討する。

**運用ルール確認**：健康・家族などセンシティブ情報は必要最小限・目的限定で扱う、という方針をChatGPT側から再確認された。既存の匿名化方針（[[feedback_handle_name_anonymity]]）と一致するため、追加対応は不要と判断。

## 2026-09-15（gig-work-research 15回目、ローカル`/loop`）

ココナラの見積もり相談機能（標準出品に当てはまらない依頼へのカスタム提案手段）を`gig-work-kit`⑤に、資料作成の「情報の粒度」使い分け（経営層＝粒度低め、現場＝粒度高め）をヒアリング項目に反映済み。

## 2026-09-15（gig-work-research 16回目、ローカル`/loop`）

ココナラの複数出品戦略（20個まで、同じ軸内で分ける）を`gig-work-kit`⑦に、クラウドワークスの支払いサイクル（15日締め・月末締めの2パターン、入金まで最大1.5ヶ月）を③に反映済み。

## 2026-09-15（gig-work-research 17回目、ローカル`/loop`）

ココナラのクーポン配布機能（リピート化施策として取引終了時に配布）を`gig-work-kit`⑦に、議事録AIツール（Notta等の話者分離）の使い分けを⑤に反映済み。

## 2026-09-15（gig-work-research 18回目、ローカル`/loop`）

ココナラのサービス画像仕様（1220×1240px、上下115.5px要注意）を`gig-work-kit`⑦に、クラウドワークス提案文の文字数目安（300〜500字）を④に反映済み。4テーマの知見はかなり細部まで出尽くしており、次回以降はより新しい情報が出るまで既存内容の重複が増える可能性が高い。実案件が入り次第、そちらのLearning Loopを優先する判断は継続。

## 2026-09-16（gig-work-research 19回目、ローカル`/loop`）

ココナラの提供日数設定（守れる日数を正直に設定）を`gig-work-kit`④に、インボイス制度が副業に与える影響（免税事業者のリスク・2割特例）を③に反映済み。

## 2026-09-16（gig-work-research 20回目、ローカル`/loop`）

クラウドワークスの本人確認（実質必須、スカウト増加効果）を`gig-work-kit`⑦に、ココナラのトラブル対応フロー（早期終了→運営相談→ブロック、キャンセル申請の手順）を⑥に反映済み。

## 2026-09-16（gig-work-research 21回目、ローカル`/loop`）

グラフの使い分け（相対比較=円・帯、絶対比較=棒、時系列=折れ線）を`gig-work-kit`⑤に、納品物の著作権帰属（下請法・フリーランス保護法の必須記載事項である点含む）を④に反映済み。

## 2026-09-14（gig-work-research 14回目、ローカル`/loop`）

**重要な整理**：「AIっぽさを消す」（文章品質）と「AI利用を隠す」（規約上の透明性）は別問題。クラウドワークスはAI利用の事前開示・非隠蔽を公式に求めている。ココナラはイラスト等でAI生成物の直接販売を原則不可としAI判定システムも導入（テキスト系は同等の厳格さではなさそうだが要注意）。「AIも活用しつつ最終確認は人間が行う」旨を提案文・出品文に明記する方針を`gig-work-kit`⑥に反映済み。非公開スカウト案件の仕組み（実績・評価の積み上げが唯一の近道）も⑦に反映済み。

## 2026-10-22（いつものルーティーン：約5週間ぶりの実行）

前回実行（2026-09-16）から間隔が空いたため、4カテゴリ（転職活動／note・コンテンツ制作／個人の業務効率／チームの業務効率）をWeb調査。このクラウド実行環境には`knowledge/inbox/`（ChatGPT・NotebookLM由来）はPublic repoの許可リスト対象外で同期されておらず中身が存在しないため、Inbox処理は今回スキップ（ローカル環境で貯まっていれば次回ローカル実行時に処理される想定）。

**新規スキル候補（★有望・ドラフト作成済み）**
- **[invoice-tax-prep]** 副業の請求書・見積書作成をテンプレ化し（CLAUDE.md相当の雛形保存→毎月一言で済ませる）、`spot-consulting/収益トラッカー.md`の記録を確定申告の要否判定・経費仕分けのたたき台に変換する下ごしらえキット。税務判断・提出代理はできない前提を明記。
  - きっかけ：Web調査で「Claude Codeに請求書テンプレを保存して翌月から一言で作成」「freee MCP連携での仕訳半自動化」という実践例を複数確認。既存`gig-work-kit`/`spot-consulting-kit`は確定申告基準・インボイス制度を「知識」として持つが、請求書作成や仕訳たたき台という「作業」はどちらにも無く、毎月発生する作業である点でSkill化判断ルールに合致すると判断
  - ステータス：ドラフト作成済み（→ `skill-scout/drafts/invoice-tax-prep`）

**ネタ帳（今回の調査分）**

転職活動
- [転職活動最適化（求人分析・書類カスタマイズ）実践ガイド](https://library.libecity.com/articles/01KQ15KN1N3210WWDFZVBMY320)（libecity、2026-04-26）：採用目線を持つ筆者が、求人分析→複数社比較→書類カスタマイズまでをフォルダ運用で繰り返す手順。`job-hunt-kit`の運用改善に参考
- [転職エージェント向けClaude Code業務効率化セミナー](https://genai-ai.co.jp/ai-kanri/course/tenshoku-cc-sem/)：求人票・推薦理由書・書類添削の自動化を扱う。求職者本人向けではなくエージェント業界側の動向だが、AIコンサル方向の市場感として一応メモ

個人の業務効率
- 請求書・見積書・確定申告の下ごしらえ自動化（複数ブログ事例。[sejuku](https://generative-ai.sejuku.net/?p=310960)、[saiteki-ai](https://saiteki-ai.com/?p=5387)、[genai-ai.co.jp](https://genai-ai.co.jp/ai-kanri/blog/cc-kakutei-koritsu/)等）：請求書テンプレ保存、freee/マネーフォワードAPI連携での仕訳半自動化、税務判断は人（税理士）が最終確認という整理。→上記`invoice-tax-prep`としてドラフト化済み

note・コンテンツ制作
- 過去記事の文体パターンを抽出してスキルとして保存・再利用する事例（libecity）：`note-writer`に「自分の過去記事から文体を学習させる」工程を追加するアイデアとして有望。おすすめ度4
- note記事の執筆→校正→入稿→公開までの自動化手順（[sejuku](https://generative-ai.sejuku.net/?p=312719)）：Playwrightでの自動投稿に触れているが、noteの利用規約上自動投稿が許容されるか未確認のため★ではなく「要注意」扱い。公開前の目視確認は必須という立場は`note-boss`の運用方針と一致

チームの業務効率
- [NotionタスクをGitHub Issue経由でClaude Code Actionに自動実装させる事例](https://zenn.dev/mgdx_blog/articles/d231961da48a53)：全員がClaude Codeを直接使うハードルを避けてGitHub Actions経由にした設計。AIコンサルとしてクライアントに提案する際の「段階的導入」の具体例として有望 ★
- [Claude Code×freee/HubSpot/SlackのAPI連携による部門横断automation事例](https://start-link.jp/hubspot-ai/ai/claude-code-practice/claude-code-api-business-integration)：受注データ入力→請求書作成→Slack通知、という業務ロジックをまとめて書ける点がZapier等との違いとして紹介。`dx-consulting-framework`の提案ネタに使える
- [Claude CodeとSlackの公式連携](https://claude.com/ja-jp/blog/claude-code-and-slack)（2025-12-08、研究プレビュー）：Slackでの@メンションからバグ修正・リファクタ等のコーディングタスクをClaude Codeに直接依頼できる機能。今回のユーザーの非エンジニア業務とはズレるため優先度は低いが、クライアント先が開発チームを持つ場合の提案ネタとして一応メモ

ステータス：全て「ネタ帳」段階。`invoice-tax-prep`のみ有望と判断しドラフト化。他は`categories.md`の「未導入・検討中」にも反映済み。

**Step4レビュー**：`categories.md`の導入済みスキル一覧を確認。`dx-consulting-framework`・`ai-workflow-redesign`は2026-09-12時点で正式スキル昇格済みだが`スキル活用一覧.xlsx`のステータスが「検討中」のまま古くなっていたため「導入済み」に更新。`spot-consulting-kit`・`gig-work-kit`も実運用中の正式スキルだがxlsxに行が無かったため追加。明らかな重複・放置スキルは見当たらず「要整理」対象は無し（なお、このクラウド実行環境では`02_面接対策`等の実作業フォルダは非公開のため同期されておらず、実際の使用頻度までは確認できていない）。

## 2026-10-23（いつものルーティーン：前日実行の翌日）

前回（2026-10-22）から1日しか経っておらず、`knowledge/inbox/`もこのクラウド実行環境には同期されていないため未処理。4カテゴリをWeb調査したが、ヒットの大半は前回調査済みの記事と重複（libecity・sejuku・genai-ai.co.jp等）。新たに★候補と判断できるものは無く、ドラフト作成は見送り。

**ネタ帳（今回の調査分・補足のみ）**

転職活動
- [クラシル株式会社の採用業務効率化セミナー（Offers）](https://voix.jp/?p=86500)：求職者本人向けではなく採用側（企業）の事例。ペルソナ設計→スカウト文生成を4段階パイプライン化し作業時間を1/4に短縮したと発表。転職エージェント向け事例と同様、AIコンサル方向の市場感メモとして追加（★ではない）

個人の業務効率
- [Claude Code×MCP 個人業務自動化ガイド：メール/カレンダー/Notion連携](https://aurant-technologies.com/?p=1373)：`job-daily-planner`（ドラフト済み）や既出の`Email Triage Commander`/Google Workspace MCPと内容が重複。新規候補としては追加せず、既存ドラフトの実装参考リンクとして記録のみ

ステータス：新規★候補なし。`categories.md`「未導入・検討中」への追記は見送り（既出事例の重複が中心で、独立した反映価値が薄いため）。xlsxへの新規行追加もなし。

**Step4レビュー**：`categories.md`の導入済みスキル一覧を再確認。前回（2026-10-22）からの変更点なし。明らかな重複・放置スキルは見当たらず「要整理」対象は無し。

## 2026-10-24（いつものルーティーン）

前回（2026-10-23）から1日しか経っておらず、`knowledge/inbox/`もこのクラウド実行環境には同期されていないため未処理（ローカル環境で貯まっていれば次回ローカル実行時に処理される想定）。4カテゴリをWeb調査。

**ネタ帳（今回の調査分）**

転職活動
- [2026年版:Claudeを24時間365日稼働の転職活動の武器にする方法(金融+AI業界編)](https://youmind.com/ja-JP/landing/x-viral-articles/claude-job-search-finance-ai)：履歴書最適化・模擬面接・給与交渉をClaudeで行う手順。既存の`salary-negotiation`候補（優先度B・未着手）を補強する参考事例として追記
- [非エンジニア経営者が「Claude Code」でやった13のこと](https://library.libecity.com/articles/01KMCNP73W8G9QZC4CFA6KB3GS)：SES業務の要員登録・案件登録などの自動化事例。転職活動というより個人の業務効率／AIコンサル方向の非エンジニア活用例としてメモ

note・コンテンツ制作
- [自分の文章の書き方をスキル化して記事を書いた体験談](https://library.libecity.com/articles/01KQP2K62H8S9Y1K7Y3Z0B1RBA)：2026-10-22に記録済みの「過去記事の文体パターンを抽出してスキル化」と同じ着想の別事例。`note-writer`拡張アイデアの裏付けとして追記のみ（新規候補としては追加しない）

個人の業務効率／チームの業務効率
- [Claude Code チーム導入5ステップ（uravation.com media一覧）](https://uravation.com/media-category/claude-code/)、[Claude Code活用セミナー（digirise.ai、560社支援実績）](https://digirise.ai/en/seminar/20260605-2/)：議事録・営業日報・アンケート集計・経費精算等の自動化事例。本文の数値（月50時間削減等）は未検証のため鵜呑み厳禁。`pm-ai-kit`の拡張ネタ（経費精算・営業日報）として一応メモ

ステータス：新規★候補なし。既存候補（`salary-negotiation`・`note-writer`拡張アイデア）の補強参考のみで、独立した新規候補としての反映価値は薄いため`categories.md`「未導入・検討中」への追記・`スキル活用一覧.xlsx`への新規行追加は見送り。

**Step4レビュー**：`categories.md`の導入済みスキル一覧を再確認。前回（2026-10-23）からの変更点なし。明らかな重複・放置スキルは見当たらず「要整理」対象は無し。

## 2026-10-25（いつものルーティーン）

実行前に、ローカルで実行された直近2回（2026-10-23・10-24）のコミットがこのクラウド環境のローカルrefでは一時的にdetached HEAD扱いで古い`main`参照しか見えていなかったことに気づいた。`git fetch`で確認した結果、実際には両コミットとも既に`origin/main`にpush済みで実害はなし（ローカルrefが単に古いキャッシュだった）。`main`ブランチをfast-forwardして整合させただけで、追加pushは発生していない。

`knowledge/inbox/`（ChatGPT・NotebookLM由来）はこのクラウド実行環境には同期されておらず中身が無いため、Inbox処理は今回も未実施。4カテゴリをWeb調査。

**新規候補（ネタ帳に追加。いずれも即ドラフト化は見送り）**

転職活動
- [squerne/open-career-skills](https://trendshift.io/repositories/75916)（GitHub、MITライセンス）：求人探索・模擬面接・カバーレター作成等7スキルの中に **evidence-miner**（git履歴や過去の作業ドキュメントから実績を自動抽出してSTARストーリー化する）という発想がある。既存`job-hunt-kit`はゼロから想定問答を作る前提だが、「過去の案件・作業ログから実績の種を自動で掘り出す」工程は無い。本プロジェクトの`gig-work-kit`納品物や`spot-consulting`の相談記録を素材にできそうで、既存スキルと微妙に粒度が違う作業として有望。もう1点、/applyパイプラインで「ドラフト担当が主張した実績をレビュー担当が裏取りする」という事実捏造防止の二段構成も、`job-hunt-kit`の品質チェックに参考になる
  - 判断：すぐにはドラフト化せず、まずは次回以降`job-hunt-kit`への追記（実績ソースから想定問答の種を拾う工程、捏造防止チェック）として検討する候補に留める

個人の業務効率／チームの業務効率
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)（Anthropic公式、2026年1月公開、**Apache-2.0**）：営業・カスタマーサポート・プロダクトマネジメント・マーケティング・法務・財務・データ分析・エンタープライズ検索・バイオ研究・プラグイン管理など11分野以上のプラグイン集（Skill＋スラッシュコマンド＋MCPコネクタ構成）。`skill-creator`/`mcp-builder`等と同じAnthropic公式路線で、ライセンス的にも取り込みやすい。特に財務・法務・データ分析系はAIコンサル方向（`dx-consulting-framework`/`spot-consulting-kit`）のクライアント提案ネタとして相性が良さそう
  - 判断：11分野を一度に検討するには範囲が広すぎるため即ドラフト化は見送り。`categories.md`「未導入・検討中」に★候補として追記し、次回以降に個別プラグイン（財務/データ分析あたりから）を絞って調査する

ステータス：新規★候補2件を`categories.md`・`スキル活用一覧.xlsx`に反映。ドラフト作成は見送り（範囲の絞り込みが必要なため）。

**Step4レビュー**：`categories.md`の導入済みスキル一覧を再確認。前回（2026-10-24）からの変更点なし。明らかな重複・放置スキルは見当たらず「要整理」対象は無し。

## 2026-10-26（いつものルーティーン）

`knowledge/inbox/`（ChatGPT・NotebookLM由来）はこのクラウド実行環境には同期されておらず中身が無いため、Inbox処理は今回も未実施（ローカル環境で貯まっていれば次回ローカル実行時に処理される想定）。4カテゴリをWeb調査。

**ネタ帳（今回の調査分）**

転職活動
- 今回の検索では転職活動専用のClaude Codeスキル・事例に新規ヒットなし。上位結果は「2026年版おすすめClaude Codeスキル一覧」系のまとめ記事（Skill Creator・Git Commit Writer等、開発者向け汎用スキルが中心）で、転職活動に直接使える新しい型は見当たらなかった

note・コンテンツ制作
- note投稿までの一連の流れ（企画→Codexで文章修正→タイトル選定→見出し画像→投稿準備）、「1記事5日→1時間に短縮・アフィリエイト初収益149円」体験談、「Claude Codeに役割分担させて1週間で約20記事投稿」など、libecity等の個人体験談が複数ヒット。いずれも既存の`note-boss`チーム構成・`note-writer`文体学習アイデア（2026-10-22/24に記録済み）と同系統で、新規の型としての独立反映価値は薄いと判断
- [claudeskills.info 執筆スキルランキング](https://claudeskills.info/ja/best/writing-skills/)：edit-article系スキル（記事の編集・推敲用）がインストール数上位。第三者の独立検証はなく、`note-editor`との機能重複比較の参考メモ程度

個人の業務効率
- 検索結果の多くが研修会社・資料請求サイトの販促ページ（「業務時間60%削減」等、根拠不明の数字を掲げるもの）で、具体的な新規の型は確認できず。MCP連携の概要紹介（GitHub/Slack/GA4等）は既存知見の範囲内

チームの業務効率
- 同様に、セミナー・解説記事・自社宣伝記事が中心で、実名・数値付きの新規導入事例は見つからず。対象業務（Excel操作・ファイル処理・市場調査・資料作成の自動化）も既存の`pm-ai-kit`/`dx-consulting-framework`の範囲内
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)のFinanceプラグインについて追加調査：第三者ガイドで「variance analysis workflow」「GAAPスタンダード準拠」と言及されているのを確認したが、GAAPは米国基準で日本の会計実務とは異なり、リポジトリ側のskills/配下の具体的な内容（ファイル名・プロンプト構成）までは今回確認できなかった。前回（2026-10-25）の方針通り「次回以降に個別プラグインを絞って調査」を継続するが、Finance単体を今すぐ★候補に上げるには情報不足と判断し見送り

ステータス：新規★候補なし。既出テーマの補強メモのみで、`categories.md`「未導入・検討中」への追記・`スキル活用一覧.xlsx`への新規行追加は見送り。

**Step4レビュー**：`categories.md`の導入済みスキル一覧を再確認。前回（2026-10-25）からの変更点なし。明らかな重複・放置スキルは見当たらず「要整理」対象は無し。

## 2026-10-27（いつものルーティーン）

`knowledge/inbox/`（ChatGPT・NotebookLM由来）はこのクラウド実行環境には同期されておらず中身が無いため、Inbox処理は今回も未実施（ローカル環境で貯まっていれば次回ローカル実行時に処理される想定）。4カテゴリをWeb調査。

**ネタ帳（今回の調査分・補足のみ）**

個人の業務効率／チームの業務効率
- [Aurant Technologies「Claude Codeサービス」](https://aurant-technologies.com/service/claude-code/)：会計ソフトへの記帳など本番データを書き換える処理でAIに直接権限を渡さず、最小権限・承認フロー・操作ログの統制レイヤーを挟む構成を明示。既出の「freee/HubSpot/Slack連携事例」（2026-10-22記録）と同じ発信元だが、今回は統制設計（ガバナンス）の観点が新規。`dx-consulting-framework`のクライアント提案時に「AI自動化＋承認フロー」というセットで説明する際の参考として追記のみ（新規候補としては追加しない）

転職活動／note・コンテンツ制作
- 今回の検索では新規ヒットなし。上位結果は`job-hunt-kit`運用改善の参考記事（2026-10-22既出のlibecity記事）やnote自動化体験談（2026-10-22/24/26既出のsejuku・libecity記事）の再ヒットのみで、重複が中心

ステータス：新規★候補なし。補強メモのみのため`categories.md`「未導入・検討中」への追記・`スキル活用一覧.xlsx`への新規行追加は見送り。

**Step4レビュー**：`.claude/skills/`配下の実フォルダ一覧（19スキル）と`categories.md`の導入済み一覧を突き合わせ確認。両者は完全に一致し、明らかな重複・放置スキルは見当たらず「要整理」対象は無し。

## 2026-10-28（いつものルーティーン）

`knowledge/inbox/`（ChatGPT・NotebookLM由来）はこのクラウド実行環境には同期されておらず中身が無いため、Inbox処理は今回も未実施（ローカル環境で貯まっていれば次回ローカル実行時に処理される想定）。4カテゴリをWeb調査したが、大半は既出記事（libecity・sejuku・digirise.ai・uravation.com等）の再ヒットで新規性は薄い。

**ネタ帳（今回の調査分）**

個人の業務効率／チームの業務効率（AIコンサル方向）
- [anthropics/financial-services](https://github.com/anthropics/financial-services)（Anthropic公式、Apache-2.0）：金融モデリング・エクイティリサーチ・投資銀行・プライベートエクイティ・資産運用向けのプラグイン集（Agent plugins・Vertical plugins・Partner plugins構成、LSEG/S&P Global等のデータ連携）。2026-10-25/26に追記した`anthropics/knowledge-work-plugins`のFinanceプラグインとは別リポジトリ
  - 判断：内容は投資銀行・資産運用等のウォール街的専門領域に特化しており、当プロジェクトが想定するSME（中小企業）向けDXコンサル（`dx-consulting-framework`/`spot-consulting-kit`）とは対象レイヤーがズレる。★候補にはせずメモのみ。クライアントに金融機関が含まれる場合の将来ネタとして記録

転職活動／note・コンテンツ制作
- 今回の検索では新規ヒットなし。上位結果はこれまでに記録済みの記事（求人分析・書類カスタマイズガイド、note自動化体験談等）の再ヒットのみ

ステータス：新規★候補なし。`anthropics/financial-services`は対象ズレのため`categories.md`「未導入・検討中」への追記・`スキル活用一覧.xlsx`への新規行追加は見送り。

**Step4レビュー**：`.claude/skills/`配下の実フォルダ一覧（19スキル）と`categories.md`の導入済み一覧を再確認。前回（2026-10-27）からの変更点なし。明らかな重複・放置スキルは見当たらず「要整理」対象は無し。
