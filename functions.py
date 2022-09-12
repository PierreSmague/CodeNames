def fonction_eval(vect_equipe, vect_adv, vect_neutre, mot_noir_simil):
    eval_equipe = 0
    eval_adv = 0
    eval_neutre = 0
    for i in range(0, len(vect_equipe)):
        if vect_equipe[i] > 0.15:
            eval_equipe += (0.7 * i + 1) * vect_equipe[i]
    for i in range(0, len(vect_adv)):
        if vect_adv[i] > 0.13:
            eval_adv += (2 - 0.5 * i) * vect_adv[i]
    for i in range(0, len(vect_neutre)):
        if vect_neutre[i] > 0.13:
            eval_neutre += (2 - 0.5 * i) * vect_neutre[i]
            
    eval_globale_mot = round(eval_equipe - 0.8 * eval_adv - 0.4 * eval_neutre - 3 * mot_noir_simil * (mot_noir_simil > 0.08), 2)

    return [eval_globale_mot, eval_equipe, eval_adv, eval_neutre, mot_noir_simil]

def mot_indice(model, liste_equipe = [], liste_adversaire = [], liste_neutre = [], mot_noir = "", nbre_indices = 1):
    
    mots_candidats = [["", -100]] * 10
    inter_vector = []
    inter_vector_adv = []
    inter_vector_neutre = []
    
    for word_tested in model.index_to_key[0:50000]:
        if (word_tested[-1] in ["n", "v", "a"]) and (word_tested not in ["être_v", "avoir_v"]) and (word_tested not in liste_equipe):
            mot_noir_simil = model.similarity(mot_noir, word_tested)
            for word in liste_equipe:
                inter_vector.append(model.similarity(word, word_tested))
                inter_vector.sort(reverse=True)
            for word in liste_adversaire:
                inter_vector_adv.append(model.similarity(word, word_tested))
                inter_vector_adv.sort(reverse=True)
            for word in liste_neutre:
                inter_vector_neutre.append(model.similarity(word, word_tested))
                inter_vector_neutre.sort(reverse=True)
    
            eval_mot = fonction_eval(inter_vector, inter_vector_adv, inter_vector_neutre, mot_noir_simil)[0]
            if eval_mot > mots_candidats[9][1]:
                mots_candidats[9] = [word_tested, eval_mot]
                mots_candidats.sort(key=lambda x: x[1], reverse=True)
                print(mots_candidats)


        inter_vector = []
        inter_vector_adv = []
        inter_vector_neutre = []
                
    return mots_candidats

def explication_mot(mot, model, liste_equipe, liste_adversaire, liste_neutre, mot_noir):
    mot_noir_simil = model.similarity(mot_noir, mot)
    inter_vector = []
    explain_vector = []
    inter_vector_adv = []
    inter_vector_neutre = []
    for word in liste_equipe:
        inter_vector.append(model.similarity(word, mot))
        inter_vector.sort(reverse=True)
    for word in liste_adversaire:
        inter_vector_adv.append(model.similarity(word, mot))
        inter_vector_adv.sort(reverse=True)
    for word in liste_neutre:
        inter_vector_neutre.append(model.similarity(word, mot))
        inter_vector_neutre.sort(reverse=True)
    
    for word in liste_equipe:
        explain_vector.append([word, model.similarity(word, mot)])
    
    print(fonction_eval(inter_vector, inter_vector_adv, inter_vector_neutre, mot_noir_simil))
    print(explain_vector)

