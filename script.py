import whisper #importe a biblioteca whisper

modelo = whisper.load_model("tiny") # dando load no modelo tiny do whisper

resposta = modelo.transcribe("Audio1.MP3") # seu áudio aqui

print(resposta)
