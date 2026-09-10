"""Curated topic modules.

Each topic holds a small set of high-value content words per language, with an
English gloss. The engine uses these two ways:

  1. Words that match a topic the learner cares about get their rank boosted.
  2. Curated words that fall outside the raw frequency list are still injected
     into the candidate pool (so e.g. "passport" can make the list for someone
     who is learning the language mainly to travel).

This is seed data. It is meant to be expanded - add more words per topic, or
more topics, and the engine picks them up automatically.
"""

TOPIC_LABELS = {
    "family": "Family & relationships",
    "food_drink": "Food & drink",
    "work_office": "Work & office",
    "school_study": "School & studying",
    "travel_tourism": "Travel & tourism",
    "technology": "Phones & technology",
    "health_body": "Health & the body",
    "home_daily": "Home & daily life",
    "shopping_money": "Shopping & money",
    "nature_weather": "Nature & weather",
    "social_emotions": "Socialising & emotions",
    "transport": "Getting around",
    "sports_fitness": "Sport & fitness",
    "arts_media": "Arts & media",
    "city_places": "The city & places",
}

TOPICS = {
    "es": {
        "family": [
            ("familia", "family"), ("madre", "mother"), ("padre", "father"),
            ("hijo", "son"), ("hija", "daughter"), ("hermano", "brother"),
            ("hermana", "sister"), ("niño", "child"), ("esposo", "husband"),
            ("esposa", "wife"), ("padres", "parents"), ("abuela", "grandmother"),
            ("abuelo", "grandfather"), ("bebé", "baby"), ("pareja", "partner / couple"),
        ],
        "food_drink": [
            ("agua", "water"), ("pan", "bread"), ("café", "coffee"),
            ("leche", "milk"), ("vino", "wine"), ("cerveza", "beer"),
            ("carne", "meat"), ("pescado", "fish (food)"), ("fruta", "fruit"),
            ("verdura", "vegetable"), ("huevo", "egg"), ("queso", "cheese"),
            ("arroz", "rice"), ("azúcar", "sugar"), ("sal", "salt"),
            ("desayuno", "breakfast"), ("almuerzo", "lunch"), ("cena", "dinner"),
            ("restaurante", "restaurant"), ("menú", "menu"),
        ],
        "work_office": [
            ("trabajo", "work / job"), ("empleo", "employment"), ("oficina", "office"),
            ("jefe", "boss"), ("colega", "colleague"), ("reunión", "meeting"),
            ("correo", "email / mail"), ("ordenador", "computer"), ("proyecto", "project"),
            ("cliente", "client"), ("sueldo", "salary"), ("empresa", "company"),
            ("contrato", "contract"), ("horario", "schedule"), ("tarea", "task"),
        ],
        "school_study": [
            ("escuela", "school"), ("profesor", "teacher"), ("estudiante", "student"),
            ("clase", "class"), ("libro", "book"), ("examen", "exam"),
            ("deberes", "homework"), ("universidad", "university"), ("pregunta", "question"),
            ("respuesta", "answer"), ("palabra", "word"), ("idioma", "language"),
            ("lección", "lesson"), ("nota", "grade / note"), ("aprender", "to learn"),
        ],
        "travel_tourism": [
            ("viaje", "trip"), ("hotel", "hotel"), ("aeropuerto", "airport"),
            ("billete", "ticket"), ("pasaporte", "passport"), ("equipaje", "luggage"),
            ("mapa", "map"), ("playa", "beach"), ("museo", "museum"),
            ("turista", "tourist"), ("reserva", "reservation"), ("vuelo", "flight"),
            ("estación", "station"), ("guía", "guide"), ("foto", "photo"),
        ],
        "technology": [
            ("teléfono", "phone"), ("internet", "internet"), ("pantalla", "screen"),
            ("contraseña", "password"), ("aplicación", "app"), ("wifi", "wifi"),
            ("batería", "battery"), ("mensaje", "message"), ("archivo", "file"),
            ("teclado", "keyboard"), ("red", "network"), ("descargar", "to download"),
            ("cargador", "charger"), ("cámara", "camera"), ("actualización", "update"),
        ],
        "health_body": [
            ("médico", "doctor"), ("hospital", "hospital"), ("medicina", "medicine"),
            ("dolor", "pain"), ("cabeza", "head"), ("estómago", "stomach"),
            ("mano", "hand"), ("pie", "foot"), ("ojo", "eye"), ("diente", "tooth"),
            ("fiebre", "fever"), ("sangre", "blood"), ("cita", "appointment"),
            ("farmacia", "pharmacy"), ("enfermo", "sick"),
        ],
        "home_daily": [
            ("casa", "house / home"), ("habitación", "room"), ("cocina", "kitchen"),
            ("baño", "bathroom"), ("cama", "bed"), ("puerta", "door"),
            ("ventana", "window"), ("mesa", "table"), ("silla", "chair"),
            ("llave", "key"), ("luz", "light"), ("suelo", "floor"),
            ("pared", "wall"), ("limpiar", "to clean"), ("dormir", "to sleep"),
        ],
        "shopping_money": [
            ("dinero", "money"), ("precio", "price"), ("tienda", "shop"),
            ("mercado", "market"), ("efectivo", "cash"), ("tarjeta", "card"),
            ("cambio", "change"), ("cuenta", "bill / account"), ("barato", "cheap"),
            ("caro", "expensive"), ("comprar", "to buy"), ("vender", "to sell"),
            ("rebaja", "sale / discount"), ("recibo", "receipt"), ("banco", "bank"),
        ],
        "nature_weather": [
            ("sol", "sun"), ("lluvia", "rain"), ("viento", "wind"), ("nieve", "snow"),
            ("nube", "cloud"), ("cielo", "sky"), ("árbol", "tree"), ("flor", "flower"),
            ("río", "river"), ("montaña", "mountain"), ("mar", "sea"),
            ("frío", "cold"), ("calor", "heat"), ("tiempo", "weather"), ("tormenta", "storm"),
        ],
        "social_emotions": [
            ("amigo", "friend"), ("amor", "love"), ("feliz", "happy"),
            ("triste", "sad"), ("enfadado", "angry"), ("cansado", "tired"),
            ("asustado", "afraid"), ("contento", "glad"), ("perdón", "sorry"),
            ("gracias", "thank you"), ("hola", "hello"), ("adiós", "goodbye"),
            ("sentimiento", "feeling"), ("divertido", "fun"), ("favor", "favour"),
        ],
        "transport": [
            ("coche", "car"), ("autobús", "bus"), ("tren", "train"),
            ("bicicleta", "bicycle"), ("carretera", "road"), ("calle", "street"),
            ("conductor", "driver"), ("parada", "stop"), ("tráfico", "traffic"),
            ("gasolina", "petrol / gas"), ("aparcar", "to park"), ("izquierda", "left"),
            ("derecha", "right"), ("recto", "straight ahead"), ("semáforo", "traffic light"),
        ],
        "sports_fitness": [
            ("partido", "match"), ("equipo", "team"), ("pelota", "ball"),
            ("correr", "to run"), ("nadar", "to swim"), ("gimnasio", "gym"),
            ("jugador", "player"), ("ganar", "to win"), ("perder", "to lose"),
            ("ejercicio", "exercise"), ("músculo", "muscle"), ("fuerte", "strong"),
            ("caminar", "to walk"), ("entrenar", "to train"), ("juego", "game"),
        ],
        "arts_media": [
            ("película", "film"), ("música", "music"), ("canción", "song"),
            ("actor", "actor"), ("cuadro", "painting"), ("teatro", "theatre"),
            ("noticias", "news"), ("historia", "story / history"), ("arte", "art"),
            ("concierto", "concert"), ("autor", "author"), ("escena", "scene"),
            ("bailar", "to dance"), ("leer", "to read"), ("dibujo", "drawing"),
        ],
        "city_places": [
            ("ciudad", "city"), ("plaza", "square"), ("parque", "park"),
            ("iglesia", "church"), ("puente", "bridge"), ("edificio", "building"),
            ("esquina", "corner"), ("centro", "centre"), ("barrio", "neighbourhood"),
            ("dirección", "address / direction"), ("biblioteca", "library"),
            ("pueblo", "town / village"), ("acera", "pavement / sidewalk"),
            ("farola", "streetlight"), ("ayuntamiento", "town hall"),
        ],
    },
    "fr": {
        "family": [
            ("famille", "family"), ("mère", "mother"), ("père", "father"),
            ("fils", "son"), ("fille", "daughter / girl"), ("frère", "brother"),
            ("sœur", "sister"), ("enfant", "child"), ("mari", "husband"),
            ("femme", "wife / woman"), ("parents", "parents"), ("grand-mère", "grandmother"),
            ("grand-père", "grandfather"), ("bébé", "baby"), ("couple", "couple"),
        ],
        "food_drink": [
            ("eau", "water"), ("pain", "bread"), ("café", "coffee"),
            ("lait", "milk"), ("vin", "wine"), ("bière", "beer"),
            ("viande", "meat"), ("poisson", "fish (food)"), ("fruit", "fruit"),
            ("légume", "vegetable"), ("œuf", "egg"), ("fromage", "cheese"),
            ("riz", "rice"), ("sucre", "sugar"), ("sel", "salt"),
            ("petit-déjeuner", "breakfast"), ("déjeuner", "lunch"), ("dîner", "dinner"),
            ("restaurant", "restaurant"), ("carte", "menu / map"),
        ],
        "work_office": [
            ("travail", "work"), ("emploi", "job"), ("bureau", "office / desk"),
            ("patron", "boss"), ("collègue", "colleague"), ("réunion", "meeting"),
            ("courriel", "email"), ("ordinateur", "computer"), ("projet", "project"),
            ("client", "client"), ("salaire", "salary"), ("entreprise", "company"),
            ("contrat", "contract"), ("horaire", "schedule"), ("tâche", "task"),
        ],
        "school_study": [
            ("école", "school"), ("professeur", "teacher"), ("étudiant", "student"),
            ("classe", "class"), ("livre", "book"), ("examen", "exam"),
            ("devoirs", "homework"), ("université", "university"), ("question", "question"),
            ("réponse", "answer"), ("mot", "word"), ("langue", "language / tongue"),
            ("leçon", "lesson"), ("note", "grade / note"), ("apprendre", "to learn"),
        ],
        "travel_tourism": [
            ("voyage", "trip"), ("hôtel", "hotel"), ("aéroport", "airport"),
            ("billet", "ticket"), ("passeport", "passport"), ("bagage", "luggage"),
            ("plan", "map / plan"), ("plage", "beach"), ("musée", "museum"),
            ("touriste", "tourist"), ("réservation", "reservation"), ("vol", "flight"),
            ("gare", "station"), ("guide", "guide"), ("photo", "photo"),
        ],
        "technology": [
            ("téléphone", "phone"), ("internet", "internet"), ("écran", "screen"),
            ("passe", "password (mot de passe)"), ("application", "app"), ("wifi", "wifi"),
            ("batterie", "battery"), ("message", "message"), ("fichier", "file"),
            ("clavier", "keyboard"), ("réseau", "network"), ("télécharger", "to download"),
            ("chargeur", "charger"), ("caméra", "camera"), ("logiciel", "software"),
        ],
        "health_body": [
            ("médecin", "doctor"), ("hôpital", "hospital"), ("médicament", "medicine"),
            ("douleur", "pain"), ("tête", "head"), ("ventre", "belly / stomach"),
            ("main", "hand"), ("pied", "foot"), ("œil", "eye"), ("dent", "tooth"),
            ("fièvre", "fever"), ("sang", "blood"), ("rendez-vous", "appointment"),
            ("pharmacie", "pharmacy"), ("malade", "sick"),
        ],
        "home_daily": [
            ("maison", "house / home"), ("chambre", "room / bedroom"), ("cuisine", "kitchen"),
            ("douche", "shower"), ("lit", "bed"), ("porte", "door"),
            ("fenêtre", "window"), ("table", "table"), ("chaise", "chair"),
            ("clé", "key"), ("lumière", "light"), ("sol", "floor / ground"),
            ("mur", "wall"), ("nettoyer", "to clean"), ("dormir", "to sleep"),
        ],
        "shopping_money": [
            ("argent", "money / silver"), ("prix", "price"), ("magasin", "shop"),
            ("marché", "market"), ("espèces", "cash"), ("carte", "card"),
            ("monnaie", "change / currency"), ("addition", "bill (restaurant)"),
            ("cher", "expensive / dear"), ("acheter", "to buy"), ("vendre", "to sell"),
            ("solde", "sale"), ("reçu", "receipt"), ("banque", "bank"), ("caisse", "checkout"),
        ],
        "nature_weather": [
            ("soleil", "sun"), ("pluie", "rain"), ("vent", "wind"), ("neige", "snow"),
            ("nuage", "cloud"), ("ciel", "sky"), ("arbre", "tree"), ("fleur", "flower"),
            ("rivière", "river"), ("montagne", "mountain"), ("mer", "sea"),
            ("froid", "cold"), ("chaud", "hot"), ("temps", "weather / time"), ("orage", "storm"),
        ],
        "social_emotions": [
            ("ami", "friend"), ("amour", "love"), ("heureux", "happy"),
            ("triste", "sad"), ("fâché", "angry"), ("fatigué", "tired"),
            ("peur", "fear"), ("content", "glad"), ("pardon", "sorry"),
            ("merci", "thank you"), ("bonjour", "hello"), ("revoir", "goodbye (au revoir)"),
            ("sentiment", "feeling"), ("amusant", "fun"), ("sourire", "smile"),
        ],
        "transport": [
            ("voiture", "car"), ("bus", "bus"), ("train", "train"),
            ("vélo", "bicycle"), ("route", "road"), ("rue", "street"),
            ("conducteur", "driver"), ("arrêt", "stop"), ("circulation", "traffic"),
            ("essence", "petrol / gas"), ("garer", "to park"), ("gauche", "left"),
            ("droite", "right"), ("tout droit", "straight ahead"), ("feu", "traffic light / fire"),
        ],
        "sports_fitness": [
            ("match", "match"), ("équipe", "team"), ("ballon", "ball"),
            ("courir", "to run"), ("nager", "to swim"), ("gymnase", "gym"),
            ("joueur", "player"), ("gagner", "to win"), ("perdre", "to lose"),
            ("exercice", "exercise"), ("muscle", "muscle"), ("fort", "strong"),
            ("marcher", "to walk"), ("entraîner", "to train"), ("jeu", "game"),
        ],
        "arts_media": [
            ("film", "film"), ("musique", "music"), ("chanson", "song"),
            ("acteur", "actor"), ("tableau", "painting / board"), ("théâtre", "theatre"),
            ("nouvelles", "news"), ("histoire", "story / history"), ("art", "art"),
            ("concert", "concert"), ("auteur", "author"), ("scène", "scene / stage"),
            ("danser", "to dance"), ("lire", "to read"), ("dessin", "drawing"),
        ],
        "city_places": [
            ("ville", "city / town"), ("place", "square / place"), ("parc", "park"),
            ("église", "church"), ("pont", "bridge"), ("bâtiment", "building"),
            ("coin", "corner"), ("centre", "centre"), ("quartier", "neighbourhood"),
            ("adresse", "address"), ("bibliothèque", "library"), ("village", "village"),
            ("trottoir", "pavement / sidewalk"), ("mairie", "town hall"), ("marché", "market"),
        ],
    },
}


def build_indexes():
    """Return (word -> set(topics), word -> gloss) per language."""
    word_topics = {}
    word_gloss = {}
    for lang, topics in TOPICS.items():
        wt = {}
        wg = {}
        for topic, entries in topics.items():
            for word, gloss in entries:
                wt.setdefault(word, set()).add(topic)
                wg.setdefault(word, gloss)
        word_topics[lang] = wt
        word_gloss[lang] = wg
    return word_topics, word_gloss


WORD_TOPICS, WORD_GLOSS = build_indexes()
