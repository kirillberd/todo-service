from sqlmodel import Session
from sqlalchemy import Engine
import logging

module_logger = logging.getLogger(__name__)

class PostgresContextProvider:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._sessinon = None

    def __enter__(self):
        try:
            self._sessinon = Session(self._engine)
            return self._sessinon
        except:
            return None
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            if exc_type:
                module_logger.error(exc_type)
                self._session.rollback()
            else:
                self._session.commit()
            self._session.close()
        return True
        