from flask import Flask, jsonify
import subprocess
import shutil
import os

app = Flask(__name__)

# Caminhos importantes
OUTPUT_DIR = "/ig/output"
#APACHE_DIR = "/var/www/html/guia"
APACHE_DIR = "/var/www/html"

@app.route('/atualizar', methods=['GET'])
def atualizar_guia():
    try:
        print("Atualizando o Guia, por favor aguarde...")
        # Executa o script de atualização
        resultado = subprocess.run(["/bin/bash", "/ig/_genonce.sh", "--yes"], capture_output=True, text=True)
        
        # Se a execução foi bem-sucedida, copiar os arquivos para o Apache
        if resultado.returncode == 0:
            # Remove diretório antigo
            if os.path.exists(APACHE_DIR):
                shutil.rmtree(APACHE_DIR)
            
            # Copia os novos arquivos
            shutil.copytree(OUTPUT_DIR, APACHE_DIR)
        
            return jsonify({
                "mensagem": "Atualização concluída com sucesso!",
                "output": resultado.stdout
            }), 200
        else:
            return jsonify({
                "erro": "Falha na execução do _genonce.sh",
                "output": resultado.stderr
            }), 500

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
