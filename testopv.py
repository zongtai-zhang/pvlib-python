import numpy as np

from scipy import constants
from scipy import optimize
from scipy.special import lambertw

from pvlib.pvsystem import calcparams_pvsyst, singlediode, v_from_i
from pvlib.singlediode import bishop88_mpp

from pvlib.ivtools.utils import rectify_iv_curve, _numdiff
from pvlib.ivtools.sde import _fit_sandia_cocontent
from pvlib.ivtools.sdm import fit_desoto

from pvlib.tools import _first_order_centered_difference


v_mp = 46.9 
i_mp = 4.69 
v_oc = 59.4
i_sc = 5.1
alpha_sc = 0.004539 
beta_voc = -0.22216  
cells_in_series = 60


fit_desoto(v_mp, i_mp, v_oc, i_sc, alpha_sc, beta_voc, cells_in_series, EgRef=1.121, dEgdT=- 0.0002677, temp_ref=25, irrad_ref=1000, root_kwargs={})
