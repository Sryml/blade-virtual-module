import typing
from typing import (
    List,
    Tuple,
    Dict,
    Any,
    AnyStr,
    Callable,
    Union,
    Optional,
    Literal,
    overload,
)

Int = Union[int, float]
Bool = Union[bool, Literal[0, 1]]
Vector3 = Tuple[float, float, float]
Quaternion = Tuple[float, float, float, float]
RGBColor = Tuple[int, int, int]
# Any_ = Union[Any, None]
Unknown = str_ = Any
Radian = float

NodeType = Literal[
    "Center",
    "Chest",
    "Head",
    "R_Shoulder",
    "R_Arm",
    "R_Elbow",
    "R_Forearm",
    "R_Wrist",
    "R_Hand",
    "L_Shoulder",
    "L_Arm",
    "L_Elbow",
    "L_Forearm",
    "L_Wrist",
    "L_Hand",
    "R_Ass",
    "R_Leg",
    "R_Knee",
    "R_Boot",
    "R_Foot",
    "L_Ass",
    "L_Leg",
    "L_Knee",
    "L_Boot",
    "L_Foot",
]

Builtin_Kind = Literal[
    "Entity Aura",
    "Entity Camera",
    "Entity Dynamic Fire",
    "Entity ElectricBolt",
    "Entity Fire",
    "Entity Lava",
    "Entity Magic Missile",
    "Entity Particle",
    "Entity Particle System D1",
    "Entity Particle System D2",
    "Entity Particle System D3",
    "Entity Particle System Dobj",
    "Entity Particle System Dperson",
    "Entity Pool",
    "Entity Sliding Area",
    "Entity Sound",
    "Entity Spot",
    "Entity Water",
]

ParticleType = Literal[
    "AnkBlood",
    "BigFire",
    "BladeSwordMissile",
    "Blood",
    "BlueMagicMissile",
    "BlueSpark",
    "BlueTrail",
    "BrillosBladeSword",
    "DGLevelUpParticle",
    "DGLifeUpEnergyConc",
    "DLLevelUpParticle",
    "DLLifeUpEnergyConc",
    "DarkSmoke",
    "DeathCloud",
    "DeepGreenEnergyConc",
    "DeepGreenMagicMissile",
    "DeepOrangeEnergyConc",
    "DeepOrangeMagicMissile",
    "DeepRedEnergyConc",
    "DeepRedMagicMissile",
    "DemonShield",
    "Dust",
    "Energia2",
    "Energia3",
    "EnergyConc",
    "EnergyDissip",
    "FastEnergyConc",
    "FastRedEnergyConc",
    "Fire",
    "Flame",
    "FuegoInvocacion",
    "GDLevelUpParticle",
    "GDLifeUpEnergyConc",
    "GasVenenoso",
    "GasVenenoso2",
    "GotasSangre",
    "GreenBlood",
    "GreenFire",
    "GreenTrail",
    "GreyBlood",
    "LargeDust",
    "LargeFire",
    "LargeFlame",
    "LevelUpParticle",
    "LittleBlueEnergyConc",
    "LittleBlueSpark",
    "LittleDeepOrangeMagicMissile",
    "LittleEnergyDissip",
    "Llamita",
    "Llamita2",
    "LucesCools",
    "MediumDust",
    "Miguillas",
    "MulticolourEnergyDissip",
    "RedMagicMissile",
    "RedTrail",
    "SacredFX",
    "Sand",
    "ShitSmoke",
    "Smoke",
    "SnowDust",
    "Splinter",
    "Vaho",
    "Venom",
    "VenomSmoke",
    "Vomit",
    "WhiteTrail",
    "YellowTrail",
]

BodList = Literal[
    "Amz_Bng",
    "Amazon_L",
    "Amazon_N",
    "AmzSkin1",
    "DarkLord",
    "Ank2",
    "Ank_Bng",
    "Barbarian",
    "Bar_Bng",
    "Barbarian_L",
    "Barbarian_N",
    "BarSkin1",
    "Bat",
    "ChaosKnight",
    "Chk_Bng",
    "Cos",
    "Cos_Bng",
    "Crw",
    "DalGurak",
    "Dgk_Bng",
    "Dark_Knight",
    "Dkn_Bng",
    "Dark_Ork",
    "Dok_Bng",
    "Dragon",
    "Dwf_Bng",
    "Dwarf_L",
    "Dwarf_M",
    "Dwarf_N",
    "DwfSkin1",
    "Ena_Bng",
    "Enano1",
    "Enano2",
    "Enano3",
    "Enano4",
    "Gargoyle_Stone_Form",
    "Great_Demon",
    "Gdm_Bng",
    "Glm_Bng",
    "Golem_clay",
    "Golem_lava",
    "Golem_metal",
    "Golem_stone",
    "Great_Ork",
    "Gok_Bng",
    "Kgt_Bng",
    "Knight_F",
    "Knight_L",
    "Knight_M",
    "Knight_N",
    "Knight_traitor",
    "KgtSkin1",
    "Lich",
    "Lch_Bng",
    "Little_Demon",
    "Ldm_Bng",
    "Minotaur",
    "Min_Bng",
    "Gold_Ork",
    "Org_Bng",
    "Ork",
    "Ork_Bng",
    "Pio",
    "Prisoner_1",
    "Prisoner_2",
    "Prisoner_3",
    "Prisoner_4",
    "Prisoner_5",
    "Prisoner_6",
    "Prs_Bng",
    "Rat",
    "Ragnar",
    "Rgn_Bng",
    "Sgl",
    "Shank",
    "Shn_Bng",
    "Skeleton",
    "Skl_Bng",
    "Skeleton_Optimiced",
    "Salamander",
    "Slm_Bng",
    "Spidersmall",
    "Spd_Bng",
    "Knight_Traitor",
    "Tkn_Bng",
    "Trl_Bng",
    "Troll_Dark",
    "Troll_snow",
    "Vejete",
    "Vamp",
    "Vmp_Bng",
    "Wyvern",
    "Knight_Zombie",
    "Zkn_Bng",
    "Duque",
    "Mortimer",
    "NP_Knight",
    "Golem_ice",
    "BarSkin2",
    "KgtSkin2",
    "AmzSkin2",
    "DwfSkin2",
    "Adoquinpulsador",
    "Adoquinpulsador2",
    "AdoquinRuna",
    "AdoquinRuna2",
    "AdoquinRuna3",
    "Agarramanos",
    "Agarrapies",
    "Alabarda",
    "AlabardaPieza1",
    "AlabardaPieza2",
    "Alfanje",
    "AlfanjePieza1",
    "AlfanjePieza2",
    "AlfanjePieza3",
    "Alfeizar",
    "Alforjas",
    "Altar",
    "AltarPieza1",
    "AltarPieza10",
    "AltarPieza11",
    "AltarPieza12",
    "AltarPieza13",
    "AltarPieza14",
    "AltarPieza15",
    "AltarPieza16",
    "AltarPieza17",
    "AltarPieza18",
    "AltarPieza19",
    "AltarPieza2",
    "AltarPieza20",
    "AltarPieza3",
    "AltarPieza4",
    "AltarPieza5",
    "AltarPieza6",
    "AltarPieza7",
    "AltarPieza8",
    "AltarPieza9",
    "Amuletofantasma",
    "Amuleto",
    "Amuletoserpiente",
    "Amazon_Head",
    "AnilloFoso",
    "AntorchaAtlante",
    "Antidoto",
    "Antorcha2",
    "Antorcha",
    "Lamparacobra",
    "Antorchaenpared",
    "ArbolNevado2",
    "Arbolseco",
    "Arbolseco2",
    "Arco",
    "Arco2",
    "Arco3",
    "Arco_Amz_seleccion",
    "Argolla",
    "Armadura",
    "ArmaduraAmazonaLigera",
    "ArmaduraBarbaroLigera",
    "ArmaduraEnanoLigera",
    "ArmaduraEnanoMedia",
    "ArmaduraCaballeroCompleta",
    "ArmaduraCaballeroLigera",
    "ArmaduraCaballeroMedia",
    "ArmaduraBlade",
    "Armero",
    "Armero2",
    "Armero2Pieza1",
    "Armero2Pieza2",
    "Armero2Pieza3",
    "Armero2Pieza4",
    "Armero2Pieza5",
    "ArmeroPieza1",
    "ArmeroPieza2",
    "ArmeroPieza3",
    "ArmeroPieza4",
    "AroMagico",
    "Arpon",
    "ArponPieza1",
    "ArponPieza2",
    "ArponPieza3",
    "ArponPieza4",
    "Atril",
    "Axe_Dwf_seleccion",
    "Axpear",
    "AxpearPieza1",
    "AxpearPieza2",
    "AxpearPieza3",
    "AxpearPieza4",
    "Baldosa_01",
    "Baldosa_rota",
    "Banco",
    "BancoPieza1",
    "BancoPieza2",
    "BancoPieza3",
    "BancoPieza4",
    "Bandeja",
    "Barbarian_Head_1",
    "Barbarian_Head_2",
    "BarroteAurelio",
    "Barril",
    "BaseCono",
    "Baston",
    "Baston2",
    "Baston3",
    "Bichero",
    "BicheroPieza1",
    "BicheroPieza2",
    "BicheroPieza3",
    "BigSword",
    "BigSwordPieza1",
    "BigSwordPieza2",
    "BigSwordPieza3",
    "LlaveNegra",
    "BladeSword",
    "BladeSword2",
    "BladeSword2Barbarian",
    "BladeSword2Poly",
    "BladeSwordBarbarian",
    "BladeSwordPoly",
    "BlasonAurelio",
    "Blason1",
    "Blason2",
    "Blason3",
    "Blason4",
    "Blason5",
    "Blason6",
    "Bloodbol",
    "Bloque",
    "BloqueManu",
    "BloqueTallado",
    "LlaveAzul",
    "Bo",
    "Boingtotem2",
    "BolaDalGurak",
    "BoladePiedra",
    "BolaRayos",
    "BoPieza1",
    "BoPieza2",
    "Botella",
    "BotellaVerde",
    "BotellaSagrada",
    "BarrilPieza1",
    "BarrilPieza2",
    "BarrilPieza3",
    "BarrilPieza4",
    "BarrilPieza5",
    "BarrilPieza6",
    "Brasero1",
    "Braseroarana",
    "Brazalete",
    "LlaveMarron",
    "ButacaMago",
    "CabezaFernando",
    "Cabezon",
    "CabezaSerpiente",
    "Caja_i_i",
    "Caja_i_r",
    "Cajama",
    "Cajon",
    "Cajon2",
    "Caliz",
    "Camabad",
    "Camapaja",
    "Camastro",
    "Camavampiro",
    "Campana",
    "CandilAurelio",
    "Candelabro",
    "Candelpeque",
    "Candil",
    "Candil2",
    "Canica",
    "Cantimplora",
    "Carburo",
    "Carcaj",
    "Carcaj_Amz_seleccion",
    "Carcaj_E",
    "CarcajEnvenenado",
    "CarcajEnvenenado_E",
    "CarcajFuego",
    "CarcajFuego_E",
    "Carretilla",
    "CascoBlade",
    "Casco1",
    "Casco2",
    "Casco3",
    "Casco4",
    "Casco5",
    "Cazo",
    "Cebolla",
    "Cepo",
    "Cerbatana",
    "CerraduraBlade",
    "Cerradura",
    "Cerraduracobox",
    "Cerraduracutre",
    "Cerradurcob",
    "Cerradurdor",
    "Cerradurpla",
    "Chakram",
    "Chakram2",
    "Chakram2Pieza1",
    "Chakram2Pieza2",
    "ChakramPieza1",
    "ChakramPieza2",
    "Chaosword",
    "ChaoswordPieza1",
    "ChaoswordPieza2",
    "ChispasBladeSword",
    "CilindroMagico",
    "CilindroMagico2",
    "CilindroTransportador",
    "Cimitarra",
    "CimitarraPieza1",
    "CimitarraPieza2",
    "Cincel",
    "Cirio",
    "CajamaPieza1",
    "CajamaPieza10",
    "CajamaPieza11",
    "CajamaPieza12",
    "CajamaPieza13",
    "CajamaPieza14",
    "CajamaPieza15",
    "CajamaPieza16",
    "CajamaPieza17",
    "CajamaPieza18",
    "CajamaPieza2",
    "CajamaPieza3",
    "CajamaPieza4",
    "CajamaPieza5",
    "CajamaPieza6",
    "CajamaPieza7",
    "CajamaPieza8",
    "CajamaPieza9",
    "Cofre",
    "Cofrepeque",
    "CofrePieza1",
    "CofrePieza2",
    "CofrePieza3",
    "ColaSerpiente",
    "Columnaestrecha",
    "Columna",
    "Cono1",
    "Coraza1",
    "Coraza2",
    "Coraza3",
    "CorazaBlade",
    "Corona",
    "Costilla",
    "CajonPieza1",
    "CajonPieza10",
    "CajonPieza11",
    "CajonPieza12",
    "CajonPieza13",
    "CajonPieza14",
    "CajonPieza15",
    "CajonPieza16",
    "CajonPieza17",
    "CajonPieza18",
    "CajonPieza2",
    "CajonPieza3",
    "CajonPieza4",
    "CajonPieza5",
    "CajonPieza6",
    "CajonPieza7",
    "CajonPieza8",
    "CajonPieza9",
    "Cracorn1",
    "Cracorn2",
    "CraneoCornudo3",
    "CraneoCornudo4",
    "CristalMineral",
    "Crosspear",
    "CrosspearPieza1",
    "CrosspearPieza2",
    "CrosspearPieza3",
    "CrosspearPieza4",
    "CrushBo",
    "CrushBoPieza1",
    "CrushBoPieza2",
    "CrushBoPieza3",
    "CrushHammer",
    "CrushHammerPieza1",
    "CrushHammerPieza2",
    "CrushHammerPieza3",
    "Cubo",
    "CuchillaFernando",
    "Cuchillo",
    "CuchilloPieza1",
    "CuchilloPieza2",
    "Cuerda",
    "CuerdaLarguisima",
    "CuerdasPuenteFernando",
    "Cupula",
    "Daga",
    "DagaPieza1",
    "DagaPieza2",
    "Dagarrojar",
    "DagarrojarPieza1",
    "DagarrojarPieza2",
    "Dagesse",
    "DagessePieza1",
    "DagessePieza2",
    "DalBlade",
    "DalShield",
    "DalShieldPieza1",
    "DalShieldPieza2",
    "DalShieldPieza3",
    "DalWeapon",
    "DalWeaponPieza1",
    "DalWeaponPieza2",
    "Dardo",
    "DeathBo",
    "DeathBoPieza1",
    "DeathBoPieza2",
    "DeathBoPieza3",
    "DeathKatar",
    "DeathKatarPieza1",
    "DeathKatarPieza2",
    "DeathSword",
    "DeathSwordPieza1",
    "DeathSwordPieza2",
    "DoubleSword",
    "DoubleSwordPieza1",
    "DoubleSwordPieza2",
    "DoubleSwordPieza3",
    "DoubleSwordPieza4",
    "Dragon_estatua",
    "Dragonsw",
    "Eclipse",
    "EclipsePieza1",
    "EclipsePieza2",
    "EgyptSword",
    "EgyptSwordPieza1",
    "EgyptSwordPieza2",
    "Elefante",
    "EscudoBlade2",
    "Escblade3",
    "EscudoBlade",
    "Escudo1",
    "Escudo1Pieza1",
    "Escudo1Pieza2",
    "Escudo2",
    "Escudo2Pieza1",
    "Escudo2Pieza2",
    "Escudo3",
    "Escudo3Pieza1",
    "Escudo3Pieza2",
    "Escudo4",
    "Escudo4Pieza1",
    "Escudo4Pieza2",
    "Escudo5",
    "Escudo5Pieza1",
    "Escudo5Pieza2",
    "Escudo6",
    "Escudo6Pieza1",
    "Escudo6Pieza2",
    "Escudo6Pieza3",
    "Escudo7",
    "Escudo7Pieza1",
    "Escudo7Pieza2",
    "Escudo8",
    "Escudo8Pieza1",
    "Escudo8Pieza2",
    "Escudo8Pieza3",
    "Escudo8x8",
    "Escudo9",
    "Escudo9Pieza1",
    "Escudo9Pieza2",
    "Escudo9Pieza3",
    "Escudon",
    "EscudonPoly",
    "Escudonx6",
    "EsferaGemaAzul",
    "EsferaGemaRoja",
    "EsferaGemaVerde",
    "EsferaNegra",
    "EsferaOrbital",
    "Escudobollado1",
    "Escudobollado2",
    "Eslabon1",
    "Eslabon2",
    "Eslabon3",
    "Espadacurva",
    "Espada",
    "Espada_Bar_seleccion",
    "EspadacurvaPieza1",
    "EspadacurvaPieza2",
    "EspadaelficaPieza1",
    "EspadaelficaPieza2",
    "EspadafiloPieza1",
    "EspadafiloPieza2",
    "EspadaMagica1Pieza1",
    "EspadaMagica1Pieza2",
    "EspadaMagica2Pieza1",
    "EspadaMagica2Pieza2",
    "EspadaMagica3Pieza1",
    "EspadaMagica3Pieza2",
    "EspadaPieza1",
    "EspadaPieza2",
    "EspadaromanaPieza1",
    "EspadaromanaPieza2",
    "Espadaelfica",
    "Espadon",
    "EspadonPoly",
    "Espadafilo",
    "Espadaromana",
    "Espectro",
    "EspadaMagica1",
    "EspadaMagica2",
    "EspadaMagica3",
    "EsqueletoPieza1",
    "EsqueletoPieza10",
    "EsqueletoPieza2",
    "EsqueletoPieza3",
    "EsqueletoPieza4",
    "EsqueletoPieza5",
    "EsqueletoPieza6",
    "EsqueletoPieza7",
    "EsqueletoPieza8",
    "EsqueletoPieza9",
    "Esquirla",
    "Estaca",
    "EstacaFernando",
    "Estalact1",
    "Estalact2",
    "EstatuaGolem",
    "Farol",
    "Farol2",
    "Femur",
    "Fetiche",
    "FireAxe",
    "FireAxePieza1",
    "FireAxePieza2",
    "FireAxePieza3",
    "BoladeFuego",
    "BoladeFuego2",
    "BolitadeFuego",
    "FireBigSword",
    "FireBigSwordPieza1",
    "FireBigSwordPieza2",
    "FireBigSwordPieza3",
    "FireBo",
    "FireBoPieza1",
    "FireBoPieza2",
    "FireRing",
    "FireSword",
    "FireSwordPieza1",
    "FireSwordPieza2",
    "FireSwordPieza3",
    "FireSwordPieza4",
    "BolilladeFuego",
    "FlatSword",
    "FlatSwordPieza1",
    "FlatSwordPieza2",
    "Flecha",
    "Flecha_Amz_seleccion",
    "FlechaEnvenenada",
    "FlechaFuego",
    "Fuelle",
    "GanchoAurelio",
    "Gancho",
    "Garfio",
    "Garfio2",
    "Garfio3",
    "GargolaFernando",
    "Gargola02",
    "Gargola",
    "GargolaNevada",
    "Garropin",
    "GarropinPieza1",
    "GarropinPieza2",
    "Garrote",
    "Garrote2",
    "Garrote2Pieza1",
    "Garrote2Pieza2",
    "GarrotePieza1",
    "GarrotePieza2",
    "Gema",
    "Gemaazul",
    "Gemapurpura",
    "Gemaroja",
    "Geoda",
    "GeodaPieza1",
    "GeodaPieza2",
    "GeodaPieza3",
    "GeodaPieza4",
    "GeodaPieza5",
    "GhostPointer",
    "Gladius",
    "GladiusPieza1",
    "GladiusPieza2",
    "GladiusSeleccion",
    "Globo",
    "Gozne",
    "Grifoserpiente",
    "Guadanya",
    "GuadanyaPieza1",
    "GuadanyaPieza2",
    "GuadanyaPieza3",
    "Hacha",
    "Hacha2",
    "Hacha2hojas",
    "Hacha2hojasPieza1",
    "Hacha2hojasPieza2",
    "Hacha2hojasPieza3",
    "Hacha2Pieza1",
    "Hacha2Pieza2",
    "Hacha3",
    "Hacha3Pieza1",
    "Hacha3Pieza2",
    "Hacha4",
    "Hacha4Pieza1",
    "Hacha4Pieza2",
    "Hacha5",
    "Hacha5Pieza1",
    "Hacha5Pieza2",
    "Hacha6",
    "Hacha6Pieza1",
    "Hacha6Pieza2",
    "Hachacarnicero",
    "HachacarniceroPieza1",
    "HachacarniceroPieza2",
    "HachacarniceroPieza3",
    "HachacarniceroPieza4",
    "HachacuchillaPieza1",
    "HachacuchillaPieza2",
    "HachaPieza1",
    "HachaPieza2",
    "Hacharrajada",
    "HacharrajadaPieza1",
    "HacharrajadaPieza2",
    "HacharrajadaPieza3",
    "Hachacuchilla",
    "Halcon",
    "Halcon2",
    "ElefantePartido",
    "HalfmoonTrail",
    "MartilloForja",
    "Helice",
    "Hogaza",
    "Hoguera",
    "HookSword",
    "HookSwordPieza1",
    "HookSwordPieza2",
    "HookSwordPieza3",
    "HookSwordPieza4",
    "Hornacina",
    "IceAxe",
    "IceAxePieza1",
    "IceAxePieza2",
    "IceAxePieza3",
    "IceAxePieza4",
    "IceAxePieza5",
    "IceHammer",
    "IceHammerPieza1",
    "IceHammerPieza2",
    "IceHammerPieza3",
    "IceHammerPieza4",
    "IceHammerPieza5",
    "IceHammerPieza6",
    "IceSword",
    "IceSwordPieza1",
    "IceSwordPieza2",
    "IceSwordPieza3",
    "IceSwordPieza4",
    "IceWandPieza1",
    "IceWandPieza2",
    "IceWandPieza3",
    "Jar_Dwf_seleccion",
    "Jarra",
    "Jarrita",
    "Jaula",
    "Katana",
    "KatanaPieza1",
    "KatanaPieza2",
    "Katar",
    "KatarDoble",
    "KatarDoblePieza1",
    "KatarDoblePieza2",
    "KatarDoblePieza3",
    "KatarDoblePieza4",
    "Katarmoon",
    "KatarmoonPieza1",
    "KatarmoonPieza2",
    "KatarmoonPieza3",
    "KatarmoonPieza4",
    "KatarPieza1",
    "KatarPieza2",
    "KatarPieza3",
    "Keysup",
    "KingShield",
    "KingShieldPieza1",
    "KingShieldPieza2",
    "KingShieldPieza3",
    "KingSword",
    "KingSwordPieza1",
    "KingSwordPieza2",
    "KingSwordPieza3",
    "LamparaKongo",
    "Lamparatecho",
    "LamparaNegra",
    "Lampared",
    "LamparaAurelio",
    "Lampcolg",
    "Lamparaegipto",
    "Gancholamp",
    "LamparaMiguel",
    "LamparaMiguelSinPeana",
    "Lanza",
    "LanzaAncha",
    "LanzaAnchaPieza1",
    "LanzaAnchaPieza2",
    "LanzaAnchaPieza3",
    "LanzaAnchaPieza4",
    "LanzaPieza1",
    "LanzaPieza2",
    "Lanzapivotes",
    "Lapida",
    "Obelisco",
    "Lapida3",
    "LapidaAmazona",
    "LapidaBarbaro",
    "LapidaCaballero",
    "LapidaManuel",
    "LeonBronce",
    "Libro",
    "Libro2",
    "Libro3",
    "LibroPulsador",
    "LightEdge",
    "LightEdgePieza1",
    "LightEdgePieza2",
    "LightEdgePieza3",
    "Llave",
    "Llavecob",
    "Llavecobox",
    "Llavecutre",
    "LlaveDoblada",
    "Llavedor",
    "Llavepla",
    "Llavero",
    "LongSword",
    "LongSwordPieza1",
    "LongSwordPieza2",
    "LongSwordPieza3",
    "LuzDivinaFina",
    "LuzDivinaGorda",
    "Astillas1",
    "Astillas2",
    "Astillas3",
    "MagicShield",
    "MagicShield2",
    "MagicShield3",
    "MagicShieldBreak",
    "MandibulaSerpiente",
    "Manzana",
    "Martillo2",
    "Martillo",
    "Martillo2Pieza1",
    "Martillo2Pieza2",
    "Martillo3",
    "Martillo3Pieza1",
    "Martillo3Pieza2",
    "MartilloForjaPieza1",
    "MartilloForjaPieza2",
    "MartilloPieza1",
    "MartilloPieza2",
    "Maza",
    "Maza2",
    "Maza2Pieza1",
    "Maza2Pieza2",
    "Maza3",
    "Maza3Pieza1",
    "Maza3Pieza2",
    "MazaDoble",
    "MazaDoblePieza1",
    "MazaDoblePieza2",
    "Mazapiedra",
    "MazapiedraPieza1",
    "MazapiedraPieza2",
    "MazapiedraPieza3",
    "MazaPieza1",
    "MazaPieza2",
    "Menhir1",
    "Menhir2",
    "Menhir3",
    "Mesa",
    "MesaPieza1",
    "MesaPieza2",
    "MesaPieza3",
    "MesaPieza4",
    "MesaPieza5",
    "Mesita",
    "MesitaPieza1",
    "MesitaPieza2",
    "MesitaPieza3",
    "MesitaPieza4",
    "Meson",
    "MesonPieza1",
    "MesonPieza2",
    "Mesonroto",
    "Meteorito",
    "Monjecaliz",
    "Monjema",
    "Monjescudo",
    "Monjespada",
    "Mortero",
    "Naginata",
    "Naginata2",
    "Naginata2Pieza1",
    "Naginata2Pieza2",
    "Naginata2Pieza3",
    "NaginataPieza1",
    "NaginataPieza2",
    "Ninjato",
    "NinjatoPieza1",
    "NinjatoPieza2",
    "Nube",
    "ObeliscoGrande",
    "ObeliscoNevado",
    "OndaExpansiva",
    "Libroabierto2",
    "Libroabierto",
    "Orbe",
    "Orksword",
    "OrkswordPieza1",
    "OrkswordPieza2",
    "Pala",
    "Palanca1",
    "Palanca2",
    "Palanca3",
    "PalancaSuelo",
    "PalancaTimon",
    "Palangana",
    "Palancatortura",
    "Paletilla",
    "Panoplia",
    "PasarelaCorta",
    "PasarelaLarga",
    "Peanapiedra",
    "Pelele",
    "PeleleNevado",
    "Pendon1",
    "Pendon2",
    "Pendon3",
    "Pendon4",
    "Pendulo",
    "Pendulo2",
    "Pergamino2",
    "Pergamino",
    "Perola",
    "Phurbhu",
    "PhurbhuPieza1",
    "PhurbhuPieza2",
    "Pico",
    "PiedraNevada",
    "Piedra_01",
    "Piedra_02",
    "Piedra_03",
    "Piedra_04",
    "Piedra_05",
    "Piedra_06",
    "Piedra_07",
    "Piedra_08",
    "Piedra_09",
    "Piedra_10",
    "Piedra_Bar_seleccion",
    "Piedra_Glm_cl",
    "Piedra_Glm_ic",
    "Piedra_Glm_lv",
    "Piedra_Glm_mt",
    "Piedra_Glm_st",
    "PiedraInformativa",
    "PiedrasBarbaro",
    "PiedraNevadaCortada",
    "PinchoManuel",
    "PinchoMiguel",
    "Pinchos",
    "PinchoSotano",
    "Pivote",
    "Pivote2",
    "PivoteEnvenenado",
    "PlacaTallada",
    "Planta1",
    "Planta2",
    "Planta3",
    "Plantita",
    "PlataformaFernando",
    "Plataforma",
    "PlataformaRail",
    "Pluma",
    "Pocima100",
    "Pocima200",
    "Pocima25",
    "Pocima50",
    "PocimaTodo",
    "Polea",
    "PowerPotion",
    "PowerupGold",
    "PowerupSilver",
    "PuenteAdolfoDerecho",
    "PuenteAdolfoIzquierdo",
    "PuenteAurelio",
    "Puenteau_Plano",
    "PuenteFernando",
    "PuertaFernando",
    "PuertaMiguelDerecha",
    "PuertaMiguelIzquierda",
    "QueenSword",
    "QueenSwordPieza1",
    "QueenSwordPieza2",
    "QueenSwordPieza3",
    "Queso",
    "Rabano",
    "Rail",
    "Rail2",
    "Raiz",
    "Rama1",
    "Rama2",
    "RamaNevada",
    "Rastrillo",
    "Rastrillo2",
    "ReinaAurelio",
    "Reja",
    "Restos",
    "Reyaurelio",
    "RhinoClub",
    "RhinoClubPieza1",
    "RhinoClubPieza2",
    "Roca1Aurelio",
    "Roca2Aurelio",
    "Roca1",
    "Roca2",
    "Roca3",
    "RollodeCuerda",
    "Sablazo",
    "SablazoPieza1",
    "SablazoPieza2",
    "Saquito",
    "SawSword",
    "SawSwordPieza1",
    "SawSwordPieza2",
    "SectorVolcan",
    "SemiBolaRayos",
    "Semipuxero",
    "Seta",
    "Setas",
    "Shield_Kgt_seleccion",
    "Silla",
    "SillaPieza1",
    "SillaPieza2",
    "SillaPieza3",
    "SillaPieza4",
    "SillaPieza5",
    "SillaPieza6",
    "Skull",
    "Soporteantorcha",
    "SoporteOrbe",
    "SteelFeather",
    "SteelFeatherPieza1",
    "SteelFeatherPieza2",
    "SteelFeatherPieza3",
    "SteelFeatherPieza4",
    "Supositorio",
    "Suriken",
    "Tabla_l",
    "Tabla_rota",
    "Tabla_rota2",
    "Tabla_xl",
    "Tabla_xlpieza2",
    "Tabla_xPieza1",
    "Tablatortura",
    "Tablilla1",
    "Tablilla2",
    "Tablilla3",
    "Tablilla4",
    "Tablilla5",
    "Tablilla6",
    "Taburete",
    "Taburete_Dwf_seleccion",
    "TaburetePieza1",
    "TaburetePieza2",
    "TaburetePieza3",
    "TaburetePieza4",
    "TabureteSeleccion",
    "Tacita",
    "TaiSword",
    "TaiSwordPieza1",
    "TaiSwordPieza2",
    "TaiSwordPieza3",
    "TaiSwordPieza4",
    "Tapiz",
    "Tapiz2",
    "Tapiz3",
    "Tapiz4",
    "Tapiz5",
    "Tapiz6",
    "TapizAurelio",
    "TapizEscorpion",
    "Tapizkemado1",
    "Tapizkemado2",
    "TelaranyaCuadrada",
    "TelaranyaCuadrada2",
    "TelaranyaEsquina",
    "TelaranyaTriangular",
    "Telescopio",
    "Timon",
    "Tinaja",
    "Tintero",
    "Tocon",
    "Totem",
    "Totem2",
    "TinajaPieza1",
    "TinajaPieza2",
    "TinajaPieza3",
    "TinajaPieza4",
    "TinajaPieza5",
    "Trampilla",
    "Tridente",
    "TridentePieza1",
    "TridentePieza2",
    "Trillo",
    "Tronchy",
    "Tronco",
    "TroncoGrande",
    "TroncoNevado",
    "TroncoTrampa",
    "Tronoliso",
    "TronoEscarabeu",
    "Tronera",
    "Tronera2",
    "Trono",
    "TronoManuel",
    "Tumbacobra",
    "Lapidareina",
    "Lapidarey",
    "Vagoneta",
    "VampShield",
    "VampShieldPieza1",
    "VampShieldPieza2",
    "VampWeapon",
    "VampWeaponPieza1",
    "VampWeaponPieza2",
    "Varilla",
    "Varillaancha",
    "Varita1",
    "Varita1Pieza1",
    "Varita1Pieza2",
    "Varita2",
    "Varita2Pieza1",
    "Varita2Pieza2",
    "Varita5",
    "Varita5Pieza1",
    "Varita5Pieza2",
    "Varita6",
    "Varita6Pieza1",
    "Varita6Pieza2",
    "Varita7",
    "Varita7Pieza1",
    "Varita7Pieza2",
    "Velon",
    "Viga",
    "VigaPlana",
    "Vigaro1",
    "Vigaro2",
    "Vampire_Head",
    "Vortice1",
    "Vortice2",
    "LlaveBlanca",
    "Xkorpyon",
    "LlaveAmarilla",
    "LlaveAmarilla_Aura",
    "Yunque",
    "Zocalo1",
    "Zocalo2",
    "Zocalo3",
    "ZocaloSerpiente",
    "ZocaloSuelo",
    "ZocaloTimon",
    "Rastrillo3",
    "Rastrillo32",
    "IceWand",
    "trozogran1",
    "trozogran10",
    "trozogran11",
    "trozogran12",
    "trozogran2",
    "trozogran3",
    "trozogran4",
    "trozogran5",
    "trozogran6",
    "trozogran7",
    "trozogran8",
    "trozogran9",
    "trozope1",
    "trozope2",
    "trozope3",
    "trozope4",
    "trozope5",
    "trozope6",
    "trozope7",
    "trozope8",
    "Rastrillo10",
    "Rastrillo102",
    "BarraCareto",
    "BarraElefante",
    "BarraNarizon",
    "BarraPajaro",
    "AlabardaPieza3",
    "puertagran",
    "puertamed",
    "puertapeque1",
    "puertapeque2",
    "puertapeque3",
    "puertapeque4",
    "Carcaj1",
    "Carcaj2",
    "Carcaj3",
    "CarcajEnvenenado1",
    "CarcajEnvenenado2",
    "CarcajEnvenenado3",
    "CarcajFuego1",
    "CarcajFuego2",
    "CarcajFuego3",
]
