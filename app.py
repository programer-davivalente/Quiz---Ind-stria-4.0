from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/verificar', methods=['POST'])
def verificar():

    pontos = 0
    erros_lista = []

    respostas = {
        "PERGUNTA1": "A conexão digital entre máquinas e sistemas",
        "PERGUNTA2": "Conexão de objetos físicos à internet",
        "PERGUNTA3": "Analisar grandes volumes de informações",
        "PERGUNTA4": "Armazenar e acessar dados pela internet",
        "PERGUNTA5": "Manufatura Aditiva",
        "PERGUNTA6": "Ele trabalha em parceria com seres humanos",
        "PERGUNTA7": "Para proteger a fábrica de ataques de hackers",
        "PERGUNTA8": "Aumentar a eficiência e reduzir desperdícios"
    }

    for pergunta, resposta_correta in respostas.items():

        resposta_usuario = request.form.get(pergunta)

        if resposta_usuario == resposta_correta:
            pontos += 1

        else:
            erros_lista.append({
                "numero": pergunta.replace("PERGUNTA", ""),
                "resposta_usuario": resposta_usuario or "Não respondeu",
                "resposta_correta": resposta_correta
            })

    erros = len(respostas) - pontos

    if pontos == 8:
        mensagem = "🏆 Parabéns! Você acertou todas as perguntas! Excelente desempenho!"
    elif pontos >= 6:
        mensagem = "👏 Muito bom! Você conhece bastante sobre a Indústria 4.0."
    elif pontos >= 4:
        mensagem = "🙂 Bom trabalho! Você já sabe bastante, mas ainda pode melhorar."
    elif pontos >= 2:
        mensagem = "📚 Continue estudando. Você está no caminho certo!"
    else:
        mensagem = "💡 Não desanime! Revise o conteúdo e tente novamente."

    return render_template(
        "resultado.html",
        pontos=pontos,
        erros=erros,
        mensagem=mensagem,
        erros_lista=erros_lista
    )


if __name__ == '__main__':
    app.run(debug=True)