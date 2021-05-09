from flask import (
    Flask
)
import database.db_session as db_session
import os


def create_app():
    import moduls.home as home_page
    import moduls.blog as blog_page
    import moduls.courses as course_page
    import moduls.parents as parents_pages
    import moduls.auth as auth_page
    from moduls.auth import login_manager

    app = Flask(__name__)
    app.config.from_object('config')

    db_session.global_init("database\\db\\speech_therapist_online.db")
    login_manager.init_app(app)
    app.register_blueprint(home_page.bp)
    app.register_blueprint(blog_page.bp)
    app.register_blueprint(course_page.bp)
    app.register_blueprint(parents_pages.bp)
    app.register_blueprint(auth_page.bp)
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=port)
