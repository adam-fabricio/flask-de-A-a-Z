from app import create_app
from config import app_config, app_active


app = create_app()

if __name__ == "__main__":
    config = app_config[app_active]
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
