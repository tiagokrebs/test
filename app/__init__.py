import flask
from . import auth
from . import orders
from . import metrics
from . import logs


def create_app():
    app = flask.Flask(__name__)

    @app.route('/check', methods=['GET'])
    # @auth.login_required
    def index():
        return flask.jsonify({'message': 'OK'})
    
    # register blueprints if needed
    app.register_blueprint(auth.bp)
    app.register_blueprint(orders.bp)

    # extra
    metrics.setup_metrics(app)
    logs.setup_logging(app)

    @app.after_request
    def after_request(response):
        app.logger.info(f"Request to {flask.request.path} completed with status {response.status_code}")
        return response

    return app
