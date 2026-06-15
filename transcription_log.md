/Users/cormac/opt/anaconda3/envs/ogcogo/lib/python3.10/site-packages/requests/__init__.py:109: RequestsDependencyWarning: urllib3 (1.26.9) or chardet (7.3.0)/charset_normalizer (2.1.0) doesn't match a supported version!
  warnings.warn(
# Pre-processing rules


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%            pre-processing rules               %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% Initial inventory
%
% stops: p, pp, t, tt, c, cc
% stops/fricatives: b, bb, d, dd, g, gg, m, mm
% fricatives: f, ph, th, ch, s, h, ṡ
% sonorants: n, nn, ŋ, l, ll, r, rr
% other: ḟ
% vowels: a, e, i, o, u, á, é, í, ó, ú, ä, ë, ï, ö, ü
% symbols: -, ·, :, /s, ᴸ, ᴺ, ᴴ
%
%%%%%%%%%%%%%%%    Fortis segments written with singleton consonants     %%%%%%%%%%%%%%%
%
% Most frequently fortis segments, e.g. /p t k b d g m ɴ ŋ ʟ ʀ/ are written with double consonants in the normalised orthography,
% e.g. /t/ is written <tt>, /m/ is written <mm>.
% However, there are some exceptions, where the normalised orthography follows convention and writes these with single consonants.
% e.g. /t/ is written <t> in tech, but <tt> in catt.
%
% The following rules rewrite single consonants as double ones in these environemnts.
% e.g. intial /t/ is rewritten from <t> to <tt>, e.g. tech -> ttech.
%
% This makes it easier to convert to phonological representations
%
% The two contexts of these exceptions are 1) initially, and 2) in clusters.
%
% Rule 1 covers initial context, Rule 2 clusters.
%
%%%% 1. Doubling in initial position
%
% This rule targets fortis segments in initial, non-mutated, position.
% Outside of initial position, these segments are written double, e.g. /t/ is written <t> in tech, but <tt> in catt.
% This rule doubles the spelling.
%
% Three contexts are relevant here: i) absolute initial position, ii) after the mid-dot, iii) after non-mutated whitespace.
%
% e.g.
% i) 	gairid -> ggairid
% ii)	as·beir -> as·bbeir
% iii)	as·beir cormmacc -> as·bbeir ccormmac
%
0 -> p / (?=^|·|[^ᴸᴺᴴ]/s)p _
Sample of maximum 20 input/output pairs:

	peccad -> ppeccad
	peccad -> ppeccad
	peccthach -> ppeccthach
	peccthach -> ppeccthach
	pendait -> ppendait
	pendait -> ppendait
	persan -> ppersan
	persa -> ppersa
	pían -> ppían
	popul -> ppopul
	preicept -> ppreicept
	preiciupt -> ppreiciupt
	preiceupt -> ppreiceupt
	preiceptóir -> ppreiceptóir
	prímit -> pprímit
	praind -> ppraind


0 -> t / (?=^|·|[^ᴸᴺᴴ]/s)t _
Sample of maximum 20 input/output pairs:

	tabairt -> ttabairt
	tabart -> ttabart
	taidbsiu -> ttaidbsiu
	taidchor -> ttaidchor
	taidchrecc -> ttaidchrecc
	taidchricc -> ttaidchricc
	tairchomracc -> ttairchomracc
	táirggiud -> ttáirggiud
	tairisem -> ttairisem
	tairmmthecht -> ttairmmthecht
	tairṅgire -> ttairṅgire
	talam -> ttalam
	tathaír -> ttathaír
	taig -> ttaig
	tech -> ttech
	teg -> tteg
	techt -> ttecht
	techtaire -> ttechtaire
	techtairecht -> ttechtairecht
	tecmmallad -> ttecmmallad


0 -> c / (?=^|·|[^ᴸᴺᴴ]/s)c _
Sample of maximum 20 input/output pairs:

	caín-chomracc -> ccaín-chomracc
	caín-dúthracht -> ccaín-dúthracht
	caín-gníom -> ccaín-gníom
	caín-scél -> ccaín-scél
	caindléoir -> ccaindléoir
	caiṅgen -> ccaiṅgen
	carae -> ccarae
	caratrad -> ccaratrad
	carcar -> ccarcar
	cath -> ccath
	caithir -> ccaithir
	cathair -> ccathair
	céile -> ccéile
	céilide -> ccéilide
	ceinél -> cceinél
	ceinél -> cceinél
	ceinélae -> cceinélae
	ceist -> cceist
	cenn -> ccenn
	censae -> ccensae


0 -> b / (?=^|·|[^ᴸᴺᴴ]/s)b _
Sample of maximum 20 input/output pairs:

	baë -> bbaë
	bág -> bbág
	bairgen -> bbairgen
	baithes -> bbaithes
	baithis -> bbaithis
	bathais -> bbathais
	ball -> bball
	bás -> bbás
	béimm -> bbéimm
	bél -> bbél
	bélrae -> bbélrae
	ben -> bben
	bendacht -> bbendacht
	bendacht -> bbendacht
	béo -> bbéo
	bés -> bbés
	bésad -> bbésad
	béscnae -> bbéscnae
	béstatu -> bbéstatu
	bethu -> bbethu


0 -> d / (?=^|·|[^ᴸᴺᴴ]/s)d _
Sample of maximum 20 input/output pairs:

	dag-doíni -> ddag-doíni
	dag-duine -> ddag-duine
	dag-gníom -> ddag-gníom
	daltae -> ddaltae
	dam -> ddam
	dán -> ddán
	dé-ṡerc -> ddé-ṡerc
	deächt -> ddeächt
	deäd -> ddeäd
	deäd -> ddeäd
	díad -> ddíad
	debuith -> ddebuith
	dechor -> ddechor
	déicsiu -> ddéicsiu
	déide -> ddéide
	deimnigiud -> ddeimnigiud
	deimnigud -> ddeimnigud
	deiscipul -> ddeiscipul
	deisimmrecht -> ddeisimmrecht
	deismrecht -> ddeismrecht


0 -> g / (?=^|·|[^ᴸᴺᴴ]/s)g _
Sample of maximum 20 input/output pairs:

	gabáil -> ggabáil
	gabál -> ggabál
	gairdde -> ggairdde
	galar -> ggalar
	galar -> ggalar
	gáu -> ggáu
	gein -> ggein
	geinti -> ggeinti
	geintlide -> ggeintlide
	gell -> ggell
	genas -> ggenas
	giun -> ggiun
	glúas -> gglúas
	gnás -> ggnás
	gníom -> ggníom
	gnúis -> ggnúis
	goire -> ggoire
	gortae -> ggortae
	grád -> ggrád
	gráinne -> ggráinne


0 -> m / (?=^|·|[^ᴸᴺᴴ]/s)m _
Sample of maximum 20 input/output pairs:

	maäm -> mmaäm
	mám -> mmám
	macc -> mmacc
	machthad -> mmachthad
	maigister -> mmaigister
	martrae -> mmartrae
	mebul -> mmebul
	meirtrech -> mmeirtrech
	méit -> mméit
	mét -> mmét
	menmmae -> mmenmmae
	mes -> mmes
	míl -> mmíl
	míle -> mmíle
	mílte -> mmílte
	miscuis -> mmiscuis
	mod -> mmod
	maín -> mmaín
	moídem -> mmoídem
	molad -> mmolad


0 -> n / (?=^|·|[^ᴸᴺᴴ]/s)n _
Sample of maximum 20 input/output pairs:

	neb-buith -> nneb-buith
	neb-chomalnad -> nneb-chomalnad
	neb-martu -> nneb-martu
	neb-thabart -> nneb-thabart
	nem -> nnem
	nert -> nnert
	nertad -> nnertad
	nochtae -> nnochtae
	nóebad -> nnóebad
	nú-ḟíadnaise -> nnú-ḟíadnaise


0 -> l / (?=^|·|[^ᴸᴺᴴ]/s)l _
Sample of maximum 20 input/output pairs:

	labrad -> llabrad
	laë -> llaë
	lá -> llá
	laithe -> llaithe
	lám -> llám
	láine -> lláine
	lánae -> llánae
	lánamnas -> llánamnas
	lann -> llann
	láthar -> lláthar
	láthar -> lláthar
	legad -> llegad
	léigend -> lléigend
	léire -> lléire
	les -> lles
	lestar -> llestar
	leth -> lleth
	leth -> lleth
	lí -> llí
	liï -> lliï


0 -> r / (?=^|·|[^ᴸᴺᴴ]/s)r _
Sample of maximum 20 input/output pairs:

	rann -> rrann
	rath -> rrath
	recht -> rrecht
	ré -> rré
	reë -> rreë
	reë -> rreë
	rélad -> rrélad
	réit -> rréit
	rét -> rrét
	rí -> rrí
	ríar -> rríar
	ríchtu -> rríchtu
	riuth -> rriuth
	rosc -> rrosc
	rosc -> rrosc
	ruccae -> rruccae
	ruccae -> rruccae
	rún -> rrún


%%%% 2. Doubling in clusters
%
%%%% 2a. Doubling of <p t c>
%
% In the normalised orthography, /p t k/ are written singleton <p t c> in the following clusters:
%
% i) after <s>,
% ii) after a homorganic nasal,
% ii) after a sonorant <l> or <r>,
% iv) after <ch> (<t> only)
% v) in the infrequent clusters <pt> and <ct>, occurring in Latin loans, which we assume to stand for /pt/ and /kt/.
%
% e.g.
% i)    stair 	-> sttair
%	    scél 	-> sccél
% ii)	sacart 	-> sacartt
% iii) 	sant 	-> santt
% iv)	secht   -> sechtt
%
0 -> p / [slrm] _ (?=p([^h]|#))
Sample of maximum 20 input/output pairs:

	ccorp -> ccorpp
	ccorp -> ccorpp
	espoc -> esppoc
	spirut -> sppirut
	spirut -> sppirut
	spiurt -> sppiurt
	ttempul -> ttemppul


0 -> t / [slrnh] _ (?=t([^h]|#))
Sample of maximum 20 input/output pairs:

	adaltras -> adalttras
	aidpart -> aidpartt
	erchisecht -> erchisechtt
	altóir -> alttóir
	altramm -> alttramm
	apstal -> apsttal
	apstalacht -> apsttalachtt
	apstanait -> apsttanait
	apstainit -> apsttainit
	aipstinait -> aipsttinait
	astud -> asttud
	bbendacht -> bbendachtt
	bbendacht -> bbendachtt
	bbéstatu -> bbésttatu
	bbreithemnacht -> bbreithemnachtt
	bbrithemnacht -> bbrithemnachtt
	ccaín-dúthracht -> ccaín-dúthrachtt
	cceist -> cceistt
	ccomairbert -> ccomairbertt
	ccoimitecht -> ccoimitechtt


0 -> c / [slrn] _ (?=c([^h]|#))
Sample of maximum 20 input/output pairs:

	aincride -> ainccride
	aircor -> airccor
	ascnam -> asccnam
	bbéscnae -> bbésccnae
	ccaín-scél -> ccaín-sccél
	ccarcar -> ccarccar
	ccosc -> ccoscc
	ccoscrad -> ccosccrad
	ccumscugud -> ccumsccugud
	ddé-ṡerc -> ddé-ṡercc
	ddeiscipul -> ddeisccipul
	écosc -> écoscc
	epscop -> epsccop
	etarcertt -> etarccertt
	etircertt -> etirccertt
	etercertt -> eterccertt
	etarscarad -> etarsccarad
	foircenn -> foirccenn
	forcan -> forccan
	foircital -> foirccital


0 -> t / [pc] _ (?=t([^h]|#))
Sample of maximum 20 input/output pairs:

	eixceptaid -> eixcepttaid
	ppreicept -> ppreiceptt
	ppreiciupt -> ppreiciuptt
	ppreiceupt -> ppreiceuptt
	ppreiceptóir -> ppreicepttóir


0 -> p / p _ (?=t([^h]|#))
Sample of maximum 20 input/output pairs:

	eixcepttaid -> eixceppttaid
	ppreiceptt -> ppreicepptt
	ppreiciuptt -> ppreiciupptt
	ppreiceuptt -> ppreiceupptt
	ppreicepttóir -> ppreiceppttóir


%%%% 2b. Doubling of <b d g>
%
% In clusters, /b d g/ are normally written as <bb dd gg>.
% An exception is after homorganic nasals, where they are written singleton <b d g>.
%
0 -> b / m _ b
Sample of maximum 20 input/output pairs:

	ccimbid -> ccimbbid
	imbad -> imbbad
	imbed -> imbbed
	imbresan -> imbbresan


0 -> d / n _ d
Sample of maximum 20 input/output pairs:

	aisndís -> aisnddís
	aisndís -> aisnddís
	aisndéis -> aisnddéis
	bbendachtt -> bbenddachtt
	bbendachtt -> bbenddachtt
	ccaindléoir -> ccainddléoir
	ccland -> cclandd
	ccondairggile -> cconddairggile
	ccuindrech -> ccuinddrech
	ccundubartt -> ccunddubartt
	écndach -> écnddach
	forband -> forbandd
	indarbbae -> inddarbbae
	indas -> inddas
	indeb -> inddeb
	indírge -> inddírge
	indnaide -> inddnaide
	indocbál -> inddocbál
	lléigend -> lléigendd
	ppendait -> ppenddait


0 -> g / ṅ _ g
Sample of maximum 20 input/output pairs:

	aiṅgel -> aiṅggel
	ccaiṅgen -> ccaiṅggen
	ccumaṅg -> ccumaṅgg
	forṅgaire -> forṅggaire
	fulaṅg -> fulaṅgg
	ttairṅgire -> ttairṅggire


%%%% 2c. Doubling of nasals
%
% Before homorganic obstruents, /m/, /ɴ/, and /ŋ/ are written <m>, <n>, <ṅ> respectively (see rule 2b).
% This rule rewrites them as <mm>, <nn>, and <ŋ>.
% e.g.
%	cimbid  ->  cimmbbid
%   indas   ->  innddas
%   senchas ->  seŋchas
%
% While /m/ is usually written <mm> it is written <m> initially after <s> (cf. Rule 2a(i)).
% This rule rewrites it <mm>.
% e.g. smacht   ->  smmacht
%
0 -> m / m _ (?=(p|b)([^h]|#))
Sample of maximum 20 input/output pairs:

	ccimbbid -> ccimmbbid
	imbbad -> immbbad
	imbbed -> immbbed
	imbbresan -> immbbresan
	ttemppul -> ttemmppul


0 -> n / n _ (?=(t|d|s)([^h]|#))
Sample of maximum 20 input/output pairs:

	áinsem -> áinnsem
	aisnddís -> aisnnddís
	aisnddís -> aisnnddís
	aisnddéis -> aisnnddéis
	bbenddachtt -> bbennddachtt
	bbenddachtt -> bbennddachtt
	ccainddléoir -> ccainnddléoir
	ccensae -> ccennsae
	cclandd -> cclanndd
	cconddairggile -> cconnddairggile
	ccoraintte -> ccorainntte
	ccuinddrech -> ccuinnddrech
	ccunddubartt -> ccunnddubartt
	ccunttubartt -> ccunnttubartt
	écnddach -> écnnddach
	forbandd -> forbanndd
	ggeintti -> ggeinntti
	ggeinttlide -> ggeinnttlide
	inddarbbae -> innddarbbae
	inddas -> innddas


0 -> m / (?=^|·|[^ᴸᴺᴴ]/s)[s] _ m
Sample of maximum 20 input/output pairs:

	smachtt -> smmachtt


%%%% 2d. Doubling of <l r>
%
% In clusters before a coronal stop or nasal, /ʟ/ and /ʀ/ are written <l> and <r>
% This rule doubles them to <ll> and <rr>, respectively.
%
% e.g.
%   daltae  ->  dallttae
%   fiurt   ->  fiurrtt
%
% 0 -> l / l _ (?=(t|d|s|n)([^h]|#))
% 0 -> r / r _ (?=(t|d|s|n)([^h]|#))
0 -> l / _ l[tdsn]
Sample of maximum 20 input/output pairs:

	acalddam -> acallddam
	adalttras -> adallttras
	alttóir -> allttóir
	alttramm -> allttramm
	ccoicéilsine -> ccoicéillsine
	ccomalnad -> ccomallnad
	ddalttae -> ddallttae
	ddílttud -> ddíllttud
	ddoguilse -> ddoguillse
	éilned -> éillned
	apalttu -> apallttu
	eipelttu -> eipellttu
	eipilttiu -> eipillttiu
	fáiltte -> fáilltte
	fellsam -> felllsam
	felsub -> fellsub
	foilsigud -> foillsigud
	incholnugud -> inchollnugud
	mmíltte -> mmílltte
	nneb-chomalnad -> nneb-chomallnad


0 -> r / _ r[tsn]
Sample of maximum 20 input/output pairs:

	aidpartt -> aidparrtt
	airnaigde -> airrnaigde
	ccomairbertt -> ccomairberrtt
	ccúairtt -> ccúairrtt
	ccumdubartt -> ccumdubarrtt
	ccumtubartt -> ccumtubarrtt
	ccunnddubartt -> ccunnddubarrtt
	ccunnttubartt -> ccunnttubarrtt
	ccúrsagad -> ccúrrsagad
	ccúrsagad -> ccúrrsagad
	eipertt -> eiperrtt
	erbertt -> erberrtt
	etarccertt -> etarccerrtt
	etirccertt -> etirccerrtt
	eterccertt -> eterccerrtt
	etarsccarad -> etarrsccarad
	fiurtt -> fiurrtt
	forṅggaire -> forrṅggaire
	forttachtt -> forrttachtt
	forttachtt -> forrttachtt


%%%%%%%%%%%%%%%    Rare clusters     %%%%%%%%%%%%%%%
%
% The following rules capture a number of conventions in the normalised orthography.
%
%%%% 3. ṅ
%
% ref: GOI §24, §33.1, §236
%
% <ṅ> is used in two contexts:
% i) in the combination <ṅg>, representing /ŋ/, distinguished from <ng> representing /nɣ/
% ii) initially, for the nasalisation of a vowel-initial word
%
% e.g.
% i)	iṅgen  -> iŋen 	('nail')
%	    ingen 		('daughter')
% ii) 	aᴺathair = aṅathair -> annathair
%
ṅ -> ŋ / _ g
Sample of maximum 20 input/output pairs:

	aiṅggel -> aiŋggel
	ccaiṅggen -> ccaiŋggen
	ccumaṅgg -> ccumaŋgg
	forrṅggaire -> forrŋggaire
	fulaṅgg -> fulaŋgg
	ttairrṅggire -> ttairrŋggire


%%%% 4. Orthographic x is xs
%
% ref: GOI §24.5
%
% Quite rare, <x> is equivalent to <xs>
%
% e.g.
%	exceptaid -> exsceptaid
%
0 -> s / x _
Sample of maximum 20 input/output pairs:

	eixceppttaid -> eixsceppttaid


%%%% 6. Orthographic bḟ is b
%
% In the normalised orthography <bḟ> occurs from the nasalisation of <f>.
% It patterns with <b>.
%
% e.g.
%	innaᴺfer = innabḟer -> innaber (gen.pl of fer 'man')
%
ḟ -> 0 / b _
Sample of maximum 20 input/output pairs:

	ccobḟodlus -> ccobodlus


%%%%%%%%%%%%%%%    Orthography of vowels in hiatus     %%%%%%%%%%%%%%%
%%%% 7. Syllable break for vowels in hiatus
%
% The second of two vowels in hiatus is usually written with a diaeresis in scholarly orthography of Old Irish.
% The normalised orthography follows this convention. However, the syllable break <.> is more common and appropriate in phonological representations.
%
% e.g. laë -> la.e, deäd -> de.ad
%
ä -> .a / _
Sample of maximum 20 input/output pairs:

	aiär -> ai.ar
	aiär -> ai.ar
	bbiäd -> bbi.ad
	ddeächtt -> dde.achtt
	ddeäd -> dde.ad
	ddeäd -> dde.ad
	ddeä -> dde.a
	ddiäs -> ddi.as
	ddiäs -> ddi.as
	mmaäm -> mma.am
	ttriär -> ttri.ar


ë -> .e / _
Sample of maximum 20 input/output pairs:

	bbaë -> bba.e
	ddië -> ddi.e
	llaë -> lla.e
	llië -> lli.e
	llië -> lli.e
	rreë -> rre.e
	rreë -> rre.e
	sain-laë -> sain-la.e


ï -> .i / _
Sample of maximum 20 input/output pairs:

	ddruiï -> ddrui.i
	lliï -> lli.i


ü -> .u / _
Sample of maximum 20 input/output pairs:

	ddiü -> ddi.u


# Post-processing rules


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%            post-processing rules               %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%
%%%% Inventory after mapping
%%%%
%
% stops: p, t, c, b, d, g
% fricatives: ɸ, θ, x, β, ð, ɣ, s, h
% sonorants: m, μ, ɴ, n, ŋ, ʟ, l, ʀ, r
% other: Ø
% vowels: a, e, i, o, u, A, E, I, O, U
% symbols: -, ·, :, /., \s, ᴸ, ᴺ, ᴴ
%
%%%%%%%%%%%%%%%    Shorthands     %%%%%%%%%%%%%%%
%
%%%% 1. Shorthands
%
% We use two shorthands for readability and brevity in the rules.
%
% 1i. Defines the class of vowels. Capital <I, U, E, O, A> stand for
% long <í ú é ó á> in the normalised orthography.
%
% 1ii. Defines the class of consonants (omitting the zero consonant Ø).
%
%%%% 1i. Defining the class of vowels
%
%%%% 1ii. Defining the class of consonants
%
%%%%%%%%%%%%%%%     Boundary markers and stress     %%%%%%%%%%%%%%%
%
% The normalised orthography permits the following boundary markers:
% <-, ·, :, ᴸ, ᴺ, ᴴ, \s (whitespace)> In addition, we use here
% </. (full stop)>, separating hiatus vowels. Descriptions follow.
%
% 1) Three mutation markers <ᴸ, ᴺ, ᴴ>, preceding a stressed syllable. A following consonant following is parsed as radical (phrase-initial).
% The following contexts occur:
% a) Without another marker: preceding a stressed syllable, after an unstressed constitutent.
% e.g. aᴸcatt 'his cat'; aᴺcatt 'their cat'
% b) With whitespace: preceding a stressed syllable, after a stressed constitutent.
% e.g. Cúᴸ Culainn
% c) With the hyphen: preceding a stressed syllable, after a stressed constitutent.
% e.g. senᴸ-máthair
% A further operation can resolve these to phonological forms
% e.g. a̟ᴸcatt -> a:chatt 'his cat'; aᴺcatt -> a:catt 'their cat'; Cúᴸ Culainn -> Cú Chulainn; sen-máthair
%
% 2) The mid-dot <·>, preceding a stressed syllable, after an unstressed constitutent. A following consonant following is parsed as radical (phrase-initial).
% e.g. as·beir 'says'
%
% 3) The colon <:>, preceding a stressed syllable, after an unstressed constitutent. A following consonant following has its ordinary contextual value.
% e.g. a:chatt 'his cat'; a:ccatt 'her cat'; a:catt 'their cat'
%
% 4) The hyphen <->, preceding a stressed syllable, after a stressed constitutent (see note). A following consonant following has its ordinary contextual value.
% e.g. sen-máthair ~ senᴸ-máthair 'grandmother'
%
% 5) The equals sign <=>, preceding an unstressed syllable. Used before one of the closed class of notae augentes and immediately followed by whitespace.
% e.g. ad·cobra=som 'he desires'
%
% 6) Whitespace < \s (whitespace)>. Used before a new stress group,
% outside of close compounds (where the hyphen is used)
%
%%%% 2. Stress assignment
%
% Stress can be assigned in the following contexts:
% i) After a mutation marker, optionally followed by whitespace
% ii) After the mid-dot, colon, or hyphen
% iii) After whitespace, except when the following string contains a mutation marker, a mid-dot, or a colon
% iv) Initially on the line
%
0 -> ˈ / ([ᴸᴺᴴ]\s?)|[·:-]|\s(?![^\s]+[·:])|# _
Sample of maximum 20 input/output pairs:

	agaʟdaμ -> ˈagaʟdaμ
	akoβor -> ˈakoβor
	akoμol -> ˈakoμol
	aðaiɣ -> ˈaðaiɣ
	aðaʟtras -> ˈaðaʟtras
	aðβar -> ˈaðβar
	aðnagul -> ˈaðnagul
	aðrað -> ˈaðrað
	Aes -> ˈAes
	Aes -> ˈAes
	ai.ar -> ˈai.ar
	ai.ar -> ˈai.ar
	Aixθiu -> ˈAixθiu
	aigneð -> ˈaigneð
	aiðbaʀt -> ˈaiðbaʀt
	ail -> ˈail
	ail -> ˈail
	Ail -> ˈAil
	aiʟe -> ˈaiʟe
	aimser -> ˈaimser


0 -> u / (^|\s)ˈi _ l-
Sample of maximum 20 input/output pairs:

	ˈil-ˈβaiʟ -> ˈiul-ˈβaiʟ
	ˈil-ˈβEim -> ˈiul-ˈβEim
	ˈil-ˈβElrae -> ˈiul-ˈβElrae


%%%% 4. Prepositional elements
%
% It is unclear the extent to which prepositional elements assimilate in colour to a following element.
% The following policy is adopted here:
% 1) For imm-, ind-, and frith-, we assume assimilation to following i-colour and u-colour, but not to a-colour.
% 2) For com- we assume assimilation to following u-colour and a-colour, but not to i-colour (unless the orthography indicates otherwise.
% 3) For etar-, we do not assume assimilation to following i-colour or u-colour. With etir-, we do not assume assimilation to following u-colour or a-colour.
% 4) For air-/er- we assume assimilation to following i-colour and u-colour but not a-colour (cf. Rule 6)
% 5) For aid- we assume assimilation only to following i-colour
%
% As this is a closed class, we fully specify these elements here and protect them from the ensuing sound changes
%
% ad etc.
ˈaið -> ˈØˠəðʷ! / _ ::C::*[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈaiðbaʀt -> ˈØˠəðʷ!baʀt


ˈtaið -> ˈtˠəðʲ! / _ ::C::*[eiEI]
Sample of maximum 20 input/output pairs:

	ˈtaiðβsiu -> ˈtˠəðʲ!βsiu
	ˈtaiðxrek -> ˈtˠəðʲ!xrek
	ˈtaiðxrik -> ˈtˠəðʲ!xrik


% ar etc.
ˈair -> ˈØˠərʷ! / _ ::C::*[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈairAil -> ˈØˠərʷ!Ail
	ˈairβAɣ -> ˈØˠərʷ!βAɣ
	ˈairxrae -> ˈØˠərʷ!xrae
	ˈairkor -> ˈØˠərʷ!kor
	ˈairɣaire -> ˈØˠərʷ!ɣaire
	ˈairɣal -> ˈØˠərʷ!ɣal
	ˈairladu -> ˈØˠərʷ!ladu
	ˈairOgrae -> ˈØˠərʷ!Ograe


ˈer -> ˈØˠərʲ! / _ ::C::*[eiEI]
Sample of maximum 20 input/output pairs:

	ˈerxiɴex -> ˈØˠərʲ!xiɴex
	ˈerxisext -> ˈØˠərʲ!xisext
	ˈeridiu -> ˈØˠərʲ!idiu
	ˈerliguð -> ˈØˠərʲ!liguð
	ˈerμidiu -> ˈØˠərʲ!μidiu
	ˈerβeʀt -> ˈØˠərʲ!βeʀt
	ˈere -> ˈØˠərʲ!e
	ˈeres -> ˈØˠərʲ!es
	ˈeres -> ˈØˠərʲ!es
	ˈeresxae -> ˈØˠərʲ!esxae


ˈtair -> ˈtˠərʷ! / _ ::C::*[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈtairxoμrak -> ˈtˠərʷ!xoμrak


% com- etc.
ˈkoμ -> ˈkʷaμʷ! / _ ::C::*[ouOU]
Sample of maximum 20 input/output pairs:

	ˈkoμrorgon -> ˈkʷaμʷ!rorgon


ˈkoμ -> ˈkʷaμˠ! / _ ::C::*[aeiAEI]
Sample of maximum 20 input/output pairs:

	ˈkoμakoβor -> ˈkʷaμˠ!akoβor
	ˈkoμairβeʀt -> ˈkʷaμˠ!airβeʀt
	ˈkoμairle -> ˈkʷaμˠ!airle
	ˈkoμaidext -> ˈkʷaμˠ!aidext
	ˈkoμaʟnað -> ˈkʷaμˠ!aʟnað
	ˈkoμarbus -> ˈkʷaμˠ!arbus
	ˈkoμarðae -> ˈkʷaμˠ!arðae
	ˈkoμnesaμ -> ˈkʷaμˠ!nesaμ
	ˈkoμθinOl -> ˈkʷaμˠ!θinOl


% edar- etc.
ˈedar -> ˈØʲadˠarˠ! / _
Sample of maximum 20 input/output pairs:

	ˈedarkeʀt -> ˈØʲadˠarˠ!keʀt
	ˈedardiβe -> ˈØʲadˠarˠ!diβe
	ˈedargnae -> ˈØʲadˠarˠ!gnae


ˈedir -> ˈØʲadʲərʲ! / _
Sample of maximum 20 input/output pairs:

	ˈedirkeʀt -> ˈØʲadʲərʲ!keʀt


ˈeder -> ˈØʲadʲarʲ! / _
Sample of maximum 20 input/output pairs:

	ˈederkeʀt -> ˈØʲadʲarʲ!keʀt


% frith etc.
ˈɸriθ -> ˈɸʲrʲəθʷ! / _ ::C::*[ouOU]
Sample of maximum 20 input/output pairs:

	ˈɸriθorgon -> ˈɸʲrʲəθʷ!orgon


% imm- etc.
ˈim -> ˈØʲəmʲ! / _ ::C::*[eiEI]
Sample of maximum 20 input/output pairs:

	ˈimbeð -> ˈØʲəmʲ!beð
	ˈimbresan -> ˈØʲəmʲ!bresan
	ˈimxist -> ˈØʲəmʲ!xist
	ˈimðiβe -> ˈØʲəmʲ!ðiβe
	ˈimneð -> ˈØʲəmʲ!neð
	ˈimθext -> ˈØʲəmʲ!θext
	ˈimθrEnuɣuð -> ˈØʲəmʲ!θrEnuɣuð


ˈim -> ˈØʲəmʷ! / _ ::C::*[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈimbað -> ˈØʲəmʷ!bað
	ˈimarμus -> ˈØʲəmʷ!arμus
	ˈimxoμark -> ˈØʲəmʷ!xoμark
	ˈimxoμrag -> ˈØʲəmʷ!xoμrag
	ˈimoɣaiβedu -> ˈØʲəmʷ!oɣaiβedu
	ˈimrAðuð -> ˈØʲəmʷ!rAðuð
	ˈimrOl -> ˈØʲəmʷ!rOl
	ˈimθAnað -> ˈØʲəmʷ!θAnað
	ˈimθAnuð -> ˈØʲəmʷ!θAnuð
	ˈimθuɣae -> ˈØʲəmʷ!θuɣae


% ind- etc.
ˈiɴd -> ˈØʲəɴʲdʲ! / _ ::C::*[eiEI]
Sample of maximum 20 input/output pairs:

	ˈiɴdeβ -> ˈØʲəɴʲdʲ!eβ
	ˈiɴdIrɣe -> ˈØʲəɴʲdʲ!Irɣe


ˈiɴd -> ˈØʲəɴʷdʷ! / _ ::C::*[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈiɴdarbae -> ˈØʲəɴʷdʷ!arbae
	ˈiɴdas -> ˈØʲəɴʷdʷ!as
	ˈiɴdnaiðe -> ˈØʲəɴʷdʷ!naiðe
	ˈiɴdogβAl -> ˈØʲəɴʷdʷ!ogβAl


%%%%%%%%%%%%%%%     Rewriting vowels before colour assignment     %%%%%%%%%%%%%%%
%
% Vowels in Old Irish have a dual function of indicating vowel quality and marking consonant colour.
% The following rules rewrite vowels before consonant colour assignment.
%
%%%%
%%%% Source and target vowel inventories
%%%%
%
% short vowels: a, ai, au; e, ei, eu; o, oi; i, iu; u, ui; əi, əu
% target:
% aa, ai, au
% ea, ei, eu
% oa, oi, ou
% əu, əi
% ii, iu
% uu, ui
%
%
% final vowels: a, ea; ae, e; o, eo; ai, i; u, iu
% target:
% aA, iA, uA
% aE, iE, uE
% aO, iO, uO
% aI, iI, uI
% aU, iU, uU
%
% long vowels: á, ái, ía, úa, úai; áe, aí, é, éi, óe, oí; áu, éo, éoi, ó, ói; ío, í, uí; íu, íui, ú, úi
% target:
% aA, aAa, aAi, aAu; iA, iAa, (iAi), iAu; uA, uAa, uAi, uAu
% aE, aEa, aEi, aEu; iE, iEa, iEi, iEu; uE, uEa, uEi, uEu
% aO, aOa, aOi, aOu; iO, iOa, iOi, iOu; uO, uOa, uOi, uOu
% aI, aIa, aIi, aIu; iI, iIa, iIi, iIu; uI, uIa, uIi, uIu
% aU, aUa, aUi, aUu; iU, iUa, iUi, iUu; uU, uUa, uUi, uUu
%
%
%%%% 5.  Assign Ø
%
% A vowel must be preceded by a colour marker [ˠʲʷ]. In the phonology, only a consonant can host a colour marker.
% This rule assigns a zero consonant to act as host, where no consonant precedes.
% There are two contexts in which this occurs:
% 1) Initially
% 2) After a prepositional element (see Rule 5)
%
0 -> Ø / [ˈ!] _ ::V::
Sample of maximum 20 input/output pairs:

	ˈagaʟdaμ -> ˈØagaʟdaμ
	ˈakoβor -> ˈØakoβor
	ˈakoμol -> ˈØakoμol
	ˈaðaiɣ -> ˈØaðaiɣ
	ˈaðaʟtras -> ˈØaðaʟtras
	ˈaðβar -> ˈØaðβar
	ˈaðnagul -> ˈØaðnagul
	ˈaðrað -> ˈØaðrað
	ˈAes -> ˈØAes
	ˈAes -> ˈØAes
	ˈai.ar -> ˈØai.ar
	ˈai.ar -> ˈØai.ar
	ˈAixθiu -> ˈØAixθiu
	ˈaigneð -> ˈØaigneð
	ˈail -> ˈØail
	ˈail -> ˈØail
	ˈAil -> ˈØAil
	ˈaiʟe -> ˈØaiʟe
	ˈaimser -> ˈØaimser
	ˈainkriðe -> ˈØainkriðe


%%%% 6. The obscure vowel ö
%
% The obscure vowel ö, 'for which the Irish script had no ambiguous symbol' (GOI §80) is spelled in the normalised orthography with
% <ai> before u-colour or a-colour, and with <e> before i-colour.
% This rarely occurs outside the prepositional element air-/er-, for which see Rule 4.
% For cases outside this environment we assume the representations /ˠəi/ before i-colour and /ˠəu/ before u-colour.
%
e -> ˠəi / _ ::C::+[eiEI]
Sample of maximum 20 input/output pairs:

	ˈØenex -> ˈØˠəinex


ai -> ˠəu / _ ::C::+[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈØaiʀnaiɣðe -> ˈØˠəuʀnaiɣðe
	ˈØainax -> ˈØˠəunax
	ˈtaiðxor -> ˈtˠəuðxor


au -> ˠəu / _ ::C::+[aouAOU]
Sample of maximum 20 input/output pairs:

	ˈØauɣdorðAs -> ˈØˠəuɣdorðAs


%%%% 7. Long vowels with initial fada
%
% The normalised orthography follows scholarly conventions with respect to placement of the fada.
% These rules rewrite these conventions to facilitate assignment of consonant colour.
% This is necessary at this point in the derivation so that Eoi and Uai do not interfere with the reassignment rules for short vowels.
%
Ae -> aE / _
Sample of maximum 20 input/output pairs:

	ˈØAes -> ˈØaEs
	ˈØAes -> ˈØaEs
	ˈsAeβ-ˈØabstal -> ˈsaEβ-ˈØabstal
	ˈsAeɣul -> ˈsaEɣul
	ˈsAeθ -> ˈsaEθ
	ˈsAeθar -> ˈsaEθar
	ˈsAeθar -> ˈsaEθar


aI -> aEi / _
Sample of maximum 20 input/output pairs:

	ˈØaIs -> ˈØaEis
	ˈkaIn-ˈxoμrak -> ˈkaEin-ˈxoμrak
	ˈkaIn-ˈðUθraxt -> ˈkaEin-ˈðUθraxt
	ˈkaIn-ˈɣnIoμ -> ˈkaEin-ˈɣnIoμ
	ˈkaIn-ˈskEl -> ˈkaEin-ˈskEl
	ˈkomaIn -> ˈkomaEin
	ˈmaIn -> ˈmaEin
	ˈtaθaIr -> ˈtaθaEir


Au -> aO / _
Sample of maximum 20 input/output pairs:

	ˈgAu -> ˈgaO


Eo -> iO / _
Sample of maximum 20 input/output pairs:

	ˈbEo -> ˈbiO
	ˈkaiɴdlEoir -> ˈkaiɴdliOir
	ˈdEolaðaxt -> ˈdiOlaðaxt


Oe -> uE / _
Sample of maximum 20 input/output pairs:

	ˈdOenaxt -> ˈduEnaxt
	ˈɴOeβað -> ˈɴuEβað
	ˈØOeɴtu -> ˈØuEɴtu
	ˈØOeɴtu -> ˈØuEɴtu
	ˈØOenur -> ˈØuEnur
	ˈsOerað -> ˈsuErað
	ˈtOeβ -> ˈtuEβ
	ˈtOeβ -> ˈtuEβ


oI -> uEi / _
Sample of maximum 20 input/output pairs:

	ˈkloIne -> ˈkluEine
	ˈdaɣ-ˈðoIni -> ˈdaɣ-ˈðuEini
	ˈderxoIniuð -> ˈderxuEiniuð
	ˈdoInext -> ˈduEinext
	ˈdoIre -> ˈduEire
	ˈdoIni -> ˈduEini
	ˈɸoIsidiu -> ˈɸuEisidiu
	ˈmoIðeμ -> ˈmuEiðeμ
	ˈØoIɣi -> ˈØuEiɣi
	ˈsoIre -> ˈsuEire
	ˈtoIniuð -> ˈtuEiniuð


Ia -> iA / _
Sample of maximum 20 input/output pairs:

	ˈbrIaθar -> ˈbriAθar
	ˈbrIaθar -> ˈbriAθar
	ˈkIaʟ -> ˈkiAʟ
	ˈdIað -> ˈdiAð
	ˈdIa -> ˈdiA
	ˈdIaβol -> ˈdiAβol
	ˈdIas -> ˈdiAs
	ˈɸIax -> ˈɸiAx
	ˈɸIaðnaise -> ˈɸiAðnaise
	ˈɸIor-ˈðIa -> ˈɸIor-ˈðiA
	ˈɸIrIanuɣuð -> ˈɸIriAnuɣuð
	ˈØIarɸaiɣið -> ˈØiArɸaiɣið
	ˈɴU-ˈØIaðnaise -> ˈɴU-ˈØiAðnaise
	ˈpIan -> ˈpiAn
	ˈʀIar -> ˈʀiAr
	ˈsIaɴs -> ˈsiAɴs


Iu -> iU / _
Sample of maximum 20 input/output pairs:

	ˈdIu -> ˈdiU
	ˈdIuite -> ˈdiUite
	ˈØIuðae -> ˈØiUðae
	ˈØIuðaiðe -> ˈØiUðaiðe


Ua -> uA / _
Sample of maximum 20 input/output pairs:

	ˈbUaið -> ˈbuAið
	ˈkUaiʀt -> ˈkuAiʀt
	ˈkUaird -> ˈkuAird
	ˈɸUagrae -> ˈɸuAgrae
	ˈɸUaθ -> ˈɸuAθ
	ˈglUas -> ˈgluAs
	ˈsUaineμ -> ˈsuAineμ
	ˈtUarae -> ˈtuArae
	ˈtUargun -> ˈtuArgun
	ˈtUaθ -> ˈtuAθ
	ˈØUaβar -> ˈØuAβar
	ˈØUaxt -> ˈØuAxt
	ˈØUailβe -> ˈØuAilβe
	ˈØUaʟ -> ˈØuAʟ
	ˈØUar -> ˈØuAr
	ˈØUaθað -> ˈØuAθað
	ˈØUaθað -> ˈØuAθað


Io -> Iu / _
Sample of maximum 20 input/output pairs:

	ˈkaEin-ˈɣnIoμ -> ˈkaEin-ˈɣnIuμ
	ˈdaɣ-ˈɣnIoμ -> ˈdaɣ-ˈɣnIuμ
	ˈdIoθ -> ˈdIuθ
	ˈdroɣ-ˈɣnIoμ -> ˈdroɣ-ˈɣnIuμ
	ˈɸIon -> ˈɸIun
	ˈɸIor-ˈðiA -> ˈɸIur-ˈðiA
	ˈgnIoμ -> ˈgnIuμ
	ˈØIok -> ˈØIuk
	ˈʟIon -> ˈʟIun
	ˈʟIon -> ˈʟIun
	ˈsIol -> ˈsIul


%%%% 8. a-colour and u-colour with short vowels
%
% The normalised orthography allows:
% i) <ai> not <ui> after <u> or <i>, the obscure vowel, ú or ío  e.g. cumtaig, foircitlaid
% ii) <a> for <o> between u-colour and a-colour consonants, when preceded by stressed <i> or <u>
% iii) <o> for <u> between u-colour and u-colour, when <o> follows
% iv) <u> for <au> after preceding <a>
%
% The normalised orthography writes stressed <a, e> before u-colour when <o, u> follows,
% so baull but ballu, neurt but nertu etc.
% Conventionally, <o> is written before u-colour both in monosylables and when <o, u> follows,
% so roth and rothu
%
% The normalised orthography writes <i> before u-colour when <o or u> follows in both
% stressed and unstressed syllables, so stressed fiur but firu, unstressed deimnigud
%
%
% 8i. 	ai -> ui: cumtaig -> cumtuig, utmaille -> utmuille, foircitlaid -> foircitluid, timmnae -> timmnue, airchrae -> Øˠəurchrue, iúdae -> iúdue
% 8ii. 	a -> oa: muntar -> muntoar, ilar -> iloar, foircital -> foircitoal, tindnaccul -> tindnoaccol, immarmus -> immoarmus, airlatu -> airloatu, múnad -> múnoad
% 8iii. o -> oa: accoubor -> accouboar, immḟogaibetu -> immḟoagaibetu, áugtordás -> áugtoardás, imchomracc -> imchoamracc, bolad -> boalad
% 8iv. 	u -> au: immoarmus -> immoarmaus, adnacul -> adnacaul, eipeltu -> eipeltau, béstatu -> béstatau
% 8v. 	o -> ou: cotlud -> coutlud, popul -> poupul, accobor -> accoubor, comaccobor -> comaccoubor
% 	i -> iu: deimnigiud -> deimniugud, immról -> iummról, foróil -> fouróil
%	a !-> au: omaldóit
%	e !-> eu: preiceptóir (not preiciuptóir)
%
% 8pre. o is u in final syllable
o -> u / [pkbgɸxβɣμmŋ] _ [ɴʟʀnlr](-|#)
Sample of maximum 20 input/output pairs:

	ˈØakoβor -> ˈØakoβur
	ˈØakoμol -> ˈØakoμul
	ˈØˠərʷ!kor -> ˈØˠərʷ!kur
	ˈkol -> ˈkul
	ˈkʷaμˠ!Øakoβor -> ˈkʷaμˠ!Øakoβur
	ˈkʷaμʷ!rorgon -> ˈkʷaμʷ!rorgun
	ˈkor -> ˈkur
	ˈdexor -> ˈdexur
	ˈdeμon -> ˈdeμun
	ˈdeμon -> ˈdeμun
	ˈdiAβol -> ˈdiAβul
	ˈØesorgon -> ˈØesorgun
	ˈØesorgon -> ˈØesorgun
	ˈɸoɣor -> ˈɸoɣur
	ˈɸregor -> ˈɸregur
	ˈɸʲrʲəθʷ!Øorgon -> ˈɸʲrʲəθʷ!Øorgun
	ˈØOμon -> ˈØOμun
	ˈØoμon -> ˈØoμun
	ˈtˠəuðxor -> ˈtˠəuðxur


% 8i.
%
a -> u / (::C::|Ø)+(ˠəu|[ui]|i?U|Iu)::C::+ _ (?=[ei])
Sample of maximum 20 input/output pairs:

	ˈØˠəuʀnaiɣðe -> ˈØˠəuʀnuiɣðe
	ˈØaibstinaid -> ˈØaibstinuid
	ˈburbae -> ˈburbue
	ˈkumae -> ˈkumue
	ˈɸoirkidlaið -> ˈɸoirkidluið
	ˈØʲəmʷ!θuɣae -> ˈØʲəmʷ!θuɣue
	ˈØinɣnae -> ˈØinɣnue
	ˈØinɣraim -> ˈØinɣruim
	ˈØinɣraim -> ˈØinɣruim
	ˈØiUðae -> ˈØiUðue
	ˈØiUðaiðe -> ˈØiUðuiðe
	ˈʟuɣae -> ˈʟuɣue
	ˈʀukae -> ˈʀukue
	ˈʀukae -> ˈʀukue
	ˈtimnae -> ˈtimnue


% 8ii.
%
0 -> o / (::C::|Ø)+(ˠəu|[ui]|U|Iu|iO)::C::+ _ (?=a::C::)
Sample of maximum 20 input/output pairs:

	ˈbunað -> ˈbunoað
	ˈkaEin-ˈðUθraxt -> ˈkaEin-ˈðUθroaxt
	ˈkuμaxtae -> ˈkuμoaxtae
	ˈkuμag -> ˈkuμoag
	ˈkuμaŋg -> ˈkuμoaŋg
	ˈkuμsanað -> ˈkuμsoanað
	ˈkuμdax -> ˈkuμdoax
	ˈkuμðuβaʀt -> ˈkuμðuβoaʀt
	ˈkuμduβaʀt -> ˈkuμduβoaʀt
	ˈkuɴduβaʀt -> ˈkuɴduβoaʀt
	ˈkuɴtuβaʀt -> ˈkuɴtuβoaʀt
	ˈkUʀsaɣað -> ˈkUʀsoaɣað
	ˈkUʀsaɣað -> ˈkUʀsoaɣað
	ˈdiOlaðaxt -> ˈdiOloaðaxt
	ˈdUθraxt -> ˈdUθroaxt
	ˈdUθraxt -> ˈdUθroaxt
	ˈØˠəunax -> ˈØˠəunoax
	ˈɸoirkidal -> ˈɸoirkidoal
	ˈɸuɣaʟ -> ˈɸuɣoaʟ
	ˈɸulax -> ˈɸuloax


% 8iii.
%
0 -> a / (::C::|Ø)o _ ::C::+([aA]|#)
Sample of maximum 20 input/output pairs:

	ˈØˠəuɣdorðAs -> ˈØˠəuɣdoarðAs
	ˈbolað -> ˈboalað
	ˈboθ -> ˈboaθ
	ˈboθ -> ˈboaθ
	ˈkaEin-ˈxoμrak -> ˈkaEin-ˈxoaμrak
	ˈkolaiɴ -> ˈkoalaiɴ
	ˈkomaEin -> ˈkoamaEin
	ˈkoɴdairgile -> ˈkoaɴdairgile
	ˈkoraiɴte -> ˈkoaraiɴte
	ˈkorp -> ˈkoarp
	ˈkorp -> ˈkoarp
	ˈkos -> ˈkoas
	ˈkosk -> ˈkoask
	ˈkoskrað -> ˈkoaskrað
	ˈkosnaμ -> ˈkoasnaμ
	ˈkrox -> ˈkroax
	ˈkrox -> ˈkroax
	ˈkroxað -> ˈkroaxað
	ˈkrot -> ˈkroat
	ˈdEnoμ -> ˈdEnoaμ


% 8iv.
%
0 -> a / (::V::|!)(::C::|Ø)+o?[ae]::C::+ _ u
Sample of maximum 20 input/output pairs:

	ˈØaðnagul -> ˈØaðnagaul
	ˈØˠərʷ!ladu -> ˈØˠərʷ!ladau
	ˈbEstadu -> ˈbEstadau
	ˈkʷaμˠ!Øarbus -> ˈkʷaμˠ!Øarbaus
	ˈØabaʟtu -> ˈØabaʟtau
	ˈØeibeʟtu -> ˈØeibeʟtau
	ˈɸoirβθedu -> ˈɸoirβθedau
	ˈØʲəmʷ!Øarμus -> ˈØʲəmʷ!Øarμaus
	ˈØʲəmʷ!Øoaɣaiβedu -> ˈØʲəmʷ!Øoaɣaiβedau
	ˈtiɴdnoakul -> ˈtiɴdnoakaul


% 8v.
%
0 -> u / (::C::|Ø)[oiu] _ (?=::C::+O)
Sample of maximum 20 input/output pairs:

	ˈkʷaμˠ!θinOl -> ˈkʷaμˠ!θiunOl
	ˈɸorOil -> ˈɸourOil
	ˈtinOl -> ˈtiunOl


0 -> u / (::C::|Ø)::V:: _ (?=::C::+[ouU])
Sample of maximum 20 input/output pairs:

	ˈØakoβur -> ˈØaukouβur
	ˈØakoμul -> ˈØaukouμul
	ˈØairiɣuð -> ˈØairiuɣuð
	ˈØˠərʲ!liguð -> ˈØˠərʲ!liuguð
	ˈØaibstinuid -> ˈØaibstiunuid
	ˈØabθu -> ˈØaubθu
	ˈØastuð -> ˈØaustuð
	ˈØatluɣuð -> ˈØautluuɣuð
	ˈbeθu -> ˈbeuθu
	ˈbeθu -> ˈbeuθu
	ˈbiβðu -> ˈbiuβðu
	ˈbiθ-ˈβeθu -> ˈbiθ-ˈβeuθu
	ˈbunoað -> ˈbuunoað
	ˈburbue -> ˈbuurbue
	ˈkaEin-ˈðUθroaxt -> ˈkaEin-ˈðUuθroaxt
	ˈkEdβuið -> ˈkEudβuið
	ˈkeθarxo -> ˈkeθaurxo
	ˈkoβoðlus -> ˈkouβouðlus
	ˈkoβuir -> ˈkouβuir
	ˈkoguβus -> ˈkouguuβus


%%%% 9. Rewriting short and hiatus vowels
%
% These rules rewrite short vowels for colour assignment
%
% 9i. Adds a vowel after a short vowel for colour assignment, also in hiatus.
% 9ii. Standardises the first vowel in hiatus, where only /ə/ is permitted before i-colour or u-colour.
% 9iii. Adds a vowel before a short vowel for colour assignment.
% 9iv. Rewrites the second vowel in hiatus for colour assignment.
%
% 9i.
%
0 -> a / (::C::|Ø)[aeo] _ (?=::C::|\.)
Sample of maximum 20 input/output pairs:

	ˈØagaʟdaμ -> ˈØaagaaʟdaaμ
	ˈØaðaiɣ -> ˈØaaðaiɣ
	ˈØaðaʟtras -> ˈØaaðaaʟtraas
	ˈØaðβar -> ˈØaaðβaar
	ˈØaðnagaul -> ˈØaaðnaagaul
	ˈØaðrað -> ˈØaaðraað
	ˈØaigneð -> ˈØaigneað
	ˈØˠəðʷ!baʀt -> ˈØˠəðʷ!baaʀt
	ˈØaimser -> ˈØaimsear
	ˈØainegnae -> ˈØaineagnae
	ˈØaiŋgel -> ˈØaiŋgeal
	ˈØAiɴseμ -> ˈØAiɴseaμ
	ˈØˠərʲ!xiɴex -> ˈØˠərʲ!xiɴeax
	ˈØˠərʲ!xisext -> ˈØˠərʲ!xiseaxt
	ˈØaireg -> ˈØaireag
	ˈØairexas -> ˈØaireaxaas
	ˈØˠərʷ!ɣal -> ˈØˠərʷ!ɣaal
	ˈØˠərʷ!ladau -> ˈØˠərʷ!laadau
	ˈØalmsan -> ˈØaalmsaan
	ˈØaʟtOir -> ˈØaaʟtOir


0 -> i / (::C::|Ø)i _ (?=::C::|\.)
Sample of maximum 20 input/output pairs:

	ˈØainkriðe -> ˈØainkriiðe
	ˈØaibɣidir -> ˈØaibɣiidiir
	ˈØˠərʲ!xiɴeax -> ˈØˠərʲ!xiiɴeax
	ˈØˠərʲ!xiseaxt -> ˈØˠərʲ!xiiseaxt
	ˈØAiriʟiuð -> ˈØAiriiʟiuð
	ˈØAiriʟiuð -> ˈØAiriiʟiuð
	ˈØˠərʲ!Øidiu -> ˈØˠərʲ!Øiidiu
	ˈØˠərʲ!μidiu -> ˈØˠərʲ!μiidiu
	ˈØaiθirɣe -> ˈØaiθiirɣe
	ˈØaiθriɣe -> ˈØaiθriiɣe
	ˈØaiθis -> ˈØaiθiis
	ˈØainim -> ˈØainiim
	ˈØaabstainid -> ˈØaabstainiid
	ˈbaiθis -> ˈbaiθiis
	ˈbi.að -> ˈbii.að
	ˈbiθ-ˈβeuθu -> ˈbiiθ-ˈβeuθu
	ˈbriθ -> ˈbriiθ
	ˈbriθeaμ -> ˈbriiθeaμ
	ˈbriθeaμnaaxt -> ˈbriiθeaμnaaxt
	ˈbiθ -> ˈbiiθ


0 -> u / (::C::|Ø)u _ (?=::C::|\.)
Sample of maximum 20 input/output pairs:

	ˈØaukouβur -> ˈØaukouβuur
	ˈØaukouμul -> ˈØaukouμuul
	ˈØˠərʷ!kur -> ˈØˠərʷ!kuur
	ˈØairiuɣuð -> ˈØairiuɣuuð
	ˈØˠərʲ!liuguð -> ˈØˠərʲ!liuguuð
	ˈØaustuð -> ˈØaustuuð
	ˈØautluuɣuð -> ˈØautluuɣuuð
	ˈkouβouðlus -> ˈkouβouðluus
	ˈkouguuβus -> ˈkouguuβuus
	ˈkul -> ˈkuul
	ˈkʷaμˠ!Øaukouβur -> ˈkʷaμˠ!Øaukouβuur
	ˈkʷaμʷ!rourgun -> ˈkʷaμʷ!rourguun
	ˈkur -> ˈkuur
	ˈkoudluð -> ˈkoudluuð
	ˈkrAuβuð -> ˈkrAuβuuð
	ˈkruθ -> ˈkruuθ
	ˈkuuβus -> ˈkuuβuus
	ˈkuuμskuuɣuð -> ˈkuuμskuuɣuuð
	ˈkuudruumus -> ˈkuudruumuus
	ˈdeuxur -> ˈdeuxuur


% 9ii.
%
e -> i / _ a\.
Sample of maximum 20 input/output pairs:

	ˈdea.axt -> ˈdia.axt
	ˈdea.að -> ˈdia.að
	ˈdea.að -> ˈdia.að
	ˈdea.a -> ˈdia.a
	ˈʀea.e -> ˈʀia.e
	ˈʀea.e -> ˈʀia.e


% 9iii.
%
0 -> a / _ (?=a[aiu]::C::)|a-
Sample of maximum 20 input/output pairs:

	ˈØaagaaʟdaaμ -> ˈØaaagaaaʟdaaaμ
	ˈØaukouβuur -> ˈØaaukouβuur
	ˈØaukouμuul -> ˈØaaukouμuul
	ˈØaaðaiɣ -> ˈØaaaðaaiɣ
	ˈØaaðaaʟtraas -> ˈØaaaðaaaʟtraaas
	ˈØaaðβaar -> ˈØaaaðβaaar
	ˈØaaðnaagaul -> ˈØaaaðnaaagaaul
	ˈØaaðraað -> ˈØaaaðraaað
	ˈØaigneað -> ˈØaaigneað
	ˈØˠəðʷ!baaʀt -> ˈØˠəðʷ!baaaʀt
	ˈØail -> ˈØaail
	ˈØail -> ˈØaail
	ˈØaiʟe -> ˈØaaiʟe
	ˈØaimsear -> ˈØaaimsear
	ˈØainkriiðe -> ˈØaainkriiðe
	ˈØaineagnae -> ˈØaaineagnae
	ˈØainɸius -> ˈØaainɸius
	ˈØaiŋgeal -> ˈØaaiŋgeal
	ˈØainm -> ˈØaainm
	ˈØainμne -> ˈØaainμne


0 -> i / _ (?=[ei][aiu]::C::)|[ei]-
Sample of maximum 20 input/output pairs:

	ˈØaaigneað -> ˈØaaignieað
	ˈØaaimsear -> ˈØaaimsiear
	ˈØaainkriiðe -> ˈØaainkriiiðe
	ˈØaaineagnae -> ˈØaainieagnae
	ˈØaainɸius -> ˈØaainɸiius
	ˈØaaiŋgeal -> ˈØaaiŋgieal
	ˈØAiɴseaμ -> ˈØAiɴsieaμ
	ˈØaaibɣiidiir -> ˈØaaibɣiiidiiir
	ˈØˠərʲ!xiiɴeax -> ˈØˠərʲ!xiiiɴieax
	ˈØˠərʲ!xiiseaxt -> ˈØˠərʲ!xiiisieaxt
	ˈØaaireag -> ˈØaairieag
	ˈØaaireaxaaas -> ˈØaairieaxaaas
	ˈØaairiuɣuuð -> ˈØaairiiuɣuuð
	ˈØAiriiʟiuð -> ˈØAiriiiʟiiuð
	ˈØAiriiʟiuð -> ˈØAiriiiʟiiuð
	ˈØˠərʲ!Øiidiu -> ˈØˠərʲ!Øiiidiu
	ˈØˠərʲ!liuguuð -> ˈØˠərʲ!liiuguuð
	ˈØˠərʲ!μiidiu -> ˈØˠərʲ!μiiidiu
	ˈØaaiθiirɣe -> ˈØaaiθiiirɣe
	ˈØaaiθriiɣe -> ˈØaaiθriiiɣe


0 -> u / _ (?=[ou][aiu]::C::)|[ou]-
Sample of maximum 20 input/output pairs:

	ˈØaaukouβuur -> ˈØaaukuouβuuur
	ˈØaaukouμuul -> ˈØaaukuouμuuul
	ˈØˠərʷ!kuur -> ˈØˠərʷ!kuuur
	ˈØaairiiuɣuuð -> ˈØaairiiuɣuuuð
	ˈØˠərʲ!liiuguuð -> ˈØˠərʲ!liiuguuuð
	ˈØˠəuʀnuiɣðe -> ˈØˠəuʀnuuiɣðe
	ˈØaaibstiiunuid -> ˈØaaibstiiunuuid
	ˈØaaustuuð -> ˈØaaustuuuð
	ˈØaautluuɣuuð -> ˈØaautluuuɣuuuð
	ˈØˠəuɣdoarðAs -> ˈØˠəuɣduoarðAs
	ˈboalaaað -> ˈbuoalaaað
	ˈbuiðe -> ˈbuuiðe
	ˈbuiɴe -> ˈbuuiɴe
	ˈboaθ -> ˈbuoaθ
	ˈboaθ -> ˈbuoaθ
	ˈbuiθ -> ˈbuuiθ
	ˈbuunoað -> ˈbuuunuoað
	ˈbuirbe -> ˈbuuirbe
	ˈbuurbue -> ˈbuuurbue
	ˈkaEin-ˈxoaμraaak -> ˈkaEin-ˈxuoaμraaak


% 9iv.
%
0 -> a / \.[oea] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØai.ar -> ˈØai.aar
	ˈØai.ar -> ˈØai.aar
	ˈbii.að -> ˈbii.aað
	ˈdia.axt -> ˈdia.aaxt
	ˈdia.að -> ˈdia.aað
	ˈdia.að -> ˈdia.aað
	ˈdii.as -> ˈdii.aas
	ˈdii.as -> ˈdii.aas
	ˈmaa.aμ -> ˈmaa.aaμ
	ˈtrii.ar -> ˈtrii.aar


%%%% 10. Rewriting long vowels
%
% These rules rewrite long vowels for colour assignment.
%
% 10i. There is ambiguity in the case of medial ó and ói, where these might follow a-colour or u-colour.
% This rule isolates the a-colour cases (where <ó, ói> are the medial realisations of <áu, áui>.
%
% e.g. umaldóit, preceptóir
%
% 10ii. Elsewhere, the quality of a preceding consonant can be straightforwardly inferred by the vowel representation.
% These rules assign short vowels before long vowels for colour assignment
%
% 10iii. In many cases, the normalised orthography of long vowels is the same whether an a-colour or u-colour consonant follows.
% In most cases (10iv.) we take the following vowel to be indicative of consonant colour, but the situation is less clear with final consonants.
% For ó before a final consonant, e.g. brón, a-colour is assumed.
%
% The normalised orthography underdetermines the phonology in the case of é. Here, we assume as default that it represents CʲaØʲ etc.
% Goidinflex manually annotates cases where it is rather CʲaØʷCˠ, i.e. the é that alternates with éo and éoi in certain paradigms.
%
% Similarly, we cannot tell from the normalised orthography if éi represents CʲaØʲCʲ (iéi) or CʲaØˠCʲ (iái). The latter alternates with ía.
% Here, we assume the representation CʲaØʲCʲ.
%
% 10iv. When a vowel follows, we have taken this to indicate the colour of the preceding consonant, except where a follows long ú.
%
% 10i.
%
0 -> a / a::C::+ _ O
Sample of maximum 20 input/output pairs:

	ˈØaaaʟtOir -> ˈØaaaʟtaOir
	ˈprieigieaptOir -> ˈprieigieaptaOir
	ˈØuoaμaaaʟdOid -> ˈØuoaμaaaʟdaOid


% 10ii.
%
0 -> a / ::C::|Ø _ A
Sample of maximum 20 input/output pairs:

	ˈØAixθiu -> ˈØaAixθiu
	ˈØAil -> ˈØaAil
	ˈØAiɴsieaμ -> ˈØaAiɴsieaμ
	ˈØˠərʷ!ØAil -> ˈØˠərʷ!ØaAil
	ˈØˠərʷ!βAɣ -> ˈØˠərʷ!βaAɣ
	ˈØAiriiiʟiiuð -> ˈØaAiriiiʟiiuð
	ˈØAiriiiʟiiuð -> ˈØaAiriiiʟiiuð
	ˈØAnae -> ˈØaAnae
	ˈØAitrieaβ -> ˈØaAitrieaβ
	ˈØˠəuɣduoarðAs -> ˈØˠəuɣduoarðaAs
	ˈbAɣ -> ˈbaAɣ
	ˈbAs -> ˈbaAs
	ˈbrAθ -> ˈbraAθ
	ˈbrAθaair -> ˈbraAθaair
	ˈkrAuβuuuð -> ˈkraAuβuuuð
	ˈdAn -> ˈdaAn
	ˈduu-ˈØAlaaiɣ -> ˈduu-ˈØaAlaaiɣ
	ˈɸAiʟte -> ˈɸaAiʟte
	ˈɸAiθ -> ˈɸaAiθ
	ˈgaaaβAil -> ˈgaaaβaAil


0 -> i / ::C::|Ø _ [EI]
Sample of maximum 20 input/output pairs:

	ˈØaaisɴdIs -> ˈØaaisɴdiIs
	ˈØaaisɴdIs -> ˈØaaisɴdiIs
	ˈØaaisɴdEis -> ˈØaaisɴdiEis
	ˈbEim -> ˈbiEim
	ˈbEl -> ˈbiEl
	ˈbElrae -> ˈbiElrae
	ˈbEs -> ˈbiEs
	ˈbEsaaað -> ˈbiEsaaað
	ˈbEsknae -> ˈbiEsknae
	ˈbEstaaadau -> ˈbiEstaaadau
	ˈbrIɣ -> ˈbriIɣ
	ˈkaEin-ˈɣnIuμ -> ˈkaEin-ˈɣniIuμ
	ˈkaEin-ˈskEl -> ˈkaEin-ˈskiEl
	ˈkEile -> ˈkiEile
	ˈkEiliiiðe -> ˈkiEiliiiðe
	ˈkieinEl -> ˈkieiniEl
	ˈkieinEl -> ˈkieiniEl
	ˈkieinElae -> ˈkieiniElae
	ˈkEsaaað -> ˈkiEsaaað
	ˈkEd -> ˈkiEd


0 -> u / ::C::|Ø _ [OU]
Sample of maximum 20 input/output pairs:

	ˈØˠərʷ!ØOgrae -> ˈØˠərʷ!ØuOgrae
	ˈbrOn -> ˈbruOn
	ˈkaEin-ˈðUuθruoaxt -> ˈkaEin-ˈðuUuθruoaxt
	ˈkʷaμˠ!θiiunOl -> ˈkʷaμˠ!θiiunuOl
	ˈkOrae -> ˈkuOrae
	ˈkUl -> ˈkuUl
	ˈkUuʀsuoaɣaaað -> ˈkuUuʀsuoaɣaaað
	ˈkUuʀsuoaɣaaað -> ˈkuUuʀsuoaɣaaað
	ˈdlUμ -> ˈdluUμ
	ˈdUil -> ˈduUil
	ˈdUilxiiiɴe -> ˈduUilxiiiɴe
	ˈdUuθruoaxt -> ˈduUuθruoaxt
	ˈdUuθruoaxt -> ˈduUuθruoaxt
	ˈɸOgrae -> ˈɸuOgrae
	ˈɸuourOil -> ˈɸuouruOil
	ˈgnUis -> ˈgnuUis
	ˈØʲəmʷ!rOl -> ˈØʲəmʷ!ruOl
	ˈʟOɣ -> ˈʟuOɣ
	ˈmOraaað -> ˈmuOraaað
	ˈmUinieað -> ˈmuUinieað


% 10iii.
%
0 -> a / [AEO] _ ::C::+(-|·|#)
Sample of maximum 20 input/output pairs:

	ˈØaEs -> ˈØaEas
	ˈØaEs -> ˈØaEas
	ˈØˠərʷ!βaAɣ -> ˈØˠərʷ!βaAaɣ
	ˈØˠəuɣduoarðaAs -> ˈØˠəuɣduoarðaAas
	ˈbaAɣ -> ˈbaAaɣ
	ˈbaAs -> ˈbaAas
	ˈbiEl -> ˈbiEal
	ˈbiEs -> ˈbiEas
	ˈbraAθ -> ˈbraAaθ
	ˈbruOn -> ˈbruOan
	ˈkaEin-ˈskiEl -> ˈkaEin-ˈskiEal
	ˈkieiniEl -> ˈkieiniEal
	ˈkieiniEl -> ˈkieiniEal
	ˈkiEd -> ˈkiEad
	ˈkiAʟ -> ˈkiAaʟ
	ˈkuoiμiEd -> ˈkuoiμiEad
	ˈkʷaμˠ!θiiunuOl -> ˈkʷaμˠ!θiiunuOal
	ˈdaAn -> ˈdaAan
	ˈdiAð -> ˈdiAað
	ˈdiAs -> ˈdiAas


0 -> i / I _ ::C::+(-|·|#)
Sample of maximum 20 input/output pairs:

	ˈØaaisɴdiIs -> ˈØaaisɴdiIis
	ˈØaaisɴdiIs -> ˈØaaisɴdiIis
	ˈbriIɣ -> ˈbriIiɣ
	ˈmiIl -> ˈmiIil
	ˈsiIð -> ˈsiIið
	ˈtiIr -> ˈtiIir


0 -> u / U _ ::C::+(-|·|#)
Sample of maximum 20 input/output pairs:

	ˈkuUl -> ˈkuUul
	ˈdluUμ -> ˈdluUuμ
	ˈʀuUn -> ˈʀuUun
	ˈtiiuɴtuUð -> ˈtiiuɴtuUuð


% 10iv.
%
0 -> a / [AEIO] _ ::C::+[a]
Sample of maximum 20 input/output pairs:

	ˈØˠərʷ!ØuOgrae -> ˈØˠərʷ!ØuOagrae
	ˈØaAnae -> ˈØaAanae
	ˈbiElrae -> ˈbiEalrae
	ˈbiEsaaað -> ˈbiEasaaað
	ˈbiEsknae -> ˈbiEasknae
	ˈbiEstaaadau -> ˈbiEastaaadau
	ˈbraAθaair -> ˈbraAaθaair
	ˈbriAθaaar -> ˈbriAaθaaar
	ˈbriAθaaar -> ˈbriAaθaaar
	ˈkieiniElae -> ˈkieiniEalae
	ˈkiEsaaað -> ˈkiEasaaað
	ˈkuOrae -> ˈkuOarae
	ˈdiIðnaaað -> ˈdiIaðnaaað
	ˈdiIɣaaal -> ˈdiIaɣaaal
	ˈdiIɣaaal -> ˈdiIaɣaaal
	ˈduEnaaaxt -> ˈduEanaaaxt
	ˈduu-ˈØaAlaaiɣ -> ˈduu-ˈØaAalaaiɣ
	ˈØiEgɴdaaax -> ˈØiEagɴdaaax
	ˈØiEdaaax -> ˈØiEadaaax
	ˈØiEdraaað -> ˈØiEadraaað


0 -> i / [AEIOU] _ ::C::+[ei]
Sample of maximum 20 input/output pairs:

	ˈdiIμiiigieaμ -> ˈdiIiμiiigieaμ
	ˈdiIdiu -> ˈdiIidiu
	ˈɸiIriAnuuuɣuuuð -> ˈɸiIiriAnuuuɣuuuð
	ˈɸiIriiiɴe -> ˈɸiIiriiiɴe
	ˈØʲəɴʲdʲ!ØiIrɣe -> ˈØʲəɴʲdʲ!ØiIirɣe
	ˈmiIle -> ˈmiIile
	ˈmiIʟte -> ˈmiIiʟte
	ˈpriIμiiid -> ˈpriIiμiiid
	ˈskriIβieaɴd -> ˈskriIiβieaɴd
	ˈskriIβieaɴt -> ˈskriIiβieaɴt


0 -> u / [AEIOU] _ ::C::+[ou]
Sample of maximum 20 input/output pairs:

	ˈdiOluoaðaaaxt -> ˈdiOuluoaðaaaxt
	ˈdiAβuuul -> ˈdiAuβuuul
	ˈɸiIiriAnuuuɣuuuð -> ˈɸiIiriAunuuuɣuuuð
	ˈØiUðue -> ˈØiUuðue
	ˈØiUðuuiðe -> ˈØiUuðuuiðe
	ˈØuEɴtu -> ˈØuEuɴtu
	ˈØuEɴtu -> ˈØuEuɴtu
	ˈØuEnuuur -> ˈØuEunuuur
	ˈsaEɣuuul -> ˈsaEuɣuuul
	ˈtuArguuun -> ˈtuAurguuun


0 -> i / (::V::::C::+)|(!Ø) _ [ei]#
Sample of maximum 20 input/output pairs:

	ˈØaaiʟe -> ˈØaaiʟie
	ˈØaainkriiiðe -> ˈØaainkriiiðie
	ˈØaainμne -> ˈØaainμnie
	ˈØaairðe -> ˈØaairðie
	ˈØˠərʷ!ɣaaire -> ˈØˠərʷ!ɣaairie
	ˈØˠəuʀnuuiɣðe -> ˈØˠəuʀnuuiɣðie
	ˈØaaiθe -> ˈØaaiθie
	ˈØaaiθɣne -> ˈØaaiθɣnie
	ˈØaaiθiiirɣe -> ˈØaaiθiiirɣie
	ˈØaaiθriiiɣe -> ˈØaaiθriiiɣie
	ˈbuuiðe -> ˈbuuiðie
	ˈbuuiɴe -> ˈbuuiɴie
	ˈbuuirbe -> ˈbuuirbie
	ˈkiEile -> ˈkiEilie
	ˈkiEiliiiðe -> ˈkiEiliiiðie
	ˈkluEine -> ˈkluEinie
	ˈkuoiβse -> ˈkuoiβsie
	ˈkuoigiEiʟsiiine -> ˈkuoigiEiʟsiiinie
	ˈkʷaμˠ!Øaairle -> ˈkʷaμˠ!Øaairlie
	ˈkuoaɴdaairgiiile -> ˈkuoaɴdaairgiiilie


0 -> u / (::V::::C::+)|(!Ø) _ [ou]#
Sample of maximum 20 input/output pairs:

	ˈØaaubθu -> ˈØaaubθuu
	ˈbieuθu -> ˈbieuθuu
	ˈbieuθu -> ˈbieuθuu
	ˈbiiuβðu -> ˈbiiuβðuu
	ˈbiiiθ-ˈβieuθu -> ˈbiiiθ-ˈβieuθuu
	ˈkieaθaaurxo -> ˈkieaθaaurxuo
	ˈɴieaβ-ˈμaauʀtu -> ˈɴieaβ-ˈμaauʀtuu
	ˈØuEuɴtu -> ˈØuEuɴtuu
	ˈØuEuɴtu -> ˈØuEuɴtuu
	ˈʀiIuxtu -> ˈʀiIuxtuu
	ˈtiIuxtu -> ˈtiIuxtuu


0 -> a / (::V::::C::+)|(!Ø) _ a#
Sample of maximum 20 input/output pairs:

	ˈØaaanmxaaara -> ˈØaaanmxaaaraa
	ˈpieaʀsa -> ˈpieaʀsaa


%%%% 12. Final vowels and first of two vowels in hiatus as long vowels
%
% It is convenient in the derivation to treat final vowels and the first of two vowels in hiatus as long.
%
a -> A / _ (\.|#)
Sample of maximum 20 input/output pairs:

	ˈØaaanmxaaaraa -> ˈØaaanmxaaaraA
	ˈbaa.e -> ˈbaA.e
	ˈdia.aaxt -> ˈdiA.aaxt
	ˈdia.aað -> ˈdiA.aað
	ˈdia.aað -> ˈdiA.aað
	ˈdia.a -> ˈdiA.A
	ˈʟaa.e -> ˈʟaA.e
	ˈmaa.aaμ -> ˈmaA.aaμ
	ˈpieaʀsaa -> ˈpieaʀsaA
	ˈʀia.e -> ˈʀiA.e
	ˈʀia.e -> ˈʀiA.e
	ˈsaain-ˈlaa.e -> ˈsaain-ˈlaA.e


e -> E / _ #
Sample of maximum 20 input/output pairs:

	ˈØaaiʟie -> ˈØaaiʟiE
	ˈØaainkriiiðie -> ˈØaainkriiiðiE
	ˈØaainieagnae -> ˈØaainieagnaE
	ˈØaainμnie -> ˈØaainμniE
	ˈØˠərʷ!xrae -> ˈØˠərʷ!xraE
	ˈØaairðie -> ˈØaairðiE
	ˈØˠərʷ!ɣaairie -> ˈØˠərʷ!ɣaairiE
	ˈØˠəuʀnuuiɣðie -> ˈØˠəuʀnuuiɣðiE
	ˈØˠərʷ!ØuOagrae -> ˈØˠərʷ!ØuOagraE
	ˈØaaiθie -> ˈØaaiθiE
	ˈØaaiθɣnie -> ˈØaaiθɣniE
	ˈØaaiθiiirɣie -> ˈØaaiθiiirɣiE
	ˈØaaiθriiiɣie -> ˈØaaiθriiiɣiE
	ˈØaAanae -> ˈØaAanaE
	ˈØaaanaaam-ˈxaaarae -> ˈØaaanaaam-ˈxaaaraE
	ˈbaA.e -> ˈbaA.E
	ˈbiEalrae -> ˈbiEalraE
	ˈbiEasknae -> ˈbiEasknaE
	ˈbuuiðie -> ˈbuuiðiE
	ˈbuuiɴie -> ˈbuuiɴiE


o -> O / _ #
Sample of maximum 20 input/output pairs:

	ˈkieaθaaurxuo -> ˈkieaθaaurxuO


i -> I / _ (\.|#)
Sample of maximum 20 input/output pairs:

	ˈØai.aar -> ˈØaI.aar
	ˈØai.aar -> ˈØaI.aar
	ˈbii.aað -> ˈbiI.aað
	ˈdaaaɣ-ˈðuEinii -> ˈdaaaɣ-ˈðuEiniI
	ˈdii.aas -> ˈdiI.aas
	ˈdii.aas -> ˈdiI.aas
	ˈdii.u -> ˈdiI.u
	ˈdii.E -> ˈdiI.E
	ˈdrui.i -> ˈdruI.I
	ˈduEinii -> ˈduEiniI
	ˈgieiɴtii -> ˈgieiɴtiI
	ˈʟii.i -> ˈʟiI.I
	ˈʟii.E -> ˈʟiI.E
	ˈʟii.E -> ˈʟiI.E
	ˈØuEiɣii -> ˈØuEiɣiI
	ˈtrii.aar -> ˈtriI.aar


u -> U / _ (\.|#)
Sample of maximum 20 input/output pairs:

	ˈØaAixθiu -> ˈØaAixθiU
	ˈØˠərʲ!Øiiidiu -> ˈØˠərʲ!ØiiidiU
	ˈØˠərʷ!laaadau -> ˈØˠərʷ!laaadaU
	ˈØˠərʲ!μiiidiu -> ˈØˠərʲ!μiiidiU
	ˈØaaubθuu -> ˈØaaubθuU
	ˈbiEastaaadau -> ˈbiEastaaadaU
	ˈbieuθuu -> ˈbieuθuU
	ˈbieuθuu -> ˈbieuθuU
	ˈbiiuβðuu -> ˈbiiuβðuU
	ˈbiiiθ-ˈβieuθuu -> ˈbiiiθ-ˈβieuθuU
	ˈkuoimðiu -> ˈkuoimðiU
	ˈdiEigsiu -> ˈdiEigsiU
	ˈdieiθiiidiu -> ˈdieiθiiidiU
	ˈdiIidiu -> ˈdiIidiU
	ˈdiI.u -> ˈdiI.U
	ˈØaaabaaaʟtau -> ˈØaaabaaaʟtaU
	ˈØieibieaʟtau -> ˈØieibieaʟtaU
	ˈØieibiiiʟtiu -> ˈØieibiiiʟtiU
	ˈɸuoaðaaidiu -> ˈɸuoaðaaidiU
	ˈɸuoirβθieadau -> ˈɸuoirβθieadaU


%%%%%%%%%%%%%%%     Consonant colour assignment     %%%%%%%%%%%%%%%
%%%% 13. Consonant colour before vowels
%
% 13i. This rule assigns consonant colour before vowels.
%
% 13ii. This rule assigns consonant colour after vowels.
%
% 13i
a -> ˠ / (?<=::C::+|Ø) _ ::V::
Sample of maximum 20 input/output pairs:

	ˈØaaagaaaʟdaaaμ -> ˈØˠaagˠaaʟdˠaaμ
	ˈØaaukuouβuuur -> ˈØˠaukuouβuuur
	ˈØaaukuouμuuul -> ˈØˠaukuouμuuul
	ˈØaaaðaaiɣ -> ˈØˠaaðˠaiɣ
	ˈØaaaðaaaʟtraaas -> ˈØˠaaðˠaaʟtrˠaas
	ˈØaaaðβaaar -> ˈØˠaaðβˠaar
	ˈØaaaðnaaagaaul -> ˈØˠaaðnˠaagˠaul
	ˈØaaaðraaað -> ˈØˠaaðrˠaað
	ˈØaEas -> ˈØˠEas
	ˈØaEas -> ˈØˠEas
	ˈØaI.aar -> ˈØˠI.aar
	ˈØaI.aar -> ˈØˠI.aar
	ˈØaAixθiU -> ˈØˠAixθiU
	ˈØaaignieað -> ˈØˠaignieað
	ˈØˠəðʷ!baaaʀt -> ˈØˠəðʷ!bˠaaʀt
	ˈØaail -> ˈØˠail
	ˈØaail -> ˈØˠail
	ˈØaAil -> ˈØˠAil
	ˈØaaiʟiE -> ˈØˠaiʟiE
	ˈØaaimsiear -> ˈØˠaimsiear


i -> ʲ / (?<=::C::+|Ø) _ ::V::
Sample of maximum 20 input/output pairs:

	ˈØˠAixθiU -> ˈØˠAixθʲU
	ˈØˠaignieað -> ˈØˠaignʲeað
	ˈØˠaiʟiE -> ˈØˠaiʟʲE
	ˈØˠaimsiear -> ˈØˠaimsʲear
	ˈØˠainkriiiðiE -> ˈØˠainkrʲiiðʲE
	ˈØˠainieagnˠE -> ˈØˠainʲeagnˠE
	ˈØˠainɸiius -> ˈØˠainɸʲius
	ˈØˠaiŋgieal -> ˈØˠaiŋgʲeal
	ˈØˠainμniE -> ˈØˠainμnʲE
	ˈØˠAiɴsieaμ -> ˈØˠAiɴsʲeaμ
	ˈØˠaibɣiiidiiir -> ˈØˠaibɣʲiidʲiir
	ˈØˠərʲ!xiiiɴieax -> ˈØˠərʲ!xʲiiɴʲeax
	ˈØˠərʲ!xiiisieaxt -> ˈØˠərʲ!xʲiisʲeaxt
	ˈØˠairðiE -> ˈØˠairðʲE
	ˈØˠairieag -> ˈØˠairʲeag
	ˈØˠairieaxˠaas -> ˈØˠairʲeaxˠaas
	ˈØˠərʷ!ɣˠairiE -> ˈØˠərʷ!ɣˠairʲE
	ˈØˠairiiuɣuuuð -> ˈØˠairʲiuɣuuuð
	ˈØˠAiriiiʟiiuð -> ˈØˠAirʲiiʟʲiuð
	ˈØˠAiriiiʟiiuð -> ˈØˠAirʲiiʟʲiuð


u -> ʷ / (?<=::C::+|Ø) _ ::V::
Sample of maximum 20 input/output pairs:

	ˈØˠaukuouβuuur -> ˈØˠaukʷouβʷuur
	ˈØˠaukuouμuuul -> ˈØˠaukʷouμʷuul
	ˈØˠərʷ!kuuur -> ˈØˠərʷ!kʷuur
	ˈØˠairʲiuɣuuuð -> ˈØˠairʲiuɣʷuuð
	ˈØˠərʲ!lʲiuguuuð -> ˈØˠərʲ!lʲiugʷuuð
	ˈØˠəuʀnuuiɣðʲE -> ˈØˠəuʀnʷuiɣðʲE
	ˈØˠərʷ!ØuOagrˠE -> ˈØˠərʷ!ØʷOagrˠE
	ˈØˠaibstʲiunuuid -> ˈØˠaibstʲiunʷuid
	ˈØˠaubθuU -> ˈØˠaubθʷU
	ˈØˠaustuuuð -> ˈØˠaustʷuuð
	ˈØˠautluuuɣuuuð -> ˈØˠautlʷuuɣʷuuð
	ˈØˠəuɣduoarðˠAas -> ˈØˠəuɣdʷoarðˠAas
	ˈbʲeuθuU -> ˈbʲeuθʷU
	ˈbʲeuθuU -> ˈbʲeuθʷU
	ˈbʲiuβðuU -> ˈbʲiuβðʷU
	ˈbʲiiθ-ˈβʲeuθuU -> ˈbʲiiθ-ˈβʲeuθʷU
	ˈbuoalˠaað -> ˈbʷoalˠaað
	ˈbruOan -> ˈbrʷOan
	ˈbuAið -> ˈbʷAið
	ˈbuuiðʲE -> ˈbʷuiðʲE


% 13ii
%
a -> ˠ / ([ˠʲʷ]|\.)::V:: _
Sample of maximum 20 input/output pairs:

	ˈØˠaagˠaaʟdˠaaμ -> ˈØˠaˠgˠaˠʟdˠaˠμ
	ˈØˠaaðˠaiɣ -> ˈØˠaˠðˠaiɣ
	ˈØˠaaðˠaaʟtrˠaas -> ˈØˠaˠðˠaˠʟtrˠaˠs
	ˈØˠaaðβˠaar -> ˈØˠaˠðβˠaˠr
	ˈØˠaaðnˠaagˠaul -> ˈØˠaˠðnˠaˠgˠaul
	ˈØˠaaðrˠaað -> ˈØˠaˠðrˠaˠð
	ˈØˠEas -> ˈØˠEˠs
	ˈØˠEas -> ˈØˠEˠs
	ˈØˠI.aar -> ˈØˠI.aˠr
	ˈØˠI.aar -> ˈØˠI.aˠr
	ˈØˠaignʲeað -> ˈØˠaignʲeˠð
	ˈØˠəðʷ!bˠaaʀt -> ˈØˠəðʷ!bˠaˠʀt
	ˈØˠaimsʲear -> ˈØˠaimsʲeˠr
	ˈØˠainʲeagnˠE -> ˈØˠainʲeˠgnˠE
	ˈØˠaiŋgʲeal -> ˈØˠaiŋgʲeˠl
	ˈØˠAiɴsʲeaμ -> ˈØˠAiɴsʲeˠμ
	ˈØˠərʷ!βˠAaɣ -> ˈØˠərʷ!βˠAˠɣ
	ˈØˠərʲ!xʲiiɴʲeax -> ˈØˠərʲ!xʲiiɴʲeˠx
	ˈØˠərʲ!xʲiisʲeaxt -> ˈØˠərʲ!xʲiisʲeˠxt
	ˈØˠairʲeag -> ˈØˠairʲeˠg


i -> ʲ / ([ˠʲʷ]|\.)::V:: _
Sample of maximum 20 input/output pairs:

	ˈØˠaˠðˠaiɣ -> ˈØˠaˠðˠaʲɣ
	ˈØˠAixθʲU -> ˈØˠAʲxθʲU
	ˈØˠaignʲeˠð -> ˈØˠaʲgnʲeˠð
	ˈØˠail -> ˈØˠaʲl
	ˈØˠail -> ˈØˠaʲl
	ˈØˠAil -> ˈØˠAʲl
	ˈØˠaiʟʲE -> ˈØˠaʲʟʲE
	ˈØˠaimsʲeˠr -> ˈØˠaʲmsʲeˠr
	ˈØˠainkrʲiiðʲE -> ˈØˠaʲnkrʲiʲðʲE
	ˈØˠainʲeˠgnˠE -> ˈØˠaʲnʲeˠgnˠE
	ˈØˠainɸʲius -> ˈØˠaʲnɸʲius
	ˈØˠaiŋgʲeˠl -> ˈØˠaʲŋgʲeˠl
	ˈØˠainm -> ˈØˠaʲnm
	ˈØˠainμnʲE -> ˈØˠaʲnμnʲE
	ˈØˠAiɴsʲeˠμ -> ˈØˠAʲɴsʲeˠμ
	ˈØˠaibɣʲiidʲiir -> ˈØˠaʲbɣʲiʲdʲiʲr
	ˈØˠərʷ!ØˠAil -> ˈØˠərʷ!ØˠAʲl
	ˈØˠərʲ!xʲiiɴʲeˠx -> ˈØˠərʲ!xʲiʲɴʲeˠx
	ˈØˠərʲ!xʲiisʲeˠxt -> ˈØˠərʲ!xʲiʲsʲeˠxt
	ˈØˠairðʲE -> ˈØˠaʲrðʲE


u -> ʷ / ([ˠʲʷ]|\.)::V:: _
Sample of maximum 20 input/output pairs:

	ˈØˠaukʷouβʷuur -> ˈØˠaʷkʷoʷβʷuʷr
	ˈØˠaukʷouμʷuul -> ˈØˠaʷkʷoʷμʷuʷl
	ˈØˠaˠðnˠaˠgˠaul -> ˈØˠaˠðnˠaˠgˠaʷl
	ˈØˠaʲnɸʲius -> ˈØˠaʲnɸʲiʷs
	ˈØˠərʷ!kʷuur -> ˈØˠərʷ!kʷuʷr
	ˈØˠaʲrʲiuɣʷuuð -> ˈØˠaʲrʲiʷɣʷuʷð
	ˈØˠAʲrʲiʲʟʲiuð -> ˈØˠAʲrʲiʲʟʲiʷð
	ˈØˠAʲrʲiʲʟʲiuð -> ˈØˠAʲrʲiʲʟʲiʷð
	ˈØˠərʲ!lʲiugʷuuð -> ˈØˠərʲ!lʲiʷgʷuʷð
	ˈØˠəuʀnʷuʲɣðʲE -> ˈØˠəʷʀnʷuʲɣðʲE
	ˈØˠaʲbstʲiunʷuʲd -> ˈØˠaʲbstʲiʷnʷuʲd
	ˈØˠaubθʷU -> ˈØˠaʷbθʷU
	ˈØˠaustʷuuð -> ˈØˠaʷstʷuʷð
	ˈØˠautlʷuuɣʷuuð -> ˈØˠaʷtlʷuʷɣʷuʷð
	ˈØˠəuɣdʷoˠrðˠAˠs -> ˈØˠəʷɣdʷoˠrðˠAˠs
	ˈbʲeuθʷU -> ˈbʲeʷθʷU
	ˈbʲeuθʷU -> ˈbʲeʷθʷU
	ˈbʲiuβðʷU -> ˈbʲiʷβðʷU
	ˈbʲiʲθ-ˈβʲeuθʷU -> ˈbʲiʲθ-ˈβʲeʷθʷU
	ˈbʲiuθ -> ˈbʲiʷθ


%%%%%%%%%%%%%%%     Vowel reduction     %%%%%%%%%%%%%%%
%%%% 14. Reduce short vowels
%
% This rule reduces short vowels to /a/ or /ə/
%
e -> a / [ʲ]|\. _ [ʲʷˠ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʲgnʲeˠð -> ˈØˠaʲgnʲaˠð
	ˈØˠaʲmsʲeˠr -> ˈØˠaʲmsʲaˠr
	ˈØˠaʲnʲeˠgnˠE -> ˈØˠaʲnʲaˠgnˠE
	ˈØˠaʲŋgʲeˠl -> ˈØˠaʲŋgʲaˠl
	ˈØˠAʲɴsʲeˠμ -> ˈØˠAʲɴsʲaˠμ
	ˈØˠərʲ!xʲiʲɴʲeˠx -> ˈØˠərʲ!xʲiʲɴʲaˠx
	ˈØˠərʲ!xʲiʲsʲeˠxt -> ˈØˠərʲ!xʲiʲsʲaˠxt
	ˈØˠaʲrʲeˠg -> ˈØˠaʲrʲaˠg
	ˈØˠaʲrʲeˠxˠaˠs -> ˈØˠaʲrʲaˠxˠaˠs
	ˈØˠaˠμˠaʲrʲeˠs -> ˈØˠaˠμˠaʲrʲaˠs
	ˈØˠaˠμˠaʲrʲeˠsˠaˠx -> ˈØˠaˠμˠaʲrʲaˠsˠaˠx
	ˈØˠAʲtrʲeˠβ -> ˈØˠAʲtrʲaˠβ
	ˈbˠaʲrɣʲeˠn -> ˈbˠaʲrɣʲaˠn
	ˈbˠaʲθʲeˠs -> ˈbˠaʲθʲaˠs
	ˈbʲeˠn -> ˈbʲaˠn
	ˈbʲeˠɴdˠaˠxt -> ˈbʲaˠɴdˠaˠxt
	ˈbʲeˠɴdˠaˠxt -> ˈbʲaˠɴdˠaˠxt
	ˈbʲeʷθʷU -> ˈbʲaʷθʷU
	ˈbʲeʷθʷU -> ˈbʲaʷθʷU
	ˈbʲiʲθ-ˈβʲeʷθʷU -> ˈbʲiʲθ-ˈβʲaʷθʷU


o -> a / [ʷ]|\. _ [ʲʷˠ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷoʷβʷuʷr -> ˈØˠaʷkʷaʷβʷuʷr
	ˈØˠaʷkʷoʷμʷuʷl -> ˈØˠaʷkʷaʷμʷuʷl
	ˈØˠəʷɣdʷoˠrðˠAˠs -> ˈØˠəʷɣdʷaˠrðˠAˠs
	ˈbʷoˠlˠaˠð -> ˈbʷaˠlˠaˠð
	ˈbʷoˠθ -> ˈbʷaˠθ
	ˈbʷoˠθ -> ˈbʷaˠθ
	ˈbʷuʷnʷoˠð -> ˈbʷuʷnʷaˠð
	ˈkˠEʲn-ˈxʷoˠμrˠaˠk -> ˈkˠEʲn-ˈxʷaˠμrˠaˠk
	ˈkˠEʲn-ˈðʷUʷθrʷoˠxt -> ˈkˠEʲn-ˈðʷUʷθrʷaˠxt
	ˈkʷoʷβʷoʷðlʷuʷs -> ˈkʷaʷβʷaʷðlʷuʷs
	ˈkʷoʷβʷuʲr -> ˈkʷaʷβʷuʲr
	ˈkʷoʷgʷuʷβʷuʷs -> ˈkʷaʷgʷuʷβʷuʷs
	ˈkʷoʲβðʲaˠlˠaˠx -> ˈkʷaʲβðʲaˠlˠaˠx
	ˈkʷoʲβðʲaˠlˠaˠx -> ˈkʷaʲβðʲaˠlˠaˠx
	ˈkʷoʲβsʲE -> ˈkʷaʲβsʲE
	ˈkʷoʲgʲEʲʟsʲiʲnʲE -> ˈkʷaʲgʲEʲʟsʲiʲnʲE
	ˈkʷoʲμʲEʲd -> ˈkʷaʲμʲEʲd
	ˈkʷoʲμʲEˠd -> ˈkʷaʲμʲEˠd
	ˈkʷoʲmðʲU -> ˈkʷaʲmðʲU
	ˈkʷoˠlˠaʲɴ -> ˈkʷaˠlˠaʲɴ


i -> ə / [ʲ]|\. _ [ʲʷ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʲnkrʲiʲðʲE -> ˈØˠaʲnkrʲəʲðʲE
	ˈØˠaʲnɸʲiʷs -> ˈØˠaʲnɸʲəʷs
	ˈØˠaʲbɣʲiʲdʲiʲr -> ˈØˠaʲbɣʲəʲdʲəʲr
	ˈØˠərʲ!xʲiʲɴʲaˠx -> ˈØˠərʲ!xʲəʲɴʲaˠx
	ˈØˠərʲ!xʲiʲsʲaˠxt -> ˈØˠərʲ!xʲəʲsʲaˠxt
	ˈØˠaʲrʲiʷɣʷuʷð -> ˈØˠaʲrʲəʷɣʷuʷð
	ˈØˠAʲrʲiʲʟʲiʷð -> ˈØˠAʲrʲəʲʟʲəʷð
	ˈØˠAʲrʲiʲʟʲiʷð -> ˈØˠAʲrʲəʲʟʲəʷð
	ˈØˠərʲ!ØʲiʲdʲU -> ˈØˠərʲ!ØʲəʲdʲU
	ˈØˠərʲ!lʲiʷgʷuʷð -> ˈØˠərʲ!lʲəʷgʷuʷð
	ˈØˠərʲ!μʲiʲdʲU -> ˈØˠərʲ!μʲəʲdʲU
	ˈØˠaʲθʲiʲrɣʲE -> ˈØˠaʲθʲəʲrɣʲE
	ˈØˠaʲθrʲiʲɣʲE -> ˈØˠaʲθrʲəʲɣʲE
	ˈØˠaʲθʲiʲs -> ˈØˠaʲθʲəʲs
	ˈØˠaʲnʲiʲm -> ˈØˠaʲnʲəʲm
	ˈØˠaˠbstˠaʲnʲiʲd -> ˈØˠaˠbstˠaʲnʲəʲd
	ˈØˠaʲbstʲiʷnʷuʲd -> ˈØˠaʲbstʲəʷnʷuʲd
	ˈbˠaʲθʲiʲs -> ˈbˠaʲθʲəʲs
	ˈbʲiʷβðʷU -> ˈbʲəʷβðʷU
	ˈbʲiʲθ-ˈβʲaʷθʷU -> ˈbʲəʲθ-ˈβʲaʷθʷU


u -> ə / [ʷ]|\. _ [ʲʷ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷaʷβʷuʷr -> ˈØˠaʷkʷaʷβʷəʷr
	ˈØˠaʷkʷaʷμʷuʷl -> ˈØˠaʷkʷaʷμʷəʷl
	ˈØˠərʷ!kʷuʷr -> ˈØˠərʷ!kʷəʷr
	ˈØˠaʲrʲəʷɣʷuʷð -> ˈØˠaʲrʲəʷɣʷəʷð
	ˈØˠərʲ!lʲəʷgʷuʷð -> ˈØˠərʲ!lʲəʷgʷəʷð
	ˈØˠəʷʀnʷuʲɣðʲE -> ˈØˠəʷʀnʷəʲɣðʲE
	ˈØˠaʲbstʲəʷnʷuʲd -> ˈØˠaʲbstʲəʷnʷəʲd
	ˈØˠaʷstʷuʷð -> ˈØˠaʷstʷəʷð
	ˈØˠaʷtlʷuʷɣʷuʷð -> ˈØˠaʷtlʷəʷɣʷəʷð
	ˈbʷuʲðʲE -> ˈbʷəʲðʲE
	ˈbʷuʲɴʲE -> ˈbʷəʲɴʲE
	ˈbʷuʲθ -> ˈbʷəʲθ
	ˈbʷuʷnʷaˠð -> ˈbʷəʷnʷaˠð
	ˈbʷuʲrbʲE -> ˈbʷəʲrbʲE
	ˈbʷuʷrbʷE -> ˈbʷəʷrbʷE
	ˈkʲEʷdβʷuʲð -> ˈkʲEʷdβʷəʲð
	ˈkʷaʷβʷaʷðlʷuʷs -> ˈkʷaʷβʷaʷðlʷəʷs
	ˈkʷaʷβʷuʲr -> ˈkʷaʷβʷəʲr
	ˈkʷaʷgʷuʷβʷuʷs -> ˈkʷaʷgʷəʷβʷəʷs
	ˈkʷuʷl -> ˈkʷəʷl


%%%% 15. Reduce long vowels
%
% This rule reduces long vowels to /a/ or /ə/ followed by /Ø/ and a colour marker
%
A -> aØˠ / _
Sample of maximum 20 input/output pairs:

	ˈØˠAʲxθʲU -> ˈØˠaØˠʲxθʲU
	ˈØˠAʲl -> ˈØˠaØˠʲl
	ˈØˠAʲɴsʲaˠμ -> ˈØˠaØˠʲɴsʲaˠμ
	ˈØˠərʷ!ØˠAʲl -> ˈØˠərʷ!ØˠaØˠʲl
	ˈØˠərʷ!βˠAˠɣ -> ˈØˠərʷ!βˠaØˠˠɣ
	ˈØˠAʲrʲəʲʟʲəʷð -> ˈØˠaØˠʲrʲəʲʟʲəʷð
	ˈØˠAʲrʲəʲʟʲəʷð -> ˈØˠaØˠʲrʲəʲʟʲəʷð
	ˈØˠAˠnˠE -> ˈØˠaØˠˠnˠE
	ˈØˠaˠnmxˠaˠrˠA -> ˈØˠaˠnmxˠaˠrˠaØˠ
	ˈØˠAʲtrʲaˠβ -> ˈØˠaØˠʲtrʲaˠβ
	ˈØˠəʷɣdʷaˠrðˠAˠs -> ˈØˠəʷɣdʷaˠrðˠaØˠˠs
	ˈbˠA.E -> ˈbˠaØˠ.E
	ˈbˠAˠɣ -> ˈbˠaØˠˠɣ
	ˈbˠAˠs -> ˈbˠaØˠˠs
	ˈbrˠAˠθ -> ˈbrˠaØˠˠθ
	ˈbrˠAˠθˠaʲr -> ˈbrˠaØˠˠθˠaʲr
	ˈbrʲAˠθˠaˠr -> ˈbrʲaØˠˠθˠaˠr
	ˈbrʲAˠθˠaˠr -> ˈbrʲaØˠˠθˠaˠr
	ˈbʷAʲð -> ˈbʷaØˠʲð
	ˈkʲAˠʟ -> ˈkʲaØˠˠʟ


E -> aØʲ / _
Sample of maximum 20 input/output pairs:

	ˈØˠEˠs -> ˈØˠaØʲˠs
	ˈØˠEˠs -> ˈØˠaØʲˠs
	ˈØˠaʲʟʲE -> ˈØˠaʲʟʲaØʲ
	ˈØˠaʲnkrʲəʲðʲE -> ˈØˠaʲnkrʲəʲðʲaØʲ
	ˈØˠaʲnʲaˠgnˠE -> ˈØˠaʲnʲaˠgnˠaØʲ
	ˈØˠaʲnμnʲE -> ˈØˠaʲnμnʲaØʲ
	ˈØˠərʷ!xrˠE -> ˈØˠərʷ!xrˠaØʲ
	ˈØˠaʲrðʲE -> ˈØˠaʲrðʲaØʲ
	ˈØˠərʷ!ɣˠaʲrʲE -> ˈØˠərʷ!ɣˠaʲrʲaØʲ
	ˈØˠəʷʀnʷəʲɣðʲE -> ˈØˠəʷʀnʷəʲɣðʲaØʲ
	ˈØˠərʷ!ØʷOˠgrˠE -> ˈØˠərʷ!ØʷOˠgrˠaØʲ
	ˈØˠEʲs -> ˈØˠaØʲʲs
	ˈØˠaʲsɴdʲEʲs -> ˈØˠaʲsɴdʲaØʲʲs
	ˈØˠaʲθʲE -> ˈØˠaʲθʲaØʲ
	ˈØˠaʲθɣnʲE -> ˈØˠaʲθɣnʲaØʲ
	ˈØˠaʲθʲəʲrɣʲE -> ˈØˠaʲθʲəʲrɣʲaØʲ
	ˈØˠaʲθrʲəʲɣʲE -> ˈØˠaʲθrʲəʲɣʲaØʲ
	ˈØˠaØˠˠnˠE -> ˈØˠaØˠˠnˠaØʲ
	ˈØˠaˠnˠaˠm-ˈxˠaˠrˠE -> ˈØˠaˠnˠaˠm-ˈxˠaˠrˠaØʲ
	ˈbˠaØˠ.E -> ˈbˠaØˠ.aØʲ


O -> aØʷ / _
Sample of maximum 20 input/output pairs:

	ˈØˠərʷ!ØʷOˠgrˠaØʲ -> ˈØˠərʷ!ØʷaØʷˠgrˠaØʲ
	ˈØˠaˠʟtˠOʲr -> ˈØˠaˠʟtˠaØʷʲr
	ˈbʲO -> ˈbʲaØʷ
	ˈbrʷOˠn -> ˈbrʷaØʷˠn
	ˈkˠaʲɴdlʲOʲr -> ˈkˠaʲɴdlʲaØʷʲr
	ˈkʲaˠθˠaʷrxʷO -> ˈkʲaˠθˠaʷrxʷaØʷ
	ˈkʷaμˠ!θʲəʷnʷOˠl -> ˈkʷaμˠ!θʲəʷnʷaØʷˠl
	ˈkʷOˠrˠaØʲ -> ˈkʷaØʷˠrˠaØʲ
	ˈdʲOʷlʷaˠðˠaˠxt -> ˈdʲaØʷʷlʷaˠðˠaˠxt
	ˈɸʷOˠgrˠaØʲ -> ˈɸʷaØʷˠgrˠaØʲ
	ˈɸʷaʷrʷOʲl -> ˈɸʷaʷrʷaØʷʲl
	ˈgˠO -> ˈgˠaØʷ
	ˈØʲəmʷ!rʷOˠl -> ˈØʲəmʷ!rʷaØʷˠl
	ˈʟʷOˠɣ -> ˈʟʷaØʷˠɣ
	ˈmʷOˠrˠaˠð -> ˈmʷaØʷˠrˠaˠð
	ˈØʷOˠɣˠaØʲ -> ˈØʷaØʷˠɣˠaØʲ
	ˈØʷOʲɣʲaØʲ -> ˈØʷaØʷʲɣʲaØʲ
	ˈØʷOʷμʷəʷn -> ˈØʷaØʷʷμʷəʷn
	ˈprʲaʲgʲaˠptˠOʲr -> ˈprʲaʲgʲaˠptˠaØʷʲr
	ˈtʲəʷnʷOˠl -> ˈtʲəʷnʷaØʷˠl


I -> əØʲ / _
Sample of maximum 20 input/output pairs:

	ˈØˠI.aˠr -> ˈØˠəØʲ.aˠr
	ˈØˠI.aˠr -> ˈØˠəØʲ.aˠr
	ˈØˠaʲsɴdʲIʲs -> ˈØˠaʲsɴdʲəØʲʲs
	ˈØˠaʲsɴdʲIʲs -> ˈØˠaʲsɴdʲəØʲʲs
	ˈbʲI.aˠð -> ˈbʲəØʲ.aˠð
	ˈbrʲIʲɣ -> ˈbrʲəØʲʲɣ
	ˈkˠaØʲʲn-ˈɣnʲIʷμ -> ˈkˠaØʲʲn-ˈɣnʲəØʲʷμ
	ˈdˠaˠɣ-ˈðʷaØʲʲnʲI -> ˈdˠaˠɣ-ˈðʷaØʲʲnʲəØʲ
	ˈdˠaˠɣ-ˈɣnʲIʷμ -> ˈdˠaˠɣ-ˈɣnʲəØʲʷμ
	ˈdʲI.aˠs -> ˈdʲəØʲ.aˠs
	ˈdʲI.aˠs -> ˈdʲəØʲ.aˠs
	ˈdʲIˠðnˠaˠð -> ˈdʲəØʲˠðnˠaˠð
	ˈdʲIˠɣˠaˠl -> ˈdʲəØʲˠɣˠaˠl
	ˈdʲIˠɣˠaˠl -> ˈdʲəØʲˠɣˠaˠl
	ˈdʲIʷlɣʷəʷð -> ˈdʲəØʲʷlɣʷəʷð
	ˈdʲIʷʟtʷəʷð -> ˈdʲəØʲʷʟtʷəʷð
	ˈdʲIʲμʲəʲgʲaˠμ -> ˈdʲəØʲʲμʲəʲgʲaˠμ
	ˈdʲIʷθ -> ˈdʲəØʲʷθ
	ˈdʲIʲdʲU -> ˈdʲəØʲʲdʲU
	ˈdʲI.U -> ˈdʲəØʲ.U


U -> əØʷ / _
Sample of maximum 20 input/output pairs:

	ˈØˠaØˠʲxθʲU -> ˈØˠaØˠʲxθʲəØʷ
	ˈØˠərʲ!ØʲəʲdʲU -> ˈØˠərʲ!ØʲəʲdʲəØʷ
	ˈØˠərʷ!lˠaˠdˠU -> ˈØˠərʷ!lˠaˠdˠəØʷ
	ˈØˠərʲ!μʲəʲdʲU -> ˈØˠərʲ!μʲəʲdʲəØʷ
	ˈØˠaʷbθʷU -> ˈØˠaʷbθʷəØʷ
	ˈbʲaØʲˠstˠaˠdˠU -> ˈbʲaØʲˠstˠaˠdˠəØʷ
	ˈbʲaʷθʷU -> ˈbʲaʷθʷəØʷ
	ˈbʲaʷθʷU -> ˈbʲaʷθʷəØʷ
	ˈbʲəʷβðʷU -> ˈbʲəʷβðʷəØʷ
	ˈbʲəʲθ-ˈβʲaʷθʷU -> ˈbʲəʲθ-ˈβʲaʷθʷəØʷ
	ˈkˠaØʲʲn-ˈðʷUʷθrʷaˠxt -> ˈkˠaØʲʲn-ˈðʷəØʷʷθrʷaˠxt
	ˈkʷaʲmðʲU -> ˈkʷaʲmðʲəØʷ
	ˈkʷUʷl -> ˈkʷəØʷʷl
	ˈkʷUʷʀsʷaˠɣˠaˠð -> ˈkʷəØʷʷʀsʷaˠɣˠaˠð
	ˈkʷUʷʀsʷaˠɣˠaˠð -> ˈkʷəØʷʷʀsʷaˠɣˠaˠð
	ˈdʲaØʲʲgsʲU -> ˈdʲaØʲʲgsʲəØʷ
	ˈdʲaʲθʲəʲdʲU -> ˈdʲaʲθʲəʲdʲəØʷ
	ˈdʲəØʲʲdʲU -> ˈdʲəØʲʲdʲəØʷ
	ˈdʲəØʲ.U -> ˈdʲəØʲ.əØʷ
	ˈdʲU -> ˈdʲəØʷ


%%%%%%%%%%%%%%%     Assimilate consonant colour colour    %%%%%%%%%%%%%%%
%%%% 16. Regressive assimilation of consonant colour
%
0 -> ˠ / (?<=([ˈ]|(!))::C::) _ (?=(::C::){1,2}ˠ)
Sample of maximum 20 input/output pairs:

	ˈØˠərʷ!xrˠaØʲ -> ˈØˠərʷ!xˠrˠaØʲ
	ˈbrˠaØˠˠθ -> ˈbˠrˠaØˠˠθ
	ˈbrˠaØˠˠθˠaʲr -> ˈbˠrˠaØˠˠθˠaʲr
	ˈklˠaʲðʲaˠβ -> ˈkˠlˠaʲðʲaˠβ
	ˈklˠaˠɴd -> ˈkˠlˠaˠɴd
	ˈkrˠaØˠʷβʷəʷð -> ˈkˠrˠaØˠʷβʷəʷð
	ˈØʲadˠarˠ!gnˠaØʲ -> ˈØʲadˠarˠ!gˠnˠaØʲ
	ˈɸlˠaʲθ -> ˈɸˠlˠaʲθ
	ˈɸlˠaʲθʲaˠμnˠaˠxt -> ˈɸˠlˠaʲθʲaˠμnˠaˠxt
	ˈgnˠaØˠˠs -> ˈgˠnˠaØˠˠs
	ˈgrˠaØˠˠð -> ˈgˠrˠaØˠˠð
	ˈgrˠaØˠʲɴʲaØʲ -> ˈgˠrˠaØˠʲɴʲaØʲ
	ˈmrˠaˠθ -> ˈmˠrˠaˠθ
	ˈprˠaʲɴd -> ˈpˠrˠaʲɴd
	ˈskˠaˠrˠaˠð -> ˈsˠkˠaˠrˠaˠð
	ˈsmˠaˠxt -> ˈsˠmˠaˠxt


0 -> ʲ / (?<=([ˈ]|(!))::C::) _ (?=(::C::){1,2}ʲ)
Sample of maximum 20 input/output pairs:

	ˈbrʲaØˠˠθˠaˠr -> ˈbʲrʲaØˠˠθˠaˠr
	ˈbrʲaØˠˠθˠaˠr -> ˈbʲrʲaØˠˠθˠaˠr
	ˈbrʲəØʲʲɣ -> ˈbʲrʲəØʲʲɣ
	ˈbrʲaʲθ -> ˈbʲrʲaʲθ
	ˈbrʲəʲθ -> ˈbʲrʲəʲθ
	ˈbrʲaʲθʲaˠμ -> ˈbʲrʲaʲθʲaˠμ
	ˈbrʲəʲθʲaˠμ -> ˈbʲrʲəʲθʲaˠμ
	ˈbrʲaʲθʲaˠμnˠaˠxt -> ˈbʲrʲaʲθʲaˠμnˠaˠxt
	ˈbrʲəʲθʲaˠμnˠaˠxt -> ˈbʲrʲəʲθʲaˠμnˠaˠxt
	ˈkˠaØʲʲn-ˈɣnʲəØʲʷμ -> ˈkˠaØʲʲn-ˈɣʲnʲəØʲʷμ
	ˈkˠaØʲʲn-ˈskʲaØʲˠl -> ˈkˠaØʲʲn-ˈsʲkʲaØʲˠl
	ˈklʲaʲθ -> ˈkʲlʲaʲθ
	ˈklʲaˠθ -> ˈkʲlʲaˠθ
	ˈklʲaˠθ -> ˈkʲlʲaˠθ
	ˈkrʲaʲdʲaˠμ -> ˈkʲrʲaʲdʲaˠμ
	ˈkrʲəʲðʲaØʲ -> ˈkʲrʲəʲðʲaØʲ
	ˈdˠaˠɣ-ˈɣnʲəØʲʷμ -> ˈdˠaˠɣ-ˈɣʲnʲəØʲʷμ
	ˈdlʲəʲɣʲaˠð -> ˈdʲlʲəʲɣʲaˠð
	ˈdrʷaˠɣ-ˈɣnʲəØʲʷμ -> ˈdrʷaˠɣ-ˈɣʲnʲəØʲʷμ
	ˈɸlʲaˠð -> ˈɸʲlʲaˠð


0 -> ʷ / (?<=([ˈ]|(!))::C::) _ (?=(::C::){1,2}ʷ)
Sample of maximum 20 input/output pairs:

	ˈbrʷaØʷˠn -> ˈbʷrʷaØʷˠn
	ˈklʷaØʲʲnʲaØʲ -> ˈkʷlʷaØʲʲnʲaØʲ
	ˈkrʷaˠx -> ˈkʷrʷaˠx
	ˈkrʷaˠx -> ˈkʷrʷaˠx
	ˈkrʷaˠxˠaˠð -> ˈkʷrʷaˠxˠaˠð
	ˈkrʷaˠt -> ˈkʷrʷaˠt
	ˈkrʷəʷθ -> ˈkʷrʷəʷθ
	ˈdlʷəØʷʷμ -> ˈdʷlʷəØʷʷμ
	ˈdrʷaˠɣ-ˈɣʲnʲəØʲʷμ -> ˈdʷrʷaˠɣ-ˈɣʲnʲəØʲʷμ
	ˈdrʷəØʲ -> ˈdʷrʷəØʲ
	ˈdrʷəØʲ.əØʲ -> ˈdʷrʷəØʲ.əØʲ
	ˈglʷaØˠˠs -> ˈgʷlʷaØˠˠs
	ˈgnʷəØʷʲs -> ˈgʷnʷəØʷʲs
	ˈtrʷaØʷˠkˠaʲrʲaØʲ -> ˈtʷrʷaØʷˠkˠaʲrʲaØʲ


%%%% 17. Progressive assimilation of consonant colour
%
0 -> ˠ / (?<![!]::C::{1,2})(?<=[^Ø]ˠ::C::{1,3}) _
Sample of maximum 20 input/output pairs:

	ˈØˠaˠgˠaˠʟdˠaˠμ -> ˈØˠaˠgˠˠaˠʟˠdˠˠaˠμˠ
	ˈØˠaˠðˠaʲɣ -> ˈØˠaˠðˠˠaʲɣ
	ˈØˠaˠðˠaˠʟtrˠaˠs -> ˈØˠaˠðˠˠaˠʟˠtˠrˠˠaˠsˠ
	ˈØˠaˠðβˠaˠr -> ˈØˠaˠðˠβˠˠaˠrˠ
	ˈØˠaˠðnˠaˠgˠaʷl -> ˈØˠaˠðˠnˠˠaˠgˠˠaʷl
	ˈØˠaˠðrˠaˠð -> ˈØˠaˠðˠrˠˠaˠðˠ
	ˈØˠaØʲˠs -> ˈØˠaØʲˠsˠ
	ˈØˠaØʲˠs -> ˈØˠaØʲˠsˠ
	ˈØˠəØʲ.aˠr -> ˈØˠəØʲ.aˠrˠ
	ˈØˠəØʲ.aˠr -> ˈØˠəØʲ.aˠrˠ
	ˈØˠaʲgnʲaˠð -> ˈØˠaʲgnʲaˠðˠ
	ˈØˠəðʷ!bˠaˠʀt -> ˈØˠəðʷ!bˠaˠʀˠtˠ
	ˈØˠaʲmsʲaˠr -> ˈØˠaʲmsʲaˠrˠ
	ˈØˠaʲnʲaˠgnˠaØʲ -> ˈØˠaʲnʲaˠgˠnˠˠaØʲ
	ˈØˠaʲŋgʲaˠl -> ˈØˠaʲŋgʲaˠlˠ
	ˈØˠaØˠʲɴsʲaˠμ -> ˈØˠaØˠʲɴsʲaˠμˠ
	ˈØˠərʷ!βˠaØˠˠɣ -> ˈØˠərʷ!βˠaØˠˠɣˠ
	ˈØˠərʲ!xʲəʲɴʲaˠx -> ˈØˠərʲ!xʲəʲɴʲaˠxˠ
	ˈØˠərʲ!xʲəʲsʲaˠxt -> ˈØˠərʲ!xʲəʲsʲaˠxˠtˠ
	ˈØˠərʷ!xˠrˠaØʲ -> ˈØˠərʷ!xˠrˠˠaØʲ


0 -> ʲ / (?<![!]::C::{1,2})(?<=[^Ø]ʲ::C::{1,3}) _
Sample of maximum 20 input/output pairs:

	ˈØˠaˠðˠˠaʲɣ -> ˈØˠaˠðˠˠaʲɣʲ
	ˈØˠaØˠʲxθʲəØʷ -> ˈØˠaØˠʲxʲθʲʲəØʷ
	ˈØˠaʲgnʲaˠðˠ -> ˈØˠaʲgʲnʲʲaˠðˠ
	ˈØˠaʲl -> ˈØˠaʲlʲ
	ˈØˠaʲl -> ˈØˠaʲlʲ
	ˈØˠaØˠʲl -> ˈØˠaØˠʲlʲ
	ˈØˠaʲʟʲaØʲ -> ˈØˠaʲʟʲʲaØʲ
	ˈØˠaʲmsʲaˠrˠ -> ˈØˠaʲmʲsʲʲaˠrˠ
	ˈØˠaʲnkrʲəʲðʲaØʲ -> ˈØˠaʲnʲkʲrʲʲəʲðʲʲaØʲ
	ˈØˠaʲnʲaˠgˠnˠˠaØʲ -> ˈØˠaʲnʲʲaˠgˠnˠˠaØʲ
	ˈØˠaʲnɸʲəʷs -> ˈØˠaʲnʲɸʲʲəʷs
	ˈØˠaʲŋgʲaˠlˠ -> ˈØˠaʲŋʲgʲʲaˠlˠ
	ˈØˠaʲnm -> ˈØˠaʲnʲmʲ
	ˈØˠaʲnμnʲaØʲ -> ˈØˠaʲnʲμʲnʲʲaØʲ
	ˈØˠaØˠʲɴsʲaˠμˠ -> ˈØˠaØˠʲɴʲsʲʲaˠμˠ
	ˈØˠaʲbɣʲəʲdʲəʲr -> ˈØˠaʲbʲɣʲʲəʲdʲʲəʲrʲ
	ˈØˠərʷ!ØˠaØˠʲl -> ˈØˠərʷ!ØˠaØˠʲlʲ
	ˈØˠərʲ!xʲəʲɴʲaˠxˠ -> ˈØˠərʲ!xʲəʲɴʲʲaˠxˠ
	ˈØˠərʲ!xʲəʲsʲaˠxˠtˠ -> ˈØˠərʲ!xʲəʲsʲʲaˠxˠtˠ
	ˈØˠaʲrðʲaØʲ -> ˈØˠaʲrʲðʲʲaØʲ


0 -> ʷ / (?<![!]::C::{1,2})(?<=[^Ø]ʷ::C::{1,3}) _
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷaʷβʷəʷr -> ˈØˠaʷkʷʷaʷβʷʷəʷrʷ
	ˈØˠaʷkʷaʷμʷəʷl -> ˈØˠaʷkʷʷaʷμʷʷəʷlʷ
	ˈØˠaˠðˠnˠˠaˠgˠˠaʷl -> ˈØˠaˠðˠnˠˠaˠgˠˠaʷlʷ
	ˈØˠaʲnʲɸʲʲəʷs -> ˈØˠaʲnʲɸʲʲəʷsʷ
	ˈØˠərʷ!kʷəʷr -> ˈØˠərʷ!kʷəʷrʷ
	ˈØˠaʲrʲʲəʷɣʷəʷð -> ˈØˠaʲrʲʲəʷɣʷʷəʷðʷ
	ˈØˠaØˠʲrʲʲəʲʟʲʲəʷð -> ˈØˠaØˠʲrʲʲəʲʟʲʲəʷðʷ
	ˈØˠaØˠʲrʲʲəʲʟʲʲəʷð -> ˈØˠaØˠʲrʲʲəʲʟʲʲəʷðʷ
	ˈØˠərʲ!lʲəʷgʷəʷð -> ˈØˠərʲ!lʲəʷgʷʷəʷðʷ
	ˈØˠəʷʀnʷəʲɣʲðʲʲaØʲ -> ˈØˠəʷʀʷnʷʷəʲɣʲðʲʲaØʲ
	ˈØˠaʲbʲsʲtʲʲəʷnʷəʲdʲ -> ˈØˠaʲbʲsʲtʲʲəʷnʷʷəʲdʲ
	ˈØˠaʷbθʷəØʷ -> ˈØˠaʷbʷθʷʷəØʷ
	ˈØˠaʷstʷəʷð -> ˈØˠaʷsʷtʷʷəʷðʷ
	ˈØˠaʷtlʷəʷɣʷəʷð -> ˈØˠaʷtʷlʷʷəʷɣʷʷəʷðʷ
	ˈØˠəʷɣdʷaˠrˠðˠˠaØˠˠsˠ -> ˈØˠəʷɣʷdʷʷaˠrˠðˠˠaØˠˠsˠ
	ˈbʲaʷθʷəØʷ -> ˈbʲaʷθʷʷəØʷ
	ˈbʲaʷθʷəØʷ -> ˈbʲaʷθʷʷəØʷ
	ˈbʲəʷβðʷəØʷ -> ˈbʲəʷβʷðʷʷəØʷ
	ˈbʲəʲθʲ-ˈβʲaʷθʷəØʷ -> ˈbʲəʲθʲ-ˈβʲaʷθʷʷəØʷ
	ˈbʲəʷθ -> ˈbʲəʷθʷ


%%%% 18. Remove ! and .
%
% The protective environment for prepositional elements and the hiatus marker are no longer necessary.
%
! -> 0 / _
Sample of maximum 20 input/output pairs:

	ˈØˠəðʷ!bˠaˠʀˠtˠ -> ˈØˠəðʷbˠaˠʀˠtˠ
	ˈØˠərʷ!ØˠaØˠʲlʲ -> ˈØˠərʷØˠaØˠʲlʲ
	ˈØˠərʷ!βˠaØˠˠɣˠ -> ˈØˠərʷβˠaØˠˠɣˠ
	ˈØˠərʲ!xʲəʲɴʲʲaˠxˠ -> ˈØˠərʲxʲəʲɴʲʲaˠxˠ
	ˈØˠərʲ!xʲəʲsʲʲaˠxˠtˠ -> ˈØˠərʲxʲəʲsʲʲaˠxˠtˠ
	ˈØˠərʷ!xˠrˠˠaØʲ -> ˈØˠərʷxˠrˠˠaØʲ
	ˈØˠərʷ!kʷəʷrʷ -> ˈØˠərʷkʷəʷrʷ
	ˈØˠərʷ!ɣˠaʲrʲʲaØʲ -> ˈØˠərʷɣˠaʲrʲʲaØʲ
	ˈØˠərʷ!ɣˠaˠlˠ -> ˈØˠərʷɣˠaˠlˠ
	ˈØˠərʲ!ØʲəʲdʲʲəØʷ -> ˈØˠərʲØʲəʲdʲʲəØʷ
	ˈØˠərʷ!lˠaˠdˠˠəØʷ -> ˈØˠərʷlˠaˠdˠˠəØʷ
	ˈØˠərʲ!lʲəʷgʷʷəʷðʷ -> ˈØˠərʲlʲəʷgʷʷəʷðʷ
	ˈØˠərʲ!μʲəʲdʲʲəØʷ -> ˈØˠərʲμʲəʲdʲʲəØʷ
	ˈØˠərʷ!ØʷaØʷˠgˠrˠˠaØʲ -> ˈØˠərʷØʷaØʷˠgˠrˠˠaØʲ
	ˈkʷaμˠ!Øˠaʷkʷʷaʷβʷʷəʷrʷ -> ˈkʷaμˠØˠaʷkʷʷaʷβʷʷəʷrʷ
	ˈkʷaμˠ!Øˠaʲrʲβʲʲaˠʀˠtˠ -> ˈkʷaμˠØˠaʲrʲβʲʲaˠʀˠtˠ
	ˈkʷaμˠ!ØˠaʲrʲlʲʲaØʲ -> ˈkʷaμˠØˠaʲrʲlʲʲaØʲ
	ˈkʷaμˠ!Øˠaʲdʲʲaˠxˠtˠ -> ˈkʷaμˠØˠaʲdʲʲaˠxˠtˠ
	ˈkʷaμˠ!Øˠaˠʟˠnˠˠaˠðˠ -> ˈkʷaμˠØˠaˠʟˠnˠˠaˠðˠ
	ˈkʷaμˠ!Øˠaˠrˠbˠˠaʷsʷ -> ˈkʷaμˠØˠaˠrˠbˠˠaʷsʷ


\. -> 0 / _
Sample of maximum 20 input/output pairs:

	ˈØˠəØʲ.aˠrˠ -> ˈØˠəØʲaˠrˠ
	ˈØˠəØʲ.aˠrˠ -> ˈØˠəØʲaˠrˠ
	ˈbˠaØˠ.aØʲ -> ˈbˠaØˠaØʲ
	ˈbʲəØʲ.aˠðˠ -> ˈbʲəØʲaˠðˠ
	ˈdʲaØˠ.aˠxˠtˠ -> ˈdʲaØˠaˠxˠtˠ
	ˈdʲaØˠ.aˠðˠ -> ˈdʲaØˠaˠðˠ
	ˈdʲaØˠ.aˠðˠ -> ˈdʲaØˠaˠðˠ
	ˈdʲaØˠ.aØˠ -> ˈdʲaØˠaØˠ
	ˈdʲəØʲ.aˠsˠ -> ˈdʲəØʲaˠsˠ
	ˈdʲəØʲ.aˠsˠ -> ˈdʲəØʲaˠsˠ
	ˈdʲəØʲ.əØʷ -> ˈdʲəØʲəØʷ
	ˈdʲəØʲ.aØʲ -> ˈdʲəØʲaØʲ
	ˈdʷrʷʷəØʲ.əØʲ -> ˈdʷrʷʷəØʲəØʲ
	ˈʟˠaØˠ.aØʲ -> ˈʟˠaØˠaØʲ
	ˈʟʲəØʲ.əØʲ -> ˈʟʲəØʲəØʲ
	ˈʟʲəØʲ.aØʲ -> ˈʟʲəØʲaØʲ
	ˈʟʲəØʲ.aØʲ -> ˈʟʲəØʲaØʲ
	ˈmˠaØˠ.aˠμˠ -> ˈmˠaØˠaˠμˠ
	ˈʀʲaØˠ.aØʲ -> ˈʀʲaØˠaØʲ
	ˈʀʲaØˠ.aØʲ -> ˈʀʲaØˠaØʲ


%%%%%%%%%%%%%%%     Housekeeping    %%%%%%%%%%%%%%%
%%%% 20. Reduction of duplicate colour diacritics
%
ʲ -> 0 / _ ʲ
Sample of maximum 20 input/output pairs:

	ˈØˠaØˠʲxʲθʲʲəØʷ -> ˈØˠaØˠʲxʲθʲəØʷ
	ˈØˠaʲgʲnʲʲaˠðˠ -> ˈØˠaʲgʲnʲaˠðˠ
	ˈØˠaʲʟʲʲaØʲ -> ˈØˠaʲʟʲaØʲ
	ˈØˠaʲmʲsʲʲaˠrˠ -> ˈØˠaʲmʲsʲaˠrˠ
	ˈØˠaʲnʲkʲrʲʲəʲðʲʲaØʲ -> ˈØˠaʲnʲkʲrʲəʲðʲaØʲ
	ˈØˠaʲnʲʲaˠgˠnˠˠaØʲ -> ˈØˠaʲnʲaˠgˠnˠˠaØʲ
	ˈØˠaʲnʲɸʲʲəʷsʷ -> ˈØˠaʲnʲɸʲəʷsʷ
	ˈØˠaʲŋʲgʲʲaˠlˠ -> ˈØˠaʲŋʲgʲaˠlˠ
	ˈØˠaʲnʲμʲnʲʲaØʲ -> ˈØˠaʲnʲμʲnʲaØʲ
	ˈØˠaØˠʲɴʲsʲʲaˠμˠ -> ˈØˠaØˠʲɴʲsʲaˠμˠ
	ˈØˠaʲbʲɣʲʲəʲdʲʲəʲrʲ -> ˈØˠaʲbʲɣʲəʲdʲəʲrʲ
	ˈØˠərʲxʲəʲɴʲʲaˠxˠ -> ˈØˠərʲxʲəʲɴʲaˠxˠ
	ˈØˠərʲxʲəʲsʲʲaˠxˠtˠ -> ˈØˠərʲxʲəʲsʲaˠxˠtˠ
	ˈØˠaʲrʲðʲʲaØʲ -> ˈØˠaʲrʲðʲaØʲ
	ˈØˠaʲrʲʲaˠgˠ -> ˈØˠaʲrʲaˠgˠ
	ˈØˠaʲrʲʲaˠxˠˠaˠsˠ -> ˈØˠaʲrʲaˠxˠˠaˠsˠ
	ˈØˠərʷɣˠaʲrʲʲaØʲ -> ˈØˠərʷɣˠaʲrʲaØʲ
	ˈØˠaʲrʲʲəʷɣʷʷəʷðʷ -> ˈØˠaʲrʲəʷɣʷʷəʷðʷ
	ˈØˠaØˠʲrʲʲəʲʟʲʲəʷðʷ -> ˈØˠaØˠʲrʲəʲʟʲəʷðʷ
	ˈØˠaØˠʲrʲʲəʲʟʲʲəʷðʷ -> ˈØˠaØˠʲrʲəʲʟʲəʷðʷ


ʷ -> 0 / _ ʷ
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷʷaʷβʷʷəʷrʷ -> ˈØˠaʷkʷaʷβʷəʷrʷ
	ˈØˠaʷkʷʷaʷμʷʷəʷlʷ -> ˈØˠaʷkʷaʷμʷəʷlʷ
	ˈØˠaʲrʲəʷɣʷʷəʷðʷ -> ˈØˠaʲrʲəʷɣʷəʷðʷ
	ˈØˠərʲlʲəʷgʷʷəʷðʷ -> ˈØˠərʲlʲəʷgʷəʷðʷ
	ˈØˠəʷʀʷnʷʷəʲɣʲðʲaØʲ -> ˈØˠəʷʀʷnʷəʲɣʲðʲaØʲ
	ˈØˠaʲbʲsʲtʲəʷnʷʷəʲdʲ -> ˈØˠaʲbʲsʲtʲəʷnʷəʲdʲ
	ˈØˠaʷbʷθʷʷəØʷ -> ˈØˠaʷbʷθʷəØʷ
	ˈØˠaʷsʷtʷʷəʷðʷ -> ˈØˠaʷsʷtʷəʷðʷ
	ˈØˠaʷtʷlʷʷəʷɣʷʷəʷðʷ -> ˈØˠaʷtʷlʷəʷɣʷəʷðʷ
	ˈØˠəʷɣʷdʷʷaˠrˠðˠˠaØˠˠsˠ -> ˈØˠəʷɣʷdʷaˠrˠðˠˠaØˠˠsˠ
	ˈbʲaʷθʷʷəØʷ -> ˈbʲaʷθʷəØʷ
	ˈbʲaʷθʷʷəØʷ -> ˈbʲaʷθʷəØʷ
	ˈbʲəʷβʷðʷʷəØʷ -> ˈbʲəʷβʷðʷəØʷ
	ˈbʲəʲθʲ-ˈβʲaʷθʷʷəØʷ -> ˈbʲəʲθʲ-ˈβʲaʷθʷəØʷ
	ˈbʷrʷʷaØʷˠnˠ -> ˈbʷrʷaØʷˠnˠ
	ˈbʷəʷnʷʷaˠðˠ -> ˈbʷəʷnʷaˠðˠ
	ˈbʷəʷrʷbʷʷaØʲ -> ˈbʷəʷrʷbʷaØʲ
	ˈkˠaØʲnʲ-ˈðʷəØʷʷθʷrʷʷaˠxˠtˠ -> ˈkˠaØʲnʲ-ˈðʷəØʷθʷrʷaˠxˠtˠ
	ˈkʲaØʲʷdʷβʷʷəʲðʲ -> ˈkʲaØʲʷdʷβʷəʲðʲ
	ˈkʲaˠθˠˠaʷrʷxʷʷaØʷ -> ˈkʲaˠθˠˠaʷrʷxʷaØʷ


ˠ -> 0 / _ ˠ
Sample of maximum 20 input/output pairs:

	ˈØˠaˠgˠˠaˠʟˠdˠˠaˠμˠ -> ˈØˠaˠgˠaˠʟˠdˠaˠμˠ
	ˈØˠaˠðˠˠaʲɣʲ -> ˈØˠaˠðˠaʲɣʲ
	ˈØˠaˠðˠˠaˠʟˠtˠrˠˠaˠsˠ -> ˈØˠaˠðˠaˠʟˠtˠrˠaˠsˠ
	ˈØˠaˠðˠβˠˠaˠrˠ -> ˈØˠaˠðˠβˠaˠrˠ
	ˈØˠaˠðˠnˠˠaˠgˠˠaʷlʷ -> ˈØˠaˠðˠnˠaˠgˠaʷlʷ
	ˈØˠaˠðˠrˠˠaˠðˠ -> ˈØˠaˠðˠrˠaˠðˠ
	ˈØˠaʲnʲaˠgˠnˠˠaØʲ -> ˈØˠaʲnʲaˠgˠnˠaØʲ
	ˈØˠərʷβˠaØˠˠɣˠ -> ˈØˠərʷβˠaØˠɣˠ
	ˈØˠərʷxˠrˠˠaØʲ -> ˈØˠərʷxˠrˠaØʲ
	ˈØˠaʲrʲaˠxˠˠaˠsˠ -> ˈØˠaʲrʲaˠxˠaˠsˠ
	ˈØˠərʷlˠaˠdˠˠəØʷ -> ˈØˠərʷlˠaˠdˠəØʷ
	ˈØˠərʷØʷaØʷˠgˠrˠˠaØʲ -> ˈØˠərʷØʷaØʷˠgˠrˠaØʲ
	ˈØˠaˠlˠmˠsˠˠaˠnˠ -> ˈØˠaˠlˠmˠsˠaˠnˠ
	ˈØˠaˠʟˠtˠˠaØʷʲrʲ -> ˈØˠaˠʟˠtˠaØʷʲrʲ
	ˈØˠaˠʟˠtˠrˠˠaˠmˠ -> ˈØˠaˠʟˠtˠrˠaˠmˠ
	ˈØˠaˠμˠˠaʲrʲaˠsˠ -> ˈØˠaˠμˠaʲrʲaˠsˠ
	ˈØˠaˠμˠˠaʲrʲaˠsˠˠaˠxˠ -> ˈØˠaˠμˠaʲrʲaˠsˠaˠxˠ
	ˈØˠaˠnˠˠaˠðˠ -> ˈØˠaˠnˠaˠðˠ
	ˈØˠaØˠˠnˠˠaØʲ -> ˈØˠaØˠnˠaØʲ
	ˈØˠaˠnˠˠaʲmʲ -> ˈØˠaˠnˠaʲmʲ


%%%% 21. Loss of colour markers before a consonant
%
ˠ -> 0 / Ø[ʲʷˠ]|[aə] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØˠaˠgˠaˠʟˠdˠaˠμˠ -> ˈØˠagˠaʟˠdˠaμˠ
	ˈØˠaˠðˠaʲɣʲ -> ˈØˠaðˠaʲɣʲ
	ˈØˠaˠðˠaˠʟˠtˠrˠaˠsˠ -> ˈØˠaðˠaʟˠtˠrˠasˠ
	ˈØˠaˠðˠβˠaˠrˠ -> ˈØˠaðˠβˠarˠ
	ˈØˠaˠðˠnˠaˠgˠaʷlʷ -> ˈØˠaðˠnˠagˠaʷlʷ
	ˈØˠaˠðˠrˠaˠðˠ -> ˈØˠaðˠrˠaðˠ
	ˈØˠaØʲˠsˠ -> ˈØˠaØʲsˠ
	ˈØˠaØʲˠsˠ -> ˈØˠaØʲsˠ
	ˈØˠəØʲaˠrˠ -> ˈØˠəØʲarˠ
	ˈØˠəØʲaˠrˠ -> ˈØˠəØʲarˠ
	ˈØˠaʲgʲnʲaˠðˠ -> ˈØˠaʲgʲnʲaðˠ
	ˈØˠəðʷbˠaˠʀˠtˠ -> ˈØˠəðʷbˠaʀˠtˠ
	ˈØˠaʲmʲsʲaˠrˠ -> ˈØˠaʲmʲsʲarˠ
	ˈØˠaʲnʲaˠgˠnˠaØʲ -> ˈØˠaʲnʲagˠnˠaØʲ
	ˈØˠaʲŋʲgʲaˠlˠ -> ˈØˠaʲŋʲgʲalˠ
	ˈØˠaØˠʲɴʲsʲaˠμˠ -> ˈØˠaØˠʲɴʲsʲaμˠ
	ˈØˠərʲxʲəʲɴʲaˠxˠ -> ˈØˠərʲxʲəʲɴʲaxˠ
	ˈØˠərʲxʲəʲsʲaˠxˠtˠ -> ˈØˠərʲxʲəʲsʲaxˠtˠ
	ˈØˠaʲrʲaˠgˠ -> ˈØˠaʲrʲagˠ
	ˈØˠaʲrʲaˠxˠaˠsˠ -> ˈØˠaʲrʲaxˠasˠ


ʲ -> 0 / Ø[ʲʷˠ]|[aə] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØˠaðˠaʲɣʲ -> ˈØˠaðˠaɣʲ
	ˈØˠaØˠʲxʲθʲəØʷ -> ˈØˠaØˠxʲθʲəØʷ
	ˈØˠaʲgʲnʲaðˠ -> ˈØˠagʲnʲaðˠ
	ˈØˠaʲlʲ -> ˈØˠalʲ
	ˈØˠaʲlʲ -> ˈØˠalʲ
	ˈØˠaØˠʲlʲ -> ˈØˠaØˠlʲ
	ˈØˠaʲʟʲaØʲ -> ˈØˠaʟʲaØʲ
	ˈØˠaʲmʲsʲarˠ -> ˈØˠamʲsʲarˠ
	ˈØˠaʲnʲkʲrʲəʲðʲaØʲ -> ˈØˠanʲkʲrʲəðʲaØʲ
	ˈØˠaʲnʲagˠnˠaØʲ -> ˈØˠanʲagˠnˠaØʲ
	ˈØˠaʲnʲɸʲəʷsʷ -> ˈØˠanʲɸʲəʷsʷ
	ˈØˠaʲŋʲgʲalˠ -> ˈØˠaŋʲgʲalˠ
	ˈØˠaʲnʲmʲ -> ˈØˠanʲmʲ
	ˈØˠaʲnʲμʲnʲaØʲ -> ˈØˠanʲμʲnʲaØʲ
	ˈØˠaØˠʲɴʲsʲaμˠ -> ˈØˠaØˠɴʲsʲaμˠ
	ˈØˠaʲbʲɣʲəʲdʲəʲrʲ -> ˈØˠabʲɣʲədʲərʲ
	ˈØˠərʷØˠaØˠʲlʲ -> ˈØˠərʷØˠaØˠlʲ
	ˈØˠərʲxʲəʲɴʲaxˠ -> ˈØˠərʲxʲəɴʲaxˠ
	ˈØˠərʲxʲəʲsʲaxˠtˠ -> ˈØˠərʲxʲəsʲaxˠtˠ
	ˈØˠaʲrʲðʲaØʲ -> ˈØˠarʲðʲaØʲ


ʷ -> 0 / Ø[ʲʷˠ]|[aə] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷaʷβʷəʷrʷ -> ˈØˠakʷaβʷərʷ
	ˈØˠaʷkʷaʷμʷəʷlʷ -> ˈØˠakʷaμʷəlʷ
	ˈØˠaðˠnˠagˠaʷlʷ -> ˈØˠaðˠnˠagˠalʷ
	ˈØˠanʲɸʲəʷsʷ -> ˈØˠanʲɸʲəsʷ
	ˈØˠərʷkʷəʷrʷ -> ˈØˠərʷkʷərʷ
	ˈØˠarʲəʷɣʷəʷðʷ -> ˈØˠarʲəɣʷəðʷ
	ˈØˠaØˠrʲəʟʲəʷðʷ -> ˈØˠaØˠrʲəʟʲəðʷ
	ˈØˠaØˠrʲəʟʲəʷðʷ -> ˈØˠaØˠrʲəʟʲəðʷ
	ˈØˠərʲlʲəʷgʷəʷðʷ -> ˈØˠərʲlʲəgʷəðʷ
	ˈØˠəʷʀʷnʷəɣʲðʲaØʲ -> ˈØˠəʀʷnʷəɣʲðʲaØʲ
	ˈØˠabʲsʲtʲəʷnʷədʲ -> ˈØˠabʲsʲtʲənʷədʲ
	ˈØˠaʷbʷθʷəØʷ -> ˈØˠabʷθʷəØʷ
	ˈØˠaʷsʷtʷəʷðʷ -> ˈØˠasʷtʷəðʷ
	ˈØˠaʷtʷlʷəʷɣʷəʷðʷ -> ˈØˠatʷlʷəɣʷəðʷ
	ˈØˠəʷɣʷdʷarˠðˠaØˠsˠ -> ˈØˠəɣʷdʷarˠðˠaØˠsˠ
	ˈbʲaʷθʷəØʷ -> ˈbʲaθʷəØʷ
	ˈbʲaʷθʷəØʷ -> ˈbʲaθʷəØʷ
	ˈbʲəʷβʷðʷəØʷ -> ˈbʲəβʷðʷəØʷ
	ˈbʲəθʲ-ˈβʲaʷθʷəØʷ -> ˈbʲəθʲ-ˈβʲaθʷəØʷ
	ˈbʲəʷθʷ -> ˈbʲəθʷ


%%%% 22. Ensure /ə/ not /a/
%
% Only /ə/ not /a/ occurs in unstressed position for final closed vowels.
%
a -> ə / (?<![ˈ]((Ø[ˠʲʷ])|((::C::[ˠʲʷ]){1,4}))) _ ((::C::[ˠʲʷ])+)(=|#)
Sample of maximum 20 input/output pairs:

	ˈØˠagˠaʟˠdˠaμˠ -> ˈØˠagˠaʟˠdˠəμˠ
	ˈØˠaðˠaɣʲ -> ˈØˠaðˠəɣʲ
	ˈØˠaðˠaʟˠtˠrˠasˠ -> ˈØˠaðˠaʟˠtˠrˠəsˠ
	ˈØˠaðˠβˠarˠ -> ˈØˠaðˠβˠərˠ
	ˈØˠaðˠnˠagˠalʷ -> ˈØˠaðˠnˠagˠəlʷ
	ˈØˠaðˠrˠaðˠ -> ˈØˠaðˠrˠəðˠ
	ˈØˠəØʲarˠ -> ˈØˠəØʲərˠ
	ˈØˠəØʲarˠ -> ˈØˠəØʲərˠ
	ˈØˠagʲnʲaðˠ -> ˈØˠagʲnʲəðˠ
	ˈØˠəðʷbˠaʀˠtˠ -> ˈØˠəðʷbˠəʀˠtˠ
	ˈØˠamʲsʲarˠ -> ˈØˠamʲsʲərˠ
	ˈØˠaŋʲgʲalˠ -> ˈØˠaŋʲgʲəlˠ
	ˈØˠaØˠɴʲsʲaμˠ -> ˈØˠaØˠɴʲsʲəμˠ
	ˈØˠərʲxʲəɴʲaxˠ -> ˈØˠərʲxʲəɴʲəxˠ
	ˈØˠərʲxʲəsʲaxˠtˠ -> ˈØˠərʲxʲəsʲəxˠtˠ
	ˈØˠarʲagˠ -> ˈØˠarʲəgˠ
	ˈØˠarʲaxˠasˠ -> ˈØˠarʲaxˠəsˠ
	ˈØˠərʷɣˠalˠ -> ˈØˠərʷɣˠəlˠ
	ˈØˠalˠmˠsˠanˠ -> ˈØˠalˠmˠsˠənˠ
	ˈØˠaʟˠtˠrˠamˠ -> ˈØˠaʟˠtˠrˠəmˠ
