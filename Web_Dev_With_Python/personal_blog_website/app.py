from flask import Flask, render_template

app = Flask(__name__)

# sample blogs posts

posts = [
    {
        'id': 1,
        'title': 'Blog Post 1',
        'content': 'First post content',
        'author': 'Pranay',
        'date_posted': 'April 20, 2025'
    },
    {
        'id': 2,
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'author': 'Pranay',
        'date_posted': 'April 21, 2025'
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return '<h1>Post not found</h1>', 404


if __name__ == '__main__':
    app.run(debug=True)
    