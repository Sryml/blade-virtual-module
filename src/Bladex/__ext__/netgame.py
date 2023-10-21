# Module 'netgame'
from __future__ import annotations

import Bladex.__sub__.b_types as __bt


def AddPosition(*args: __bt.todo) -> __bt.todo:
    """AddPosition(x,y,z)
    Agrega una posicion nueva a la lista."""
    ...


def AddSoundToClient(*args: __bt.todo) -> __bt.todo:
    """AddSoundToClient(EntityName,AnimationName,SoundObject)
    Para el cliente:
       Agrega un sonido a los eventos del cliente."""
    ...


def Bind(*args: __bt.todo) -> __bt.todo:
    """Bind('accion',funcion,SeIgnoraEnHost)
      La funcion debe recibir un parametro, el nombre de jugador.
      SeIgnoraEnHost implica que solo se ejecutara la operacion de
    los clientes, el funcionamiento local no sera modificado ."""
    ...


def BrowseSessions(*args: __bt.todo) -> __bt.todo:
    """BrowseSessions([direccion IP])
    Busca en una direccion IP especifica. Si se omite busca en la red IPX"""
    ...


def CallEventSound(*args: __bt.todo) -> __bt.todo:
    """CallEventSound(entityname,id)
    Sevidor indica un sonido a los clientes"""
    ...


def ChangeAnmSoundIndex(*args: __bt.todo) -> __bt.todo:
    """ChangeAnmSoundIndex(PersonName,Index)
       Cambia el indice del de la animacion del sonido que se enviara por red
    (*)Este valor suele usarse solo para servidor dedicado."""
    ...


def ClearPools(*args: __bt.todo) -> __bt.todo:
    """ClearPools()
    Para todos:
       Limpia la sangre"""
    ...


def CreateMainPlayer(*args: __bt.todo) -> __bt.todo:
    """CreateMainPlayer()
    Crea el jugador principal si es cliente o servidor
    Se llama 'Player1' y esta funcion se llama solo una vez
    Retorna verdadero si se creo con exito
    Usese como un bucle while(not)"""
    ...


def GetBrowseResult(*args: __bt.todo) -> __bt.todo:
    """GetBrowseResult(indice del servidor)
    retorna (nombre,jugadores,maximo) o None"""
    ...


def GetClientId(*args: __bt.todo) -> __bt.todo:
    """GetClientId()
    Solo para clientes:
       obtiene el nombre de su entidad en el servidor"""
    ...


def GetLocalOptions(*args: __bt.todo) -> __bt.todo:
    """GetLocalOptions()
    Retorna (nombre,raza,arma,escudo) elegidos para la red"""
    ...


def GetNetState(*args: __bt.todo) -> __bt.todo:
    """GetNetState()
    Retorna
                  0 : SinglePlayer
         1 : Server
         2 : Client"""
    ...


def GetNextPosition(*args: __bt.todo) -> __bt.todo:
    """GetNextPosition()
    Retorna la posicion proxima en la lista de salidas"""
    ...


def GetPlayerData(*args: __bt.todo) -> __bt.todo:
    """GetPlayerData(entityname)
    Retorna
                  (energy,life)"""
    ...


def GetTime(*args: __bt.todo) -> __bt.todo:
    """GetTime()
    Obtiene el estado del tiempo de red
    Si es cliente, obtiene el tiempo del servidor
    Si es servidor, obtiene el tiempo actual"""
    ...


def IsDedicated(*args: __bt.todo) -> __bt.todo:
    """IsDedicated()
    Devuelve verdadero si el servidor arrancara como dedicado."""
    ...


def IsValidProtocol(*args: __bt.todo) -> __bt.todo:
    """IsValidProtocol(TCP)
    Devuelve verdadero si un protocolo esta disponible.
    0 : Para IPX/SPX
    1 : Para TCP/IP"""
    ...


def JoinSession(*args: __bt.todo) -> __bt.todo:
    """JoinSession(indice del servidor,nombre del jugador)"""
    ...


def RestartNet(*args: __bt.todo) -> __bt.todo:
    """RestartNet()
    Reinicia la red en offline"""
    ...


def SendUnguaranteedUserString(*args: __bt.todo) -> __bt.todo:
    """SendUnguaranteedUserString(int,string)
    Envia una cadena:    - Al servidor si cliente
      - A todos si servidor
    Los valores que se envian, son el tipo de cadena y
     la cadena en cuestion"""
    ...


def SendUserString(*args: __bt.todo) -> __bt.todo:
    """SendUserString(int,string)
    Envia una cadena:    - Al servidor si cliente
      - A todos si servidor
    Los valores que se envian, son el tipo de cadena y
     la cadena en cuestion"""
    ...


def ServerChangeLevel(*args: __bt.todo) -> __bt.todo:
    """ServerChangeLevel(LevelName)
    Cambia de nivel si es servidor"""
    ...


def ServerInfoBlock(*args: __bt.todo) -> __bt.todo:
    """ServerInfoBlock()
    Retorna estadisticas de la red para el servidor"""
    ...


def SetByePlayerFunc(*args: __bt.todo) -> __bt.todo:
    """SetByePlayerFunc(func)
    Activa la funcion Callback de desconeccion de usuario
    la funcion recibe un entero y una cadena :
      I- Identificador del jugador
      S- Identificador del jugador"""
    ...


def SetClientDamageFunc(*args: __bt.todo) -> __bt.todo:
    """SetClientDamageFunc(func)
    Activa la funcion Callback de daño del cliente
    la funcion recibe una cadena :
      S- Identificador del jugador"""
    ...


def SetDedicated(*args: __bt.todo) -> __bt.todo:
    """SetDedicated(ds)
    Activa/desactiva el flag de servidor dedicado."""
    ...


def SetJoinPlayerFunc(*args: __bt.todo) -> __bt.todo:
    """SetJoinPlayerFunc(func)
    Activa la funcion Callback de creacion de objetos personaje
    la funcion recibe un entero y cinco cadenas :
      I- Identificador del jugador
      S- Nombre de la entidad
      S- Nombre del jugador
      S- Tipo de raza
      S- Arma deseada
      S- escudo deseado
    Cuando esta funcion es llamada ya esta creado el personaje
    Mas no sus armas
    En el caso del cliente, la funcion llamada solo tiene : ('Nombre de la entidad','raza')
    """
    ...


def SetLocalOptions(*args: __bt.todo) -> __bt.todo:
    """SetLocalOptions(name,kind,weapon,shield,map)"""
    ...


def SetMutilaFunc(*args: __bt.todo) -> __bt.todo:
    """SetMutilaFunc(func)
    Activa la funcion Callback de mutilaciones del cliente
    la funcion recibe:
      S    - Identificador del jugador
      S    - Identificador del miembro mutilado
      X,Y,Z- Posicion
      X,Y,Z- Velocidad
      I    - Identificador del nodo mutilado"""
    ...


def SetObjectState(*args: __bt.todo) -> __bt.todo:
    """SetObjectState('entidad',Enviar)
    Activa y desactiva el trafico de la red para una entidad determinada."""
    ...


def SetPPS(*args: __bt.todo) -> __bt.todo:
    """SetPPS(i)
    Cambia el numero de paquetes por segundo
    Los valores validos van de 1 a 60
    0 es para que se procese una vez por frame"""
    ...


def SetPersonView(*args: __bt.todo) -> __bt.todo:
    """SetPersonView(entityname)
    Hace que la camara apunte a alguna entidad de red"""
    ...


def SetServerState(*args: __bt.todo) -> __bt.todo:
    """SetServerState(boolean)
    Si envia el valor 1, el servidor pondra a los objetos que se creen, en la red
    En caso contrario, no lo pondra como objetos de red"""
    ...


def SetSoundFunc(*args: __bt.todo) -> __bt.todo:
    """SetSoundFunc(func)
    Activa la funcion Callback de sonidos del cliente
    la funcion recibe:
      S    - Identificador del objeto
      i    - Identificador del miembro mutilado"""
    ...


def SetStringUserFunc(*args: __bt.todo) -> __bt.todo:
    """SetStringUserFunc(func)
    Activa la funcion Callback de recepcion de cadenas de usuario
    la funcion recibe dos enteros y una cadena :
      I- Identificador del jugador    I- Tipo de cadena    S- Cadena de caracteres"""
    ...


def StartServer(*args: __bt.todo) -> __bt.todo:
    """StartServer(GameName,PlayerName,MaxPlayers,TCP)
    Inicia los protocolos del el servidor"""
    ...
