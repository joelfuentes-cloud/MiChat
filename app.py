from flask import Flask, request, jsonify, render_template_string
from redis import Redis
import os

app = Flask(__name__)
db = Redis(host=os.getenv("REDIS_HOST"), port=6379, decode_responses=True)

# HTML con estilo de chat
HTML_INTERFACE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mi Chat Docker</title>
    <style>
        body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background: #f0f2f5; }
        #chat-box { width: 400px; height: 500px; border: 1px solid #ccc; background: white; padding: 10px; overflow-y: scroll; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .msg { background: #e1ffc7; padding: 8px; margin: 5px 0; border-radius: 5px; border: 1px solid #dcf8c6; }
        .input-area { margin-top: 10px; display: flex; width: 400px; }
        input { flex-grow: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px 0 0 5px; outline: none; }
        button { padding: 10px; background: #25d366; color: white; border: none; border-radius: 0 5px 5px 0; cursor: pointer; }
    </style>
</head>
<body>
    <h2>Chat en Docker (Linux + Redis)</h2>
    <div id="chat-box"></div>
    <div class="input-area">
        <input type="text" id="mensaje" placeholder="Escribe un mensaje..." onkeypress="if(event.key==='Enter') enviar()">
        <button onclick="enviar()">Enviar</button>
    </div>

    <script>
        function cargarMensajes() {
            fetch('/recibir')
                .then(res => res.json())
                .then(data => {
                    const box = document.getElementById('chat-box');
                    box.innerHTML = data.historial.map(m => `<div class="msg">${m}</div>`).join('');
                    box.scrollTop = box.scrollHeight;
                });
        }

        function enviar() {
            const input = document.getElementById('mensaje');
            fetch('/enviar', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({mensaje: input.value})
            }).then(() => {
                input.value = '';
                cargarMensajes();
            });
        }
        setInterval(cargarMensajes, 2000); // Actualiza cada 2 segundos
        cargarMensajes();
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_INTERFACE)

@app.route("/enviar", methods=["POST"])
def enviar():
    msg = request.json.get("mensaje")
    if msg:
        db.rpush("chat", msg)
    return jsonify({"status": "Guardado"}), 201

@app.route("/recibir", methods=["GET"])
def recibir():
    return jsonify({"historial": db.lrange("chat", 0, -1)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)