import app.service.repository.api_manager as api_manager

URL = 'https://aves.ninjas.cl/api/birds/'
response = {
    "data": None,
    "message": ""
}
data = {}

def get_birds(uid:str = None, cantidad:int = 0):
    url = URL if uid is None else f"{URL}{uid}"
    if uid is not None:
        if len(uid) > 0:
            data = api_manager.get(url)
            return obtener_response(data=data)
        else:
            return obtener_response(data=data, tipo="ERROR", message="El servicio ha tenido un error")
    else:
        data = api_manager.get(url)
        return obtener_response(data[:cantidad] if type(data) == list and cantidad <= len(data) else data)

def obtener_response(data, tipo: str = "OK", message: str = ""):
    response["data"] = data
    response["message"] = f"{tipo}: {message}" if tipo != "OK" else f"{tipo}: Petición exitosa"
    return response