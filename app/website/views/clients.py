from app.system.models.client import Client
from app.system.models.message import Message
from app.system.repositories.messages_repository import MessageRepository,


def createMessage(to: int):
    repositoryMessage = MessageRepository()
    message: Message = repositoryMessage.find(int(to))
    print(message)
    return "Foi"


def showClientsFollow(to: int):
    repositoryMessage = MessageRepository()
    message: Message = repositoryMessage.find(int(to))
    print(message)
    return "Foi"
