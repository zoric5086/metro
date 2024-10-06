class ClasseLigne14():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((250, "SAINT DENIS PLEYEL", 2, 350))
    liste_stations.append((250, "SAINT DENIS PLEYEL", 4, 350))
    liste_stations.append((650, "MAIRIE DE ST OUEN", 2, 280))
    liste_stations.append((650, "MAIRIE DE ST OUEN", 4, 280))
    liste_stations.append((1145, "SAINT OUEN", 2, 240))
    liste_stations.append((1145, "SAINT OUEN", 4, 240))
    liste_stations.append((1675, "PORTE DE CLICHY", 2, 225))
    liste_stations.append((1675, "PORTE DE CLICHY", 4, 225))
    liste_stations.append((2235, "PONT CARDINET", 2, 225))
    liste_stations.append((2235, "PONT CARDINET", 4, 225))
    liste_stations.append((2675, "SAINT LAZARE", 2, 330))
    liste_stations.append((2675, "SAINT LAZARE", 4, 330))
    liste_stations.append((3135, "MADELEINE", 2, 330))
    liste_stations.append((3135, "MADELEINE", 4, 330))
    liste_stations.append((3655, "PYRAMIDES",2, 300))
    liste_stations.append((3655, "PYRAMIDES", 4, 300))
    liste_stations.append((4215, "CHATELET",2, 350))
    liste_stations.append((4215, "CHATELET", 4, 350))
    liste_stations.append((4875, "GARE DE LYON",3, 350))
    liste_stations.append((5335, "BERCY",2, 280))
    liste_stations.append((5335, "BERCY", 4, 280))
    liste_stations.append((5895, "COUR ST EMILLION",2, 225))
    liste_stations.append((5895, "COUR ST EMILLION", 4, 225))
    liste_stations.append((6472, "BIBLIOTHEQUE FRANCOIS MITTERRAND",2, 300))
    liste_stations.append((6472, "BIBLIOTHEQUE FRANCOIS MITTERRAND", 4, 300))
    liste_stations.append((6869, "OLYMPIADES",2, 280))
    liste_stations.append((6869, "OLYMPIADES", 4, 280))
    liste_stations.append((7269, "MAISON BLANCHE",2, 280))
    liste_stations.append((7269, "MAISON BLANCHE", 4, 280))
    liste_stations.append((7669, "HOPITAL BICETRE",2, 280))
    liste_stations.append((7669, "HOPITAL BICETRE", 4, 280))
    liste_stations.append((8069, "VILLEJUIF GUSTAVE ROUSSY",2, 280))
    liste_stations.append((8069, "VILLEJUIF GUSTAVE ROUSSY",4,280))
    liste_stations.append((8469, "L'HAI LES ROSES",2, 280))
    liste_stations.append((8469, "L'HAI LES ROSES", 4, 280))
    liste_stations.append((8869, "CHEVILLY LARUE",2, 280))
    liste_stations.append((8869, "CHEVILLY LARUE", 4, 280))
    liste_stations.append((9269, "THIAIS ORLY",2, 280))
    liste_stations.append((9269, "THIAIS ORLY", 4, 280))
    liste_stations.append((9669, "AEROPORT D'ORLY",2, 350))
    liste_stations.append((9669, "AEROPORT D'ORLY", 4, 350))
    liste_eguillages = []
    liste_eguillages.append((160,130,190, 100, 2, "Eg SAINT DENIS PLEYEL1"))
    liste_eguillages.append((160, 100, 190, 130, 0, "Eg SAINT DENIS PLEYEL2"))
    liste_eguillages.append((560,130,590, 100, 0, "Eg MAIRIE DE SAINT OUEN1"))
    liste_eguillages.append((560, 100, 590, 130, 0, "Eg MAIRIE DE SAINT OUEN2"))
    liste_eguillages.append((845, 100, 875, 130, 0, "Eg SAINT OUEN"))
    liste_eguillages.append(( 1560, 130,1590, 100, 0, "Eg PORTE DE CLICHY1"))
    liste_eguillages.append((1560, 100, 1590, 130, 0, "Eg PORTE DE CLICHY2"))
    liste_eguillages.append((2430, 100, 2460, 130, 0, "Eg SAINT LAZARE1"))
    liste_eguillages.append((3060, 100,3090, 130, 0, "Eg MADELEINE1"))
    liste_eguillages.append((3060, 130,3090, 100, 0, "Eg MADELEINE2"))
    liste_eguillages.append((4295, 130,4325, 100, 0, "Eg chatelet1"))
    liste_eguillages.append((4990, 100,5020, 130, 0, "Eg gare de lyon1"))
    liste_eguillages.append(( 6560, 130,6590, 100, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND1"))
    liste_eguillages.append((6560, 100, 6590, 130, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND2"))
    liste_eguillages.append(( 6810, 130,6840, 100, 0, "Eg OLYMPIADES1"))
    liste_eguillages.append((6810, 100, 6840, 130, 0, "Eg OLYMPIADES2"))
    liste_eguillages.append(( 6960, 130,6990, 100, 0, "Eg OLYMPIADES3"))
    liste_eguillages.append((6960, 100, 6990, 130, 0, "Eg OLYMPIADES4"))
    liste_eguillages.append(( 7360, 100,7390, 130, 0, "Eg MAISON BLANCHE1"))
    liste_eguillages.append(( 8160, 100,8190, 130, 0, "Eg VILLEJUIF GUSTAVE ROUSSY1"))
    liste_eguillages.append(( 9360, 100,9390, 130, 0, "Eg THAIS ORLY1"))
    liste_eguillages.append(( 9770, 130,9800, 100, 1, "Eg AEROPORT D'ORLY1"))
    liste_eguillages.append((9770, 100, 9800, 130, 0, "Eg AEROPORT D'ORLY2"))
    liste_terminus = []
    liste_terminus.append((130, 100, "SAINT DENIS PLEYEL1"))
    liste_terminus.append((130, 130, "SAINT DENIS PLEYEL2"))
    #liste_terminus.append((470, 100, "MAIRIE DE SAINT OUEN1"))
    #liste_terminus.append((470, 130, "MAIRIE DE SAINT OUEN2"))
    #liste_terminus.append((1045, 190, "D1"))
    #liste_terminus.append((1045, 220, "D2"))
    #liste_terminus.append((1045, 250, "D3"))
    #liste_terminus.append((1045, 280, "D4"))
    #liste_terminus.append((1045, 310, "D5"))
    #liste_terminus.append((2380, 100, "SAINT LAZARE"))
    #liste_terminus.append((4375, 100, "CHATELET"))
    #liste_terminus.append((5100, 130, "GARE DE LYON"))
    #liste_terminus.append((7060, 100, "OLYMPIADES1"))
    #liste_terminus.append((7060, 130, "OLYMPIADES2"))
    #liste_terminus.append((7120, 100, "OLYMPIADES3"))
    #liste_terminus.append((7120, 130, "OLYMPIADES4"))
    #liste_terminus.append((7200, 100, "OLYMPIADES5"))
    #liste_terminus.append((7200, 130, "OLYMPIADES6"))
    liste_terminus.append((9820, 100, "AEROPORT D'ORLY1"))
    liste_terminus.append((9820, 130, "AEROPORT D'ORLY2"))

    liste_metro = []
    #train direction chateau de vincennes
    #liste_metro.append(("Train 1", 100,  1, 80,1,"#FFCC45" ))
    #liste_metro.append(("Train 2",430, 1, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 3",845,  0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 4",1375, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 5",1890,  0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 6",2315, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 7",2895, 0.45,80, 1,"#EB0004" ))
    liste_metro.append(("Train 8",3355,0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 9",3835,  0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 10",4355, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 11",4835,  0.45,80, 1,"#EB0004" ))
    liste_metro.append(("Train 12",5395,0.45, 80 , 1,"#EB0004" ))
    liste_metro.append(("Train 13",5875,  0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 14",6335,0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 15",6815,  0.45, 80 , 1,"#EB0004" ))
    liste_metro.append(("Train 16",250, 0.45, 80 , 1,"#EB0004" ))
    liste_metro.append(("Train 17", 5635, -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 18",250,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 19", 6422, -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 20",645,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 21", 1160, -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 22",1655,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 23", 2135, -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 24",2695,  -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 25", 3175, -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 26",3635,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 27", 4115, -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 28",4635,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 29", 5115, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 30",6175,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 31", 6655, -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 32  ",7035, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 33",8069,  -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 34", 8069, 0.45, 80, 1,"#EB0004" ))
    #liste_metro.append(("Train 35",7269,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 36", 7269, 0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 37  ",7669, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 38",7669,  0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 39", 8469, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 40",8469,  0.45, 80 , 1,"#EB0004" ))
    liste_metro.append(("Train 41", 6655, -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 42  ",7035, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 43",8069,  -0.45,50 , 1,"#EB0004" ))
    #liste_metro.append(("Train 44", 8069, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 45",8869,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 46", 8869, 0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 47  ",9269, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 48",9269,  0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 49  ",9669, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 50",9669,  0.45,80 , 1,"#EB0004" ))
    #liste_metro.append(("Train 51",7069,  0.45,50 , 1,"#EB0004" ))
    #liste_metro.append(("Train 52",7069,  0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 53", 7469, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 54",7469,  0.45, 80 , 1,"#EB0004" ))
    liste_metro.append(("Train 55", 7869, -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 56  ",7869, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 57",8269,  -0.45,50 , 1,"#EB0004" ))
    liste_metro.append(("Train 58", 8269, 0.45, 80, 1,"#EB0004" ))
    liste_metro.append(("Train 58",8669,  -0.45, 50 , 1,"#EB0004" ))
    liste_metro.append(("Train 60", 8669, 0.45,80 , 1,"#EB0004" ))
    liste_metro.append(("Train 61  ",9069, -0.45, 50, 1,"#EB0004" ))
    liste_metro.append(("Train 62",9069,  0.45, 80, 1,"#EB0004" ))


    liste_lignes = []
    liste_lignes.append((10, 100, 350, 100, "#EBEBEB", 2))
    liste_lignes.append((10, 130, 350, 130, "#EBEBEB", 2))
    liste_lignes.append((560, 100, 6990, 100, "#EBEBEB", 2))
    liste_lignes.append((560, 130, 6990, 130, "#EBEBEB", 2))
    liste_lignes.append((7200, 100, 10000, 100, "#EBEBEB", 2))
    liste_lignes.append((7200, 130, 10000, 130, "#EBEBEB", 2))


    liste_depot_eguillage = []
    # eguillage depot
    liste_depot_eguillage.append((885, 130, 915, 160, 0, "Eg SAINT OUEN1","#CCCCCC"))
    liste_depot_eguillage.append((915, 160, 945, 190, 0, "Eg D1","#CCCCCC"))
    liste_depot_eguillage.append((945, 190, 975, 220, 0, "Eg D2","#CCCCCC"))
    liste_depot_eguillage.append((1065, 190, 1095, 220, 0, "Eg D3","#CCCCCC"))
    liste_depot_eguillage.append((1065, 220, 1095, 190, 0, "Eg D4","#CCCCCC"))
    liste_depot_eguillage.append((1095, 190, 1125, 160, 0, "Eg D5","#CCCCCC"))
    liste_depot_eguillage.append((1095, 220, 1125, 250, 0, "Eg D6","#CCCCCC"))
    liste_depot_eguillage.append((1125, 250, 1155, 280, 0, "Eg D7","#CCCCCC"))
    liste_depot_eguillage.append((1155, 280, 1185, 310, 0, "Eg D7","#CCCCCC"))
    liste_eguillages.append((7060, 130, 7090, 160, 0, "Eg OLYMPIADES","#CCCCCC"))



    liste_depot_ligne = []
     #ligne depot
    liste_depot_ligne.append((6990, 100, 7260, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((6990, 130, 7260, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((350, 100, 560, 100, "#CCCCCC", 2))
    liste_depot_ligne.append((350, 130, 560, 130, "#CCCCCC", 2))
    liste_depot_ligne.append((1125, 160, 1395, 160, "#CCCCCC", 2))
    liste_depot_ligne.append((945, 190, 1395, 190, "#CCCCCC", 2))
    liste_depot_ligne.append((975, 220, 1395, 220, "#CCCCCC", 2))
    liste_depot_ligne.append((1125, 250, 1395, 250, "#CCCCCC", 2))
    liste_depot_ligne.append((1155, 280, 1395, 280, "#CCCCCC", 2))
    liste_depot_ligne.append((1185, 310, 1395, 310, "#CCCCCC", 2))
    liste_depot_ligne.append((7090, 160, 7150, 160, "#CCCCCC", 2))

    liste_feu_traffic = []
    # feu eguillage terminus saint denis pleyel
    liste_feu_traffic.append((200, 100, 1))
    liste_feu_traffic.append((200, 130, 1))
    liste_feu_traffic.append((150, 100, 1))
    liste_feu_traffic.append((150, 130, 1))
    # feu terminus saint denis pleyel direction saint denis pleyel
    liste_feu_traffic.append((250, 100, 1))
    liste_feu_traffic.append((320, 100, 1))
    # feu terminus saint denis pleyel direction aéroport d'orly
    liste_feu_traffic.append((250, 130, 1))
    liste_feu_traffic.append((320, 130, 1))
    # feu eguillage terminus la mairie de saint ouen
    liste_feu_traffic.append((560, 100, 1))
    liste_feu_traffic.append((560, 130, 1))
    #feu d'arriver mairie de saint ouen direction mso
    liste_feu_traffic.append((720, 100, 1))
    #feu d'arriver mairie de saint ouen direction o
    liste_feu_traffic.append((640, 130, 1))
    #feu départ mairie de saint ouen direction mso
    liste_feu_traffic.append((640, 100, 1))
    #feu départ mairie de saint ouen direction o
    liste_feu_traffic.append((730, 130, 1))
    #feu départ saint ouen direction mso
    liste_feu_traffic.append((1145, 100, 1))
    #feu départ saint ouen direction o
    liste_feu_traffic.append((1205, 130, 1))
    #feu départ porte de clichy direction mso
    liste_feu_traffic.append((1675, 100, 1))
    #feu départ porte de clichy direction o
    liste_feu_traffic.append((1735, 130, 1))
    #feu départ pont cardinet direction mso
    liste_feu_traffic.append((2235, 100, 1))
    #feu départ pont cardinet direction o
    liste_feu_traffic.append((2295, 130, 1))
    #feu départ saint lazare direction mso
    liste_feu_traffic.append((2675, 100, 1))
    #feu départ saint lazare direction o
    liste_feu_traffic.append((2735, 130, 1))
    #feu départ madeleine direction mso
    liste_feu_traffic.append((3135, 100, 1))
    #feu départ madeleine direction o
    liste_feu_traffic.append((3195, 130, 1))
    #feu départ pyramide direction mso
    liste_feu_traffic.append((3655, 100, 1))
    #feu départ pyramide direction o
    liste_feu_traffic.append((3715, 130, 1))
    #feu départ chatelet direction mso
    liste_feu_traffic.append((4215, 100, 1))
    #feu départ chatelet direction o
    liste_feu_traffic.append((4275, 130, 1))
    #feu départ gare de lyon direction mso
    liste_feu_traffic.append((4875, 100, 1))
    #feu départ gare de lyon direction o
    liste_feu_traffic.append((4935, 130, 1))
    #feu départ bercy direction mso
    liste_feu_traffic.append((5335, 100, 1))
    #feu départ bercy direction o
    liste_feu_traffic.append((5395, 130, 1))
    #feu départ cour st emillion directio1 mso
    liste_feu_traffic.append((5895, 100, 1))
    #feu départ cour st emillion direction o
    liste_feu_traffic.append((5955, 130, 1))
    #feu départ bibliotheque francois mitterand direction mso
    liste_feu_traffic.append((6472, 100, 1))
    #feu départ bibliotheque francois mitterand direction o
    liste_feu_traffic.append((6532, 130, 1))
    #feu départ olympiade direction mso
    liste_feu_traffic.append((6869, 100, 1))
    #feu départ olympiade direction o
    liste_feu_traffic.append((6929, 130, 1))
    #feu arrivé olympiade direction mso
    liste_feu_traffic.append((6929, 100, 1))
    #feu arrivé olympiade direction o
    liste_feu_traffic.append((6869, 130, 1))
    #feu eguillage olympiade
    liste_feu_traffic.append((7000, 100, 1))
    liste_feu_traffic.append((7000, 130, 1))
    #feu eguillage maison blanche
    liste_feu_traffic.append((7269, 100, 1))
    liste_feu_traffic.append((7330, 130, 1))
    #feu eguillage hopital bicetre
    liste_feu_traffic.append((7669, 100, 1))
    liste_feu_traffic.append((7730, 130, 1))
    #feu eguillage villejuif gustave roussy
    liste_feu_traffic.append((8069, 100, 1))
    liste_feu_traffic.append((8130, 130, 1))
    #feu eguillage l'hai les roses
    liste_feu_traffic.append((8469, 100, 1))
    liste_feu_traffic.append((8530, 130, 1))
    #feu eguillage chevilly la rue
    liste_feu_traffic.append((8869, 100, 1))
    liste_feu_traffic.append((8930, 130, 1))
    #feu eguillage thiais orly
    liste_feu_traffic.append((9269, 100, 1))
    liste_feu_traffic.append((9330, 130, 1))
    #feu eguillage aéroport d'orly direction aéroport d'orly
    liste_feu_traffic.append((9669, 130, 1))
    liste_feu_traffic.append((9730, 130, 1))
    #feu eguillage aéroport d'orly direction saint denis pleyel
    liste_feu_traffic.append((9669, 100, 1))
    liste_feu_traffic.append((9730, 100, 1))
    #feu eguillage terminus aéroport d'orly
    liste_feu_traffic.append((9830, 100, 1))
    liste_feu_traffic.append((9760, 100, 1))
    liste_feu_traffic.append((9830, 130, 1))
    liste_feu_traffic.append((9760, 130, 1))
    #feu depot
    liste_feu_traffic.append((985, 190, 1))
    liste_feu_traffic.append((985, 220, 1))
    liste_feu_traffic.append((1100, 190, 1))
    liste_feu_traffic.append((1100, 220, 1))


