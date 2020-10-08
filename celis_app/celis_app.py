from app import app,db
from app.models import User,thread,post


@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User':User,'thread':thread,'post':post}


if __name__ == '__main__':
    app.run(debug=True)
