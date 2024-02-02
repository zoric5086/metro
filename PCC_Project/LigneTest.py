class ClasseLigne0():
    #Position Station(x, nom, ligne de haut en base)
    liste_stations = []
    liste_stations.append((150, "station1", 3, 150))
    liste_stations.append((650, "station2", 3, 150))



    liste_eguillages = []
    liste_eguillages.append((60,130,90, 100, 2, "Egstation1 1"))
    liste_eguillages.append((100, 100, 130, 130, 0, "Egstation1 2"))
    liste_eguillages.append((525, 100, 555, 130, 0, "Eg esplanade de la défense"))
    liste_eguillages.append(( 730, 130, 760, 100, 1, "Eg station2"))
    liste_eguillages.append((730, 100,760, 130, 0, "Eg station2"))



    liste_terminus = []
    liste_terminus.append((10, 100, "TERMINUS LA DEFENSE 1"))
    liste_terminus.append((10, 130, "TERMINUS LA DEFENSE 1"))
    liste_terminus.append((800, 100, "CHATEAU DE VINCENNES 1"))
    liste_terminus.append((800, 130, "CHATEAU DE VINCENNES 2"))


    liste_metro = []
    liste_metro.append(("Train 1", 10,  2, 80,1,"#FFCC45" ))
    liste_metro.append(("Train 2",430, -2, 50, 1,"#FFCC45" ))
    liste_metro.append(("Train 3", 40,  -2, 50,1,"#FFCC45" ))
    liste_metro.append(("Train 4",430, 2, 80, 1,"#FFCC45" ))
    liste_metro.append(("Train 5", 200,  -2, 50,1,"#FFCC45" ))
    liste_metro.append(("Train 6",200, 2, 80, 1,"#FFCC45" ))


    liste_lignes = []
    liste_lignes.append((10, 100, 850, 100, "#FCFF42", 2))
    liste_lignes.append((10, 130, 850, 130, "#FCFF42", 2))

    liste_feu_traffic = []
    # feu eguillage terminus porte de cligancourt
    liste_feu_traffic.append((260, 50, 2))