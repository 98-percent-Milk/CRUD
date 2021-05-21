from flask import Flask, Blueprint, render_template, session, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

fc = Blueprint('fc', __name__, url_prefix='/fc', template_folder='../templates/')
db = SQLAlchemy()


class flash_card(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    term = db.Column('term', db.String(50))
    definition = db.Column('def', db.String(50))

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


@fc.route('/', methods=['GET', 'POST'])
def fc_index():
    return render_template('index.html')


@fc.route('/add', methods=['GET', 'POST'])
def add_flashcard():
    if request.method == 'POST':
        session.permanent = True
        fc_term = request.form['term']
        fc_def = request.form['definition']

        found_fc = flash_card.query.filter_by(term=fc_term).first()
        if found_fc: #when flashcard already exists in the database
            flash(f"Flashcard:<{fc_term}> already exists here in the database")
            return render_template('single_flashcard.html', card=found_fc)
        elif fc_term == "":
            flash("Please enter a Term")
            return render_template("create.html")
        elif fc_def == "":
            flash("Please enter a Definition")
            return render_template("create.html")
        else: # when flashcard doesn't exist in the database
            new_flashcard = flash_card(fc_term, fc_def)
            db.session.add(new_flashcard)
            db.session.commit()
            flash("Successfully added a new flashcard")
        return redirect(url_for('fc.fc_index'))
    else:
        return render_template("create.html")


@fc.route("/view")
def view():
    return render_template('flashcards.html', flashcards=flash_card.query.all())


@fc.route('/remove', methods=['GET', 'POST'])
def pop_fc():
    session.pop('flashcard', None)
    return redirect(url_for('fc.add_flashcard'))


@fc.route('/delete/<int:fc_id>', methods=['GET', 'POST'])
def delete(fc_id: int):
    if request.method == 'POST':
        found_fc = flash_card.query.filter_by(id=fc_id).delete()
        db.session.commit()
        return redirect(url_for('fc.view'))
    else:
        return redirect(url_for('fc.view'))


@fc.route('/update/<int:fc_id>', methods=['GET', 'POST'])
def update(fc_id: int):
    if request.method == 'POST':
        found_fc = flash_card.query.filter_by(id=fc_id).first()
        found_fc.term = request.form['term']
        found_fc.definition = request.form['definition']
        db.session.commit()
        return redirect(url_for('fc.view'))
    else:
        return redirect(url_for('fc.view'))


@fc.route('/edit/<int:fc_id>', methods=['GET', 'POST'])
def edit(fc_id:int):
    if request.method == 'POST':
        found_fc = flash_card.query.filter_by(id=fc_id).first()
        return render_template('single_flashcard.html', card=found_fc)
    else:
        redirect(url_for('fc.index'))

@fc.route('/practice', methods=['GET', 'POST'])
def practice():
    fc_terms = flash_card.query.with_entities(flash_card.term).all()
    fc_definition = flash_card.query.with_entities(flash_card.definition).all()
    terms = [x[0] for x in fc_terms]
    definition = [x[0] for x in fc_definition]
    return render_template('practice.html', flashcards = terms, fc_def=definition)

@fc.route("/cancel", methods=['POST'])
def cancel():
    return redirect(url_for('fc.view'))