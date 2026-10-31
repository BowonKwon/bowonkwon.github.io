"""Build the hub site (index.html + en/index.html) from the project list below.

  python src/build.py
"""
from pathlib import Path
import datetime as dt

ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today().isoformat()

# ---------------------------------------------------------------- content
LLH = "https://bowonkwon.github.io/Legal-Language-Handbooks/"
AIH = "https://bowonkwon.github.io/AI-Assisted-Handbooks/"
CMM = "https://bowonkwon.github.io/Classical-Music-Metrics/"
GH = "https://github.com/BowonKwon/"

PROJECTS = [
    dict(
        key="llh", color="s1", site=LLH, repo=GH + "Legal-Language-Handbooks",
        ko=dict(
            tag="법률 외국어", title="법률 외국어 자습서", en_title="Legal Language Handbooks",
            lead="한국 법률가가 외국 법령·판결·원전을 원문으로 읽고 외국 법률가와 말할 수 있게 하려고 엮은 자습서. 열 개 언어, 각각 화면본·PDF·Anki 덱.",
            items=[
                ("Objection!", "법률 영어 첫걸음", "objection/"),
                ("異議あり", "조문과 판례로 배우는 일본어", "igiari/"),
                ("Anspruch", "청구권으로 읽는 법률 독일어", "anspruch/"),
                ("Par ces motifs", "법전과 법정의 프랑스어", "par-ces-motifs/"),
                ("本院认为", "조문과 판결의 중국어", "benyuan-renwei/"),
                ("Suum cuique", "원전으로 읽는 법률 라틴어", "suum-cuique/"),
                ("En nombre del Rey", "법전과 법정의 스페인어", "en-nombre-del-rey/"),
                ("In nome del popolo italiano", "법전과 법정의 이탈리아어", "in-nome-del-popolo-italiano/"),
                ("Nhân danh", "조문과 판결의 베트남어", "nhan-danh/"),
                ("Установи́л", "조문과 판결로 읽는 법률 러시아어", "ustanovil/"),
            ],
            extra=("곁가지 연구", "세종의 글자로 보는 외래어 표기", "훈민정음의 글자로 외국어 소리를 적는 보조 표기와 그 근거(스페인어·러시아어·중국어)", "sejong/"),
            facts=[("10", "언어판"), ("1.0", "대외판"), ("3", "꼴 — 화면본·PDF·Anki")],
        ),
        en=dict(
            tag="Legal languages", title="Legal Language Handbooks", en_title="",
            lead="Self-study handbooks for Korean lawyers who want to read statutes, judgments and classic texts in the original. Ten languages, each as a web edition, a PDF and an Anki deck.",
            items=[
                ("Objection!", "First steps in legal English", "objection/"),
                ("異議あり", "Japanese through statutes and case law", "igiari/"),
                ("Anspruch", "Legal German through the language of claims", "anspruch/"),
                ("Par ces motifs", "French of the code and the courtroom", "par-ces-motifs/"),
                ("本院认为", "Chinese of statutes and judgments", "benyuan-renwei/"),
                ("Suum cuique", "Legal Latin from the sources", "suum-cuique/"),
                ("En nombre del Rey", "Spanish of the code and the courtroom", "en-nombre-del-rey/"),
                ("In nome del popolo italiano", "Italian of the code and the courtroom", "in-nome-del-popolo-italiano/"),
                ("Nhân danh", "Vietnamese of statutes and judgments", "nhan-danh/"),
                ("Установи́л", "Legal Russian through statutes and judgments", "ustanovil/"),
            ],
            extra=("Side study", "Foreign sounds in Sejong's letters", "An auxiliary transcription of foreign sounds using the letters of Hunminjeongeum, with its evidence (Spanish, Russian, Chinese)", "sejong/"),
            facts=[("10", "languages"), ("1.0", "public edition"), ("3", "formats — web, PDF, Anki")],
        ),
    ),
    dict(
        key="aih", color="s3", site=AIH, repo=GH + "AI-Assisted-Handbooks",
        ko=dict(
            tag="AI·컴퓨터과학", title="AI 자습서", en_title="AI-Assisted Handbooks",
            lead="생성형 AI와 함께 엮은 자습서. Agentic AI 논문 읽기와 그 실전편, AI 인프라와 반도체, 법률가를 위한 LLM 위키.",
            items=[
                ("생각하고, 행동하고, 고쳐 쓰는 기계", "ReAct에서 LLM Wiki까지, Agentic AI 논문 읽기", "agentic-ai-reading/"),
                ("고삐를 쥐고 기계에게 일을 맡기는 법", "Claude Code·Codex로 내 일을 대신할 에이전트 짓기", "agentic-ai-practice/"),
                ("AI 인프라와 반도체", "통계·전산·AI 배경 학습자를 위한 일곱 회차 자습서", "ai-infra-semiconductors/"),
                ("읽은 것이 사라지지 않는 서재", "법률가를 위한 LLM 위키 자습서", "llm-wiki/"),
            ],
            extra=None,
            facts=[("4", "자습서"), ("3", "영어판 병행"), ("PDF", "인쇄본 함께")],
        ),
        en=dict(
            tag="AI · computer science", title="AI-Assisted Handbooks", en_title="",
            lead="Study handbooks compiled with generative AI: reading agentic-AI papers and its hands-on companion, AI infrastructure and semiconductors, and an LLM wiki guide for lawyers.",
            items=[
                ("Machines That Think, Act, and Revise", "Reading agentic-AI papers, from ReAct to LLM Wiki", "agentic-ai-reading/en/"),
                ("Harness in Hand", "Building AI agents with Claude Code and Codex", "agentic-ai-practice/en/"),
                ("AI Infrastructure and Semiconductors", "A seven-session self-study guide", "ai-infra-semiconductors/en/"),
                ("A Library That Remembers What You Read", "Building an LLM wiki — a guide for lawyers (Korean only)", "llm-wiki/"),
            ],
            extra=None,
            facts=[("4", "handbooks"), ("3", "with English editions"), ("PDF", "print editions included")],
        ),
    ),
    dict(
        key="cmm", color="s2", site=CMM, repo=GH + "Classical-Music-Metrics",
        ko=dict(
            tag="음악·데이터", title="서양 고전 음악 메트릭스", en_title="Classical Music Metrics",
            lead="악보와 연주를 숫자로 읽는 공개 데이터 사이트. 지표마다 정의·공식·표본·한계를 함께 두고, 공개 악보 코퍼스와 연주 데이터셋에서 뽑은 수치를 한 면씩 보여 준다. 첫 판은 바흐와 베토벤.",
            items=[
                ("지표 24개", "악보 14 · 연주 6 · 레퍼토리 4", "ko/index.html"),
                ("읽기용 판", "숫자가 말하는 것을 한 편의 글로", "ko/reading.html"),
                ("데이터", "CSV 내려받기와 라이선스", "ko/data.html"),
                ("방법·출처", "자료원·코드·장기 과제", "ko/method.html"),
            ],
            extra=None,
            facts=[("679", "악장(음표 63만 8천)"), ("36", "지휘자, 베토벤 교향곡 템포"), ("185", "시즌, 뉴욕 필 레퍼토리")],
        ),
        en=dict(
            tag="Music · data", title="Classical Music Metrics", en_title="",
            lead="An open data site that reads scores and performances as numbers. Every metric carries its definition, formula, sample and caveats, computed from open score corpora and performance datasets. The first edition covers Bach and Beethoven.",
            items=[
                ("24 metrics", "14 score · 6 performance · 4 repertoire", "en/index.html"),
                ("Reading edition", "What the numbers say, as one essay", "en/reading.html"),
                ("Data", "CSV downloads and licences", "en/data.html"),
                ("Method & sources", "Datasets, code, long-term tasks", "en/method.html"),
            ],
            extra=None,
            facts=[("679", "movements (638k notes)"), ("36", "conductors, Beethoven symphony tempi"), ("185", "seasons of NY Phil repertoire")],
        ),
    ),
]

TALKS = dict(
    ko=[
        ("AI-and-Law-Presentations", "인공지능과 법에 관한 초청 강연·학회 발표 슬라이드", GH + "AI-and-Law-Presentations"),
        ("SundayAI", "「일요일은 AI」 스터디 발제 자료", GH + "SundayAI"),
        ("PseudoLab_Study", "가짜연구소 스터디 발제 자료", GH + "PseudoLab_Study"),
    ],
    en=[
        ("AI-and-Law-Presentations", "Slides from invited talks and conference presentations on AI and law", GH + "AI-and-Law-Presentations"),
        ("SundayAI", "Presentations for the “Sunday is AI” study group", GH + "SundayAI"),
        ("PseudoLab_Study", "Presentations for the PseudoLab study group", GH + "PseudoLab_Study"),
    ],
)

TEXT = dict(
    ko=dict(
        title="권보원 — 공개 자료", name="권보원", sub="Bowon Kwon",
        hero="생성형 AI와 함께 엮은 공개 자료",
        hero_lead="법률 외국어 자습서, AI 자습서, 서양 고전 음악 데이터 사이트. 모두 원문과 대조하고 독립된 AI 검토를 거쳤지만, 틀린 서술이 남아 있을 수 있습니다. 원문과 다른 서술뿐 아니라 오탈자·풀이의 잘못·끊어진 링크 등 무엇이든 각 저장소의 Issues로 알려 주십시오.",
        nav=[("#projects", "자료"), ("#talks", "발표·스터디"), ("#about", "일러두기")],
        projects_h="자료", talks_h="발표·스터디", about_h="일러두기",
        site="사이트로", repo="저장소", more="전부 보기", contents="들어 있는 것",
        projects_sub="세 묶음 — 자세한 것은 각 사이트에", talks_sub="슬라이드는 GitHub 저장소에",
        about=[
            "<b>원문 대조</b> 조문·판결·원전·수치는 공식 원문이나 공개 데이터와 기계로 대조했고, 작성에 쓰지 않은 별도의 AI(Codex)가 원자료만 보고 블라인드로 검토했습니다. 그래도 틀린 서술이 남아 있을 수 있습니다.",
            "<b>이용 허락</b> 엮은이에게 권리가 있는 부분은 CC BY-NC 4.0(저작자표시-비영리)으로, 코드는 PolyForm Noncommercial 1.0.0 또는 각 저장소가 정한 조건으로 공개합니다. 인용한 법령·판결·원전·데이터는 각 권리자의 조건을 따릅니다. 자세한 조건은 저장소마다 적혀 있습니다.",
            "<b>개인 자료</b> 엮은이가 개인적으로 공부하며 만든 것으로, 엮은이가 속한 기관의 견해나 업무와는 관계가 없습니다. 법률 자문이 아닙니다.",
        ],
        foot="© 2026 권보원(Bowon Kwon) · 갱신 " + TODAY,
        lang_link=("en/index.html", "English"),
    ),
    en=dict(
        title="Bowon Kwon — Public materials", name="Bowon Kwon", sub="권보원",
        hero="Public materials compiled with generative AI",
        hero_lead="Legal-language handbooks, AI handbooks and a classical-music data site. All were checked against the originals and reviewed by an independent AI reviewer, but errors may remain. Anything wrong — a reading that departs from the original, a typo, a faulty gloss, a dead link — please report it via each repository's Issues.",
        nav=[("#projects", "Materials"), ("#talks", "Talks & study groups"), ("#about", "Notes")],
        projects_h="Materials", talks_h="Talks & study groups", about_h="Notes",
        site="Open site", repo="Repository", more="See all", contents="Inside",
        projects_sub="Three collections — details on each site", talks_sub="Slides live in the GitHub repositories",
        about=[
            "<b>Checked against the originals</b> Statutes, judgments, source texts and figures were machine-checked against official texts or open datasets, and a separate AI reviewer (Codex) that took no part in the writing reviewed them blind, from the raw sources only. Errors may still remain.",
            "<b>Licence</b> To the extent the editor holds rights, texts are licensed under CC BY-NC 4.0 and code under the PolyForm Noncommercial 1.0.0 or the terms stated in each repository. Quoted statutes, judgments, source texts and data remain subject to their own rights holders. Details are in each repository.",
            "<b>Personal materials</b> These were compiled as personal study and do not represent the views or work of any institution the editor belongs to. They are not legal advice.",
        ],
        foot="© 2026 Bowon Kwon · updated " + TODAY,
        lang_link=("../index.html", "한국어"),
    ),
)

# ---------------------------------------------------------------- style
CSS = """
:root{color-scheme:light;
  --bg:#f8f7f4;--bg2:#efede8;--bg3:#e6e3db;--card:#ffffff;--line:#dedbd3;--line2:#ebe8e1;
  --fg:#1d1f24;--fg2:#5a5e68;--fg3:#8a8e98;--accent:#3f6a9e;--accent2:#b5833f;
  --s1:#3a6fb0;--s2:#b5833f;--s3:#7f63ad;--glow:13%;
  --shadow:0 1px 2px rgba(30,32,40,.05),0 8px 24px rgba(30,32,40,.06);
  --shadow2:0 2px 4px rgba(30,32,40,.06),0 14px 32px rgba(30,32,40,.10);
  --display:"Noto Serif KR","Source Serif 4",Georgia,"Times New Roman",serif;
  --body:"Noto Sans KR",-apple-system,"Segoe UI","Apple SD Gothic Neo",Roboto,sans-serif}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
  --bg:#1b1c1f;--bg2:#222326;--bg3:#2a2b30;--card:#232428;--line:#34363c;--line2:#2b2d32;
  --fg:#ebe9e4;--fg2:#b3b1aa;--fg3:#80827f;--accent:#7ea4d6;--accent2:#d1a35f;
  --s1:#5a8ccf;--s2:#b5863a;--s3:#9078c4;--glow:17%;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px rgba(0,0,0,.28);
  --shadow2:0 2px 4px rgba(0,0,0,.35),0 14px 32px rgba(0,0,0,.4)}}
:root[data-theme="dark"]{color-scheme:dark;
  --bg:#1b1c1f;--bg2:#222326;--bg3:#2a2b30;--card:#232428;--line:#34363c;--line2:#2b2d32;
  --fg:#ebe9e4;--fg2:#b3b1aa;--fg3:#80827f;--accent:#7ea4d6;--accent2:#d1a35f;
  --s1:#5a8ccf;--s2:#b5863a;--s3:#9078c4;--glow:17%;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px rgba(0,0,0,.28);
  --shadow2:0 2px 4px rgba(0,0,0,.35),0 14px 32px rgba(0,0,0,.4)}
*{box-sizing:border-box}html{scroll-behavior:smooth}html,body{max-width:100%;overflow-x:hidden}
body{margin:0;font:16px/1.7 var(--body);background:var(--bg);color:var(--fg);overflow-wrap:anywhere;-webkit-font-smoothing:antialiased;position:relative}
body::before{content:"";position:absolute;inset:0 0 auto 0;height:720px;z-index:-1;pointer-events:none;
  background:
    radial-gradient(640px 420px at 8% -5%,color-mix(in srgb,var(--s1) var(--glow),transparent),transparent 70%),
    radial-gradient(560px 380px at 92% 4%,color-mix(in srgb,var(--s2) var(--glow),transparent),transparent 70%),
    radial-gradient(520px 360px at 55% 30%,color-mix(in srgb,var(--s3) var(--glow),transparent),transparent 70%);
  -webkit-mask-image:linear-gradient(#000 55%,transparent);mask-image:linear-gradient(#000 55%,transparent)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline;text-underline-offset:3px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
[id]{scroll-margin-top:4.2rem}
header{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 84%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);padding:.55rem 1.2rem;display:flex;gap:1.4rem;align-items:center;flex-wrap:wrap}
header .brand{font-family:var(--display);font-weight:600;font-size:1.05rem;color:var(--fg);display:flex;align-items:center;gap:.55rem}
header .brand i{display:inline-block;width:10px;height:10px;border-radius:3px;background:linear-gradient(135deg,var(--s1),var(--s3) 55%,var(--s2))}
header nav{display:flex;gap:1.1rem;flex-wrap:wrap}header nav a{color:var(--fg2);font-size:.92rem;padding:.2rem 0;border-bottom:1.5px solid transparent}header nav a:hover{text-decoration:none;color:var(--fg);border-color:var(--fg3)}
header .right{margin-left:auto;display:flex;gap:.6rem;align-items:center}
header .lang{font-size:.88rem;color:var(--fg2);border:1px solid var(--line);border-radius:999px;padding:.15rem .7rem;background:var(--card)}header .lang:hover{text-decoration:none;color:var(--fg);border-color:var(--fg3)}
.theme{border:1px solid var(--line);background:var(--card);color:var(--fg2);border-radius:999px;width:30px;height:30px;cursor:pointer;font-size:.9rem;line-height:1;padding:0}.theme:hover{color:var(--fg);border-color:var(--fg3)}
main{max-width:1100px;margin:0 auto;padding:2.2rem 1.2rem 4rem;min-width:0}
h1{word-break:keep-all;font-family:var(--display);font-weight:600;font-size:clamp(2rem,4.6vw,3.1rem);line-height:1.2;letter-spacing:-.018em;margin:.4rem 0 .9rem;text-wrap:balance}
h2{font-family:var(--display);font-weight:600;font-size:1.45rem;line-height:1.3;margin:0 0 .3rem}
.sec{margin-top:3.4rem}.sec-head{display:flex;align-items:baseline;gap:1rem;padding-bottom:.6rem;margin-bottom:1.3rem;border-bottom:1px solid var(--line);flex-wrap:wrap}
.sec-head .no{font-family:var(--display);font-size:.9rem;color:var(--fg3);letter-spacing:.12em}
.sec-head p{margin:0;color:var(--fg2);font-size:.92rem;margin-left:auto}
.hero{padding:2.2rem 0 2.4rem;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:2.5rem;align-items:center}
.hero .who{color:var(--fg3);font-size:.86rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.3rem}
.lead{word-break:keep-all;color:var(--fg2);font-size:1.1rem;max-width:62ch;margin:0}
.hero .lead{font-size:1.14rem}
.hero .cta{margin-top:1.4rem;display:flex;gap:.6rem;flex-wrap:wrap}
.chip{display:inline-flex;align-items:center;gap:.5rem;padding:.4rem .95rem .4rem .7rem;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--fg);font-size:.92rem;box-shadow:var(--shadow);transition:transform .15s,box-shadow .15s,border-color .15s}
.chip i{width:9px;height:9px;border-radius:50%;background:var(--c);flex:none}
.chip:hover{text-decoration:none;transform:translateY(-1px);box-shadow:var(--shadow2);border-color:var(--c)}
.mosaic{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr auto;gap:.6rem}
.mosaic a{border-radius:14px;padding:.9rem .95rem;display:flex;flex-direction:column;justify-content:flex-end;color:#fff;position:relative;overflow:hidden;min-height:120px;
  background:linear-gradient(160deg,color-mix(in srgb,var(--c) 92%,#fff),color-mix(in srgb,var(--c) 78%,#000));box-shadow:var(--shadow);transition:transform .18s,box-shadow .18s}
.mosaic a::after{content:"";position:absolute;inset:auto -30% -45% auto;width:75%;aspect-ratio:1;border-radius:50%;background:rgba(255,255,255,.12)}
.mosaic a:hover{text-decoration:none;transform:translateY(-2px);box-shadow:var(--shadow2)}
.mosaic .n{font-family:var(--display);font-size:clamp(1.6rem,3vw,2.3rem);font-weight:600;line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.mosaic small{font-size:.8rem;line-height:1.35;opacity:.92;margin-top:.3rem}
.mosaic .m1{grid-column:1/3;grid-row:1/3}.mosaic .m2{grid-column:3;grid-row:1/3}.mosaic .m3{grid-column:1/4;grid-row:3;min-height:0}
.mosaic .m3{flex-direction:row;align-items:baseline;gap:.8rem;justify-content:flex-start}.mosaic .m3 small{margin:0}
.proj{background:var(--card);border:1px solid var(--line);border-radius:16px;margin:1.3rem 0;box-shadow:var(--shadow);position:relative;overflow:hidden;
  display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:0}
.proj::before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:var(--c)}
.proj .num{position:absolute;right:1.1rem;top:.6rem;font-family:var(--display);font-size:3.6rem;font-weight:600;line-height:1;color:var(--c);opacity:.14;letter-spacing:-.04em;pointer-events:none;user-select:none}
.proj .info{padding:1.6rem 1.6rem 1.5rem 1.9rem;display:flex;flex-direction:column;min-width:0}
.proj .side{padding:1.6rem 1.6rem 1.5rem;background:var(--bg2);border-left:1px solid var(--line2);min-width:0}
.proj h3{word-break:keep-all;font-family:var(--display);font-weight:600;font-size:1.5rem;margin:.1rem 0 0;line-height:1.3}
.proj h3 small{display:block;font-family:var(--body);font-weight:400;color:var(--fg3);font-size:.9rem;margin-top:.1rem}
.tag{display:inline-block;font-size:.74rem;letter-spacing:.06em;padding:.12rem .6rem;border-radius:999px;color:var(--c);background:color-mix(in srgb,var(--c) 11%,transparent);border:1px solid color-mix(in srgb,var(--c) 30%,transparent);align-self:flex-start}
.proj .lead{font-size:.98rem;margin:.8rem 0 1.1rem}
.facts{display:flex;gap:0;margin:0 0 1.3rem;border-top:1px solid var(--line2);border-bottom:1px solid var(--line2)}
.facts div{flex:1;padding:.7rem .6rem .6rem 0;line-height:1.2;border-right:1px solid var(--line2);margin-right:.8rem}.facts div:last-child{border:0;margin:0}
.facts .n{font-family:var(--display);font-size:1.65rem;font-weight:600;color:var(--c);font-variant-numeric:tabular-nums;letter-spacing:-.02em}.facts small{display:block;color:var(--fg2);font-size:.8rem;margin-top:.25rem;line-height:1.35}
.links{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:auto}
.btn{display:inline-flex;align-items:center;gap:.4rem;font-size:.9rem;padding:.42rem 1rem;border-radius:999px;border:1px solid var(--line);color:var(--fg2);background:var(--card)}.btn:hover{text-decoration:none;color:var(--fg);border-color:var(--fg3)}
.btn.primary{background:var(--c);border-color:var(--c);color:#fff}.btn.primary:hover{background:color-mix(in srgb,var(--c) 85%,#000)}
.btn .ar{font-size:.95em;transition:transform .15s}.btn:hover .ar{transform:translateX(2px)}
.side .h{font-size:.76rem;letter-spacing:.1em;color:var(--fg3);text-transform:uppercase;margin:0 0 .6rem}
.items{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:.55rem;margin:0;padding:0;list-style:none}
.items a{display:block;padding:.6rem .8rem .55rem;border:1px solid var(--line2);border-radius:10px;background:var(--card);color:var(--fg);transition:transform .15s,box-shadow .15s,border-color .15s;position:relative}
.items a::after{content:"\\2197";position:absolute;right:.65rem;top:.45rem;color:var(--fg3);font-size:.8rem;opacity:0;transition:opacity .15s}
.items a:hover{text-decoration:none;border-color:var(--c);transform:translateY(-1px);box-shadow:var(--shadow)}.items a:hover::after{opacity:1}
.items b{display:block;font-size:.95rem;color:var(--fg);padding-right:1rem}.items small{color:var(--fg2);font-size:.83rem;line-height:1.45;display:block}
.extra{font-size:.9rem;color:var(--fg2);margin:.9rem 0 0;padding:.7rem .85rem;border:1px dashed var(--line);border-radius:10px;background:var(--card)}.extra b{color:var(--fg)}.extra .tag{margin-right:.3rem}
.talks{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:.8rem;padding:0;margin:0;list-style:none}
.talks a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1rem 1.1rem;box-shadow:var(--shadow);color:var(--fg);transition:transform .15s,box-shadow .15s,border-color .15s;position:relative}
.talks a:hover{text-decoration:none;transform:translateY(-2px);box-shadow:var(--shadow2);border-color:var(--fg3)}
.talks .gh{font-size:.74rem;letter-spacing:.08em;color:var(--fg3);text-transform:uppercase;display:block;margin-bottom:.25rem}
.talks b{display:block;color:var(--fg);font-size:1rem;font-family:var(--display)}.talks small{color:var(--fg2);font-size:.86rem;line-height:1.5;display:block;margin-top:.2rem}
.about{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:.8rem}
.about div{background:var(--bg2);border:1px solid var(--line2);border-radius:12px;padding:1rem 1.15rem;font-size:.93rem;line-height:1.65;color:var(--fg2)}
.about div b{display:block;color:var(--fg);font-family:var(--display);font-size:1.02rem;margin-bottom:.3rem}
footer{border-top:1px solid var(--line);color:var(--fg3);font-size:.82rem;padding:1.4rem 1.2rem;text-align:center}
footer .dots{display:inline-flex;gap:.35rem;margin-bottom:.6rem}footer .dots i{width:8px;height:8px;border-radius:50%;display:inline-block}
@media(max-width:860px){.hero{grid-template-columns:1fr;gap:1.6rem}.mosaic{max-width:440px}.proj{grid-template-columns:1fr}.proj .side{border-left:0;border-top:1px solid var(--line2)}}
@media(max-width:520px){.facts{flex-wrap:wrap}.facts div{flex:1 1 40%;border:0}.proj .num{font-size:2.6rem}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}html{scroll-behavior:auto}}
"""

THEME_JS = """(function(){var q=new URLSearchParams(location.search).get("theme");if(q==="light"||q==="dark"){localStorage.setItem("hub-theme",q)}else if(q==="auto"){localStorage.removeItem("hub-theme")}var v=localStorage.getItem("hub-theme");if(v)document.documentElement.setAttribute("data-theme",v)})();"""
TOGGLE_JS = """(function(){var b=document.querySelector(".theme");function cur(){return localStorage.getItem("hub-theme")||"auto"}function show(){b.textContent={auto:"\\u25d1",light:"\\u2600",dark:"\\u263e"}[cur()];b.title={auto:"Theme: auto",light:"Theme: light",dark:"Theme: dark"}[cur()]}b.addEventListener("click",function(){var n={auto:"light",light:"dark",dark:"auto"}[cur()];if(n==="auto"){localStorage.removeItem("hub-theme");document.documentElement.removeAttribute("data-theme")}else{localStorage.setItem("hub-theme",n);document.documentElement.setAttribute("data-theme",n)}show()});show()})();"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def project(p, i, lang):
    t, T = p[lang], TEXT[lang]
    h = [f"<section class='proj' id='{p['key']}' style='--c:var(--{p['color']})'>"]
    h.append(f"<span class='num' aria-hidden='true'>{i:02d}</span>")
    h.append("<div class='info'>")
    h.append(f"<span class='tag'>{esc(t['tag'])}</span>")
    sub = f"<small>{esc(t['en_title'])}</small>" if t["en_title"] else ""
    h.append(f"<h3>{esc(t['title'])}{sub}</h3>")
    h.append(f"<p class='lead'>{esc(t['lead'])}</p>")
    h.append("<div class='facts'>" + "".join(f"<div><span class='n'>{esc(n)}</span><small>{esc(l)}</small></div>" for n, l in t["facts"]) + "</div>")
    h.append(f"<div class='links'><a class='btn primary' href='{p['site']}'>{T['site']} <span class='ar'>→</span></a><a class='btn' href='{p['repo']}'>{T['repo']} (GitHub)</a></div>")
    h.append("</div><div class='side'>")
    h.append(f"<p class='h'>{esc(T['contents'])}</p>")
    h.append("<ul class='items'>" + "".join(f"<li><a href='{p['site']}{path}'><b>{esc(a)}</b><small>{esc(b)}</small></a></li>" for a, b, path in t["items"]) + "</ul>")
    if t["extra"]:
        k, a, b, path = t["extra"]
        h.append(f"<p class='extra'><span class='tag'>{esc(k)}</span> <a href='{p['site']}{path}'><b>{esc(a)}</b></a> — {esc(b)}</p>")
    h.append("</div></section>")
    return "\n".join(h)


def page(lang):
    T = TEXT[lang]
    nav = "".join(f"<a href='{h}'>{esc(l)}</a>" for h, l in T["nav"])
    projs = "\n".join(project(p, i + 1, lang) for i, p in enumerate(PROJECTS))
    chips = "".join(f"<a class='chip' href='#{p['key']}' style='--c:var(--{p['color']})'><i></i>{esc(p[lang]['title'])}</a>" for p in PROJECTS)
    mosaic = "".join(
        f"<a class='m{i+1}' href='#{p['key']}' style='--c:var(--{p['color']})'><span class='n'>{esc(p[lang]['facts'][0][0])}</span><small>{esc(p[lang]['facts'][0][1])} · {esc(p[lang]['title'])}</small></a>"
        for i, p in enumerate(PROJECTS))
    talks = "".join(f"<li><a href='{u}'><span class='gh'>GitHub</span><b>{esc(a)}</b><small>{esc(b)}</small></a></li>" for a, b, u in TALKS[lang])
    about = "".join(f"<div>{x}</div>" for x in T["about"])
    ll = T["lang_link"]
    dots = "".join(f"<i style='background:var(--{p['color']})'></i>" for p in PROJECTS)
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(T['title'])}</title><meta name="description" content="{esc(T['hero'])}">
<script>{THEME_JS}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header><a class="brand" href="#"><i></i>{esc(T['name'])}</a><nav>{nav}</nav>
<div class="right"><a class="lang" href="{ll[0]}">{ll[1]}</a><button class="theme" aria-label="theme">◑</button></div></header>
<main>
<div class="hero"><div><div class="who">{esc(T['name'])} · {esc(T['sub'])}</div><h1>{esc(T['hero'])}</h1><p class="lead">{esc(T['hero_lead'])}</p>
<div class="cta">{chips}</div></div>
<div class="mosaic" aria-hidden="true">{mosaic}</div></div>
<div class="sec" id="projects"><div class="sec-head"><span class="no">01</span><h2>{esc(T['projects_h'])}</h2><p>{esc(T['projects_sub'])}</p></div>
{projs}
</div>
<div class="sec" id="talks"><div class="sec-head"><span class="no">02</span><h2>{esc(T['talks_h'])}</h2><p>{esc(T['talks_sub'])}</p></div>
<ul class="talks">{talks}</ul></div>
<div class="sec" id="about"><div class="sec-head"><span class="no">03</span><h2>{esc(T['about_h'])}</h2></div>
<div class="about">{about}</div></div>
</main>
<footer><div class="dots">{dots}</div><br>{esc(T['foot'])} · <a href="{GH}">GitHub</a></footer>
<script>{TOGGLE_JS}</script>
</body></html>
"""


def main():
    (ROOT / "index.html").write_text(page("ko"), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("built", TODAY)


if __name__ == "__main__":
    main()
