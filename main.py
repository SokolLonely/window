import PySimpleGUI as sg
import console
import openai
import subprocess
def askIlon(question):
 openai.api_key = ""#write your OpenAI key hear
 prompt = "Напиши команду для консоли windows " + question + "  Дай только код! Никакого текста и комментариев! Если нет такой команды, напиши error"
 response = openai.Completion.create(engine="text-davinci-002",prompt=prompt,  max_tokens=1024,  n=1,  stop=None,  temperature=0.5, )
 story = response.choices[0].text
 return story
def askConsole(string):
 result = subprocess.run(string.split(), capture_output=True, encoding='cp866')
 return result.stderr + result.stdout
layout = [   [sg.Text('введите ваш запрос'), sg.InputText(),   ],  [sg.Submit(), sg.Cancel()], [sg.Output(size=(60, 10), key='_OUT_')]]
window = sg.Window('Clever Console is a present for sysadmin', layout)
while True:                             # The Event Loop
    event, values = window.read()
    if event == 'Submit':
        converted = askIlon(values[0])
        print(converted)
        if converted != "error":
         print(askConsole(converted))
        else:
         print("I'm sorry. ChatGPT can't understand you")
    if event in (None, 'Exit', 'Cancel'):
        break
