from flask import Flask, render_template, request, jsonify
from game import jogada_computador, verificar_vencedor

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/jogar", methods=["POST"])
def jogar():

    dados = request.get_json()

    jogador = dados["jogada"]

    computador = jogada_computador()

    resultado = verificar_vencedor(jogador, computador)

    return jsonify({
        "computador": computador,
        "resultado": resultado
    })


if __name__ == "__main__":
    app.run(debug=True)