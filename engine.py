import logging

from loading import *



def init_logging():
    logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode='w',
                        format="%(asctime)s - %(levelname)s - %(message)s")
    


if __name__=='__main__':
    rooms = loader.rooms
    entities = loader.entities
    init_logging()
    
    logging.info(rooms)
    logging.info(entities)
    #logging.info(f"{rooms[0].info()}\n{rooms[0].entities[2].info()}")
    
    """Check if object is from class (will be importan later)"""
    # if isinstance(entities[0], Entity):
    #     print("pog")

