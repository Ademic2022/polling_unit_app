from web_app import create_app, configure_db


app = create_app()
configure_db(app)  # Call the configure_db function

if __name__ == "__main__":
    app.run(port=5001, debug=True)