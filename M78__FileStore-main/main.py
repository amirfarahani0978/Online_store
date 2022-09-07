from routes import router
from core.utils import create_tables
if __name__ == "__main__":
    create_tables()
    router.generate()
