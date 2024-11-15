class ClasseLigne0():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((250, "SAINT DENIS PLEYEL Q1", 2, 100))
    liste_stations.append((250, "SAINT DENIS PLEYEL Q2", 4, 100))
    liste_stations.append((650, "MAIRIE DE ST OUEN Q1", 2, 100))
    liste_stations.append((650, "MAIRIE DE ST OUEN Q2", 4, 100))
    liste_stations.append((1145, "SAINT OUEN Q1", 2, 100))
    liste_stations.append((1145, "SAINT OUEN Q2", 4, 100))
    liste_stations.append((1675, "PORTE DE CLICHY Q1", 2, 100))
    liste_stations.append((1675, "PORTE DE CLICHY Q2", 4, 100))
    liste_stations.append((2235, "PONT CARDINET Q1", 2, 100))
    liste_stations.append((2235, "PONT CARDINET Q2", 4, 100))
    liste_stations.append((2675, "SAINT LAZARE Q1", 2, 100))
    liste_stations.append((2675, "SAINT LAZARE Q2", 4, 100))
    liste_stations.append((3135, "MADELEINE Q1", 2, 100))
    liste_stations.append((3135, "MADELEINE Q2", 4, 100))
    liste_stations.append((3655, "PYRAMIDES Q1",2, 100))
    liste_stations.append((3655, "PYRAMIDES Q2", 4, 100))
    liste_stations.append((4215, "CHATELET Q1",2, 100))
    liste_stations.append((4215, "CHATELET Q2", 4, 100))
    liste_stations.append((4875, "GARE DE LYON Q1",3, 100))
    liste_stations.append((5335, "BERCY Q1",2, 100))
    liste_stations.append((5335, "BERCY Q2", 4, 100))
    liste_stations.append((5895, "COUR ST EMILLION Q1",2, 100))
    liste_stations.append((5895, "COUR ST EMILLION Q2", 4, 100))
    liste_stations.append((6472, "BIBLIOTHEQUE FRANCOIS MITTERRAND Q1",2, 100))
    liste_stations.append((6472, "BIBLIOTHEQUE FRANCOIS MITTERRAND Q2", 4, 100))
    liste_stations.append((6869, "OLYMPIADES Q1",2, 100))
    liste_stations.append((6869, "OLYMPIADES Q2", 4, 100))
    liste_stations.append((7269, "MAISON BLANCHE Q1",2, 100))
    liste_stations.append((7269, "MAISON BLANCHE Q2", 4, 100))
    liste_stations.append((7669, "HOPITAL BICETRE Q1",2, 100))
    liste_stations.append((7669, "HOPITAL BICETRE Q2", 4, 100))
    liste_stations.append((8069, "VILLEJUIF GUSTAVE ROUSSY Q1",2, 100, 0))
    liste_stations.append((8069, "VILLEJUIF GUSTAVE ROUSSY Q2",4,100, 0))
    liste_stations.append((8469, "L'HAI LES ROSES Q1",2, 100))
    liste_stations.append((8469, "L'HAI LES ROSES Q2", 4, 100))
    liste_stations.append((8869, "CHEVILLY LARUE Q1",2, 100))
    liste_stations.append((8869, "CHEVILLY LARUE Q2", 4, 100))
    liste_stations.append((9269, "THIAIS ORLY Q1",2, 100))
    liste_stations.append((9269, "THIAIS ORLY Q2", 4, 100))
    liste_stations.append((9669, "AEROPORT D'ORLY Q1",2, 100))
    liste_stations.append((9669, "AEROPORT D'ORLY Q2", 4, 100))
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
    liste_eguillages.append(( 6390, 130,6420, 100, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND1"))
    liste_eguillages.append((6390, 100, 6420, 130, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND2"))
    liste_eguillages.append(( 6560, 130,6590, 100, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND3"))
    liste_eguillages.append((6560, 100, 6590, 130, 0, "Eg BIBLIOTHEQUE FRANCOIS MITTERRAND4"))
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
    liste_terminus.append((100, 100, "SAINT DENIS PLEYEL1"))
    liste_terminus.append((100, 130, "SAINT DENIS PLEYEL2"))
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
    liste_metro.append(("1",500, -4, 80, 1,"#EB0004" ))



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

    # feu equillage depot
    liste_feu_traffic = []
    liste_feu_traffic.append(("543", 840, 2, 1))
    liste_feu_traffic.append(("521", 840, 4, 1))
    # feu départ saint ouen direction sdp
    liste_feu_traffic.append(("556", 1025, 1, 1))
    # feu départ saint ouen direction ao
    liste_feu_traffic.append(("553", 1085, 4, 1))
    # feu arrivé saint ouen direction sdp
    liste_feu_traffic.append(("554", 1085, 1, 1))
    # feu arrivé saint ouen direction ao
    liste_feu_traffic.append(("551", 1025, 4, 1))

    liste_feu_traffic.append(("552", 1355, 1, 1))

    # feu départ porte de clichy direction mso
    liste_feu_traffic.append(("314", 1445, 1, 1))
    # feu départ porte de clichy direction o
    liste_feu_traffic.append(("314", 1505, 4, 1))
    # feu arrivé porte de clichy direction mso
    liste_feu_traffic.append(("314", 1505, 1, 1))
    # feu arrivé porte de clichy direction o
    liste_feu_traffic.append(("314", 1445, 4, 1))  # changement a continué:
    # feu départ pont cardinet direction mso
    liste_feu_traffic.append(("314", 1695, 1, 1))
    # feu départ pont cardinet direction o
    liste_feu_traffic.append(("314", 1755, 4, 1))
    # feu arrivé pont cardinet direction mso
    liste_feu_traffic.append(("314", 1755, 1, 1))
    # feu arrivé pont cardinet direction o
    liste_feu_traffic.append(("314", 1695, 4, 1))
    # feu départ saint lazare direction mso
    liste_feu_traffic.append(("314", 2115, 1, 1))
    # feu départ saint lazare direction o
    liste_feu_traffic.append(("314", 2175, 4, 1))
    # feu arrivé saint lazare direction mso
    liste_feu_traffic.append(("314", 2175, 1, 1))
    # feu arrivé saint lazare direction o
    liste_feu_traffic.append(("314", 2115, 4, 1))
    # feu départ madeleine direction mso
    liste_feu_traffic.append(("314", 2385, 1, 1))
    # feu départ madeleine direction o
    liste_feu_traffic.append(("314", 2445, 4, 1))
    # feu arrivé madeleine direction mso
    liste_feu_traffic.append(("314", 2445, 1, 1))
    # feu arrivé madeleine direction o
    liste_feu_traffic.append(("314", 2385, 4, 1))
    # feu départ pyramide direction mso
    liste_feu_traffic.append(("314", 3655, 1, 1))
    # feu départ pyramide direction o
    liste_feu_traffic.append(("314", 3715, 4, 1))
    # feu arrivé pyramide direction
    liste_feu_traffic.append(("314", 3715, 1, 1))
    # feu arrivé pyramide direction o
    liste_feu_traffic.append(("314", 3655, 4, 1))
    # feu départ chatelet direction mso
    liste_feu_traffic.append(("314", 4215, 1, 1))
    # feu départ chatelet direction o
    liste_feu_traffic.append(("314", 4275, 4, 1))
    # feu arrivé chatelet direction mso
    liste_feu_traffic.append(("314", 4275, 1, 1))
    # feu arrivé chatelet direction o
    liste_feu_traffic.append(("314", 4215, 4, 1))
    # feu départ gare de lyon direction mso
    liste_feu_traffic.append(("314", 4875, 1, 1))
    # feu départ gare de lyon direction o
    liste_feu_traffic.append(("314", 4935, 4, 1))
    # feu arrivé gare de lyon direction mso
    liste_feu_traffic.append(("314", 4935, 1, 1))
    # feu arrivé gare de lyon direction o
    liste_feu_traffic.append(("314", 4875, 4, 1))
    # feu départ bercy direction mso
    liste_feu_traffic.append(("314", 5335, 1, 1))
    # feu départ bercy direction o
    liste_feu_traffic.append(("314", 5395, 4, 1))
    # feu arrivé bercy direction mso
    liste_feu_traffic.append(("314", 5395, 1, 1))
    # feu arrivé bercy direction o
    liste_feu_traffic.append(("314", 5335, 4, 1))
    # feu départ cour st emillion directio1 mso
    liste_feu_traffic.append(("314", 5895, 1, 1))
    # feu départ cour st emillion direction o
    liste_feu_traffic.append(("314", 5955, 4, 1))
    # feu arrivé cour st emillion directio1 mso
    liste_feu_traffic.append(("314", 5955, 1, 1))
    # feu arrivé cour st emillion direction o
    liste_feu_traffic.append(("314", 5895, 4, 1))
    # feu départ bibliotheque francois mitterand direction mso
    liste_feu_traffic.append(("314", 6472, 1, 1))
    # feu départ bibliotheque francois mitterand direction o
    liste_feu_traffic.append(("314", 6532, 4, 1))
    # feu arrivé bibliotheque francois mitterand direction mso
    liste_feu_traffic.append(("314", 6532, 1, 1))
    # feu arrivé bibliotheque francois mitterand direction o
    liste_feu_traffic.append(("314", 6472, 4, 1))
    # feu départ olympiade direction mso
    liste_feu_traffic.append(("314", 6869, 1, 1))
    # feu départ olympiade direction o
    liste_feu_traffic.append(("314", 6929, 4, 1))
    # feu arrivé olympiade direction mso
    liste_feu_traffic.append(("314", 6929, 1, 1))
    # feu arrivé olympiade direction o
    liste_feu_traffic.append(("314", 6869, 4, 1))
    # feu eguillage olympiade
    liste_feu_traffic.append(("314", 7000, 1, 1))
    liste_feu_traffic.append(("314", 7000, 4, 1))
    # feu eguillage maison blanche
    liste_feu_traffic.append(("314", 7269, 1, 1))
    liste_feu_traffic.append(("314", 7330, 4, 1))
    liste_feu_traffic.append(("314", 7330, 1, 1))
    liste_feu_traffic.append(("314", 7269, 4, 1))
    # feu eguillage hopital bicetre
    liste_feu_traffic.append(("314", 7669, 1, 1))
    liste_feu_traffic.append(("314", 7730, 4, 1))
    liste_feu_traffic.append(("314", 7730, 1, 1))
    liste_feu_traffic.append(("314", 7669, 4, 1))
    # feu eguillage villejuif gustave roussy
    liste_feu_traffic.append(("314", 8069, 1, 1))
    liste_feu_traffic.append(("314", 8130, 4, 1))
    liste_feu_traffic.append(("314", 8130, 1, 1))
    liste_feu_traffic.append(("314", 8069, 4, 1))
    # feu eguillage l'hai les roses
    liste_feu_traffic.append(("314", 8469, 1, 1))
    liste_feu_traffic.append(("314", 8530, 4, 1))
    liste_feu_traffic.append(("314", 8530, 1, 1))
    liste_feu_traffic.append(("314", 8469, 4, 1))
    # feu eguillage chevilly la rue
    liste_feu_traffic.append(("314", 8869, 1, 1))
    liste_feu_traffic.append(("314", 8930, 4, 1))
    liste_feu_traffic.append(("314", 8930, 1, 1))
    liste_feu_traffic.append(("314", 8869, 4, 1))
    # feu eguillage thiais orly
    liste_feu_traffic.append(("314", 9269, 1, 1))
    liste_feu_traffic.append(("314", 9330, 4, 1))
    liste_feu_traffic.append(("314", 9330, 1, 1))
    liste_feu_traffic.append(("314", 9269, 4, 1))
    # feu eguillage aéroport d'orly direction aéroport d'orly
    liste_feu_traffic.append(("314", 9669, 4, 1))
    liste_feu_traffic.append(("314", 9730, 4, 1))
    # feu eguillage aéroport d'orly direction saint denis pleyel
    liste_feu_traffic.append(("314", 9669, 1, 1))
    liste_feu_traffic.append(("314", 9730, 1, 1))
    # feu eguillage terminus aéroport d'orly
    liste_feu_traffic.append(("314", 9830, 1, 1))
    liste_feu_traffic.append(("314", 9760, 1, 1))
    liste_feu_traffic.append(("314", 9830, 4, 1))
    liste_feu_traffic.append(("314", 9760, 4, 1))
    # feu depot
    liste_feu_traffic.append(("314", 985, 5, 1))
    liste_feu_traffic.append(("314", 985, 6, 1))
    liste_feu_traffic.append(("314", 1100, 7, 1))
    liste_feu_traffic.append(("314", 1100, 8, 1))


