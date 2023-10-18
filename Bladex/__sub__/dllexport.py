# 09 2023 sryml
# Module 'Bladex'
from __future__ import annotations

import typing as __t

from . import b_object as __b_object
from . import b_types as __bt
from . import character as __character
from . import entity as __entity


def ActivateInput() -> int:
    """ActivateInput()
    Reactivate the input for the main player."""
    ...


def AddActionStepSound(table: str, action: str, step_sound_table: str) -> int:
    """AddActionStepSound(table,action,step_sound_table)"""
    ...


def AddAnimFlags(
    anm_name: str,
    wuea: __t.Literal[0, 1, 2],
    mod_y: __bt.Bool,
    solf: __bt.Bool,
    copy_rot: __bt.Bool,
    bng_mov: __t.Literal[0, 1, 2, 3, 4, 5],
    headf: __t.Literal[0, 1, 2, 3],
) -> __bt.Bool:
    """
    AddAnimFlags(string,wuea,mdf_y,solf,copy_rot,bng_mov,head_f)\n
    :bng_mov:
        BM_IDC = 0\n
        BM_NONE = 1\n
        BM_XYZ = 2\n
        BM_XZ = 3\n
        BM_2ANM = 4\n
        BM_SCRIPT = 5
    :headf:
        HEADF_ENG = 0\n
        HEADF_ANM = 1\n
        HEADF_ANM2SEE = 2\n
        HEADF_ANM2ENG = 3
    """
    ...


def AddAnmEvent(anm_name: str, event_name: str, event_frame: float) -> int:
    """AnmAddEvent(anm_name,event_name,event_frame)"""
    ...


def AddAnmLRelease(anm_name: str, anm_frame: float) -> int:
    """"""
    ...


def AddAnmLStep(anm_name: str, anm_frame: float) -> int:
    """"""
    ...


def AddAnmRRelease(anm_name: str, anm_frame: float) -> int:
    """"""
    ...


def AddAnmRStep(anm_name: str, anm_frame: float) -> int:
    """"""
    ...


@__t.overload
def AddBipedAction(
    biped_name: str,
    action_name: str,
    anm_name: str,
    anm_frame_start: float,
    anm_frame_end: float,
    i_unknown: int,
) -> int:
    """"""
    ...


@__t.overload
def AddBipedAction(
    biped_name: str,
    action_name: str,
    anm_name: str,
    s_unknown: str,
    anm_frame_start: float,
    anm_frame_end: float,
    i_unknown: int,
) -> int:
    """"""
    ...


def AddBipedAction(*args: __t.Any, **kwargs: __t.Any) -> __t.Any:
    """"""
    ...


@__t.overload
def AddBoundFunc(action_name: str, proc: __t.Callable[[], __t.Any]) -> int:
    ...


@__t.overload
def AddBoundFunc(action_name: str, proc: str) -> int:
    ...


def AddBoundFunc(*args: __t.Any, **kwargs: __t.Any) -> __t.Any:
    """AddBoundFunc(string key,proc)
     Asigna el procedimiento pr al suceso key.
    AddBoundFunc(string key,string predproc)
     Asigna el procedimiento predefinifo predproc  al suceso key.
     predproc puede ser: Forward, Backwards, Up, Down, Left, Right, RotateLeft, RotateRight, RotateUp, RotateDown (más, preguntar a Jose)
    """
    ...


def AddCombustionDataFor(
    object_kind: str,
    fire_kind: __t.Union[__bt.str_, __bt.ParticleType],
    upper_treshol: float,
    lower_treshold: float,
    flame_height: float,
    flame_size: float,
    speed: float,
    livetime: float,
) -> int:
    """AddCombustionDataFor(object_kind,upper_treshol,lower_treshold,flame_height,flame_size,speed,livetime)\n
    :livetime: 144000 - It will be extinct in 40 hours!
    """
    ...


def AddFloorCTolerance(anm_name: str, tolerance: float) -> __t.Literal[1]:
    """AddFloorCTolerance(anm_name,float)"""
    ...


def AddGhostSector(
    ghost_sector_name: str,
    group_name: str,
    floor_height: float,
    roof_height: float,
    points: list,
) -> int:
    """AddGhostSector(string GhostName,string GroupName,float FloorHeight,float RoofHeight,List points)
    Crea."""
    ...


def AddInputAction(action_name: str, npi: __bt.Bool) -> int:
    """AddInputAction(string action_name,int npi)
    Crea una acción nueva."""
    ...


def AddMaterialStepSound(table: str, material: str, step_sound: str) -> int:
    """AddMaterialStepSound(table,material,step_sound)"""
    ...


def AddMusicEventADPCM(
    event_name: str,
    file: str,
    f_in: float,
    f_out: float,
    volume: float,
    priority: float,
    background: __bt.Bool,
    loop: int,
    unknown: int = 0,
) -> int:
    """AddMusicEventADPCM( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext )"""
    ...


def AddMusicEventCD(
    event_name: str,
    track: int,
    f_in: float,
    f_out: float,
    volume: float,
    priority: float,
    background: __bt.Bool,
    loop: int,
) -> int:
    """AddMusicEventCD(lpszEventName, iTrack, dFIn, dFOut, fVolume, fPriority, bBackGround, iNext)"""
    ...


def AddMusicEventMP3(
    event_name: str,
    file: str,
    f_in: float,
    f_out: float,
    volume: float,
    priority: float,
    background: __bt.Bool,
    loop: int,
    unknown: int = 0,
) -> int:
    """AddMusicEventMP3( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext )"""
    ...


def AddMusicEventWAV(
    event_name: str,
    file: str,
    f_in: float,
    f_out: float,
    volume: float,
    priority: float,
    background: __bt.Bool,
    loop: int,
    opened: int = 0,
) -> int:
    """AddMusicEventWAV( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext, [opened])"""
    ...


def AddParticleGType(
    type_name: str,
    bitmap_name: str,
    particle_type: __t.Literal[0, 1, 2, 3],
    duration: int,
) -> int:
    """
    :particle_type:
        B_PARTICLE_GTYPE_COPY = 0\n
        B_PARTICLE_GTYPE_BLEND = 1\n
        B_PARTICLE_GTYPE_ADD = 2\n
        B_PARTICLE_GTYPE_MUL = 3\n
    """
    ...


def AddScheduledFunc(
    time: float, func: __t.Callable, func_args: tuple, name: str = "Unnamed"
) -> int:
    """AddScheduledFunc(double time,Func,Args)
    Llama a la funcion Func con los argumentos Args en el tiempo time"""
    ...


def AddStepSound(name: str, sound: __b_object.B_PySound) -> int:
    """AddStepSound(name,sound)"""
    ...


def AddStopTests(anm_name: str) -> __t.Literal[1]:
    """AnmStopTests(anm_name)"""
    ...


def AddTextureMaterial(texture: str, material: str) -> int:
    """AddTextureMaterial(texture,material)"""
    ...


def AddTranTime(
    biped_name: str, next_anm: str, prev_anm: str, time: float, unknown: int = 1
) -> int:
    """AddTranTime (string biped_name,string next_anm , string prev_anm , double time )
    Al pasar de animacion prev_anm a next_anm la transicion dura t segs . 0 si no transicion .
    """
    ...


def AddTriggerSector(
    trigger_sector_name: str,
    group_name: str,
    floor_height: float,
    roof_height: float,
    points: list,
) -> int:
    """AddTriggerSector(string TriggerSectorName,string GroupName,float FloorHeight,float RoofHeight,List points)
    Crea."""
    ...


def AddWatchAnim(anm: str) -> __bt.Bool:
    """AddWatchAnim(string)
     Establece esa animacion como una de las incluidas en modo watch.
    NOTA : NO es ejecutada por defecto por ningun personaje , para eso hay otra funcion !.
    """
    ...


def AnmAddEvent(anm_name: str, event_name: str, event_frame: float) -> __t.Literal[1]:
    """AnmAddEvent(anm_name,event_name,event_frame)
    Declara en la animacion de nombre anm_name un evento de nombre event_name en el frame event_frame
    """
    ...


def AnmClearEvents(anm_name: str) -> __t.Literal[1]:
    """AnmClearEvents(anm_name)
    Borra en la animacion de nombre anm_name todos los eventos"""
    ...


def AnmDelEvent(anm_name: str, event_name: str) -> __t.Literal[1]:
    """AnmDelEvent(anm_name,event_name)
    Borra en la animacion de nombre anm_name el evento de nombre event_name"""
    ...


def AnmGetEventFrame(anm_name: str, event_name: str) -> float:
    """AnmGetEventFrame(anm_name,event_name)
    Devuelve en la animacion de nombre anm_name frame del evento de nombre event_name y si no existe devuelve -1
    """
    ...


def AnmTypeLSteps(ent_name: str, anm_name: str) -> __bt.Bool:
    """"""
    ...


def AnmTypeRSteps(ent_name: str, anm_name: str) -> __bt.Bool:
    """"""
    ...


def AssocKey(
    action: str,
    input_device: __t.Literal["Keyboard", "Mouse", "Gamepad"],
    key: str,
    on_press: __bt.Bool = 1,
) -> __bt.Bool:
    """bool AssocKey(string action,string input_device,string key[,int press])
    Asocia la acción action con la tecla key del dispositivo input_device"""
    ...


def BeginLoadGame() -> None:
    """void BeginLoadGame()
    Indica a la engine que se va a cargar una partida grabada para que pueda ajustar parámetros.
    """
    ...


def Bind2(
    action_name1: str, action_name2: str, new_action: str, time_window: int
) -> __bt.Bool:
    """Bind2(void)
    Associate a combination of 2 Actions keys to a new Action, time window settings."""
    ...


def BodInspector() -> str:
    """BodInspector()"""
    ...


def CDCallBack(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int CDCallBack(func f)
    Establece la función CD."""
    ...


def CDLenght(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int CDLenght()
    Devuelve la duración del CD en milisegundos."""
    ...


def CDPause(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int CDPause()
    Detiene el CD."""
    ...


def CDPlayTrack(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """PlayCDTrack(int ntrack)
    Reproduce la pista ntrack del CD.
    Si ntrack==1 reproduce todo el CD."""
    ...


def CDPresent(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int CDPresent()
    Indica si está el CD."""
    ...


def CDStop(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int CDStop()
    Detiene el CD."""
    ...


def CDTrackLenght(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """CDTrackLenght(int ntrack)
    Devuelve la duración en milisegundos de la pista ntrack."""
    ...


def CDnTracks(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int nCDTracks()
    Devuelve el número de pistas del CD."""
    ...


def CheckAnims() -> __bt.Bool:
    """Gives a report of anims not assigned"""
    ...


def CheckPyErrors() -> __bt.Bool:
    """returns whether a python error has occured."""
    ...


def CleanArea(x: float, y: float, z: float, distance: float) -> __t.Literal[1]:
    """CleanArea(x,y,z,distance)
      Limpia una zona esferica con centro en 'x,y,z'
    y distancia 'distance' de sangre."""
    ...


def CloseDebugChannel(channel_name: str) -> __bt.Bool:
    """bool CloseDebugChannel(string channel_name)
    Cierra el canal de depuración de nombre channel_name."""
    ...


def CloseLevel(statement: str, map_name: str) -> None:
    """CloseLevel([string statement])
    Cierra el nivel actual y ejecuta la instrucción statement."""
    ...


def CloseProfileSection(section: int) -> __bt.Bool:
    """bool CloseProfileSection(int section)
    Tiene que estar activado el profiler interno.
    Cierra la sección i."""
    ...


def CreateBipedData(biped_name: str, kind: str) -> int:
    """"""
    ...


def CreateDFCAnimation(
    file1: str, file2: str, internal_name: str, n_armonics: int
) -> int:
    """CreateDFCAnmimation(str File1,str File2,str InternalName,int n_armonics)"""
    ...


# CreateEntity >>>

# __Type = __t.NewType("B_PyEntity", __entity.B_Entity_Aura)


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Aura"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Aura:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Camera"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Camera:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity ElectricBolt"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_ElectricBolt:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Fire", "Entity Dynamic Fire"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Fire:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Lava"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Lava:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Magic Missile"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Magic_Missile:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Particle"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Particle:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal[
        "Entity Particle System D1",
        "Entity Particle System D2",
        "Entity Particle System D3",
        "Entity Particle System Dobj",
        "Entity Particle System Dperson",
    ],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> B_Entity_Particle_System:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Pool"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Pool:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Sliding Area"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Sliding_Area:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Sound"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Sound:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Spot"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Spot:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Water"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Water:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Actor"],
    mesh_name: str = "",
) -> __entity.B_Entity_Actor:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Person"],
    mesh_name: str = "",
) -> __entity.B_Entity_Person:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Arrow", "Weapon"],
    mesh_name: str = "",
) -> __entity.B_Entity_Weapon:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Physic"],
    mesh_name: str = "",
) -> __entity.B_Entity_Physic:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Union[__bt.Builtin_Kind, __bt.BodList],
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["", "Actor", "Arrow", "Person", "Physic", "Weapon"] = "",
    mesh_name: str = "",
):
    ...


def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __t.Any:
    """CreateEntity(string name,string kind,double x,double y,double z)\n
    Crea una entidad nueva."""
    ...


# CreateEntity <<<


def CreateFCAnimation(file: str, internal_name: str, n_armonics: int) -> int:
    """CreateFCAnmimation(str File,str InternalName,int n_armonics)"""
    ...


def CreateMaterial(name: str) -> __b_object.B_PyMaterial:
    """CreateMaterial(string name)
    Crea un nuevo material con nombre name."""
    ...


def CreateRoute() -> __b_object.B_PyRoute:
    """CreateRoute()
    Crea una ruta vacía nueva."""
    ...


def CreateSound(file_name: str, sound_name: str) -> __b_object.B_PySound:
    """CreateSound(string filename,string soundname)
    Crea un sonido a partir del filename y con nombre name."""
    ...


def CreateSpark(
    name: str,
    x: float,
    y: float,
    z: float,
    x_spark_dir: float,
    y_spark_dir: float,
    z_spark_dir: float,
    angle: float,
    normal_velocity: __bt.Int,
    unknown1: float,
    YGravity: __bt.Int,
    scale: float,
    r1: int,
    g1: int,
    b1: int,
    r2: int,
    g2: int,
    b2: int,
    pps: int,
    Time2Live: float,
    DeathTime: float,
    isglow: __bt.Bool,
) -> __entity.B_Entity_Spark:
    """CreateSpark(string name,double x,double y,double z,)\n
    Crea un efecto de chispas.\n
    :unknown1: Reference = 100"""
    ...


def CreateTimer(timer_name: str, period: float) -> __bt.Bool:
    """CreateTimer(string TimerName,double period)
    Crea un Timer de nombre TimerName con periodo period."""
    ...


def DeactivateInput() -> int:
    """DeactivateInput()
    Disabled the input for the main player."""
    ...


def DeleteEntity(arg: __t.Union[str, __entity.B_PyEntity]) -> __bt.Bool:
    """DeleteEntity(string name/object entity)
    Delete existing object.  Use with care.  Subscribe to Pin if unsure."""
    ...


def DeleteStringValue(v: str) -> __bt.Bool:
    """string DeleteStringValue(string variable)
    Elimina variable."""
    ...


def DisableProfiler() -> __bt.Bool:
    """bool DisableProfiler(void)
    desactivar profiler interno."""
    ...


def DoneLoadGame() -> None:
    """void DoneLoadGame()
    Indica a la engine que se ha cargado una partida grabada para que pueda ajustar parámetros.
    """
    ...


def DrawBOD(
    bodname: str, x: int, y: int, w: int, h: int, scale: float, i_unknown: int
) -> __bt.Bool:
    """DrawBOD(string BODName,int x,int y,int ancho,int alto)
    Dibuja el BOD de nombre BODName en el rectángulo x,y,ancho,alto."""
    ...


def DumpMemoryLeaks(filename: str) -> __bt.Bool:
    """bool DumpMemoryLeaks(string filename)
    Dumps cuurent memory allocations to filename."""
    ...


def EnableProfiler() -> __bt.Bool:
    """bool EnableProfiler(void)
    activar profiler interno."""
    ...


def ExeMusicEvent(event_idx: int, unknown2: __bt.Bool = 0) -> int:
    """e.g: ExeMusicEvent(-1)"""
    ...


def ExportWorld(file_name: str) -> __bt.Bool:
    """ExportWorld ()
    Export the world to owner Max format."""
    ...


def GenerateEntityName() -> str:
    """string GenerateEntityName()
    Generates a new and unique entity name."""
    ...


def GetAecGap() -> float:
    """bool GetAecGap()
    Devuelve tiempo de auto encaramientpo....."""
    ...


def GetAfterFrameFunc(name: str) -> __t.Callable:
    """GetAfterFrameFunc(name)
    Devuelve la función AfterFrame de nombre name."""
    ...


def GetAfterFrameFuncName(index: int) -> __t.Union[str, None]:
    """string GetAfterFrameFuncName(int idx)
    Devuelve el nombre de la función AfterFrame del sistema de índice idx."""
    ...


def GetAnimationDuration(anm_name: str) -> float:
    """GetAnimationDuration (string sampled animation name )
    Resturns the duration in seconds of the full animation disregarding interpolation.
    """
    ...


def GetAnmRaces() -> __t.List:
    """list GetAnmRaces(void)
    Devuelve una lista con los nombres de las razas cargadas en memoria."""
    ...


def GetAppMode() -> str:
    """string GetAppMode()
    Obtiene el modo de la aplicación (Game, Menu,...)."""
    ...


def GetAutoEngageCombat() -> __bt.Bool:
    """bool GetAutoEngageCombat()
    Devuelve true si se encara automaticanmente si se puede."""
    ...


def GetBloodLevel() -> __bt.Bool:
    """int GetBloodLevel()
    Obtiene el nivel de sangre."""
    ...


def GetCharType(name: str, short_name: str) -> __character.B_PyChar:
    """GetCharType(Barbarian,Bar)
    Crea un CharType , o raza de personaje."""
    ...


def GetCombos(person_name: str) -> __t.List:
    """tuple GetCombos(blah blah BLAH!)"""
    ...


def GetCommandLine() -> str:
    """string GetCommandLine()
    Obtiene la línea de órdenes que se ha pasado a la aplicación."""
    ...


def GetCurrentMap() -> str:
    """string GetCurrentMap()
    Devuelve el mapa actual."""
    ...


def GetDrawObjectShadows() -> __bt.Bool:
    """bool GetDrawObjectShadows()
    Devuelve si se dibujan las sombras de los objetos/personajes."""
    ...


def GetEAXOverride() -> __bt.Bool:
    """float GetEAXOverride()"""
    ...


def GetEnemiesVisibleFrom(
    center: __bt.Vector3, radius: float, direction: __bt.Vector3, angle: float
) -> tuple:
    """tuple GetEnemiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""
    ...


def GetEntitiesAt(x: float, y: float, z: float, radius: float) -> tuple:
    """tuple GetEntitiesAt(double x,double y,double z,double radius)
    Obtiene las entidades que están en un radio radius de la posición (x,y,z)"""
    ...


def GetEntitiesVisibleFrom(
    center: __bt.Vector3, radius: float, direction: __bt.Vector3, angle: float
) -> tuple:
    """tuple GetEntitiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""
    ...


@__t.overload
def GetEntity(arg: __t.Literal["Player1"]) -> __entity.B_Entity_Person:
    ...


@__t.overload
def GetEntity(arg: __t.Literal["Camera"]) -> __entity.B_Entity_Camera:
    ...


@__t.overload
def GetEntity(
    arg: __t.Union[str, int, __t.Literal["Camera", "Player1"]]
) -> __entity.B_PyEntity:
    ...


def GetEntity(arg: __t.Any) -> __t.Any:
    """GetEntity(int n)
     Crea una entidad de Python que referencia a la entidad Blade de índice n.
    GetEntity(string name)
     Crea una entidad de Python que referencia a la entidad Blade de nombre name."""
    ...


def GetGhostSectorSound(gs_name: str) -> __b_object.B_PySound:
    """GetGhostSectorSound(string gsname)
    Devuelve el sonido ambiente perteneciente al sector fantasma de nombre gsname."""
    ...


def GetInputMode(device: str) -> str:
    """string GetInputMode(string device)
    Obtiene el modo del dispositivo device."""
    ...


def GetLastPlayerCType() -> str:
    """string GetLastPlayerCType()"""
    ...


def GetMaterial(x: __t.Union[str, int]) -> __b_object.B_PyMaterial:
    """GetMaterial(int n)
     Crea un objeto Python que referencia al material Blade de índice n.
    GetMaterial(string name)
     Crea un objeto Python que referencia al material Blade de nombre name."""
    ...


def GetMenuTgapFunc() -> __bt.Unknown:
    """GetMenuTgapFunc()
    Devuelve ....."""
    ...


def GetModelPos(person_name: str) -> __bt.Vector3:
    """GetModelPos(string Person)
    Devuelve la posicion del modelo 3D del Person especificado"""
    ...


def GetMouseState() -> __t.Tuple[int, float, float]:
    """GetMouseState()
    retorna invert,xsens,ysens"""
    ...


def GetMusicEvent(event_name: str) -> int:
    """GetMusicEvent(lpszEventName)\n
    :return: event_idx
    """
    ...


def GetMusicEventPriority(event_idx: int) -> float:
    """ """
    ...


def GetMusicVolume() -> float:
    """float GetMusicVolume()
    Obtiene el volumen de la musica."""
    ...


def GetMutilationLevel() -> __bt.Bool:
    """int GetMutilationLevel()
    Obtiene el nivel de mutilaciones."""
    ...


def GetNewExclusionGroupId() -> __bt.Unknown:
    """int GetNewExclusionGroupId()(void)
    Devuelve un nuevo y unico identificador para los grupos de exclusion."""
    ...


def GetObjectEntitiesVisibleFrom(
    center: __bt.Vector3, radius: float, direction: __bt.Vector3, angle: float
) -> tuple:
    """tuple GetObjectEntitiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""
    ...


def GetPTime() -> float:
    """GetPTime()
    real timer"""
    ...


def GetParticleGType(index: int) -> __t.Tuple[str, str, int, int]:
    """Preguntar a Angel\n
    :return: tuple(type_name, bitmap_name, particle_type, duration)
    """
    ...


def GetParticleGVal(type: str, index: int) -> __t.Tuple[int, int, int, float, float]:
    """Preguntar a Angel\n
    :return: tuple(r, g, b, a, size)
    """
    ...


def GetProgramId() -> int:
    """int GetProgramId()
    Devuelve identificador de la aplicación.
    (HWND en Windows)"""
    ...


def GetRootWidget() -> int:
    """SetRootWidget(widget w)
    Establece el Widget raiz."""
    ...


def GetSSQuality() -> int:
    """Undoc(0-2)"""
    ...


def GetSaveInfo() -> __t.Tuple[int, __t.Tuple[int]]:
    """tuple GetSaveInfo(void)
    Obtiene información de estado."""
    ...


def GetScheduledFunc(index: int) -> tuple:
    """(func,arg,name,time) GetScheduledFunc(int index)
    Devuelve una tupla con la función, los argumentos, el nombre y cuando se ejecuta."""
    ...


def GetScreenRect() -> tuple:
    """
    :return: (x_min, y_min, x_max, y_max)
    """
    ...


def GetScreenXY(ent_pos: __bt.Vector3) -> __bt.Vector2:
    """
    :return: (screen_x, screen_y)
    """
    ...


@__t.overload
def GetSector(index: int) -> __b_object.B_PySector:
    ...


@__t.overload
def GetSector(x: float, y: float, z: float) -> __b_object.B_PySector:
    ...


def GetSector(*args: __t.Any, **kwargs: __t.Any) -> __t.Any:
    """GetSector(int n)
     Crea un sector de Python que referencia al sector Blade de índice n.
    GetSector(double x,double y,double z)
     Crea un sector de Python que referencia al sector Blade que contiene al punto (x,y,z).
    """
    ...


def GetSound(sound_name: str) -> __b_object.B_PySound:
    """GetSound(name)"""
    ...


def GetSoundFileName(sound_idx: int) -> str:
    """string GetSoundFileName(int idx)
    Devuelve el archivo del sonido idx."""
    ...


def GetSoundName(sound_idx: int) -> str:
    """string GetSoundName(int idx)
    Devuelve el nombre del sonido idx."""
    ...


def GetSoundVolume() -> float:
    """float GetSoundVolume()
    Obtiene el volumen del sistema de sonido."""
    ...


def GetSpeakerConfig() -> int:
    """Undoc(0-3)"""
    ...


def GetStringValue(key: str) -> str:
    """string GetStringValue(string variable)
    Devuelve el valor de variable, None si no esta definida."""
    ...


def GetTextWH(text: str) -> __t.Tuple[float, float]:
    """"""
    ...


def GetTime() -> float:
    """float GetTime(void)
    Devuelve el tiempo del juego en segundos."""
    ...


def GetTimeActionHeld(action_name: str) -> float:
    """Return the amount of milliseconds a key has been hald down, or zero if it is currently considered released"""
    ...


def GetTimeSpeed() -> float:
    """float GetTimeSpeed(void)
    Devuelve la velocidad tiempo del juego."""
    ...


def GetTimerInfo(timer_idx: int) -> tuple:
    """(name,period) GetTimerInfo(int iTimer)
    Devuelve información sobre el timer de índice iTimer."""
    ...


def GetTrailType(name: str) -> __b_object.B_PyTrail:
    """GetTrailType(esteraCorta)
    Crea un TrailType , o tipo de estelas."""
    ...


def GetTriggerSectorData(trigger_sector_name: str) -> __t.Any:
    """GetTriggerSectorFunc(string TriggerSectorName)
    Devuelve el objeto Python asociado al campo Data del triggersector TriggerSectorName.
    """
    ...


def GetTriggerSectorFloorHeight(trigger_sector_name: str) -> int:
    """GetTriggerSectorFloorHeight(string TriggerSectorName)
    Devuelve la altura del suelo asociada al trigersector TriggerSectorName."""
    ...


def GetTriggerSectorFunc(trigger_sector_name: str, func_type: str) -> __t.Callable:
    """GetTriggerSectorFunc(string TriggerSectorName,string FuncType)
    Devuelve la funcion asociada al evento FuncType del triggersector TriggerSectorName.
    """
    ...


def GetTriggerSectorGroup(trigger_sector_name: str) -> str:
    """GetTriggerSectorGroup(string TriggerSectorName)
    Devuelve el grupo asociado al trigersector TriggerSectorName."""
    ...


def GetTriggerSectorName(index: int) -> str:
    """string GetTriggerSectorName(int idx)
    Devuelve el triggersector de índice idx, None si no existe."""
    ...


def GetTriggerSectorPoints(trigger_sector_name: str) -> list:
    """GetTriggerSectorPoints(string TriggerSectorName)
    Devuelve los puntos asociados al trigersector TriggerSectorName."""
    ...


def GetTriggerSectorRoofHeight(trigger_sector_name: str) -> int:
    """GetTriggerSectorRoofHeight(string TriggerSectorName)
    Devuelve la altura del techo asociada al trigersector TriggerSectorName."""
    ...


def GetWeaponCombos(person_name: str, weapon_kind: str) -> list:
    """tuple GetWeaponCombos(blah blah BLAH!)"""
    ...


def GetWindowId() -> int:
    """int GetWindowId()
    Devuelve identificador de la ventana de la aplicación.
    (HWND en Windows)"""
    ...


def GetWorldFileName() -> str:
    """string GetWorldFileName()
    Obtiene el nombre del archivo del que se ha cargado el mundo actual."""
    ...


def GetnAfterFrameFuncs() -> int:
    """int GetnAfterFrameFuncs()
    Devuelve el nº de funciones AfterFrame en el sistema."""
    ...


def GetnParticleGType() -> int:
    """int GetnParticleGType(void)
    Devuelve el nº de tipos de partículas."""
    ...


def GetnScheduledFuncs() -> int:
    """int GetnScheduledFuncs(void)
    Devuelve el nº de funciones diferidas."""
    ...


def GetnTimers() -> int:
    """int GetnTimers(void)
    Devuelve el número de timers del sistema."""
    ...


def GiveAnims(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """GiveAnims(race_name). Da las anims de la raza en cuestion"""
    ...


def GoToTime(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetClockTime(float time)
    Establece el tiempo del juego en segundos...."""
    ...


def HeapCheckAllAllocations(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """HeapCheckAllAllocations(integer)
    Sets the Heap Checking to be performed on every allocation.  Functions only in debug.
    """
    ...


def HeapCheckDelayFree(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """HeapCheckDelayFree(integer)
    Simulates low memory conditions by delaying freeing until program termination.  Functions only in debug.
    """
    ...


def HeapCheckLeaks(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """HeapCheckSystemMemory(integer)
    Enables leak checking on program termination.  Functions only in debug."""
    ...


def HeapCheckSetMark(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """HeapCheckSetMark()
    Sets a memory checkpoint.  Reterns current bytes allocated. Only working in DEBUG"""
    ...


def HeapCheckSystemMemory(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """HeapCheckSystemMemory(integer)
    Includes memory used in runtime libraries for checking.  Functions only in debug."""
    ...


def Input(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """Input(string texto)
    Crea una ventana de introducción de datos."""
    ...


def InsideActionArea(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """InsideActionArea(int AA,double x,double y,double z)
    ....blah blah !"""
    ...


def KillMusic(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """KillMusic ()
    Guess...;) .n"""
    ...


def LoadAnmRaceData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool LoadAnmRaceData(string filename,string race)
    Carga las animaciones de la raza en el archivo filename."""
    ...


def LoadAnmSoundData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool LoadAnmSoundData(string filename,string race)
    Carga la información de sonido de las animaciones de la raza en el archivo filename.
    """
    ...


def LoadCombustionData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool LoadCombustionData(string filename)
    Carga los datos de los combustion data del archivo filename."""
    ...


def LoadEntitiesData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool LoadEntitiesData(string filename)
    Carga los datos de las entidades del archivo filename."""
    ...


def LoadLevel(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """LoadLevel(string dir_name)
    Lee de disco el nivel en el directorio dir_name."""
    ...


def LoadMusicState(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """loadMusicState(filename)"""
    ...


def LoadParticleSystemsData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool LoadParticleSystemsData(string filename)
    Carga los datos de los sistemas de partículas del archivo filename."""
    ...


def LoadSampledAnimation(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """LoadSampledAnm(str File,str InternalName,int Type)"""
    ...


def LoadSoundDataBase(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """loadSoundDataBase(filename)"""
    ...


def LoadWorld(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """LoadWorld(string filename)
    Lee de disco el mapa (.bw) de nombre filename."""
    ...


def OpenDebugChannel(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool OpenDebugChannel(string channel_name)
    Abre el canal de depuración de nombre channel_name."""
    ...


def OpenProfileSection(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool OpenProfileSection(int section[,string comment])
    Tiene que estar activado el profiler interno.
    Abre la sección i."""
    ...


def PauseSoundSystem(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """PauseSoundSystem ()
    Guess...;) .n"""
    ...


def PauseSoundSystemButMusic(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """PauseSoundSystemButMusic ()
    Idem than pauseSoundSystem BUt with muzic ."""
    ...


def PerformHeapCheck(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """PerformHeapCheck()
    Performs an integrity check on the heap now.  Integrity assertion only working in DEBUG
    """
    ...


def PlaySound(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """PlaySound(int i,double x,double y,double z)
    Reproduce el sonido i en la posición (x,y,z)."""
    ...


def Quit(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool Quit()
    Termina el programa."""
    ...


def ReadAlphaBitMap(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """ReadAlphaBitMap(string file_name,string internal_name)
    Lee de disco una textura alpha."""
    ...


def ReadBitMap(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """ReadBitMap(string file_name,string internal_name)
    Lee de disco una textura."""
    ...


def ReadLevel(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """ReadLevel(string filename)
    Lee de disco el nivel (.lvl) filename."""
    ...


def ReassignCombustionData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool ReassignCombustionData(void)
    Reasigna los datos de los combustion data del archivo filename."""
    ...


def RemoveAfterFrameFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """GetAfterFrameFunc(name)
    Devuelve la función AfterFrame del sistema de nombre name."""
    ...


def RemoveBipedAction(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def RemoveBoundFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """RemoveBoundFunc(string key,proc)
     Quita el procedimiento pr del suceso key.
    RemoveBoundFunc(string key,string predproc)
     Quita el procedimiento predefinifo predproc  del suceso key.
     predproc puede ser: Forward, Backwards, Up, Down, Left, Right, RotateLeft, RotateRight, RotateUp, RotateDown (más, preguntar a Jose)
    """
    ...


def RemoveInputAction(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """RemoveInputAction(string action_name)
    Quita una acción existente."""
    ...


def RemoveScheduledFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """RemoveScheduledFunc(atring FuncName)
    Removes a previously named sceduled function.  Removes first func found with this name.
    """
    ...


def RemoveTriggerSectorFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """RemoveTriggerSectorFunc(string TriggerSectorName,string FuncType)
    Desvincula la funcion asociada al evento FuncType del triggersector TriggerSectorName.
    """
    ...


def RestartTime(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """RestartTime(void)
    Reinicia el tiempo del juego."""
    ...


def ResumeSoundSystem(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """ResumeSoundSystem ()
    Guess...;) .n"""
    ...


def SaveAnmRaceData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SaveAnmRaceData(string filename,string race)
    Guarda las animaciones de la raza race en el archivo filename."""
    ...


def SaveAnmSoundData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SaveAnmSoundData(string filename,string race)
    Guarda información de sonido de las animaciones de la raza race en el archivo filename.
    """
    ...


def SaveCombustionData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SaveCombustionData(string filename)
    Guarda los datos de los combustion  data en el archivo filename."""
    ...


def SaveEntitiesData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SaveEntitiesData(string filename)
    Guarda los datos de las entidades en el archivo filename."""
    ...


def SaveMusicState(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """saveMusicState(filename)"""
    ...


def SaveParticleSystemsData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SaveParticleSystemsData(string filename)
    Guarda los datos de los sistemas de partículas en el archivo filename."""
    ...


def SaveProfileData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SaveProfileData(string filename)
    Tiene que estar activado el profiler interno.
    Guarda información de los tiempos de las secciones activas en el archivo filename.
    """
    ...


def SaveSSConfig(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """Undoc"""
    ...


def SaveScreenShot(file_name: str, width: int, height: int) -> __t.Literal[1]:
    """SaveScreenShot(filename,width,height)
    Acaso necesita descripcion?"""
    ...


def SaveSoundDataBase(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """saveSoundDataBase(filename)"""
    ...


def SaveStats(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """Save statistics"""
    ...


def SetActionCameraMovement(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetActionCameraMovement(char* action_name,double angle,double start_pos,double end_pos)
    Interpolates the camera in the given action , the given angle in the given gap"""
    ...


def SetActionEventTable(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def SetAecGap(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetAutoEngageCombat(double aec_gap)
    Establece tiempo auto encaramiento."""
    ...


def SetAfterFrameFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetAfterFrameFunc(name,function)
    Sets a function referenced with name that is going to be called at the end of each frame.
    """
    ...


def SetAnimationFactor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetAnimationFactor(string mov , float new_speed_factor )
    Cambia la velocidad del movimiento dado ."""
    ...


def SetAppMode(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetAppMode(string mode)
    Establece el modo de la aplicación (Game, Menu,...)."""
    ...


def SetAutoEngageCombat(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetAutoEngageCombat(bool auto)
    Establece si se encara automaticamente los enemigos."""
    ...


def SetAutoGenTexture(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetAutoGenTexture (string TexturName , integer TextEfecct )
    A la texture con dicho nombre se le aplica el efecto dado ."""
    ...


def SetBloodLevel(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetBloodLevel(int level)
    Establece el nivel de sangre."""
    ...


def SetCallCheck(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetCallCheck(int check)
     Activa/desactiva la comprobación de errores de Python en las llamadas que hace Blade.
    Devuelve el estado anterior"""
    ...


def SetCombos(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetCombos(tuple combos)"""
    ...


def SetCurrentMap(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetCurrentMap(string dir_map)
    Establece el directorio de mapa actual."""
    ...


def SetDefaultMass(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetDefaultMass(string entity_kind,double mass)
    Establece la masa mass predefinida para las nuevas entidades de tipo kind."""
    ...


def SetDefaultMaterial(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetDefaultMaterial(string entity_kind,double material)
    Establece el material predefinido para las nuevas entidades de tipo kind."""
    ...


def SetDrawObjectShadows(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetDrawObjectShadows(bool draw)
    Establece si se deben dibujar las sombras de los objetos/personajes."""
    ...


def SetEAX(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetEAX(integer eax_flag)
    Establece la distorsion eax indicada."""
    ...


def SetEAXOverride(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetEAXOverride(0/1)"""
    ...


def SetEventTableFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def SetEventTableFuncC(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def SetGhostSectorGroupSound(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetGhostSectorGroupSound(string GroupName,string filename,double Volume,double BaseVolume,double MinDist,double MaxDist,double Scale)
    Establece el sonido del archivo filename al grupo de sectores fantasma GhostName."""
    ...


def SetGhostSectorSound(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetGhostSectorSound(string GhostName,string filename,double Volume,double BaseVolume,double MinDist,double MaxDist,double vMaxDist,double Scale)
    Establece el sonido del archivo filename al sector fantasma GhostName."""
    ...


def SetInputMode(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetInputMode(string device,string mode)
    Establece el modo del dispositivo device."""
    ...


def SetListenerPosition(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetListenerPosition(int modo[,double x,double y,double z])
    Cambia posicion o modo del oyente.
    mode : 0 - Punto en el mapa
           1 - Personaje
           2 - Cámara"""
    ...


def SetMenuTgapFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetMenuTgapFunc(function)
    Sets a function blah blah blah..."""
    ...


def SetMouseState(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetMouseState(invert,xsens,ysens)"""
    ...


def SetMusicVolume(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetMusicVolume (float factor)
    Guess...;) .n"""
    ...


def SetMutilationLevel(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetMutilationLevel(int level)
    Establece el nivel de mutilaciones."""
    ...


def SetParticleGVal(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def SetRootWidget(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetRootWidget(widget w)
    Establece el Widget raiz."""
    ...


def SetRunString(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """void SetRunString(string variable)
    Ejecuta la cadena de caracteres variable."""
    ...


def SetSS2dChannels(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetSS2dChannels (int num_ch)
    Tells the sound system the number of 2d channels ."""
    ...


def SetSS3dChannels(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetSS3dChannels (int num_ch)
    Tells the sound system the number of 3d channels ."""
    ...


def SetSSFilter(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetSSFilter (bool)
    Tells the sound system to filter the output or not ."""
    ...


def SetSSFrecuency(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetSSFrecuency (int frec)
    Tells the sound system the base frecuency to use ."""
    ...


def SetSSQuality(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """Undoc(0-2)"""
    ...


def SetSaveInfo(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """int SetSaveInfo(tuple info)
    Establece información de estado."""
    ...


def SetSolidMask(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def SetSoundVolume(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetSoundVolume(double Volume)
    Establece el volumen del sistema de sonido."""
    ...


def SetSpeakerConfig(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """Undoc(0-3)"""
    ...


def SetStringValue(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetStringValue(string variable,string value)
    Guarda la cadena de caracteres value cobn el nombre variable."""
    ...


def SetSun(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetSun(int exists,double x,double y,double z)
    Establece la posicion del sol mediante la direccion de la luz exterior. exists indica si se dibuja (1) o no (0)
    """
    ...


def SetTime(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool SetTime(float time)
    Establece el tiempo del juego en segundos."""
    ...


def SetTimeSpeed(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """GetTimeSpeed(void)
    Devuelve la velocidad tiempo del juego."""
    ...


def SetTriggerSectorData(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetTriggerSectorData(string TriggerSectorName,Data)
    Asigna el objeto Python Data al campo Data del triggersector TriggerSectorName."""
    ...


def SetTriggerSectorFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetTriggerSectorFunc(string TriggerSectorName,string FuncType,Func)
    Asigna la funcion Func al evento FuncType del triggersector TriggerSectorName."""
    ...


def SetTurnSpeed(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SetTurnSpeed(string name_raza,float new_speed )
    Cambia la velocidad de giro de una raza . En radianes."""
    ...


def ShowActionAreas(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def ShowSounds(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """ShowSounds(int sh)
    Establece si se debe mostrar un objeto para indicar donde estan los sonido ambiente.
    """
    ...


def ShutDownSoundChannels(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """ShutDownSoundChannels ()
    Guess...;) .n"""
    ...


def SoundSystemActive(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """SoundSystemActive ()
    Tells if the sound system if active or not ."""
    ...


def StartProfile(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """bool StartProfile(void)
    Tiene que estar activado el profiler interno.
    Reinicia sesión."""
    ...


def StopTime(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """StopTime(void)
    Detiene el tiempo del juego."""
    ...


def TakeSnapShot(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """Takes a snapshot"""
    ...


def UnBindAll(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """UnBindAll()
    Borra la configuración de teclado."""
    ...


def WriteText(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """"""
    ...


def YSSInfo(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """YSSInfo()"""
    ...


def nEntities() -> int:
    """int nEntities(void)
    Devuelve el nº de entidades en el mapa."""
    ...


def nMaterials() -> int:
    """nMaterials(void)
    Devuelve el nº de materiales."""
    ...


def nSectors() -> int:
    """int nEntities(void)
    Devuelve el nº de sectors en el mapa."""
    ...


def nSounds() -> int:
    """int nSounds(void)
    Devuelve el nº de sonidos en el mapa."""
    ...


def nTriggerSectors() -> int:
    """int nTriggerSectors(void)
    Desvincula el número de triggersectors en el mapa."""
    ...


#########
# reissue


def ApplyVideoSettings(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool ApplyVideoSettings()
    Apply changed video settings"""
    ...


def FakeInputAction(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    FakeInput(string action_name)"""
    ...


def GetActiveControllerType(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    GetActiveControllerType()"""
    ...


def GetActiveMonitor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int GetActiveMonitor()
    Get active monitor"""
    ...


def GetAntialiasing(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetAntialiasing()
     Get antialiasing"""
    ...


def GetAspectRatio(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int GetAspectRatio()
    Get aspect ratio"""
    ...


def GetFieldOfView(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetFieldOfView()
     Get field of view"""
    ...


def GetHideUI(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetHideUI()
     Get Hide UI"""
    ...


def GetLastUsedController(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    GetLastUsedController()"""
    ...


def GetLimitFps(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*"""
    ...


def GetNumMonitor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int GetNumMonitor()
    Get number of available monitor"""
    ...


def GetPlayIntro(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetPlayIntro()
    Devuelve true si se encara automaticanmente si se puede."""
    ...


def GetResolution(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    string GetResolution()
    Get window resolution"""
    ...


def GetReworkedCamera(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetReworkedCamera()
    Use a new non stuttering camera"""
    ...


def GetScreenMode(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int GetScreenMode()
    Get if window is in fullscreen mode"""
    ...


def GetSubtitlesEnable(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetSubtitlesEnable()
     Get usability of subtitles"""
    ...


def GetSupportedResolution(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetSupportedResolution()
    Get all supported window resolution"""
    ...


def GetUIScaleFactor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int GetUIScaleFactor()
     Get UI Scale Factor"""
    ...


def GetUpperCaseRussian(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    GetUpperCaseRussian(string word)"""
    ...


def GetVerticalSync(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetVerticalSync()
    get vertical sync"""
    ...


def GetVibration(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool GetVibration()
    get vibration"""
    ...


def IsRunningOnHandheldDevice(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    IsRunningOnHandheldDevice()
    Returns true if running on a handheld device."""
    ...


def IsUseMsgActive(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool IsUseMsgActive()
    Is Use active this frame"""
    ...


def PlayHaptic(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    PlayHaptic(hapticValue)"""
    ...


def SetActiveMonitor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int SetActiveMonitor(int active_monitor)
    Set active monitor"""
    ...


def SetAntialiasing(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetAntialiasing(bool antialiasing)
     Set antialiasing"""
    ...


def SetAspectRatio(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int SetAspectRatio(char* aspect_ratio)
    set aspect ratio"""
    ...


def SetFieldOfView(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetFieldOfView(float field_of_view)
     Set field of view"""
    ...


def SetGamepadChangeFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetGamepadChangeFunc(controllerType,function)"""
    ...


def SetGamepadDisconnectFunc(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetGamepadDisconnectFunc(isDisconnect,function)"""
    ...


def SetHideUI(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetHideUI(float field_of_view)
     Hide UI"""
    ...


def SetLimitFps(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*"""
    ...


def SetMessageWidget(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetMessageWidget(widget w)
     Establece el Widget raiz."""
    ...


def SetPlayIntro(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool SetPlayIntro(bool auto)
    Establece si se encara automaticamente los enemigos."""
    ...


def SetResolution(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool SetResolution(int width, int height)
    Set screen resolution"""
    ...


def SetReworkedCamera(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool SetReworkedCamera(bool reworked)
    Set reworked camera"""
    ...


def SetScreenMode(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool SetScreenMode(bool windowed)
    Set screen mode"""
    ...


def SetSubtitlesEnable(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetSubtitlesEnable(bool subtitles_enable)
     Set usability of subtitles"""
    ...


def SetUIScaleFactor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    SetUIScaleFactor(int v)
     Set UI Scale Factor"""
    ...


def SetVerticalSync(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    int SetVerticalSync()
    Set vertical sync"""
    ...


def SetVibration(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool SetVibration(bool reworked)
    Set vibration"""
    ...


def ShowCriticalWarning(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    ShowCriticalWarning(string title,string msg)"""
    ...


def TriggerEvent(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    TriggerEvent(string event_name)
    Pass the index of the achievement to be activated."""
    ...


def TriggerEventInner(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    TriggerEventInner()
    Tries to unlock complete game as (id=50..53)."""
    ...


def TurnAround(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*
    bool TurnAround()
    Turn around"""
    ...
