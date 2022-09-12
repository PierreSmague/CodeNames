from gensim.models import KeyedVectors
from functions import *

model = KeyedVectors.load_word2vec_format("vecsfr_poids.bin", binary=True, unicode_errors="ignore")

liste_equipe = ["tonnerre_n", "pingouin_n", "blé_n", "colonie_n", "mammouth_n", "voeu_n", "beethoven_n", "main_n"]
liste_adversaire = ["service_n", "physique_n", "piste_n", "corbeau_n", "épée_n", "cycle_n", "chanteur_n", "pêche_n", "jeu_n"]
liste_neutre = ["cocon_n", "dinosaure_n", "visage_n", "ensemble_n", "amérique_n", "sahara_n", "branche_n"]
mot_noir = "barrière_n"

print(mot_indice(model, liste_adversaire, liste_equipe, liste_neutre, mot_noir))

# print(explication_mot("loisir_n", model, liste_adversaire, liste_equipe, liste_neutre, mot_noir))
