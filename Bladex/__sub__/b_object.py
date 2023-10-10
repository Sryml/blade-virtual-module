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


class B_PySector:
    def __init__(self) -> None:
        pass

    def DoBreak(
        self,
        impulse: Vector3,
        pos: Vector3,
        unknown: Vector3,
    ) -> Bool:
        ...

    def GetSelfLight(self, surface_index: int) -> float:
        ...

    def GetSpecularLight(self, surface_index: int) -> float:
        ...

    def GetSpecularShininess(self, surface_index: int) -> float:
        ...

    def GetSurfaceTexture(self, surface_index: int) -> str:
        ...

    def GetSurfaceTextureX(self, surface_index: int) -> float:
        ...

    def GetSurfaceTextureY(self, surface_index: int) -> float:
        ...

    def GetSurfaceTextureZoomX(self, surface_index: int) -> float:
        ...

    def GetSurfaceTextureZoomY(self, surface_index: int) -> float:
        ...

    def InitBreak(
        self,
        vec1: Vector3,
        vec2: Vector3,
        vec3: Vector3,
        sound_name: str,
        unknown1: float,
        unknown2: int,
    ) -> Bool:
        ...

    def SetSelfLight(self, surface_index: int, self_light: str) -> Bool:
        ...

    def SetSpecularLight(self, surface_index: int, specular_light: str) -> Bool:
        ...

    def SetSpecularShininess(self, surface_index: int, specular_shininess: str) -> Bool:
        ...

    def SetSurfaceTexture(self, surface_index: int, texture: str) -> Bool:
        ...

    def SetSurfaceTextureX(self, surface_index: int, texture_x: float) -> Bool:
        ...

    def SetSurfaceTextureY(self, surface_index: int, texture_y: float) -> Bool:
        ...

    def SetSurfaceTextureZoomX(self, surface_index: int, zoom_x: float) -> Bool:
        ...

    def SetSurfaceTextureZoomY(self, surface_index: int, zoom_y: float) -> Bool:
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


class B_PyTrail:
    def __init__(self) -> None:
        self.Color: RGBColor
        self.ShrinkFactor: float
        self.Time2Live: float
        self.Transparency: float
