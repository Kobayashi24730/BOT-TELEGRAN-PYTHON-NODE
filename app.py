from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# ===============================
# BANCO SIMULADO DE HORÁRIOS
# ===============================

availability_db: Dict[str, List[str]] = {
    "2026-02-01": ["10:00", "12:00", "15:00"],
    "2026-02-02": ["09:00", "11:00", "18:00"],
    "2026-02-03": ["08:00", "14:00", "20:00"],
    "2026-02-04": ["07:00", "13:00", "19:00"],
}

# ===============================
# MODELOS
# ===============================

class BookingRequest(BaseModel):
    playerId: str
    date: str
    hour: str


# ===============================
# ENDPOINT 1: CONSULTAR HORÁRIOS
# ===============================

@app.get("/availability")
def get_availability(date: str):
    """
    Retorna horários disponíveis para uma data.
    Exemplo:
    GET /availability?date=2026-02-01
    """
    hours = availability_db.get(date, [])

    return {
        "date": date,
        "available_hours": hours
    }


# ===============================
# ENDPOINT 2: FAZER RESERVA
# ===============================

@app.post("/book")
def book_hour(req: BookingRequest):
    """
    Reserva um horário se estiver disponível.
    """

    if req.date not in availability_db:
        return {"success": False, "message": "Data inválida"}

    if req.hour not in availability_db[req.date]:
        return {"success": False, "message": "Horário não disponível"}

    # Remove horário da lista (reservado)
    availability_db[req.date].remove(req.hour)

    return {
        "success": True,
        "message": f"Reserva confirmada para {req.date} às {req.hour}",
        "player": req.playerId
    }


# ===============================
# ENDPOINT 3: LISTAR TODAS DATAS
# ===============================

@app.get("/calendar")
def calendar():
    """
    Retorna todas as datas e horários disponíveis.
    """
    return availability_db
