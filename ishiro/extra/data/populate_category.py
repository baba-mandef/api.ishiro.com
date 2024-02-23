from ishiro.category.models import Category
categories = [

    ################
    #####income#####
    ################
    {
        "label": "prestastions",
        "description": "Cette catégorie prends en compte les revenues relatifs aux différentes prestations de services que vous offrez.",
        "icon": "BriefcaseSolid",
        "category_type": "income"
    },


    {
        "label": "salaire",
        "description": "Cette catégorie prends en compte les revenus relatifs à vos différents revenus en tant que employé ou travailleur indépendant.",
        "icon": "WalletSolid",
        "category_type": "income"
    },


    {
        "label": "vente",
        "description": "Cette catégorie prends en compte les revenus relatifs a votre commerce ou a la vente d'articles en général.",
        "icon": "TagSolid",
        "category_type": "income"
    },


    {
        "label": "dons",
        "description": "Cette catégorie prends en compte les revenus relatifs aux dons et cadeaux.",
        "icon": "GiftsSolid",
        "category_type": "income"
    },

    {
        "label": "investissement",
        "description": "Cette catégorie prends en compte les revenus relatifs à vos différents investissements, placements d'argent etc...",
        "icon": "ChartLineSolid",
        "category_type": "income"
    },

    ################
    ####expense#####
    ################
    {


        "label": "nourritures",
        "description": "Cette catégorie prends en compte les dépenses relatives aliments et boissons.",
        "icon": "HamburgerSolid",
        "category_type": "expense"
    },
    {
        "label": "factures",
        "description": "Cette catégorie prends en compte les dépenses relatives aux différentes factures(Eau, électricité, internet...).",
        "icon": "FileInvoiceDollarSolid",
        "category_type": "expense"
    },
    {
        "label": "abonnements",
        "description": "Cette catégorie prends en compte les dépenses relatives aux abonnements à divers services.",
        "icon": "Bookmark",
        "category_type": "expense"
    },
    {
        "label": "achats",
        "description": "Cette catégorie prends en compte les dépenses relatives aux achats de tous genres .",
        "icon": "ShoppingCartSolid",
        "category_type": "expense"
    },
    {
        "label": "transports",
        "description": "Cette catégorie prends en compte les dépenses relatives aux moyens de transports.",
        "icon": "CarSolid",
        "category_type": "expense"
    },
    {
        "label": "éducations",
        "description": "Cette catégorie prends en compte les dépenses relatives à l'éducation(formations, universités, livres...).",
        "icon": "GraduationCapSolid",
        "category_type": "expense"
    },
    {
        "label": "divertissements",
        "description": "Cette catégorie prends en compte les dépenses relatives aux divertissements(films, jeux vidéos, concert...).",
        "icon": "GamepadSolid",
        "category_type": "expense"
    },
    {
        "label": "vêtements",
        "description": "Cette catégorie prends en compte les dépenses relatives aux vêtements, accessoires et autres.",
        "icon": "TshirtSolid",
        "category_type": "expense"
    },
    {
        "label": "soins personnels",
        "description": "Cette catégorie prends en compte les dépenses relatives aux soins personnels(coiffure, SPA, accessoires...).",
        "icon": "HeartSolid",
        "category_type": "expense"
    },
    {
        "label": "impots",
        "description": "Cette catégorie prends en compte les dépenses relatives aux impots et taxes",
        "icon": "MoneyCheckAltSolid",
        "category_type": "expense"
    },
    {
        "label": "vacances",
        "description": "Cette catégorie prends en compte les dépenses relatives aux voyages, vacances etc...",
        "icon": "UmbrellaBeachSolid",
        "category_type": "expense"
    },
    {
        "label": "dons",
        "description": "Cette catégorie prends en compte les dépenses relatives aux dons, aux cadeaux, contributions caritatives...",
        "icon": "GiftSolid",
        "category_type": "expense"
    },
    {
        "label": "santé",
        "description": "Cette catégorie prends en compte les dépenses à la santé et au bien être.",
        "icon": "MedkitSolid",
        "category_type": "expense"
    },

    {
        "label": "assurances",
        "description": "Cette catégorie prends en compte les dépenses relatives aux assurances et sécurité",
        "icon": "ShieldAltSolid",
        "category_type": "expense"
    },

    ################
    #####wallet#####
    ################

    {
        "label": "carte",
        "description": "Cette categorie prends en compte vos cartes bancaires.",
        "icon": "CreditCard",
        "category_type": "wallet"
    },

    {
        "label": "bank",
        "description": "Cette categorie prends en compte vos différents comptes bancaires",
        "icon": "LandmarkSolid",
        "category_type": "wallet"
    },
    {
        "label": "cash",
        "description": "Cette categorie prends en compte votre argent en liquidité",
        "icon": "MoneyBillAltSolid",
        "category_type": "wallet"
    },
    {
        "label": "wallet",
        "description": "Cette categorie prends en compte vos différents portefeuilles électronique(paypal, mobile money, btc...).",
        "icon": "WalletSolid",
        "category_type": "wallet"
    },
    {
        "label": "épargne",
        "description": "Cette categorie prends en compte vos différente épargnes et économies",
        "icon": "PiggyBankSolid",
        "category_type": "wallet"
    },

]

def populate_category(category_list=None):
    if category_list is None:
        category_list = categories
    for category in categories:
        Category.objects.create(**category)
        print(f'adding {category.type} category\'s : {category.label} ')

