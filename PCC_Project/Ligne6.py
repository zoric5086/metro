class ClasseLigne6():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((150, "CHARLES DE GHAULES ETOILE", 3))
    liste_stations.append((430, "KLEBER", 2))
    liste_stations.append((430, "KLEBER", 4))
    liste_stations.append((645, "BOISSIERE", 2))
    liste_stations.append((645, "BOISSIERE", 4))
    liste_stations.append((860, "TROCADERO", 2))
    liste_stations.append((860, "TROCADERO", 4))
    liste_stations.append((1175, "PASSY", 2))
    liste_stations.append((1175, "PASSY", 4))
    liste_stations.append((1455, "BIR-HAKEIM", 2))
    liste_stations.append((1455, "BIR-HAKEIM", 4))
    liste_stations.append((1735, "DUPLEIX", 2))
    liste_stations.append((1735, "DUPLEIX", 4))
    liste_stations.append((2015, "LA MOTTE PIQUET GRENELLE", 2))
    liste_stations.append((2015, "LA MOTTE PIQUET GRENELLE", 4))
    liste_stations.append((2295, "CAMBRONNE", 2))
    liste_stations.append((2295, "CAMBRONNE", 4))
    liste_stations.append((2575, "SEVRES-LECOUBRE", 2))
    liste_stations.append((2575, "SEVRES-LECOUBRE", 4))
    liste_stations.append((2855, "PASTEUR", 2))
    liste_stations.append((2855, "PASTEUR", 4))
    liste_stations.append((3135, "MONTPARNASSE BIENVENUE", 2))
    liste_stations.append((3135, "MONTPARNASSE BIENVENUE", 4))
    liste_stations.append((3415, "EDGAR QUINET",2))
    liste_stations.append((3415, "EDGAR QUINET", 4))
    liste_stations.append((3655, "RASPAIL",2))
    liste_stations.append((3655, "RASPAIL", 4))
    liste_stations.append((3935, "DENFERT ROCHEREAU",2))
    liste_stations.append((3935, "DENFERT ROCHEREAU",4))
    liste_stations.append((4215, "SAINT-JACQUES",2))
    liste_stations.append((4215, "SAINT-JACQUES", 4))
    liste_stations.append((4495, "GLACIERE",2))
    liste_stations.append((4495, "GLACIERE", 4))
    liste_stations.append((4775, "CORVISART",2))
    liste_stations.append((4775, "CORVISART", 4))
    liste_stations.append((5055, "PLACE D'ITALIE",2))
    liste_stations.append((5055, "PLACE D'ITALIE", 4))
    liste_stations.append((5335, "NATIONALE",2))
    liste_stations.append((5335, "NATIONALE", 4))
    liste_stations.append((5615, "CHEVALERET",2))
    liste_stations.append((5615, "CHEVALERET", 4))
    liste_stations.append((5895, "QUAI DE LA GARE",2))
    liste_stations.append((5895, "QUAI DE LA GARE", 4))
    liste_stations.append((6175, "BERCY",2))
    liste_stations.append((6175, "BERCY", 4))
    liste_stations.append((6422, "DUGOMMIER",2))
    liste_stations.append((6422, "DUGOMMIER", 4))
    liste_stations.append((6810, "BEL-AIR",2))
    liste_stations.append((6810, "BEL-AIR", 4))
    liste_stations.append((7060, "PICPUS",2))
    liste_stations.append((7060, "PICPUS", 4))
    liste_stations.append((7310, "NATION",3))


    liste_eguillages = []
    liste_eguillages.append((230, 100, 260, 130, 1, "Eg CHARLES DE GAULES ETOILE 1"))
    liste_eguillages.append((525, 100, 555, 130, 0, "Eg esplanade de la défense"))
    liste_eguillages.append((1830, 100,1860, 130, 0, "Eg étoile1"))
    liste_eguillages.append((2930, 100,2960, 130, 0, "Eg concorde1"))
    liste_eguillages.append((3890, 100,3920, 130, 0, "Eg chatelet1"))
    liste_eguillages.append(( 5010, 100,5040, 70, 0, "Eg gare de lyon1"))
    liste_eguillages.append(( 5140, 70,5170, 100, 0, "Eg gare de lyon2"))
    liste_eguillages.append((5190, 100,5220, 130, 0, "Eg gare de lyon3"))
    liste_eguillages.append((5570, 100,5600, 130, 0, "Eg nation1"))
    liste_eguillages.append(( 5860, 100,5890, 70, 0, "Eg porte de vincennes1"))
    liste_eguillages.append((5850, 100,5880, 130, 0, "Eg porte de vincennes2"))
    liste_eguillages.append((5970, 70, 6000, 100, 0, "Eg porte de vincennes3"))
    liste_eguillages.append(( 5850, 130, 5880, 160, 0, "Eg porte de vincennes4"))
    liste_eguillages.append((5970, 160,6000, 130, 0, "Eg porte de vincennes5"))
    liste_eguillages.append(( 6634, 100,6668, 70, 0, "Eg chateau de vincennes1"))
    liste_eguillages.append((6744, 70, 6778, 100, 0, "Eg chateau de vincennes2"))
    liste_eguillages.append((6624, 100, 6658, 130, 0, "Eg chateau de vincennes3"))
    liste_eguillages.append((6624, 130, 6658, 160, 0, "Eg chateau de vincennes4"))
    liste_eguillages.append((6774, 100, 6808, 130, 0, "Eg chateau de vincennes5"))
    liste_eguillages.append((6874, 100, 6908, 130, 0, "Eg chateau de vincennes6"))
    liste_eguillages.append((6904, 130,6938, 100, 1, "Eg chateau de vincennes7"))
    liste_eguillages.append((6914, 130,6948, 160, 0, "Eg chateau de vincennes8"))
    liste_eguillages.append((6894, 130,6864, 160, 0, "Eg chateau de vincennes9"))
    liste_eguillages.append((7058, 160, 7088, 190, 0, "Eg D1"))
    liste_eguillages.append((7088, 190, 7118, 220, 0, "Eg D2"))
    liste_eguillages.append((7118, 220, 7148, 250, 0, "Eg D3"))
    liste_eguillages.append((7148, 250, 7178, 280, 0, "Eg D4"))
    liste_eguillages.append((7178, 280, 7208, 310, 0, "Eg D5"))

    liste_terminus = []
    liste_terminus.append((10, 100, "CHARLES DE GAULES ETOILE1"))
    liste_terminus.append((150, 100, "CHARLES DE GAULES ETOILE2"))
    liste_terminus.append((7000, 100, "CHATEAU DE VINCENNES 1"))
    liste_terminus.append((7000, 130, "CHATEAU DE VINCENNES 2"))
    liste_terminus.append(( 7918, 190, "TERMINUS D1"))
    liste_terminus.append(( 7918, 220, "TERMINUS D2"))
    liste_terminus.append(( 7918, 250, "TERMINUS D3"))
    liste_terminus.append(( 7918, 280, "TERMINUS D4"))
    liste_terminus.append(( 7918, 310, "TERMINUS D5"))

    liste_metro = []
    #train direction chateau de vincennes
    #depart train garage la defense
    liste_metro.append(("Train 1", 10, 1, 50,1,"#FFCC45" ))
    #liste_metro.append(("Train 3",430, 1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 6",645,  1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 7", 860,1,80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 8",1175, 1, 110, 1,"#FFCC45" ))
    #liste_metro.append(("Train 9",1455, 1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 10", 1735, 1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 11",2015, 1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 12",2295,  1,80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 13", 2575,1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 14",2855, 1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 15",3135, 1,80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 16", 3415, 1, 80, 1,#FFCC45" ))
    #liste_metro.append(("Train 17",3655,1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 18",3935,  1,80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 19", 4215, 1,80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 20",4495, 1, 80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 21",4775,  1,80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 22", 5055, 1, 80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 23",5335, 1,80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 24",5615, 1, 80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 4", 6422,1, 80, 1,"#FFCC45" ))
    #liste_metro.append(("Train 5",6422, 1, 80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 25", 5335, -1,50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 26",430, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 27",10,  -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 28", 6422, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 29",6175, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 30",645,  -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 31", 860, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 32",1175, -1, 20 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 33",1455,  -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 34", 1735, -1,50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 35",2015, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 36",2295,  -1, 50, 1,"#FFCC45" ))
    #liste_metro.append(("Train 37", 2575, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 38",2855, -1, 50, 1,"#FFCC45" ))
    #liste_metro.append(("Train 39",3135,  -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 40", 3415, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 41",3655, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 42",3935,  -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 43", 4215, -1, 50, 1,"#FFCC45" ))
    #liste_metro.append(("Train 44",4495, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 45",4775,  -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 46", 5055, -1,50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 47  ",5335, -1, 50, 1,"#FFCC45" ))
    #liste_metro.append(("Train 48",5615,  -1,50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 49", 7918, -1, 200, 1,"#FFCC45" ))
    #liste_metro.append(("Train 50",1046, -1, 50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 51",1046,  -1, 80 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 52", 5055, -1,50 , 1,"#FFCC45" ))
    #liste_metro.append(("Train 53  ",5335, -1, 50, 1,"#FFCC45" ))
    #liste_metro.append(("Train 54",5615,  -1,50 , 1,"#FFCC45" ))
    liste_lignes = []
    liste_lignes.append((10, 100, 7058, 100, "#FCFF42", 2))
    liste_lignes.append((260, 130, 7058, 130, "#FCFF42", 2))
    liste_lignes.append((420, 70, 500, 70, "#FCFF42", 2))
    liste_lignes.append((420, 160, 600, 160, "#FCFF42", 2))
    liste_lignes.append((1175, 115, 1240, 115, "black", 2))
    liste_lignes.append((5040, 70, 5010, 100, "#FCFF42",2))
    liste_lignes.append((5040, 70, 5140, 70, "#FCFF42", 2))
    liste_lignes.append((5890, 70, 5970, 70, "#FCFF42", 2))
    liste_lignes.append((5880, 160, 5970, 160, "#FCFF42",2))
    liste_lignes.append((5895, 115, 5960, 115,"black", 2))
    liste_lignes.append((6668, 70, 6748, 70, "#FCFF42", 2))
    liste_lignes.append((6658, 160, 7058, 160, "#FCFF42",2))
    liste_lignes.append((7088, 190, 7918, 190, "#FCFF42", 2))
    liste_lignes.append((7118, 220, 7918, 220, "#FCFF42", 2))
    liste_lignes.append((7148, 250, 7918, 250, "#FCFF42", 2))
    liste_lignes.append((7178, 280, 7918, 280, "#FCFF42", 2))
    liste_lignes.append((7208, 310, 7918, 310, "#FCFF42", 2))

    liste_depot_eguillage = []
    # eguillage depot
    liste_depot_eguillage.append((7058, 160, 7088, 190, 0, "Eg D1","#CCCCCC"))
    liste_depot_eguillage.append((7088, 190, 7118, 220, 0, "Eg D2","#CCCCCC"))
    liste_depot_eguillage.append((7118, 220, 7148, 250, 0, "Eg D3","#CCCCCC"))
    liste_depot_eguillage.append((7148, 250, 7178, 280, 0, "Eg D4","#CCCCCC"))
    liste_depot_eguillage.append((7178, 280, 7208, 310, 0, "Eg D5","#CCCCCC"))


    liste_depot_ligne = []
     #ligne depot
    liste_depot_ligne.append((7088, 190, 7918, 190, "#CCCCCC", 2))
    liste_depot_ligne.append((7118, 220, 7918, 220, "#CCCCCC", 2))
    liste_depot_ligne.append((7148, 250, 7918, 250, "#CCCCCC", 2))
    liste_depot_ligne.append((7178, 280, 7918, 280, "#CCCCCC", 2))
    liste_depot_ligne.append((7208, 310, 7918, 310, "#CCCCCC", 2))


    liste_feu_traffic = []
    # feu eguillage terminus porte de cligancourt
    liste_feu_traffic.append((260, 50, 2))