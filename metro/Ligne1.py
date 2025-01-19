class ClasseLigne1():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((250, "LA DEFENSE", 3, 350))
    liste_stations.append((250, "LA DEFENSE", 4, 350))
    liste_stations.append((530, "ESPLANADE DE LA DEFENSE", 3, 380))
    liste_stations.append((530, "ESPLANADE DE LA DEFENSE", 4, 380))
    liste_stations.append((745, "PONT DE NEUILLY", 2, 380))
    liste_stations.append((745, "PONT DE NEUILLY", 5, 280))
    liste_stations.append((960, "LES SABLONS", 2, 400))
    liste_stations.append((960, "LES SABLONS", 5, 400))
    liste_stations.append((1275, "PORTE MAILLOT", 1, 400))
    liste_stations.append((1275, "PORTE MAILLOT", 3, 400))
    liste_stations.append((1275, "PORTE MAILLOT", 4, 400))
    liste_stations.append((1275, "PORTE MAILLOT", 6, 400))
    liste_stations.append((1555, "ARGENTINE", 2, 325))
    liste_stations.append((1555, "ARGENTINE", 5, 325))
    liste_stations.append((1835, "ETOILE", 2, 475))
    liste_stations.append((1835, "ETOILE", 5, 475))
    liste_stations.append((2115, "GEORGE V", 2, 380))
    liste_stations.append((2115, "GEORGE V", 5, 380))
    liste_stations.append((2395, "FRANKLIN D. ROOSEVELT", 2, 400))
    liste_stations.append((2395, "FRANKLIN D. ROOSEVELT", 5, 400))
    liste_stations.append((2675, "CHAMPS ELISEE CLEMENCEAU", 2, 400))
    liste_stations.append((2675, "CHAMPS ELISEE CLEMENCEAU", 5, 400))
    liste_stations.append((2955, "CONCORDE", 2, 500))
    liste_stations.append((2955, "CONCORDE", 5, 500))
    liste_stations.append((3235, "TUILERIES", 2, 355))
    liste_stations.append((3235, "TUILERIES", 5, 355))
    liste_stations.append((3515, "PALAIS ROYAL MUSEE DU LOUVRE",2, 380))
    liste_stations.append((3515, "PALAIS ROYAL MUSEE DU LOUVRE", 5, 380))
    liste_stations.append((3755, "LOUVRE RIVOLI",2, 325))
    liste_stations.append((3755, "LOUVRE RIVOLI", 5, 325))
    liste_stations.append((4035, "CHATELET",2, 475))
    liste_stations.append((4035, "CHATELET",5, 475))
    liste_stations.append((4315, "HOTEL DE VILLE",2, 400))
    liste_stations.append((4315, "HOTEL DE VILLE", 5, 400))
    liste_stations.append((4595, "SAINT PAUL",2, 380))
    liste_stations.append((4595, "SAINT PAUL", 5, 380))
    liste_stations.append((4875, "BASTILLE",2, 475))
    liste_stations.append((4875, "BASTILLE", 5, 475))
    liste_stations.append((5155, "GARE DE LYON",2, 475))
    liste_stations.append((5155, "GARE DE LYON", 5, 475))
    liste_stations.append((5435, "REUILLY DIDEROT",2, 325))
    liste_stations.append((5435, "REUILLY DIDEROT", 5, 325))
    liste_stations.append((5715, "NATION",2, 530))
    liste_stations.append((5715, "NATION", 5, 530))
    liste_stations.append((5995, "PORTE DE VINCENNES",2, 400))
    liste_stations.append((5995, "PORTE DE VINCENNES", 5, 400))
    liste_stations.append((6275, "SAINT MANDE",2, 325))
    liste_stations.append((6275, "SAINT MANDE", 5, 325))
    liste_stations.append((6522, "BERAULT",2, 325))
    liste_stations.append((6522, "BERAULT", 5, 325))
    liste_stations.append((6769, "CHATEAU DE VINCENNES",2, 350))
    liste_stations.append((6769, "CHATEAU DE VINCENNES", 5, 350))

    liste_eguillages = []
    liste_eguillages.append((625, 100, 655, 130, 0, "Eg esplanade de la défense"))
    liste_eguillages.append((1040, 100, 1070, 70,2, "Eg sablons1"))
    liste_eguillages.append((1040, 130, 1070, 160, 1, "Eg sablons4"))
    liste_eguillages.append((1350, 70, 1380, 100, 2, "Eg maillot1"))
    liste_eguillages.append(( 1210, 100, 1240, 70, 0, "Eg maillot2"))
    liste_eguillages.append((1350, 160, 1380, 130, 1, "Eg maillot4"))
    liste_eguillages.append((1930, 100,1960, 130, 0, "Eg étoile1"))
    liste_eguillages.append((3030, 100,3060, 130, 0, "Eg concorde1"))
    liste_eguillages.append((3990, 100,4020, 130, 0, "Eg chatelet1"))
    liste_eguillages.append(( 5110, 100,5140, 70, 0, "Eg gare de lyon1"))
    liste_eguillages.append(( 5240, 70,5270, 100, 0, "Eg gare de lyon2"))
    liste_eguillages.append((5290, 100,5320, 130, 1, "Eg gare de lyon3"))
    liste_eguillages.append((5670, 100,5700, 130, 0, "Eg nation1"))
    liste_eguillages.append(( 5960, 100,5990, 70, 0, "Eg porte de vincennes1"))
    liste_eguillages.append((5950, 100,5980, 130, 0, "Eg porte de vincennes2"))
    liste_eguillages.append((6070, 70, 6100, 100, 0, "Eg porte de vincennes3"))
    liste_eguillages.append(( 5950, 130, 5980, 160, 0, "Eg porte de vincennes4"))
    liste_eguillages.append((6070, 160,6100, 130, 0, "Eg porte de vincennes5"))
    liste_eguillages.append(( 6734, 100,6768, 70, 0, "Eg chateau de vincennes1"))
    liste_eguillages.append((6844, 70, 6878, 100, 0, "Eg chateau de vincennes2"))
    liste_eguillages.append((6724, 100, 6758, 130, 0, "Eg chateau de vincennes3"))
    liste_eguillages.append((6724, 130, 6758, 160, 0, "Eg chateau de vincennes4"))




    liste_terminus = []
    liste_terminus.append((20, 100, "TERMINUS LA DEFENSE 1",0))
    liste_terminus.append((20, 130, "TERMINUS LA DEFENSE 2",0))
    liste_terminus.append((100, 100, "TERMINUS LA DEFENSE 3",1))
    liste_terminus.append((100, 130, "TERMINUS LA DEFENSE 4",1))
    liste_terminus.append((7100, 100, "CHATEAU DE VINCENNES 1",1))
    liste_terminus.append((7100, 130, "CHATEAU DE VINCENNES 2",1))
    liste_terminus.append((6930, 130, "CHATEAU DE VINCENNES 3",1))
    liste_terminus.append(( 8018, 190, "TERMINUS D1",0))
    liste_terminus.append(( 8018, 220, "TERMINUS D2",0))
    liste_terminus.append(( 8018, 250, "TERMINUS D3",0))
    liste_terminus.append(( 8018, 280, "TERMINUS D4",0))
    liste_terminus.append(( 8018, 310, "TERMINUS D5",0))

    liste_metro = []
    #train direction chateau de vincennes
    #depart train garage la defense
    liste_metro.append(("1", 110,0.50, 80,1,"#EB0004" ))
    liste_metro.append(("3",530,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("6",745,  0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("7", 960,0.50,80, 1,"#EB0004" ))
    liste_metro.append(("8",1275, 0.50, 110, 1,"#EB0004" ))
    liste_metro.append(("9",1555, 0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("10", 1835,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("11",2115,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("12",2395,0.50,80, 1,"#EB0004" ))
    liste_metro.append(("13", 2675,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("14",2955,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("15",3235,0.50,80 , 1, "#EB0004" ))
    liste_metro.append(("16", 3515, 0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("17",3755,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("18",4035,  0.50,80, 1,"#EB0004" ))
    liste_metro.append(("19", 4315, 0.50,80 , 1,"#EB0004" ))
    liste_metro.append(("20",4595, 0.50, 80 , 1,"#EB0004" ))
    liste_metro.append(("21",4875, 0.50,80 , 1,"#EB0004" ))
    liste_metro.append(("22", 5155, 0.50, 80 , 1,"#EB0004" ))
    liste_metro.append(("23",5435,0.50,80 , 1,"#EB0004" ))
    liste_metro.append(("24",5715, 0.50, 80 , 1,"#EB0004" ))
    #liste_metro.append(("4", 6522,0.50, 80, 1,"#EB0004" ))
    liste_metro.append(("5",6522,0.50, 80 , 1,"#EB0004" ))
    liste_metro.append(("25", 5435, -0.50,50 , 1,"#EB0004" ))
    liste_metro.append(("26",530, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("27",6769,  -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("28", 7100, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("29",6225, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("30",745,  -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("31", 960, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("32",5995, 0.50, 80 , 1,"#EB0004" ))
    liste_metro.append(("33",1555,  -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("34", 1835, -0.50,50 , 1,"#EB0004" ))
    liste_metro.append(("35",2115, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("36",2395,  -0.50, 50, 1,"#EB0004" ))
    liste_metro.append(("37", 2675, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("38",2955, -0.50, 50, 1,"#EB0004" ))
    liste_metro.append(("39",3235,  -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("40", 3515, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("41",3755, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("42",4035,  -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("43", 4315, -0.50, 50, 1,"#EB0004" ))
    liste_metro.append(("44",4595, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("45",4875,  -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("46", 5155, -0.50,50 , 1,"#EB0004" ))
    liste_metro.append(("47  ",5935, -0.50, 50, 1,"#EB0004" ))
    liste_metro.append(("48",5715,  -0.50,50 , 1,"#EB0004" ))
    liste_metro.append(("49", 6769, -0.50, 50, 1,"#EB0004" ))
    liste_metro.append(("50",1146, -0.50, 50 , 1,"#EB0004" ))
    liste_metro.append(("51",6275,  0.50, 80 , 1,"#EB0004" ))
    liste_metro.append(("52", 5155, -0.50,50 , 1,"#EB0004" ))
    liste_metro.append(("53  ",6435, -0.50, 50, 1,"#EB0004" ))
    liste_metro.append(("54",5715,  -0.50,50 , 1,"#EB0004" ))
    liste_lignes = []
    liste_lignes.append((200, 100, 6908, 100, "#EBEBEB", 2))
    liste_lignes.append((200, 130, 6908, 130, "#EBEBEB", 2))
    liste_lignes.append((1070, 70, 1350, 70, "#EBEBEB", 2))
    liste_lignes.append((1070, 160, 1350, 160, "#EBEBEB", 2))
    liste_lignes.append((1275, 115, 1340, 115, "black", 2))
    liste_lignes.append((5140, 70, 5110, 100, "#EBEBEB",2))
    liste_lignes.append((5140, 70, 5240, 70, "#EBEBEB", 2))
    liste_lignes.append((5990, 70, 6070, 70, "#EBEBEB", 2))
    liste_lignes.append((5980, 160, 6070, 160, "#EBEBEB",2))
    liste_lignes.append((5995, 115, 6060, 115,"black", 2))
    liste_lignes.append((6768, 70, 6848, 70, "#EBEBEB", 2))
    liste_lignes.append((6758, 160, 6908, 160, "#EBEBEB",2))


    liste_depot_eguillage = []
    # eguillage depot
    liste_depot_eguillage.append((160,130,190, 100, 2, "Eg LA DEFENSE 1", "#CCCCCC"))
    liste_depot_eguillage.append((200, 100, 230, 130, 0, "Eg LA DEFENSE 2", "#CCCCCC"))
    liste_depot_eguillage.append(( 1040, 130,1070, 100, 0, "Eg sablons2", "#CCCCCC"))
    liste_depot_eguillage.append((1040, 100, 1070, 130, 0, "Eg sablons3", "#CCCCCC"))
    liste_depot_eguillage.append((1230, 100,1260, 130, 0, "Eg maillot3", "#CCCCCC"))
    liste_depot_eguillage.append((6874, 100, 6908, 130, 2, "Eg chateau de vincennes5", "#CCCCCC"))
    liste_depot_eguillage.append((6974, 100, 7004, 130, 0, "Eg chateau de vincennes6", "#CCCCCC"))
    liste_depot_eguillage.append((7004, 130,7034, 100, 0, "Eg chateau de vincennes7", "#CCCCCC"))
    liste_depot_eguillage.append((7014, 130,7044, 160, 0, "Eg chateau de vincennes8", "#CCCCCC"))
    liste_depot_eguillage.append((6994, 130,6964, 160, 0, "Eg chateau de vincennes9", "#CCCCCC"))
    liste_depot_eguillage.append((6864, 160, 6898, 130, 0, "Eg chateau de vincennes10", "#CCCCCC"))
    liste_depot_eguillage.append((7158, 130, 7188, 160, 0, "Eg D1", "#CCCCCC"))
    liste_depot_eguillage.append((7308, 160, 7338, 190, 0, "Eg D2", "#CCCCCC"))
    liste_depot_eguillage.append((7308, 160, 7338, 130, 0, "Eg D3", "#CCCCCC"))
    liste_depot_eguillage.append((7248, 160, 7278, 190, 0, "Eg D4", "#CCCCCC"))
    liste_depot_eguillage.append((7278, 190, 7308, 220, 0, "Eg D5", "#CCCCCC"))
    liste_depot_eguillage.append((7308, 220, 7338, 250, 0, "Eg D6", "#CCCCCC"))
    liste_depot_eguillage.append((7338, 250, 7368, 280, 0, "Eg D7", "#CCCCCC"))

    liste_depot_ligne = []
     #ligne depot
    liste_depot_ligne.append((6908, 100, 7158, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((6908, 130, 7158, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((6908, 160, 7718, 160, "#CCCCCC", 2))
    liste_depot_ligne.append((10, 100, 230, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((10, 130, 230, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((1040, 100, 1380, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((7338, 130, 7718, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((7338, 190, 7718, 190, "#CCCCCC", 2))
    liste_depot_ligne.append((7308, 220, 7718, 220, "#CCCCCC", 2))
    liste_depot_ligne.append((7338, 250, 7718, 250, "#CCCCCC", 2))
    liste_depot_ligne.append((7368, 280, 7718, 280, "#CCCCCC", 2))
    #liste_depot_ligne.append((7278, 280, 7718, 280, "#CCCCCC", 2))

    liste_feu_traffic = []
    # feu eguillage terminus la defense
    liste_feu_traffic.append(("314",160, 1, 1))
    liste_feu_traffic.append(("314",160, 4, 1))
    #feu de départ vers le depot la défense
    liste_feu_traffic.append(("314",230, 1, 1))
    #feu de départ la défense direction CV
    liste_feu_traffic.append(("314",300, 4, 1))
    #feu d'arriver la défense direction D
    liste_feu_traffic.append(("314",300, 1, 1))
    #feu d'arriver la defense direction CV
    liste_feu_traffic.append(("314",230,4, 1))
    #feu de départ esplanade de la defense direction D
    liste_feu_traffic.append(("314",520, 1, 1))
    #feu de départ esplanade de la defense direction CV
    liste_feu_traffic.append(("314",590, 4, 1))
    #feu de départ pont de neuilly direction D
    liste_feu_traffic.append(("314",725, 1, 1))
    #feu de départ pont de neuilly direction CV
    liste_feu_traffic.append(("314",805, 4, 1))
    #feu de départ les sablons direction D
    liste_feu_traffic.append(("314",940, 1, 1))
    #feu de départ les sablons direction CV
    liste_feu_traffic.append(("314",1020, 4, 1))
    #feu de départ porte maillot direction D
    liste_feu_traffic.append(("314",1255, 1, 1))
    #feu de départ porte maillot direction CV
    liste_feu_traffic.append(("314",1335, 4, 1))
    #feu de départ argentine direction D
    liste_feu_traffic.append(("314",1535, 1, 1))
    #feu de départ argentine direction CV
    liste_feu_traffic.append(("314",1615, 4, 1))
    #feu de départ etoile direction D
    liste_feu_traffic.append(("314",1815, 1, 1))
    #feu de départ etoile direction CV
    liste_feu_traffic.append(("314",1895, 4, 1))
    #feu de départ george V direction D
    liste_feu_traffic.append(("314",2095, 1, 1))
    #feu de départ george V direction CV
    liste_feu_traffic.append(("314",2175, 4, 1))
    #feu de départ franklin d roosevelt direction D
    liste_feu_traffic.append(("314",2375, 1, 1))
    #feu de départ franklin d roosevelt direction CV
    liste_feu_traffic.append(("314",2455, 4, 1))
    #feu de départ champs elisee clemenceau direction D
    liste_feu_traffic.append(("314",2655, 1, 1))
    #feu de départ champs elisee clemenceau direction CV
    liste_feu_traffic.append(("314",2735, 4, 1))
    #feu de départ concorde direction D
    liste_feu_traffic.append(("314",2935, 1, 1))
    #feu de départ concorde direction CV
    liste_feu_traffic.append(("314",3015, 4, 1))
    #feu de départ tuileries direction D
    liste_feu_traffic.append(("314",3215, 1, 1))
    #feu de départ tuileries direction CV
    liste_feu_traffic.append(("314",3295, 4, 1))
    #feu de départ palais royal musee du louvre direction D
    liste_feu_traffic.append(("314",3495, 1, 1))
    #feu de départ palais royal musee du louvre direction CV
    liste_feu_traffic.append(("314",3575, 4, 1))
    #feu de départ louvre rivoli direction D
    liste_feu_traffic.append(("314",3735, 1, 1))
    #feu de départ louvre rivoli direction CV
    liste_feu_traffic.append(("314",3815, 4, 1))
    #feu de départ chatelet direction D
    liste_feu_traffic.append(("314",4015, 1, 1))
    #feu de départ  chatelet direction CV
    liste_feu_traffic.append(("314",4095, 4, 1))
    #feu de départ hotel de ville direction D
    liste_feu_traffic.append(("314",4295, 1, 1))
    #feu de départ  hotel de ville direction CV
    liste_feu_traffic.append(("314",4375, 4, 1))
    #feu de départ saint paul direction D
    liste_feu_traffic.append(("314",4575, 1, 1))
    #feu de départ  saint paul direction CV
    liste_feu_traffic.append(("314",4655, 4, 1))
    #feu de départ bastille direction D
    liste_feu_traffic.append(("314",4855, 1, 1))
    #feu de départ bastille direction CV
    liste_feu_traffic.append(("314",4935, 4, 1))
    #feu de départ gare de lyon direction D
    liste_feu_traffic.append(("314",5135, 1, 1))
    #feu de départ gare de lyon direction CV
    liste_feu_traffic.append(("314",5215, 4, 1))
    #feu de départ reuilly diderot direction D
    liste_feu_traffic.append(("314",5415, 1, 1))
    #feu de départ reuilly diderot direction CV
    liste_feu_traffic.append(("314",5495, 4, 1))
    #feu de départ nation direction D
    liste_feu_traffic.append(("314",5695, 1, 1))
    #feu de départ nation direction CV
    liste_feu_traffic.append(("314",5775, 4, 1))
    #feu de départ porte de vincennes direction D
    liste_feu_traffic.append(("314",5975, 1, 1))
    #feu de départ porte de vincennes direction CV
    liste_feu_traffic.append(("314",6055, 4, 1))
    #feu de départ saint mande direction D
    liste_feu_traffic.append(("314",6255, 1, 1))
    #feu de départ saint mande direction CV
    liste_feu_traffic.append(("314",6335, 4, 1))
    #feu de départ berault direction D
    liste_feu_traffic.append(("314",6502, 1, 1))
    #feu de départ berault direction CV
    liste_feu_traffic.append(("314",6582, 4, 1))
    #feu de départ chateau de vincennes direction D
    liste_feu_traffic.append(("314",6749, 1, 1))
    liste_feu_traffic.append(("314",6749, 2, 1))
    #feu de départ chateau de vincennes direction CV
    liste_feu_traffic.append(("314",6849, 4, 1))
    liste_feu_traffic.append(("314",6849, 3, 1))
    #feu de arrivé chateau de vincennes direction D
    liste_feu_traffic.append(("314",6849, 1, 1))
    liste_feu_traffic.append(("314",6849, 2, 1))
    #feu de arrivé chateau de vincennes direction CV
    liste_feu_traffic.append(("314",6749, 4, 1))
    liste_feu_traffic.append(("314",6749, 3, 1))
    #feu de depot chateau de vincennns
    liste_feu_traffic.append(("314",6910, 4, 1))
