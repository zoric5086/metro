class ClasseLigne4():
    #Position Station(x, nom, ligne de haut en base)
    # x, Nom, Offset, Duree Arret
    liste_stations = []
    liste_stations.append((350, "PORTE DE CLIGNANCOURT", 2, 280))
    liste_stations.append((350, "PORTE DE CLIGNANCOURT", 4, 280))
    liste_stations.append((630, "SIMPLON", 2, 280))
    liste_stations.append((630, "SIMPLON", 4, 280))
    liste_stations.append((845, "MARCADET POISSONNIERS", 2, 280))
    liste_stations.append((845, "MARCADET POISSONNIERS", 4, 280))
    liste_stations.append((1060, "CHATEAU ROUGE", 2, 280))
    liste_stations.append((1060, "CHATEAU ROUGE", 4, 280))
    liste_stations.append((1375, "BARBES ROCHECHOUART", 2, 280))
    liste_stations.append((1375, "BARBES ROCHECHOUART", 4, 280))
    liste_stations.append((1655, "GARE DU NORD", 2, 280))
    liste_stations.append((1655, "GARE DU NORD", 4, 280))
    liste_stations.append((1935, "GARE DE L'EST", 2, 280))
    liste_stations.append((1935, "GARE DE L'EST", 4, 280))
    liste_stations.append((2215, "CHATEAU D'EAU", 2, 280))
    liste_stations.append((2215, "CHATEAU D'EAU", 4, 280))
    liste_stations.append((2495, "STARSBOURG ST DENIS", 2, 280))
    liste_stations.append((2495, "STARSBOURG ST DENIS", 4, 280))
    liste_stations.append((2775, "REAUMUR SEBASTOPOL", 2, 280))
    liste_stations.append((2775, "REAUMUR SEBASTOPOL", 4, 280))
    liste_stations.append((3055, "ETIENNE MARCEL", 2, 280))
    liste_stations.append((3055, "ETIENNE MARCEL", 4, 280))
    liste_stations.append((3335, "LES HALLES", 2, 280))
    liste_stations.append((3335, "LES HALLES", 4, 280))
    liste_stations.append((3615, "CHATELET",2, 280))
    liste_stations.append((3615, "CHATELET", 4, 280))
    liste_stations.append((3855, "CITE",2, 280))
    liste_stations.append((3855, "CITE", 4, 280))
    liste_stations.append((4135, "SAINT MICHEL",2, 280))
    liste_stations.append((4135, "SAINT MICHEL",4, 280))
    liste_stations.append((4415, "ODEON",2, 280))
    liste_stations.append((4415, "ODEON", 4, 280))
    liste_stations.append((4695, "ST GERMAIN DES PRES",2, 280))
    liste_stations.append((4695, "ST GERMAIN DES PRES", 4, 280))
    liste_stations.append((4975, "SAINT SULPICE",2, 280))
    liste_stations.append((4975, "SAINT SULPICE", 4, 280))
    liste_stations.append((5255, "SAINT PLACIDE",2, 280))
    liste_stations.append((5255, "SAINT PLACIDE", 4, 280))
    liste_stations.append((5535, "MONTPARNASSE BIENVENUE",2, 280))
    liste_stations.append((5535, "MONTPARNASSE BIENVENUE", 4, 280))
    liste_stations.append((5815, "VAVIN",2, 280))
    liste_stations.append((5815, "VAVIN", 4, 280))
    liste_stations.append((6095, "RASPAIL",2, 280))
    liste_stations.append((6095, "RASPAIL", 4, 280))
    liste_stations.append((6375, "DENFERT ROCHEREAU",2, 280))
    liste_stations.append((6375, "DENFERT ROCHEREAU", 4, 280))
    liste_stations.append((6622, "MOUTON DUVERNET",2, 280))
    liste_stations.append((6622, "MOUTON DUVERNET", 4, 280))
    liste_stations.append((6869, "ALESIA",2, 280))
    liste_stations.append((6869, "ALESIA", 4, 280))
    liste_stations.append((7119, "PORTE D'ORLEANS",2, 280))
    liste_stations.append((7119, "PORTE D'ORLEANS", 4, 280))
    liste_stations.append((7369, "MAIRIE DE MONTROUGE",2, 280))
    liste_stations.append((7369, "MAIRIE DE MONTROUGE", 4, 280))
    liste_stations.append((7619, "BARBARA",2, 280))
    liste_stations.append((7619, "BARBARA", 4, 280))
    liste_stations.append((7869, "BAGNEUX LUCIE AUBRAC",2, 280))
    liste_stations.append((7869, "BAGNEUX LUCIE AUBRAC", 4, 280))

    # X1, Y1, X2, Y2, 0=Eteint - 1=Vers la droite - 2=Vers la gauche, Nom)
    liste_eguillages = []
    liste_eguillages.append((450, 100, 480, 130, 0, "Eg PORTE DE CLIGNANCOURT2"))
    liste_eguillages.append((1260, 100, 1290, 130, 0, "Eg BARBES ROCHECHOUART1"))
    liste_eguillages.append((2870, 100, 2900, 130, 0, "Eg REAUMUR SEBASTOPOL1"))
    liste_eguillages.append((3170, 130, 3200, 160, 0, "Eg ETIENNE MARCEL1"))
    liste_eguillages.append((3560, 130,35<90, 100, 0, "Eg chatelet1"))
    liste_eguillages.append((4260, 100,4290, 130, 0, "Eg ODEON1"))
    liste_eguillages.append((4890, 70,4920, 100, 0, "Eg SAINT SULPICE1"))
    liste_eguillages.append((5750, 100,5780, 130, 0, "Eg VAVIN1"))
    liste_eguillages.append((7200, 130,7230, 100, 0, "Eg PORTE D'ORLEANS1"))
    liste_eguillages.append((7300, 130,7330, 100, 0, "Eg PORTE D'ORLEANS2"))
    liste_eguillages.append((7450, 130,7480, 100, 0, "Eg MAIRIE DE MONTROUGE1"))
    liste_eguillages.append((7820, 100,7850, 70, 2, "Eg BAGNEUX1"))
    liste_eguillages.append((7820, 130,7850, 100, 0, "Eg BAGNEUX2"))



    # X, Y, Nom
    liste_terminus = []
    liste_terminus.append((200, 100, " PORTE DE CLIGNANCOURT1"))
    #liste_terminus.append((5880, 130, " VAVIN1"))
    #liste_terminus.append((7200, 130, " MAIRIE DE MONTROUGE1"))
    liste_terminus.append((8200, 70, "BAGNEUX LUCIE AUBRAC1"))
    liste_terminus.append((8200, 100, "BAGNEUX LUCIE AUBRAC2"))
    liste_terminus.append((8200, 130, "BAGNEUX LUCIE AUBRAC 3"))
    liste_terminus.append((8050, 70, "BAGNEUX LUCIE AUBRAC 4"))
    liste_terminus.append((8050, 100, "BAGNEUX LUCIE AUBRAC 4"))

    liste_metro = []
    #train direction chateau de vincennes
    #depart train garage la defense
    liste_metro.append(("Train 2", 10,  1, 80,1,"#FFCC45" ))
    #depart train esplanade de la defense
    liste_metro.append(("Train 3",430, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 4", 6422, 1, 80, 1,"#FFCC45"))
    liste_metro.append(("Train 5", 6422, 1, 80, 1,"#FFCC45"))
    liste_metro.append(("Train 6",645,  1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 7", 860, 1,80, 1,"#FFCC45" ))
    liste_metro.append(("Train 8",1175, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 9",1455,  1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 10", 1735, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 11",2015, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 12",2295,  1,80, 1,"#FFCC45" ))
    liste_metro.append(("Train 13", 2575, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 14",2855, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 15",3135,  1,80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 16", 3415, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 17",3655, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 18",3935,  1,80, 1,"#FFCC45" ))
    liste_metro.append(("Train 19", 4215, 1,80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 20",4495, 1, 80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 21",4775,  1,80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 22", 5055, 1, 80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 23",5335, 1,80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 24",5615,  1, 80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 25", 5335, -1,50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 26",430, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 27",10,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 28", 6422, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 29",6175, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 30",645,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 31", 860, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 32",1175, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 33",1455,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 34", 1735, -1,50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 35",2015, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 36",2295,  -1, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 37", 2575, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 38",2855, -1, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 39",3135,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 40", 3415, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 41",3655, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 42",3935,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 43", 4215, -1, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 44",4495, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 45",4775,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 46", 5055, -1,50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 47",5335, -1, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 48",5615,  -1,50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 49",6869,  1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 50", 6869, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 51",7119, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 52",7119,  -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 53", 7369, 1, 80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 54",7369, -1, 50 , 1,"#FFCC45" ))
    liste_metro.append(("Train 55",7619,  1, 80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 56", 7619, -1, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 57",8200, -1, 20 , 0,"#FFCC45" ))
    liste_metro.append(("Train 58",8200,  -1, 50 , 0,"#FFCC45" ))
    liste_metro.append(("Train 59", 7869, 1,80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 60",7869, -1, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 61", 9050, 1,80 , 1,"#FFCC45" ))
    liste_metro.append(("Train 62",8200, -1, 80, 0,"#FFCC45" ))

    liste_lignes = []
    liste_lignes.append((345, 100, 7940, 100, "#FCFF42", 2))
    liste_lignes.append((345, 130, 7940, 130, "#FCFF42", 2))
    liste_lignes.append((3200, 160, 3300, 160, "#FCFF42", 2))
    liste_lignes.append((4790, 70, 4890, 70, "#FCFF42", 2))
    liste_lignes.append((7850, 70, 8020, 70, "#FCFF42", 2))

    liste_depot_eguillage = []
    # eguillage depot
    liste_depot_eguillage.append((250, 100, 280, 130, 1, "Eg PORTE DE CLIGNANCOURT1","#CCCCCC"))
    liste_depot_eguillage.append((285, 130, 315, 160, 0, "Eg CLIGNANCOURT","#CCCCCC"))
    liste_depot_eguillage.append((315, 160, 345, 190, 0, "Eg D1","#CCCCCC"))
    liste_depot_eguillage.append((345, 190, 375, 220, 0, "Eg D2","#CCCCCC"))
    liste_depot_eguillage.append((375, 220, 405, 250, 0, "Eg D3","#CCCCCC"))
    liste_depot_eguillage.append((405, 250, 435, 280, 0, "Eg D4","#CCCCCC"))
    liste_depot_eguillage.append((435, 280, 465, 310, 0, "Eg D5","#CCCCCC"))
    liste_depot_eguillage.append((7940, 130,7965, 100, 1, "Eg BAGNEUX3","#CCCCCC"))
    liste_depot_eguillage.append((8020, 100,8050, 70, 1, "Eg BAGNEUX4","#CCCCCC"))
    liste_depot_eguillage.append((8020, 70,8050, 100, 0, "Eg BAGNEUX5","#CCCCCC"))
    liste_depot_eguillage.append((8120, 100,8150, 70, 0, "Eg BAGNEUX6","#CCCCCC"))
    liste_depot_eguillage.append((8120, 130,8150, 100, 0, "Eg BAGNEUX7","#CCCCCC"))


    liste_depot_ligne = []
     #ligne depot
    liste_depot_ligne.append((7940, 70, 8250, 70, "#CCCCCC", 2))
    liste_depot_ligne.append((7940, 100, 8250, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((7940, 130, 9250, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((10, 100, 345, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((10, 130, 345, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((315, 160, 745, 160, "#CCCCCC", 2))
    liste_depot_ligne.append((345, 190, 745, 190, "#CCCCCC", 2))
    liste_depot_ligne.append((375, 220, 745, 220, "#CCCCCC", 2))
    liste_depot_ligne.append((405, 250, 745, 250, "#CCCCCC", 2))
    liste_depot_ligne.append((435, 280, 745, 280, "#CCCCCC", 2))
    liste_depot_ligne.append((465, 310, 745, 310, "#CCCCCC", 2))

    liste_feu_traffic = []
    # feu eguillage terminus porte de cligancourt
    liste_feu_traffic.append((260, 100, 1))
    #feu de départ vers le depot la défense
    liste_feu_traffic.append((330, 100, 1))
    #feu de départ la défense direction CV
    liste_feu_traffic.append((400, 130, 1))
    #feu d'arriver la défense direction D
    liste_feu_traffic.append((400, 100, 1))
    #feu d'arriver la defense direction CV
    liste_feu_traffic.append((330, 130, 1))
    #feu de départ esplanade de la defense direction D
    liste_feu_traffic.append((610, 100, 1))
    #feu de départ esplanade de la defense direction CV
    liste_feu_traffic.append((690, 130, 1))
    #feu de départ pont de neuilly direction D
    liste_feu_traffic.append((825, 100, 1))
    #feu de départ pont de neuilly direction CV
    liste_feu_traffic.append((905, 130, 1))
    #feu de départ les sablons direction D
    liste_feu_traffic.append((1040, 100, 1))
    #feu de départ les sablons direction CV
    liste_feu_traffic.append((1120, 130, 1))
    #feu de départ porte maillot direction D
    liste_feu_traffic.append((1355, 100, 1))
    #feu de départ porte maillot direction CV
    liste_feu_traffic.append((1435, 130, 1))
    #feu de départ argentine direction D
    liste_feu_traffic.append((1635, 100, 1))
    #feu de départ argentine direction CV
    liste_feu_traffic.append((1715, 130, 1))
    #feu de départ etoile direction D
    liste_feu_traffic.append((1915, 100, 1))
    #feu de départ etoile direction CV
    liste_feu_traffic.append((1995, 130, 1))
    #feu de départ george V direction D
    liste_feu_traffic.append((2195, 100, 1))
    #feu de départ george V direction CV
    liste_feu_traffic.append((2275, 130, 1))
    #feu de départ franklin d roosevelt direction D
    liste_feu_traffic.append((2475, 100, 1))
    #feu de départ franklin d roosevelt direction CV
    liste_feu_traffic.append((2555, 130, 1))
    #feu de départ champs elisee clemenceau direction D
    liste_feu_traffic.append((2755, 100, 1))
    #feu de départ champs elisee clemenceau direction CV
    liste_feu_traffic.append((2835, 130, 1))
    #feu de départ concorde direction D
    liste_feu_traffic.append((3035, 100, 1))
    #feu de départ concorde direction CV
    liste_feu_traffic.append((3115, 130, 1))
    #feu de départ tuileries direction D
    liste_feu_traffic.append((3315, 100, 1))
    #feu de départ tuileries direction CV
    liste_feu_traffic.append((3395, 130, 1))
    #feu de départ palais royal musee du louvre direction D
    liste_feu_traffic.append((3595, 100, 1))
    #feu de départ palais royal musee du louvre direction CV
    liste_feu_traffic.append((3675, 130, 1))
    #feu de départ louvre rivoli direction D
    liste_feu_traffic.append((3835, 100, 1))
    #feu de départ louvre rivoli direction CV
    liste_feu_traffic.append((3915, 130, 1))
    #feu de départ chatelet direction D
    liste_feu_traffic.append((4115, 100, 1))
    #feu de départ  chatelet direction CV
    liste_feu_traffic.append((4195, 130, 1))
    #feu de départ hotel de ville direction D
    liste_feu_traffic.append((4395, 100, 1))
    #feu de départ  hotel de ville direction CV
    liste_feu_traffic.append((4475, 130, 1))
    #feu de départ saint paul direction D
    liste_feu_traffic.append((4675, 100, 1))
    #feu de départ  saint paul direction CV
    liste_feu_traffic.append((4755, 130, 1))
    #feu de départ bastille direction D
    liste_feu_traffic.append((4955, 100, 1))
    #feu de départ bastille direction CV
    liste_feu_traffic.append((5035, 130, 1))
    #feu de départ gare de lyon direction D
    liste_feu_traffic.append((5235, 100, 1))
    #feu de départ gare de lyon direction CV
    liste_feu_traffic.append((5315, 130, 1))
    #feu de départ reuilly diderot direction D
    liste_feu_traffic.append((5515, 100, 1))
    #feu de départ reuilly diderot direction CV
    liste_feu_traffic.append((5595, 130, 1))
    #feu de départ nation direction D
    liste_feu_traffic.append((5795, 100, 1))
    #feu de départ nation direction CV
    liste_feu_traffic.append((6875, 130, 1))
    #feu de départ porte de vincennes direction D
    liste_feu_traffic.append((6075, 100, 1))
    #feu de départ porte de vincennes direction CV
    liste_feu_traffic.append((6155, 130, 1))
    #feu de départ saint mande direction D
    liste_feu_traffic.append((6355, 100, 1))
    #feu de départ saint mande direction CV
    liste_feu_traffic.append((6435, 130, 1))
    #feu de départ berault direction D
    liste_feu_traffic.append((6602, 100, 1))
    #feu de départ berault direction CV
    liste_feu_traffic.append((6682, 130, 1))
    #feu de départ chateau de vincennes direction D
    liste_feu_traffic.append((6849, 100, 1))
    #feu de départ chateau de vincennes direction CV
    liste_feu_traffic.append((6929, 130, 1))
    #feu de départ porte d'orléan direction D
    liste_feu_traffic.append((7099, 100, 1))
    #feu de départ porte d'orléan direction CV
    liste_feu_traffic.append((7179, 130, 1))
    #feu de départ montrouge direction D
    liste_feu_traffic.append((7349, 100, 1))
    #feu de départ montrouge direction CV
    liste_feu_traffic.append((7429, 130, 1))
    #feu de départ barbara direction D
    liste_feu_traffic.append((7599, 100, 1))
    #feu de départ barbara direction CV
    liste_feu_traffic.append((7679, 130, 1))
    #feu de départ bagneux lucie au brac direction D
    liste_feu_traffic.append((7849, 100, 1))
    #feu de départ bagneux lucie au brac direction CV
    liste_feu_traffic.append((7929, 130, 1))
    #feu d'arrivé bagneux lucie au brac direction D
    liste_feu_traffic.append((7929, 100, 1))
    #feu d'arrivé bagneux lucie au brac direction CV
    liste_feu_traffic.append((7849, 130, 1))
    #feu d'arrivé bagneux lucie au brac direction CV
    liste_feu_traffic.append((7929, 70, 1))
    #feu de départ bagneux lucie au brac direction CV
    liste_feu_traffic.append((7849, 70, 1))
#feu eguillage terminus bagneux lucie au brac
    liste_feu_traffic.append((8010, 70, 1))
    liste_feu_traffic.append((8010, 100, 1))


