class ClasseLigne14():
    #Position Station(x, nom, ligne de haut en bas,Haut/Bas,Temps)
    liste_stations = []
    liste_stations.append((350, "SAINT DENIS PLEYEL Q1", 1, "H", 350))
    liste_stations.append((350, "SAINT DENIS PLEYEL Q2", 2, "B", 410))
    liste_stations.append((650, "MAIRIE DE SAINT-OUEN Q1", 1, "H", 280))
    liste_stations.append((650, "MAIRIE DE SAINT-OUEN Q2", 2, "B", 280))
    liste_stations.append((1025, "CLICHY SAINT-OUEN Q1", 1, "H", 240))
    liste_stations.append((1025, "CLICHY SAINT-OUEN Q2", 2, "B", 240))
    liste_stations.append((1445, "PORTE DE CLICHY Q1", 1, "H", 225))
    liste_stations.append((1445, "PORTE DE CLICHY Q2", 2, "B", 225))
    liste_stations.append((1695, "PONT CARDINET Q1", 1, "H", 225))
    liste_stations.append((1695, "PONT CARDINET Q2", 2, "B", 225))
    liste_stations.append((2125, "SAINT LAZARE Q1", 1, "H", 330))
    liste_stations.append((2125, "SAINT LAZARE Q2", 2, "B", 330))
    liste_stations.append((2395, "MADELEINE Q1", 1, "H", 330))
    liste_stations.append((2395, "MADELEINE Q2", 2, "B", 330))
    liste_stations.append((3325, "PYRAMIDES Q1", 1, "H", 300))
    liste_stations.append((3325, "PYRAMIDES Q2", 2, "B", 300))
    liste_stations.append((3885, "CHATELET Q1", 1, "H", 350))
    liste_stations.append((3885, "CHATELET Q2", 2, "B", 350))
    liste_stations.append((4545, "GARE DE LYON Q1", 1.5, "", 350))
    liste_stations.append((5005, "BERCY Q1", 1, "H", 280))
    liste_stations.append((5005, "BERCY Q2", 2, "B", 280))
    liste_stations.append((5565, "COUR ST EMILLION Q1", 1, "H", 225))
    liste_stations.append((5565, "COUR ST EMILLION Q2", 2, "B", 225))
    liste_stations.append((6144, "BIBLIOTHEQUE FRANCOIS MITTERRAND Q1", 1, "H", 300))
    liste_stations.append((6144, "BIBLIOTHEQUE FRANCOIS MITTERRAND Q2", 2, "B", 300))
    liste_stations.append((6539, "OLYMPIADES Q1", 1, "H", 280))
    liste_stations.append((6539, "OLYMPIADES Q2", 2, "B", 280))
    liste_stations.append((6939, "MAISON BLANCHE Q1", 1, "H", 280))
    liste_stations.append((6939, "MAISON BLANCHE Q2", 2, "B", 280))
    liste_stations.append((7339, "HOPITAL BICETRE Q1", 1, "H", 350))
    liste_stations.append((7339, "HOPITAL BICETRE Q2", 2, "B", 350))
    liste_stations.append((7739, "VILLEJUIF GUSTAVE ROUSSY Q1", 1, "H", 280))
    liste_stations.append((7739, "VILLEJUIF GUSTAVE ROUSSY Q2", 2, "B", 280))
    liste_stations.append((8119, "L'HAI LES ROSES Q1", 1, "H", 350))
    liste_stations.append((8119, "L'HAI LES ROSES Q2", 2, "B", 350))
    liste_stations.append((8319, "CHEVILLY LARUE Q1", 1, "H", 280))
    liste_stations.append((8319, "CHEVILLY LARUE Q2", 2, "B", 280))
    liste_stations.append((8939, "THIAIS ORLY Q1", 1, "H", 280))
    liste_stations.append((8939, "THIAIS ORLY Q2", 2, "B", 280))
    liste_stations.append((9339, "AEROPORT D'ORLY Q1", 1, "H", 350))
    liste_stations.append((9339, "AEROPORT D'ORLY Q2", 2, "B", 350))

    liste_eguillages = []
    liste_eguillages.append((110, 2, 140, 1, 0, "Eg SAINT DENIS PLEYEL1","#EBEBEB"))
    liste_eguillages.append((110, 1, 140, 2, 0, "Eg SAINT DENIS PLEYEL2","#EBEBEB"))
    liste_eguillages.append((290,1, 260, 2, 2, "Eg SAINT DENIS PLEYEL3","#EBEBEB"))
    liste_eguillages.append((260, 1, 290, 2, 0, "Eg 00SAINT DENIS PLEYEL4","#EBEBEB"))
    liste_eguillages.append((560,2,590, 1, 0, "Eg MAIRIE DE SAINT OUEN1","#EBEBEB"))
    liste_eguillages.append((560, 1, 590, 2, 0, "Eg MAIRIE DE SAINT OUEN2","#EBEBEB"))
    liste_eguillages.append((845, 1, 875, 2, 0, "Eg SAINT OUEN","#EBEBEB"))
    liste_eguillages.append((1380, 2,1410, 1, 0, "Eg PORTE DE CLICHY1","#EBEBEB"))
    liste_eguillages.append((1380, 1, 1410, 2, 0, "Eg PORTE DE CLICHY2","#EBEBEB"))
    liste_eguillages.append((2030, 1, 2060, 2, 0, "Eg SAINT LAZARE1","#EBEBEB"))
    liste_eguillages.append((2360, 1,2390, 2, 0, "Eg MADELEINE1","#EBEBEB"))
    liste_eguillages.append((2360, 2,2390, 1, 0, "Eg MADELEINE2","#EBEBEB"))
    liste_eguillages.append((3975, 2,3945, 1, 0, "Eg chatelet1","#EBEBEB"))
    liste_eguillages.append((4620, 1,4650, 2, 0, "Eg gare de lyon1","#EBEBEB"))
    liste_eguillages.append((6200, 1, 6230, 2, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND1","#EBEBEB"))
    liste_eguillages.append(( 6620, 2,6650, 1, 0, "Eg OLYMPIADES1","#EBEBEB"))
    liste_eguillages.append((6620, 1, 6650, 2, 0, "Eg OLYMPIADES2","#EBEBEB"))
    liste_eguillages.append(( 6999, 1,7029, 2, 0, "Eg MAISON BLANCHE1","#EBEBEB"))
    liste_eguillages.append(( 7820, 1,7850, 2, 0, "Eg VILLEJUIF GUSTAVE ROUSSY1","#EBEBEB"))
    liste_eguillages.append(( 9010, 1,9040, 2, 0, "Eg THAIS ORLY1","#EBEBEB"))
    liste_eguillages.append(( 9440, 2,9470, 1, 1, "Eg AEROPORT D'ORLY1","#EBEBEB"))
    liste_eguillages.append((9440, 1, 9470, 2, 0, "Eg AEROPORT D'ORLY2","#EBEBEB"))
    liste_eguillages.append(( 9620, 2,9650, 1, 0, "Eg AEROPORT D'ORLY3","#EBEBEB"))
    liste_eguillages.append((9620, 1, 9650, 2, 0, "Eg AEROPORT D'ORLY4","#EBEBEB"))

    liste_terminus = []
    liste_terminus.append((200, 1, "SAINT DENIS PLEYEL1",1))
    liste_terminus.append((200, 2, "SAINT DENIS PLEYEL2",1))
    liste_terminus.append((470, 1, "MAIRIE DE SAINT OUEN1", 0))
    liste_terminus.append((470, 2, "MAIRIE DE SAINT OUEN2", 0))
    liste_terminus.append((1045, 3, "D1", 0))
    liste_terminus.append((1045, 4, "D2", 0))
    liste_terminus.append((1045, 5, "D3", 0))
    liste_terminus.append((1045, 6, "D4", 0))
    liste_terminus.append((1045, 7, "D5", 0))
    liste_terminus.append((1310, 1, "PORTE DE CLICHY1", 0))
    liste_terminus.append((1310, 2, "PORTE DE CLICHY2", 0))
    liste_terminus.append((1970, 1, "SAINT LAZARE", 0))
    liste_terminus.append((2290, 1, "MADELEINE1", 0))
    liste_terminus.append((2290, 2, "MADELEINE2", 0))
    liste_terminus.append((4035, 2, "CHATELET", 0))
    liste_terminus.append((4660, 2, "GARE DE LYON", 0))
    liste_terminus.append((4545, 1, "GARE DE LYON I", 0))
    liste_terminus.append((6290, 2, "BIBLIOTHEQUE FRANCOIS MITTERRAND1", 0))
    liste_terminus.append((6710, 1, "OLYMPIADES1", 0))
    liste_terminus.append((6710, 2, "OLYMPIADES2", 0))
    liste_terminus.append((7069, 2, "MAISON BLANCHE1", 0))
    liste_terminus.append((6939, 1, "MAISON BLANCHE I", 0))
    liste_terminus.append((7949, 2, "VILLEJUIF GUSTAVE ROUSSY1", 0))
    liste_terminus.append((9100, 2, "THAIS ORLY1", 0))
    liste_terminus.append((9530, 1, "AEROPORT D'ORLY1", 1))
    liste_terminus.append((9530, 2, "AEROPORT D'ORLY2", 1))

    liste_metro = []
    #train direction chateau de vincennes
    liste_metro.append(("1", 8800, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("2",200, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("3",700,  0.30, 2, 1, "#EB0004"))
    liste_metro.append(("4",1000, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("5",1300,  0.30, 2, 1, "#EB0004"))
    liste_metro.append(("6",1600, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("7",1900, 0.30,2, 1, "#EB0004"))
    liste_metro.append(("8",2200,0.30, 2, 1, "#EB0004"))
    liste_metro.append(("9",2500,  0.30,2 , 1, "#EB0004"))
    liste_metro.append(("10",2800, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("11",3100,  0.30,2, 1, "#EB0004"))
    liste_metro.append(("12",3400,0.30, 2 , 1, "#EB0004"))
    liste_metro.append(("13",3700,  0.30, 2 , 1, "#EB0004"))
    liste_metro.append(("14",4000,0.30, 2, 1, "#EB0004"))
    liste_metro.append(("15",4300,  0.30, 2, 1, "#EB0004"))
    liste_metro.append(("16",4600, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("17", 400, 0.30, 2, 1, "#EB0004"))
    liste_metro.append(("18",400,  -0.30, 1, 1,"#EB0004"))
    liste_metro.append(("19", 700, -0.30, 1, 1, "#EB0004"))
    liste_metro.append(("20",1000,  -0.30, 1, 1, "#EB0004"))
    liste_metro.append(("21", 1300, -0.30, 1, 1, "#EB0004"))
    liste_metro.append(("22",1600,  -0.30, 1, 1, "#EB0004"))
    liste_metro.append(("23", 1900, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("24",2200,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("25", 2500, -0.30, 1 , 1,"#EB0004" ))
    liste_metro.append(("26",2800,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("27", 3100, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("28",3400,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("29", 3700, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("30",4000,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("31", 4300, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("32", 4600, -0.30, 1, +1,"#EB0004" ))
    liste_metro.append(("33",4900,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("34", 4900, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("35",5200,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("36", 5200, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("37",5500, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("38",5500,  0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("39", 5800, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("40",5800,  0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("41", 6100, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("42  ",6100, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("43",6400,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("44", 6400, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("45",6700,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("46", 6700, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("47  ",7000, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("48",7000,  0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("49  ",7300, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("50",7300,  0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("51",7600,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("52",7600,  0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("53", 7900, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("54",7900,  0.30, 2 , 1,"#EB0004" ))
    liste_metro.append(("55", 8200, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("56 ",8200, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("57",8500,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("58", 8500, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("59",8800,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("61", 9100, 0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("62",9100, -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("63",9400,  0.30, 2, 1,"#EB0004" ))
    liste_metro.append(("64",9400,  -0.30, 1, 1,"#EB0004" ))
    liste_metro.append(("65",9700,  0.30, 2, 0,"#EB0004" ))
    liste_metro.append(("66",9700,  -0.30, 1, 0,"#EB0004" ))


    liste_lignes = []
    liste_lignes.append(( 1, 10, 10000, "#EBEBEB", 4))
    liste_lignes.append(( 2, 10, 10000, "#EBEBEB", 4))



    liste_depot_eguillage = []
    # eguillage depot
    liste_depot_eguillage.append((885, 2, 915, 3, 0, "Eg SAINT OUEN1","#CCCCCC"))
    liste_depot_eguillage.append((915, 3, 945, 4, 0, "Eg D1","#CCCCCC"))
    liste_depot_eguillage.append((945, 4, 975, 5, 0, "Eg D2","#CCCCCC"))
    liste_depot_eguillage.append((1065, 4, 1095, 5, 0, "Eg D3","#CCCCCC"))
    liste_depot_eguillage.append((1065, 5, 1095, 6, 0, "Eg D4","#CCCCCC"))
    liste_depot_eguillage.append((1095, 4, 1125, 3, 0, "Eg D5","#CCCCCC"))
    liste_depot_eguillage.append((1095, 5, 1125, 6, 0, "Eg D6","#CCCCCC"))
    liste_depot_eguillage.append((1125, 6, 1155, 7, 0, "Eg D7","#CCCCCC"))
    liste_depot_eguillage.append((1155, 7, 1185, 8, 0, "Eg D7","#CCCCCC"))
    liste_eguillages.append((6720, 2, 6750, 3, 0, "Eg OLYMPIADES","#CCCCCC"))



    liste_depot_ligne = []
     #ligne depot
    liste_depot_ligne.append((6990, 1, 7260, "#EBEBEB", 4))
    liste_depot_ligne.append((6990, 2, 7260, "#EBEBEB", 4))
    liste_depot_ligne.append((350, 1, 560, "#EBEBEB", 4))
    liste_depot_ligne.append((350, 2, 560, "#EBEBEB", 4))
    liste_depot_ligne.append((1125, 3, 1395, "#EBEBEB", 4))
    liste_depot_ligne.append((945, 4, 1395, "#EBEBEB", 4))
    liste_depot_ligne.append((975, 5, 1395, "#EBEBEB", 4))
    liste_depot_ligne.append((1125, 6, 1395,  "#EBEBEB", 4))
    liste_depot_ligne.append((1155, 7, 1395, "#EBEBEB", 4))
    liste_depot_ligne.append((1185, 8, 1395, "#EBEBEB", 4))
    liste_depot_ligne.append((6750, 3, 6810, "#EBEBEB", 4))

    liste_feu_traffic = []
    # feu eguillage terminus saint denis pleyel
    liste_feu_traffic.append(("325",110, 1, "B", 1))
    liste_feu_traffic.append(("315",110, 2, "B", 1))
    liste_feu_traffic.append(("326",140, 1, "H", 1))
    liste_feu_traffic.append(("318",140, 2, "H", 1))
    liste_feu_traffic.append(("322",300, 1, "H", 1))
    liste_feu_traffic.append(("314",300, 2, "H", 1))
    # feu eguillage terminus saint denis pleyel
    liste_feu_traffic.append(("324",200, 1, "H", 2))
    liste_feu_traffic.append(("327",200, 1, "B", 2))
    liste_feu_traffic.append(("316",200, 2, "H", 2))
    liste_feu_traffic.append(("317",200, 2, "B", 2))


    liste_feu_traffic.append(("319",255, 2, "B", 1))
    liste_feu_traffic.append(("329",250, 1, "B", 1))
    # feu terminus saint denis pleyel direction saint denis pleyel
    liste_feu_traffic.append(("320",350, 1, "H", 1))

    # feu terminus saint denis pleyel direction aéroport d'orly
    liste_feu_traffic.append(("312",347, 2, "B", 1))
    liste_feu_traffic.append(("331",350, 2, "B", 1))
    liste_feu_traffic.append(("351",410, 2, "B", 1))
    # feu service provisoire mairie de saint ouen
    liste_feu_traffic.append(("407",500, 2, "B", 1))
    # feu equillage mairie de saint ouen
    liste_feu_traffic.append(("409",560, 1, "B", 1))
    liste_feu_traffic.append(("411",560, 2, "B", 1))
    liste_feu_traffic.append(("430",590, 1, "H", 1))
    liste_feu_traffic.append(("432",590, 2, "H", 1))
    #feu d'arriver mairie de saint ouen direction sdp
    liste_feu_traffic.append(("544",710, 1, "H", 1))
    #feu d'arriver mairie de saint ouen direction ao
    liste_feu_traffic.append(("428",640, 2, "H", 1))
    liste_feu_traffic.append(("413",640, 2, "B", 1))
    #feu départ mairie de saint ouen direction sdp
    liste_feu_traffic.append(("426",640, 1, "H", 1))
    #feu départ mairie de saint ouen direction ao
    liste_feu_traffic.append(("451",710, 2, "B", 1))

    liste_feu_traffic.append(("519",775, 2, "B", 1))
    liste_feu_traffic.append(("542",850, 1, "H", 1))


    #feu equillage depot
    liste_feu_traffic.append(("543",840, 1, "B", 1))
    liste_feu_traffic.append(("521",840, 2, "B", 1))
    #feu départ saint ouen direction sdp
    liste_feu_traffic.append(("556",1025, 1, "H", 1))
    #feu départ saint ouen direction ao
    liste_feu_traffic.append(("553",1085, 2, "B", 1))
    #feu arrivé saint ouen direction sdp
    liste_feu_traffic.append(("554",1085, 1, "H", 1))
    #feu arrivé saint ouen direction ao
    liste_feu_traffic.append(("551",1025, 2, "B", 1))

    liste_feu_traffic.append(("552",1355, 1, "H", 1))

    #feu départ porte de clichy direction mso
    liste_feu_traffic.append(("314",1445, 1, "H", 1))
    #feu départ porte de clichy direction o
    liste_feu_traffic.append(("314",1505, 2, "B", 1))
    #feu arrivé porte de clichy direction mso
    liste_feu_traffic.append(("314",1505, 1, "H", 1))
    #feu arrivé porte de clichy direction o
    liste_feu_traffic.append(("314",1445, 2, "B", 1))# changement a continué:
    #feu départ pont cardinet direction mso
    liste_feu_traffic.append(("314",1695, 1, "H", 1))
    #feu départ pont cardinet direction o
    liste_feu_traffic.append(("314",1755, 2, "B", 1))
    #feu arrivé pont cardinet direction mso
    liste_feu_traffic.append(("314",1755, 1, "H", 1))
    #feu arrivé pont cardinet direction o
    liste_feu_traffic.append(("314",1695, 2, "B", 1))
    #feu départ saint lazare direction mso
    liste_feu_traffic.append(("314",2115, 1, "H", 1))
    #feu départ saint lazare direction o
    liste_feu_traffic.append(("314",2175, 2, "B", 1))
    #feu arrivé saint lazare direction mso
    liste_feu_traffic.append(("314",2175, 1, "H", 1))
    #feu arrivé saint lazare direction o
    liste_feu_traffic.append(("314",2115, 2, "B", 1))
    #feu départ madeleine direction mso
    liste_feu_traffic.append(("314",2385, 1, "H", 1))
    #feu départ madeleine direction o
    liste_feu_traffic.append(("314",2445, 2, "B", 1))
    #feu arrivé madeleine direction mso
    liste_feu_traffic.append(("314",2445, 1, "H", 1))
    #feu arrivé madeleine direction o
    liste_feu_traffic.append(("314",2385, 2, "B", 1))
    #feu départ pyramide direction mso
    liste_feu_traffic.append(("314",3655, 1, "H", 1))
    #feu départ pyramide direction o
    liste_feu_traffic.append(("314",3715, 2, "B", 1))
    #feu arrivé pyramide direction
    liste_feu_traffic.append(("314",3715, 1, "H", 1))
    #feu arrivé pyramide direction o
    liste_feu_traffic.append(("314",3655, 2, "B", 1))
    #feu départ chatelet direction mso
    liste_feu_traffic.append(("314",4215, 1, "H", 1))
    #feu départ chatelet direction o
    liste_feu_traffic.append(("314",4275, 2, "B", 1))
    #feu arrivé chatelet direction mso
    liste_feu_traffic.append(("314",4275, 1, "H", 1))
    #feu arrivé chatelet direction o
    liste_feu_traffic.append(("314",4215, 2, "B", 1))
    #feu départ gare de lyon direction mso
    liste_feu_traffic.append(("314",4875, 1, "H", 1))
    #feu départ gare de lyon direction o
    liste_feu_traffic.append(("314",4935, 2, "B", 1))
    #feu arrivé gare de lyon direction mso
    liste_feu_traffic.append(("314",4935, 1, "H", 1))
    #feu arrivé gare de lyon direction o
    liste_feu_traffic.append(("314",4875, 2, "B", 1))
    #feu départ bercy direction mso
    liste_feu_traffic.append(("314",5335, 1, "H", 1))
    #feu départ bercy direction o
    liste_feu_traffic.append(("314",5395, 2, "B", 1))
    #feu arrivé bercy direction mso
    liste_feu_traffic.append(("314",5395, 1, "H", 1))
    #feu arrivé bercy direction o
    liste_feu_traffic.append(("314",5335, 2, "B", 1))
    #feu départ cour st emillion directio1 mso
    liste_feu_traffic.append(("314",5895, 1, "H", 1))
    #feu départ cour st emillion direction o
    liste_feu_traffic.append(("314",5955, 2, "B", 1))
    #feu arrivé cour st emillion directio1 mso
    liste_feu_traffic.append(("314",5955, 1, "H", 1))
    #feu arrivé cour st emillion direction o
    liste_feu_traffic.append(("314",5895, 2, "B", 1))
    #feu départ bibliotheque francois mitterand direction mso
    liste_feu_traffic.append(("314",6472, 1, "H", 1))
    #feu départ bibliotheque francois mitterand direction o
    liste_feu_traffic.append(("314",6532, 2, "B", 1))
    #feu arrivé bibliotheque francois mitterand direction mso
    liste_feu_traffic.append(("314",6532, 1, "H", 1))
    #feu arrivé bibliotheque francois mitterand direction o
    liste_feu_traffic.append(("314",6472, 2, "B", 1))
    #feu départ olympiade direction mso
    liste_feu_traffic.append(("314",6869, 1, "H", 1))
    #feu départ olympiade direction o
    liste_feu_traffic.append(("314",6929, 2, "B", 1))
    #feu arrivé olympiade direction mso
    liste_feu_traffic.append(("314",6929, 1, "H", 1))
    #feu arrivé olympiade direction o
    liste_feu_traffic.append(("314",6869, 2, "B", 1))
    #feu eguillage olympiade
    liste_feu_traffic.append(("314",7000, 1, "H", 1))
    liste_feu_traffic.append(("314",7000, 2, "B", 1))
    #feu eguillage maison blanche
    liste_feu_traffic.append(("314",7269, 1, "H", 1))
    liste_feu_traffic.append(("314",7330, 2, "B", 1))
    liste_feu_traffic.append(("314",7330, 1, "H", 1))
    liste_feu_traffic.append(("314",7269, 2, "B", 1))
    #feu eguillage hopital bicetre
    liste_feu_traffic.append(("314",7669, 1, "H", 1))
    liste_feu_traffic.append(("314",7730, 2, "B", 1))
    liste_feu_traffic.append(("314",7730, 1, "H", 1))
    liste_feu_traffic.append(("314",7669, 2, "B", 1))
    #feu eguillage villejuif gustave roussy
    liste_feu_traffic.append(("314",8069, 1, "H", 1))
    liste_feu_traffic.append(("314",8130, 2, "B", 1))
    liste_feu_traffic.append(("314",8130, 1, "H", 1))
    liste_feu_traffic.append(("314",8069, 2, "B", 1))
    #feu eguillage l'hai les roses
    liste_feu_traffic.append(("314",8469, 1, "H", 1))
    liste_feu_traffic.append(("314",8530, 2, "B", 1))
    liste_feu_traffic.append(("314",8530, 1, "H", 1))
    liste_feu_traffic.append(("314",8469, 2, "B", 1))
    #feu eguillage chevilly la rue
    liste_feu_traffic.append(("314",8869, 1, "H", 1))
    liste_feu_traffic.append(("314",8930, 2, "B", 1))
    liste_feu_traffic.append(("314",8930, 1, "H", 1))
    liste_feu_traffic.append(("314",8869, 2, "B", 1))
    #feu eguillage thiais orly
    liste_feu_traffic.append(("314",9269, 1, "H", 1))
    liste_feu_traffic.append(("314",9330, 2, "B", 1))
    liste_feu_traffic.append(("314",9330, 1, "H", 1))
    liste_feu_traffic.append(("314",9269, 2, "B", 1))
    #feu eguillage aéroport d'orly direction aéroport d'orly
    liste_feu_traffic.append(("314",9669, 2, "B", 1))
    liste_feu_traffic.append(("314",9730, 2, "B", 1))
    #feu eguillage aéroport d'orly direction saint denis pleyel
    liste_feu_traffic.append(("314",9669, 1, "H", 1))
    liste_feu_traffic.append(("314",9730, 1, "H", 1))
    #feu eguillage terminus aéroport d'orly
    liste_feu_traffic.append(("314",9830, 1, "H", 1))
    liste_feu_traffic.append(("314",9760, 2, "B", 1))
    liste_feu_traffic.append(("314",9830, 2, "B", 1))
    liste_feu_traffic.append(("314",9760, 2, "B", 1))
    #feu depot
    liste_feu_traffic.append(("314",985, 5, "H", 1))
    liste_feu_traffic.append(("314",985, 6,  "H",1))
    liste_feu_traffic.append(("314",1100, 7, "H", 1))
    liste_feu_traffic.append(("314",1100, 8, "H",1))


