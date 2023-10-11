from __future__ import annotations

from .b_types import *


class B_PyInventory:
    def __init__(self) -> None:
        self.__HasBow: Bool
        self.__HasBowOnBack: Bool
        self.__HasShieldOnBack: Bool
        self.__HoldingBow: Bool
        self.__HoldingShield: Bool
        self.maxObjects: int
        self.maxQuivers: int
        self.maxShields: int
        self.maxWeapons: int
        self.__Name: str
        self.__nKeys: int
        self.__nKindObjects: int
        self.__nObjects: int
        self.__nQuivers: int
        self.__nShields: int
        self.__nSpecialKeys: int
        self.__nTablets: int
        self.__nWeapons: int
        self.__Owner: str

    @property
    def HasBow(self):
        """*read only*"""
        return self.__HasBow

    @property
    def HasBowOnBack(self):
        """*read only*"""
        return self.__HasBowOnBack

    @property
    def HasShieldOnBack(self):
        """*read only*"""
        return self.__HasShieldOnBack

    @property
    def HoldingBow(self):
        """*read only*"""
        return self.__HoldingBow

    @property
    def HoldingShield(self):
        """*read only*"""
        return self.__HoldingShield

    @property
    def Name(self):
        """*read only*"""
        return self.__Name

    @property
    def nKeys(self):
        """*read only*"""
        return self.__nKeys

    @property
    def nKindObjects(self):
        """*read only*"""
        return self.__nKindObjects

    @property
    def nObjects(self):
        """*read only*"""
        return self.__nObjects

    @property
    def nQuivers(self):
        """*read only*"""
        return self.__nQuivers

    @property
    def nShields(self):
        """*read only*"""
        return self.__nShields

    @property
    def nSpecialKeys(self):
        """*read only*"""
        return self.__nSpecialKeys

    @property
    def nTablets(self):
        """*read only*"""
        return self.__nTablets

    @property
    def nWeapons(self):
        """*read only*"""
        return self.__nWeapons

    @property
    def Owner(self):
        """*read only*"""
        return self.__Owner

    def AddBow(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddKey(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddMagicShield(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddObject(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddQuiver(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddShield(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddSpecialKey(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddTablet(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddWeapon(self, weapon_name: str, flag: Literal[0, 1, 2, 3] = 0) -> int:
        """
        :flag:
            W_FLAG_1H = 0  # One handed _whatever_ weapon\n
            W_FLAG_2W = 1  # Two handed sword\n
            W_FLAG_AXE = 2  # Two handed axw\n
            W_FLAG_SP = 3  # Two handed spear
        """
        ...

    def CarringObject(self, obj_name: str) -> int:
        """"""
        ...

    def CycleKeys(self) -> None:
        """"""
        ...

    def CycleObjects(self) -> None:
        """"""
        ...

    def CycleQuivers(self) -> None:
        """"""
        ...

    def CycleShields(self) -> None:
        """"""
        ...

    def CycleWeapons(self) -> None:
        """"""
        ...

    def GetActiveQuiver(self) -> str:
        """"""
        ...

    def GetActiveShield(self) -> str:
        """"""
        ...

    def GetActiveWeapon(self) -> str:
        """"""
        ...

    def GetBow(self) -> str:
        """"""
        ...

    def GetKey(self, obj: Union[int, str]) -> str:
        """"""
        ...

    def GetLeftBack(self) -> str:
        """"""
        ...

    def GetMagicShield(self) -> str:
        """"""
        ...

    def GetMaxNumberObjectsAt(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetNumberObjectsAt(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetObject(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetQuiver(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetRightBack(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetSelectedKey(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetSelectedObject(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetSelectedQuiver(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetSelectedShield(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetSelectedWeapon(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetShield(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetSpecialKey(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetTablet(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def GetWeapon(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def IsKeySelected(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def IsObjectSelected(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def IsQuiverSelected(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def IsShieldSelected(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def IsWeaponSelected(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkBack(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkLeft(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkLeftBack(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkLeftHand(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkLeftHand2(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkRight(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkRightBack(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def LinkRightHand(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveBow(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveKey(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveMagicShield(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveObject(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveQuiver(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveShield(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveSpecialKey(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveTablet(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def RemoveWeapon(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...

    def SetCurrentQuiver(self, *args: todo, **kwargs: todo) -> todo:
        """"""
        ...
