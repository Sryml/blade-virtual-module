import typing
import os
import Bladex

"""
NodeType
ParticleType
BodList

entity
knight
RasterMode
rel2abs

"""
o=Bladex.CreateEntity("obj1","Entity Particle System Dperson",0, 0, 0)
o.PersonNodeName="Head"
o.ParticleType="BladeSwordMissile"
char=Bladex.GetEntity("Player1")
char.RasterMode="AdditiveAlpha"

def bar1(name, kind, x, y, z, class_=""):
    o = Bladex.CreateEntity(name, kind, x, y, z, class_)
    # o.Actor


bar = Bladex.GetCharType("", "")
bar.AllowAttack("", "", "", "", "", "1H")

x = Bladex.CreateMaterial("")
s = Bladex.CreateSound("../../Sounds/cambio-armadura2.wav", "testsnd")

o1 = Bladex.CreateEntity("", "", 0, 0, 0)
o2 = Bladex.CreateEntity("", "", 0, 0, 0, "Actor")
o3 = Bladex.CreateEntity("", "FireAxe", 0, 0, 0, "Weapon")
o4 = Bladex.CreateEntity("", "", 0, 0, 0, "Person")

o5 = Bladex.CreateEntity("", "", 0, 0, 0, "Physic")
o1.Lights = [(1, 3, (0, 0, 100))]
o4.AddAnmEventFunc
o4.UseFunc
o6 = Bladex.CreateEntity("", "Entity Aura", 0, 0, 0)
o7 = Bladex.CreateEntity("", "Entity Camera", 0, 0, 0)
o8 = Bladex.CreateEntity("", "Entity Dynamic Fire", 0, 0, 0)
o9 = Bladex.CreateEntity("", "Entity Fire", 0, 0, 0)
o10 = Bladex.CreateEntity("", "Entity Lava", 0, 0, 0)
o11 = Bladex.CreateEntity("", "Entity Magic Missile", 0, 0, 0)
o12 = Bladex.CreateEntity("", "Entity Particle System D1", 0, 0, 0)
o12.ParticleType

o13 = Bladex.CreateEntity("", "Entity Particle System D2", 0, 0, 0)
o14 = Bladex.CreateEntity("", "Entity Particle System D3", 0, 0, 0)
o15 = Bladex.CreateEntity("", "Entity Particle System Dobj", 0, 0, 0)
o16 = Bladex.CreateEntity("", "Entity Particle System Dperson", 0, 0, 0)
o17 = Bladex.CreateEntity("", "Entity Particle", 0, 0, 0)
o18 = Bladex.CreateEntity("", "Entity Pool", 0, 0, 0)
o19 = Bladex.CreateEntity("", "Entity Sliding Area", 0, 0, 0)
o20 = Bladex.CreateEntity("", "Entity Sound", 0, 0, 0)
o20.SetSound("../../Sounds/M-CREAKCUERDA-3b.wav")
o21 = Bladex.CreateEntity("", "Entity Spot", 0, 0, 0)
o22 = Bladex.CreateEntity("", "Entity Water", 0, 0, 0)
o23 = Bladex.CreateEntity("", "Entity ElectricBolt", 0, 0, 0)

og1 = Bladex.GetEntity("Camera")
og2 = Bladex.GetEntity("Player1")
og3 = Bladex.GetEntity("1")
inv = o1.GetInventory()
inv.AddWeapon

o = Bladex.CreateEntity("Knight_N", "Knight_N", 0, 0, 0.1, "Person")
o.RasterMode
o.Name
o.RasterModeZ
o.Data = "q"
o.Data

b = o.Abs2RelPoint
o.MessageEvent

# fmt:off
# print 3
xxx =3
# fmt:on
xxx4 = 5
# xd3=Bladex.CreateEntity(None,"",0,0,0)

if 1:

    def QuakeStep(personaje):
        print(personaje)

    char.OnStepFunc = QuakeStep

o2 = Bladex.CreateEntity("FireSword", "FireSword", 0, 0, 0.1, "Weapon")
# s=Bladex.CreateEntity("FireSword","FireSword",0,0,0.1,"Static")
# p=Bladex.CreateEntity("FireSword","FireSword",0,0,0.1,"Physic")
# o=Bladex.CreateEntity("Knight_N","Knight_N",0,0,0.1,"Client")
o = Bladex.CreateEntity("Knight_N", "Knight_N", 0, 0, 0.1, "Actor")
# o=Bladex.CreateEntity("Knight_N","Entity Weapon",0,0,0.1)
# o2.AAA


class foo:
    __a = 3
    b = __a

    def func(self):
        import os

        print(foo.__a, foo.b)


class foo2(foo):
    def __init__(self) -> None:
        super().__init__()


a: str

A = typing.TypeVar("A", str, bytes)


def longest(x: A, y: A) -> A:
    return x if len(x) >= len(y) else y


@typing.overload
def abc(a) -> str:
    ...


@typing.overload
def abc(a: int) -> list:
    ...


def abc(a) -> typing.Union[list, str]:
    ...


def fxxx(ef3):
    # type: (str)->Any
    xxxx = abc(ef3)


def my_function():
    print("This line has incorrect indentation")


import os
import sys
if 1:
    snd = Bladex.CreateSound("./YourRecordedVoice.mp3","YourRecordedVoice")
    bg_snd = Bladex.CreateSound("./BackgroundSound.mp3","BackgroundSound")
    snd.PlayStereo()
    bg_snd.PlayStereo()
