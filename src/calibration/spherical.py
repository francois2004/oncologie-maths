"""
Calibration pour le 1er modèle, tumeur sphérique. 
"""
import numpy as np
import nibabel as nib

from src.utils.dataloader import Loader

def estimate_radius(mask, voxel_spacing, method = "spherical", q = .95):
    """
    Retourne le rayon de la partie considérée de la tumeur, selon la méthode pris en entrée. 

    Paramètres 
    ----------
    mask : tableau 3D booléen
        True = région segmentée
        False = extérieur

    voxel_spacing : tuple
        taille d’un voxel, par exemple (sx, sy, sz) en mm

    method : str
        méthode choisie pour convertir la région 3D en rayon

    q : float
        quantile choisi pour la méthode "quantile"
    """
    nb_cells = mask.sum()
    if nb_cells == 0:
        raise ValueError("Empty mask")
    space_x, space_y, space_z = voxel_spacing
    vol_cell = space_x * space_y * space_z

    if method == "spherical":
        vol = nb_cells * vol_cell
        R = (3*vol / (4*np.pi))**(1/3)
    if method == "quantile": 
        coords = np.argwhere(mask)
        coords_mm = coords * np.array(voxel_spacing)
        center_mm = coords_mm.mean(axis = 0)
        distances = np.linalg.norm(coords_mm - center_mm, axis = 1)
        R = np.quantile(distances, q)
    else : 
        raise ValueError("methode non reconnue")

    return R



def derivated_quantities(R0, R1, R2): 
    """
    Calcule les quantités dérivées d'un IRM, 
    dans un cadre où la tumeur est considérée comme sphérique. 

    Paramètres
    ----------
    R0 : float
        rayon nécrose
    R1 : float
        rayon zone contrastée
    R2 : float
        rayon oedème
    """
    L1 = R1 - R0
    if L1 < 0: 
        raise ValueError("R1 < R0, incohérent avec notre modélisation")
    L2 = R2 - R1
    if L2 < 0:
        raise ValueError("R2 < R1, incohérent avec notre modélisation")
    return L1, L2

