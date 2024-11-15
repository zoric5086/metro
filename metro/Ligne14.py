class ClasseLigne14():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((350, "SAINT DENIS PLEYEL", 2, 350))
    liste_stations.append((350, "SAINT DENIS PLEYEL", 4, 410))
    liste_stations.append((650, "MAIRIE DE SAINT-OUEN", 2, 280))
    liste_stations.append((650, "MAIRIE DE SAINT-OUEN", 4, 280))
    liste_stations.append((1025, "CLICHY SAINT-OUEN", 2, 240))
    liste_stations.append((1025, "CLICHY SAINT-OUEN", 4, 240))
    liste_stations.append((1445, "PORTE DE CLICHY", 2, 225))
    liste_stations.append((1445, "PORTE DE CLICHY", 4, 225))
    liste_stations.append((1695, "PONT CARDINET", 2, 225))
    liste_stations.append((1695, "PONT CARDINET", 4, 225))
    liste_stations.append((2125, "SAINT LAZARE", 2, 330))
    liste_stations.append((2125, "SAINT LAZARE", 4, 330))
    liste_stations.append((2395, "MADELEINE", 2, 330))
    liste_stations.append((2395, "MADELEINE", 4, 330))
    liste_stations.append((3325, "PYRAMIDES",2, 300))
    liste_stations.append((3325, "PYRAMIDES", 4, 300))
    liste_stations.append((3885, "CHATELET",2, 350))
    liste_stations.append((3885, "CHATELET", 4, 350))
    liste_stations.append((4545, "GARE DE LYON",3, 350))
    liste_stations.append((5005, "BERCY",2, 280))
    liste_stations.append((5005, "BERCY", 4, 280))
    liste_stations.append((5565, "COUR ST EMILLION",2, 225))
    liste_stations.append((5565, "COUR ST EMILLION", 4, 225))
    liste_stations.append((6144, "BIBLIOTHEQUE FRANCOIS MITTERRAND",2, 300))
    liste_stations.append((6144, "BIBLIOTHEQUE FRANCOIS MITTERRAND", 4, 300))
    liste_stations.append((6539, "OLYMPIADES",2, 280))
    liste_stations.append((6539, "OLYMPIADES", 4, 280))
    liste_stations.append((6939, "MAISON BLANCHE",2, 280))
    liste_stations.append((6939, "MAISON BLANCHE", 4, 280))
    liste_stations.append((7339, "HOPITAL BICETRE",2, 350))
    liste_stations.append((7339, "HOPITAL BICETRE", 4, 350))
    liste_stations.append((7739, "VILLEJUIF GUSTAVE ROUSSY",2, 280, 0))
    liste_stations.append((7739, "VILLEJUIF GUSTAVE ROUSSY",4,280, 0))
    liste_stations.append((8119, "L'HAI LES ROSES",2, 350))
    liste_stations.append((8119, "L'HAI LES ROSES", 4, 350))
    liste_stations.append((8319, "CHEVILLY LARUE",2, 280))
    liste_stations.append((8319, "CHEVILLY LARUE", 4, 280))
    liste_stations.append((8939, "THIAIS ORLY",2, 280))
    liste_stations.append((8939, "THIAIS ORLY", 4, 280))
    liste_stations.append((9339, "AEROPORT D'ORLY",2, 350))
    liste_stations.append((9339, "AEROPORT D'ORLY", 4, 350))
    liste_eguillages = []
    liste_eguillages.append((110,130,140, 100, 0, "Eg SAINT DENIS PLEYEL1"))
    liste_eguillages.append((110, 100, 140, 130, 0, "Eg SAINT DENIS PLEYEL2"))
    liste_eguillages.append((260,130,290, 100, 2, "Eg SAINT DENIS PLEYEL3"))
    liste_eguillages.append((260, 100, 290, 130, 0, "Eg SAINT DENIS PLEYEL4"))
    liste_eguillages.append((560,130,590, 100, 0, "Eg MAIRIE DE SAINT OUEN1"))
    liste_eguillages.append((560, 100, 590, 130, 0, "Eg MAIRIE DE SAINT OUEN2"))
    liste_eguillages.append((845, 100, 875, 130, 0, "Eg SAINT OUEN"))
    liste_eguillages.append(( 1380, 130,1410, 100, 0, "Eg PORTE DE CLICHY1"))
    liste_eguillages.append((1380, 100, 1410, 130, 0, "Eg PORTE DE CLICHY2"))
    liste_eguillages.append((2030, 100, 2060, 130, 0, "Eg SAINT LAZARE1"))
    liste_eguillages.append((2360, 100,2390, 130, 0, "Eg MADELEINE1"))
    liste_eguillages.append((2360, 130,2390, 100, 0, "Eg MADELEINE2"))
    liste_eguillages.append((4295, 130,4325, 100, 0, "Eg chatelet1"))
    liste_eguillages.append((4990, 100,5020, 130, 0, "Eg gare de lyon1"))
    liste_eguillages.append((6560, 100, 6590, 130, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND1"))
    liste_eguillages.append(( 6810, 130,6840, 100, 0, "Eg OLYMPIADES1"))
    liste_eguillages.append((6810, 100, 6840, 130, 0, "Eg OLYMPIADES2"))
    liste_eguillages.append(( 6960, 130,6990, 100, 0, "Eg OLYMPIADES3"))
    liste_eguillages.append((6960, 100, 6990, 130, 0, "Eg OLYMPIADES4"))
    liste_eguillages.append(( 7360, 100,7390, 130, 0, "Eg MAISON BLANCHE1"))
    liste_eguillages.append(( 8160, 100,8190, 130, 0, "Eg VILLEJUIF GUSTAVE ROUSSY1"))
    liste_eguillages.append(( 9360, 100,9390, 130, 0, "Eg THAIS ORLY1"))
    liste_eguillages.append(( 9770, 130,9800, 100, 1, "Eg AEROPORT D'ORLY1"))
    liste_eguillages.append((9770, 100, 9800, 130, 0, "Eg AEROPORT D'ORLY2"))
    liste_eguillages.append(( 9920, 130,9950, 100, 0, "Eg AEROPORT D'ORLY3"))
    liste_eguillages.append((9920, 100, 9950, 130, 0, "Eg AEROPORT D'ORLY4"))
    liste_terminus = []
    liste_terminus.append((200, 100, "SAINT DENIS PLEYEL1"))
    liste_terminus.append((200, 130, "SAINT DENIS PLEYEL2"))
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
    #liste_terminus.append((6330, 130, "BIBLIOTHEQUE FRANCOIS MITTERRAND1"))
    #liste_terminus.append((6330, 100, "BIBLIOTHEQUE FRANCOIS MITTERRAND2"))
    #liste_terminus.append((7060, 130, "OLYMPIADES2"))
    #liste_terminus.append((7060, 100, "OLYMPIADES1"))
    #liste_terminus.append((7060, 130, "OLYMPIADES2"))
    #liste_terminus.append((7120, 100, "OLYMPIADES3"))
    #liste_terminus.append((7120, 130, "OLYMPIADES4"))
    #liste_terminus.append((7200, 100, "OLYMPIADES5"))
    #liste_terminus.append((7200, 130, "OLYMPIADES6"))
    liste_terminus.append((9840, 100, "AEROPORT D'ORLY1"))
    liste_terminus.append((9840, 130, "AEROPORT D'ORLY2"))

    liste_metro = []
    #train direction chateau de vincennes
    liste_metro.append(("1", 8800, 0.30, 80,1,"#EB0004" ))
    liste_metro.append(("2",200, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("3",700,  0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("4",1000, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("5",1300,  0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("6",1600, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("7",1900, 0.30,80, 1,"#EB0004" ))
    liste_metro.append(("8",2200,0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("9",2500,  0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("10",2800, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("11",3100,  0.30,80, 1,"#EB0004" ))
    liste_metro.append(("12",3400,0.30, 80 , 1,"#EB0004" ))
    liste_metro.append(("13",3700,  0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("14",4000,0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("15",4300,  0.30, 80 , 1,"#EB0004" ))
    liste_metro.append(("16",4600, 0.30, 80 , 1,"#EB0004" ))
    liste_metro.append(("17", 400, 0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("18",400,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("19", 700, -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("20",1000,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("21", 1300, -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("22",1600,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("23", 1900, -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("24",2200,  -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("25", 2500, -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("26",2800,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("27", 3100, -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("28",3400,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("29", 3700, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("30",4000,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("31", 4300, -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("32  ",4600, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("33",4900,  -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("34", 4900, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("35",5200,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("36", 5200, 0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("37",5500, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("38",5500,  0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("39", 5800, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("40",5800,  0.30, 80 , 1,"#EB0004" ))
    liste_metro.append(("41", 6100, -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("42  ",6100, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("43",6400,  -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("44", 6400, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("45",6700,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("46", 6700, 0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("47  ",7000, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("48",7000,  0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("49  ",7300, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("50",7300,  0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("51",7600,  -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("52",7600,  0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("53", 7900, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("54",7900,  0.30, 80 , 1,"#EB0004" ))
    liste_metro.append(("55", 8200, -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("56 ",8200, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("57",8500,  -0.30,50 , 1,"#EB0004" ))
    liste_metro.append(("58", 8500, 0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("59",8800,  -0.30, 50 , 1,"#EB0004" ))
    liste_metro.append(("61", 9100, 0.30,80 , 1,"#EB0004" ))
    liste_metro.append(("62",9100, -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("63",9400,  0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("64",9400,  -0.30, 50, 1,"#EB0004" ))
    liste_metro.append(("65",9700,  0.30, 80, 1,"#EB0004" ))
    liste_metro.append(("66",9700,  -0.30, 50, 1,"#EB0004" ))


    liste_lignes = []
    liste_lignes.append((10, 100, 350, 100, "#EBEBEB", 4))
    liste_lignes.append((10, 130, 350, 130, "#EBEBEB", 4))
    liste_lignes.append((560, 100, 6990, 100, "#EBEBEB", 4))
    liste_lignes.append((560, 130, 6990, 130, "#EBEBEB", 4))
    liste_lignes.append((7200, 100, 10000, 100, "#EBEBEB", 4))
    liste_lignes.append((7200, 130, 10000, 130, "#EBEBEB", 4))


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
    liste_depot_ligne.append((6990, 100, 7260, 100, "#EBEBEB", 4))
    liste_depot_ligne.append((6990, 130, 7260, 130, "#EBEBEB", 4))
    liste_depot_ligne.append((350, 100, 560, 100, "#EBEBEB", 4))
    liste_depot_ligne.append((350, 130, 560, 130, "#EBEBEB", 4))
    liste_depot_ligne.append((1125, 160, 1395, 160, "#EBEBEB", 4))
    liste_depot_ligne.append((945, 190, 1395, 190, "#EBEBEB", 4))
    liste_depot_ligne.append((975, 220, 1395, 220, "#EBEBEB", 4))
    liste_depot_ligne.append((1125, 250, 1395, 250, "#EBEBEB", 4))
    liste_depot_ligne.append((1155, 280, 1395, 280, "#EBEBEB", 4))
    liste_depot_ligne.append((1185, 310, 1395, 310, "#EBEBEB", 4))
    liste_depot_ligne.append((7090, 160, 7150, 160, "#EBEBEB", 4))

    liste_feu_traffic = []
    # feu eguillage terminus saint denis pleyel
    liste_feu_traffic.append(("325",110, 2, 1))
    liste_feu_traffic.append(("315",110, 4, 1))
    liste_feu_traffic.append(("326",140, 1, 1))
    liste_feu_traffic.append(("318",140, 3, 1))
    liste_feu_traffic.append(("322",300, 1, 1))
    liste_feu_traffic.append(("314",300, 3, 1))
    # feu eguillage terminus saint denis pleyel
    liste_feu_traffic.append(("324",200, 1, 2))
    liste_feu_traffic.append(("327",200, 2, 2))
    liste_feu_traffic.append(("316",200, 3, 2))
    liste_feu_traffic.append(("317",200, 4, 2))


    liste_feu_traffic.append(("319",255, 4, 1))
    liste_feu_traffic.append(("329",250, 2, 1))
    # feu terminus saint denis pleyel direction saint denis pleyel
    liste_feu_traffic.append(("320",350, 1, 1))

    # feu terminus saint denis pleyel direction aéroport d'orly
    liste_feu_traffic.append(("312",347, 3, 1))
    liste_feu_traffic.append(("331",350, 4, 1))
    liste_feu_traffic.append(("351",410, 4, 1))
    # feu service provisoire mairie de saint ouen
    liste_feu_traffic.append(("407",500, 4, 1))
    # feu equillage mairie de saint ouen
    liste_feu_traffic.append(("409",560, 2, 1))
    liste_feu_traffic.append(("411",560, 4, 1))
    liste_feu_traffic.append(("430",590, 1, 1))
    liste_feu_traffic.append(("432",590, 3, 1))
    #feu d'arriver mairie de saint ouen direction sdp
    liste_feu_traffic.append(("544",710, 1, 1))
    #feu d'arriver mairie de saint ouen direction ao
    liste_feu_traffic.append(("428",640, 3, 1))
    liste_feu_traffic.append(("413",640, 4, 1))
    #feu départ mairie de saint ouen direction sdp
    liste_feu_traffic.append(("426",640, 1, 1))
    #feu départ mairie de saint ouen direction ao
    liste_feu_traffic.append(("451",710, 4, 1))

    liste_feu_traffic.append(("519",775, 4, 1))
    liste_feu_traffic.append(("542",850, 1, 1))


    #feu equillage depot
    liste_feu_traffic.append(("543",840, 2, 1))
    liste_feu_traffic.append(("521",840, 4, 1))
    #feu départ saint ouen direction sdp
    liste_feu_traffic.append(("556",1025, 1, 1))
    #feu départ saint ouen direction ao
    liste_feu_traffic.append(("553",1085, 4, 1))
    #feu arrivé saint ouen direction sdp
    liste_feu_traffic.append(("554",1085, 1, 1))
    #feu arrivé saint ouen direction ao
    liste_feu_traffic.append(("551",1025, 4, 1))

    liste_feu_traffic.append(("552",1355, 1, 1))

    #feu départ porte de clichy direction mso
    liste_feu_traffic.append(("314",1445, 1, 1))
    #feu départ porte de clichy direction o
    liste_feu_traffic.append(("314",1505, 4, 1))
    #feu arrivé porte de clichy direction mso
    liste_feu_traffic.append(("314",1505, 1, 1))
    #feu arrivé porte de clichy direction o
    liste_feu_traffic.append(("314",1445, 4, 1))# changement a continué:
    #feu départ pont cardinet direction mso
    liste_feu_traffic.append(("314",1695, 1, 1))
    #feu départ pont cardinet direction o
    liste_feu_traffic.append(("314",1755, 4, 1))
    #feu arrivé pont cardinet direction mso
    liste_feu_traffic.append(("314",1755, 1, 1))
    #feu arrivé pont cardinet direction o
    liste_feu_traffic.append(("314",1695, 4, 1))
    #feu départ saint lazare direction mso
    liste_feu_traffic.append(("314",2115, 1, 1))
    #feu départ saint lazare direction o
    liste_feu_traffic.append(("314",2175, 4, 1))
    #feu arrivé saint lazare direction mso
    liste_feu_traffic.append(("314",2175, 1, 1))
    #feu arrivé saint lazare direction o
    liste_feu_traffic.append(("314",2115, 4, 1))
    #feu départ madeleine direction mso
    liste_feu_traffic.append(("314",2385, 1, 1))
    #feu départ madeleine direction o
    liste_feu_traffic.append(("314",2445, 4, 1))
    #feu arrivé madeleine direction mso
    liste_feu_traffic.append(("314",2445, 1, 1))
    #feu arrivé madeleine direction o
    liste_feu_traffic.append(("314",2385, 4, 1))
    #feu départ pyramide direction mso
    liste_feu_traffic.append(("314",3655, 1, 1))
    #feu départ pyramide direction o
    liste_feu_traffic.append(("314",3715, 4, 1))
    #feu arrivé pyramide direction
    liste_feu_traffic.append(("314",3715, 1, 1))
    #feu arrivé pyramide direction o
    liste_feu_traffic.append(("314",3655, 4, 1))
    #feu départ chatelet direction mso
    liste_feu_traffic.append(("314",4215, 1, 1))
    #feu départ chatelet direction o
    liste_feu_traffic.append(("314",4275, 4, 1))
    #feu arrivé chatelet direction mso
    liste_feu_traffic.append(("314",4275, 1, 1))
    #feu arrivé chatelet direction o
    liste_feu_traffic.append(("314",4215, 4, 1))
    #feu départ gare de lyon direction mso
    liste_feu_traffic.append(("314",4875, 1, 1))
    #feu départ gare de lyon direction o
    liste_feu_traffic.append(("314",4935, 4, 1))
    #feu arrivé gare de lyon direction mso
    liste_feu_traffic.append(("314",4935, 1, 1))
    #feu arrivé gare de lyon direction o
    liste_feu_traffic.append(("314",4875, 4, 1))
    #feu départ bercy direction mso
    liste_feu_traffic.append(("314",5335, 1, 1))
    #feu départ bercy direction o
    liste_feu_traffic.append(("314",5395, 4, 1))
    #feu arrivé bercy direction mso
    liste_feu_traffic.append(("314",5395, 1, 1))
    #feu arrivé bercy direction o
    liste_feu_traffic.append(("314",5335, 4, 1))
    #feu départ cour st emillion directio1 mso
    liste_feu_traffic.append(("314",5895, 1, 1))
    #feu départ cour st emillion direction o
    liste_feu_traffic.append(("314",5955, 4, 1))
    #feu arrivé cour st emillion directio1 mso
    liste_feu_traffic.append(("314",5955, 1, 1))
    #feu arrivé cour st emillion direction o
    liste_feu_traffic.append(("314",5895, 4, 1))
    #feu départ bibliotheque francois mitterand direction mso
    liste_feu_traffic.append(("314",6472, 1, 1))
    #feu départ bibliotheque francois mitterand direction o
    liste_feu_traffic.append(("314",6532, 4, 1))
    #feu arrivé bibliotheque francois mitterand direction mso
    liste_feu_traffic.append(("314",6532, 1, 1))
    #feu arrivé bibliotheque francois mitterand direction o
    liste_feu_traffic.append(("314",6472, 4, 1))
    #feu départ olympiade direction mso
    liste_feu_traffic.append(("314",6869, 1, 1))
    #feu départ olympiade direction o
    liste_feu_traffic.append(("314",6929, 4, 1))
    #feu arrivé olympiade direction mso
    liste_feu_traffic.append(("314",6929, 1, 1))
    #feu arrivé olympiade direction o
    liste_feu_traffic.append(("314",6869, 4, 1))
    #feu eguillage olympiade
    liste_feu_traffic.append(("314",7000, 1, 1))
    liste_feu_traffic.append(("314",7000, 4, 1))
    #feu eguillage maison blanche
    liste_feu_traffic.append(("314",7269, 1, 1))
    liste_feu_traffic.append(("314",7330, 4, 1))
    liste_feu_traffic.append(("314",7330, 1, 1))
    liste_feu_traffic.append(("314",7269, 4, 1))
    #feu eguillage hopital bicetre
    liste_feu_traffic.append(("314",7669, 1, 1))
    liste_feu_traffic.append(("314",7730, 4, 1))
    liste_feu_traffic.append(("314",7730, 1, 1))
    liste_feu_traffic.append(("314",7669, 4, 1))
    #feu eguillage villejuif gustave roussy
    liste_feu_traffic.append(("314",8069, 1, 1))
    liste_feu_traffic.append(("314",8130, 4, 1))
    liste_feu_traffic.append(("314",8130, 1, 1))
    liste_feu_traffic.append(("314",8069, 4, 1))
    #feu eguillage l'hai les roses
    liste_feu_traffic.append(("314",8469, 1, 1))
    liste_feu_traffic.append(("314",8530, 4, 1))
    liste_feu_traffic.append(("314",8530, 1, 1))
    liste_feu_traffic.append(("314",8469, 4, 1))
    #feu eguillage chevilly la rue
    liste_feu_traffic.append(("314",8869, 1, 1))
    liste_feu_traffic.append(("314",8930, 4, 1))
    liste_feu_traffic.append(("314",8930, 1, 1))
    liste_feu_traffic.append(("314",8869, 4, 1))
    #feu eguillage thiais orly
    liste_feu_traffic.append(("314",9269, 1, 1))
    liste_feu_traffic.append(("314",9330, 4, 1))
    liste_feu_traffic.append(("314",9330, 1, 1))
    liste_feu_traffic.append(("314",9269, 4, 1))
    #feu eguillage aéroport d'orly direction aéroport d'orly
    liste_feu_traffic.append(("314",9669, 4, 1))
    liste_feu_traffic.append(("314",9730, 4, 1))
    #feu eguillage aéroport d'orly direction saint denis pleyel
    liste_feu_traffic.append(("314",9669, 1, 1))
    liste_feu_traffic.append(("314",9730, 1, 1))
    #feu eguillage terminus aéroport d'orly
    liste_feu_traffic.append(("314",9830, 1, 1))
    liste_feu_traffic.append(("314",9760, 1, 1))
    liste_feu_traffic.append(("314",9830, 4, 1))
    liste_feu_traffic.append(("314",9760, 4, 1))
    #feu depot
    liste_feu_traffic.append(("314",985, 5, 1))
    liste_feu_traffic.append(("314",985, 6, 1))
    liste_feu_traffic.append(("314",1100, 7, 1))
    liste_feu_traffic.append(("314",1100, 8, 1))


