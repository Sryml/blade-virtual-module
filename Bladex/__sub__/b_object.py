from __future__ import annotations

from .b_types import *
from . import entity


class B_PyMaterial:
    def __init__(self) -> None:
        self.BreakSound: B_PySound
        self.FrictionSound: B_PySound
        self.HitSound: B_PySound
        self.__Name: str
        self.Weight: float

    @property
    def Name(self):
        return self.__Name

    def AddHitSoundComb(self, material_name: str, sound: B_PySound) -> Bool:
        ...


class B_PyRoute:
    def __init__(self) -> None:
        ...

    def AddPoint(self, x: float, y: float, z: float) -> Literal[1]:
        ...


class B_PySound:
    def __init__(self) -> None:
        self.BaseVolume: float
        self.MaxDistance: float
        self.MinDistance: float
        self.__Name: str
        self.Pitch: float
        self.Scale: float
        self.SendNotify: Bool
        self.Volume: float

    @property
    def Name(self):
        return self.__Name

    def AddAltSound(self, alt_sound: str) -> Bool:
        ...

    def Play(self, x: float, y: float, z: float, cycles: int = 0) -> Bool:
        ...

    def PlayStereo(self, cycles: int = 0) -> Bool:
        ...

    def SetPitchVar(
        self,
        i_unknown: int,
        f_unknown1: float,
        f_unknown2: float,
        f_unknown3: float,
        f_unknown4: float,
    ) -> Literal[1]:
        ...

    def Stop(self) -> Bool:
        ...
