class ClasseLigne4():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((350, "PORTE DE CLIGNANCOURT", 2))
    liste_stations.append((350, "PORTE DE CLIGNANCOURT", 4))
    liste_stations.append((630, "SIMPLON", 2))
    liste_stations.append((630, "SIMPLON", 4))
    liste_stations.append((845, "MARCADET POISSONNIERS", 2))
    liste_stations.append((845, "MARCADET POISSONNIERS", 4))
    liste_stations.append((1060, "CHATEAU ROUGE", 2))
    liste_stations.append((1060, "CHATEAU ROUGE", 4))
    liste_stations.append((1375, "BARBES ROCHECHOUART", 2))
    liste_stations.append((1375, "BARBES ROCHECHOUART", 4))
    liste_stations.append((1655, "GARE DU NORD", 2))
    liste_stations.append((1655, "GARE DU NORD", 4))
    liste_stations.append((1935, "GARE DE L'EST", 2))
    liste_stations.append((1935, "GARE DE L'EST", 4))
    liste_stations.append((2215, "CHATEAU D'EAU", 2))
    liste_stations.append((2215, "CHATEAU D'EAU", 4))
    liste_stations.append((2495, "STARSBOURG ST DENIS", 2))
    liste_stations.append((2495, "STARSBOURG ST DENIS", 4))
    liste_stations.append((2775, "REAUMUR SEBASTOPOL", 2))
    liste_stations.append((2775, "REAUMUR SEBASTOPOL", 4))
    liste_stations.append((3055, "ETIENNE MARCEL", 2))
    liste_stations.append((3055, "ETIENNE MARCEL", 4))
    liste_stations.append((3335, "LES HALLES", 2))
    liste_stations.append((3335, "LES HALLES", 4))
    liste_stations.append((3615, "CHATELET",2))
    liste_stations.append((3615, "CHATELET", 4))
    liste_stations.append((3855, "CITE",2))
    liste_stations.append((3855, "CITE", 4))
    liste_stations.append((4135, "SAINT MICHEL",2))
    liste_stations.append((4135, "SAINT MICHEL",4))
    liste_stations.append((4415, "ODEON",2))
    liste_stations.append((4415, "ODEON", 4))
    liste_stations.append((4695, "ST GERMAIN DES PRES",2))
    liste_stations.append((4695, "ST GERMAIN DES PRES", 4))
    liste_stations.append((4975, "SAINT SULPICE",2))
    liste_stations.append((4975, "SAINT SULPICE", 4))
    liste_stations.append((5255, "SAINT PLACIDE",2))
    liste_stations.append((5255, "SAINT PLACIDE", 4))
    liste_stations.append((5535, "MONTPARNASSE BIENVENUE",2))
    liste_stations.append((5535, "MONTPARNASSE BIENVENUE", 4))
    #liste_stations.append((5815, "VAVIN",2))
    #liste_stations.append((5815, "VAVIN", 4))
    liste_stations.append((6095, "RASPAIL",2))
    liste_stations.append((6095, "RASPAIL", 4))
    liste_stations.append((6375, "DENFERT ROCHEREAU",2))
    liste_stations.append((6375, "DENFERT ROCHEREAU", 4))
    liste_stations.append((6622, "MOUTON DUVERNET",2))
    liste_stations.append((6622, "MOUTON DUVERNET", 4))
    liste_stations.append((6869, "ALESIA",2))
    liste_stations.append((6869, "ALESIA", 4))
    liste_stations.append((7119, "PORTE D'ORLEANS",2))
    liste_stations.append((7119, "PORTE D'ORLEANS", 4))
    liste_stations.append((7369, "MAIRIE DE MONTROUGE",2))
    liste_stations.append((7369, "MAIRIE DE MONTROUGE", 4))
    liste_stations.append((7619, "BARBARA",2))
    liste_stations.append((7619, "BARBARA", 4))
    liste_stations.append((7869, "BAGNEUX LUCIE AUBRAC",2))
    liste_stations.append((7869, "BAGNEUX LUCIE AUBRAC", 4))

    liste_eguillages = []
    liste_eguillages.append((260, 100, 290, 130, 1, "Eg PORTE DE CLIGNANCOURT1"))
    liste_eguillages.append((460, 100, 490, 130, 0, "Eg PORTE DE CLIGNANCOURT2"))
    liste_eguillages.append((1260, 100, 1290, 130, 0, "Eg BARBES ROCHECHOUART1"))
    liste_eguillages.append((2870, 100, 2900, 130, 0, "Eg REAUMUR SEBASTOPOL1"))
    liste_eguillages.append((3170, 130, 3200, 160, 0, "Eg ETIENNE MARCEL1"))
    liste_eguillages.append((3260, 130,3290, 100, 0, "Eg chatelet1"))
    liste_eguillages.append((4260, 100,4290, 130, 0, "Eg ODEON1"))
    liste_eguillages.append((4890, 70,4920, 100, 0, "Eg SAINT SULPICE1"))
    liste_eguillages.append((5750, 100,5780, 130, 0, "Eg VAVIN1"))
    liste_eguillages.append((7200, 130,7230, 100, 0, "Eg PORTE D'ORLEANS1"))
    liste_eguillages.append((7300, 130,7330, 100, 0, "Eg PORTE D'ORLEANS2"))
    liste_eguillages.append((7450, 130,7480, 100, 0, "Eg MAIRIE DE MONTROUGE1"))
    liste_eguillages.append((7820, 100,7850, 70, 2, "Eg BAGNEUX1"))
    liste_eguillages.append((7820, 130,7850, 100, 0, "Eg BAGNEUX2"))
    liste_eguillages.append((7970, 130,8000, 100, 1, "Eg BAGNEUX3"))
    liste_eguillages.append((8020, 100,8050, 70, 1, "Eg BAGNEUX4"))
    liste_eguillages.append((8020, 70,8050, 100, 0, "Eg BAGNEUX5"))
    liste_eguillages.append((8120, 100,8150, 70, 0, "Eg BAGNEUX6"))
    liste_eguillages.append((8120, 130,8150, 100, 0, "Eg BAGNEUX7"))

    liste_eguillages.append((7058, 160, 7088, 190, 0, "Eg D1"))
    liste_eguillages.append((7088, 190, 7118, 220, 0, "Eg D2"))
    liste_eguillages.append((7118, 220, 7148, 250, 0, "Eg D3"))
    liste_eguillages.append((7148, 250, 7178, 280, 0, "Eg D4"))
    liste_eguillages.append((7178, 280, 7208, 310, 0, "Eg D5"))

    liste_terminus = []
    liste_terminus.append((200, 100, " PORTE DE CLIGNANCOURT1"))
    #liste_terminus.append((5880, 130, " VAVIN1"))
    #liste_terminus.append((7200, 130, " MAIRIE DE MONTROUGE1"))
    liste_terminus.append((8200, 70, "BAGNEUX LUCIE AUBRAC1"))
    liste_terminus.append((8200, 100, "BAGNEUX LUCIE AUBRAC2"))
    liste_terminus.append((8200, 130, "BAGNEUX LUCIE AUBRAC 3"))
    liste_terminus.append((8100, 70, "BAGNEUX LUCIE AUBRAC 4"))


    liste_metro = []
    #train direction chateau de vincennes
    #depart train garage la defense
    liste_metro.append(("Train 2", 10,  1, 80,"#FFCC45" ))
    #depart train esplanade de la defense
    liste_metro.append(("Train 3",430, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 4", 6422, 1, 80, "#FFCC45"))
    liste_metro.append(("Train 5", 6422, 1, 80, "#FFCC45"))
    liste_metro.append(("Train 6",645,  1, 80, "#FFCC45" ))
    liste_metro.append(("Train 7", 860, 1,80, "#FFCC45" ))
    liste_metro.append(("Train 8",1175, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 9",1455,  1, 80, "#FFCC45" ))
    liste_metro.append(("Train 10", 1735, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 11",2015, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 12",2295,  1,80, "#FFCC45" ))
    liste_metro.append(("Train 13", 2575, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 14",2855, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 15",3135,  1,80 , "#FFCC45" ))
    liste_metro.append(("Train 16", 3415, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 17",3655, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 18",3935,  1,80, "#FFCC45" ))
    liste_metro.append(("Train 19", 4215, 1,80 , "#FFCC45" ))
    liste_metro.append(("Train 20",4495, 1, 80 , "#FFCC45" ))
    liste_metro.append(("Train 21",4775,  1,80 , "#FFCC45" ))
    liste_metro.append(("Train 22", 5055, 1, 80 , "#FFCC45" ))
    liste_metro.append(("Train 23",5335, 1,80 , "#FFCC45" ))
    liste_metro.append(("Train 24",5615,  1, 80 , "#FFCC45" ))
    liste_metro.append(("Train 25", 5335, -1,50 , "#FFCC45" ))
    liste_metro.append(("Train 26",430, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 27",10,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 28", 6422, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 29",6175, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 30",645,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 31", 860, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 32",1175, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 33",1455,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 34", 1735, -1,50 , "#FFCC45" ))
    liste_metro.append(("Train 35",2015, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 36",2295,  -1, 50, "#FFCC45" ))
    liste_metro.append(("Train 37", 2575, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 38",2855, -1, 50, "#FFCC45" ))
    liste_metro.append(("Train 39",3135,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 40", 3415, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 41",3655, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 42",3935,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 43", 4215, -1, 50, "#FFCC45" ))
    liste_metro.append(("Train 44",4495, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 45",4775,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 46", 5055, -1,50 , "#FFCC45" ))
    liste_metro.append(("Train 47",5335, -1, 50, "#FFCC45" ))
    liste_metro.append(("Train 48",5615,  -1,50 , "#FFCC45" ))
    liste_metro.append(("Train 49",6869,  1, 80, "#FFCC45" ))
    liste_metro.append(("Train 50", 6869, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 51",7119, 1, 80, "#FFCC45" ))
    liste_metro.append(("Train 52",7119,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 53", 7369, 1, 80 , "#FFCC45" ))
    liste_metro.append(("Train 54",7369, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 55",7619,  1, 80 , "#FFCC45" ))
    liste_metro.append(("Train 56", 7619, -1, 50, "#FFCC45" ))
    liste_metro.append(("Train 57",4495, -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 58",4775,  -1, 50 , "#FFCC45" ))
    liste_metro.append(("Train 59", 7869, 1,80 , "#FFCC45" ))
    liste_metro.append(("Train 60",7869, -1, 50, "#FFCC45" ))
    liste_metro.append(("Train 61", 9050, 1,80 , "#FFCC45" ))
    liste_metro.append(("Train 62",7869, -1, 50, "#FFCC45" ))

    liste_lignes = []
    liste_lignes.append((10, 100, 8250, 100, "#FCFF42", 2))
    liste_lignes.append((10, 130, 8250, 130, "#FCFF42", 2))
    liste_lignes.append((3200, 160, 3300, 160, "#FCFF42", 2))
    liste_lignes.append((4790, 70, 4890, 70, "#FCFF42", 2))
    liste_lignes.append((7850, 70, 8250, 70, "#FCFF42", 2))
