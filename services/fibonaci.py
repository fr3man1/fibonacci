import flask
import decimal
import operator

app = flask.Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def decimal_range(start, stop, step=1):
    """Provides an alternative to `xrange` for very high numbers."""
    proceed = operator.lt
    while proceed(start, stop):
        yield start
        start += step


def fibonacci(n):
    """
    Computes Fibonacci numbers using decimal.Decimal for high
    precision and without recursion
    """
    a, b = decimal.Decimal(0), decimal.Decimal(1)
    for i in decimal_range(0, n):
        a, b = b, a + b
    return a


def fib_array(length):
    fib_list = []
    fib_array = (range(length))
    for nth in fib_array:
        fib_list.append(int(fibonacci(nth)))
    return fib_list


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/fib/<nth>", methods=['GET'])
def fib(nth):
    try:
        if int(nth) >= 0:
            return str(fib_array(int(nth)))
        elif int(nth) < 0:
            raise InvalidUsage('Invalid usage, number cannot be negative', status_code=400)
    except ValueError:
        raise InvalidUsage('Invalid usage', status_code=400)


if __name__ == "__main__":
    app.run(port=5005, debug=False)
