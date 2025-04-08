class ClasseLigne0():
    #x, nom, offset=ligne, position H/B temps arret
    liste_stations = []
    liste_stations.append((350, "SAINT DENIS PLEYEL Q1", 1, "H", 500))
    liste_stations.append((350, "SAINT DENIS PLEYEL Q2", 2, "B", 500))
    liste_stations.append((650, "MAIRIE DE SAINT-OUEN Q1", 1, "H", 500))
    liste_stations.append((650, "MAIRIE DE SAINT-OUEN Q2", 2, "B", 500))

    liste_eguillages = []
    liste_eguillages.append((110, 2, 140, 1, 0, "Eg SAINT DENIS PLEYEL1","#EBEBEB"))
    liste_eguillages.append((110, 1, 140, 2, 0, "Eg SAINT DENIS PLEYEL2","#EBEBEB"))
    liste_eguillages.append((290,1, 260, 2, 2, "Eg SAINT DENIS PLEYEL3","#EBEBEB"))
    liste_eguillages.append((260, 1, 290, 2, 0, "Eg SAINT DENIS PLEYEL4","#EBEBEB"))
    liste_eguillages.append((730,2,760, 1, 2, "Eg MAIRIE DE SAINT OUEN1","#EBEBEB"))
    liste_eguillages.append((730, 1, 760, 2, 0, "Eg MAIRIE DE SAINT OUEN2","#EBEBEB"))

    liste_terminus = []
    liste_terminus.append((200, 1, "SAINT DENIS PLEYEL1",1))
    liste_terminus.append((200, 2, "SAINT DENIS PLEYEL2",1))
    liste_terminus.append((800, 1, "MAIRIE DE SAINT OUEN1", 1))
    liste_terminus.append((800, 2, "MAIRIE DE SAINT OUEN2", 1))


    liste_metro = []
    #train direction chateau de vincennes

    liste_metro.append(("1", 500, 0.2, 2, 1, "#EB0004"))
    liste_metro.append(("2", 600, -0.2, 1, 1, "#EB0004"))


    liste_lignes = []
    # Offset, x debut, x fin, couleur, largeur
    liste_lignes.append((1,250, 900, "#EBEBEB", 3))
    liste_lignes.append((2,250, 900,  "#EBEBEB", 3))


    liste_depot_eguillage = []




    liste_depot_ligne = []
     #ligne depot

    liste_depot_ligne.append((1, 10,  250,  "#CCCCCC", 2))
    liste_depot_ligne.append((2, 10, 250,  "#CCCCCC", 2))

    # feu equillage depot
    liste_feu_traffic = []
    #Nom, X, Offset Ligne, "H"=haut / "B"=bas, 1=vert 2=rouge
    liste_feu_traffic.append(("543", 840, 1, "H", 1))
    liste_feu_traffic.append(("521", 840, 2, "B", 1))


