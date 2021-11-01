from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def root():
    return render_template("home.html", words=story.prompts)

@app.route('/story')
def create_madlib():
    ans = {}
    for prompt in story.prompts:
        ans.update({prompt: request.args.get(prompt)})
    return render_template("madlib.html", complete_story = story.generate(ans))