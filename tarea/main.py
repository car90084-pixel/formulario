from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def inicio():

    return """
    <h2>Inicio de sesión</h2>

    <form action="/login" method="post">

        Usuario:
        <input type="text" name="usuario"><br><br>

        Contraseña:
        <input type="password" name="contrasena"><br><br>

        <button type="submit">Ingresar</button>

    </form>
    """

@app.post("/login")
def login(usuario: str = Form(...), contrasena: str = Form(...)):

   
    if contrasena == "1234":

        return HTMLResponse(f"""
        <h1>Bienvenido {usuario}</h1>
        """)

    return RedirectResponse(url="/", status_code=302)