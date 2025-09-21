from objects.repositories.poll_repository import poll_repository

def add_poll(poll_data):
    print(poll_data)
    poll_repository.add_poll(poll_data)