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
ANS = "https://bowonkwon.github.io/Animal-Signals/"
PCM = "https://bowonkwon.github.io/Physical-Constants-Metrics/"
SKM = "https://bowonkwon.github.io/Sillok-Metrics/"
PPM = "https://bowonkwon.github.io/Privilege-Metrics/"
MJM = "https://bowonkwon.github.io/Munjip-Metrics/"
AHP = "https://bowonkwon.github.io/AI-History-in-Papers/"
KMC = "https://bowonkwon.github.io/Korean-Music-Charts/"
BPH = "https://bowonkwon.github.io/Book-Publishing-History/"
GH = "https://github.com/BowonKwon/"

PROJECTS = [
    dict(
        key="llh", color="s1", site=LLH, repo=GH + "Legal-Language-Handbooks",
        ko=dict(
            # 순서(소유자 2026-11-11, 두 칸씩 한 줄): 영·일 / 독·프 / 중·베 / 스·포 / 이·라 / 러·튀 / 네·스웨 — 새 언어판은 이 자리에 끼운다(en 목록도 같게)
            tag="법률 외국어", title="법률 외국어 자습서", en_title="Legal Language Handbooks",
            lead="한국 법률가가 외국 법령·판결·원전을 원문으로 읽고 외국 법률가와 말할 수 있게 하려고 엮은 자습서. 열두 개 언어, 각각 화면본·PDF·Anki 덱.",
            items=[
                ("Objection!", "법률 영어 첫걸음", "objection/"),
                ("異議あり", "조문과 판례로 배우는 일본어", "igiari/"),
                ("Anspruch", "청구권으로 읽는 법률 독일어", "anspruch/"),
                ("Par ces motifs", "법전과 법정의 프랑스어", "par-ces-motifs/"),
                ("本院认为", "조문과 판결의 중국어", "benyuan-renwei/"),
                ("Nhân danh", "조문과 판결의 베트남어", "nhan-danh/"),
                ("En nombre del Rey", "법전과 법정의 스페인어", "en-nombre-del-rey/"),
                ("In nome del popolo italiano", "법전과 법정의 이탈리아어", "in-nome-del-popolo-italiano/"),
                ("Suum cuique", "원전으로 읽는 법률 라틴어", "suum-cuique/"),
                ("Установи́л", "조문과 판결로 읽는 법률 러시아어", "ustanovil/"),
                ("Gereği düşünüldü", "조문으로 읽는 법률 튀르키예어", "https://bowonkwon.github.io/geregi-dusunuldu/"),
                ("Recht doende", "조문으로 읽는 법률 네덜란드어", "https://bowonkwon.github.io/recht-doende/"),
            ],
            extra=("곁가지 연구", "세종의 글자로 보는 외래어 표기", "훈민정음의 글자로 외국어 소리를 적는 보조 표기와 그 근거(스페인어·러시아어·중국어)", "sejong/"),
            facts=[("11", "언어판"), ("1.0", "대외판"), ("3", "꼴 — 화면본·PDF·Anki")],
        ),
        en=dict(
            tag="Legal languages", title="Legal Language Handbooks", en_title="",
            lead="Self-study handbooks for Korean lawyers who want to read statutes, judgments and classic texts in the original. Twelve languages, each as a web edition, a PDF and an Anki deck.",
            items=[
                ("Objection!", "First steps in legal English", "objection/"),
                ("異議あり", "Japanese through statutes and case law", "igiari/"),
                ("Anspruch", "Legal German through the language of claims", "anspruch/"),
                ("Par ces motifs", "French of the code and the courtroom", "par-ces-motifs/"),
                ("本院认为", "Chinese of statutes and judgments", "benyuan-renwei/"),
                ("Nhân danh", "Vietnamese of statutes and judgments", "nhan-danh/"),
                ("En nombre del Rey", "Spanish of the code and the courtroom", "en-nombre-del-rey/"),
                ("In nome del popolo italiano", "Italian of the code and the courtroom", "in-nome-del-popolo-italiano/"),
                ("Suum cuique", "Legal Latin from the sources", "suum-cuique/"),
                ("Установи́л", "Legal Russian through statutes and judgments", "ustanovil/"),
                ("Gereği düşünüldü", "Legal Turkish through the statutes", "https://bowonkwon.github.io/geregi-dusunuldu/"),
                ("Recht doende", "Legal Dutch through the statutes", "https://bowonkwon.github.io/recht-doende/"),
            ],
            extra=("Side study", "Foreign sounds in Sejong's letters", "An auxiliary transcription of foreign sounds using the letters of Hunminjeongeum, with its evidence (Spanish, Russian, Chinese)", "sejong/"),
            facts=[("11", "languages"), ("1.0", "public edition"), ("3", "formats — web, PDF, Anki")],
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
            facts=[("4", "자습서"), ("4", "영어판 병행"), ("PDF", "인쇄본 함께")],
        ),
        en=dict(
            tag="AI · computer science", title="AI-Assisted Handbooks", en_title="",
            lead="Study handbooks compiled with generative AI: reading agentic-AI papers and its hands-on companion, AI infrastructure and semiconductors, and an LLM wiki guide for lawyers.",
            items=[
                ("Machines That Think, Act, and Revise", "Reading agentic-AI papers, from ReAct to LLM Wiki", "agentic-ai-reading/en/"),
                ("Harness in Hand", "Building AI agents with Claude Code and Codex", "agentic-ai-practice/en/"),
                ("AI Infrastructure and Semiconductors", "A seven-session self-study guide", "ai-infra-semiconductors/en/"),
                ("A Library That Remembers What You Read", "Building an LLM wiki — a guide for lawyers", "llm-wiki/en/"),
            ],
            extra=None,
            facts=[("4", "handbooks"), ("4", "with English editions"), ("PDF", "print editions included")],
        ),
    ),
    dict(
        key="ahp", color="s9", site=AHP, repo=GH + "AI-History-in-Papers",
        ko=dict(
            tag="기술사·논문", title="논문으로 읽는 인공지능의 역사", en_title="AI History in Papers",
            lead="1943년부터 지금까지 인공지능 연구를 원 논문 191편으로 따라가는 역사 사이트. 점마다 원문 링크와 쪽을 밝힌 원문 한 문장, 인용이 확인된 선만 긋는 계보, 양쪽 서지를 나란히 놓는 우선권 상자, 수치로 다시 보는 「겨울」.",
            items=[
                ("시대 7장", "기원 1943부터 에이전트 2022까지, 장마다 서술·계보 그림·논문 카드", "ko/chapters/index.html"),
                ("계보", "주제 묶음 8개, 인용이 확인된 선만 실선", "ko/lineage/index.html"),
                ("겨울과 붐", "제목 구절 비율·학회 참가자·NeurIPS 채택 수를 같은 연도축에", "ko/winters.html"),
                ("논문 목록·방법", "191편 표와 CSV, 목록을 만들기 전에 등록한 선정 기준", "ko/papers.html"),
            ],
            extra=None,
            facts=[("191", "원 논문, 1943–2025"), ("1,108", "확인된 인용선"), ("76%", "AAAI 참가자 감소, 1986→1997")],
        ),
        en=dict(
            tag="History of technology · papers", title="AI History in Papers", en_title="",
            lead="The history of AI research from 1943 to today, followed through 191 original papers: a link to the source and one quoted sentence with its page for every point, lineage lines drawn only where a citation is confirmed, priority boxes that show both sides, and the \"winters\" re-examined with numbers.",
            items=[
                ("Seven eras", "From the origins of 1943 to agents since 2022: narrative, lineage graph and paper cards per chapter", "en/chapters/index.html"),
                ("Lineage", "Eight theme groups; solid lines only for confirmed citations", "en/lineage/index.html"),
                ("Winters and booms", "Title-phrase share, conference attendance and NeurIPS acceptances on one time axis", "en/winters.html"),
                ("Paper list and method", "191 papers as a table and CSV; selection rules registered before the list was made", "en/papers.html"),
            ],
            extra=None,
            facts=[("191", "original papers, 1943–2025"), ("1,108", "confirmed citation lines"), ("76%", "fall in AAAI attendance, 1986→1997")],
        ),
    ),
    dict(
        key="kmc", color="s10", site=KMC, repo=GH + "Korean-Music-Charts",
        ko=dict(
            tag="가요사·연대표", title="가요 차트 100년", en_title="Korean Music Charts",
            lead="1906년 유성기 녹음부터 디지털 차트까지, 누가 무엇으로 어떻게 한국 가요의 순위를 매겨 왔는지를 한 연대표로 잇는 역사 사이트. 집계 체계마다 주체·방식·표본·출처 등급을 적고, 1위 목록은 당대 신문과 집계표 사본으로 대조한 행에만 1차 출처를 단다.",
            items=[
                ("여섯 장", "순위를 매기는 방법들부터 공인 차트와 플랫폼까지", "ko/ch0.html"),
                ("집계 체계 연표", "체계·공백 29개를 한 시간축에, 2차 자료로만 받쳐지는 구간은 빗금", "ko/ch0.html"),
                ("데이터", "음반협회 월간 1위 122개월, 「가요톱10」 889행 등 CSV 8개", "ko/data.html"),
                ("방법", "미리 정한 표본 규칙, 출처 등급, 대조 결과", "ko/method.html"),
            ],
            extra=None,
            facts=[("122", "음반협회 월간 가요 1위, 1998–2008 사본 전수 대조"), ("29", "집계 체계와 공백 구간"), ("85 / 241", "「가요톱10」 1위 연속 중 정확히 5주에서 끝난 횟수")],
        ),
        en=dict(
            tag="Popular music history · timeline", title="Korean Music Charts", en_title="",
            lead="A history site that traces, on one timeline from the gramophone recordings of 1906 to digital charts, who ranked Korean popular songs, with what, and how. Each ranking system carries its actor, method, sample and source grade; in the No. 1 lists only rows checked against newspapers or archived tables of the time carry a primary source.",
            items=[
                ("Six chapters", "From ways of ranking songs to official charts and platforms", "en/ch0.html"),
                ("Timeline of systems", "29 systems and gaps on one time axis; spans backed only by secondary sources are hatched", "en/ch0.html"),
                ("Data", "Eight CSV files, including 122 months of the record association's monthly No. 1 and 889 rows of Gayo Top 10", "en/data.html"),
                ("Method", "Sampling rules fixed in advance, source grades, check results", "en/method.html"),
            ],
            extra=None,
            facts=[("122", "monthly No. 1 albums, 1998–2008, all checked against archived tables"), ("29", "ranking systems and gaps"), ("85 / 241", "Gayo Top 10 No. 1 runs that ended at exactly five weeks")],
        ),
    ),
    dict(
        key="cmm", color="s2", site=CMM, repo=GH + "Classical-Music-Metrics",
        ko=dict(
            tag="음악·데이터", title="서양 고전 음악 메트릭스", en_title="Classical Music Metrics",
            lead="악보와 연주를 숫자로 읽는 공개 데이터 사이트. 지표마다 정의·공식·표본·한계를 함께 두고, 공개 악보 코퍼스와 연주 데이터셋에서 뽑은 수치를 한 면씩 보여 준다. 바흐·베토벤·모차르트 악보, 뉴욕 필하모닉 전 작곡가 레퍼토리, IMSLP로 본 작품 활동과 A음 높이의 역사, 공연 기록으로 견준 악단 레퍼토리(1.5), 곡집 40개로 본 화성의 역사와 듣는 음계(1.6), 같은 시대 건반 소나타 곡집 일곱 개의 비교(1.8), 낭만기 피아노 소품과 색으로 그린 조성 지도(1.9), 악장을 지표로 펼친 곡 지도(1.10), 작곡가 30명의 생애 장르 흐름(1.11)까지.",
            items=[
                ("지표 68개", "악보 47 · 연주 9 · 레퍼토리 12", "ko/metrics/index.html"),
                ("작품·역사", "작품 활동·편성·템포 지시어·A음 높이", "ko/history.html"),
                ("화성의 역사", "곡집 40개로 본 7화음·반음계, 1590~1931", "ko/harmony.html"),
                ("음계와 조율", "시대·지역별 음계 45개를 보고 듣기", "ko/scales.html"),
                ("고전기 건반 소나타", "스카를라티부터 베토벤까지 곡집 일곱 개", "ko/sonatas.html"),
                ("낭만기 피아노 소품", "쇼팽에서 메트너까지, 조성 지도", "ko/romantic.html"),
                ("곡 지도", "악장 1,182개를 지표로 펼친 지도", "ko/map.html"),
                ("음 분포와 화음 진행", "근음 전이 행렬과 마디끼리의 닮음", "ko/profiles.html"),
                ("작곡가와 장르", "30명의 생애에 걸친 장르 흐름", "ko/genres.html"),
                ("악단 비교", "뉴욕 필·카네기홀·게반트하우스·서울시향", "ko/orchestras.html"),
                ("읽기용 판", "숫자가 말하는 것을 한 편의 글로", "ko/reading.html"),
                ("데이터", "CSV 내려받기와 라이선스", "ko/data.html"),
                ("방법·출처", "자료원·코드·장기 과제", "ko/method.html"),
            ],
            extra=None,
            facts=[("733", "악장(음표 74만)"), ("68", "지표, 악보·연주·레퍼토리"), ("185", "시즌, 뉴욕 필 레퍼토리")],
        ),
        en=dict(
            tag="Music · data", title="Classical Music Metrics", en_title="",
            lead="An open data site that reads scores and performances as numbers. Every metric carries its definition, formula, sample and caveats, computed from open score corpora and performance datasets: Bach, Beethoven and Mozart scores, the New York Philharmonic's repertoire across every composer, work activity and the history of the pitch of a′ from IMSLP, orchestras' repertoire compared from performance records (1.5), a history of harmony over 40 collections with scales you can hear (1.6), seven keyboard-sonata collections of the Classical era compared (1.8), Romantic piano pieces with colour key maps (1.9), a map of movements laid out by their metrics (1.10), and genres across the lives of 30 composers (1.11).",
            items=[
                ("68 metrics", "47 score · 9 performance · 12 repertoire", "en/metrics/index.html"),
                ("Works & history", "Work activity, orchestration, tempo marks, pitch of a′", "en/history.html"),
                ("History of harmony", "Seventh chords and chromaticism in 40 collections, 1590–1931", "en/harmony.html"),
                ("Scales and tuning", "45 scales across periods and regions, to see and hear", "en/scales.html"),
                ("Classical-era keyboard sonatas", "Seven collections, from Scarlatti to Beethoven", "en/sonatas.html"),
                ("Romantic piano miniatures", "From Chopin to Medtner, with key maps", "en/romantic.html"),
                ("Piece map", "1,182 movements laid out by their metrics", "en/map.html"),
                ("Pitch classes and chord progressions", "Root-transition matrices and how alike the measures are", "en/profiles.html"),
                ("Composers and genres", "Genres across the lives of 30 composers", "en/genres.html"),
                ("Orchestras", "NY Phil, Carnegie Hall, Gewandhaus, Seoul Phil", "en/orchestras.html"),
                ("Reading edition", "What the numbers say, as one essay", "en/reading.html"),
                ("Data", "CSV downloads and licenses", "en/data.html"),
                ("Method & sources", "Datasets, code, long-term tasks", "en/method.html"),
            ],
            extra=None,
            facts=[("733", "movements (740k notes)"), ("68", "metrics: score, performance, repertoire"), ("185", "seasons of NY Phil repertoire")],
        ),
    ),
    dict(
        key="ans", color="s4", site=ANS, repo=GH + "Animal-Signals",
        ko=dict(
            tag="생물학·근거", title="동물의 신호, 어디까지 알았나", en_title="Animal Signals",
            lead="동물 신호 연구를 주장 하나씩 나누어, 원 논문을 읽고 근거 수준을 매긴 사이트. 소리뿐 아니라 시각·화학·진동·전기 신호와 사람–동물 소통까지. 등급은 보고된 설계가 어디까지 왔는지의 좌표이고, 매긴 기준은 전부 공개되어 있다. 보도 문장과 논문 본문도 나란히 둔다.",
            items=[
                ("지도", "갈래와 신호 유형별 등급 분포", "map.html"),
                ("주장 카드", "주장마다 등급·이유·통제·문헌", "claims.html"),
                ("보도와 논문, 나란히", "보도 제목과 논문 본문의 간극", "press.html"),
                ("사람과 동물", "영리한 한스 점검표", "aic.html"),
                ("직접 해 보기", "향유고래 코다를 원 데이터 수치로 합성", "try.html"),
            ],
            extra=None,
            facts=[("183", "주장, 등급 A~NS"), ("96", "원 논문"), ("37", "보도 문장, 논문과 대조")],
        ),
        en=dict(
            tag="Biology · evidence", title="Animal Signals", en_title="",
            lead="Research on animal signals split into single claims, each graded for evidence from the original paper: sound, but also visual, chemical, vibrational and electric signals, and human–animal communication. A grade records how far the reported design has gone, under criteria published in full. Press sentences sit beside the papers they cite.",
            items=[
                ("Map", "Grade distribution by lineage and signal type", "map.html"),
                ("Claims", "Grade, reason, controls and sources per claim", "claims.html"),
                ("Press and papers", "The gap between headline and paper", "press.html"),
                ("Human and animal", "The Clever Hans checklist", "aic.html"),
                ("Try it", "Sperm-whale codas synthesised from the published data", "try.html"),
            ],
            extra=None,
            facts=[("183", "claims, graded A–NS"), ("96", "source papers"), ("37", "press sentences checked against papers")],
        ),
    ),
    dict(
        key="pcm", color="s5", site=PCM, repo=GH + "Physical-Constants-Metrics",
        ko=dict(
            tag="물리·데이터", title="물리 상수 메트릭스", en_title="Physical Constants Metrics",
            lead="물리 상수(CODATA 와 그 이전, 1929~)와 CIAAW 원자량의 권고값, 그리고 1929년 이후 발표된 허블 상수 추정값이 스스로 밝힌 불확도만큼 믿을 만했는지 센다.",
            items=[
                ("지표", "반감기·판간 이동·2022 판 기준 놓침률·꼬리 두께", "ko/metrics/index.html"),
                ("상수·원자량", "상수 31개·원소 88개, 판별 값과 그림", "ko/constants/index.html"),
                ("허블 상수", "발표된 H0 추정값과 오차, 1929~2019 연대기와 지표", "ko/hubble/index.html"),
                ("CODATA 이전", "1929~1969년 권고값과 Henrion & Fischhoff 재계산", "ko/early/index.html"),
                ("읽기", "오차 막대와 그 다음 판", "ko/reading.html"),
                ("데이터", "CSV 내려받기와 라이선스", "ko/data.html"),
            ],
            extra=None,
            facts=[("10", "판, 1969~2022"), ("17", "핵심 상수"), ("12.9%", "판간 이동이 불확도의 2배 초과(정규 4.6%)")],
        ),
        en=dict(
            tag="Physics · data", title="Physical Constants Metrics", en_title="",
            lead="Whether the recommended values of the physical constants (CODATA and its predecessors since 1929) and CIAAW atomic weights, and the Hubble-constant estimates published since 1929, were as reliable as their own stated uncertainties.",
            items=[
                ("Metrics", "Half-life, edition-to-edition moves, miss rate against 2022, tails", "en/metrics/index.html"),
                ("Constants & atomic weights", "31 constants and 88 elements, values by edition with plots", "en/constants/index.html"),
                ("Hubble constant", "Published H0 estimates and their errors: 1929–2019 chronology and metrics", "en/hubble/index.html"),
                ("Before CODATA", "Recommended values 1929–1969 and Henrion & Fischhoff recomputed", "en/early/index.html"),
                ("Reading", "Error bars and the next edition", "en/reading.html"),
                ("Data", "CSV downloads and licenses", "en/data.html"),
            ],
            extra=None,
            facts=[("10", "editions, 1969–2022"), ("17", "core constants"), ("12.9%", "moves beyond twice the uncertainty (normal 4.6%)")],
        ),
    ),
    dict(
        key="skm", color="s6", site=SKM, repo=GH + "Sillok-Metrics",
        ko=dict(
            tag="역사·데이터", title="실록 메트릭스", en_title="Sillok Metrics",
            lead="조선왕조실록 기사 41만 건을 센 지표 34개와, 지표마다 붙인 신뢰도 카드. 1.2 에서 고려사 천문지·고려사절요·승정원일기의 천문 기사 13,337건을 실록과 같은 코드북·같은 천문 계산으로 대조한 「사료 셋」 계열과, 승정원일기 날씨 칸 10만여 날을 토큰 규칙으로 분해해 측우기·기상청 관측과 맞춘 계열을 더했다.",
            items=[
                ("지표", "기록의 양·판본·하늘·정치·형정에 사료 셋·날씨 칸을 더한 일곱 계열 34개", "ko/metrics/index.html"),
                ("왕대", "27대 각각의 기사·글자·지표와 재위 리본", "ko/kings/index.html"),
                ("읽기용 판", "하늘은 맞았나, 사형 기사는 사형이 아니다", "ko/reading.html"),
                ("데이터", "기사 테이블·코드북·판정 전부 CSV", "ko/data.html"),
            ],
            extra=None,
            facts=[("414,501", "기사, 판본 33종"), ("34", "지표, 일곱 계열"), ("73%", "측우기가 비를 잰 날 가운데 날씨 칸에 雨가 있는 비율")],
        ),
        en=dict(
            tag="History · data", title="Sillok Metrics", en_title="",
            lead="The Veritable Records of the Joseon Dynasty counted across 414,501 articles: 34 metrics, each with a reliability card saying how far to trust the number. Version 1.2 adds two series. One codes 13,337 astronomical articles from the Goryeosa astronomical treatise, the Goryeosa-jeolyo and the Seungjeongwon Ilgi with the Sillok's codebook and checks them against the same computed sky. The other splits the Ilgi's daily weather cell into tokens and compares it with rain-gauge and modern station records.",
            items=[
                ("Metrics", "34 across seven series: volume, editions, sky, politics, justice, three sources compared, and the weather cell", "en/metrics/index.html"),
                ("Reigns", "All 27, with counts, metrics and a reign ribbon", "en/kings/index.html"),
                ("Reading edition", "Was the sky right? A death-penalty article is not an execution", "en/reading.html"),
                ("Data", "Article table, codebooks and every judgment as CSV", "en/data.html"),
            ],
            extra=None,
            facts=[("414,501", "articles, 33 editions"), ("34", "metrics in seven series"), ("73%", "days the rain gauge measured rain on which the weather cell says 雨")],
        ),
    ),
    dict(
        key="ppm", color="s7", site=PPM, repo=GH + "Privilege-Metrics",
        ko=dict(
            tag="법·역사·데이터", title="특권에서 특허로", en_title="From Privilege to Patent",
            lead="근대 특허법·저작권법이 생기기 전, 베네치아·잉글랜드·네덜란드에서 군주와 의회가 하나씩 내준 발명·출판 특권을 지금까지 전하는 목록에서 한 건씩 센 지표 18개와 신뢰도 카드.",
            items=[
                ("지표", "몇 건·어느 분야·누가·어떤 조건, 출판 등록까지 다섯 계열 18개", "ko/metrics/index.html"),
                ("관할", "잉글랜드·베네치아·네덜란드, 목록과 단위", "ko/places.html"),
                ("읽기용 판", "1624년 전후, 누가 받았나, 출판 쪽", "ko/reading.html"),
                ("데이터", "Woodcroft 14,359번·출판업조합 등록·코딩 표 전부 CSV", "ko/data.html"),
            ],
            extra=None,
            facts=[("14,375", "잉글랜드 발명 허여, 1561–1852"), ("10,453", "런던 출판업조합 등록, 1557–1640"), ("93 / 96", "1625–1640 허여 중 존속기간 14년 이하")],
        ),
        en=dict(
            tag="Law · history · data", title="From Privilege to Patent", en_title="",
            lead="Before modern patent and copyright law, rulers and assemblies in Venice, England and the Dutch Republic granted invention and printing privileges one petitioner at a time. 18 metrics count the surviving lists grant by grant, each with a reliability card.",
            items=[
                ("Metrics", "18 in five series: how many, which trades, to whom, on what terms, and the Stationers' Register", "en/metrics/index.html"),
                ("Jurisdictions", "England, Venice and the Dutch Republic: lists and units", "en/places.html"),
                ("Reading edition", "Before and after 1624, who received them, printing", "en/reading.html"),
                ("Data", "Woodcroft's 14,359 entries, the Stationers' Register and every coding table as CSV", "en/data.html"),
            ],
            extra=None,
            facts=[("14,375", "English invention grants, 1561–1852"), ("10,453", "Stationers' Register entries, 1557–1640"), ("93 / 96", "grants of 1625–1640 with a term of 14 years or less")],
        ),
    ),
    dict(
        key="bph", color="s11", site=BPH, repo=GH + "Book-Publishing-History",
        ko=dict(
            tag="출판사·연대표", title="책 출간의 역사", en_title="A History of Book Publishing",
            lead="필사본에서 전자책까지, 한 해에 책이 몇 종 나왔는지를 세는 방법과 함께 보는 역사 사이트. 출처마다 다른 선으로 놓고 출처가 셈법을 바꾼 해를 표시한다. 독일어권·네덜란드·인큐내뷸러 종합목록은 규칙을 먼저 정해 직접 다시 셌고, 한국·일본·중국·미국의 공식 표는 원문에서 옮겨 대조했다.",
            items=[
                ("일곱 장", "「책 한 종」을 어떻게 세나부터 디지털 이후까지", "ko/ch0.html"),
                ("정의 단절 연대표", "UNESCO 1964 권고부터 출처마다 셈법이 바뀐 자리", "ko/ch0.html"),
                ("데이터", "판 수·종수·정의 단절 표 CSV 21개", "ko/data.html"),
                ("방법", "미리 정한 계수 규칙과 사후 정정, 독립 재계수 결과", "ko/method.html"),
            ],
            extra=None,
            facts=[("669,442", "독일어권 인쇄본 판 수, 1501–1800(VD16·17·18)"), ("28,530", "1500년까지 인쇄된 판(ISTC)"), ("11", "출처가 셈법을 바꾼 자리")],
        ),
        en=dict(
            tag="Publishing history · timeline", title="A History of Book Publishing", en_title="",
            lead="A history site that follows, from manuscripts to e-books, how many books appeared each year together with how they were counted. Each source gets its own line, and the years in which a source changed its counting are marked. The German, Dutch and incunabula union catalogs were recounted under rules fixed in advance; official tables for Korea, Japan, China and the United States were transcribed from the originals and checked against them.",
            items=[
                ("Seven chapters", "From how to count \"one book\" to after digital", "en/ch0.html"),
                ("Timeline of definition breaks", "From the 1964 UNESCO recommendation on, each point where a source changed its counting", "en/ch0.html"),
                ("Data", "21 CSV files of editions, titles and definition breaks", "en/data.html"),
                ("Method", "Counting rules fixed in advance, later corrections, and the independent recount", "en/method.html"),
            ],
            extra=None,
            facts=[("669,442", "editions printed in the German-speaking lands, 1501–1800 (VD16, VD17, VD18)"), ("28,530", "editions printed up to 1500 (ISTC)"), ("11", "points where a source changed its counting")],
        ),
    ),
    dict(
        key="mjm", color="s8", site=MJM, repo=GH + "Munjip-Metrics",
        ko=dict(
            tag="한문학·데이터", title="문집 메트릭스", en_title="Munjip Metrics",
            lead="한국문집총간 1,249종의 원문 XML 전문을 편(시 한 수·편지 한 통·묘지명 한 편) 단위로 나눈 637,203편을 세어 규모·문체 구성·관계 문체·저자와 간행의 네 계열 23개 지표로 보이는 공개 데이터 사이트. 고전번역원의 문체분류를 그대로 쓰고, 파싱·연결은 표본으로 정밀도를 잰다. 원문은 싣지 않고 편마다 고전종합DB로 연결한다.",
            items=[
                ("지표 23개", "규모 7 · 문체 구성 8 · 관계 문체 3 · 저자와 간행 5", "ko/metrics/index.html"),
                ("문집 1,249종", "문집마다 한 면과 순위표, 인물 면 10", "ko/collections/index.html"),
                ("읽기용 판", "숫자가 말하는 것을 한 편의 글로", "ko/reading.html"),
                ("데이터", "작품 테이블 637,203행과 모든 표의 CSV", "ko/data.html"),
            ],
            extra=None,
            facts=[("637,203", "편, 문집 1,249종"), ("62%", "저자 글 중 시 — 15세기 88%에서 19세기 42%로"), ("613", "저자 1,248명 중 문과방목 연결")],
        ),
        en=dict(
            tag="Sinographic literature · data", title="Munjip Metrics", en_title="",
            lead="The full XML text of the 1,249 collections of the Hanguk munjip chonggan, split into 637,203 works (one poem, one letter, one epitaph), counted in 23 metrics across four series: size, genre composition, relationship genres, authors and publication. Genre classes are the ITKC's own; parsing and linkage steps carry sampled precision. No text is reproduced; every work links to the ITKC database.",
            items=[
                ("23 metrics", "7 size · 8 genre composition · 3 relationship genres · 5 authors and publication", "en/metrics/index.html"),
                ("1,249 collections", "A page for each collection, a sortable list, ten person pages", "en/collections/index.html"),
                ("Reading edition", "What the numbers say, as one essay", "en/reading.html"),
                ("Data", "The 637,203-row work table and every table as CSV", "en/data.html"),
            ],
            extra=None,
            facts=[("637,203", "works in 1,249 collections"), ("62%", "of authors' own works are poems — 88% (15th c.) to 42% (19th)"), ("613", "of 1,248 authors linked to the examination roster")],
        ),
    ),
]

ORDER = ["llh", "aih", "ahp", "cmm", "kmc", "ans", "pcm", "ppm", "bph", "skm", "mjm"]
assert sorted(ORDER) == sorted(p["key"] for p in PROJECTS)
PROJECTS.sort(key=lambda p: ORDER.index(p["key"]))

TALKS = dict(
    ko=[
        ("AI-and-Law-Presentations", "인공지능과 법에 관한 초청 강연·학회 발표 슬라이드(정리 중, 차례로 게시)", GH + "AI-and-Law-Presentations"),
        ("SundayAI", "「일요일은 AI」 스터디 발제 자료", GH + "SundayAI"),
        ("PseudoLab_Study", "가짜연구소 스터디 발제 자료", GH + "PseudoLab_Study"),
    ],
    en=[
        ("AI-and-Law-Presentations", "Slides from invited talks and conference presentations on AI and law (being prepared; posted in stages)", GH + "AI-and-Law-Presentations"),
        ("SundayAI", "Presentations for the “Sunday is AI” study group", GH + "SundayAI"),
        ("PseudoLab_Study", "Presentations for the PseudoLab study group", GH + "PseudoLab_Study"),
    ],
)

TEXT = dict(
    ko=dict(
        title="권보원의 실험실 — 생성형 AI와 함께 엮은 공개 자료", name="권보원", sub="Bowon Kwon", lab="실험실 · Lab",
        hero="생성형 AI와 함께 엮은 공개 자료",
        hero_lead="완성된 책이나 확정된 결론이 아니라, 생성형 AI와 함께 이것저것 시도해 보고 자료를 모아 엮어 본 실험의 기록입니다. 법률 외국어 자습서, AI 자습서, 동물 신호 연구의 근거 등급표, 그리고 서양 고전 음악·물리 상수·조선왕조실록·근대 이전 특권·한국문집총간을 숫자로 센 데이터 사이트 다섯, 논문·가요 차트·책 출간으로 엮은 역사 사이트 셋. 판마다 원문과 대조하고 독립된 AI 검토를 거쳤지만 아직 고쳐 가는 중이어서, 틀린 서술이 남아 있을 수 있습니다. 원문과 다른 서술뿐 아니라 오탈자·풀이의 잘못·끊어진 링크 등 무엇이든 각 저장소의 Issues로 알려 주십시오.",
        nav=[("#projects", "자료"), ("#talks", "발표·스터디"), ("#about", "일러두기")],
        projects_h="자료", talks_h="발표·스터디", about_h="일러두기",
        site="사이트로", repo="저장소", more="전부 보기", contents="들어 있는 것",
        projects_sub="열한 묶음 — 자세한 것은 각 사이트에", talks_sub="슬라이드는 GitHub 저장소에",
        about=[
            "<b>원문 대조</b> 조문·판결·원전·수치는 공식 원문이나 공개 데이터와 기계로 대조했고, 작성에 쓰지 않은 별도의 AI(Codex)가 원자료만 보고 블라인드로 검토했습니다. 그래도 틀린 서술이 남아 있을 수 있습니다.",
            "<b>이용 허락</b> 엮은이에게 권리가 있는 부분은 CC BY-NC 4.0(저작자표시-비영리) 또는 CC BY 4.0으로, 코드는 PolyForm Noncommercial 1.0.0 또는 MIT 등 각 저장소가 정한 조건으로 공개합니다. 인용한 법령·판결·원전·데이터는 각 권리자의 조건을 따릅니다. 자세한 조건은 저장소마다 적혀 있습니다.",
            "<b>개인 자료</b> 엮은이가 개인적으로 공부하며 만든 것으로, 엮은이가 속한 기관의 견해나 업무와는 관계가 없습니다. 법률 자문이 아닙니다.",
        ],
        foot="© 2026 권보원(Bowon Kwon) · 갱신 " + TODAY,
        lang_link=("en/index.html", "English"),
    ),
    en=dict(
        title="Bowon Kwon’s Lab — Public materials compiled with generative AI", name="Bowon Kwon", sub="권보원", lab="Lab · 실험실",
        hero="Public materials compiled with generative AI",
        hero_lead="These are not finished books or settled conclusions but a record of experiments — things tried out, and material gathered and put together, with generative AI. Legal-language handbooks, AI handbooks, an evidence table for animal-signal research, and five data sites that count classical music, physical constants, the Joseon Veritable Records, pre-modern privileges and Korean literary collections, and three history sites built from papers, music charts and book publishing. Each release was checked against the originals and reviewed by an independent AI reviewer, but the work is still being revised and errors may remain. Anything wrong — a reading that departs from the original, a typo, a faulty gloss, a dead link — please report it via each repository's Issues.",
        nav=[("#projects", "Materials"), ("#talks", "Talks & study groups"), ("#about", "Notes")],
        projects_h="Materials", talks_h="Talks & study groups", about_h="Notes",
        site="Open site", repo="Repository", more="See all", contents="Inside",
        projects_sub="Eleven collections — details on each site", talks_sub="Slides live in the GitHub repositories",
        about=[
            "<b>Checked against the originals</b> Statutes, judgments, source texts and figures were machine-checked against official texts or open datasets, and a separate AI reviewer (Codex) that took no part in the writing reviewed them blind, from the raw sources only. Errors may still remain.",
            "<b>Licence</b> To the extent the editor holds rights, texts are licensed under CC BY-NC 4.0 or CC BY 4.0, and code under the PolyForm Noncommercial 1.0.0, MIT or the terms stated in each repository. Quoted statutes, judgments, source texts and data remain subject to their own rights holders. Details are in each repository.",
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
  --s1:#3a6fb0;--s2:#b5833f;--s3:#7f63ad;--s4:#4d8a5f;--s5:#2f7470;--s6:#8a4f5c;--s7:#9a4a32;--s8:#2e6b5e;--s9:#5b6a9c;--s10:#7d6b2e;--s11:#8e4f86;--glow:13%;
  --shadow:0 1px 2px rgba(30,32,40,.05),0 8px 24px rgba(30,32,40,.06);
  --shadow2:0 2px 4px rgba(30,32,40,.06),0 14px 32px rgba(30,32,40,.10);
  --display:"Noto Serif KR","Source Serif 4",Georgia,"Times New Roman",serif;
  --body:"Noto Sans KR",-apple-system,"Segoe UI","Apple SD Gothic Neo",Roboto,sans-serif}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
  --bg:#1b1c1f;--bg2:#222326;--bg3:#2a2b30;--card:#232428;--line:#34363c;--line2:#2b2d32;
  --fg:#ebe9e4;--fg2:#b3b1aa;--fg3:#80827f;--accent:#7ea4d6;--accent2:#d1a35f;
  --s1:#5a8ccf;--s2:#b5863a;--s3:#9078c4;--s4:#6aa97c;--s5:#6fb0aa;--s6:#c08595;--s7:#d0866b;--s8:#6fb3a3;--s9:#8f9fd6;--s10:#b9a55c;--s11:#c487b9;--glow:17%;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px rgba(0,0,0,.28);
  --shadow2:0 2px 4px rgba(0,0,0,.35),0 14px 32px rgba(0,0,0,.4)}}
:root[data-theme="dark"]{color-scheme:dark;
  --bg:#1b1c1f;--bg2:#222326;--bg3:#2a2b30;--card:#232428;--line:#34363c;--line2:#2b2d32;
  --fg:#ebe9e4;--fg2:#b3b1aa;--fg3:#80827f;--accent:#7ea4d6;--accent2:#d1a35f;
  --s1:#5a8ccf;--s2:#b5863a;--s3:#9078c4;--s4:#6aa97c;--s5:#6fb0aa;--s6:#c08595;--s7:#d0866b;--s8:#6fb3a3;--s9:#8f9fd6;--s10:#b9a55c;--s11:#c487b9;--glow:17%;
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
.mosaic{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:minmax(86px,auto);gap:.6rem;
  grid-template-areas:"L1 L1 T1 S1" "L1 L1 T1 S2" "S3 W1 W1 T2" "L2 L2 S4 T2" "L2 L2 L3 L3" "W2 W2 L3 L3"}
.mosaic a{border-radius:14px;padding:.85rem .9rem;display:flex;flex-direction:column;justify-content:flex-end;color:#fff;position:relative;overflow:hidden;min-height:0;
  background:var(--motif) right -6% top -8%/auto 64% no-repeat,linear-gradient(160deg,color-mix(in srgb,var(--c) 92%,#fff),color-mix(in srgb,var(--c) 78%,#000));box-shadow:var(--shadow);transition:transform .18s,box-shadow .18s}
.mosaic a.sz-W{background-size:auto 96%,auto;background-position:right -2% center,0 0}.mosaic a.sz-S{background-size:auto 58%,auto;background-position:right -16% top -12%,0 0}
.mosaic a.sz-T{background-size:96% auto,auto;background-position:right -12% top -4%,0 0}
.mosaic a:hover{text-decoration:none;transform:translateY(-2px);box-shadow:var(--shadow2)}
.mosaic .n{font-family:var(--display);font-size:clamp(1.5rem,2.6vw,2.1rem);font-weight:600;line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums;position:relative}
.mosaic .sz-L .n{font-size:clamp(1.9rem,3.4vw,2.7rem)}
.mosaic small{font-size:.78rem;line-height:1.35;opacity:.94;margin-top:.3rem;position:relative;text-shadow:0 1px 2px rgba(0,0,0,.18)}
.mosaic small{overflow-wrap:normal;word-break:keep-all;hyphens:auto}.mosaic .sz-S small,.mosaic .sz-T small{font-size:.74rem}.mosaic .sz-W small{max-width:66%}
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
html[lang="ko"] p,html[lang="ko"] small,html[lang="ko"] li{word-break:keep-all;overflow-wrap:break-word}
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
@media(max-width:860px){.hero{grid-template-columns:1fr;gap:1.6rem}.mosaic{max-width:520px;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-areas:"L1 L1" "T1 S1" "T1 S2" "W1 W1" "S3 T2" "S4 T2" "L2 L2" "W2 W2" "L3 L3"}.mosaic a.sz-L{background-size:auto 82%,auto}.proj{grid-template-columns:1fr}.proj .side{border-left:0;border-top:1px solid var(--line2)}}
@media(max-width:520px){.facts{flex-wrap:wrap}.facts div{flex:1 1 40%;border:0}.proj .num{font-size:2.6rem}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}html{scroll-behavior:auto}}
"""

THEME_JS = """(function(){var q=new URLSearchParams(location.search).get("theme");if(q==="light"||q==="dark"){localStorage.setItem("hub-theme",q)}else if(q==="auto"){localStorage.removeItem("hub-theme")}var v=localStorage.getItem("hub-theme");if(v)document.documentElement.setAttribute("data-theme",v)})();"""
TOGGLE_JS = """(function(){var b=document.querySelector(".theme");function cur(){return localStorage.getItem("hub-theme")||"auto"}function show(){b.textContent={auto:"\\u25d1",light:"\\u2600",dark:"\\u263e"}[cur()];b.title={auto:"Theme: auto",light:"Theme: light",dark:"Theme: dark"}[cur()]}b.addEventListener("click",function(){var n={auto:"light",light:"dark",dark:"auto"}[cur()];if(n==="auto"){localStorage.removeItem("hub-theme");document.documentElement.removeAttribute("data-theme")}else{localStorage.setItem("hub-theme",n);document.documentElement.setAttribute("data-theme",n)}show()});show()})();"""


# Hero mosaic: a 4 x 6 bento grid (areas in the .mosaic CSS). L = 2x2, T = 1x2 tall, W = 2x1 wide, S = 1x1.
# Sites with the longest headline numbers take the large tiles; small tiles show the number and title only.
SLOT = {"bph": "L1", "mjm": "L2", "skm": "L3", "llh": "T1", "aih": "T2", "ppm": "W1", "ans": "W2",
        "cmm": "S1", "ahp": "S2", "pcm": "S3", "kmc": "S4"}  # tall tiles are one column wide: only short labels fit
# Motif by kind of site, drawn in white over the colour: metrics = bars, history = timeline,
# handbooks = stacked pages, evidence table = signal waves.
KIND = {"cmm": "bars", "pcm": "bars", "skm": "bars", "ppm": "bars", "mjm": "bars",
        "ahp": "time", "kmc": "time", "bph": "time", "llh": "pages", "aih": "pages", "ans": "waves"}


def _svg(body: str) -> str:
    from urllib.parse import quote
    return "url(\"data:image/svg+xml," + quote(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>{body}</svg>", safe="") + "\")"


MOTIF = {
    "bars": _svg("<g fill='#fff' fill-opacity='.15'><rect x='8' y='62' width='14' height='38' rx='2'/><rect x='28' y='40' width='14' height='60' rx='2'/>"
                 "<rect x='48' y='52' width='14' height='48' rx='2'/><rect x='68' y='18' width='14' height='82' rx='2'/></g>"
                 "<polyline points='15,56 35,34 55,46 75,12' fill='none' stroke='#fff' stroke-opacity='.3' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/>"),
    "time": _svg("<g stroke='#fff' stroke-opacity='.28' stroke-width='2.2' stroke-linecap='round'><line x1='4' y1='62' x2='98' y2='62'/>"
                 "<line x1='22' y1='62' x2='22' y2='40'/><line x1='50' y1='62' x2='50' y2='28'/><line x1='78' y1='62' x2='78' y2='46'/></g>"
                 "<g fill='#fff' fill-opacity='.2'><circle cx='22' cy='62' r='6'/><circle cx='50' cy='62' r='8'/><circle cx='78' cy='62' r='6'/>"
                 "<rect x='12' y='30' width='20' height='8' rx='2'/><rect x='38' y='17' width='24' height='9' rx='2'/><rect x='68' y='36' width='20' height='8' rx='2'/></g>"),
    "pages": _svg("<g stroke='#fff' stroke-opacity='.3' stroke-width='2' fill='#fff' fill-opacity='.07'>"
                  "<rect x='34' y='8' width='54' height='70' rx='4' transform='rotate(8 61 43)'/><rect x='24' y='16' width='54' height='70' rx='4'/></g>"
                  "<g stroke='#fff' stroke-opacity='.3' stroke-width='2.2' stroke-linecap='round'><line x1='33' y1='32' x2='68' y2='32'/><line x1='33' y1='44' x2='68' y2='44'/>"
                  "<line x1='33' y1='56' x2='60' y2='56'/><line x1='33' y1='68' x2='64' y2='68'/></g>"),
    "waves": _svg("<g fill='none' stroke='#fff' stroke-opacity='.28' stroke-width='2.4' stroke-linecap='round'>"
                  "<path d='M30 74 a16 16 0 0 1 0 -32'/><path d='M44 84 a30 30 0 0 1 0 -52'/><path d='M58 94 a44 44 0 0 1 0 -72'/><path d='M72 104 a58 58 0 0 1 0 -92'/></g>"
                  "<circle cx='22' cy='58' r='6' fill='#fff' fill-opacity='.25'/>"),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# Keep the hub's language on the target site. Each site's root otherwise picks
# a language from the browser (or its own saved choice), so a Korean-language
# browser landed on Korean pages even from the English hub.
SPLIT = {"ahp", "kmc", "cmm", "pcm", "skm", "ppm", "bph", "mjm"}  # ko/ and en/ folders
QUERY = {"aih", "ans"}  # one page per language switch; honour ?lang=


def entry(p, lang):
    if p["key"] in SPLIT:
        return f"{p['site']}{lang}/index.html"
    if p["key"] in QUERY:
        return f"{p['site']}?lang={lang}"
    return p["site"]


def link(p, path, lang):
    url = path if path.startswith("https://") else p["site"] + path
    if p["key"] == "ans":
        url += f"?lang={lang}"
    return url


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
    h.append(f"<div class='links'><a class='btn primary' href='{entry(p, lang)}'>{T['site']} <span class='ar'>→</span></a><a class='btn' href='{p['repo']}'>{T['repo']} (GitHub)</a></div>")
    h.append("</div><div class='side'>")
    h.append(f"<p class='h'>{esc(T['contents'])}</p>")
    h.append("<ul class='items'>" + "".join(f"<li><a href='{link(p, path, lang)}'><b>{esc(a)}</b><small>{esc(b)}</small></a></li>" for a, b, path in t["items"]) + "</ul>")
    if t["extra"]:
        k, a, b, path = t["extra"]
        h.append(f"<p class='extra'><span class='tag'>{esc(k)}</span> <a href='{link(p, path, lang)}'><b>{esc(a)}</b></a> — {esc(b)}</p>")
    h.append("</div></section>")
    return "\n".join(h)


def page(lang):
    T = TEXT[lang]
    nav = "".join(f"<a href='{h}'>{esc(l)}</a>" for h, l in T["nav"])
    projs = "\n".join(project(p, i + 1, lang) for i, p in enumerate(PROJECTS))
    chips = "".join(f"<a class='chip' href='#{p['key']}' style='--c:var(--{p['color']})'><i></i>{esc(p[lang]['title'])}</a>" for p in PROJECTS)
    def tile(p):
        slot = SLOT[p["key"]]
        size = slot[0]
        fact, label = p[lang]["facts"][0]
        text = esc(p[lang]["title"]) if size == "S" else f"{esc(label)} · {esc(p[lang]['title'])}"
        return (f"<a class='sz-{size}' href='#{p['key']}' title='{esc(label)} · {esc(p[lang]['title'])}' "
                f"style='grid-area:{slot};--c:var(--{p['color']});--motif:{MOTIF[KIND[p['key']]]}'><span class='n'>{esc(fact)}</span><small>{text}</small></a>")
    mosaic = "".join(tile(p) for p in PROJECTS)
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
<div class="hero"><div><div class="who">{esc(T['lab'])}</div><h1>{esc(T['hero'])}</h1><p class="lead">{esc(T['hero_lead'])}</p>
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
