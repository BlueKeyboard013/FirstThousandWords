"""Mandatory "glue" words: articles, pronouns, prepositions, conjunctions,
auxiliary verbs and high-frequency particles.

These are deliberately kept OUT of the personalised 1000-word list because
every learner needs them regardless of what they talk about. They are served
as a separate list instead.

Each entry is (word, short English gloss). Keep words lowercase.
"""

FUNCTION_WORDS = {
    "es": [
        # articles
        ("el", "the (m.)"), ("la", "the (f.)"), ("los", "the (m. pl.)"),
        ("las", "the (f. pl.)"), ("un", "a (m.)"), ("una", "a (f.)"),
        ("unos", "some (m.)"), ("unas", "some (f.)"), ("lo", "the / it (neuter)"),
        # prepositions
        ("de", "of / from"), ("a", "to / at"), ("en", "in / on"),
        ("con", "with"), ("por", "for / by / through"), ("para", "for / in order to"),
        ("sin", "without"), ("sobre", "on / about"), ("entre", "between"),
        ("hasta", "until / up to"), ("desde", "from / since"), ("hacia", "toward"),
        ("según", "according to"), ("durante", "during"), ("contra", "against"),
        ("tras", "after / behind"),
        # conjunctions
        ("y", "and"), ("e", "and (before i-)"), ("o", "or"), ("u", "or (before o-)"),
        ("pero", "but"), ("sino", "but rather"), ("porque", "because"),
        ("que", "that / which"), ("si", "if"), ("aunque", "although"),
        ("como", "as / like"), ("cuando", "when"), ("mientras", "while"),
        ("pues", "so / well"), ("ni", "nor"),
        # pronouns & determiners
        ("yo", "I"), ("tú", "you"), ("él", "he"), ("ella", "she"),
        ("usted", "you (formal)"), ("nosotros", "we"), ("vosotros", "you (pl.)"),
        ("ellos", "they (m.)"), ("ellas", "they (f.)"), ("ustedes", "you (pl.)"),
        ("me", "me"), ("te", "you (obj.)"), ("se", "oneself"), ("nos", "us"),
        ("os", "you (pl. obj.)"), ("le", "to him / her"), ("les", "to them"),
        ("mi", "my"), ("tu", "your"), ("su", "his / her / their"),
        ("mis", "my (pl.)"), ("tus", "your (pl.)"), ("sus", "their (pl.)"),
        ("nuestro", "our"), ("este", "this"), ("esta", "this (f.)"),
        ("esto", "this (neuter)"), ("ese", "that"), ("esa", "that (f.)"),
        ("eso", "that (neuter)"), ("aquel", "that (over there)"),
        ("estos", "these"), ("esos", "those"),
        ("qué", "what"), ("quién", "who"), ("cuál", "which"),
        ("cuánto", "how much"), ("cómo", "how"), ("dónde", "where"),
        ("cuándo", "when"), ("cuanto", "as much as"),
        # auxiliary / core verbs
        ("ser", "to be (essence)"), ("estar", "to be (state)"),
        ("haber", "to have (auxiliary)"), ("he", "I have"), ("has", "you have"),
        ("ha", "he/she has"), ("hemos", "we have"), ("han", "they have"),
        ("es", "is"), ("son", "are"), ("soy", "I am"), ("eres", "you are"),
        ("está", "is (state)"), ("están", "are (state)"), ("estoy", "I am (state)"),
        ("fue", "was / went"), ("era", "was (ongoing)"), ("hay", "there is / are"),
        ("tener", "to have"), ("tiene", "has"), ("hace", "does / makes / ago"),
        # adverbs & particles
        ("no", "no / not"), ("sí", "yes"), ("muy", "very"), ("más", "more"),
        ("menos", "less"), ("también", "also"), ("tampoco", "neither"),
        ("ya", "already / now"), ("todavía", "still / yet"), ("aún", "still"),
        ("aquí", "here"), ("allí", "there"), ("ahí", "there"), ("ahora", "now"),
        ("luego", "later / then"), ("entonces", "then"), ("siempre", "always"),
        ("nunca", "never"), ("casi", "almost"), ("solo", "only / alone"),
        ("bien", "well"), ("mal", "badly"), ("así", "thus / like this"),
        ("tan", "so"), ("todo", "all / everything"), ("nada", "nothing"),
        ("algo", "something"), ("alguien", "someone"), ("nadie", "nobody"),
        ("cada", "each"), ("otro", "other / another"), ("mismo", "same"),
        ("poco", "little / few"), ("mucho", "a lot"), ("tanto", "so much"),
    ],
    "fr": [
        # articles
        ("le", "the (m.)"), ("la", "the (f.)"), ("les", "the (pl.)"),
        ("un", "a (m.)"), ("une", "a (f.)"), ("des", "some (pl.)"),
        ("du", "of the / some (m.)"), ("l", "the (before vowel)"),
        ("au", "to the (m.)"), ("aux", "to the (pl.)"),
        # prepositions
        ("de", "of / from"), ("à", "to / at"), ("en", "in / to"),
        ("dans", "in / inside"), ("sur", "on"), ("sous", "under"),
        ("avec", "with"), ("sans", "without"), ("pour", "for"),
        ("par", "by / through"), ("chez", "at (someone's place)"),
        ("vers", "toward"), ("entre", "between"), ("pendant", "during"),
        ("depuis", "since / for"), ("avant", "before"), ("après", "after"),
        ("contre", "against"), ("selon", "according to"),
        # conjunctions
        ("et", "and"), ("ou", "or"), ("mais", "but"), ("donc", "so / therefore"),
        ("car", "because"), ("or", "yet / now"), ("ni", "nor"),
        ("que", "that"), ("qui", "who / which"), ("si", "if"),
        ("quand", "when"), ("comme", "as / like"), ("lorsque", "when"),
        ("puisque", "since"), ("quoique", "although"),
        # pronouns & determiners
        ("je", "I"), ("tu", "you"), ("il", "he / it"), ("elle", "she / it"),
        ("on", "one / we"), ("nous", "we / us"), ("vous", "you"),
        ("ils", "they (m.)"), ("elles", "they (f.)"), ("me", "me"),
        ("te", "you (obj.)"), ("se", "oneself"), ("lui", "to him / her"),
        ("leur", "to them / their"), ("y", "there / to it"), ("moi", "me"),
        ("toi", "you"), ("soi", "oneself"), ("mon", "my (m.)"), ("ma", "my (f.)"),
        ("mes", "my (pl.)"), ("ton", "your (m.)"), ("ta", "your (f.)"),
        ("tes", "your (pl.)"), ("son", "his / her (m.)"), ("sa", "his / her (f.)"),
        ("ses", "his / her (pl.)"), ("notre", "our"), ("nos", "our (pl.)"),
        ("votre", "your"), ("vos", "your (pl.)"), ("leurs", "their (pl.)"),
        ("ce", "this / it"), ("cet", "this (m. before vowel)"), ("cette", "this (f.)"),
        ("ces", "these"), ("celui", "the one"), ("celle", "the one (f.)"),
        ("ça", "that / it"), ("cela", "that"), ("ceci", "this"),
        ("quel", "which (m.)"), ("quelle", "which (f.)"), ("quoi", "what"),
        ("dont", "whose / of which"), ("où", "where"),
        # auxiliaries / core verbs
        ("être", "to be"), ("avoir", "to have"), ("suis", "am"), ("es", "are"),
        ("est", "is"), ("sommes", "are (we)"), ("êtes", "are (you)"),
        ("sont", "are (they)"), ("ai", "have (I)"), ("as", "have (you)"),
        ("a", "has"), ("avons", "have (we)"), ("avez", "have (you)"),
        ("ont", "have (they)"), ("été", "been"), ("était", "was"),
        ("fait", "does / makes"), ("faire", "to do / make"),
        ("va", "goes"), ("aller", "to go"),
        # adverbs & particles
        ("ne", "not (part 1)"), ("pas", "not (part 2)"), ("non", "no"),
        ("oui", "yes"), ("plus", "more"), ("moins", "less"), ("très", "very"),
        ("trop", "too much"), ("aussi", "also"), ("encore", "still / again"),
        ("déjà", "already"), ("ici", "here"), ("là", "there"),
        ("maintenant", "now"), ("puis", "then"), ("ensuite", "next / then"),
        ("alors", "so / then"), ("toujours", "always"), ("jamais", "never"),
        ("souvent", "often"), ("presque", "almost"), ("seulement", "only"),
        ("bien", "well"), ("mal", "badly"), ("ainsi", "thus"),
        ("tout", "all / everything"), ("rien", "nothing"),
        ("personne", "nobody"), ("chaque", "each"), ("autre", "other"),
        ("même", "same / even"), ("peu", "little / few"), ("beaucoup", "a lot"),
    ],
}

FUNCTION_WORD_SET = {
    lang: {w for w, _ in entries} for lang, entries in FUNCTION_WORDS.items()
}

FUNCTION_WORD_GLOSS = {
    lang: {w: g for w, g in entries} for lang, entries in FUNCTION_WORDS.items()
}
