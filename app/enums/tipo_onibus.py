from enum import Enum


class TipoOnibus(str, Enum):
    LEITO = "leito"
    SEMILEITO = "semileito"
    EXECUTIVO = "executivo"
