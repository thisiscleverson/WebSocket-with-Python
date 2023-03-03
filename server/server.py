import logging
from websocket_server import WebsocketServer
##################
import json
import os

host ="localhost"
port = 8765
data = []

'''
def handle(client, server):
    #message = client.set_fn_message_received()
    server.send_message_to_all('Hello, welcome to user test websocket!')
'''

def messageReceived(client, server, message):
    def issertNewData(user, point):
        data.append({
            "user": user,
            "point": point
        }) # salvar os novos dados em uma variavel

    def updateDataUsers(data):
        '''
        o for vai pecorre todo o array 
        e verifica se já tem algum usu-
        ário registrado. Se sim, ele a-
        tualiza os pontos do usuário, se
        não ele registra um novo user.
        '''
        for i in range(0, len(data)):
            if data[i]['user'] == recvData['user']:
                data[i]['point'] = recvData['point']
                return True 
        return False

    print(f'message: {message}')
    recvData = json.loads(message) # converter a string para json

    if len(data) == 0:
        issertNewData(recvData['user'], recvData['point'])
    else:
        wasUpdate = updateDataUsers(data=data)
        if wasUpdate == False:
            issertNewData(recvData['user'], recvData['point'])
     
    print(data)
    server.send_message_to_all(json.dumps(data))


if __name__ == "__main__":
    print("start server ...")
    os.system(f'npx kill-port {port}')
    os.system('clear')

    server = WebsocketServer(host=host, port=port, loglevel=logging.INFO)
    #server.set_fn_new_client(handle)
    server.set_fn_message_received(messageReceived)
    server.run_forever()

    print(f'SERVER: "ws://{host}:{port}/"')
    print('------------------------------')
