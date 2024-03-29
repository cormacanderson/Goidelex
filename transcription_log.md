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
%%%%%%%%%%%%%%%    Fortis segments     %%%%%%%%%%%%%%%
%%%% 1. Doubling of radical segments
%
% These are radical segments, stressed and word initial but not mutated.
% Written single in the normalised orthography, they are phonologically equivalent to segments written double elsewhere.
% This change doubles the spelling so that they pattern correctly in the rest of the derivation.
%
% Three contexts are relevant here: i) absolute initial position, ii) after the mid-dot, iii) after non-mutated whitespace.
%
% e.g.
% i) 	gairid -> ggairid
% ii)	as·beir -> as·bbeir
% iii)	as·beir cormmacc -> as·bbeir ccormmac
%
%
0 -> p / (?=^|·|[^ᴸᴺᴴ]/s)p _
Sample of maximum 20 input/output pairs:

	peccad -> ppeccad
	peccthach -> ppeccthach
	pían -> ppían
	pennait -> ppennait
	persan -> ppersan
	popul -> ppopul
	preicept -> ppreicept
	preiceptóir -> ppreiceptóir
	prímit -> pprímit
	proind -> pproind
	praind -> ppraind


0 -> t / (?=^|·|[^ᴸᴺᴴ]/s)t _
Sample of maximum 20 input/output pairs:

	tabairt -> ttabairt
	tabart -> ttabart
	taidbsiu -> ttaidbsiu
	taidchor -> ttaidchor
	taidchur -> ttaidchur
	taidchricc -> ttaidchricc
	taidchrecc -> ttaidchrecc
	táirggiud -> ttáirggiud
	tairisem -> ttairisem
	tairmmthecht -> ttairmmthecht
	tairṅgire -> ttairṅgire
	talam -> ttalam
	tathaír -> ttathaír
	techt -> ttecht
	techtairecht -> ttechtairecht
	tecmmallad -> ttecmmallad
	techtaire -> ttechtaire
	tech -> ttech
	teg -> tteg
	taig -> ttaig


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
	cathair -> ccathair
	caithir -> ccaithir
	céile -> ccéile
	ceist -> cceist
	céilide -> ccéilide
	ceinél -> cceinél
	ceinélae -> cceinélae
	cenn -> ccenn
	censae -> ccensae
	cerdd -> ccerdd


0 -> b / (?=^|·|[^ᴸᴺᴴ]/s)b _
Sample of maximum 20 input/output pairs:

	baë -> bbaë
	bág -> bbág
	bairgen -> bbairgen
	baithes -> bbaithes
	bathais -> bbathais
	baithis -> bbaithis
	ball -> bball
	bás -> bbás
	béimm -> bbéimm
	bél -> bbél
	bélrae -> bbélrae
	ben -> bben
	bendacht -> bbendacht
	béo -> bbéo
	bés -> bbés
	bésad -> bbésad
	béscnae -> bbéscnae
	béstatu -> bbéstatu
	bethu -> bbethu
	biäd -> bbiäd


0 -> d / (?=^|·|[^ᴸᴺᴴ]/s)d _
Sample of maximum 20 input/output pairs:

	dag-duine -> ddag-duine
	dag-doíni -> ddag-doíni
	dag-gníom -> ddag-gníom
	daltae -> ddaltae
	dam -> ddam
	dán -> ddán
	deächt -> ddeächt
	deäd -> ddeäd
	deäd -> ddeäd
	debuith -> ddebuith
	dechor -> ddechor
	dechur -> ddechur
	déide -> ddéide
	déicsiu -> ddéicsiu
	deimnigiud -> ddeimnigiud
	deimnigud -> ddeimnigud
	delb -> ddelb
	demun -> ddemun
	demon -> ddemon
	demon -> ddemon


0 -> g / (?=^|·|[^ᴸᴺᴴ]/s)g _
Sample of maximum 20 input/output pairs:

	gabál -> ggabál
	gabáil -> ggabáil
	gairdde -> ggairdde
	galar -> ggalar
	gáu -> ggáu
	gein -> ggein
	gell -> ggell
	genas -> ggenas
	geinti -> ggeinti
	geintlide -> ggeintlide
	giun -> ggiun
	glúas -> gglúas
	gnás -> ggnás
	gníom -> ggníom
	gnúis -> ggnúis
	goire -> ggoire
	gortae -> ggortae
	grád -> ggrád
	gráinne -> ggráinne
	guide -> gguide


0 -> m / (?=^|·|[^ᴸᴺᴴ]/s)m _
Sample of maximum 20 input/output pairs:

	maäm -> mmaäm
	mám -> mmám
	macc -> mmacc
	machdad -> mmachdad
	machthad -> mmachthad
	maigister -> mmaigister
	maín -> mmaín
	martrae -> mmartrae
	mebul -> mmebul
	méit -> mméit
	mét -> mmét
	menmmae -> mmenmmae
	meirtrech -> mmeirtrech
	mes -> mmes
	míl -> mmíl
	míle -> mmíle
	mílte -> mmílte
	miscuis -> mmiscuis
	mod -> mmod
	moídem -> mmoídem


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

	laë -> llaë
	lám -> llám
	labrad -> llabrad
	laithe -> llaithe
	lánamnas -> llánamnas
	lánae -> llánae
	láine -> lláine
	lann -> llann
	láthar -> lláthar
	legad -> llegad
	léigend -> lléigend
	léire -> lléire
	les -> lles
	lestar -> llestar
	leth -> lleth
	leth -> lleth
	lië -> llië
	lië -> llië
	lí -> llí
	lí -> llí


0 -> r / (?=^|·|[^ᴸᴺᴴ]/s)r _
Sample of maximum 20 input/output pairs:

	rann -> rrann
	rath -> rrath
	reë -> rreë
	ré -> rré
	recht -> rrecht
	rét -> rrét
	réit -> rréit
	rélad -> rrélad
	ríar -> rríar
	ríchtu -> rríchtu
	rí -> rrí
	riuth -> rriuth
	rosc -> rrosc
	rosc -> rrosc
	ruccae -> rruccae
	rún -> rrún


%%%%%%%%%%%%%%%    Orthography of fricatives and stops     %%%%%%%%%%%%%%%
%%%% 2. Orthographic x is xs
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

	eixceptaid -> eixsceptaid


%%%% 3. Orthographic ff is f
%
% In the normalised orthography, <ff> occurs from the gemination of <f>.
% However, <f> and <ff> pattern together.
%
% e.g.
%	níᴴferaid = nífferaid -> níferaid
%
f -> 0 / f _
Sample of maximum 20 input/output pairs:

	iffernn -> ifernn


%%%% 5. Stops after s or a homorganic nasal
%
% <p, t, c> represent fortis segments <pp, tt, cc> after:
% i) <s> (also m in this environment, but only initially), ii) a sonorant <l> or <r>, or iii) a homorganic nasal.
% Further, <t> represents <tt> iv) after <ch>.
% <b, d, g> represent lenis stops <bb, dd, gg> after a homorganic nasal (unless considered reduced by rule 10).
%
% e.g.
% i) 	stair 	-> sttair
%	scél 	-> sccél
% ii)	sacart 	-> sacartt
% iii) 	sant 	-> santt
%	muince 	-> mmuince (by rule 1)
%		-> muincce
% iv)	lucht 	-> llucht (by rule 1)
%		-> lluchtt
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

	apstanait -> apsttanait
	adaltras -> adalttras
	erbert -> erbertt
	airchisecht -> airchisechtt
	altóir -> alttóir
	altramm -> alttramm
	apstal -> apsttal
	apstalach -> apsttalach
	astud -> asttud
	bbendacht -> bbendachtt
	bbéstatu -> bbésttatu
	bbrithemnacht -> bbrithemnachtt
	bbreithemnacht -> bbreithemnachtt
	ccaín-dúthracht -> ccaín-dúthrachtt
	cceist -> cceistt
	ccomairbert -> ccomairbertt
	ccomaitecht -> ccomaitechtt
	ccoimitecht -> ccoimitechtt
	ccuntubart -> ccunttubartt
	ccundubart -> ccundubartt


0 -> c / [slrn] _ (?=c([^h]|#))
Sample of maximum 20 input/output pairs:

	aircor -> airccor
	aincride -> ainccride
	ascnam -> asccnam
	bbéscnae -> bbésccnae
	ccaín-scél -> ccaín-sccél
	ccarcar -> ccarccar
	ccosc -> ccoscc
	ccoscrad -> ccosccrad
	ccumscugud -> ccumsccugud
	ddeiscipul -> ddeisccipul
	ddé-ṡerc -> ddé-ṡercc
	écosc -> écoscc
	epscop -> epsccop
	etarcertt -> etarccertt
	etircertt -> etirccertt
	etarscarad -> etarsccarad
	eixsceptaid -> eixscceptaid
	foircenn -> foirccenn
	forcan -> forccan
	foircital -> foirccital


0 -> m / (?=^|·|[^ᴸᴺᴴ]/s)[s] _ m
Sample of maximum 20 input/output pairs:

	smachtt -> smmachtt


0 -> b / m _ b
Sample of maximum 20 input/output pairs:

	ccimbid -> ccimbbid
	imbed -> imbbed
	imbad -> imbbad
	imbresan -> imbbresan


0 -> d / n _ d
Sample of maximum 20 input/output pairs:

	aisndís -> aisnddís
	bbendachtt -> bbenddachtt
	ccaindléoir -> ccainddléoir
	ccland -> cclandd
	ccondairggile -> cconddairggile
	ccundubartt -> ccunddubartt
	ccuindrech -> ccuinddrech
	écndach -> écnddach
	forband -> forbandd
	indarbbae -> inddarbbae
	indas -> inddas
	indeb -> inddeb
	indírge -> inddírge
	indnaide -> inddnaide
	indocbál -> inddocbál
	lléigend -> lléigendd
	pproind -> pproindd
	ppraind -> ppraindd
	sccríbend -> sccríbendd
	secndap -> secnddap


0 -> g / ṅ _ g
Sample of maximum 20 input/output pairs:

	aiṅgel -> aiṅggel
	ccaiṅgen -> ccaiṅggen
	forṅgaire -> forṅggaire
	fulaṅg -> fulaṅgg
	ttairṅgire -> ttairṅggire


%%%% 6. Clusters pt and ct
%
% The cluster <pt> is rare in Old Irish, occurring only in Latin loans, e.g. preicept. We assume /pt/ for this.
%
% The cluster <ct> is found at times for <cht>, which we prefer in the normalised orthography.
% Elsewhere, it is found in occasional Latin loans, e.g. sanctáir, where we assume /kt/.
%
0 -> t / [pc] _ (?=t([^h]|#))
Sample of maximum 20 input/output pairs:

	eixscceptaid -> eixsccepttaid
	ppreicept -> ppreiceptt
	ppreiceptóir -> ppreicepttóir


0 -> p / p _ (?=t([^h]|#))
Sample of maximum 20 input/output pairs:

	eixsccepttaid -> eixscceppttaid
	ppreiceptt -> ppreicepptt
	ppreicepttóir -> ppreiceppttóir


%%%%%%%%%%%%%%%    Orthography of sonorants     %%%%%%%%%%%%%%%
%%%% 7. ṅ
%
% ref: GOI §24, §33.1, §236
%
% <ṅ> is used in two contexts:
% i) in the combination <ṅg>, representing /ŋ/, distinguished from <ng> representing /nɣ/
% ii) initially, for the nasalisation of a vowel-initial word
%
% e.g.
% i)	iṅgen  -> iŋen 	('nail')
%	ingen 		('daughter')
% ii) 	aᴺathair = aṅathair -> annathair
%
ṅ -> ŋ / _ g
Sample of maximum 20 input/output pairs:

	aiṅggel -> aiŋggel
	ccaiṅggen -> ccaiŋggen
	forṅggaire -> forŋggaire
	fulaṅgg -> fulaŋgg
	ttairṅggire -> ttairŋggire


%%%% 8. nc and nch
%
% <n> is velar before <c, ch>
%
% e.g.
%  	senchas -> seŋchas
%	muince 	-> muincce (by 2.)
%		-> muiŋcce
%
n -> ŋ / _ c
Sample of maximum 20 input/output pairs:

	ainccride -> aiŋccride
	incholnugud -> iŋcholnugud
	senchas -> seŋchas
	ttinchoscc -> ttiŋchoscc


%%%% 9. mp and nt
%
% Before homorganic stops, <m> and <n> are /m/ and /ɴ/ respectively, so are rewritten here as <mm> and <nn>. cf. rule 2.
%
% e.g.
%	aᴺpraind = ampraind
%		-> amppraind (by 2.)
%		-> ammppraind
%
0 -> m / m _ (?=(p|b)([^h]|#))
Sample of maximum 20 input/output pairs:

	ccimbbid -> ccimmbbid
	imbbed -> immbbed
	imbbad -> immbbad
	imbbresan -> immbbresan
	ttemppul -> ttemmppul


0 -> n / n _ (?=(t|d)([^h]|#))
Sample of maximum 20 input/output pairs:

	aisnddís -> aisnnddís
	bbenddachtt -> bbennddachtt
	ccainddléoir -> ccainnddléoir
	cclandd -> cclanndd
	cconddairggile -> cconnddairggile
	ccunttubartt -> ccunnttubartt
	ccunddubartt -> ccunnddubartt
	ccoraintte -> ccorainntte
	ccuinddrech -> ccuinnddrech
	écnddach -> écnnddach
	forbandd -> forbanndd
	ggeintti -> ggeinntti
	ggeinttlide -> ggeinnttlide
	inddarbbae -> innddarbbae
	inddas -> innddas
	inddeb -> innddeb
	inddírge -> innddírge
	inddnaide -> innddnaide
	inddocbál -> innddocbál
	inttliuchtt -> innttliuchtt


%%%% 10. ns and nth
%
% Before <s> and <th> it might be assumed that <n> is also /ɴ/, so rewritten here as <nn>. cf. rule 9.
%
0 -> n / n _ (s|th)
Sample of maximum 20 input/output pairs:

	áinsem -> áinnsem
	ccensae -> ccennsae
	inscce -> innscce
	síans -> síanns
	séns -> sénns


%%%% 11. Reduction of mb, nd, ṅg (optional)
%
% It might be assumed that <mb>, <nd> and <ṅg> have been levelled to /m/, /ɴ/, and /ŋ/ respectively.
%
%
% e.g. 	aᴺpraind = ampraind
%		-> amppraind (by 2.)
%		-> ammppraind (by 8.)
%		-> ammpprainn
%	aᴺbráthair = ambráthair -> ammráthair
%	aᴺdruí = andruí -> annruí
%
% bb -> m / m _
% dd -> n / n _
% gg -> 0 / ŋ _
%%%%%%%%%%%%%%%    Orthography of vowels in hiatus     %%%%%%%%%%%%%%%
%%%% 10. Syllable break for vowels in hiatus
%
% The second of two vowels in hiatus is usually given
% a diaeresis in scholarly orthography of Old Irish. However,
% the syllable break <.> is more common and appropriate for
% phonological representations.
%
% e.g. laë -> la.e, deäd -> de.ad
%
ä -> .a / _
Sample of maximum 20 input/output pairs:

	bbiäd -> bbi.ad
	ddeächtt -> dde.achtt
	ddeäd -> dde.ad
	ddeäd -> dde.ad
	ddiäs -> ddi.as
	ddiäs -> ddi.as
	mmaäm -> mma.am
	ttriär -> ttri.ar


ë -> .e / _
Sample of maximum 20 input/output pairs:

	aiër -> ai.er
	bbaë -> bba.e
	llaë -> lla.e
	llië -> lli.e
	llië -> lli.e
	rreë -> rre.e
	sain-laë -> sain-la.e


ï -> .i / _
Sample of maximum 20 input/output pairs:

	ddruiï -> ddrui.i


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
% symbols: -, ·, :, /., /s, ᴸ, ᴺ, ᴴ
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
% 1ii. Defines the class of vowels (omitting the zero consonant Ø).
%
%%%% 1i. Defining the class of vowels
%
%%%% 1ii. Defining the class of consonants
%
%%%%%%%%%%%%%%%     Boundary markers and stress     %%%%%%%%%%%%%%%
%
% The normalised orthography permits the following boundary markers:
% <-, ·, :, ᴸ, ᴺ, ᴴ, /s (whitespace)> In addition, we use here
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
% While conventionally used for compounds, this can be replaced by a mutation marker and whitespace.
% e.g. sen-máthair ~ senᴸ máthair 'grandmother'
%
% 5) The equals sign <=>, preceding an unstressed syllable. Used before one of the closed class of notae augentes and immediately followed by whitespace.
% e.g. ad·cobra=som 'he desires'
%
% 6) Whitespace < /s (whitespace)>. Used before a new stress group.
%
%%%% 2. Stress assignment
%
% Stress can be assigned in the following contexts:
% i) After a mutation marker, optionally followed by whitespace
% ii) After the mid-dot, colon, or hyphen
% iii) After whitespace, except when the following string contains a mutation marker, a mid-dot, or a colon
% iv) Initially on the line
%
0 -> ˈ / ([ᴸᴺᴴ]/s?)|[·:-]|/s(?![^/s]+[·:])|# _
Sample of maximum 20 input/output pairs:

	ai.er -> ˈai.er
	aibɣidir -> ˈaibɣidir
	abstanaid -> ˈabstanaid
	agalðaμ -> ˈagalðaμ
	akoβor -> ˈakoβor
	akoμol -> ˈakoμol
	aðaiɣ -> ˈaðaiɣ
	aðaltras -> ˈaðaltras
	aðβar -> ˈaðβar
	aðnagul -> ˈaðnagul
	aðrað -> ˈaðrað
	Eidiuð -> ˈEidiuð
	aigneð -> ˈaigneð
	Aiɣθiu -> ˈAiɣθiu
	ail -> ˈail
	ail -> ˈail
	Ail -> ˈAil
	aiʟe -> ˈaiʟe
	aimser -> ˈaimser
	enex -> ˈenex


%%%% 4. Prepositional elements
%
% It is unclear the extent to which prepositional elements assimilate in colour to a following element.
% The following policy is adopted here:
% i) For imm-, ind-, and frith-, we assume assimilation to following i-colour and u-colour, but not to a-colour.
% ii) For com- we assume assimilation to following u-colour and a-colour, but not to i-colour (unless the orthography indicates otherwise.
% iii) For etar-, we do not assume assimilation to following i-colour or u-colour. With etir-, we don not assume assimilation to following u-colour or a-colour.
% iv) For air-/er-, we assume assimilation to following i-colour, u-colour and a-colour (cf. Rule 6)
%
% As this is a closed class, we fully specify these elements here and protect them from the ensuing sound changes
%
ˈim -> ˈØʲəmʲ! / _ ::C::*[ieIE]
Sample of maximum 20 input/output pairs:

	ˈimbeð -> ˈØʲəmʲ!beð
	ˈimbresan -> ˈØʲəmʲ!bresan
	ˈimxist -> ˈØʲəmʲ!xist
	ˈimðiβe -> ˈØʲəmʲ!ðiβe
	ˈimneð -> ˈØʲəmʲ!neð
	ˈimθext -> ˈØʲəmʲ!θext
	ˈimθrEnuɣuð -> ˈØʲəmʲ!θrEnuɣuð


ˈim -> ˈØʲəmʷ! / _
Sample of maximum 20 input/output pairs:

	ˈimbað -> ˈØʲəmʷ!bað
	ˈimxoμark -> ˈØʲəmʷ!xoμark
	ˈimØoɣaiβedu -> ˈØʲəmʷ!Øoɣaiβedu
	ˈimarμus -> ˈØʲəmʷ!arμus
	ˈimrAðuð -> ˈØʲəmʷ!rAðuð
	ˈimrOl -> ˈØʲəmʷ!rOl
	ˈimθAnað -> ˈØʲəmʷ!θAnað
	ˈimθAnuð -> ˈØʲəmʷ!θAnuð
	ˈimθuɣae -> ˈØʲəmʷ!θuɣae


ˈkoμ -> ˈkʷaμʷ! / _ ::C::*[uoUO]
Sample of maximum 20 input/output pairs:

	ˈkoμrorgon -> ˈkʷaμʷ!rorgon


ˈkoμ -> ˈkʷaμˠ! / _
Sample of maximum 20 input/output pairs:

	ˈkoμakoβor -> ˈkʷaμˠ!akoβor
	ˈkoμairβert -> ˈkʷaμˠ!airβert
	ˈkoμairle -> ˈkʷaμˠ!airle
	ˈkoμaidext -> ˈkʷaμˠ!aidext
	ˈkoμalnað -> ˈkʷaμˠ!alnað
	ˈkoμarbus -> ˈkʷaμˠ!arbus
	ˈkoμarðae -> ˈkʷaμˠ!arðae
	ˈkoμnesaμ -> ˈkʷaμˠ!nesaμ
	ˈkoμθinOl -> ˈkʷaμˠ!θinOl


ˈedar -> ˈØʲadˠarˠ! / _
Sample of maximum 20 input/output pairs:

	ˈedarkert -> ˈØʲadˠarˠ!kert
	ˈedardiβe -> ˈØʲadˠarˠ!diβe
	ˈedarskarað -> ˈØʲadˠarˠ!skarað
	ˈedargnae -> ˈØʲadˠarˠ!gnae


ˈedir -> ˈØʲadʲərʲ! / _
Sample of maximum 20 input/output pairs:

	ˈedirkert -> ˈØʲadʲərʲ!kert


ˈer -> ˈØˠərʲ! / _ ::C::*[ieIE]
Sample of maximum 20 input/output pairs:

	ˈerβert -> ˈØˠərʲ!βert
	ˈere -> ˈØˠərʲ!e
	ˈeresxae -> ˈØˠərʲ!esxae
	ˈeres -> ˈØˠərʲ!es


ˈair -> ˈØˠərʷ! / _ ::C::*[uoUO]
Sample of maximum 20 input/output pairs:

	ˈairkor -> ˈØˠərʷ!kor


ˈair -> ˈØʲarˠ! / _ ::C::*[aA]
Sample of maximum 20 input/output pairs:

	ˈairɣaire -> ˈØʲarˠ!ɣaire
	ˈairladu -> ˈØʲarˠ!ladu
	ˈairAil -> ˈØʲarˠ!Ail
	ˈairβAɣ -> ˈØʲarˠ!βAɣ
	ˈairxrae -> ˈØʲarˠ!xrae
	ˈairɣal -> ˈØʲarˠ!ɣal
	ˈairnaiɣðe -> ˈØʲarˠ!naiɣðe


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
% ii, iu
% uu, ui
% əu, əi
%
%
% final vowels: a, ea; ae, e; ai, i; o, eo; u, iu
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
% A vowel must be preceded by a colour marker [ʲʷˠ]. In the phonology, only a consonant can host a colour marker.
% This rule assigns a zero consonant to act as host, where no consonant precedes.
% There are two contexts in which this occurs:
% 1) Initially
% 2) After a prepositional element (see Rule 5)
%
0 -> Ø / [ˈ!] _ ::V::
Sample of maximum 20 input/output pairs:

	ˈai.er -> ˈØai.er
	ˈaibɣidir -> ˈØaibɣidir
	ˈabstanaid -> ˈØabstanaid
	ˈagalðaμ -> ˈØagalðaμ
	ˈakoβor -> ˈØakoβor
	ˈakoμol -> ˈØakoμol
	ˈaðaiɣ -> ˈØaðaiɣ
	ˈaðaltras -> ˈØaðaltras
	ˈaðβar -> ˈØaðβar
	ˈaðnagul -> ˈØaðnagul
	ˈaðrað -> ˈØaðrað
	ˈEidiuð -> ˈØEidiuð
	ˈaigneð -> ˈØaigneð
	ˈAiɣθiu -> ˈØAiɣθiu
	ˈail -> ˈØail
	ˈail -> ˈØail
	ˈAil -> ˈØAil
	ˈaiʟe -> ˈØaiʟe
	ˈaimser -> ˈØaimser
	ˈenex -> ˈØenex


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

	ˈØainax -> ˈØˠəunax
	ˈØaiðbart -> ˈØˠəuðbart
	ˈtaiðxor -> ˈtˠəuðxor
	ˈtaiðxur -> ˈtˠəuðxur
	ˈtairxoμrak -> ˈtˠəurxoμrak


%%%% 7. Long vowels with initial fada
%
% The normalised orthography follows scholarly conventions with respect to placement of the fada.
% These rules rewrite these conventions to facilitate assignment of consonant colour.
% This is necessary at this point in the derivation so that Eoi and Uai do not interfere with the reassignment rules for short vowel.
%
Ae -> aE / _
Sample of maximum 20 input/output pairs:

	ˈØAes -> ˈØaEs
	ˈsAeβ-ˈØabstal -> ˈsaEβ-ˈØabstal
	ˈsAeɣul -> ˈsaEɣul
	ˈsAeθ -> ˈsaEθ
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

	ˈØAuɣdorðAs -> ˈØaOɣdorðAs
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
	ˈØOenur -> ˈØuEnur
	ˈØOeɴtu -> ˈØuEɴtu
	ˈØOeɴtu -> ˈØuEɴtu
	ˈsOerað -> ˈsuErað
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
	ˈkIaʟ -> ˈkiAʟ
	ˈdIa -> ˈdiA
	ˈdIaβul -> ˈdiAβul
	ˈdIaβol -> ˈdiAβol
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

	ˈdIuite -> ˈdiUite


Ua -> uA / _
Sample of maximum 20 input/output pairs:

	ˈbUaið -> ˈbuAið
	ˈkUairt -> ˈkuAirt
	ˈɸUagrae -> ˈɸuAgrae
	ˈɸUaθ -> ˈɸuAθ
	ˈglUas -> ˈgluAs
	ˈØairØUagrae -> ˈØairØuAgrae
	ˈʟUaɣ -> ˈʟuAɣ
	ˈØUaxt -> ˈØuAxt
	ˈØUar -> ˈØuAr
	ˈsUaineμ -> ˈsuAineμ
	ˈtUargun -> ˈtuArgun
	ˈtUarae -> ˈtuArae
	ˈtUaθ -> ˈtuAθ
	ˈØUaβar -> ˈØuAβar
	ˈØUailβe -> ˈØuAilβe
	ˈØUaʟ -> ˈØuAʟ
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
% ii) <a> for <o> between u-colour and a-colour consonants, when preceded by stressed <i>, <u>
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
% 8ii. 	a -> oa: muntar -> muntoar, ilar -> iloarfoircital -> foircitoal, tindnaccul -> tindnoaccol, immarmus -> immoarmus, airlatu -> airloatu, múnad -> múnoad
% 8iii. o -> oa: accoubor -> accouboar, immḟogaibetu -> immḟoagaibetu, áugtordás -> áugtoardás, imchomracc -> imchoamracc, bolad -> boalad
% 8iv. 	u -> au: immoarmus -> immoarmaus, adnacul -> adnacaul, eipeltu -> eipeltau, béstatu -> béstatau
% 8v. 	o -> ou: cotlud -> coutlud, popul -> poupul, accobor -> accoubor, comaccobor -> comaccoubor
% 	i -> iu: deimnigiud -> deimniugud, immról -> iummról, foróil -> fouróil
%	a !-> au: omaldóit
%	e !-> eu: preiceptóir (not preiciuptóir)
%
% 8i.
%
a -> u / (::C::|Ø)+(ˠəu|[ui]|U|Iu)::C::+ _ (?=[ei])
Sample of maximum 20 input/output pairs:

	ˈburbae -> ˈburbue
	ˈkumae -> ˈkumue
	ˈɸoirkidlaið -> ˈɸoirkidluið
	ˈØʲəmʷ!θuɣae -> ˈØʲəmʷ!θuɣue
	ˈØiɴdnaiðe -> ˈØiɴdnuiðe
	ˈØinɣnae -> ˈØinɣnue
	ˈØinɣraim -> ˈØinɣruim
	ˈʟuɣae -> ˈʟuɣue
	ˈʀukae -> ˈʀukue
	ˈtimnae -> ˈtimnue
	ˈØudμaiʟe -> ˈØudμuiʟe


% 8ii.
%
0 -> o / (::C::|Ø)+(ˠəu|[ui]|U|Iu)::C::+ _ (?=a::C::)
Sample of maximum 20 input/output pairs:

	ˈØˠəunax -> ˈØˠəunoax
	ˈbunað -> ˈbunoað
	ˈkaEin-ˈðUθraxt -> ˈkaEin-ˈðUθroaxt
	ˈkuɴtuβart -> ˈkuɴtuβoart
	ˈkuɴduβart -> ˈkuɴduβoart
	ˈkuμduβart -> ˈkuμduβoart
	ˈkuμðuβart -> ˈkuμðuβoart
	ˈkuμanɣ -> ˈkuμoanɣ
	ˈkuμag -> ˈkuμoag
	ˈkuμaxtae -> ˈkuμoaxtae
	ˈkuμsanað -> ˈkuμsoanað
	ˈkuμdax -> ˈkuμdoax
	ˈkUrsaɣað -> ˈkUrsoaɣað
	ˈkUrsaɣað -> ˈkUrsoaɣað
	ˈdUθraxt -> ˈdUθroaxt
	ˈɸoirkidal -> ˈɸoirkidoal
	ˈɸuɣaʟ -> ˈɸuɣoaʟ
	ˈɸulaŋg -> ˈɸuloaŋg
	ˈɸulax -> ˈɸuloax
	ˈØˠəuðbart -> ˈØˠəuðboart


% 8iii.
%
0 -> a / (::C::|Ø)o _ ::C::+([aA]|#)
Sample of maximum 20 input/output pairs:

	ˈØakoβor -> ˈØakoβoar
	ˈØakoμol -> ˈØakoμoal
	ˈØˠərʷ!kor -> ˈØˠərʷ!koar
	ˈØaOɣdorðAs -> ˈØaOɣdoarðAs
	ˈbolað -> ˈboalað
	ˈboθ -> ˈboaθ
	ˈkaEin-ˈxoμrak -> ˈkaEin-ˈxoaμrak
	ˈkoβaðlus -> ˈkoaβaðlus
	ˈkol -> ˈkoal
	ˈkolaiɴ -> ˈkoalaiɴ
	ˈkʷaμˠ!Øakoβor -> ˈkʷaμˠ!Øakoβoar
	ˈkomaEin -> ˈkoamaEin
	ˈkʷaμʷ!rorgon -> ˈkʷaμʷ!rorgoan
	ˈkoɴdairgile -> ˈkoaɴdairgile
	ˈkor -> ˈkoar
	ˈkoraiɴte -> ˈkoaraiɴte
	ˈkorp -> ˈkoarp
	ˈkorp -> ˈkoarp
	ˈkosk -> ˈkoask
	ˈkoskrað -> ˈkoaskrað


% 8iv.
%
0 -> a / (::V::|!)(::C::|Ø)+o?[ea]::C::+ _ u
Sample of maximum 20 input/output pairs:

	ˈØaðnagul -> ˈØaðnagaul
	ˈØʲarˠ!ladu -> ˈØʲarˠ!ladau
	ˈbEstadu -> ˈbEstadau
	ˈkoaβaðlus -> ˈkoaβaðlaus
	ˈkʷaμˠ!Øarbus -> ˈkʷaμˠ!Øarbaus
	ˈØeibeltu -> ˈØeibeltau
	ˈØabaltu -> ˈØabaltau
	ˈØesargun -> ˈØesargaun
	ˈɸoirβθedu -> ˈɸoirβθedau
	ˈØʲəmʷ!Øoaɣaiβedu -> ˈØʲəmʷ!Øoaɣaiβedau
	ˈØʲəmʷ!Øarμus -> ˈØʲəmʷ!Øarμaus
	ˈtiɴdnoakul -> ˈtiɴdnoakaul


% 8v.
%
0 -> u / (::C::|Ø)[iuo] _ (?=::C::+O)
Sample of maximum 20 input/output pairs:

	ˈkʷaμˠ!θinOl -> ˈkʷaμˠ!θiunOl
	ˈɸorOil -> ˈɸourOil
	ˈtinOl -> ˈtiunOl


0 -> u / (::C::|Ø)::V:: _ (?=::C::+[ouU])
Sample of maximum 20 input/output pairs:

	ˈØakoβoar -> ˈØaukouβoar
	ˈØakoμoal -> ˈØaukouμoal
	ˈØairliguð -> ˈØairliuguð
	ˈØabθu -> ˈØaubθu
	ˈØairiɣuð -> ˈØairiuɣuð
	ˈØastuð -> ˈØaustuð
	ˈØatluɣuð -> ˈØautluuɣuð
	ˈbeθu -> ˈbeuθu
	ˈbiβðu -> ˈbiuβðu
	ˈbiθ-ˈβeθu -> ˈbiθ-ˈβeuθu
	ˈbunoað -> ˈbuunoað
	ˈburbue -> ˈbuurbue
	ˈkaEin-ˈðUθroaxt -> ˈkaEin-ˈðUuθroaxt
	ˈkEdβuið -> ˈkEudβuið
	ˈkeθarxo -> ˈkeθaurxo
	ˈkoβuir -> ˈkouβuir
	ˈkoguβus -> ˈkouguuβus
	ˈkʷaμˠ!Øakoβoar -> ˈkʷaμˠ!Øaukouβoar
	ˈkʷaμʷ!rorgoan -> ˈkʷaμʷ!rourgoan
	ˈkuɴtuβoart -> ˈkuuɴtuuβoart


%%%% 9. Rewriting short and hiatus vowels
%
% These rules rewrite short vowels for colour assignment
%
% 9i. Adds a vowel after a short vowel for colour assignment, also in hiatus.
% 9ii. Raises the first vowel in hiatus, where only /ə/ is permitted after i-colour or u-colour.
% 9iii. Adds a vowel before a short vowel for colour assignment.
% 9iv. Rewrites the second vowel in hiatus for colour assignment.
%
% 9i.
%
0 -> i / (::C::|Ø)i _ (?=::C::|\.)
Sample of maximum 20 input/output pairs:

	ˈØaibɣidir -> ˈØaibɣiidiir
	ˈØairxiɴex -> ˈØairxiiɴex
	ˈØairxisext -> ˈØairxiisext
	ˈØairidiu -> ˈØairiidiu
	ˈØairμidiu -> ˈØairμiidiu
	ˈØaiθirɣe -> ˈØaiθiirɣe
	ˈØaiθriɣe -> ˈØaiθriiɣe
	ˈØaiθis -> ˈØaiθiis
	ˈØaiŋkriðe -> ˈØaiŋkriiðe
	ˈØainim -> ˈØainiim
	ˈØAiriʟiuð -> ˈØAiriiʟiuð
	ˈbaiθis -> ˈbaiθiis
	ˈbi.að -> ˈbii.að
	ˈbiθ-ˈβeuθu -> ˈbiiθ-ˈβeuθu
	ˈbriθ -> ˈbriiθ
	ˈbriθeμ -> ˈbriiθeμ
	ˈbriθeμnaxt -> ˈbriiθeμnaxt
	ˈkaiθir -> ˈkaiθiir
	ˈkEiliðe -> ˈkEiliiðe
	ˈkimbið -> ˈkiimbiið


0 -> u / (::C::|Ø)u _ (?=::C::|\.)
Sample of maximum 20 input/output pairs:

	ˈØairliuguð -> ˈØairliuguuð
	ˈØairiuɣuð -> ˈØairiuɣuuð
	ˈØaustuð -> ˈØaustuuð
	ˈØautluuɣuð -> ˈØautluuɣuuð
	ˈkouguuβus -> ˈkouguuβuus
	ˈkoudluð -> ˈkoudluuð
	ˈkrAuβuð -> ˈkrAuβuuð
	ˈkruθ -> ˈkruuθ
	ˈkuuβus -> ˈkuuβuus
	ˈkuuμskuuɣuð -> ˈkuuμskuuɣuuð
	ˈkuudruumus -> ˈkuudruumuus
	ˈdeuxur -> ˈdeuxuur
	ˈdeiμniuɣuð -> ˈdeiμniuɣuuð
	ˈdeuμun -> ˈdeuμuun
	ˈdEunuμ -> ˈdEunuuμ
	ˈdeiskiubul -> ˈdeiskiubuul
	ˈdiAβul -> ˈdiAβuul
	ˈdIulɣuð -> ˈdIulɣuuð
	ˈdIultuð -> ˈdIultuuð
	ˈdouμun -> ˈdouμuun


0 -> a / (::C::|Ø)[aeo] _ (?=::C::|\.)
Sample of maximum 20 input/output pairs:

	ˈØabstanaid -> ˈØaabstaanaid
	ˈØagalðaμ -> ˈØaagaalðaaμ
	ˈØaðaiɣ -> ˈØaaðaiɣ
	ˈØaðaltras -> ˈØaaðaaltraas
	ˈØaðβar -> ˈØaaðβaar
	ˈØaðnagaul -> ˈØaaðnaagaul
	ˈØaðrað -> ˈØaaðraað
	ˈØaigneð -> ˈØaigneað
	ˈØaimser -> ˈØaimsear
	ˈØˠəinex -> ˈØˠəineax
	ˈØaiŋgel -> ˈØaiŋgeal
	ˈØAiɴseμ -> ˈØAiɴseaμ
	ˈØˠərʲ!βert -> ˈØˠərʲ!βeart
	ˈØairxiiɴex -> ˈØairxiiɴeax
	ˈØairxiisext -> ˈØairxiiseaxt
	ˈØaireg -> ˈØaireag
	ˈØairexas -> ˈØaireaxaas
	ˈØalmsan -> ˈØaalmsaan
	ˈØaltOir -> ˈØaaltOir
	ˈØaltram -> ˈØaaltraam


% 9ii.
%
e -> i / _ a\.
Sample of maximum 20 input/output pairs:

	ˈdea.axt -> ˈdia.axt
	ˈdea.að -> ˈdia.að
	ˈdea.að -> ˈdia.að
	ˈʀea.e -> ˈʀia.e


% 9iii.
%
0 -> a / _ (?=a[aiu]::C::)|a-
Sample of maximum 20 input/output pairs:

	ˈØaibɣiidiir -> ˈØaaibɣiidiir
	ˈØaabstaanaid -> ˈØaaabstaaanaaid
	ˈØaagaalðaaμ -> ˈØaaagaaalðaaaμ
	ˈØaukouβoar -> ˈØaaukouβoar
	ˈØaukouμoal -> ˈØaaukouμoal
	ˈØaaðaiɣ -> ˈØaaaðaaiɣ
	ˈØaaðaaltraas -> ˈØaaaðaaaltraaas
	ˈØaaðβaar -> ˈØaaaðβaaar
	ˈØaaðnaagaul -> ˈØaaaðnaaagaaul
	ˈØaaðraað -> ˈØaaaðraaað
	ˈØaigneað -> ˈØaaigneað
	ˈØail -> ˈØaail
	ˈØail -> ˈØaail
	ˈØaiʟe -> ˈØaaiʟe
	ˈØaimsear -> ˈØaaimsear
	ˈØaiŋgeal -> ˈØaaiŋgeal
	ˈØainm -> ˈØaainm
	ˈØainμne -> ˈØaainμne
	ˈØairxiiɴeax -> ˈØaairxiiɴeax
	ˈØairxiiseaxt -> ˈØaairxiiseaxt


0 -> i / _ (?=[ei][aiu]::C::)|[ie]-
Sample of maximum 20 input/output pairs:

	ˈØaaibɣiidiir -> ˈØaaibɣiiidiiir
	ˈØEidiuð -> ˈØEidiiuð
	ˈØaaigneað -> ˈØaaignieað
	ˈØaaimsear -> ˈØaaimsiear
	ˈØˠəineax -> ˈØˠəinieax
	ˈØaaiŋgeal -> ˈØaaiŋgieal
	ˈØAiɴseaμ -> ˈØAiɴsieaμ
	ˈØˠərʲ!βeart -> ˈØˠərʲ!βieart
	ˈØaairxiiɴeax -> ˈØaairxiiiɴieax
	ˈØaairxiiseaxt -> ˈØaairxiiisieaxt
	ˈØaaireag -> ˈØaairieag
	ˈØaaireaxaaas -> ˈØaairieaxaaas
	ˈØaairiidiu -> ˈØaairiiidiu
	ˈØaairliuguuð -> ˈØaairliiuguuð
	ˈØaairμiidiu -> ˈØaairμiiidiu
	ˈØaaiθiirɣe -> ˈØaaiθiiirɣe
	ˈØaaiθriiɣe -> ˈØaaiθriiiɣe
	ˈØaaiθiis -> ˈØaaiθiiis
	ˈØaaaμaaireas -> ˈØaaaμaairieas
	ˈØaaaμaaireasaaax -> ˈØaaaμaairieasaaax


0 -> u / _ (?=[ou][aiu]::C::)|[ou]-
Sample of maximum 20 input/output pairs:

	ˈØaaukouβoar -> ˈØaaukuouβuoar
	ˈØaaukouμoal -> ˈØaaukuouμuoal
	ˈØˠəunoax -> ˈØˠəunuoax
	ˈØˠərʷ!koar -> ˈØˠərʷ!kuoar
	ˈØaairliiuguuð -> ˈØaairliiuguuuð
	ˈØaairiiuɣuuð -> ˈØaairiiuɣuuuð
	ˈØaaustuuð -> ˈØaaustuuuð
	ˈØaautluuɣuuð -> ˈØaautluuuɣuuuð
	ˈØaOɣdoarðAs -> ˈØaOɣduoarðAs
	ˈboalaaað -> ˈbuoalaaað
	ˈbuiðe -> ˈbuuiðe
	ˈbuiɴe -> ˈbuuiɴe
	ˈbuiθ -> ˈbuuiθ
	ˈboaθ -> ˈbuoaθ
	ˈbuunoað -> ˈbuuunuoað
	ˈbuurbue -> ˈbuuurbue
	ˈbuirbe -> ˈbuuirbe
	ˈkaEin-ˈxoaμraaak -> ˈkaEin-ˈxuoaμraaak
	ˈkaEin-ˈðUuθroaxt -> ˈkaEin-ˈðUuθruoaxt
	ˈkEudβuið -> ˈkEudβuuið


0 -> a / \.[oea] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØai.er -> ˈØai.ear
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
% e.g. umaldóit
%
% 10ii. Elsewhere, the quality of a preceding consonant can be straightforwardly inferred by the vowel representation.
% These rules assign short vowels before long vowels for colour assignment
%
% 10iii. In many cases, the normalised orthography of long vowels is the same whether an a-colour or u-colour consonant follows.
% In most cases (11iv.) we take the following vowel to be indicative of consonant colour, but the situation is less clear with final consonants.
% For ó before a final consonant, e.g. brón, a-colour is assumed.
%
% The normalised orthography underdetermines the phonology in the case of é. Here, we assume as default that it represents CʲaØʲ etc.
% Goidinflex manually annotates cases where it is rather CʲaØʷCˠ, i.e. the é that alternates with éo and éoi in certain paradigms.
%
% Similarly, we cannot tell from the normalised orthography if éi represents CʲaØʲCʲ (iéi) or CʲaØˠCʲ (iái). The latter alternates with ía.
% Here, we assume the representation CʲaØʲCʲ.
%
% 10iv. When a vowel follows, we have taken this to indicate the colour of the preceding consonant.
%
% 10i.
%
0 -> a / a::C::+ _ O
Sample of maximum 20 input/output pairs:

	ˈØaaaltOir -> ˈØaaaltaOir
	ˈprieigieaptOir -> ˈprieigieaptaOir
	ˈØuuuμuoalðOid -> ˈØuuuμuoalðaOid
	ˈØuoaμaaalðOid -> ˈØuoaμaaalðaOid


% 10ii.
%
0 -> a / ::C::|Ø _ A
Sample of maximum 20 input/output pairs:

	ˈØAiɣθiu -> ˈØaAiɣθiu
	ˈØAil -> ˈØaAil
	ˈØAiɴsieaμ -> ˈØaAiɴsieaμ
	ˈØAnae -> ˈØaAnae
	ˈØAiriiiʟiiuð -> ˈØaAiriiiʟiiuð
	ˈØAitrieaβ -> ˈØaAitrieaβ
	ˈØaOɣduoarðAs -> ˈØaOɣduoarðaAs
	ˈbAɣ -> ˈbaAɣ
	ˈbAs -> ˈbaAs
	ˈbrAθ -> ˈbraAθ
	ˈbrAθaair -> ˈbraAθaair
	ˈkrAuβuuuð -> ˈkraAuβuuuð
	ˈdAn -> ˈdaAn
	ˈduu-ˈØAlaaiɣ -> ˈduu-ˈØaAlaaiɣ
	ˈɸAilte -> ˈɸaAilte
	ˈɸAiθ -> ˈɸaAiθ
	ˈgaaaβAl -> ˈgaaaβaAl
	ˈgaaaβAil -> ˈgaaaβaAil
	ˈgnAs -> ˈgnaAs
	ˈgrAð -> ˈgraAð


0 -> i / ::C::|Ø _ [EI]
Sample of maximum 20 input/output pairs:

	ˈØEidiiuð -> ˈØiEidiiuð
	ˈØaaisɴdIs -> ˈØaaisɴdiIs
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
	ˈkieinElae -> ˈkieiniElae
	ˈkEsaaað -> ˈkiEsaaað
	ˈkEd -> ˈkiEd
	ˈkEudβuuið -> ˈkiEudβuuið
	ˈkuoigEilsiiine -> ˈkuoigiEilsiiine


0 -> u / ::C::|Ø _ [OU]
Sample of maximum 20 input/output pairs:

	ˈbrOn -> ˈbruOn
	ˈkaEin-ˈðUuθruoaxt -> ˈkaEin-ˈðuUuθruoaxt
	ˈkʷaμˠ!θiiunOl -> ˈkʷaμˠ!θiiunuOl
	ˈkOrae -> ˈkuOrae
	ˈkUl -> ˈkuUl
	ˈkUursuoaɣaaað -> ˈkuUursuoaɣaaað
	ˈkUursuoaɣaaað -> ˈkuUursuoaɣaaað
	ˈdlUμ -> ˈdluUμ
	ˈdUil -> ˈduUil
	ˈdUilxiiiɴe -> ˈduUilxiiiɴe
	ˈdUuθruoaxt -> ˈduUuθruoaxt
	ˈɸOgrae -> ˈɸuOgrae
	ˈɸuourOil -> ˈɸuouruOil
	ˈgnUis -> ˈgnuUis
	ˈØʲəmʷ!rOl -> ˈØʲəmʷ!ruOl
	ˈØaairØOgrae -> ˈØaairØuOgrae
	ˈʟOɣ -> ˈʟuOɣ
	ˈmOraaað -> ˈmuOraaað
	ˈmUunuoað -> ˈmuUunuoað
	ˈmUinieað -> ˈmuUinieað


% 10iii.
%
0 -> i / I _ ::C::+(-|·|#)
Sample of maximum 20 input/output pairs:

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
	ˈtiiuɴtuUθ -> ˈtiiuɴtuUuθ


0 -> a / [AEO] _ ::C::+(-|·|#)
Sample of maximum 20 input/output pairs:

	ˈØaEs -> ˈØaEas
	ˈØaOɣduoarðaAs -> ˈØaOɣduoarðaAas
	ˈbaAɣ -> ˈbaAaɣ
	ˈbaAs -> ˈbaAas
	ˈbiEl -> ˈbiEal
	ˈbiEs -> ˈbiEas
	ˈbraAθ -> ˈbraAaθ
	ˈbruOn -> ˈbruOan
	ˈkaEin-ˈskiEl -> ˈkaEin-ˈskiEal
	ˈkieiniEl -> ˈkieiniEal
	ˈkiEd -> ˈkiEad
	ˈkiAʟ -> ˈkiAaʟ
	ˈkuoiμiEd -> ˈkuoiμiEad
	ˈkʷaμˠ!θiiunuOl -> ˈkʷaμˠ!θiiunuOal
	ˈdaAn -> ˈdaAan
	ˈØiEd -> ˈØiEad
	ˈɸiAx -> ˈɸiAax
	ˈɸuAθ -> ˈɸuAaθ
	ˈgaaaβaAl -> ˈgaaaβaAal
	ˈgluAs -> ˈgluAas


% 10iv.
%
0 -> a / [AEIOU] _ ::C::+[a]
Sample of maximum 20 input/output pairs:

	ˈØaAnae -> ˈØaAanae
	ˈbiElrae -> ˈbiEalrae
	ˈbiEsaaað -> ˈbiEasaaað
	ˈbiEsknae -> ˈbiEasknae
	ˈbiEstaaadau -> ˈbiEastaaadau
	ˈbraAθaair -> ˈbraAaθaair
	ˈbriAθaaar -> ˈbriAaθaaar
	ˈkieiniElae -> ˈkieiniEalae
	ˈkiEsaaað -> ˈkiEasaaað
	ˈkuOrae -> ˈkuOarae
	ˈdiEnaaaμ -> ˈdiEanaaaμ
	ˈdiOlaaaðaaaxt -> ˈdiOalaaaðaaaxt
	ˈdiIðnaaað -> ˈdiIaðnaaað
	ˈdiIɣaaal -> ˈdiIaɣaaal
	ˈduEnaaaxt -> ˈduEanaaaxt
	ˈduu-ˈØaAlaaiɣ -> ˈduu-ˈØaAalaaiɣ
	ˈØiEgɴdaaax -> ˈØiEagɴdaaax
	ˈØiEdaaax -> ˈØiEadaaax
	ˈØiEdraaað -> ˈØiEadraaað
	ˈɸiAðnaaise -> ˈɸiAaðnaaise


0 -> i / [AEIOU] _ ::C::+[ie]
Sample of maximum 20 input/output pairs:

	ˈdiIμiiigieaμ -> ˈdiIiμiiigieaμ
	ˈdiIdiu -> ˈdiIidiu
	ˈɸiIriAnuuuɣuuuð -> ˈɸiIiriAnuuuɣuuuð
	ˈɸiIriiiɴe -> ˈɸiIiriiiɴe
	ˈØiiiɴdiIrɣe -> ˈØiiiɴdiIirɣe
	ˈmiIle -> ˈmiIile
	ˈmiIlte -> ˈmiIilte
	ˈpriIμiiid -> ˈpriIiμiiid
	ˈskriIβieaɴd -> ˈskriIiβieaɴd
	ˈskriIβieaɴt -> ˈskriIiβieaɴt


0 -> u / [AEIOU] _ ::C::+[ou]
Sample of maximum 20 input/output pairs:

	ˈØaOɣduoarðaAas -> ˈØaOuɣduoarðaAas
	ˈdiAβuuul -> ˈdiAuβuuul
	ˈdiAβuoal -> ˈdiAuβuoal
	ˈɸiIiriAnuuuɣuuuð -> ˈɸiIiriAunuuuɣuuuð
	ˈØuEnuuur -> ˈØuEunuuur
	ˈØuEɴtu -> ˈØuEuɴtu
	ˈØuEɴtu -> ˈØuEuɴtu
	ˈsaEɣuuul -> ˈsaEuɣuuul
	ˈtuArguuun -> ˈtuAurguuun


0 -> i / ::V::::C::+ _ [ei]#
Sample of maximum 20 input/output pairs:

	ˈØaaiʟe -> ˈØaaiʟie
	ˈØaainμne -> ˈØaainμnie
	ˈØaairðe -> ˈØaairðie
	ˈØʲarˠ!ɣaaire -> ˈØʲarˠ!ɣaairie
	ˈØaaiθe -> ˈØaaiθie
	ˈØaaiθɣne -> ˈØaaiθɣnie
	ˈØaaiθiiirɣe -> ˈØaaiθiiirɣie
	ˈØaaiθriiiɣe -> ˈØaaiθriiiɣie
	ˈØaaiŋkriiiðe -> ˈØaaiŋkriiiðie
	ˈbuuiðe -> ˈbuuiðie
	ˈbuuiɴe -> ˈbuuiɴie
	ˈbuuirbe -> ˈbuuirbie
	ˈkiEile -> ˈkiEilie
	ˈkiEiliiiðe -> ˈkiEiliiiðie
	ˈkluEine -> ˈkluEinie
	ˈkuoigiEilsiiine -> ˈkuoigiEilsiiinie
	ˈkuoiβse -> ˈkuoiβsie
	ˈkʷaμˠ!Øaairle -> ˈkʷaμˠ!Øaairlie
	ˈkuoaɴdaairgiiile -> ˈkuoaɴdaairgiiilie
	ˈkuoaraaiɴte -> ˈkuoaraaiɴtie


0 -> u / ::V::::C::+ _ [ou]#
Sample of maximum 20 input/output pairs:

	ˈØaaubθu -> ˈØaaubθuu
	ˈbieuθu -> ˈbieuθuu
	ˈbiiuβðu -> ˈbiiuβðuu
	ˈbiiiθ-ˈβieuθu -> ˈbiiiθ-ˈβieuθuu
	ˈkieaθaaurxo -> ˈkieaθaaurxuo
	ˈɴieaβ-ˈμaaurtu -> ˈɴieaβ-ˈμaaurtuu
	ˈØuEuɴtu -> ˈØuEuɴtuu
	ˈØuEuɴtu -> ˈØuEuɴtuu
	ˈʀiIuxtu -> ˈʀiIuxtuu
	ˈtiIuxtu -> ˈtiIuxtuu


0 -> a / ::V::::C::+ _ a#
Sample of maximum 20 input/output pairs:

	ˈØaaanmxaaara -> ˈØaaanmxaaaraa


%%%% 12. Final vowels and first of two in hiatus as long vowels
%
% It is convenient in the derivation to treat final vowels and the first of two in hiatus as long and this rule does that.
%
i -> I / _ (\.|#)
Sample of maximum 20 input/output pairs:

	ˈØai.ear -> ˈØaI.ear
	ˈbii.aað -> ˈbiI.aað
	ˈdaaaɣ-ˈðuEinii -> ˈdaaaɣ-ˈðuEiniI
	ˈdii.aas -> ˈdiI.aas
	ˈdii.aas -> ˈdiI.aas
	ˈdii.u -> ˈdiI.u
	ˈdrui.i -> ˈdruI.I
	ˈduEinii -> ˈduEiniI
	ˈgieiɴtii -> ˈgieiɴtiI
	ˈʟii.e -> ˈʟiI.e
	ˈʟii.e -> ˈʟiI.e
	ˈØuEiɣii -> ˈØuEiɣiI
	ˈtrii.aar -> ˈtriI.aar


u -> U / _ (\.|#)
Sample of maximum 20 input/output pairs:

	ˈØaAiɣθiu -> ˈØaAiɣθiU
	ˈØaairiiidiu -> ˈØaairiiidiU
	ˈØaairμiiidiu -> ˈØaairμiiidiU
	ˈØaaubθuu -> ˈØaaubθuU
	ˈØʲarˠ!laaadau -> ˈØʲarˠ!laaadaU
	ˈbiEastaaadau -> ˈbiEastaaadaU
	ˈbieuθuu -> ˈbieuθuU
	ˈbiiuβðuu -> ˈbiiuβðuU
	ˈbiiiθ-ˈβieuθuu -> ˈbiiiθ-ˈβieuθuU
	ˈkuoimðiu -> ˈkuoimðiU
	ˈdiEigsiu -> ˈdiEigsiU
	ˈdieiθiiidiu -> ˈdieiθiiidiU
	ˈdiI.u -> ˈdiI.U
	ˈdiIidiu -> ˈdiIidiU
	ˈØieibiealtau -> ˈØieibiealtaU
	ˈØaaabaaaltau -> ˈØaaabaaaltaU
	ˈØieibiiiltiu -> ˈØieibiiiltiU
	ˈɸuoaðaaidiu -> ˈɸuoaðaaidiU
	ˈɸuoirβθieadau -> ˈɸuoirβθieadaU
	ˈɸuEisiiidiu -> ˈɸuEisiiidiU


e -> E / _ #
Sample of maximum 20 input/output pairs:

	ˈØaaiʟie -> ˈØaaiʟiE
	ˈØaainμnie -> ˈØaainμniE
	ˈØaairðie -> ˈØaairðiE
	ˈØʲarˠ!ɣaairie -> ˈØʲarˠ!ɣaairiE
	ˈØaaiθie -> ˈØaaiθiE
	ˈØaaiθɣnie -> ˈØaaiθɣniE
	ˈØaaiθiiirɣie -> ˈØaaiθiiirɣiE
	ˈØaaiθriiiɣie -> ˈØaaiθriiiɣiE
	ˈØaAanae -> ˈØaAanaE
	ˈØaaanaaam-ˈxaaarae -> ˈØaaanaaam-ˈxaaaraE
	ˈØaainieagnae -> ˈØaainieagnaE
	ˈØaaiŋkriiiðie -> ˈØaaiŋkriiiðiE
	ˈbaa.e -> ˈbaa.E
	ˈbiEalrae -> ˈbiEalraE
	ˈbiEasknae -> ˈbiEasknaE
	ˈbuuiðie -> ˈbuuiðiE
	ˈbuuiɴie -> ˈbuuiɴiE
	ˈbuuurbue -> ˈbuuurbuE
	ˈbuuirbie -> ˈbuuirbiE
	ˈkaaarae -> ˈkaaaraE


o -> O / _ #
Sample of maximum 20 input/output pairs:

	ˈkieaθaaurxuo -> ˈkieaθaaurxuO


a -> A / _ (\.|#)
Sample of maximum 20 input/output pairs:

	ˈØaaanmxaaaraa -> ˈØaaanmxaaaraA
	ˈbaa.E -> ˈbaA.E
	ˈdia.aaxt -> ˈdiA.aaxt
	ˈdia.aað -> ˈdiA.aað
	ˈdia.aað -> ˈdiA.aað
	ˈʟaa.E -> ˈʟaA.E
	ˈmaa.aaμ -> ˈmaA.aaμ
	ˈʀia.E -> ˈʀiA.E
	ˈsaain-ˈlaa.E -> ˈsaain-ˈlaA.E


%%%%%%%%%%%%%%%     Consonant colour assignment     %%%%%%%%%%%%%%%
%%%% 15. Consonant colour before vowels
%
% This rule assigns consonant colour before vowels.
%
i -> ʲ / (?<=::C::+|Ø) _ ::V::
Sample of maximum 20 input/output pairs:

	ˈØaaibɣiiidiiir -> ˈØaaibɣʲiidʲiir
	ˈØiEidiiuð -> ˈØʲEidʲiuð
	ˈØaaignieað -> ˈØaaignʲeað
	ˈØaAiɣθiU -> ˈØaAiɣθʲU
	ˈØaaiʟiE -> ˈØaaiʟʲE
	ˈØaaimsiear -> ˈØaaimsʲear
	ˈØˠəinieax -> ˈØˠəinʲeax
	ˈØaaiŋgieal -> ˈØaaiŋgʲeal
	ˈØaainμniE -> ˈØaainμnʲE
	ˈØaAiɴsieaμ -> ˈØaAiɴsʲeaμ
	ˈØˠərʲ!βieart -> ˈØˠərʲ!βʲeart
	ˈØaairxiiiɴieax -> ˈØaairxʲiiɴʲeax
	ˈØaairxiiisieaxt -> ˈØaairxʲiisʲeaxt
	ˈØaairðiE -> ˈØaairðʲE
	ˈØaairieag -> ˈØaairʲeag
	ˈØaairieaxaaas -> ˈØaairʲeaxaaas
	ˈØʲarˠ!ɣaairiE -> ˈØʲarˠ!ɣaairʲE
	ˈØaairiiidiU -> ˈØaairʲiidʲU
	ˈØaairliiuguuuð -> ˈØaairlʲiuguuuð
	ˈØaairμiiidiU -> ˈØaairμʲiidʲU


u -> ʷ / (?<=::C::+|Ø) _ ::V::
Sample of maximum 20 input/output pairs:

	ˈØaaukuouβuoar -> ˈØaaukʷouβʷoar
	ˈØaaukuouμuoal -> ˈØaaukʷouμʷoal
	ˈØˠəunuoax -> ˈØˠəunʷoax
	ˈØˠərʷ!kuoar -> ˈØˠərʷ!kʷoar
	ˈØaairlʲiuguuuð -> ˈØaairlʲiugʷuuð
	ˈØaaubθuU -> ˈØaaubθʷU
	ˈØaairʲiuɣuuuð -> ˈØaairʲiuɣʷuuð
	ˈØaaustuuuð -> ˈØaaustʷuuð
	ˈØaautluuuɣuuuð -> ˈØaautlʷuuɣʷuuð
	ˈØaOuɣduoarðaAas -> ˈØaOuɣdʷoarðaAas
	ˈbʲeuθuU -> ˈbʲeuθʷU
	ˈbʲiuβðuU -> ˈbʲiuβðʷU
	ˈbʲiiθ-ˈβʲeuθuU -> ˈbʲiiθ-ˈβʲeuθʷU
	ˈbuoalaaað -> ˈbʷoalaaað
	ˈbruOan -> ˈbrʷOan
	ˈbuAið -> ˈbʷAið
	ˈbuuiðʲE -> ˈbʷuiðʲE
	ˈbuuiɴʲE -> ˈbʷuiɴʲE
	ˈbuuiθ -> ˈbʷuiθ
	ˈbuoaθ -> ˈbʷoaθ


a -> ˠ / (?<=::C::+|Ø) _ ::V::
Sample of maximum 20 input/output pairs:

	ˈØaI.ear -> ˈØˠI.ear
	ˈØaaibɣʲiidʲiir -> ˈØˠaibɣʲiidʲiir
	ˈØaaabstaaanaaid -> ˈØˠaabstˠaanˠaid
	ˈØaaagaaalðaaaμ -> ˈØˠaagˠaalðˠaaμ
	ˈØaaukʷouβʷoar -> ˈØˠaukʷouβʷoar
	ˈØaaukʷouμʷoal -> ˈØˠaukʷouμʷoal
	ˈØaaaðaaiɣ -> ˈØˠaaðˠaiɣ
	ˈØaaaðaaaltraaas -> ˈØˠaaðˠaaltrˠaas
	ˈØaaaðβaaar -> ˈØˠaaðβˠaar
	ˈØaaaðnaaagaaul -> ˈØˠaaðnˠaagˠaul
	ˈØaaaðraaað -> ˈØˠaaðrˠaað
	ˈØaaignʲeað -> ˈØˠaignʲeað
	ˈØaAiɣθʲU -> ˈØˠAiɣθʲU
	ˈØaail -> ˈØˠail
	ˈØaail -> ˈØˠail
	ˈØaAil -> ˈØˠAil
	ˈØaaiʟʲE -> ˈØˠaiʟʲE
	ˈØaaimsʲear -> ˈØˠaimsʲear
	ˈØaaiŋgʲeal -> ˈØˠaiŋgʲeal
	ˈØaainm -> ˈØˠainm


%%%% 15. Consonant colour after vowels
%
% This rule assigns consonant colour after vowels.
%
i -> ʲ / ([ˠʲʷ]|\.)::V:: _
Sample of maximum 20 input/output pairs:

	ˈØˠaibɣʲiidʲiir -> ˈØˠaʲbɣʲiʲdʲiʲr
	ˈØˠaabstˠaanˠaid -> ˈØˠaabstˠaanˠaʲd
	ˈØˠaaðˠaiɣ -> ˈØˠaaðˠaʲɣ
	ˈØʲEidʲiuð -> ˈØʲEʲdʲiuð
	ˈØˠaignʲeað -> ˈØˠaʲgnʲeað
	ˈØˠAiɣθʲU -> ˈØˠAʲɣθʲU
	ˈØˠail -> ˈØˠaʲl
	ˈØˠail -> ˈØˠaʲl
	ˈØˠAil -> ˈØˠAʲl
	ˈØˠaiʟʲE -> ˈØˠaʲʟʲE
	ˈØˠaimsʲear -> ˈØˠaʲmsʲear
	ˈØˠəinʲeax -> ˈØˠəʲnʲeax
	ˈØˠaiŋgʲeal -> ˈØˠaʲŋgʲeal
	ˈØˠainm -> ˈØˠaʲnm
	ˈØˠainμnʲE -> ˈØˠaʲnμnʲE
	ˈØˠAiɴsʲeaμ -> ˈØˠAʲɴsʲeaμ
	ˈØˠairxʲiiɴʲeax -> ˈØˠaʲrxʲiʲɴʲeax
	ˈØˠairxʲiisʲeaxt -> ˈØˠaʲrxʲiʲsʲeaxt
	ˈØˠairðʲE -> ˈØˠaʲrðʲE
	ˈØˠairʲeag -> ˈØˠaʲrʲeag


u -> ʷ / ([ˠʲʷ]|\.)::V:: _
Sample of maximum 20 input/output pairs:

	ˈØˠaukʷouβʷoar -> ˈØˠaʷkʷoʷβʷoar
	ˈØˠaukʷouμʷoal -> ˈØˠaʷkʷoʷμʷoal
	ˈØˠaaðnˠaagˠaul -> ˈØˠaaðnˠaagˠaʷl
	ˈØʲEʲdʲiuð -> ˈØʲEʲdʲiʷð
	ˈØˠəunʷoax -> ˈØˠəʷnʷoax
	ˈØˠaʲrlʲiugʷuuð -> ˈØˠaʲrlʲiʷgʷuʷð
	ˈØˠaʲnØʲius -> ˈØˠaʲnØʲiʷs
	ˈØˠaubθʷU -> ˈØˠaʷbθʷU
	ˈØˠaʲrʲiuɣʷuuð -> ˈØˠaʲrʲiʷɣʷuʷð
	ˈØˠAʲrʲiʲʟʲiuð -> ˈØˠAʲrʲiʲʟʲiʷð
	ˈØˠaustʷuuð -> ˈØˠaʷstʷuʷð
	ˈØˠautlʷuuɣʷuuð -> ˈØˠaʷtlʷuʷɣʷuʷð
	ˈØˠOuɣdʷoarðˠAas -> ˈØˠOʷɣdʷoarðˠAas
	ˈbʲeuθʷU -> ˈbʲeʷθʷU
	ˈbʲiuβðʷU -> ˈbʲiʷβðʷU
	ˈbʲiʲθ-ˈβʲeuθʷU -> ˈbʲiʲθ-ˈβʲeʷθʷU
	ˈbʲiuθ -> ˈbʲiʷθ
	ˈbʷuunʷoað -> ˈbʷuʷnʷoað
	ˈbʷuurbʷE -> ˈbʷuʷrbʷE
	ˈkˠEʲn-ˈðʷUuθrʷoaxt -> ˈkˠEʲn-ˈðʷUʷθrʷoaxt


a -> ˠ / ([ˠʲʷ]|\.)::V:: _
Sample of maximum 20 input/output pairs:

	ˈØˠI.ear -> ˈØˠI.eˠr
	ˈØˠaabstˠaanˠaʲd -> ˈØˠaˠbstˠaˠnˠaʲd
	ˈØˠaagˠaalðˠaaμ -> ˈØˠaˠgˠaˠlðˠaˠμ
	ˈØˠaʷkʷoʷβʷoar -> ˈØˠaʷkʷoʷβʷoˠr
	ˈØˠaʷkʷoʷμʷoal -> ˈØˠaʷkʷoʷμʷoˠl
	ˈØˠaaðˠaʲɣ -> ˈØˠaˠðˠaʲɣ
	ˈØˠaaðˠaaltrˠaas -> ˈØˠaˠðˠaˠltrˠaˠs
	ˈØˠaaðβˠaar -> ˈØˠaˠðβˠaˠr
	ˈØˠaaðnˠaagˠaʷl -> ˈØˠaˠðnˠaˠgˠaʷl
	ˈØˠaaðrˠaað -> ˈØˠaˠðrˠaˠð
	ˈØˠaʲgnʲeað -> ˈØˠaʲgnʲeˠð
	ˈØˠaʲmsʲear -> ˈØˠaʲmsʲeˠr
	ˈØˠəʲnʲeax -> ˈØˠəʲnʲeˠx
	ˈØˠəʷnʷoax -> ˈØˠəʷnʷoˠx
	ˈØˠaʲŋgʲeal -> ˈØˠaʲŋgʲeˠl
	ˈØˠAʲɴsʲeaμ -> ˈØˠAʲɴsʲeˠμ
	ˈØˠərʲ!βʲeart -> ˈØˠərʲ!βʲeˠrt
	ˈØˠaʲrxʲiʲɴʲeax -> ˈØˠaʲrxʲiʲɴʲeˠx
	ˈØˠaʲrxʲiʲsʲeaxt -> ˈØˠaʲrxʲiʲsʲeˠxt
	ˈØˠərʷ!kʷoar -> ˈØˠərʷ!kʷoˠr


%%%%%%%%%%%%%%%     Vowel reduction     %%%%%%%%%%%%%%%
%%%% 16. Reduce short vowels
%
% This rule reduces short vowels to /a/ or /ə/
%
i -> ə / [ʲ]|\. _ [ʲʷ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʲbɣʲiʲdʲiʲr -> ˈØˠaʲbɣʲəʲdʲəʲr
	ˈØʲEʲdʲiʷð -> ˈØʲEʲdʲəʷð
	ˈØˠaʲrxʲiʲɴʲeˠx -> ˈØˠaʲrxʲəʲɴʲeˠx
	ˈØˠaʲrxʲiʲsʲeˠxt -> ˈØˠaʲrxʲəʲsʲeˠxt
	ˈØˠaʲrʲiʲdʲU -> ˈØˠaʲrʲəʲdʲU
	ˈØˠaʲrlʲiʷgʷuʷð -> ˈØˠaʲrlʲəʷgʷuʷð
	ˈØˠaʲrμʲiʲdʲU -> ˈØˠaʲrμʲəʲdʲU
	ˈØˠaʲθʲiʲrɣʲE -> ˈØˠaʲθʲəʲrɣʲE
	ˈØˠaʲθrʲiʲɣʲE -> ˈØˠaʲθrʲəʲɣʲE
	ˈØˠaʲθʲiʲs -> ˈØˠaʲθʲəʲs
	ˈØˠaʲŋkrʲiʲðʲE -> ˈØˠaʲŋkrʲəʲðʲE
	ˈØˠaʲnØʲiʷs -> ˈØˠaʲnØʲəʷs
	ˈØˠaʲnʲiʲm -> ˈØˠaʲnʲəʲm
	ˈØˠaʲrʲiʷɣʷuʷð -> ˈØˠaʲrʲəʷɣʷuʷð
	ˈØˠAʲrʲiʲʟʲiʷð -> ˈØˠAʲrʲəʲʟʲəʷð
	ˈbˠaʲθʲiʲs -> ˈbˠaʲθʲəʲs
	ˈbʲiʷβðʷU -> ˈbʲəʷβðʷU
	ˈbʲiʲθ-ˈβʲeʷθʷU -> ˈbʲəʲθ-ˈβʲeʷθʷU
	ˈbʲiʷθ -> ˈbʲəʷθ
	ˈbrʲiʲθ -> ˈbrʲəʲθ


e -> a / [ʲ]|\. _ [ʲʷˠ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠI.eˠr -> ˈØˠI.aˠr
	ˈØˠaʲgnʲeˠð -> ˈØˠaʲgnʲaˠð
	ˈØˠaʲmsʲeˠr -> ˈØˠaʲmsʲaˠr
	ˈØˠəʲnʲeˠx -> ˈØˠəʲnʲaˠx
	ˈØˠaʲŋgʲeˠl -> ˈØˠaʲŋgʲaˠl
	ˈØˠAʲɴsʲeˠμ -> ˈØˠAʲɴsʲaˠμ
	ˈØˠərʲ!βʲeˠrt -> ˈØˠərʲ!βʲaˠrt
	ˈØˠaʲrxʲəʲɴʲeˠx -> ˈØˠaʲrxʲəʲɴʲaˠx
	ˈØˠaʲrxʲəʲsʲeˠxt -> ˈØˠaʲrxʲəʲsʲaˠxt
	ˈØˠaʲrʲeˠg -> ˈØˠaʲrʲaˠg
	ˈØˠaʲrʲeˠxˠaˠs -> ˈØˠaʲrʲaˠxˠaˠs
	ˈØˠaˠμˠaʲrʲeˠs -> ˈØˠaˠμˠaʲrʲaˠs
	ˈØˠaˠμˠaʲrʲeˠsˠaˠx -> ˈØˠaˠμˠaʲrʲaˠsˠaˠx
	ˈØˠaʲnʲeˠgnˠE -> ˈØˠaʲnʲaˠgnˠE
	ˈØˠAʲtrʲeˠβ -> ˈØˠAʲtrʲaˠβ
	ˈbˠaʲrɣʲeˠn -> ˈbˠaʲrɣʲaˠn
	ˈbˠaʲθʲeˠs -> ˈbˠaʲθʲaˠs
	ˈbʲeˠn -> ˈbʲaˠn
	ˈbʲeˠɴdˠaˠxt -> ˈbʲaˠɴdˠaˠxt
	ˈbʲeʷθʷU -> ˈbʲaʷθʷU


u -> ə / [ʷ]|\. _ [ʲʷ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʲrlʲəʷgʷuʷð -> ˈØˠaʲrlʲəʷgʷəʷð
	ˈØˠaʲrʲəʷɣʷuʷð -> ˈØˠaʲrʲəʷɣʷəʷð
	ˈØˠaʷstʷuʷð -> ˈØˠaʷstʷəʷð
	ˈØˠaʷtlʷuʷɣʷuʷð -> ˈØˠaʷtlʷəʷɣʷəʷð
	ˈbʷuʲðʲE -> ˈbʷəʲðʲE
	ˈbʷuʲɴʲE -> ˈbʷəʲɴʲE
	ˈbʷuʲθ -> ˈbʷəʲθ
	ˈbʷuʷnʷoˠð -> ˈbʷəʷnʷoˠð
	ˈbʷuʷrbʷE -> ˈbʷəʷrbʷE
	ˈbʷuʲrbʲE -> ˈbʷəʲrbʲE
	ˈkʲEʷdβʷuʲð -> ˈkʲEʷdβʷəʲð
	ˈkʷoʷβʷuʲr -> ˈkʷoʷβʷəʲr
	ˈkʷoʷgʷuʷβʷuʷs -> ˈkʷoʷgʷəʷβʷəʷs
	ˈkʷuʷɴtʷuʷβʷoˠrt -> ˈkʷəʷɴtʷəʷβʷoˠrt
	ˈkʷuʷɴdʷuʷβʷoˠrt -> ˈkʷəʷɴdʷəʷβʷoˠrt
	ˈkʷuʷμdʷuʷβʷoˠrt -> ˈkʷəʷμdʷəʷβʷoˠrt
	ˈkʷuʷμðʷuʷβʷoˠrt -> ˈkʷəʷμðʷəʷβʷoˠrt
	ˈkʷoʷsμʷuʲlʲəʷs -> ˈkʷoʷsμʷəʲlʲəʷs
	ˈkʷoʷdlʷuʷð -> ˈkʷoʷdlʷəʷð
	ˈkrˠAʷβʷuʷð -> ˈkrˠAʷβʷəʷð


o -> a / [ʷ]|\. _ [ʲʷˠ]|[-·]
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷoʷβʷoˠr -> ˈØˠaʷkʷaʷβʷaˠr
	ˈØˠaʷkʷoʷμʷoˠl -> ˈØˠaʷkʷaʷμʷaˠl
	ˈØˠəʷnʷoˠx -> ˈØˠəʷnʷaˠx
	ˈØˠərʷ!kʷoˠr -> ˈØˠərʷ!kʷaˠr
	ˈØˠOʷɣdʷoˠrðˠAˠs -> ˈØˠOʷɣdʷaˠrðˠAˠs
	ˈbʷoˠlˠaˠð -> ˈbʷaˠlˠaˠð
	ˈbʷoˠθ -> ˈbʷaˠθ
	ˈbʷəʷnʷoˠð -> ˈbʷəʷnʷaˠð
	ˈkˠEʲn-ˈxʷoˠμrˠaˠk -> ˈkˠEʲn-ˈxʷaˠμrˠaˠk
	ˈkˠEʲn-ˈðʷUʷθrʷoˠxt -> ˈkˠEʲn-ˈðʷUʷθrʷaˠxt
	ˈkʷoˠβˠaˠðlˠaʷs -> ˈkʷaˠβˠaˠðlˠaʷs
	ˈkʷoʷβʷəʲr -> ˈkʷaʷβʷəʲr
	ˈkʷoʲgʲEʲlsʲəʲnʲE -> ˈkʷaʲgʲEʲlsʲəʲnʲE
	ˈkʷoʷgʷəʷβʷəʷs -> ˈkʷaʷgʷəʷβʷəʷs
	ˈkʷoʲβðʲaˠlˠaˠx -> ˈkʷaʲβðʲaˠlˠaˠx
	ˈkʷoʲβðʲaˠlˠaˠx -> ˈkʷaʲβðʲaˠlˠaˠx
	ˈkʷoʲβsʲE -> ˈkʷaʲβsʲE
	ˈkʷoʲmðʲU -> ˈkʷaʲmðʲU
	ˈkʷoˠl -> ˈkʷaˠl
	ˈkʷoˠlˠaʲɴ -> ˈkʷaˠlˠaʲɴ


%%%% 17. Reduce long vowels
%
% This rule reduces long vowels to /a/ or /ə/ followed by /Ø/ and a colour marker
%
I -> əØʲ / _
Sample of maximum 20 input/output pairs:

	ˈØˠI.aˠr -> ˈØˠəØʲ.aˠr
	ˈØˠaʲsɴdʲIʲs -> ˈØˠaʲsɴdʲəØʲʲs
	ˈbʲI.aˠð -> ˈbʲəØʲ.aˠð
	ˈbrʲIʲɣ -> ˈbrʲəØʲʲɣ
	ˈkˠEʲn-ˈɣnʲIʷμ -> ˈkˠEʲn-ˈɣnʲəØʲʷμ
	ˈdˠaˠɣ-ˈðʷEʲnʲI -> ˈdˠaˠɣ-ˈðʷEʲnʲəØʲ
	ˈdˠaˠɣ-ˈɣnʲIʷμ -> ˈdˠaˠɣ-ˈɣnʲəØʲʷμ
	ˈdʲI.aˠs -> ˈdʲəØʲ.aˠs
	ˈdʲI.aˠs -> ˈdʲəØʲ.aˠs
	ˈdʲI.U -> ˈdʲəØʲ.U
	ˈdʲIˠðnˠaˠð -> ˈdʲəØʲˠðnˠaˠð
	ˈdʲIˠɣˠaˠl -> ˈdʲəØʲˠɣˠaˠl
	ˈdʲIʷlɣʷəʷð -> ˈdʲəØʲʷlɣʷəʷð
	ˈdʲIʷltʷəʷð -> ˈdʲəØʲʷltʷəʷð
	ˈdʲIʲμʲəʲgʲaˠμ -> ˈdʲəØʲʲμʲəʲgʲaˠμ
	ˈdʲIʷθ -> ˈdʲəØʲʷθ
	ˈdʲIʲdʲU -> ˈdʲəØʲʲdʲU
	ˈdrʷaˠɣ-ˈɣnʲIʷμ -> ˈdrʷaˠɣ-ˈɣnʲəØʲʷμ
	ˈdrʷI -> ˈdrʷəØʲ
	ˈdrʷI.I -> ˈdrʷəØʲ.əØʲ


U -> əØʷ / _
Sample of maximum 20 input/output pairs:

	ˈØˠAʲɣθʲU -> ˈØˠAʲɣθʲəØʷ
	ˈØˠaʲrʲəʲdʲU -> ˈØˠaʲrʲəʲdʲəØʷ
	ˈØˠaʲrμʲəʲdʲU -> ˈØˠaʲrμʲəʲdʲəØʷ
	ˈØˠaʷbθʷU -> ˈØˠaʷbθʷəØʷ
	ˈØʲarˠ!lˠaˠdˠU -> ˈØʲarˠ!lˠaˠdˠəØʷ
	ˈbʲEˠstˠaˠdˠU -> ˈbʲEˠstˠaˠdˠəØʷ
	ˈbʲaʷθʷU -> ˈbʲaʷθʷəØʷ
	ˈbʲəʷβðʷU -> ˈbʲəʷβðʷəØʷ
	ˈbʲəʲθ-ˈβʲaʷθʷU -> ˈbʲəʲθ-ˈβʲaʷθʷəØʷ
	ˈkˠEʲn-ˈðʷUʷθrʷaˠxt -> ˈkˠEʲn-ˈðʷəØʷʷθrʷaˠxt
	ˈkʷaʲmðʲU -> ˈkʷaʲmðʲəØʷ
	ˈkʷUʷl -> ˈkʷəØʷʷl
	ˈkʷUʷrsʷaˠɣˠaˠð -> ˈkʷəØʷʷrsʷaˠɣˠaˠð
	ˈkʷUʷrsʷaˠɣˠaˠð -> ˈkʷəØʷʷrsʷaˠɣˠaˠð
	ˈdʲEʲgsʲU -> ˈdʲEʲgsʲəØʷ
	ˈdʲaʲθʲəʲdʲU -> ˈdʲaʲθʲəʲdʲəØʷ
	ˈdʲəØʲ.U -> ˈdʲəØʲ.əØʷ
	ˈdʲəØʲʲdʲU -> ˈdʲəØʲʲdʲəØʷ
	ˈdʲUʲtʲE -> ˈdʲəØʷʲtʲE
	ˈdlʷUʷμ -> ˈdlʷəØʷʷμ


E -> aØʲ / _
Sample of maximum 20 input/output pairs:

	ˈØʲEʲdʲəʷð -> ˈØʲaØʲʲdʲəʷð
	ˈØˠaʲʟʲE -> ˈØˠaʲʟʲaØʲ
	ˈØˠaʲnμnʲE -> ˈØˠaʲnμnʲaØʲ
	ˈØˠaʲrðʲE -> ˈØˠaʲrðʲaØʲ
	ˈØʲarˠ!ɣˠaʲrʲE -> ˈØʲarˠ!ɣˠaʲrʲaØʲ
	ˈØˠEʲs -> ˈØˠaØʲʲs
	ˈØˠEˠs -> ˈØˠaØʲˠs
	ˈØˠaʲθʲE -> ˈØˠaʲθʲaØʲ
	ˈØˠaʲθɣnʲE -> ˈØˠaʲθɣnʲaØʲ
	ˈØˠaʲθʲəʲrɣʲE -> ˈØˠaʲθʲəʲrɣʲaØʲ
	ˈØˠaʲθrʲəʲɣʲE -> ˈØˠaʲθrʲəʲɣʲaØʲ
	ˈØˠAˠnˠE -> ˈØˠAˠnˠaØʲ
	ˈØˠaˠnˠaˠm-ˈxˠaˠrˠE -> ˈØˠaˠnˠaˠm-ˈxˠaˠrˠaØʲ
	ˈØˠaʲnʲaˠgnˠE -> ˈØˠaʲnʲaˠgnˠaØʲ
	ˈØˠaʲŋkrʲəʲðʲE -> ˈØˠaʲŋkrʲəʲðʲaØʲ
	ˈbˠA.E -> ˈbˠA.aØʲ
	ˈbʲEʲm -> ˈbʲaØʲʲm
	ˈbʲEˠl -> ˈbʲaØʲˠl
	ˈbʲEˠlrˠE -> ˈbʲaØʲˠlrˠaØʲ
	ˈbʲEˠs -> ˈbʲaØʲˠs


O -> aØʷ / _
Sample of maximum 20 input/output pairs:

	ˈØˠaˠltˠOʲr -> ˈØˠaˠltˠaØʷʲr
	ˈØˠOʷɣdʷaˠrðˠAˠs -> ˈØˠaØʷʷɣdʷaˠrðˠAˠs
	ˈbʲO -> ˈbʲaØʷ
	ˈbrʷOˠn -> ˈbrʷaØʷˠn
	ˈkˠaʲɴdlʲOʲr -> ˈkˠaʲɴdlʲaØʷʲr
	ˈkʲaˠθˠaʷrxʷO -> ˈkʲaˠθˠaʷrxʷaØʷ
	ˈkʷaμˠ!θʲəʷnʷOˠl -> ˈkʷaμˠ!θʲəʷnʷaØʷˠl
	ˈkʷOˠrˠaØʲ -> ˈkʷaØʷˠrˠaØʲ
	ˈdʲOˠlˠaˠðˠaˠxt -> ˈdʲaØʷˠlˠaˠðˠaˠxt
	ˈɸʷOˠgrˠaØʲ -> ˈɸʷaØʷˠgrˠaØʲ
	ˈɸʷaʷrʷOʲl -> ˈɸʷaʷrʷaØʷʲl
	ˈgˠO -> ˈgˠaØʷ
	ˈØʲəmʷ!rʷOˠl -> ˈØʲəmʷ!rʷaØʷˠl
	ˈØˠaʲrØʷOˠgrˠaØʲ -> ˈØˠaʲrØʷaØʷˠgrˠaØʲ
	ˈʟʷOˠɣ -> ˈʟʷaØʷˠɣ
	ˈmʷOˠrˠaˠð -> ˈmʷaØʷˠrˠaˠð
	ˈØʷOˠxt -> ˈØʷaØʷˠxt
	ˈØʷOˠɣˠaØʲ -> ˈØʷaØʷˠɣˠaØʲ
	ˈØʷOʲɣʲaØʲ -> ˈØʷaØʷʲɣʲaØʲ
	ˈØʷOʷμʷaˠn -> ˈØʷaØʷʷμʷaˠn


A -> aØˠ / _
Sample of maximum 20 input/output pairs:

	ˈØˠAʲɣθʲəØʷ -> ˈØˠaØˠʲɣθʲəØʷ
	ˈØˠAʲl -> ˈØˠaØˠʲl
	ˈØˠAʲɴsʲaˠμ -> ˈØˠaØˠʲɴsʲaˠμ
	ˈØˠAˠnˠaØʲ -> ˈØˠaØˠˠnˠaØʲ
	ˈØˠaˠnmxˠaˠrˠA -> ˈØˠaˠnmxˠaˠrˠaØˠ
	ˈØˠAʲrʲəʲʟʲəʷð -> ˈØˠaØˠʲrʲəʲʟʲəʷð
	ˈØˠAʲtrʲaˠβ -> ˈØˠaØˠʲtrʲaˠβ
	ˈØˠaØʷʷɣdʷaˠrðˠAˠs -> ˈØˠaØʷʷɣdʷaˠrðˠaØˠˠs
	ˈbˠA.aØʲ -> ˈbˠaØˠ.aØʲ
	ˈbˠAˠɣ -> ˈbˠaØˠˠɣ
	ˈbˠAˠs -> ˈbˠaØˠˠs
	ˈbrˠAˠθ -> ˈbrˠaØˠˠθ
	ˈbrˠAˠθˠaʲr -> ˈbrˠaØˠˠθˠaʲr
	ˈbrʲAˠθˠaˠr -> ˈbrʲaØˠˠθˠaˠr
	ˈbʷAʲð -> ˈbʷaØˠʲð
	ˈkʲAˠʟ -> ˈkʲaØˠˠʟ
	ˈkrˠAʷβʷəʷð -> ˈkrˠaØˠʷβʷəʷð
	ˈkʷAʲrt -> ˈkʷaØˠʲrt
	ˈdˠAˠn -> ˈdˠaØˠˠn
	ˈdʲA.aˠxt -> ˈdʲaØˠ.aˠxt


%%%%%%%%%%%%%%%     Assimilate consonant colour colour    %%%%%%%%%%%%%%%
%%%% 18. Regressive assimilation of consonant colour
%
0 -> ʲ / (?<=([ˈ]|(!))::C::) _ (?=(::C::){1,2}ʲ)
Sample of maximum 20 input/output pairs:

	ˈbrʲaØˠˠθˠaˠr -> ˈbʲrʲaØˠˠθˠaˠr
	ˈbrʲəØʲʲɣ -> ˈbʲrʲəØʲʲɣ
	ˈbrʲəʲθ -> ˈbʲrʲəʲθ
	ˈbrʲaʲθ -> ˈbʲrʲaʲθ
	ˈbrʲəʲθʲaˠμ -> ˈbʲrʲəʲθʲaˠμ
	ˈbrʲaʲθʲaˠμ -> ˈbʲrʲaʲθʲaˠμ
	ˈbrʲəʲθʲaˠμnˠaˠxt -> ˈbʲrʲəʲθʲaˠμnˠaˠxt
	ˈbrʲaʲθʲaˠμnˠaˠxt -> ˈbʲrʲaʲθʲaˠμnˠaˠxt
	ˈkˠaØʲʲn-ˈɣnʲəØʲʷμ -> ˈkˠaØʲʲn-ˈɣʲnʲəØʲʷμ
	ˈkˠaØʲʲn-ˈskʲaØʲˠl -> ˈkˠaØʲʲn-ˈsʲkʲaØʲˠl
	ˈklʲaʲθ -> ˈkʲlʲaʲθ
	ˈklʲaˠθ -> ˈkʲlʲaˠθ
	ˈkrʲaʲdʲaˠμ -> ˈkʲrʲaʲdʲaˠμ
	ˈkrʲəʲðʲaØʲ -> ˈkʲrʲəʲðʲaØʲ
	ˈdˠaˠɣ-ˈɣnʲəØʲʷμ -> ˈdˠaˠɣ-ˈɣʲnʲəØʲʷμ
	ˈdlʲəʲɣʲaˠð -> ˈdʲlʲəʲɣʲaˠð
	ˈdrʷaˠɣ-ˈɣnʲəØʲʷμ -> ˈdrʷaˠɣ-ˈɣʲnʲəØʲʷμ
	ˈɸlʲaˠð -> ˈɸʲlʲaˠð
	ˈɸrʲaʷgʷaˠr -> ˈɸʲrʲaʷgʷaˠr
	ˈɸrʲaˠgrˠaØʲ -> ˈɸʲrʲaˠgrˠaØʲ


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
	ˈprʷaʲɴd -> ˈpʷrʷaʲɴd
	ˈtrʷaØʷˠkˠaʲrʲaØʲ -> ˈtʷrʷaØʷˠkˠaʲrʲaØʲ


0 -> ˠ / (?<=([ˈ]|(!))::C::) _ (?=(::C::){1,2}ˠ)
Sample of maximum 20 input/output pairs:

	ˈbrˠaØˠˠθ -> ˈbˠrˠaØˠˠθ
	ˈbrˠaØˠˠθˠaʲr -> ˈbˠrˠaØˠˠθˠaʲr
	ˈklˠaʲðʲaˠβ -> ˈkˠlˠaʲðʲaˠβ
	ˈklˠaˠɴd -> ˈkˠlˠaˠɴd
	ˈkrˠaØˠʷβʷəʷð -> ˈkˠrˠaØˠʷβʷəʷð
	ˈØʲadˠarˠ!skˠaˠrˠaˠð -> ˈØʲadˠarˠ!sˠkˠaˠrˠaˠð
	ˈØʲadˠarˠ!gnˠaØʲ -> ˈØʲadˠarˠ!gˠnˠaØʲ
	ˈɸlˠaʲθ -> ˈɸˠlˠaʲθ
	ˈɸlˠaʲθʲaˠμnˠaˠxt -> ˈɸˠlˠaʲθʲaˠμnˠaˠxt
	ˈgnˠaØˠˠs -> ˈgˠnˠaØˠˠs
	ˈgrˠaØˠˠð -> ˈgˠrˠaØˠˠð
	ˈgrˠaØˠʲɴʲaØʲ -> ˈgˠrˠaØˠʲɴʲaØʲ
	ˈØʲarˠ!xrˠaØʲ -> ˈØʲarˠ!xˠrˠaØʲ
	ˈmrˠaˠθ -> ˈmˠrˠaˠθ
	ˈprˠaʲɴd -> ˈpˠrˠaʲɴd
	ˈskˠaˠrˠaˠð -> ˈsˠkˠaˠrˠaˠð
	ˈsmˠaˠxt -> ˈsˠmˠaˠxt


%%%% 19. Progressive assimilation of consonant colour
%
0 -> ʲ / (?<![!]::C::{1,2})(?<=[^Ø]ʲ::C::{1,3}) _
Sample of maximum 20 input/output pairs:

	ˈØˠaʲbɣʲəʲdʲəʲr -> ˈØˠaʲbʲɣʲʲəʲdʲʲəʲrʲ
	ˈØˠaˠbstˠaˠnˠaʲd -> ˈØˠaˠbstˠaˠnˠaʲdʲ
	ˈØˠaˠðˠaʲɣ -> ˈØˠaˠðˠaʲɣʲ
	ˈØʲaØʲʲdʲəʷð -> ˈØʲaØʲʲdʲʲəʷð
	ˈØˠaʲgnʲaˠð -> ˈØˠaʲgʲnʲʲaˠð
	ˈØˠaØˠʲɣθʲəØʷ -> ˈØˠaØˠʲɣʲθʲʲəØʷ
	ˈØˠaʲl -> ˈØˠaʲlʲ
	ˈØˠaʲl -> ˈØˠaʲlʲ
	ˈØˠaØˠʲl -> ˈØˠaØˠʲlʲ
	ˈØˠaʲʟʲaØʲ -> ˈØˠaʲʟʲʲaØʲ
	ˈØˠaʲmsʲaˠr -> ˈØˠaʲmʲsʲʲaˠr
	ˈØˠəʲnʲaˠx -> ˈØˠəʲnʲʲaˠx
	ˈØˠaʲŋgʲaˠl -> ˈØˠaʲŋʲgʲʲaˠl
	ˈØˠaʲnm -> ˈØˠaʲnʲmʲ
	ˈØˠaʲnμnʲaØʲ -> ˈØˠaʲnʲμʲnʲʲaØʲ
	ˈØˠaØˠʲɴsʲaˠμ -> ˈØˠaØˠʲɴʲsʲʲaˠμ
	ˈØˠaʲrxʲəʲɴʲaˠx -> ˈØˠaʲrʲxʲʲəʲɴʲʲaˠx
	ˈØˠaʲrxʲəʲsʲaˠxt -> ˈØˠaʲrʲxʲʲəʲsʲʲaˠxt
	ˈØˠaʲrðʲaØʲ -> ˈØˠaʲrʲðʲʲaØʲ
	ˈØˠaʲrʲaˠg -> ˈØˠaʲrʲʲaˠg


0 -> ʷ / (?<![!]::C::{1,2})(?<=[^Ø]ʷ::C::{1,3}) _
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷaʷβʷaˠr -> ˈØˠaʷkʷʷaʷβʷʷaˠr
	ˈØˠaʷkʷaʷμʷaˠl -> ˈØˠaʷkʷʷaʷμʷʷaˠl
	ˈØˠaˠðnˠaˠgˠaʷl -> ˈØˠaˠðnˠaˠgˠaʷlʷ
	ˈØʲaØʲʲdʲʲəʷð -> ˈØʲaØʲʲdʲʲəʷðʷ
	ˈØˠəʷnʷaˠx -> ˈØˠəʷnʷʷaˠx
	ˈØˠaʲrʲlʲʲəʷgʷəʷð -> ˈØˠaʲrʲlʲʲəʷgʷʷəʷðʷ
	ˈØˠaʲnʲØʲəʷs -> ˈØˠaʲnʲØʲəʷsʷ
	ˈØˠaʷbθʷəØʷ -> ˈØˠaʷbʷθʷʷəØʷ
	ˈØˠaʲrʲʲəʷɣʷəʷð -> ˈØˠaʲrʲʲəʷɣʷʷəʷðʷ
	ˈØˠaØˠʲrʲʲəʲʟʲʲəʷð -> ˈØˠaØˠʲrʲʲəʲʟʲʲəʷðʷ
	ˈØˠaʷstʷəʷð -> ˈØˠaʷsʷtʷʷəʷðʷ
	ˈØˠaʷtlʷəʷɣʷəʷð -> ˈØˠaʷtʷlʷʷəʷɣʷʷəʷðʷ
	ˈØˠaØʷʷɣdʷaˠrðˠaØˠˠs -> ˈØˠaØʷʷɣʷdʷʷaˠrðˠaØˠˠs
	ˈbʲaʷθʷəØʷ -> ˈbʲaʷθʷʷəØʷ
	ˈbʲəʷβðʷəØʷ -> ˈbʲəʷβʷðʷʷəØʷ
	ˈbʲəʲθʲ-ˈβʲaʷθʷəØʷ -> ˈbʲəʲθʲ-ˈβʲaʷθʷʷəØʷ
	ˈbʲəʷθ -> ˈbʲəʷθʷ
	ˈbʷrʷaØʷˠn -> ˈbʷrʷʷaØʷˠn
	ˈbʷəʷnʷaˠð -> ˈbʷəʷnʷʷaˠð
	ˈbʷəʷrbʷaØʲ -> ˈbʷəʷrʷbʷʷaØʲ


0 -> ˠ / (?<![!]::C::{1,2})(?<=[^Ø]ˠ::C::{1,3}) _
Sample of maximum 20 input/output pairs:

	ˈØˠəØʲ.aˠr -> ˈØˠəØʲ.aˠrˠ
	ˈØˠaˠbstˠaˠnˠaʲdʲ -> ˈØˠaˠbˠsˠtˠˠaˠnˠˠaʲdʲ
	ˈØˠaˠgˠaˠlðˠaˠμ -> ˈØˠaˠgˠˠaˠlˠðˠˠaˠμˠ
	ˈØˠaʷkʷʷaʷβʷʷaˠr -> ˈØˠaʷkʷʷaʷβʷʷaˠrˠ
	ˈØˠaʷkʷʷaʷμʷʷaˠl -> ˈØˠaʷkʷʷaʷμʷʷaˠlˠ
	ˈØˠaˠðˠaʲɣʲ -> ˈØˠaˠðˠˠaʲɣʲ
	ˈØˠaˠðˠaˠltrˠaˠs -> ˈØˠaˠðˠˠaˠlˠtˠrˠˠaˠsˠ
	ˈØˠaˠðβˠaˠr -> ˈØˠaˠðˠβˠˠaˠrˠ
	ˈØˠaˠðnˠaˠgˠaʷlʷ -> ˈØˠaˠðˠnˠˠaˠgˠˠaʷlʷ
	ˈØˠaˠðrˠaˠð -> ˈØˠaˠðˠrˠˠaˠðˠ
	ˈØˠaʲgʲnʲʲaˠð -> ˈØˠaʲgʲnʲʲaˠðˠ
	ˈØˠaʲmʲsʲʲaˠr -> ˈØˠaʲmʲsʲʲaˠrˠ
	ˈØˠəʲnʲʲaˠx -> ˈØˠəʲnʲʲaˠxˠ
	ˈØˠəʷnʷʷaˠx -> ˈØˠəʷnʷʷaˠxˠ
	ˈØˠaʲŋʲgʲʲaˠl -> ˈØˠaʲŋʲgʲʲaˠlˠ
	ˈØˠaØˠʲɴʲsʲʲaˠμ -> ˈØˠaØˠʲɴʲsʲʲaˠμˠ
	ˈØˠərʲ!βʲaˠrt -> ˈØˠərʲ!βʲaˠrˠtˠ
	ˈØˠaʲrʲxʲʲəʲɴʲʲaˠx -> ˈØˠaʲrʲxʲʲəʲɴʲʲaˠxˠ
	ˈØˠaʲrʲxʲʲəʲsʲʲaˠxt -> ˈØˠaʲrʲxʲʲəʲsʲʲaˠxˠtˠ
	ˈØˠərʷ!kʷaˠr -> ˈØˠərʷ!kʷaˠrˠ


%%%% 20. Remove protective environment for prepositional elements
%
% The protective environment for prepositional elements is no longer necessary.
%
! -> 0 / _
Sample of maximum 20 input/output pairs:

	ˈØˠərʲ!βʲaˠrˠtˠ -> ˈØˠərʲβʲaˠrˠtˠ
	ˈØˠərʷ!kʷaˠrˠ -> ˈØˠərʷkʷaˠrˠ
	ˈØʲarˠ!ɣˠaʲrʲʲaØʲ -> ˈØʲarˠɣˠaʲrʲʲaØʲ
	ˈØʲarˠ!lˠaˠdˠˠəØʷ -> ˈØʲarˠlˠaˠdˠˠəØʷ
	ˈkʷaμˠ!Øˠaʷkʷʷaʷβʷʷaˠrˠ -> ˈkʷaμˠØˠaʷkʷʷaʷβʷʷaˠrˠ
	ˈkʷaμˠ!Øˠaʲrʲβʲʲaˠrˠtˠ -> ˈkʷaμˠØˠaʲrʲβʲʲaˠrˠtˠ
	ˈkʷaμˠ!ØˠaʲrʲlʲʲaØʲ -> ˈkʷaμˠØˠaʲrʲlʲʲaØʲ
	ˈkʷaμˠ!Øˠaʲdʲʲaˠxˠtˠ -> ˈkʷaμˠØˠaʲdʲʲaˠxˠtˠ
	ˈkʷaμˠ!Øˠaˠlˠnˠˠaˠðˠ -> ˈkʷaμˠØˠaˠlˠnˠˠaˠðˠ
	ˈkʷaμˠ!Øˠaˠrˠbˠˠaʷsʷ -> ˈkʷaμˠØˠaˠrˠbˠˠaʷsʷ
	ˈkʷaμˠ!ØˠaˠrˠðˠˠaØʲ -> ˈkʷaμˠØˠaˠrˠðˠˠaØʲ
	ˈkʷaμˠ!nʲaˠsˠˠaˠμˠ -> ˈkʷaμˠnʲaˠsˠˠaˠμˠ
	ˈkʷaμʷ!rʷaʷrʷgʷʷaˠnˠ -> ˈkʷaμʷrʷaʷrʷgʷʷaˠnˠ
	ˈkʷaμˠ!θʲəʷnʷʷaØʷˠlˠ -> ˈkʷaμˠθʲəʷnʷʷaØʷˠlˠ
	ˈØˠərʲ!ØaØʲ -> ˈØˠərʲØaØʲ
	ˈØʲadˠarˠ!kʲaˠrˠtˠ -> ˈØʲadˠarˠkʲaˠrˠtˠ
	ˈØʲadʲərʲ!kʲaˠrˠtˠ -> ˈØʲadʲərʲkʲaˠrˠtˠ
	ˈØʲadˠarˠ!dʲəʲβʲʲaØʲ -> ˈØʲadˠarˠdʲəʲβʲʲaØʲ
	ˈØʲadˠarˠ!sˠkˠˠaˠrˠˠaˠðˠ -> ˈØʲadˠarˠsˠkˠˠaˠrˠˠaˠðˠ
	ˈØʲadˠarˠ!gˠnˠˠaØʲ -> ˈØʲadˠarˠgˠnˠˠaØʲ


%%%%%%%%%%%%%%%     Housekeeping    %%%%%%%%%%%%%%%
%%%% 22. Reduction of duplicate colour diacritics
%
ʲ -> 0 / _ ʲ
Sample of maximum 20 input/output pairs:

	ˈØˠaʲbʲɣʲʲəʲdʲʲəʲrʲ -> ˈØˠaʲbʲɣʲəʲdʲəʲrʲ
	ˈØʲaØʲʲdʲʲəʷðʷ -> ˈØʲaØʲdʲəʷðʷ
	ˈØˠaʲgʲnʲʲaˠðˠ -> ˈØˠaʲgʲnʲaˠðˠ
	ˈØˠaØˠʲɣʲθʲʲəØʷ -> ˈØˠaØˠʲɣʲθʲəØʷ
	ˈØˠaʲʟʲʲaØʲ -> ˈØˠaʲʟʲaØʲ
	ˈØˠaʲmʲsʲʲaˠrˠ -> ˈØˠaʲmʲsʲaˠrˠ
	ˈØˠəʲnʲʲaˠxˠ -> ˈØˠəʲnʲaˠxˠ
	ˈØˠaʲŋʲgʲʲaˠlˠ -> ˈØˠaʲŋʲgʲaˠlˠ
	ˈØˠaʲnʲμʲnʲʲaØʲ -> ˈØˠaʲnʲμʲnʲaØʲ
	ˈØˠaØˠʲɴʲsʲʲaˠμˠ -> ˈØˠaØˠʲɴʲsʲaˠμˠ
	ˈØˠaʲrʲxʲʲəʲɴʲʲaˠxˠ -> ˈØˠaʲrʲxʲəʲɴʲaˠxˠ
	ˈØˠaʲrʲxʲʲəʲsʲʲaˠxˠtˠ -> ˈØˠaʲrʲxʲəʲsʲaˠxˠtˠ
	ˈØˠaʲrʲðʲʲaØʲ -> ˈØˠaʲrʲðʲaØʲ
	ˈØˠaʲrʲʲaˠgˠ -> ˈØˠaʲrʲaˠgˠ
	ˈØˠaʲrʲʲaˠxˠˠaˠsˠ -> ˈØˠaʲrʲaˠxˠˠaˠsˠ
	ˈØʲarˠɣˠaʲrʲʲaØʲ -> ˈØʲarˠɣˠaʲrʲaØʲ
	ˈØˠaʲrʲʲəʲdʲʲəØʷ -> ˈØˠaʲrʲəʲdʲəØʷ
	ˈØˠaʲrʲlʲʲəʷgʷʷəʷðʷ -> ˈØˠaʲrʲlʲəʷgʷʷəʷðʷ
	ˈØˠaʲrʲμʲʲəʲdʲʲəØʷ -> ˈØˠaʲrʲμʲəʲdʲəØʷ
	ˈØˠaØʲʲsʲ -> ˈØˠaØʲsʲ


ʷ -> 0 / _ ʷ
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷʷaʷβʷʷaˠrˠ -> ˈØˠaʷkʷaʷβʷaˠrˠ
	ˈØˠaʷkʷʷaʷμʷʷaˠlˠ -> ˈØˠaʷkʷaʷμʷaˠlˠ
	ˈØˠəʷnʷʷaˠxˠ -> ˈØˠəʷnʷaˠxˠ
	ˈØˠaʲrʲlʲəʷgʷʷəʷðʷ -> ˈØˠaʲrʲlʲəʷgʷəʷðʷ
	ˈØˠaʷbʷθʷʷəØʷ -> ˈØˠaʷbʷθʷəØʷ
	ˈØˠaʲrʲəʷɣʷʷəʷðʷ -> ˈØˠaʲrʲəʷɣʷəʷðʷ
	ˈØˠaʷsʷtʷʷəʷðʷ -> ˈØˠaʷsʷtʷəʷðʷ
	ˈØˠaʷtʷlʷʷəʷɣʷʷəʷðʷ -> ˈØˠaʷtʷlʷəʷɣʷəʷðʷ
	ˈØˠaØʷʷɣʷdʷʷaˠrˠðˠˠaØˠˠsˠ -> ˈØˠaØʷɣʷdʷaˠrˠðˠˠaØˠˠsˠ
	ˈbʲaʷθʷʷəØʷ -> ˈbʲaʷθʷəØʷ
	ˈbʲəʷβʷðʷʷəØʷ -> ˈbʲəʷβʷðʷəØʷ
	ˈbʲəʲθʲ-ˈβʲaʷθʷʷəØʷ -> ˈbʲəʲθʲ-ˈβʲaʷθʷəØʷ
	ˈbʷrʷʷaØʷˠnˠ -> ˈbʷrʷaØʷˠnˠ
	ˈbʷəʷnʷʷaˠðˠ -> ˈbʷəʷnʷaˠðˠ
	ˈbʷəʷrʷbʷʷaØʲ -> ˈbʷəʷrʷbʷaØʲ
	ˈkˠaØʲnʲ-ˈðʷəØʷʷθʷrʷʷaˠxˠtˠ -> ˈkˠaØʲnʲ-ˈðʷəØʷθʷrʷaˠxˠtˠ
	ˈkʲaØʲʷdʷβʷʷəʲðʲ -> ˈkʲaØʲʷdʷβʷəʲðʲ
	ˈkʲaˠθˠˠaʷrʷxʷʷaØʷ -> ˈkʲaˠθˠˠaʷrʷxʷaØʷ
	ˈkʷlʷʷaØʲnʲaØʲ -> ˈkʷlʷaØʲnʲaØʲ
	ˈkʷaʷβʷʷəʲrʲ -> ˈkʷaʷβʷəʲrʲ


ˠ -> 0 / _ ˠ
Sample of maximum 20 input/output pairs:

	ˈØˠaˠbˠsˠtˠˠaˠnˠˠaʲdʲ -> ˈØˠaˠbˠsˠtˠaˠnˠaʲdʲ
	ˈØˠaˠgˠˠaˠlˠðˠˠaˠμˠ -> ˈØˠaˠgˠaˠlˠðˠaˠμˠ
	ˈØˠaˠðˠˠaʲɣʲ -> ˈØˠaˠðˠaʲɣʲ
	ˈØˠaˠðˠˠaˠlˠtˠrˠˠaˠsˠ -> ˈØˠaˠðˠaˠlˠtˠrˠaˠsˠ
	ˈØˠaˠðˠβˠˠaˠrˠ -> ˈØˠaˠðˠβˠaˠrˠ
	ˈØˠaˠðˠnˠˠaˠgˠˠaʷlʷ -> ˈØˠaˠðˠnˠaˠgˠaʷlʷ
	ˈØˠaˠðˠrˠˠaˠðˠ -> ˈØˠaˠðˠrˠaˠðˠ
	ˈØˠaʲrʲaˠxˠˠaˠsˠ -> ˈØˠaʲrʲaˠxˠaˠsˠ
	ˈØˠaˠlˠmˠsˠˠaˠnˠ -> ˈØˠaˠlˠmˠsˠaˠnˠ
	ˈØˠaˠlˠtˠˠaØʷʲrʲ -> ˈØˠaˠlˠtˠaØʷʲrʲ
	ˈØˠaˠlˠtˠrˠˠaˠmˠ -> ˈØˠaˠlˠtˠrˠaˠmˠ
	ˈØˠaˠμˠˠaʲrʲaˠsˠ -> ˈØˠaˠμˠaʲrʲaˠsˠ
	ˈØˠaˠμˠˠaʲrʲaˠsˠˠaˠxˠ -> ˈØˠaˠμˠaʲrʲaˠsˠaˠxˠ
	ˈØˠaˠnˠˠaˠðˠ -> ˈØˠaˠnˠaˠðˠ
	ˈØˠaØˠˠnˠˠaØʲ -> ˈØˠaØˠnˠaØʲ
	ˈØˠaˠnˠˠaˠmˠ-ˈxˠaˠrˠˠaØʲ -> ˈØˠaˠnˠaˠmˠ-ˈxˠaˠrˠaØʲ
	ˈØˠaˠnˠmˠxˠˠaˠrˠˠaØˠ -> ˈØˠaˠnˠmˠxˠaˠrˠaØˠ
	ˈØˠaʲnʲaˠgˠnˠˠaØʲ -> ˈØˠaʲnʲaˠgˠnˠaØʲ
	ˈØˠaˠnˠˠaʲmʲ -> ˈØˠaˠnˠaʲmʲ
	ˈØˠaˠnˠˠaʲmʲ -> ˈØˠaˠnˠaʲmʲ


%%%% 23. Loss of colour markers before a consonant
%
ʲ -> 0 / Ø[ʲʷˠ]|[aə] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØˠaʲbʲɣʲəʲdʲəʲrʲ -> ˈØˠabʲɣʲədʲərʲ
	ˈØˠaˠbˠsˠtˠaˠnˠaʲdʲ -> ˈØˠaˠbˠsˠtˠaˠnˠadʲ
	ˈØˠaˠðˠaʲɣʲ -> ˈØˠaˠðˠaɣʲ
	ˈØˠaʲgʲnʲaˠðˠ -> ˈØˠagʲnʲaˠðˠ
	ˈØˠaØˠʲɣʲθʲəØʷ -> ˈØˠaØˠɣʲθʲəØʷ
	ˈØˠaʲlʲ -> ˈØˠalʲ
	ˈØˠaʲlʲ -> ˈØˠalʲ
	ˈØˠaØˠʲlʲ -> ˈØˠaØˠlʲ
	ˈØˠaʲʟʲaØʲ -> ˈØˠaʟʲaØʲ
	ˈØˠaʲmʲsʲaˠrˠ -> ˈØˠamʲsʲaˠrˠ
	ˈØˠəʲnʲaˠxˠ -> ˈØˠənʲaˠxˠ
	ˈØˠaʲŋʲgʲaˠlˠ -> ˈØˠaŋʲgʲaˠlˠ
	ˈØˠaʲnʲmʲ -> ˈØˠanʲmʲ
	ˈØˠaʲnʲμʲnʲaØʲ -> ˈØˠanʲμʲnʲaØʲ
	ˈØˠaØˠʲɴʲsʲaˠμˠ -> ˈØˠaØˠɴʲsʲaˠμˠ
	ˈØˠaʲrʲxʲəʲɴʲaˠxˠ -> ˈØˠarʲxʲəɴʲaˠxˠ
	ˈØˠaʲrʲxʲəʲsʲaˠxˠtˠ -> ˈØˠarʲxʲəsʲaˠxˠtˠ
	ˈØˠaʲrʲðʲaØʲ -> ˈØˠarʲðʲaØʲ
	ˈØˠaʲrʲaˠgˠ -> ˈØˠarʲaˠgˠ
	ˈØˠaʲrʲaˠxˠaˠsˠ -> ˈØˠarʲaˠxˠaˠsˠ


ʷ -> 0 / Ø[ʲʷˠ]|[aə] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØˠaʷkʷaʷβʷaˠrˠ -> ˈØˠakʷaβʷaˠrˠ
	ˈØˠaʷkʷaʷμʷaˠlˠ -> ˈØˠakʷaμʷaˠlˠ
	ˈØˠaˠðˠnˠaˠgˠaʷlʷ -> ˈØˠaˠðˠnˠaˠgˠalʷ
	ˈØʲaØʲdʲəʷðʷ -> ˈØʲaØʲdʲəðʷ
	ˈØˠəʷnʷaˠxˠ -> ˈØˠənʷaˠxˠ
	ˈØˠarʲlʲəʷgʷəʷðʷ -> ˈØˠarʲlʲəgʷəðʷ
	ˈØˠanʲØʲəʷsʷ -> ˈØˠanʲØʲəsʷ
	ˈØˠaʷbʷθʷəØʷ -> ˈØˠabʷθʷəØʷ
	ˈØˠarʲəʷɣʷəʷðʷ -> ˈØˠarʲəɣʷəðʷ
	ˈØˠaØˠrʲəʟʲəʷðʷ -> ˈØˠaØˠrʲəʟʲəðʷ
	ˈØˠaʷsʷtʷəʷðʷ -> ˈØˠasʷtʷəðʷ
	ˈØˠaʷtʷlʷəʷɣʷəʷðʷ -> ˈØˠatʷlʷəɣʷəðʷ
	ˈbʲaʷθʷəØʷ -> ˈbʲaθʷəØʷ
	ˈbʲəʷβʷðʷəØʷ -> ˈbʲəβʷðʷəØʷ
	ˈbʲəθʲ-ˈβʲaʷθʷəØʷ -> ˈbʲəθʲ-ˈβʲaθʷəØʷ
	ˈbʲəʷθʷ -> ˈbʲəθʷ
	ˈbʷəʷnʷaˠðˠ -> ˈbʷənʷaˠðˠ
	ˈbʷəʷrʷbʷaØʲ -> ˈbʷərʷbʷaØʲ
	ˈkˠaØʲnʲ-ˈɣʲnʲəØʲʷμʷ -> ˈkˠaØʲnʲ-ˈɣʲnʲəØʲμʷ
	ˈkʲaØʲʷdʷβʷəðʲ -> ˈkʲaØʲdʷβʷəðʲ


ˠ -> 0 / Ø[ʲʷˠ]|[aə] _ ::C::
Sample of maximum 20 input/output pairs:

	ˈØˠəØʲ.aˠrˠ -> ˈØˠəØʲ.arˠ
	ˈØˠaˠbˠsˠtˠaˠnˠadʲ -> ˈØˠabˠsˠtˠanˠadʲ
	ˈØˠaˠgˠaˠlˠðˠaˠμˠ -> ˈØˠagˠalˠðˠaμˠ
	ˈØˠakʷaβʷaˠrˠ -> ˈØˠakʷaβʷarˠ
	ˈØˠakʷaμʷaˠlˠ -> ˈØˠakʷaμʷalˠ
	ˈØˠaˠðˠaɣʲ -> ˈØˠaðˠaɣʲ
	ˈØˠaˠðˠaˠlˠtˠrˠaˠsˠ -> ˈØˠaðˠalˠtˠrˠasˠ
	ˈØˠaˠðˠβˠaˠrˠ -> ˈØˠaðˠβˠarˠ
	ˈØˠaˠðˠnˠaˠgˠalʷ -> ˈØˠaðˠnˠagˠalʷ
	ˈØˠaˠðˠrˠaˠðˠ -> ˈØˠaðˠrˠaðˠ
	ˈØˠagʲnʲaˠðˠ -> ˈØˠagʲnʲaðˠ
	ˈØˠamʲsʲaˠrˠ -> ˈØˠamʲsʲarˠ
	ˈØˠənʲaˠxˠ -> ˈØˠənʲaxˠ
	ˈØˠənʷaˠxˠ -> ˈØˠənʷaxˠ
	ˈØˠaŋʲgʲaˠlˠ -> ˈØˠaŋʲgʲalˠ
	ˈØˠaØˠɴʲsʲaˠμˠ -> ˈØˠaØˠɴʲsʲaμˠ
	ˈØˠərʲβʲaˠrˠtˠ -> ˈØˠərʲβʲarˠtˠ
	ˈØˠarʲxʲəɴʲaˠxˠ -> ˈØˠarʲxʲəɴʲaxˠ
	ˈØˠarʲxʲəsʲaˠxˠtˠ -> ˈØˠarʲxʲəsʲaxˠtˠ
	ˈØˠərʷkʷaˠrˠ -> ˈØˠərʷkʷarˠ


%%%% 24. Ensure /ə/ not /a/
%
% Only /ə/ not /a/ occurs in unstressed position for non-final short vowels.
%
a -> ə / (?<![ˈ]((Ø[ˠʲʷ])|((::C::[ˠʲʷ]){1,4}))) _ [^Ø]
Sample of maximum 20 input/output pairs:

	ˈØˠəØʲ.arˠ -> ˈØˠəØʲ.ərˠ
	ˈØˠabˠsˠtˠanˠadʲ -> ˈØˠabˠsˠtˠənˠədʲ
	ˈØˠagˠalˠðˠaμˠ -> ˈØˠagˠəlˠðˠəμˠ
	ˈØˠakʷaβʷarˠ -> ˈØˠakʷəβʷərˠ
	ˈØˠakʷaμʷalˠ -> ˈØˠakʷəμʷəlˠ
	ˈØˠaðˠaɣʲ -> ˈØˠaðˠəɣʲ
	ˈØˠaðˠalˠtˠrˠasˠ -> ˈØˠaðˠəlˠtˠrˠəsˠ
	ˈØˠaðˠβˠarˠ -> ˈØˠaðˠβˠərˠ
	ˈØˠaðˠnˠagˠalʷ -> ˈØˠaðˠnˠəgˠəlʷ
	ˈØˠaðˠrˠaðˠ -> ˈØˠaðˠrˠəðˠ
	ˈØˠagʲnʲaðˠ -> ˈØˠagʲnʲəðˠ
	ˈØˠamʲsʲarˠ -> ˈØˠamʲsʲərˠ
	ˈØˠənʲaxˠ -> ˈØˠənʲəxˠ
	ˈØˠənʷaxˠ -> ˈØˠənʷəxˠ
	ˈØˠaŋʲgʲalˠ -> ˈØˠaŋʲgʲəlˠ
	ˈØˠaØˠɴʲsʲaμˠ -> ˈØˠaØˠɴʲsʲəμˠ
	ˈØˠərʲβʲarˠtˠ -> ˈØˠərʲβʲərˠtˠ
	ˈØˠarʲxʲəɴʲaxˠ -> ˈØˠarʲxʲəɴʲəxˠ
	ˈØˠarʲxʲəsʲaxˠtˠ -> ˈØˠarʲxʲəsʲəxˠtˠ
	ˈØˠərʷkʷarˠ -> ˈØˠərʷkʷərˠ


%%%% 25. /a/ before a-colour
%
% Only /a/ occurs before a-colour
%
ə -> a / _ ::C::ˠ
Sample of maximum 20 input/output pairs:

	ˈØˠəØʲ.ərˠ -> ˈØˠəØʲ.arˠ
	ˈØˠabˠsˠtˠənˠədʲ -> ˈØˠabˠsˠtˠanˠədʲ
	ˈØˠagˠəlˠðˠəμˠ -> ˈØˠagˠalˠðˠaμˠ
	ˈØˠakʷəβʷərˠ -> ˈØˠakʷəβʷarˠ
	ˈØˠakʷəμʷəlˠ -> ˈØˠakʷəμʷalˠ
	ˈØˠaðˠəlˠtˠrˠəsˠ -> ˈØˠaðˠalˠtˠrˠasˠ
	ˈØˠaðˠβˠərˠ -> ˈØˠaðˠβˠarˠ
	ˈØˠaðˠnˠəgˠəlʷ -> ˈØˠaðˠnˠagˠəlʷ
	ˈØˠaðˠrˠəðˠ -> ˈØˠaðˠrˠaðˠ
	ˈØˠagʲnʲəðˠ -> ˈØˠagʲnʲaðˠ
	ˈØˠamʲsʲərˠ -> ˈØˠamʲsʲarˠ
	ˈØˠənʲəxˠ -> ˈØˠənʲaxˠ
	ˈØˠənʷəxˠ -> ˈØˠənʷaxˠ
	ˈØˠaŋʲgʲəlˠ -> ˈØˠaŋʲgʲalˠ
	ˈØˠaØˠɴʲsʲəμˠ -> ˈØˠaØˠɴʲsʲaμˠ
	ˈØˠərʲβʲərˠtˠ -> ˈØˠərʲβʲarˠtˠ
	ˈØˠarʲxʲəɴʲəxˠ -> ˈØˠarʲxʲəɴʲaxˠ
	ˈØˠarʲxʲəsʲəxˠtˠ -> ˈØˠarʲxʲəsʲaxˠtˠ
	ˈØˠərʷkʷərˠ -> ˈØˠərʷkʷarˠ
	ˈØˠarʲəgˠ -> ˈØˠarʲagˠ


%%%% 26. The hiatus marker
%
% The hiatus marker is no longer necessary
%
\. -> 0 / _
Sample of maximum 20 input/output pairs:

	ˈØˠəØʲ.arˠ -> ˈØˠəØʲarˠ
	ˈbˠaØˠ.aØʲ -> ˈbˠaØˠaØʲ
	ˈbʲəØʲ.aðˠ -> ˈbʲəØʲaðˠ
	ˈdʲaØˠ.axˠtˠ -> ˈdʲaØˠaxˠtˠ
	ˈdʲaØˠ.aðˠ -> ˈdʲaØˠaðˠ
	ˈdʲaØˠ.aðˠ -> ˈdʲaØˠaðˠ
	ˈdʲəØʲ.asˠ -> ˈdʲəØʲasˠ
	ˈdʲəØʲ.asˠ -> ˈdʲəØʲasˠ
	ˈdʲəØʲ.əØʷ -> ˈdʲəØʲəØʷ
	ˈdʷrʷəØʲ.əØʲ -> ˈdʷrʷəØʲəØʲ
	ˈʟˠaØˠ.aØʲ -> ˈʟˠaØˠaØʲ
	ˈʟʲəØʲ.aØʲ -> ˈʟʲəØʲaØʲ
	ˈʟʲəØʲ.aØʲ -> ˈʟʲəØʲaØʲ
	ˈmˠaØˠ.aμˠ -> ˈmˠaØˠaμˠ
	ˈʀʲaØˠ.aØʲ -> ˈʀʲaØˠaØʲ
	ˈsˠanʲ-ˈlˠaØˠ.aØʲ -> ˈsˠanʲ-ˈlˠaØˠaØʲ
	ˈtʲrʲəØʲ.arˠ -> ˈtʲrʲəØʲarˠ
